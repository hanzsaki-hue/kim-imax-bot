import requests
import os

# 1. 정보 설정 (토큰과 ID 직접 입력)
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    # 실행 결과를 로그로 남겨서 성공 여부를 확인합니다.
    print(f"Telegram Response: {response.json()}")

def check_imax():
    # CGV 용산아이파크몰 시간표 페이지
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # 오늘(20일)은 영화가 이미 열려있으므로 이 두 단어는 무조건 페이지에 있습니다.
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            return True
        return False
    except:
        return False

# --- 실행 부분 ---

# 1. 실제 감시 로직 (영화가 발견되면 발사)
if check_imax():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 실전 알림] 프로젝트 헤일메리 발견!\n\n"
        "설정하신 날짜의 예매가 열린 것 같습니다.\n"
        f"👉 바로가기: {booking_url}"
    )
    send_telegram(msg)

# 2. 테스트용 무조건 발사 (연결 확인용)
# 이 줄이 살아있으면 5분마다 계속 메시지가 오니, 테스트 성공하면 이 줄 앞에 #을 붙여주세요!
send_telegram("✅ [연결 테스트] 사키님, 봇이 현재 정상 작동 중입니다! 🎬")
