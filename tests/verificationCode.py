import requests
import json
import urllib
import ddddocr
from datetime import datetime

def codeApi():
    url = f"http://192.168.1.8:7777/prod-api/captchaImage"
    response = requests.get(url)
    # 获取uuid
    uuid = response.json()["uuid"]
    # 下载图形验证码并使用ocr识别
    img_url = "data:image/gif;base64," + response.json()["img"]
    urllib.request.urlretrieve(img_url, r'C:\Users\Administrator\Desktop\img\1.jpg')
    ocr = ddddocr.DdddOcr()
    with open(r'C:\Users\Administrator\Desktop\img\1.jpg', 'rb') as f:
        img_data = f.read()
    code = ocr.classification(img_data)
    return code,uuid

