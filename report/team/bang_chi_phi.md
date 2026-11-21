# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,13 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000,00 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,49 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585,13 | | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.471,97 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | | |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (simulated).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Làm lại chiếm **51,8%** (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× (simulated) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× (simulated) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× (simulated) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× (simulated) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te` có chi phí **1,88×** mức nhân viên tự làm (simulated). Tỷ lệ lượt chạy `ok` giảm từ **30,0%** ở lần đầu xuống **11,4%** và **2,2%** ở lần hai và ba.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× (simulated) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Ở 100% và 50% khối lượng, chi phí sau khi cộng cố định lần lượt là **4.599 đ** và **5.784 đ/việc** (simulated), đều dưới 12.000 đ.

## B1 · Đổi từng yếu tố

Các số chi phí và phần trăm thay đổi trong bảng dưới đây là `simulated`.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc (+46,3%)** (simulated).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất. 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương (+23,1%). Các mức thay đổi đều là simulated.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Các số chi phí và phần trăm thay đổi trong bảng dưới đây là `simulated`.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **2 lần** rẻ nhất cho cả hệ thống (6.901.220 đ). **1 lần** cho CPS thấp nhất (4.111 đ) nhưng có thêm 85 yêu cầu không thành công so với 2 lần. Chi phí là simulated.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 948 yêu cầu xem lại và 48 ca làm lại, chi phí là **11.743 đ/việc (0,98×)** nếu làm lại 9 phút/ca và **12.415 đ/việc (1,03×)** nếu làm lại 15,3 phút/ca (simulated).
- Kết quả này nói gì về thứ pilot cần học được? Pilot cần đo phút xem lại và tỷ lệ xem lại có thể giảm an toàn. Với 5 phút xem lại mỗi lượt, chi phí đã ở sát hoặc vượt mốc **12.000 đ/việc** (simulated).
