# Báo cáo cá nhân — Nguyễn Bá Thành — 2A202603499

## 1. Thông tin thành viên

- Họ tên: Nguyễn Bá Thành.
- MSSV: 2A202603499.
- Email: 26ai.thanhnb3@vinuni.edu.vn.
- GitHub: Nguyen-Ba-Thanh.
- Nhóm: Hồng Sắc · Lớp: L3A.
- Vai trò: **TV2 · Kiểm số và thiết kế pilot**, tiếp quản code sau giải lao.

## 2. Phần việc phụ trách

- Kiểm số A1–A4; điền bảng A2–A4, B1–B4 và xếp hạng 3 yếu tố nhạy nhất.
- Tiếp nhận code A–B của TV1; bổ sung 5 câu D1 vào `src/lab13.py`, trả lời 5 câu D2, chọn cách chia, đối chứng và luật dừng trong `pilot_plan.yaml`.
- Cung cấp số kinh tế và đánh đổi thiết kế cho TV3/TV4 tổng hợp, đồng thời ghi đóng góp cá nhân trong `TEAM.md`.

## 3. Đóng góp cụ thể

| Phần | Nội dung | Kết quả |
| --- | --- | --- |
| Kiểm số A | Tính độc lập từ hai CSV bằng `csv` và `Decimal`; trình bày phép tính đối chiếu | **978** thành công; CPS **4.471,97 đ**; làm lại chiếm **51,77%** chi phí (`simulated`) |
| Bảng A–B | Hoàn thiện A1–A4, 9 kịch bản B1, B2 và so sánh B3/B4 | **2 lượt** rẻ nhất cả hệ thống: **6.901.220 đ**; xem lại 100%: **11.743 đ** với 9 phút làm lại (`simulated`) |
| Tiếp quản code | Ghép A–B từ TV1, giữ kiểm số độc lập và bổ sung D1/D3 | **3** phép thử A1 đạt; **15** cấu hình đối chiếu khớp; script chạy hết A–B–D1–D3 |
| Thiết kế pilot | D1, D2, nhóm đối chứng, 4 luật dừng, rollback và ngày quyết định | **20+20** người; **299** yêu cầu/người; **5.980** yêu cầu thực/nhánh, khoảng **859,20** hiệu dụng |

Phép tính đối chiếu: `(245.585,132 + 84.000 + 890×2.000 + 1.132×2.000) / 978 = 4.471,9684 đ/việc thành công` (`simulated`).
Tử số gồm mọi lượt, kể cả lỗi; phí chạy lại **93.804,49 đ** đã nằm trong token/tool nên không cộng lần nữa.

Xếp hạng theo các kịch bản đề yêu cầu: **làm lại +51,77% > xem lại +40,70% > lương +23,12%** (`simulated`).
Giới hạn **1 lượt** có CPS thấp nhất nhưng chuyển thêm **85** yêu cầu cho nhân viên so với **2 lượt**, nên không tối ưu chi phí cả công ty.

## 4. Bằng chứng

- [Bảng chi phí](bang_chi_phi.md): đủ A1–A4/B1–B4, phép tính và nhãn `simulated`.
- [Code nhóm](../../src/lab13.py): `kiem_so_doc_lap()`, `tinh_d1()`, `in_d1()`, `in_an_toan_pilot()`; các chế độ `--kiem-so` và `--pilot-only`.
- [Pilot plan](pilot_plan.yaml): đủ 5 câu D1, 5 câu D2, đối chứng và 4 luật dừng; ngày quyết định đề xuất **05/01/2027**.
- [Output kiểm chứng](kiem_chung_tv2.txt): kết quả chạy script và kiểm số trên môi trường máy TV2 trong phiên làm việc với Codex.
- [Bàn giao TV2](ban_giao_tv2.md) và [TEAM.md](../../TEAM.md): kết quả để TV3/TV4 sử dụng và đóng góp cá nhân.
- Commit TV2 trước bàn giao: `34da9c0`; code A–B của TV1: `97c5410`; commit ghép: `78fb538`. Các hoàn thiện sau đó được lưu bằng commit mới.

## 5. Công cụ AI đã dùng

Sử dụng **Codex/ChatGPT** để giải thích công thức, gợi ý code kiểm số/D1, soạn và rà báo cáo, giải quyết xung đột khi ghép code, chạy kiểm tra. Không dùng API key; không sửa hai CSV.

Cách kiểm chứng đã thực hiện trong phiên hỗ trợ: tính độc lập bằng `Decimal` rồi so **15 cấu hình × 9 trường số** với `mo_hinh` của TV1; chạy ba phép thử A1 và toàn bộ script; đối chiếu cỡ mẫu bằng công thức z/statsmodels; đọc YAML bằng `yaml.safe_load` và kiểm cỡ mẫu, luật dừng, lịch theo dõi.
Phép tính đối chiếu ở mục 3 cho phép kiểm lại A2 bằng máy tính tay. Kết quả chạy tự động được lưu rõ nguồn; không ghi nhận thay việc người học tự tính, hiểu bài hay nộp LMS.

## 6. Tự đánh giá

Phần kỹ thuật và tài liệu thuộc TV2 đã hoàn thiện: có code chạy được, bảng A–B khớp code TV1, thiết kế pilot và bằng chứng kiểm tra.
Chọn chia theo nhân viên để hạn chế tràn tác động; với **20 cụm/nhánh**, cỡ mẫu hiệu dụng luôn **<1.000**, nên chấp nhận thiết kế cho mức tăng **6 điểm %**. Nếu tác động thật chỉ **5 điểm %**, power xấp xỉ **64,18%**.

Chi phí có giờ nhân viên vẫn là `simulated`; phải thay bằng phút đo thật trong pilot. Xem lại 100% có thể lên **12.415 đ/việc** nếu làm lại 15,3 phút, chưa có cố định (`simulated`), nên không bỏ qua rủi ro này khi trình hồ sơ.
Thành viên tự đọc và giải thích phép tính, thống nhất phương án với nhóm, rồi tự nộp link repo trên LMS; kết quả duyệt chéo do TV4 ghi từ buổi thực tế.
