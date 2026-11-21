# Bảng chi phí · Nhiệm vụ A và B

TV2 tính độc lập từ CSV bằng `kiem_so_doc_lap()` trong `src/lab13.py`; chạy `python lab13.py --kiem-so` trong `src/`.
Số tiền làm tròn đến đồng, hóa đơn/yêu cầu giữ 1 chữ số thập phân. Toàn bộ dữ liệu là giả lập; kết quả có giờ nhân viên ghi `simulated`.
**Bàn giao đã kiểm chứng ngày 21/11/2026:** nhận A–B của TV1 từ commit `97c5410`; 3 phép thử A1 và 15 cấu hình đối chiếu với `mo_hinh` đều ĐẠT. Script ghép đã chạy hết A–B và D1 trong môi trường máy TV2 qua Codex.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Tính tay đối chiếu của TV2 | Trạng thái code TV1 |
| --- | --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | `(1 − 0,2²) / 0,8 = 1,20` | ĐẠT, khớp tính tay |
| Số lần chạy trung bình, chạy đến khi đúng | `1 / 0,8 = 1,25` | ĐẠT, khớp tính tay |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | `[(1 − 0,2³) / 0,8] / (1 − 0,2³) = 1,25` | ĐẠT, khớp tính tay |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ), trừ dòng đếm việc | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | Tổng token vào × 26/1.000 + token ra × 130/1.000, mọi lần chạy | trace giả lập |
| Tool | 84.000 | 5.600 lần gọi × 15 đ | trace giả lập |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | Token + tool với `attempt > 1`; đã nằm trong hai dòng trên | trace giả lập |
| Xem lại | 1.780.000 | 890 phút `phut_xem_lai_simulated` × 2.000 đ | simulated |
| Làm lại | 2.264.000 | 1.132 phút `phut_lam_lai_simulated` × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đếm từ dữ liệu giả lập |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585,132 / 978 | simulated |
| Hóa đơn token và tool chia cho số yêu cầu | 274,7 | 329.585,132 / 1.200 | trace giả lập |

- CPS gấp **16,28 lần** hóa đơn/yêu cầu (`simulated`); tử số tính cả lần chạy lỗi, mẫu số chỉ có **978** việc thành công.
- Làm lại lớn nhất: **51,77%**; xem lại **40,70%**; tổng giờ nhân viên **92,46%** chi phí (`simulated`).

### Phép tính tay đối chiếu của TV2

`(245.585,132 + 5.600 × 15 + 890 × 2.000 + 1.132 × 2.000) / 978 = 4.471,9684 đ/việc thành công` (`simulated`).
Không cộng thêm **93.804 đ** chạy lại lần nữa: token và tool đã bao gồm toàn bộ **1.624** lượt.

### So sánh với nhân viên tự làm

