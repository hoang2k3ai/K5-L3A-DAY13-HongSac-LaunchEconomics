# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |        |      |       |        | Người viết code A–B |
|   2 | Nguyễn Bá Thành | 2A202603499 | 26ai.thanhnb3@vinuni.edu.vn | Nguyen-Ba-Thanh | TV2 · Kiểm số và thiết kế pilot; tiếp quản code sau giải lao |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Thành viên 1 · Người viết code A–B

### Phần việc phụ trách

- Xây dựng mô hình chi phí từ trace và chạy các kịch bản độ nhạy trong `src/lab13.py`.

### Đóng góp cụ thể

- Triển khai A1–A4 và B1–B4. Chạy script trong môi trường `.venv` và chuẩn bị số liệu để TV2 kiểm tra, tiếp quản phần D1.

### Bằng chứng

- Ba phép thử A1 đều ĐẠT. Kết quả A–B được ghi trong `report/team/bang_chi_phi.md`. Bản ghép đã được Codex chạy lại trong môi trường máy TV2: A1 đạt, in hết A–B và D1; TV2 tự giải thích kết quả trước khi nộp.

## NguyenBaThanh-2A202603499 · TV2

Vai trò: người kiểm số và thiết kế pilot; thông tin liên hệ ghi ở dòng TV2 trong bảng thành viên.

### Phần việc phụ trách

- Trước giải lao: tính tay ít nhất 1 kết quả; dùng số TV1 để chốt A2–A4, B1–B4 và xếp hạng độ nhạy.
- Sau giải lao: tiếp quản code, tự chạy kiểm số, làm đủ 5 câu D1 và 5 câu D2; thiết kế đối chứng và ít nhất 3 luật dừng.

### Đóng góp cụ thể

- Hoàn thiện bảng A1–A4/B1–B4 và phép tính đối chiếu từ CSV; bổ sung D1 a–e, kiểm tỷ lệ mở lại D3 và chế độ kiểm số trong `src/lab13.py` với hỗ trợ Codex.
- Thiết kế pilot chia ngẫu nhiên 20+20 nhân viên, 299 yêu cầu/người, 5 câu D2, 4 luật dừng và rollback; ghi rõ power khoảng 64,18% nếu tác động chỉ +5 điểm phần trăm.
- Đã nhận A/B của TV1 từ `97c5410`, ghép tại `78fb538`; chạy lại script bằng Codex trên môi trường máy TV2, xác nhận 3 phép thử A1 và 15 cấu hình × 9 trường số khớp tính độc lập. Báo cáo cá nhân khai công cụ AI và cách kiểm chứng.

### Bằng chứng

- [Bảng A–B](report/team/bang_chi_phi.md): CPS 4.472 đ; giới hạn 2 lượt có chi phí hệ thống 6.901.220 đ (`simulated`).
- [Pilot plan](report/team/pilot_plan.yaml): 20 cụm/nhánh, 299 yêu cầu/người, 5.980 yêu cầu thực/nhánh, khoảng 859,20 hiệu dụng.
- [Báo cáo cá nhân](report/team/2A202603499_NguyenBaThanh.md) và [bàn giao TV2](report/team/ban_giao_tv2.md).
