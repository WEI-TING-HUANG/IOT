import RPi.GPIO as GPIO
import time

import requests

# LINE Notify 權杖
token = '###################'

# url string
urlStr = 'https://ec29-2001-b400-e2d5-5fc9-ec62-ac8b-c2da-4a20.ngrok-free.app/'

# 要發送的訊息
message = '這是用 Python 發送的訊息 , ' + urlStr

# HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + token }
data = { 'message': message }

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
while True:
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        
        requests.post("https://notify-api.line.me/api/notify",
            headers = headers, data = data)
    time.sleep(2)
