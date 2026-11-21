# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

TV3 · Bản đặc tả đề xuất có hỗ trợ Codex. Toàn bộ CSV là dữ liệu giả lập của lab; các event dưới đây là yêu cầu ghi log cho pilot, chưa phải event đã được triển khai.
Nguồn: hai CSV trong `src/`, [bảng chi phí TV1–TV2](bang_chi_phi.md), [pilot plan TV2](pilot_plan.yaml) và mục E của [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0` / tổng yêu cầu | 994/1.200 × 100 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong yêu cầu `duoc_xem_lai=1`: số có `quyet_dinh_xem_lai` là `sua` hoặc `bo` / tổng yêu cầu được xem lại | 48/177 × 100 = **27,12%** |
| An toàn | Tỉ lệ mở lại 7 ngày, đại diện lỗi lọt đến khách theo lab | Số yêu cầu có `mo_lai_trong_7_ngay=1` / tổng yêu cầu | 51/1.200 × 100 = **4,25%** |
| Dùng, tự đề xuất | Tỉ lệ yêu cầu được mở trợ lý | Số `request_id` có ít nhất 1 `agent_opened` / mọi yêu cầu đủ điều kiện của nhánh can thiệp trong kỳ | Chưa tính; CSV chưa có event mở trợ lý |
| An toàn, tự đề xuất | Tỉ lệ đơn hoàn sai tiền trong mẫu kiểm toán | Số đơn có `actual_refund_amount != expected_refund_amount` / số đơn đã kiểm toán, mỗi đơn tính một lần | Chưa tính; CSV chưa có dữ liệu kiểm toán tiền |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

**Cách tính và kiểm chứng:** đếm trực tiếp CSV thu được 1.200 yêu cầu, 994 đạt chỉ số chính, 177 được xem lại, 48 sửa/bỏ và 51 mở lại; tính tay theo các phân số trong bảng. Đã kiểm lại số đếm bằng PowerShell `Import-Csv`, không sửa CSV.
Chỉ số chính 82,83% mô tả mẫu chạy thử, không thay baseline thiết kế 70% và không chứng minh tác động của trợ lý.
Mở lại là chỉ số đại diện: không phải mọi ca mở lại đều do trợ lý sai và lỗi ngầm có thể không làm khách mở lại, nên cần thêm kiểm toán tiền.

**Quy tắc đo pilot:** tính riêng từng nhánh trên phạm vi `noi_dia + hang_nang`, theo nhánh ngẫu nhiên ban đầu, kể cả ca không mở trợ lý hoặc chuyển nhân viên. Không dùng 1.200 yêu cầu của mẫu làm mẫu số pilot.
Theo `pilot_plan.yaml`, chỉ số chính dùng cohort đã đủ 24 giờ để đóng và 7 ngày theo dõi sau đóng; thiếu theo dõi không gán là không mở lại. Tỉ lệ mở lại dùng cohort trưởng thành; cửa sổ an toàn và cỡ mẫu tối thiểu theo kế hoạch TV2.
Nếu không có yêu cầu được xem lại hoặc đơn kiểm toán thì ghi thiếu mẫu, không ghi 0%. Quyết định xem lại chưa ghi nhận là thiếu dữ liệu, không tự tính là giữ gợi ý.

## Danh sách event

Mọi event có `event_id`, `request_id`, `trace_id`, `staff_id`, `depot`, `arm`, `event_time` (UTC); `staff_id` có thể chưa được gán tại lúc khách gửi, phải bổ sung khi phân công. `arm` lấy từ roster ngẫu nhiên, không suy ra từ việc có mở trợ lý.
Tạo `trace_id` ở lúc nhận yêu cầu cho cả hai nhánh; không tạo lượt chạy agent giả cho đối chứng. Nối các lần chạy và sự kiện hậu kỳ qua `request_id`, lưu thêm `run_trace_id` khi trace từng lượt khác nhau.
Khử event gửi trùng bằng `event_id`; tính chỉ số theo `request_id`, không đếm số event hay số lượt chạy thành số yêu cầu.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `trace_id`, `loai`, `eligible`, `created_at`, `arm` | Khi nhận yêu cầu, cả hai nhánh |
| `agent_opened` | Giao diện nhân viên | `trace_id`, `staff_id`, `arm` | Khi nhân viên mở trợ lý cho yêu cầu |
| `agent_run_completed` | Agent | `trace_id`, `run_trace_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `tariff_version` | Sau mọi lượt, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `trace_id`, `suggestion_id`, `suggested_amount` | Khi gợi ý thực sự hiển thị |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `suggestion_id`, `decision=giu/sua/bo`, `review_started_at`, `review_ended_at`, `review_minutes`, `reason` | Khi chốt quyết định xem lại |
| `staff_rework_completed` | Giao diện nhân viên | `trace_id`, `rework_started_at`, `rework_ended_at`, `rework_minutes`, `reason` | Khi nhân viên hoàn thành làm lại |
| `handoff_to_staff` | Agent/điều phối | `trace_id`, `reason`, `summary`, `attempt` | Khi chuyển nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `idempotency_key`, `ledger_transaction_id`, `amount`, `result` | Sau mỗi lần ghi sổ, cả thành công và lỗi |
| `refund_status_notified` | Dịch vụ thông báo | `trace_id`, `idempotency_key`, `notified_status`, `channel` | Khi gửi trạng thái hoàn tiền cho khách |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `closed_at`, `resolution` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `reopened_at`, `reason` | Khi yêu cầu mở lại |
| `audit_sample_checked` | Công cụ kiểm toán/kế toán | `trace_id`, `audit_id`, `actual_refund_amount`, `expected_refund_amount`, `tariff_version`, `sampling_method`, `checked_at` | Khi hoàn thành kiểm tra mẫu hằng tuần |
| `input_validation_failed` | Dịch vụ xác thực đầu vào | `trace_id`, `field`, `reason` | Khi phát hiện đầu vào không hợp lệ |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` + `ticket_closed` + `ticket_reopened`; so lần đóng đầu với thời điểm nhận, kiểm tra mở lại trong 7 ngày sau đóng. Chỉ kết luận không mở lại khi cửa sổ đã đủ và log đầy đủ.
- Bỏ qua gợi ý: `staff_review_decision` + `agent_suggestion_shown`; tính số yêu cầu sửa/bỏ trên số yêu cầu được xem lại. Nếu một yêu cầu có nhiều quyết định, dùng quyết định cuối của chu kỳ xử lý trước lần đóng đầu và giữ quy tắc cố định.
- Mở lại 7 ngày: `refund_request_created` + `ticket_closed` + `ticket_reopened`; chỉ đếm một lần/yêu cầu trên cohort trưởng thành.
- Mở trợ lý: `refund_request_created` + `agent_opened`, lọc `eligible=true` và `arm=intervention`; mẫu số gồm cả yêu cầu chưa mở trợ lý.
- Sai tiền kiểm toán: `audit_sample_checked` đối chiếu `refund_ledger_write`; kiểm toán ngẫu nhiên ít nhất 100 đơn/tuần, đối chiếu cả tổng tiền thực hoàn để bắt hoàn trùng. Mẫu điều tra có chủ đích báo riêng, không gộp để ước lượng tỉ lệ toàn bộ.
- Chi phí và rủi ro: `agent_run_completed` + `staff_review_decision` + `staff_rework_completed` + `handoff_to_staff`; đo phút thật ngay ngày đầu theo kế hoạch TV2. Phút xem lại và làm lại phải tách, tránh tính cùng thời gian hai lần.
- Các ca 7, 20: đối soát `refund_status_notified` với `refund_ledger_write` mỗi giờ; kiểm tra tổng giao dịch theo `request_id` để bắt hoàn trùng kể cả khi hai lệnh dùng khóa khác nhau.

Chỉ số tiền cần người kiểm toán đối chiếu chính sách đúng phiên bản và ngày hiệu lực; không dùng lại kết luận của agent làm đáp án đúng cho chính agent.

## E2 · Rủi ro kinh tế

Các tác động dưới đây lấy từ [B1 và B4 của bảng chi phí](bang_chi_phi.md), đều là **simulated**, chưa gồm cố định và chi phí luồng nhân viên ngoài CPS. Ngưỡng giám sát và hành động là đề xuất, chưa phải kết quả pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Chi phí làm lại tăng gấp đôi | B1 toàn mẫu: CPS từ 4.472 lên **6.787 đ, +51,77% (simulated)**; mô hình nhân tiền làm lại ×2, giữ số thành công, không phải dự báo tỉ lệ thành công mới. | Hằng tuần theo dõi số ca làm lại/tổng yêu cầu và phút thật/ca; cảnh báo khi tỉ lệ >7% trong phạm vi. Mốc chạy thử phạm vi: 48/982 = 4,89%. | PM rà 20 trace làm lại trong 2 ngày và giữ bước rollout; nếu CPS >8.000 đ trong 2 tuần ổn định liên tiếp thì trình thu hẹp về nội địa theo luật TV2. | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | B4 nội địa + hàng nặng: **11.743 đ/việc = 0,979×** thủ công với 9 phút làm lại; **12.415 đ = 1,035×** với 15,3 phút **(simulated)**. B4 giả định tối đa 3 lượt; pilot TV2 chọn 2 lượt nên cần tính lại khi có phút thật. | Cuối bước rollout 25%, theo dõi % gợi ý được xem lại còn >50%, phút xem lại và sửa/bỏ; ngưỡng hòa vốn B4 **5,122** hoặc **4,803 phút/lượt (simulated)** tùy thời gian làm lại. | Giữ bước và tính lại kinh phí; chỉ duyệt giảm xem lại khi ≥100 yêu cầu đã trưởng thành 7 ngày đạt an toàn, không hoàn trùng, sửa/bỏ <15%; luôn xem lại giao dịch rủi ro cao và kiểm toán ≥100 đơn/tuần theo TV2. | Trưởng nhóm CSKH |

Mốc 4,89% tính tay từ 48 ca làm lại / 982 yêu cầu trong phạm vi, không phải 48/1.200. Không lấy tác động +51,77% toàn mẫu làm dự báo chính xác cho pilot thu hẹp.

## Bàn giao và giới hạn

- TV4 có thể dùng ba chỉ số, đặc tả event và hai rủi ro này cho mục 4 và 7 của hồ sơ; các rủi ro chi phí phải giữ nhãn `simulated`.
- Trước khi bật pilot, Kỹ sư trưởng xác minh event thực sự được ghi đủ cho hai nhánh; đây mới là đặc tả, chưa có bằng chứng triển khai.
- Bảng nhãn lỗi và đồng thuận (19/20) xem [bang_loi.md](bang_loi.md); hai bộ nhãn có AI hỗ trợ. TV3 ghi hỗ trợ Codex và cách kiểm số trong báo cáo cá nhân.
