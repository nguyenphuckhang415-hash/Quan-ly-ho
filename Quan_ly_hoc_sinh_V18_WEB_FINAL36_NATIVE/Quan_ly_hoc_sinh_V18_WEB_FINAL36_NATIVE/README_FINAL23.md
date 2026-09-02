# FINAL23 – Quan_ly_hoc_sinh_V18 Native Web

Bản tiếp theo của native-web port, tiếp tục giữ nguyên `Quan_ly_hoc_sinh_V18.py` gốc trong gói.

## Bổ sung FINAL23
- Thêm các URL/action alias tương ứng trực tiếp với các màn hình V18: dashboard giáo viên, dashboard học sinh/phụ huynh/ban cán sự, quản lý học sinh/lớp/điểm/nhiệm vụ/ban cán sự/tổng kết/tài khoản, hồ sơ giáo viên, QR giáo viên, chat picker và nhắc hẹn.
- Hoàn thiện first-login guard với đủ tên phụ huynh, email phụ huynh, tổ và nhóm.
- Duy trì tài khoản HS/PH tự sinh duy nhất và luồng Excel/QR/xác nhận mã/chuyển lớp/quyền ban cán sự.
- Đường dẫn tệp chat sử dụng basename và chỉ phục vụ file trong thư mục upload của ứng dụng.

## Kiểm tra
- `app.py`: compile OK
- `Quan_ly_hoc_sinh_V18.py`: compile OK
- template `url_for`: 0 endpoint thiếu
- ZIP integrity: OK
