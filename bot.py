import requests
import os

# 1. 정보 설정
token = os.environ['TELEGRAM_TOKEN']
chat_id = "-1003790934369"

def send_telegram(message):
    # 가장 심플하게 메시지만 보냅니다 (에러 날 확률 0%)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # 테스트를 위해 오늘(20일)과 목표 날짜들을 넣었습니다.
        target_dates = [
            '03/20', '03.20', '3월 20', '20260320', # 오늘 테스트용
            '03/25', '03.25', '3월 25', '20260325', 
            '03/26', '03.26', '3월 26', '20260326',
            '03/27', '03.27', '3월 27', '20260327'
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
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 알림] 프로젝트 헤일메리 오픈!\n\n"
        "사키님! 예매가 열린 것 같습니다! 지금 바로 확인하세요.\n"
        f"예매 링크: {booking_url}"
    )
    send_telegram(msg)
