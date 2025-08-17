import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import re

# Nếu dùng Windows, chỉ định đường dẫn tới file tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def getNumber(image):
    # Chỉ nhận số (digits)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    numbers = pytesseract.image_to_string(image, config=custom_config)
    # Lọc số từ chuỗi (đề phòng OCR trả về ký tự lạ)
    numbers_str = ''.join(char for char in numbers if char.isdigit())
    digits_only = re.sub(r'\D', '', numbers_str)

    # Chuyển sang int (nếu rỗng thì trả None hoặc 0)
    number = int(digits_only) if digits_only else 0
    return number