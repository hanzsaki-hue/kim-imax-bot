import requests
import os

# 1. 정보 설정 (토큰과 ID를 코드에 직접 박았습니다)
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    print(response.json()) # 실행 결과 로그 남기기

def check_imax():
    # CGV 용산아이파크몰 시간표 페이지
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # 오늘(20일)은 무조건 영화가 있으니 이 두 단어는 무조건 걸립니다.
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            return True
        return False
    except:
        return False

# 실행 부분
if check_imax():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 감시 중] 프로젝트 헤일메리 발견!\n\n"
        "사키님, 이 메시지가 오면 봇은 살아있는 겁니다.\n"
        f"바로가기: {booking_url}"
    )
    send_telegram(msg)
