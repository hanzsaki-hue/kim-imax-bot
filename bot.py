import requests
import os

# 1. 깃허브 Secrets에서 안전하게 정보를 가져오도록 설정했습니다.
token = os.environ['TELEGRAM_TOKEN']
chat_id = "-1003790934369" # 방금 찾은 진짜 주소로 고정!

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

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
if check_imax():
    # 영화가 떴을 때 보내는 실제 알람 멘트
    msg = "🚨 [용아맥 알림] '프로젝트 헤일메리' IMAX 예매가 열린 것 같습니다! 지금 바로 확인하세요! 🎬"
    send_telegram(msg)

# 테스트용 (제대로 연결됐는지 단톡방에 바로 쏴봅니다!)
# 나중에 테스트가 끝나면 아래 줄 앞에 #을 붙여서 지워주세요.
send_telegram("✅ [용아맥 연결 성공] 사키님, 여자친구분! 이제 봇이 5분마다 감시를 시작합니다. 푹 주무세요! 🎬")
