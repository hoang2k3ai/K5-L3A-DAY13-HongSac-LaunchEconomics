"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
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


if __name__ == '__main__':
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

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
