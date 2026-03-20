import requests

# 1. 정보 설정 (사키님 고유 정보)
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    try:
        requests.get(url, params=params, timeout=10)
    except:
        pass

def check_evidence():
    # CGV 용산아이파크몰의 '오늘(20일)' 데이터 주소
    # (25~27일로 바꾸기 전, 오늘 데이터로 뚫리는지 마지막 확인!)
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?theatercode=0013&date=20260320"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text
        
        # [핵심 로직] 버튼이고 뭐고 다 필요 없고, 이 두 단어가 '한 페이지'에 있는지만 봅니다.
        if '헤일메리' in html and 'IMAX' in html:
            return True
        return False
    except:
        return False

# --- 실행 부분 ---
if check_evidence():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 실전 탐지 성공!]\n\n"
        "사키님! 버튼은 숨겨져 있지만 '영화 정보' 흔적을 포착했습니다!\n"
        "이 글자가 떴다는 건 예매가 가능하다는 강력한 신호입니다. 🔥\n\n"
        f"👉 즉시 확인: {booking_url}"
    )
    send_telegram(msg)
else:
    # 만약 오늘 표가 있는데도 이 메시지가 온다면, 봇이 보는 페이지는 '빈 페이지'인 겁니다.
    send_telegram("⚠️ [최종 경고] 영화 제목조차 찾지 못했습니다. CGV가 봇을 완전히 차단 중일 수 있습니다.")
림] 접속은 했으나, 20일 예매 버튼을 특정하지 못했습니다. (매진 혹은 시스템 변경 가능성)")
