# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Trạng thái và nguồn hỗ trợ

Bản nháp TV3 được soạn với Codex từ 20 ca trong đề Word và mục C của [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Nhãn dưới đây là đề xuất có giải thích, không phải bằng chứng TV3 và TV4 đã gắn nhãn độc lập.
TV3 cần tự đọc và kiểm tra; TV4 cần hoàn thành bộ nhãn riêng trước khi xem bảng đề xuất này. Nếu đã xem nhãn tham khảo trước khi làm, ghi rõ trong báo cáo, không gọi đó là lượt gắn nhãn độc lập.

## Nhãn đề xuất để TV3 tự kiểm tra

| Ca | Nhãn đề xuất có hỗ trợ AI | Lý do theo nguyên nhân gốc |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập tài khoản thiếu hai chữ số; xác thực đầu vào là biện pháp khắc phục. |
| 2 | Hệ thống | Trợ lý chọn sai tham số bảng giá cho kiện 28 kg, hoàn thiếu 45.000 đ. |
| 3 | Ngữ cảnh | Hoàn về ví đúng thiết kế nhưng khách chờ tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | Không có dữ liệu chặng nước ngoài nên phải chuyển nhân viên. |
| 5 | Ngầm | Hoàn thừa ở 14 đơn chỉ được phát hiện qua kiểm tra mẫu cuối tuần. |
| 6 | Do người dùng | Khách chọn mục giao trễ trong khi vấn đề là hàng vỡ. |
| 7 | Hệ thống | Sổ cái trả 503 nhưng trợ lý vẫn báo đã hoàn thành công. |
| 8 | Hệ thống | Trợ lý viện dẫn điều 7.2 không tồn tại; thông tin sai xuất hiện trong câu trả lời. |
| 9 | Do người dùng | Khách nhập mã sàn thay cho mã vận đơn; thiếu hướng dẫn là vấn đề cần cải thiện. |
| 10 | Ngữ cảnh | Từ chối đúng điều khoản bất khả kháng nhưng trái kỳ vọng do cam kết 24 giờ trên ứng dụng. |
| 11 | Giới hạn hệ thống | Trợ lý chưa xử lý được tin nhắn âm thanh 40 giây. |
| 12 | Ngầm | Kết quả vẫn đúng nhưng chi phí token tăng gấp 3 suốt 3 tuần mà không ai nhận ra. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi; trả lời chung chung là cách xử lý giới hạn chưa tốt. |
| 14 | Do người dùng | Khách bấm nhầm xác nhận nhận tiền làm yêu cầu bị đóng. |
| 15 | Hệ thống | Trợ lý hoàn 100% thay vì 50%; nhân viên đã phát hiện trước khi gửi. |
| 16 | Ngữ cảnh | Gửi ngay đúng thiết kế nhưng thông báo lúc 2:14 sáng không phù hợp hoàn cảnh. |
| 17 | Ngầm | Bảng giá cũ làm lệch tiền ở 212 đơn trong 9 ngày mà không ai mở lại. |
| 18 | Ngữ cảnh | Hoàn 15.000 đ đúng chính sách nhưng thiếu cách tính khiến khách hiểu sai. |
| 19 | Giới hạn hệ thống | Đơn 14 tháng nằm ngoài cửa sổ dữ liệu 12 tháng. |
| 20 | Hệ thống | Thiếu khóa chống trùng khiến cùng một đơn được hoàn hai lần. |

Phân bố nhãn đề xuất: Do người dùng **4**; Hệ thống **5**; Ngữ cảnh **4**; Giới hạn hệ thống **4**; Ngầm **3**. Đây không phải tỉ lệ đồng thuận.

## Bảng nhãn TV3 và đối chiếu với TV4

Người gắn nhãn 1: TV3, đã điền bản nháp có hỗ trợ Codex từ bảng đề xuất bên trên, chờ tự kiểm tra; chưa có bằng chứng gắn nhãn độc lập. Người gắn nhãn 2: TV4, chưa có bộ nhãn được cung cấp.
Giữ nguyên hai bộ nhãn ban đầu sau khi đối chiếu; chỉ ghi kết quả thảo luận vào cột nhãn thống nhất.

| Ca | Nhãn TV3 (có hỗ trợ AI) | Nhãn TV4 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** Chưa tính vì chưa có hai bộ nhãn thực tế. Công thức: số ca trùng nhãn ban đầu / 20 × 100%; mục tiêu ít nhất 16/20 = 80%.

## Quy tắc phân biệt cho các ca không trùng

Chưa có kết quả đối chiếu để xác định ca bất đồng. Khi có hai bộ nhãn, ghi mỗi ca bất đồng một câu; nếu đồng thuận dưới 80% thì viết lại định nghĩa, vẫn giữ bộ nhãn ban đầu.

- Quy tắc tham khảo cho ca 6, 9: phân loại theo đầu vào sai của khách; cách trợ lý hướng dẫn nằm ở cột khắc phục.
- Quy tắc tham khảo cho ca 13: ngoài phạm vi là giới hạn, dù trợ lý diễn đạt giới hạn chưa rõ.
- Quy tắc tham khảo cho ca 8, 15: thông tin sai đã hiển thị hoặc đã bị phát hiện là hệ thống; không gọi là ngầm.
- Quy tắc tham khảo cho ca 12, 17: sai về chi phí hoặc tiền hoàn chưa bị nhận ra cũng là lỗi ngầm.
- Quy tắc tham khảo cho ca 18: số tiền đúng, kỳ vọng không khớp vì thiếu giải thích là ngữ cảnh.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Đây là phương án đề xuất chờ nhóm duyệt, chưa phải bằng chứng đã triển khai. Các event được đặc tả tại [chi_so.md](chi_so.md); ngưỡng dưới đây là ngưỡng đề xuất.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Đếm yêu cầu có `input_validation_failed` với `reason=wrong_id_type` hằng ngày; cảnh báo khi >2% yêu cầu trong ngày. | Nhận diện mã sàn và tra sang mã vận đơn; không tra được thì hướng dẫn nhập mã đúng. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: `refund_status_notified` báo thành công nhưng không có `refund_ledger_write` thành công cùng `request_id`, `trace_id`, `idempotency_key`; cảnh báo từ 1 ca. | Chỉ báo thành công khi sổ cái xác nhận; hết số lần thử thì báo đang xử lý và chuyển nhân viên; xử lý theo luật dừng giao dịch của pilot. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Hằng tuần kiểm tra các `ticket_reopened` có `reason=amount_dispute`; cảnh báo từ 1 ca mà `audit_sample_checked` xác nhận số tiền đúng. | Thông báo rõ phí 30.000 đ × 50% = 15.000 đ và nơi nhận tiền. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Kiểm tra hằng ngày `handoff_to_staff` có `reason=missing_data`; cảnh báo từ 1 ca thuộc phạm vi pilot. | Chuyển kèm tóm tắt và dữ liệu đã có; loại quốc tế khỏi phạm vi pilot như kế hoạch TV2. | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm toán ngẫu nhiên ít nhất 100 đơn/tuần bằng `audit_sample_checked`, đối chiếu phiên bản bảng giá; cảnh báo khi ≥1% mẫu có số tiền sai. | Xóa bộ nhớ đệm khi bảng giá đổi; ghi phiên bản bảng giá vào trace; rà các đơn bị ảnh hưởng và đối soát tiền. | Kế toán trưởng |

## Việc còn chờ trước khi bàn giao TV4

- TV3 tự kiểm tra nhãn đề xuất và ghi trung thực cách dùng AI trong báo cáo cá nhân.
- Nhận bộ nhãn thực tế của TV4, bảo toàn bộ nhãn ban đầu và ghi rõ quy trình hai người đã thực hiện.
- Tính đồng thuận ban đầu, ghi ca bất đồng và nhãn thống nhất; chưa có bằng chứng thì chưa đánh dấu nhiệm vụ C hoàn thành.
