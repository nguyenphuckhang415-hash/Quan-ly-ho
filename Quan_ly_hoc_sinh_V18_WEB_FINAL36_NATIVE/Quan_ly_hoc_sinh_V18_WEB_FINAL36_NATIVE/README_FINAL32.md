# Quan ly hoc sinh V18 - WEB FINAL32 Native

Tiếp tục từ FINAL31. Mục tiêu của bản này là tăng parity hành vi với V18 thay vì chỉ tăng số route.

Đã sửa:
- `/v18/save-score` ghi dữ liệu điểm thật và trả JSON kết quả.
- `/v18/save-task` ghi nhiệm vụ thật và trả JSON kết quả.
- `/v18/assign` ghi nhiệm vụ thật thay vì chỉ render lại trang.
- `add_student_roster` giờ tự tạo tài khoản HS và tài khoản PH duy nhất, đặt PH ở trạng thái cần đổi mật khẩu lần đầu.
- Tạo lớp/nhóm tương ứng khi thêm học sinh qua helper roster.
- Giữ nguyên `Quan_ly_hoc_sinh_V18.py` gốc trong gói.

Kiểm tra: Python compile, duplicate routes, template endpoint references, ZIP integrity.
