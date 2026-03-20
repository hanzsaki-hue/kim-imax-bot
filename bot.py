import requests

# 1. 정보 설정
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    try:
        requests.get(url, params=params, timeout=10)
    except:
        pass

def test_booking_button():
    # CGV 용산아이파크몰 진짜 데이터 주소 (20일 고정)
    test_date = "20260320"
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?theatercode=0013&date={test_date}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text
        
        # [검증 1] 영화 정보가 로딩되었는가?
        if 'info-movie' in html:
            # [검증 2] 헤일메리 영화가 있는가?
            if '헤일메리' in html:
                # [검증 3] 실제 예매 가능한 시간표 버튼(주로 'count'나 'book' 관련 태그)이 있는가?
                # 20일은 이미 상영 중이거나 예매가 열려 있으므로 이 코드가 발견되어야 합니다.
                if 'IMAX' in html and ('잔여좌석' in html or 'remains' in html or 'txt-lightblue' in html):
                    return True, "3월 20일(오늘)"
        
        return False, None
    except:
        return False, None

# --- 실행 부분 ---
success, date_name = test_booking_button()

if success:
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        f"✅ [예매 버튼 탐지 테스트 성공!]\n\n"
        f"사키님, 시스템이 {date_name}의 실제 예매 버튼을 찾아냈습니다.\n"
        f"이 로직이면 25~27일 예매가 뜨는 순간 즉시 알람이 울립니다! 🔥\n\n"
        f"👉 테스트 링크: {booking_url}"
    )
    send_telegram(msg)
else:
    # 만약 실패했다면 봇이 현재 보고 있는 상태를 알려줍니다.
    send_telegram("🔍 [테스트 알림] 접속은 했으나, 20일 예매 버튼을 특정하지 못했습니다. (매진 혹은 시스템 변경 가능성)")
