import requests
import os

# 깃허브 금고(Secrets)에서 정보를 가져옵니다
token = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['CHAT_ID']

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def check_imax():
    # CGV 용산 아이파크몰 시간표 페이지
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        # 페이지 안에 '프로젝트 헤일메리'와 'IMAX' 글자가 모두 있는지 확인
        if '프로젝트 헤일메리' in response.text and 'IMAX' in response.text:
            return True
        return False
    except:
        return False

# 실행 부분

    # 사키님이 원하시는 깔끔한 문구로 수정했습니다!
    msg = "🚨 [용아맥 알림] '프로젝트 헤일메리' IMAX 예매가 열린 것 같습니다! 지금 바로 확인하세요! 🎬"
    send_telegram(msg)

