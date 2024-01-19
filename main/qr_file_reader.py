import cv2  # Import thư viện OpenCV để xử lý ảnh và video
import pyzbar.pyzbar as pyzbar  # Import thư viện pyzbar để giải mã mã QR

def read_qr_from_file(file_path):
    # Đọc hình ảnh từ tệp
    image = cv2.imread(file_path)  # Đọc ảnh từ đường dẫn file_path
    qr_data = decode_qr_from_frame(image)  # Giải mã QR từ ảnh
    return qr_data

def decode_qr_from_frame(frame):
    # Hàm giải mã mã QR từ frame ảnh
    decoded_objs = pyzbar.decode(frame)  # Giải mã QR từ frame
    for obj in decoded_objs:  # Duyệt qua các đối tượng đã giải mã được
        return obj.data.decode('utf-8')  # Trả về dữ liệu giải mã
    return None  # Nếu không có mã QR nào được tìm thấy, trả về None
