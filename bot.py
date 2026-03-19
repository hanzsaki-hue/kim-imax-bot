import requests
import os

# 1. 정보 설정
token = os.environ['TELEGRAM_TOKEN']
chat_id = "-1003790934369"

def send_telegram(message):
    # HTML 모드를 사용해서 링크를 예쁘게 만듭니다
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        'chat_id': chat_id, 
        'text': message,
        'parse_mode': 'HTML' # 링크 클릭이 가능하게 해주는 설정
    }
    requests.get(url, params=params)

def check_imax():
    # CGV 용산아이파크몰 시간표 페이지
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        target_dates = [
            '03/24','03/25', '03.25', '3월 25', '20240325', 
            '03/26', '03.26', '3월 26', '20240326',
            '03/27', '03.27', '3월 27', '20240327'
        ]
        
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            for date in target_dates:
                if date in html:
                    return True
        return False
    except:
        return False

# 실행 부분
if check_imax():
    # 예매 페이지로 바로 가는 링크를 포함한 멘트입니다
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 <b>[용아맥 알림] 프로젝트 헤일메리 오픈!</b>\n\n"
        "사키님! 3월 25~27일 예매가 열린 것 같습니다!\n"
        f"👉 <a href='{booking_url}'>지금 바로 예매하러 가기 (클릭)</a>"
    )
    send_telegram(msg)
