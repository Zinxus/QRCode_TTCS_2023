def check_Attendance(excel_file):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    marked = False  # Biến cờ để theo dõi đã đánh dấu 'X' hay chưa

    while cap.isOpened() and not marked:
        success, img = cap.read()
        if success:
            decode_img(img, excel_file)
            cv2.imshow("decode", img)
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindo