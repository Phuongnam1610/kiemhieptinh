from google.cloud import firestore
from google.oauth2 import service_account
import requests

from datetime import datetime as a
key_path = "serviceAccountKey.json"

# Tạo credentials từ file key
credentials = service_account.Credentials.from_service_account_file(key_path)

# Khởi tạo client Firestore với credentials
db = firestore.Client(credentials=credentials, project="toollq")

import uuid
# Lấy địa chỉ MAC của máy tính
mac_address = uuid.getnode()
def checkHSD(docs):    
    # Convert data to string or int type
    hsd = docs.get().get('dateHSD')
    date_obj = a.strptime(str(hsd), "%Y-%m-%d %H:%M:%S.%f%z")
    dateHSD = date_obj
    
    # Get current time using datetime with UTC+7 offset (Vietnam timezone)
    from datetime import datetime, timedelta
    import pytz
    
    # Get current UTC time and add 7 hours for Vietnam timezone
    response = requests.get("https://www.google.com", timeout=5)
    server_time = response.headers['date']
    today = datetime.strptime(server_time, '%a, %d %b %Y %H:%M:%S %Z')
    
    # Make today timezone-aware by setting UTC timezone
    today = pytz.UTC.localize(today)
    
    if today > dateHSD:
        print("key het han")
        return 1
    else:
        return 0
def checkLogged(docs):
    # Chuyển đổi dữ liệu thành kiểu string hoặc int
    logged = docs.get().get('Logged')
    if(logged==str(mac_address)):
        return 1
    elif(logged==""):
        insertID(docs)
        return 2
    else:
        print("key da su dung")
        return 0

def MaxDevices(docs):
    # Chuyển đổi dữ liệu thành kiểu string hoặc int
    num = docs.get('Max')
    return num
    
def insertID(user_ref):
    user_ref.update({
        "Logged": f"{mac_address}"
    })

def AuthFirebase(docs):
    if(checkLogged(docs)==0):
        exit()
    else:
        if(checkHSD(docs)==1):
            exit()
doc_ref = db.collection("keys").document("cam2")
AuthFirebase(doc_ref)