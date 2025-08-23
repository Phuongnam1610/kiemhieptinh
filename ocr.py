import cv2
import numpy as np
import pytesseract
import unicodedata
def normalize_and_filter(text: str) -> str:
    # B1: bỏ dấu tiếng Việt
    nfkd_form = unicodedata.normalize('NFD', text)
    no_accents = ''.join([c for c in nfkd_form if unicodedata.category(c) != 'Mn'])
    no_accents = no_accents.replace('đ', 'd').replace('Đ', 'D')
    
    # B2: chuyển về chữ thường
    no_accents = no_accents.lower()
    
    # B3: chỉ giữ lại ký tự cho phép (không giữ khoảng trắng)
    allowed = set("yeucaudnp gim")  # chứa toàn bộ ký tự bạn yêu cầu
    allowed.discard(" ")            # bỏ space luôn
    filtered = ''.join([c for c in no_accents if c in allowed])
    
    return filtered

def contains_required_pairs(text: str) -> bool:
    filtered = normalize_and_filter(text)

    # Nếu ngắn hơn 25 ký tự thì loại
    if len(filtered) < 28:
        return False

    # Lấy 25 ký tự cuối
    filtered = filtered[-28:]
    print('chuỗi',filtered)
    # ===== Bước 1: Test 4 ký tự =====
    origin = "yeucaudangcapgiam"   # bỏ khoảng trắng
    print('origin',origin)

    base4 = [origin[i:i+5] for i in range(len(origin) - 4)]

    matches4 = [b for b in base4 if b in filtered]
    if not matches4:
        return False  # Nếu không match 4 ký tự thì coi như fail
    print('khớp 4',matches4)

    # Loại bỏ các từ 4 ký tự đã match khỏi chuỗi 25 ký tự cuối
    for m in matches4:
        filtered = filtered.replace(m, "")
        
        origin = origin.replace(m,"")
    print(filtered)
    print('origin',origin)

    # ===== Bước 2: Test 2 ký tự =====
    base2 = [origin[i:i+3] for i in range(len(origin) - 2)]
    print(base2)
    matches2 = [b for b in base2 if b in filtered]
    print('khớp',matches2)
    return len(matches2) >= 1


# ⚠️ Đường dẫn tới file tesseract.exe (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ====== Tiền xử lý ảnh ======

def unsharp_mask(img, blur_size=5, strength=2.0):
    """
    blur_size: kích thước kernel GaussianBlur (số lẻ, ví dụ 3,5,7)
    strength: hệ số tăng nét (cao hơn => nét hơn)
    """
    blur = cv2.GaussianBlur(img, (blur_size, blur_size), 0)
    sharpened = cv2.addWeighted(img, 1 + strength, blur, -strength, 0)
    return sharpened
def apply_clahe(img):
    """
    CLAHE = Contrast Limited Adaptive Histogram Equalization
    Làm sáng chữ + tối nền ở từng vùng nhỏ
    """
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    return clahe.apply(img)

def sharpen_image(img):
    """Tăng nét ảnh bằng kernel sharpen"""
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

def scale_image(img, scale_factor=2.0):
    """Phóng to ảnh để OCR chính xác hơn"""
    h, w = img.shape[:2]
    new_size = (int(w * scale_factor), int(h * scale_factor))
    return cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)
def sharpen_laplacian(img):
    # Tính cạnh bằng Laplacian
    lap = cv2.Laplacian(img, cv2.CV_64F)
    lap = cv2.convertScaleAbs(lap)

    # Cộng ngược vào ảnh gốc để tăng nét
    sharpened = cv2.addWeighted(img, 1.5, lap, -0.5, 0)
    return sharpened
def increase_contrast(img, alpha=1.8, beta=0):
    """
    alpha: hệ số tương phản (1.0 = giữ nguyên, >1.0 = tăng contrast)
    beta : độ sáng (cộng thêm, thường để 0 hoặc 10)
    """
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

def preprocess_image(img):
    """Pipeline: grayscale -> denoise -> sharpen -> scale -> threshold"""
    gray = scale_image(img, scale_factor=2.0)
    gray = cv2.detailEnhance(gray, sigma_s=80, sigma_r=0.1)

    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)



    # 1. Grayscale
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    # gray=increase_contrast(gray)

    return gray

# ====== OCR số ======
def getNumber(image_path):
    img = preprocess_image(image_path)

    # OCR chỉ lấy số
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    numbers = pytesseract.image_to_string(img, config=custom_config)

    # Lọc số
    digits_only = "".join(ch for ch in numbers if ch.isdigit())
    number = int(digits_only) if digits_only else 0
    return number

# ====== OCR tiếng Việt ======
def getVietnameseText(image_path):
    img = preprocess_image(image_path)
    # cv2.imwrite('test.png',img)
    # OCR tiếng Việt với whitelist ký tự
    custom_config = (
        r'--oem 3 --psm 6 '
    
    )
    text = pytesseract.image_to_string(img, lang="vie", config=custom_config)
    return text.strip()