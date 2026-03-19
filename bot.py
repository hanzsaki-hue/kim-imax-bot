import requests
import os

# 1. 정보 설정
token = os.environ['TELEGRAM_TOKEN']
chat_id = "-1003790934369"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    # CGV 용산아이파크몰 시간표 페이지
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # 사키님이 노리시는 25, 26, 27일 날짜 키워드들
        target_dates = [
            '03/25', '03.25', '3월 25', '20240325', 
            '03/26', '03.26', '3월 26', '20240326',
            '03/27', '03.27', '3월 27', '20240327'
        ]
        
        # '프로젝트 헤일메리'와 'IMAX'가 있으면서, 해당 날짜 중 하나라도 뜨면 성공!
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            for date in target_dates:
                if date in html:
                    return True
        return False
    except:
        return False

# 실행 부분
if check_imax():
    msg = "🚨 [용아맥 알림] 사키님! 3월 25, 26, 27일 중 '프로젝트 헤일메리' IMAX 예매가 열렸습니다! 지금 바로 접속하세요! 🎬"
    send_telegram(msg)


