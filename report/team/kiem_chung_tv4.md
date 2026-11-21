# Đối chiếu số trong hồ sơ launch v0 · TV4

Ngày 21/11/2026. Mỗi số trong `ho_so_launch_v0.md` được đối chiếu hai đường: (1) kết quả `cd src && python lab13.py`; (2) tính lại độc lập từ `src/logix_runs.csv` và `src/logix_requests.csv` bằng một script ngắn chỉ dùng thư viện chuẩn `csv` (không dùng `lab13.py`). Không sửa hai CSV. Toàn bộ là dữ liệu giả lập; số có giờ nhân viên là `simulated`.

| Mục hồ sơ | Số | Cách tính tay / từ CSV | `lab13.py` | Khớp |
| --- | --- | --- | --- | --- |
| 1 | CPS 4.472 đ | (245.585,13 + 84.000 + (890 + 1.132) × 2.000) / 978 = 4.373.585,13 / 978 = 4.471,97 | 4.471,97 | Có |
| 1 | Gấp 16,28× hóa đơn 274,7 đ | (245.585,13 + 84.000) / 1.200 = 274,65; 4.471,97 / 274,65 = 16,28 | 16,3 | Có |
| 1 | Quốc tế 22.515 đ = 1,876× | A3 theo loại; 22.515 / 12.000 | 22.515; 1,88× | Có |
| 1 | + cố định 4.599 / 5.784 đ | A4: 40 triệu đ/tháng chia số việc thành công/tháng | 4.599; 5.784 | Có |
| 2 | Làm lại +51,77%, xem lại +40,70% | 2.264.000 / 4.373.585 = 51,77%; 1.780.000 / 4.373.585 = 40,70% | +51,8%; +40,7% | Có |
| 2 | Lương +23,12%; token ×2 +5,62% | B1 | +23,1%; +5,6% | Có |
| 2 | Giờ nhân viên 92,46% | (890 + 1.132) × 2.000 / 4.373.585 | (tính từ A2) | Có |
| 3 | Cả hệ thống 5.864,65 đ = 0,489× | (4.373.585,13 + 222 × 12.000) / 1.200 = 5.864,65; / 12.000 = 0,4887 | B3: 7.037.585 đ (3 lần) | Có |
| 3 | Xem lại 100%: 11.743 đ / 12.415 đ | B4; 1.132 / 74 = 15,2973 phút | 0,98×; 1,03× | Có |
| 3 | 2 lượt rẻ nhất: 6.901.220 đ | B3 | 6.901.220 | Có |
| 4 | 994/1.200 = 82,83% | đếm `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0` | | Có |
| 4 | 48/177 = 27,12% | trong `duoc_xem_lai=1`, `sua` hoặc `bo` | | Có |
| 4 | 51/1.200 = 4,25% | đếm `mo_lai_trong_7_ngay=1` | 4,2500% | Có |
| 6 | 5.980/nhánh, hiệu dụng ≈859, DE 6,96, power 64,18% | D1 e | 5.980; 859,1954; 6,96; 64,18% | Có |
| 7 | 48/982 = 4,89% | ca làm lại trong `noi_dia` + `hang_nang` / 982 | (D3: 39/982 mở lại) | Có |
| 7 | Hòa vốn 5,122 và 4,803 phút | (12.000 × 900 − token/tool − 48 × L × 2.000) / (948 × 2.000), L = 9 và 15,2973 | | Có |

Kết luận: 16/16 số khớp. Ba phép thử A1 in "ĐẠT". Script đối chiếu độc lập chạy bằng `python3 -I` ngoài thư mục `src/`.

Giới hạn: kiểm số này chỉ chứng minh hồ sơ khớp mô hình của lab với dữ liệu giả lập, không chứng minh tác động thật của trợ lý.
