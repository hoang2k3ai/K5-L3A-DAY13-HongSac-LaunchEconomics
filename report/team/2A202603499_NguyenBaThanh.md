# Báo cáo cá nhân — Nguyễn Bá Thành — 2A202603499

## 1. Thông tin thành viên

- Họ tên: Nguyễn Bá Thành.
- MSSV: 2A202603499.
- Email: chưa cung cấp, cần bổ sung trước khi nộp.
- Vai: **TV2 · Kiểm số và thiết kế pilot**; tiếp quản code sau giải lao.
- Nhóm: Hồng Sắc; lớp L3A, theo tên repo.
- Tên/MSSV được điền theo file cá nhân đã có trong repo; cần thành viên xác nhận.

## 2. Phần việc phụ trách

- Tính tay ít nhất 1 kết quả để đối chiếu; điền A2–A4, B1–B4 và xếp hạng 3 yếu tố nhạy nhất trong [bảng chi phí](bang_chi_phi.md).
- Sau bàn giao TV1: tự chạy lại code chi phí; làm 5 câu D1 trong [lab13.py](../../src/lab13.py), trả lời 5 câu D2 và hoàn thiện [pilot plan](pilot_plan.yaml).
- Bàn giao số A–B cho TV3 viết rủi ro, số A–D cho TV4 tổng hợp hồ sơ; tự nộp link repo nhóm bằng tài khoản LMS cá nhân.

## 3. Đóng góp cụ thể

Các nội dung dưới đây đã được chuẩn bị và chạy kiểm tra bằng Codex trên bản repo hiện tại; chưa thay cho việc thành viên tự đọc, tính lại và chạy trên máy của mình.

| Phần | Nội dung đã chuẩn bị | Kết quả chính |
| --- | --- | --- |
| Kiểm số A | Phép tính tay và phép cộng độc lập bằng CSV + Decimal; điền A1–A4 | CPS **4.472 đ**, tỷ lệ làm lại trong chi phí **51,77%** (`simulated`) |
| Độ nhạy B | Đủ 9 kịch bản B1, cặp B2, ba giới hạn B3, xem lại 100% B4 | Làm lại > xem lại > lương theo các kịch bản; **2 lượt** rẻ nhất hệ thống: **6.901.220 đ** (`simulated`) |
| Cỡ mẫu D1 | Công thức z và DE, phân biệt mẫu thực với hiệu dụng | **1.251** theo yêu cầu; **3.103** với m=75; trần **1.000/300**; m tối thiểu **299** khi chấp nhận +6 điểm |
| Thiết kế D2/D3 | Đối chứng cùng thời gian, chia ngẫu nhiên theo nhân viên, kiểm soát tràn tác động, 4 luật dừng và rollback | **20+20** người, **5.980** yêu cầu thực/nhánh, **859,20** hiệu dụng; quyết định đề xuất **05/01/2027** |

Phép tính để tự giải thích: `(245.585,132 + 84.000 + 890×2.000 + 1.132×2.000) / 978 = 4.471,9684 đ` (`simulated`).
Giới hạn 1 lượt có CPS thấp nhất nhưng đẩy thêm **85** yêu cầu sang nhân viên so với 2 lượt; vì vậy tối ưu CPS không đồng nghĩa tối ưu chi phí công ty.
Chia 20 cụm/nhánh có trần hiệu dụng **1.000 < 1.251**; tăng thời gian không khắc phục được thiếu cụm cho mục tiêu +5 điểm.

## 4. Bằng chứng

- [bang_chi_phi.md](bang_chi_phi.md): A1–A4, B1–B4, nhãn `simulated`, công thức tính tay và nguồn.
- [pilot_plan.yaml](pilot_plan.yaml): D1/D2 ở chú thích, thiết kế và các ngưỡng; số lượng mẫu thực ghi rõ **5.980/nhánh**, không nhầm với **859** hiệu dụng.
- [src/lab13.py](../../src/lab13.py): `kiem_so_doc_lap`, `co_mau_hai_ti_le`, `tinh_d1`, cờ `--kiem-so` và `--pilot-only`; phần A/B của TV1 được giữ nguyên để nhận bàn giao.
- [ban_giao_tv2.md](ban_giao_tv2.md): các lệnh chạy, phụ thuộc TV1, đầu vào cho TV3/TV4 và checklist cá nhân.
- [kiem_chung_tv2.txt](kiem_chung_tv2.txt): output kiểm số và D1 tạo từ script trên bản hiện tại; có trạng thái chờ TV1.
- Commit TV2: chưa tạo; chỉ điền mã commit thật sau khi commit. Chưa ghi nhận kiểm tra trên máy khác hoặc kết quả duyệt chéo.

## 5. Công cụ AI đã dùng

**Codex/ChatGPT** hỗ trợ đọc tài liệu repo, giải thích công thức, viết phần kiểm số/D1, soạn bảng và kế hoạch, cài thư viện trong môi trường ảo, chạy kiểm tra.
Không gọi mô hình qua API; không sửa CSV, không tạo nhãn độc lập hoặc điểm hội đồng thay TV3/TV4.

**Kiểm tra tự động đã thực hiện trong phiên hỗ trợ:** cộng độc lập bằng `csv.Decimal` (module `csv` + lớp `decimal.Decimal`), kiểm quan hệ gấp đôi/giảm nửa và tính cộng B2, tính lại 5 câu D1, tính power bằng statsmodels và đọc YAML bằng `yaml.safe_load`.
Đối chiếu hướng dẫn nội bộ; riêng B4, **12.414,79 đ** được làm tròn thành **12.415 đ** (`simulated`), khác xấp xỉ 12.414 đ trong tài liệu dưới **1 đ**.

**Tự kiểm tra của thành viên trước khi nộp:** tự tính lại phép tính A2 ở mục 3; chạy 2 lệnh dưới đây; sau khi pull TV1 chạy cả script và giải thích được tử số/mẫu số, trần cỡ mẫu và lựa chọn 2 lượt. Chỉ đánh dấu hoàn thành sau khi đã thực hiện thật.

```powershell
# Từ thư mục gốc repo
$env:PYTHONIOENCODING = "utf-8"
Set-Location src
../.venv/Scripts/python.exe lab13.py --kiem-so
../.venv/Scripts/python.exe lab13.py --pilot-only
# Sau khi TV1 hoàn thiện và ghép A/B:
../.venv/Scripts/python.exe lab13.py
```

Nếu môi trường ảo nằm ở `src/.venv` theo hướng dẫn nhóm, thay đường dẫn Python bằng `./.venv/Scripts/python.exe`.

## 6. Tự đánh giá

Bộ tài liệu đã chuẩn bị đủ phần kiểm số và thiết kế của TV2; việc chốt A–B với code TV1 còn chờ bàn giao.
Kế hoạch chấp nhận MDE **+6 điểm**: nếu hiệu quả thật chỉ **+5 điểm**, power xấp xỉ **64,18%**, không phải 80%; các con số chi phí giờ người vẫn là `simulated` cho đến khi đo phút thật.
Trước nộp cần xác nhận thông tin cá nhân, tự kiểm số/chạy code, bổ sung commit thật, phối hợp TV4 ghi đóng góp cuối và tự nộp link LMS; chưa tuyên bố các việc này đã hoàn thành.
