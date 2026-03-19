import requests
import os

token = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['CHAT_ID']

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def check_imax():
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    response = requests.get(url)
    if '프로젝트 헤일메리' in response.text and 'IMAX' in response.text:
        return True
    return False

if check_imax():
    send_telegram("🚨 사키님! '프로젝트 헤일메리' IMAX 예매가 열린 것 같아요!")
