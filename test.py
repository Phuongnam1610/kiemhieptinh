import subprocess
import numpy as np
import cv2
import subprocess
import numpy as np
import cv2

def screen_capture(udid: str):
    try:
        # Lấy dữ liệu màn hình từ thiết bị Android
        result = subprocess.check_output(['adb', '-s', udid, 'exec-out', 'screencap'])
    except subprocess.CalledProcessError:
        print("❌ Lỗi khi chạy lệnh adb.")
        return None

    if len(result) < 12:
        print("❌ Dữ liệu ảnh trả về không hợp lệ.")
        return None

    # Đọc width, height từ 12 byte đầu
    width = int.from_bytes(result[0:4], byteorder='little')
    height = int.from_bytes(result[4:8], byteorder='little')
    _format = int.from_bytes(result[8:12], byteorder='little')  # thường là 1 (RGBA_8888)

    # Dữ liệu ảnh RGBA bắt đầu từ byte 12
    raw_img = np.frombuffer(result[12:], dtype=np.uint8).copy()

    # Chuyển thành ma trận ảnh với 4 kênh (RGBA)
    try:
        img = raw_img.reshape((height, width, 4))
    except ValueError:
        print("❌ Không reshape được ảnh. Có thể thiết bị không trả đúng dữ liệu.")
        return None

    # Đổi từ RGBA → BGR (bỏ kênh alpha)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

    return img_bgr


if __name__ == "__main__":
    udid = "emulator-5554"  # Ví dụ: "0123456789ABCDEF"
    image = screen_capture(udid)

    if image is not None:
        cv2.imwrite("screenshot.png",image)
        cv2.imshow("Screenshot", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Không thể chụp ảnh.")
