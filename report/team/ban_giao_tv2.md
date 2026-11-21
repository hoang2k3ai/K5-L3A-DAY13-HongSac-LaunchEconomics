# Bàn giao TV2 — Kiểm số và thiết kế pilot

**Phần kỹ thuật TV2 đã hoàn thiện.** Đã nhận A–B của TV1 (`97c5410`), ghép với code TV2 (`78fb538`) và kiểm lại các số dùng trong hồ sơ.
Báo cáo cá nhân: [Nguyễn Bá Thành — 2A202603499](2A202603499_NguyenBaThanh.md).

## 1. Đối chiếu phân công

| Việc được giao | Bằng chứng | Trạng thái kỹ thuật |
| --- | --- | --- |
| Tính ít nhất 1 kết quả đối chiếu | Phép tính A2 trong [bang_chi_phi.md](bang_chi_phi.md), kiểm độc lập `Decimal` | Hoàn thành; thành viên tự tính lại để giải thích |
| Điền A2–A4, B1–B4, xếp hạng 3 yếu tố | Các bảng đủ số và nhãn `simulated`; 15 cấu hình khớp code TV1 | Hoàn thành |
| Tiếp quản code, chạy lại chi phí | Script A–B–D1–D3 và [output kiểm chứng](kiem_chung_tv2.txt) | Hoàn thành trong phiên hỗ trợ Codex |
| Làm 5 câu D1 | `tinh_d1()`, in theo câu a–e; chú thích đầu YAML | Hoàn thành |
| Trả lời 5 câu D2, chọn đối chứng | `pilot_plan.yaml`: chia nhân viên, ngẫu nhiên phân tầng, 20+20 người | Hoàn thành |
| Viết ít nhất 3 luật dừng | 4 luật: giao dịch, mở lại, chi phí, sử dụng; đủ NẾU–TRONG–THÌ–KHÔNG THÌ | Hoàn thành |
| Báo cáo cá nhân, đóng góp | Báo cáo đúng tên MSSV, khai AI và bằng chứng; mục TV2 trong TEAM.md | Hoàn thành |

**Phụ thuộc TV1 đã được giải quyết:** A1 đạt và A–B đã nhận, kiểm số, ghép. Không còn phải chờ TV1 để hoàn thành D1/D2 hay tài liệu TV2.

## 2. Chạy và kiểm tra

Từ gốc repo, dùng môi trường ảo đã có ở `.venv/`:

```powershell
$env:PYTHONIOENCODING = "utf-8"
Set-Location src
../.venv/Scripts/python.exe lab13.py
../.venv/Scripts/python.exe lab13.py --kiem-so
../.venv/Scripts/python.exe lab13.py --pilot-only
../.venv/Scripts/python.exe -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8')); print('YAML OK')"
```

`--kiem-so` kiểm **15 cấu hình × 9 trường số**: 1 gốc, 4 loại yêu cầu, 9 kịch bản đơn, 1 cặp.
`--pilot-only` in đủ D1 a–e và tỷ lệ mở lại để kiểm luật D3. Nếu dùng môi trường `src/.venv`, thay đường dẫn Python bằng `./.venv/Scripts/python.exe`.

## 3. Số bàn giao cho TV3 và TV4

| Nội dung | Kết quả | Phạm vi và nhãn |
| --- | --- | --- |
| CPS toàn mẫu | 4.471,97 đ; 978 thành công | simulated; chưa cố định |
| Chi phí hệ thống/yêu cầu | 5.864,65 đ = 0,489× baseline | simulated; quy ước B3, chưa cố định |
| Nội địa + hàng nặng | 982 yêu cầu, 900 thành công; CPS 3.413,90 đ | CPS simulated |
| Có cố định 40 triệu đ/tháng | 4.599 đ/việc ở 45.000 yêu cầu; 5.784 đ ở 22.500 | simulated; A4 chưa gồm luồng nhân viên |
| Nhạy nhất theo kịch bản đề | Làm lại +51,77%; xem lại +40,70%; lương +23,12% | simulated |
| Giới hạn rẻ nhất B3 | 2 lượt: 6.901.220 đ/1.200 yêu cầu | simulated; toàn mẫu, cần đo thật khi pilot |
| Xem lại 100% B4 | 11.743 đ với 9 phút làm lại; 12.415 đ với 15,3 phút | simulated; chưa cố định và chuyển nhân viên |
| D1 | 20+20 người; 299 yêu cầu/người; 5.980 thực/nhánh; 859,20 hiệu dụng | DE 6,96; thiết kế MDE +6 điểm |
| Đánh đổi bất lợi | Power chỉ 64,18% nếu tác động thật +5 điểm | Xấp xỉ theo ICC 0,02; không tuyên bố power 80% ở +5 |
| Mở lại | 51/1.200 = 4,25%; phạm vi 39/982 = 3,9715% | Dữ liệu giả lập; không phải chênh đối chứng |
| Lịch pilot đề xuất | Bắt đầu 23/11/2026; đo ổn định từ 07/12; nhận mẫu đến 27/12; theo dõi hết 04/01; quyết định 05/01/2027 | Lịch kế hoạch, không phải hoạt động đã diễn ra |

TV3 dùng số B cho rủi ro và hoàn thiện event/phút đo thật. TV4 đưa đánh đổi MDE, chi phí xem lại 100% và ngày quyết định vào hồ sơ.
Kế hoạch là sản phẩm thiết kế cho tình huống giả định; không ghi đã có chữ ký chấp nhận, kết quả pilot hay điểm hội đồng.

## 4. Ba lập luận cần giải thích khi trình bày

| Nội dung | Lập luận bằng số |
| --- | --- |
| Vì sao chia cho việc thành công | 1.624 lượt đều tốn tiền, nhưng chỉ 978 việc đạt yêu cầu; dùng 1.200 làm mẫu số sẽ thành chi phí/yêu cầu, không phải CPS |
| Vì sao chọn 2 lượt | 1 lượt có CPS 4.111 đ nhưng hệ thống tốn 7.449.781 đ; 2 lượt có CPS 4.237 đ và hệ thống chỉ 6.901.220 đ (simulated) |
| Vì sao không kéo dài để đủ +5 điểm | Với 20 cụm/nhánh, n hiệu dụng <20/0,02=1.000<1.251; cần đổi thiết kế hoặc chấp nhận MDE +6, không chỉ tăng ngày |

## 5. Lưu bài và việc cá nhân cuối cùng

- Phần TV2 đã lưu ở `34da9c0`, ghép với TV1 tại `78fb538`; các hoàn thiện cuối được lưu bằng commit bổ sung.
- Có bản sao trước ghép ngoài repo: `../../../TV2_Backup/TV2_before_merge_20261121_153052.zip` (tính từ thư mục chứa file này).
- Nhánh nộp: `main`; commit hoàn thiện TV2: `1634e58`. Khi cập nhật bài, kiểm tra remote và fetch/merge nếu có thay đổi mới, không force-push.
- Thành viên tự đọc output và tính lại phép đối chiếu A2; thống nhất MDE, luật dừng và lịch kế hoạch với nhóm.
- Tự nộp cùng link repo nhóm trên tài khoản LMS trước hạn lớp; TV4 tổng hợp kết quả duyệt chéo từ thực tế.

Nguồn: quy định repo, đề lab, dữ liệu và công thức, hướng dẫn chi tiết nội bộ; xem nguồn tại [bảng chi phí](bang_chi_phi.md).
