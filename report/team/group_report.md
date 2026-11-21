# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HongSac
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Quyết định có nên pilot trợ lý hoàn phí LogiX-VN ở Gate 2a hay không, dựa trên chi phí mỗi việc thành công, độ nhạy, bảng lỗi, thiết kế pilot và chỉ số. Cả bộ CSV là dữ liệu giả lập; số có giờ nhân viên ghi `simulated`. Phạm vi đề xuất thu hẹp về `noi_dia` + `hang_nang`.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- A–B: [bang_chi_phi.md](bang_chi_phi.md) · mô hình chi phí từ trace, độ nhạy, giới hạn chạy lại, xem lại 100%.
- C: [bang_loi.md](bang_loi.md) · 20 ca, 5 ca khắc phục; đồng thuận hai người gắn nhãn còn chờ.
- D: [pilot_plan.yaml](pilot_plan.yaml) · ngẫu nhiên theo nhân viên 20+20, 4 luật dừng.
- E: [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- CPS 4.472 đ (`simulated`); cả hệ thống 5.864,65 đ/yêu cầu = 0,489× 12.000 đ (`simulated`). Làm lại ×2 (+51,77%), xem lại ×2 (+40,70%) và lương +25% (+23,12%) là ba yếu tố nhạy nhất.
- Số bất lợi: xem lại 100% làm CPS thành 11.743–12.415 đ (0,979–1,035×); power pilot ở +5 điểm chỉ 64,18%.
- **Đề xuất cuối: Go có điều kiện** (pilot 20+20, `noi_dia` + `hang_nang`), 4 điều kiện có vai trò và ngày.
- Kết quả duyệt chéo từ hội đồng: **chưa có**, điền sau buổi chấm.

## 5. Khó khăn và cách xử lý

Hai bộ nhãn độc lập chưa hoàn tất trước khi viết hồ sơ nên mục 5 ghi "Chưa". Vì không có dữ liệu thật, mọi số chi phí giữ nhãn `simulated` và hồ sơ không viết trợ lý đã nâng chỉ số. Nhiều phần được soạn có hỗ trợ AI; từng thành viên khai và tự kiểm chứng trong báo cáo cá nhân.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Dữ liệu giả lập, không có nhóm đối chứng trong mẫu, ICC 0,02 là giả định, power ở +5 điểm chưa đủ 80%, phút nhân viên chưa đo thật, bảng lỗi chưa có đồng thuận thực. Cải thiện: đo phút và event thật từ ngày đầu pilot, hoàn thành gắn nhãn độc lập, tính lại B3/B4.

## 8. Tài liệu tham khảo

`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`, Google PAIR (năm loại lỗi), các file trong `report/team/`.
