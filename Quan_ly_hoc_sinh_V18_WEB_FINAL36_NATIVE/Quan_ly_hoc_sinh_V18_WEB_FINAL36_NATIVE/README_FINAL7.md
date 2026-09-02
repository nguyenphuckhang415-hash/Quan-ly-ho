# QUAN LY HOC SINH V18 - WEB NATIVE (FINAL7)

Batch tiếp theo của bản web native dựa trực tiếp trên `Quan_ly_hoc_sinh_V18.py` gốc.

Đã bổ sung/siết các luồng V18 còn thiếu trong lớp web: đổi GVCN, đổi tên nhóm, ảnh nhóm, xóa lớp, xác nhận HS/PH bằng hai mã, quyền dữ liệu ban cán sự theo phạm vi tổ, trang tài khoản chi tiết, trang QR cho giáo viên, tải ảnh đại diện giáo viên, hoàn tất nhắc hẹn, và nhập Excel có thể nhận hàng tiêu đề trong các dòng đầu.

Quy tắc tài khoản mới vẫn được giữ: tài khoản/mật khẩu HS và PH tạo mới được sinh duy nhất; dữ liệu giáo viên chỉnh sửa là dữ liệu hiện hành; hồ sơ lần đầu của HS/PH có luồng cập nhật riêng.

Kiểm tra đã chạy: Python compile cho `app.py` và file V18 gốc; kiểm tra ZIP; kiểm tra SHA256 file V18 gốc khớp bản nguồn.

Lưu ý: môi trường này không có Flask runtime nên không chạy được Flask test-client end-to-end tại chỗ.
