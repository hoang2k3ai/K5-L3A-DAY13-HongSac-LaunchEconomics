# Báo cáo cá nhân — Lê Nhật Linh — 2A202603514

Bản nháp có hỗ trợ Codex; thành viên cần tự đọc, kiểm tra và xác nhận trước khi nộp. Các kết quả dưới đây mô tả tài liệu và phép kiểm đã thực hiện trong phiên hỗ trợ, không xác nhận hoạt động gắn nhãn độc lập hay pilot đã diễn ra.

## 1. Thông tin thành viên

- Họ tên: Lê Nhật Linh.
- MSSV: 2A202603514.
- Email: 26ai.linhln@vinuni.edu.vn.
- Vai trong nhóm: TV3 · Phân tích lỗi và chỉ số; người gắn nhãn 1.

## 2. Phần việc phụ trách

- Nhiệm vụ C: đọc tiêu chí lỗi, chuẩn bị nhãn 20 ca, đối chiếu TV4, tổng hợp đồng thuận và bảng khắc phục 5 ca thuộc 5 loại.
- Nhiệm vụ E1–E2: tính 3 chỉ số, đề xuất thêm 2 chỉ số, đặc tả ít nhất 6 event có `trace_id` và 2 rủi ro lấy số từ phần B.
- Bàn giao kết quả C và E1–E2 để TV4 tổng hợp hồ sơ launch.

## 3. Đóng góp cụ thể

- Với hỗ trợ Codex, soạn nhãn đề xuất và giải thích cho 20 ca theo nguyên nhân gốc; điền cột TV3 và 5 phương án phát hiện, khắc phục, phân công vai trò trong `bang_loi.md`.
- Hoàn thiện `chi_so.md`: 3 chỉ số từ CSV, 2 chỉ số đề xuất, 13 event có `trace_id` và liên kết event với công thức tính.
- Tổng hợp 2 rủi ro từ B1/B4 của TV1–TV2; giữ nhãn `simulated`, ghi rõ phạm vi và điều kiện áp dụng.
- Đã đối chiếu với TV4: 19/20 trùng, ca 13 thống nhất "Giới hạn hệ thống"; chi tiết trong `bang_loi.md`.

## 4. Bằng chứng

| Sản phẩm | Kết quả và cách kiểm tra |
| --- | --- |
| [Bảng lỗi](bang_loi.md) | 20 nhãn TV3 có hỗ trợ AI kèm lý do; 5 ca khắc phục đại diện đủ 5 loại; cột TV4 và đối chiếu chưa điền. |
| [Chỉ số](chi_so.md) | Chỉ số chính: 994/1.200 × 100 = **82,83%**; bỏ qua gợi ý: 48/177 × 100 = **27,12%**; mở lại: 51/1.200 × 100 = **4,25%**. |
| [Đặc tả event](chi_so.md) | 13 event đều có `trace_id`, nguồn tạo, thuộc tính và thời điểm; mỗi chỉ số đã chỉ ra event cần dùng. Đây là đặc tả đề xuất, chưa có bằng chứng ghi log thực tế. |
| [Rủi ro kinh tế](chi_so.md) | Làm lại gấp đôi: CPS **6.787 đ, +51,77% (simulated)**; xem lại 100%: **11.743 đ** hoặc **12.415 đ (simulated)** tùy phút làm lại, lấy từ bảng B của nhóm. |
| [Thông tin đóng góp](../../TEAM.md) | Đã ghi vai trò, sản phẩm, bằng chứng và phần còn chờ của TV3. |

Toàn bộ CSV là dữ liệu giả lập của lab. Chỉ số 82,83% là mô tả đợt chạy thử, không chứng minh trợ lý làm tăng kết quả so với baseline thiết kế 70%.

## 5. Công cụ AI đã dùng

- Công cụ: Codex, dùng để đọc đề, gợi ý phân loại và lý do, soạn bảng khắc phục, chỉ số, event, rủi ro và báo cáo.
- Kiểm chứng trong phiên: Codex đếm lại CSV bằng PowerShell `Import-Csv`, xác nhận 1.200 yêu cầu, 994 đạt chỉ số chính, 177 được xem lại, 48 sửa/bỏ và 51 mở lại; phép chia được ghi rõ ở mục 4.
- Số rủi ro được đối chiếu với [bảng chi phí](bang_chi_phi.md) và [kế hoạch TV2](pilot_plan.yaml). Kiểm tra đủ 20 dòng nhãn, 5 ca khắc phục, 13 event có `trace_id` và định dạng bằng `git diff --check`.
- Nhãn TV3 hiện được soạn từ gợi ý AI và tài liệu tham khảo. Không coi bản nháp này là bằng chứng hai người đã gắn nhãn độc lập; không điền thay TV4 hoặc tự tạo tỉ lệ đồng thuận.
- Việc thành viên cần tự làm trước khi nộp: đọc lại 20 tình huống, kiểm tra lý do phân loại và các phép chia; ghi nhận trung thực quy trình đã thực hiện khi đối chiếu TV4.

## 6. Tự đánh giá

- Đã có bản nháp phần nội dung TV3 để rà soát: bảng nhãn, khắc phục, chỉ số, event và rủi ro kinh tế.
- Nhiệm vụ C chưa hoàn tất: cần bộ nhãn thực tế của TV4 và kết quả đối chiếu; chưa có bằng chứng để ghi đạt ngưỡng đồng thuận 80%.
- Chưa có dữ liệu cho 2 chỉ số đề xuất, event triển khai hoặc kết quả pilot; không suy diễn những nội dung này thành kết quả đã đo.
- Thành viên tự xác nhận mức độ hiểu bài và hoàn thiện tự đánh giá sau khi đọc, kiểm tra tài liệu.
