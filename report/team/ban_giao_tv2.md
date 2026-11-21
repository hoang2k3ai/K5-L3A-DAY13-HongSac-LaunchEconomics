# Bàn giao phần TV2 — Kiểm số và thiết kế pilot

Đã chuẩn bị `bang_chi_phi.md`, `pilot_plan.yaml`, báo cáo cá nhân và phần kiểm số/D1 trong `src/lab13.py`.
Phần A/B của TV1 hiện chưa triển khai; các bảng dùng kết quả tính độc lập từ CSV trong chính `lab13.py`, không ghi nhận đã nhận bàn giao.

## 1. TV2 phụ thuộc TV1 ở đâu

| Việc | Có phải chờ TV1 | Cách chốt |
| --- | --- | --- |
| Tính tay A1/A2, kiểm dữ liệu | Không | Tự tính công thức; đối chiếu tổng phút và số thành công |
| Chuẩn bị bảng A2–A4, B1–B4 | Không để tính độc lập; có để chốt số nhóm | Chạy `--kiem-so`, rồi so với `mo_hinh` TV1 |
| Tính 5 câu D1, so sánh cách chia | Không | Dùng baseline/ICC/số người từ đề; `--pilot-only` |
| Chốt phạm vi, retry và luật chi phí | Cần A3/B3/B4 đáng tin | Đã có số độc lập; kiểm lại khi nhận A/B; không tự đổi quy ước |
| Chạy toàn bộ script, chứng minh đổi người viết code | Có | TV1 hoàn thiện A/B, TV2 tự chạy và kiểm từ đầu đến cuối |
| Báo cáo cá nhân, nộp LMS | Không | Mỗi người tự ghi đóng góp thật và tự nộp link |

TV1 cần giữ chữ ký `mo_hinh(runs, reqs, gia_vao, gia_ra, gia_tool, luong_phut, he_so_xem_lai, he_so_lam_lai, max_lan_chay)`.
Hàm phải lọc lượt theo `request_id`, giữ mọi lượt lỗi, không sửa DataFrame gốc; khi cắt lượt thì ca vượt giới hạn chuyển nhân viên, cả hai cột phút bằng 0.
Khối cuối của TV1 cần in đủ bảng A/B; giữ các hàm TV2 và lời gọi `in_d1()` để script cuối in D1.

## 2. Chạy và kiểm tra

Môi trường ảo đã được tạo ở `.venv/` tại gốc repo, nằm trong gitignore. Lệnh chạy trong `src/`:

```powershell
$env:PYTHONIOENCODING = "utf-8"
Set-Location src
../.venv/Scripts/python.exe lab13.py --kiem-so
../.venv/Scripts/python.exe lab13.py --pilot-only
../.venv/Scripts/python.exe -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8-sig')); print('YAML OK')"
```

`--kiem-so` kiểm A/B độc lập và báo rõ chờ TV1 khi A1 hoặc `mo_hinh` chưa triển khai; trạng thái đó không phải A1 ĐẠT.
Khi A/B đã có, cùng lệnh tự kiểm A1 và đối chiếu **15 cấu hình**: 1 gốc, 4 loại, 9 kịch bản đơn và 1 cặp.
Sau đó chạy `../.venv/Scripts/python.exe lab13.py`; nếu không in đủ bảng A/B thì TV1 còn cần bổ sung khối chạy, dù kiểm số hàm đã đạt.

## 3. Số bàn giao cho TV3 và TV4