Theo quy ước B3: `(4.373.585,132 + 222 × 12.000) / 1.200 = 5.864,65 đ/yêu cầu = 0,489×` baseline (`simulated`), chưa có cố định.
**222 = 74** ca làm lại + **148** ca chuyển nhân viên; đề B3 cộng 12.000 đ cho mọi ca không thành công ngoài chi phí A2.
Không dùng riêng `4.472 / 12.000` để khẳng định mức tiết kiệm cả hệ thống vì mẫu số khác nhau.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | CPS (đ, simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 783/824 = 95,02% | 916/824 = 1,112 | 2.696 | 0,225× |
| hang_nang | 158 | 117/158 = 74,05% | 232/158 = 1,468 | 8.221 | 0,685× |
| quoc_te | 150 | 41/150 = 27,33% | 348/150 = 2,320 | 22.515 | 1,876× |
| doi_tac | 68 | 37/68 = 54,41% | 128/68 = 1,882 | 10.215 | 0,851× |

- `quoc_te` không đáng nhận: **22.515 đ/việc = 1,876×** baseline (`simulated`), **2,32** lượt/yêu cầu nhưng chỉ **27,33%** thành công.
- Tỷ lệ `ok` của `quoc_te` theo lượt: **45/150 = 30,00%**, **12/105 = 11,43%**, **2/93 = 2,15%**; thêm lượt không xử lý được nguyên nhân lỗi. Đây là nhóm còn đi đến từng lượt, không phải hiệu quả nhân quả của chạy lại.
- Chọn `noi_dia + hang_nang`: **982** yêu cầu, **900** thành công; loại `doi_tac` vì thành công **54,41%** và điều khoản riêng, dù CPS **0,851×** (`simulated`).

## A4 · Chi phí cố định (noi_dia + hang_nang)

Trong phạm vi: `2.110.687,298 + 961.825,976 = 3.072.513,274 đ`; CPS `3.072.513,274 / 900 = 3.413,90 đ` (`simulated`).
Khối lượng là tổng yêu cầu toàn công ty; số thành công trong phạm vi/tháng = khối lượng × **900/1.200**, không dùng 900/982.

| Khối lượng toàn công ty | Thành công trong phạm vi/tháng | Cố định/việc (đ) | CPS + cố định (đ, simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,383× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 | 5.784 | 0,482× |

- Cố định **40 triệu đ/tháng** chưa đổi kết luận CPS ở **45.000** hay **22.500** yêu cầu/tháng (`simulated`); A4 chưa cộng luồng nhân viên cho ca không thành công và ngoài phạm vi.
- Pilot phải đo chi phí cả hệ thống và phân bổ đủ cố định **40 triệu đ/tháng**; không suy diễn A4 thành tổng tiết kiệm công ty.

## B1 · Đổi từng yếu tố

Mốc A2: **4.471,9684 đ** (`simulated`); tính phần trăm trên số chưa làm tròn. Mọi CPS và thay đổi dưới đây là `simulated`.

| Kịch bản | Cách tính | CPS (đ, simulated) | Thay đổi (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | Giá vào 52, ra 260 đ/1.000 token; tool giữ 15 đ | 4.723 | +5,62% |
| Giá token giảm một nửa | Giá vào 13, ra 65 đ/1.000 token | 4.346 | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại × 0,5 | 3.562 | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2; mẫu số giữ nguyên | 6.787 | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại × 0,5 | 3.315 | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ/phút cho xem lại và làm lại | 5.506 | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; yêu cầu cần > 2 lượt chuyển nhân viên, hai cột phút về 0 | 4.237 | −5,25% |
| Chỉ cho chạy 1 lần | Tương tự với giới hạn 1 | 4.111 | −8,07% |

## B2 · Đổi một cặp và xếp hạng

- Token và xem lại cùng gấp đôi: **6.543 đ**, tăng **46,31%**, bằng tổng hai tác động riêng trước làm tròn (`simulated`); mẫu số giữ **978**.
- Xếp theo tác động của các kịch bản đề yêu cầu: **1. Làm lại +51,77% · 2. Xem lại +40,70% · 3. Lương +23,12%** (`simulated`); các đầu vào không cùng mức tăng.
- Kiểm tra trên số chưa làm tròn: giảm nửa token/xem lại/làm lại làm CPS giảm đúng **1/2** mức tăng khi gấp đôi từng khoản (`simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Theo đề: `cả hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công`. Chi phí là `simulated`, chưa có cố định.

| Giới hạn | Tổng trợ lý (đ, simulated) | Không thành công | Cả hệ thống (đ, simulated) | CPS (đ, simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- **2 lần** rẻ nhất cả hệ thống: **6.901.220 đ**, thấp hơn 3 lần **136.365 đ**, thấp hơn 1 lần **548.560 đ** (`simulated`).
- CPS thấp nhất ở **1 lần** nhưng chuyển thêm **85** yêu cầu so với 2 lần (**97** so với 3 lần); tối ưu CPS riêng không tối ưu chi phí công ty.

## B4 · Nếu phải xem lại tất cả

Giữ tối đa **3** lượt như đề B4; B3 là kịch bản riêng. Trong **982** yêu cầu có **948** yêu cầu có ít nhất 1 lượt `ok`, **48** ca làm lại, **900** thành công.

| Thành phần | Phép tính | Chi phí (đ) | Nhãn |
| --- | --- | ---: | --- |
| Token + tool | Mọi lượt của 982 yêu cầu | 224.513 | trace giả lập |
| Xem lại 100% câu trả lời chạy ok | 948 × 5 × 2.000 | 9.480.000 | simulated, giả định B4 |
| Làm lại theo đề | 48 × 9 × 2.000 | 864.000 | simulated, giả định B4 |
| Tổng | 224.513,274 + 9.480.000 + 864.000 | 10.568.513 | simulated |
| CPS | 10.568.513,274 / 900 | 11.743 | simulated |

- Với **9 phút** làm lại: **11.743 đ = 0,979×** baseline; dùng **15,3 phút**: **12.415 đ = 1,035×** (`simulated`), chưa có cố định và luồng chuyển nhân viên.
- CSV có trung bình **1.132/74 = 15,2973 phút/ca** (`simulated`); dùng số chính xác cho **12.414,50 đ**. Mức **12.414 đ** trong hướng dẫn là xấp xỉ; làm tròn đến đồng ở đây cho **12.415 đ**.
- Pilot phải đo phút thật, giảm xem lại an toàn: hòa vốn CPS ở **5,122 phút/lượt** với 9 phút làm lại, hoặc **4,803 phút/lượt** với 15,3 phút (`simulated`); xem lại 100% không tiết kiệm dài hạn.

## Bằng chứng đối chiếu với TV1

- Nguồn: hai CSV gốc; `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và đề Word.
- `python lab13.py --kiem-so` kiểm tổng phút, mẫu số, quan hệ gấp đôi/giảm nửa và B2; đã đối chiếu **15** cấu hình với code TV1, tất cả khớp ở sai số tính số thực.
- Đã chốt **3** phép thử A1, **15** cấu hình; `python lab13.py` chạy từ đầu đến cuối và in đủ A2–A4, B1–B4, D1. Output lưu tại [kiem_chung_tv2.txt](kiem_chung_tv2.txt).
