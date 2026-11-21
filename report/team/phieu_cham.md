# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- **Nhóm chấm (hội đồng):** HongSac (L3A)
- **Nhóm được chấm:** TamKa (L3A) · https://github.com/DucTrung611/K5-L3A-DAY13-TamKa-LaunchEconomics
- **Bản đối chiếu:** nhánh `main`, truy cập ngày 21/11/2026 (chưa cố định mã commit; đề nghị hai nhóm xác nhận commit khi gửi phiếu).
- **File đã đọc:** `report/team/ho_so_launch_v0.md`, `report/team/pilot_plan.yaml`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/group_report.md`; đối chiếu `RUBRIC.md`.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất **Go có điều kiện** phù hợp chi phí cả hệ thống **5.865 đ/yêu cầu = 0,49×** mức tự làm **12.000 đ** [simulated]. Trong phạm vi `noi_dia` + `hang_nang`, chi phí gồm phần cố định là **4.599–5.784 đ/việc thành công = 0,38–0,48×** [simulated]. Nhóm không giấu rủi ro: xem lại 100% đưa chi phí lên **11.743–12.415 đ** [simulated], còn power chỉ khoảng **64,2%** nếu tác động thật là **+5 điểm**. Có đề xuất giảm xem lại theo bậc, giới hạn 2 lần chạy và điều kiện theo dõi. Tuy nhiên, điều kiện kéo dài pilot để xử lý power cần làm rõ ở phần phản biện. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Hồ sơ phân biệt trạng thái **Giả lập** ở các mục kinh tế; `bang_chi_phi.md` ghi nhãn `[simulated]` cho các kịch bản và `pilot_plan.yaml` có `simulated_inputs`. Phạm vi được giới hạn về **982/1.200 yêu cầu** (`noi_dia`: **824**, `hang_nang`: **158**), thay vì áp dụng đại trà. Loại `quoc_te` vì **22.515 đ/việc = 1,88×** và tỉ lệ thành công chỉ **27,3%**; loại `doi_tac` dù có **0,85×** do thành công mới **54,4%** và có điều khoản riêng [các chi phí là simulated]. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **5** | Có thiết kế đối chứng đồng thời, phân nhóm ngẫu nhiên theo nhân viên **20 + 20**, chia theo depot; với **MDE +6 điểm**, tính **DE = 6,96**, cần **m ≥ 299 yêu cầu/nhân viên** (tương đương khoảng **5.980 yêu cầu thô/nhánh**, hiệu dụng **859/nhánh**). Có **3 luật dừng** nêu ngưỡng (mở lại chênh ≥ **2 điểm** hoặc > **6%**, CPS > **8.000 đ**, bỏ qua gợi ý > **40%**), thời gian và vai trò; rollback **30 phút**, ngày quyết định **05/01/2027**. Tuy nhiên, cả 3 nhánh `KHÔNG THÌ` trong `stop_rules` lại cấm đi tiếp/giữ phạm vi ngay cả khi **không** chạm ngưỡng, khiến luật khó dùng để quyết định tăng bước rollout. Cần sửa logic trước pilot nên chưa chấm mức 10. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện**.

**Lý do:** HongSac đồng ý cho TamKa tiếp tục **chuẩn bị pilot có điều kiện**, chưa đồng nghĩa đã đạt điều kiện để tăng quy mô. Phương án có lợi thế chi phí rõ ràng trong `noi_dia` + `hang_nang` (**0,38–0,48×** tự làm [simulated]), có đối chứng và cỡ mẫu phù hợp với **MDE +6 điểm**. Trước khi chạy hoặc mở rộng, nhóm cần làm rõ hai vấn đề:

- **Khả năng đạt power ở +5 điểm:** `pilot_plan.yaml` mục D1 đã tính trần cỡ mẫu hiệu dụng với **20 cụm/nhánh, ICC = 0,02** là **20 / 0,02 = 1.000/nhánh**, thấp hơn **1.251/nhánh** cần cho MDE +5. Vì vậy việc kéo dài **2 tuần** để có `m ≥ 299` **không tự khắc phục** thiếu power 80% cho +5 điểm; `m ≥ 299` là mức nhóm tính cho MDE **+6**.
- **Logic luật dừng:** Trong `pilot_plan.yaml`, các câu `KHÔNG THÌ không được sang bước rollout tiếp theo`, `KHÔNG THÌ không được giữ hang_nang`, `KHÔNG THÌ không được chuyển bước rollout` đang đặt hạn chế ngay cả khi điều kiện cảnh báo không xảy ra. Cần phân biệt rõ khi nào **dừng/rollback**, khi nào **tiếp tục theo dõi**, khi nào **được xét tăng bước**. Ngoài ra, nên làm rõ cách áp dụng giới hạn CPS **8.000 đ** trong pha xem lại 100%, khi B4 ước tính **11.743–12.415 đ** [simulated].

**Một câu hỏi cho đội trình:** `pilot_plan.yaml` của TamKa tự tính rằng với **20 nhân viên/nhánh** và **ICC = 0,02**, cỡ mẫu hiệu dụng tối đa chỉ là **1.000/nhánh**, thấp hơn **1.251/nhánh** cần để phát hiện cải thiện **+5 điểm** ở power 80%. Nhưng Điều kiện 4 trong `ho_so_launch_v0.md` lại đề xuất **kéo dài pilot thêm 2 tuần để đạt m ≥ 299** nếu tác động thật chỉ +5 điểm. **Nhóm sẽ xử lý sự mâu thuẫn này như thế nào: đổi thiết kế/tăng số cụm, chấp nhận power thấp và ghi rõ hạn chế, hay chưa ra quyết định Go? Ai có quyền phê duyệt phương án và chốt trước ngày 05/01/2027?**

**Câu trả lời của đội trình (TamKa ghi sau khi nhận phiếu):**

<!-- Nhóm TamKa điền câu trả lời tại đây, giữ lại phần câu hỏi và nhận xét phía trên. -->

1. Thừa nhận Điều kiện 4 sai. Kéo dài pilot không cứu được power ở +5 điểm, vì cỡ mẫu hiệu dụng bị chặn ở 1.000/nhánh. Tôi đã tính lại bằng statsmodels: power hiện tại 0,642; kể cả kéo dài vô hạn cũng chỉ đạt tối đa 0,708.
2. Chọn "chấp nhận power thấp và ghi rõ hạn chế". Lý do: không thể tăng số cụm vì chỉ có 40 nhân viên, và chia theo yêu cầu thì tác động tràn sang nhóm đối chứng. Câu trả lời cũng nêu quy tắc đọc kết quả viết trước cho ngày 05/01/2027: không đạt thì là "chưa đủ bằng chứng", No-go cho mở rộng. Giám đốc vận hành ký chấp nhận đánh đổi trước bước 10%.
3. Phản hồi hai nhận xét còn lại. KHÔNG THÌ được viết theo mẫu của đề nhưng câu chữ dễ hiểu nhầm, nhóm sẽ viết lại cho rõ. Luật chi phí 8.000 đ đo trong 2 tuần, nên thực chất đóng vai trò giới hạn thời gian cho pha xem lại 100%.