| Nội dung | Số từ script | Lưu ý |
| --- | --- | --- |
| CPS toàn mẫu | 4.472 đ | simulated, chưa cố định |
| Chi phí cả hệ thống/yêu cầu | 5.864,65 đ | simulated, cộng 12.000 đ mỗi ca không thành công theo đề B3, chưa cố định |
| Phạm vi nội địa + hàng nặng | 982 yêu cầu, 900 thành công; CPS 3.413,90 đ | CPS simulated |
| Có cố định 40 triệu đ/tháng | 4.599 đ/việc ở 45.000 yêu cầu/tháng; 5.784 đ khi còn 22.500 | simulated; CPS chưa gồm luồng nhân viên |
| 3 yếu tố nhạy nhất | Làm lại +51,77%; xem lại +40,70%; lương +23,12% | simulated, theo mức thay đổi đầu vào của đề |
| B3 | Giới hạn 2 lượt: hệ thống 6.901.220 đ/1.200 yêu cầu | simulated; kết quả toàn mẫu, cần đo lại trên phạm vi pilot |
| B4 | 11.743 đ với 9 phút làm lại; 12.415 đ với 15,3 phút | simulated; xem lại 100% gần/hơn baseline, chưa cố định |
| D1 | 20+20 người, 299 yêu cầu/người, 5.980 thực/nhánh, khoảng 859,20 hiệu dụng | DE 6,96; MDE +6 điểm; power chỉ 0,6418 nếu tác động +5 điểm |
| Mở lại | 51/1.200=4,25%; phạm vi 39/982=3,9715% | từ dữ liệu giả lập; không phải chênh với đối chứng |
| Pilot | 4 luật dừng; ngày quyết định đề xuất 05/01/2027 | ngày và ngưỡng là đề xuất chờ duyệt; cần đủ 40 người/12 depot |

TV3 dùng số B trong rủi ro, đặc tả đủ event để tính luật dừng và phút thật; TV4 ghi rõ đánh đổi MDE và chi phí xem lại 100% trong hồ sơ.
Chưa có chữ ký chấp thuận hoặc roster thực; không ghi các điều kiện đã hoàn tất. Không tự chấm hội đồng hoặc tạo hai bộ nhãn độc lập.

## 4. Cách nhận code TV1 mà giữ phần TV2

Trước khi pull, commit riêng các file TV2. Từ gốc repo:

```powershell
git status --short
git add -- src/lab13.py report/team/bang_chi_phi.md report/team/pilot_plan.yaml report/team/2A202603499_NguyenBaThanh.md report/team/ban_giao_tv2.md report/team/kiem_chung_tv2.txt TEAM.md
git commit -m "Complete TV2 cost checks and pilot design"
git branch --show-current
git pull --no-rebase
```

Các lệnh trên là hướng dẫn, chưa được thực hiện tự động. `git pull --no-rebase` giả định nhánh hiện tại đã theo dõi đúng nhánh nhóm; nếu chưa thì kiểm tra `git branch -vv` và chốt nhánh với nhóm trước.
Cùng sửa `src/lab13.py` có thể xung đột: giữ A/B TV1, giữ hàm kiểm số/D1 và CLI TV2, ghép khối chạy rồi chạy lại các kiểm tra.
Không chọn ghi đè nguyên file theo một phía; không dùng `reset --hard`, `clean -fd` hoặc bỏ stash khi chưa kiểm tra nội dung.

## 5. Checklist cá nhân cần làm thật

- [ ] Xác nhận tên Nguyễn Bá Thành, MSSV 2A202603499 và bổ sung email/GitHub.
- [ ] Tự tính lại ít nhất 1 phép tính A2; giải thích vì sao không cộng phí chạy lại hai lần.
- [ ] Tự chạy `--kiem-so` và `--pilot-only`; đọc kết quả thay vì chỉ chép số.
- [ ] Nhận code TV1, chạy A1 và 15 cấu hình đối chiếu; chạy toàn bộ script trên máy mình.
- [ ] Thống nhất MDE +6, phạm vi pilot, ngưỡng và ngày đề xuất với nhóm; TV4 cập nhật hồ sơ.
- [ ] Commit phần đóng góp thật, ghi mã commit vào báo cáo; phối hợp TV4 cập nhật TEAM.
- [ ] Kiểm tra repo GitHub mở được rồi tự nộp cùng link nhóm trên LMS trước hạn của lớp.

Nguồn: README, RULES, CHECKPOINTS, RUBRIC, SUBMISSION, hướng dẫn chi tiết và đề Word trong repo. Các thao tác tự kiểm tra/nộp bài chỉ đánh dấu sau khi thực hiện.
