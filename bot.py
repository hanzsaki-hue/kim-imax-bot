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
        
        # 날짜 검사를 빼고, 제목과 IMAX관이 있는지만 확인합니다.
        # 지금 20일(오늘)은 이미 열려 있으니 무조건 True가 나와야 합니다.
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            return True
        return False
    except:
        return False

# 실행 부분
if check_imax():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 테스트] 프로젝트 헤일메리 발견!\n\n"
        "이 메시지가 오면 연결은 완벽한 겁니다!\n"
        f"바로가기: {booking_url}"
    )
    send_telegram(msg)
