# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HongSac · Lớp: L3A · Phạm vi đề xuất: chỉ `noi_dia` + `hang_nang` (982/1.200 yêu cầu mẫu), loại `quoc_te` và `doi_tac`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | CPS toàn mẫu **4.472 đ** (gấp 16,28× hóa đơn token+tool/yêu cầu 274,7 đ). Theo loại: nội địa 2.696 đ; hàng nặng 8.221 đ; **quốc tế 22.515 đ = 1,876× 12.000 đ** nên loại; đối tác 10.215 đ, thành công chỉ 54,41% nên loại. Phạm vi + cố định 40 triệu đ/tháng: 4.599 đ (45.000 yêu cầu/tháng) hoặc 5.784 đ (22.500). Chưa gồm luồng nhân viên cho ca thất bại. | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: **+51,77%** (6.787 đ) · xem lại ×2: **+40,70%** (6.292 đ) · lương +25%: **+23,12%**. Giờ nhân viên chiếm 92,46% chi phí; giá token ×2 chỉ +5,62%. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống (gồm 222 ca thất bại × 12.000 đ): **5.864,65 đ/yêu cầu = 0,489×** baseline 12.000 đ. **Số bất lợi:** nếu phải xem lại 100% gợi ý, CPS = 11.743 đ (**0,979×**) với 9 phút làm lại và 12.415 đ (**1,035×**, tức đắt hơn tự làm) với 15,3 phút. Giới hạn 2 lượt rẻ nhất cả hệ thống: 6.901.220 đ. | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, dùng, an toàn | Chính: đóng ≤24h và không mở lại 7 ngày **82,83%** (994/1.200). Dùng: sửa/bỏ gợi ý **27,12%** (48/177). An toàn: mở lại 7 ngày **4,25%** (51/1.200). Đây là số của mẫu chạy thử không có đối chứng; không kết luận trợ lý đã nâng chỉ số. | Giả lập | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; **5 ca khắc phục** (ca 9, 7, 18, 4, 17), mỗi dòng có event, ngưỡng và vai trò. Nhãn TV3 và TV4 đều có AI hỗ trợ; TV4 đã rà soát. Đồng thuận ban đầu **19/20 = 95%** (≥16/20); ca 13 bất đồng, đã thống nhất "Giới hạn hệ thống" theo quy tắc ghi trong `bang_loi.md`. | Chưa | Trưởng nhóm CSKH |
| 6 · Pilot plan | Ngẫu nhiên theo nhân viên, **20 + 20** nhân viên, 299 yêu cầu/người = **5.980/nhánh**, hiệu dụng ≈859 (DE 6,96, ICC 0,02 giả định). Đủ cho +6 điểm; power ở +5 điểm chỉ **64,18%** (số bất lợi, đã ký đánh đổi MDE trước khi bắt đầu). 4 luật dừng, COO có quyền tắt cờ trong 30 phút, quyết định 05/01/2027. | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | (a) Làm lại ×2: CPS 4.472 → 6.787 đ (+51,77%); mốc dừng CPS >8.000 đ hai tuần liền, làm lại hiện 48/982 = 4,89% (cảnh báo >7%). (b) Xem lại 100% kéo dài: 0,979–1,035× tự làm; hòa vốn ở 5,122 hoặc 4,803 phút xem lại/lượt. | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** (chỉ cho pilot 20+20 trong phạm vi `noi_dia` + `hang_nang`; chưa phải duyệt chạy chính thức). Lý do: CPS và chi phí cả hệ thống thấp hơn 12.000 đ trên dữ liệu giả lập, nhưng toàn bộ phụ thuộc giờ nhân viên giả lập và sẽ đảo chiều (1,035×) nếu phải xem lại 100% lâu dài.

- Điều kiện 1 · COO ký đánh đổi MDE +6 điểm, kinh phí pha xem lại 100% và roster đủ 40 nhân viên/12 depot · Giám đốc vận hành · **22/11/2026**.
- Điều kiện 2 · Kiểm thử khóa chống trùng, xác nhận sổ cái và nút tắt cờ; xác minh đủ event cho cả hai nhánh · Kỹ sư trưởng agent · **23/11/2026**.
- Điều kiện 3 · Thay phút giả lập bằng phút đo thật từ ngày đầu và tính lại CPS, B3, B4; vượt ngưỡng dừng thì thu hẹp về nội địa · PM trợ lý hoàn phí · **sau bước 10% (30/11/2026)**.
- Điều kiện 4 · Triển khai 5 cách khắc phục ở mục 5 và đo lại đồng thuận khi có nhãn người gắn thêm · Trưởng nhóm CSKH · **trước khi chuyển bước 25%**.
