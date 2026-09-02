# Quan Ly Hoc Sinh V18 — FINAL34 Native

Mức: 99%

FINAL34 tiếp tục từ V18 gốc và giữ nguyên file `Quan_ly_hoc_sinh_V18.py` trong gói để đối chiếu.

Các sửa chính của FINAL34:
- Sửa helper `edit_summary` để ghi đúng schema `summaries` của V18.
- Bổ sung helper chuyển lớp/chuyển tổ theo đúng logic V18: giữ nguyên điểm, nhiệm vụ, thành tích/hồ sơ và cập nhật `transfer_notice`.
- Loại bỏ định nghĩa hàm trùng `transfer_student` và `regenerate`.
- Giữ một endpoint chuyển lớp chính theo luồng web V18.
- Tài khoản phụ huynh tạo mới theo luồng thêm học sinh được đặt `must_change=1`, `verified=0` để đúng quy tắc đăng nhập lần đầu đã chốt.
- Giữ giáo viên là nguồn dữ liệu hiện hành đối với lớp/tổ/tên nhóm khi giáo viên chỉnh sửa.

Kiểm tra: Python AST/compile, endpoint references trong template và tính toàn vẹn gói ZIP.
