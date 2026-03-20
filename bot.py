import requests
import datetime

# 1. 사키님의 검증된 정보
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    # 블로그에서 배운 '진짜 데이터 주소' (iframe 전용)
    # 날짜를 20260320으로 고정해서 테스트해봅니다.
    target_date = "20260320"
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date={target_date}"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        # 블로그 노하우: 'info-movie'라는 글자가 있으면 일단 영화 데이터가 로딩된 것!
        if 'info-movie' in html:
            # 사키님이 노리는 키워드 확인
            if '헤일메리' in html and 'IMAX' in html:
                return True, "3월 20일"
        return False, None
    except:
        return False, None

# --- 실행 부분 (GitHub Actions 맞춤형) ---
is_open, found_date = check_imax()

if is_open:
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = f"🚨 [용아맥 정밀 탐지]\n\n사키님! {found_date} '프로젝트 헤일메리' IMAX가 포착되었습니다!\n👉 {booking_url}"
    send_telegram(msg)
else:
    # 봇이 살아있는지 확인용 (성공하면 나중에 이 줄만 지우세요!)
    send_telegram("🔍 [봇 감시 중] 정밀 주소로 접속 성공! 아직 20일 표는 인식을 못하고 있네요.")
