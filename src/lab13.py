"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import argparse
import csv
from decimal import Decimal
from pathlib import Path
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs["request_id"].isin(reqs["request_id"])]

    if max_lan_chay is not None:
        runs = runs[runs["attempt"] <= max_lan_chay]
        vuot_gioi_han = reqs["so_lan_chay"] > max_lan_chay
        reqs.loc[vuot_gioi_han, "ket_qua"] = "chuyen_nhan_vien"
        reqs.loc[
            vuot_gioi_han,
            ["phut_xem_lai_simulated", "phut_lam_lai_simulated"],
        ] = 0
    token_moi_lan = (
        runs["tokens_in"] * gia_vao + runs["tokens_out"] * gia_ra
    ) / 1000
    tool_moi_lan = runs["tool_calls"] * gia_tool

    token = token_moi_lan.sum()
    tool = tool_moi_lan.sum()
    xem_lai = reqs["phut_xem_lai_simulated"].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs["phut_lam_lai_simulated"].sum() * luong_phut * he_so_lam_lai
    thanh_cong = (reqs["ket_qua"] == "thanh_cong").sum()
    tong = token + tool + xem_lai + lam_lai
    return {
        "token": token,
        "tool": tool,
        "chay_lai": (token_moi_lan + tool_moi_lan)[runs["attempt"] > 1].sum(),
        "xem_lai": xem_lai,
        "lam_lai": lam_lai,
        "tong": tong,
        "thanh_cong": thanh_cong,
        "cps": tong / thanh_cong if thanh_cong else math.inf,
        "hoa_don_moi_yc": (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


# ---------- TV2 · Kiểm số độc lập, không thay phần A/B của TV1 ----------
def kiem_so_doc_lap():
    """Tính bằng csv + Decimal để đối chiếu mo_hinh của TV1 khi bàn giao.

    Tính độc lập rồi đối chiếu với các hàm A/B của TV1. Chi phí có giờ người
    là simulated; kịch bản giới hạn chạy tuân theo quy ước của đề lab.
    """
    thu_muc = Path(__file__).resolve().parent
    with (thu_muc / 'logix_runs.csv').open(encoding='utf-8', newline='') as f:
        luot = list(csv.DictReader(f))
    with (thu_muc / 'logix_requests.csv').open(encoding='utf-8', newline='') as f:
        yeu_cau = list(csv.DictReader(f))
    assert len(luot) == 1624 and len(yeu_cau) == 1200
    assert len({r['request_id'] for r in yeu_cau}) == len(yeu_cau)
    assert {r['request_id'] for r in luot} == {r['request_id'] for r in yeu_cau}

    def tinh(ds, gia_vao=26, gia_ra=130, luong=2000, xem=1, lam=1, gioi_han=3):
        ids = {r['request_id'] for r in ds}
        rr = [r for r in luot if r['request_id'] in ids
              and int(r['attempt']) <= gioi_han]
        duoc_giu = [r for r in ds if int(r['so_lan_chay']) <= gioi_han]
        token = sum((Decimal(r['tokens_in']) * gia_vao
                     + Decimal(r['tokens_out']) * gia_ra) / 1000 for r in rr)
        tool = sum(int(r['tool_calls']) * 15 for r in rr)
        chay_lai = sum((Decimal(r['tokens_in']) * gia_vao
                        + Decimal(r['tokens_out']) * gia_ra) / 1000
                       + int(r['tool_calls']) * 15
                       for r in rr if int(r['attempt']) > 1)
        phut_xem = sum(Decimal(r['phut_xem_lai_simulated']) for r in duoc_giu)
        phut_lam = sum(Decimal(r['phut_lam_lai_simulated']) for r in duoc_giu)
        tien_xem = phut_xem * luong * Decimal(str(xem))
        tien_lam = phut_lam * luong * Decimal(str(lam))
        tong = token + tool + tien_xem + tien_lam
        thanh_cong = sum(r['ket_qua'] == 'thanh_cong' for r in duoc_giu)
        return dict(token=token, tool=tool, chay_lai=chay_lai,
                    phut_xem=phut_xem, phut_lam=phut_lam,
                    xem_lai=tien_xem, lam_lai=tien_lam, tong=tong,
                    thanh_cong=thanh_cong, cps=tong / thanh_cong,
                    hoa_don_moi_yc=(token + tool) / len(ds),
                    so_yeu_cau=len(ds), so_luot=len(rr),
                    khong_thanh_cong=len(ds) - thanh_cong,
                    ca_he_thong=tong + (len(ds) - thanh_cong) * BASELINE)

    goc = tinh(yeu_cau)
    # Phép tính tay độc lập theo tổng token và tổng phút, không gọi mo_hinh.
    assert goc['phut_xem'] == 890 and goc['phut_lam'] == 1132
    assert goc['tool'] == 5600 * GIA_TOOL and goc['thanh_cong'] == 978
    assert goc['cps'] == (goc['token'] + 84000 + 890 * 2000 + 1132 * 2000) / 978
    theo_loai = {loai: tinh([r for r in yeu_cau if r['loai'] == loai])
                 for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac')}
    kich_ban = {
        'token_x2': dict(gia_vao=52, gia_ra=260),
        'token_chia2': dict(gia_vao=13, gia_ra=65),
        'xem_x2': dict(xem=2), 'xem_chia2': dict(xem=0.5),
        'lam_x2': dict(lam=2), 'lam_chia2': dict(lam=0.5),
        'luong_25pct': dict(luong=2500),
        'toi_da_2': dict(gioi_han=2), 'toi_da_1': dict(gioi_han=1),
        'token_va_xem_x2': dict(gia_vao=52, gia_ra=260, xem=2),
    }
    nhay = {ten: tinh(yeu_cau, **kw) for ten, kw in kich_ban.items()}
    for loai in ('token', 'xem', 'lam'):
        assert abs((nhay[f'{loai}_x2']['cps'] - goc['cps']) / 2
                   - (goc['cps'] - nhay[f'{loai}_chia2']['cps'])) < Decimal('1e-20')
    assert abs(nhay['token_va_xem_x2']['cps'] - goc['cps']
               - (nhay['token_x2']['cps'] - goc['cps'])
               - (nhay['xem_x2']['cps'] - goc['cps'])) < Decimal('1e-20')
    gioi_han = {k: tinh(yeu_cau, gioi_han=k) for k in (1, 2, 3)}

    pham_vi = [r for r in yeu_cau if r['loai'] in ('noi_dia', 'hang_nang')]
    trong_pv = tinh(pham_vi)
    ids_pv = {r['request_id'] for r in pham_vi}
    ok = {r['request_id'] for r in luot
          if r['request_id'] in ids_pv and r['status'] == 'ok'}
    ca_lam_lai = sum(r['ket_qua'] == 'lam_lai' for r in pham_vi)
    ca_lam_toan_bo = sum(r['ket_qua'] == 'lam_lai' for r in yeu_cau)
    phut_lam_tb = goc['phut_lam'] / ca_lam_toan_bo
    b4 = {}
    for ten, phut in [('9_phut', Decimal(9)), ('15.3_phut', Decimal('15.3')),
                     ('trung_binh_chinh_xac', phut_lam_tb)]:
        tong = trong_pv['token'] + trong_pv['tool'] + len(ok) * 5 * 2000 + ca_lam_lai * phut * 2000
        b4[ten] = dict(tong=tong, cps=tong / trong_pv['thanh_cong'],
                       phut_xem_hoa_von=(BASELINE * trong_pv['thanh_cong']
                                         - trong_pv['token'] - trong_pv['tool']
                                         - ca_lam_lai * phut * 2000) / (len(ok) * 2000))
    a4 = {}
    for khoi_luong in (45000, 22500):
        so_viec = Decimal(khoi_luong) * trong_pv['thanh_cong'] / len(yeu_cau)
        co_dinh = Decimal(40000000) / so_viec
        a4[khoi_luong] = dict(thanh_cong_thang=so_viec, co_dinh_moi_viec=co_dinh,
                              cps_co_dinh=trong_pv['cps'] + co_dinh)
    an_toan = {ten: dict(mo_lai=sum(int(r['mo_lai_trong_7_ngay']) for r in ds),
                         n=len(ds)) for ten, ds in [('tat_ca', yeu_cau), ('pham_vi', pham_vi)]}
    quoc_te = {r['request_id'] for r in yeu_cau if r['loai'] == 'quoc_te'}
    ok_quoc_te = {}
    for k in (1, 2, 3):
        ds = [r for r in luot if r['request_id'] in quoc_te and int(r['attempt']) == k]
        ok_quoc_te[k] = (sum(r['status'] == 'ok' for r in ds), len(ds))

    # So với code TV1 nếu đã được bàn giao; không coi NotImplemented là ĐẠT.
    ban_giao = 'CHỜ TV1: A1 hoặc mo_hinh còn NotImplementedError; chưa xác nhận A1/A-B.'
    try:
        rr = pd.read_csv(thu_muc / 'logix_runs.csv')
        qq = pd.read_csv(thu_muc / 'logix_requests.csv', keep_default_na=False)
        kiem_tra_dap_an_biet_truoc()
        doi_chieu = [(goc, mo_hinh(rr, qq))]
        for loai, gia_tri in theo_loai.items():
            doi_chieu.append((gia_tri, mo_hinh(rr, qq[qq.loai == loai])))
        for ten, kw in kich_ban.items():
            doi_ten = {'luong': 'luong_phut', 'xem': 'he_so_xem_lai',
                       'lam': 'he_so_lam_lai', 'gioi_han': 'max_lan_chay'}
            doi_chieu.append((nhay[ten], mo_hinh(rr, qq, **{doi_ten.get(k, k): v for k, v in kw.items()})))
        for doc_lap, tv1 in doi_chieu:
            for cot in ('token', 'tool', 'chay_lai', 'xem_lai', 'lam_lai',
                        'tong', 'thanh_cong', 'cps', 'hoa_don_moi_yc'):
                assert math.isclose(float(doc_lap[cot]), float(tv1[cot]), rel_tol=1e-9, abs_tol=1e-6), cot
        ban_giao = 'ĐẠT: A1 và 15 cấu hình A/B của TV1 khớp kiểm số độc lập.'
    except NotImplementedError:
        pass
    return dict(a2=goc, a3=theo_loai, a4=a4, b1_b2=nhay, b3=gioi_han,
                b4=b4, b4_so_ok=len(ok), b4_ca_lam_lai=ca_lam_lai,
                phut_lam_tb=phut_lam_tb, an_toan=an_toan,
                ok_quoc_te=ok_quoc_te, ban_giao_tv1=ban_giao)


# ---------- TV2 · Nhiệm vụ D1 · Cỡ mẫu và đánh đổi thiết kế ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.8):
    """Công thức z hai phía trong tài liệu lab; trả về số yêu cầu mỗi nhánh."""
    if not (0 < p1 < 1 and 0 < p2 < 1 and p1 != p2
            and 0 < alpha < 1 and 0 < power < 1):
        raise ValueError('Cần hai tỉ lệ khác nhau trong (0, 1), alpha và power trong (0, 1).')
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                     / (p2 - p1) ** 2)


def tinh_d1():
    """Đủ năm câu D1; n_eff là số hiệu dụng, không phải lượng cần thu thập."""
    n5 = co_mau_hai_ti_le(0.70, 0.75)
    icc, c = 0.02, 20
    de75 = 1 + (75 - 1) * icc
    n6 = 859  # Câu e cho sẵn 859; công thức z cũng ra 859.
    assert co_mau_hai_ti_le(0.70, 0.76) == n6
    m = math.ceil(n6 * (1 - icc) / (c - n6 * icc))
    de = 1 + (m - 1) * icc
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    power5 = NormalIndPower().power(
        effect_size=abs(proportion_effectsize(0.70, 0.75)),
        nobs1=c * m / de, alpha=0.05, ratio=1, alternative='two-sided')
    return dict(a_n_moi_nhom=n5, b_de=de75, b_n_moi_nhom=math.ceil(n5 * de75),
                b_so_nguoi_moi_nhom=math.ceil(math.ceil(n5 * de75) / 75),
                c_tran_hieu_dung=c / icc, d_tran_hieu_dung=6 / icc,
                e_n_hieu_dung_can=n6, e_m=m, e_de=de,
                e_n_thu_thap_moi_nhom=c * m, e_n_hieu_dung=c * m / de,
                power_neu_chi_tang_5_diem=float(power5))


def in_d1():
    print('\nD1 · Cỡ mẫu (giả định lab: baseline 0,70; ICC 0,02)')
    for ten, gia_tri in tinh_d1().items():
        print(f'{ten:32s} {gia_tri:,.6f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lab 13 · A/B của TV1, kiểm số và D1 của TV2')
    parser.add_argument('--pilot-only', action='store_true', help='Chạy riêng đủ 5 câu D1, không chờ A/B của TV1')
    parser.add_argument('--kiem-so', action='store_true', help='Kiểm số A/B độc lập từ CSV, rồi tính D1')
    args = parser.parse_args()
    if args.pilot_only:
        in_d1()
        raise SystemExit(0)
    if args.kiem_so:
        import json
        print('TV2 · Kiểm số độc lập từ CSV; mọi chi phí có giờ người là simulated.')
        print(json.dumps(kiem_so_doc_lap(), ensure_ascii=False, indent=2, default=str))
        in_d1()
        raise SystemExit(0)
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print("\nA2 - Chi phí từ trace")
    for ten, gia_tri in ket_qua.items():
        nhan = " simulated" if ten in {"xem_lai", "lam_lai", "tong", "cps"} else ""
        print(f"{ten:16s} {gia_tri:>14,.2f}{nhan}")
    he_so_hoa_don = ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]
    ty_trong_lam_lai = ket_qua["lam_lai"] / ket_qua["tong"]
    print(f"CPS gấp {he_so_hoa_don:.1f} lần hóa đơn mỗi yêu cầu (simulated)")
    print(f"Làm lại chiếm {ty_trong_lam_lai:.1%} tổng chi phí (simulated)")

    print("\nA3 - Chi phí theo loại yêu cầu (simulated)")
    for loai, nhom in reqs.groupby("loai"):
        ket_qua_nhom = mo_hinh(runs, nhom)
        ty_le = ket_qua_nhom["thanh_cong"] / len(nhom)
        so_lan_trung_binh = nhom["so_lan_chay"].mean()
        cps_nhom = ket_qua_nhom["cps"]
        print(
            f"{loai:10s} {len(nhom):4d} yêu cầu | {ty_le:6.1%} thành công | "
            f"{so_lan_trung_binh:.2f} lần/yêu cầu | {cps_nhom:,.0f} đ | "
            f"{cps_nhom / BASELINE:.2f}x"
        )

    quoc_te = reqs.loc[reqs["loai"] == "quoc_te", "request_id"]
    runs_quoc_te = runs[runs["request_id"].isin(quoc_te)]
    ty_le_ok = runs_quoc_te["status"].eq("ok").groupby(runs_quoc_te["attempt"]).mean()
    for lan, ty_le in ty_le_ok.items():
        print(f"Quốc tế, lần {lan}: {ty_le:.1%} lượt chạy ok")

    pham_vi = reqs[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    ket_qua_pham_vi = mo_hinh(runs, pham_vi)
    viec_thanh_cong_thang = 45_000 * ket_qua_pham_vi["thanh_cong"] / len(reqs)
    co_dinh_moi_viec = 40_000_000 / viec_thanh_cong_thang
    print("\nA4 - Chi phí gồm cố định (simulated)")
    for ty_le_khoi_luong in (1.0, 0.5):
        co_dinh = co_dinh_moi_viec / ty_le_khoi_luong
        cps = ket_qua_pham_vi["cps"] + co_dinh
        print(
            f"{ty_le_khoi_luong:.0%} khối lượng: "
            f"{viec_thanh_cong_thang * ty_le_khoi_luong:,.0f} việc thành công/tháng | "
            f"cố định {co_dinh:,.0f} đ/việc | tổng {cps:,.0f} đ/việc "
            f"({cps / BASELINE:.2f}x)"
        )

    cps_goc = ket_qua["cps"]
    kich_ban = {
        "Token gấp đôi": {"gia_vao": 52, "gia_ra": 260},
        "Token giảm một nửa": {"gia_vao": 13, "gia_ra": 65},
        "Xem lại gấp đôi": {"he_so_xem_lai": 2},
        "Xem lại giảm một nửa": {"he_so_xem_lai": 0.5},
        "Làm lại gấp đôi": {"he_so_lam_lai": 2},
        "Làm lại giảm một nửa": {"he_so_lam_lai": 0.5},
        "Lương tăng 25%": {"luong_phut": 2500},
        "Tối đa 2 lần chạy": {"max_lan_chay": 2},
        "Tối đa 1 lần chạy": {"max_lan_chay": 1},
    }

    print("\nB1 - Độ nhạy (simulated)")
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        thay_doi = 100 * (cps / cps_goc - 1)
        print(f"{ten}: {cps:,.0f} đ ({thay_doi:+.1f}%)")

    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)["cps"]
    print("\nB2 - Token và xem lại cùng gấp đôi (simulated)")
    print(f"{cps_cap:,.0f} đ ({100 * (cps_cap / cps_goc - 1):+.1f}%)")

    print("\nB3 - Chi phí theo giới hạn lần chạy (simulated)")
    for k in (1, 2, 3):
        ket_qua_gioi_han = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - ket_qua_gioi_han["thanh_cong"]
        tong_he_thong = ket_qua_gioi_han["tong"] + BASELINE * khong_thanh_cong
        print(
            f"{k} lần | trợ lý {ket_qua_gioi_han['tong']:,.0f} đ | "
            f"{khong_thanh_cong} yêu cầu không thành công | "
            f"hệ thống {tong_he_thong:,.0f} đ | CPS {ket_qua_gioi_han['cps']:,.0f} đ"
        )

    runs_pham_vi = runs[runs["request_id"].isin(pham_vi["request_id"])]
    so_yeu_cau_ok = runs_pham_vi.loc[
        runs_pham_vi["status"] == "ok", "request_id"
    ].nunique()
    so_ca_lam_lai = (pham_vi["ket_qua"] == "lam_lai").sum()
    print("\nB4 - Xem lại toàn bộ yêu cầu có lượt ok (simulated)")
    print(f"{so_yeu_cau_ok} yêu cầu có lượt ok | {so_ca_lam_lai} ca làm lại")
    token_tool = ket_qua_pham_vi["token"] + ket_qua_pham_vi["tool"]
    tien_xem_lai = 5 * so_yeu_cau_ok * LUONG_PHUT
    for phut_lam_lai in (9, 15.3):
        tien_lam_lai = phut_lam_lai * so_ca_lam_lai * LUONG_PHUT
        cps = (token_tool + tien_xem_lai + tien_lam_lai) / ket_qua_pham_vi["thanh_cong"]
        print(f"{phut_lam_lai:g} phút làm lại/ca | {cps:,.0f} đ/việc ({cps / BASELINE:.2f}x)")

    # CP4 · TV2 tính đủ năm câu D1 sau các bảng A/B của TV1.
    in_d1()
