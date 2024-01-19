import qrcode  # Import thư viện qrcode để tạo mã QR

def generate_qr_code(data, file_path):
    # Hàm tạo mã QR từ dữ liệu và lưu vào file hình ảnh tại đường dẫn được chỉ định
    qr = qrcode.QRCode(
        version=1,  # Phiên bản của mã QR
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Mức độ sửa lỗi
        box_size=10,  # Kích thước ô vuông cho mỗi module
        border=4,  # Kích thước đường viền
    )
    qr.add_data(data)  # Thêm dữ liệu vào mã QR
    qr.make(fit=True)  # Tạo mã QR

    img = qr.make_image(fill_color="black", back_color="white")  # Tạo hình ảnh từ mã QR với màu sắc chỉ định
    img.save(file_path)  # Lưu hình ảnh mã QR vào đường dẫn được chỉ định
