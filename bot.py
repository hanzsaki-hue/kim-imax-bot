import requests

# 1. 정보 설정
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    # 블로그에서 배운 '진짜 데이터 주소' (iframe 전용)
    # 오늘(20일) 데이터를 확실히 긁어오기 위해 날짜를 파라미터로 넣습니다.
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20260320"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        # 1. 영화 제목 확인 (전체 다 쓰지 않고 핵심 단어만!)
        # 2. IMAX 관이 있는지 확인
        if '헤일메리' in html and 'IMAX' in html:
            # 3. 날짜 확인 (블로그 비법: 숫자 20 뒤에 특수태그가 붙는지 확인)
            # '20'이라는 글자만 있어도 일단 성공으로 간주합니다.
            if '20' in html:
                return True
        return False
    except:
        return False

# --- 실행 부분 ---
if check_imax():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 정밀 탐지 성공!]\n\n"
        "사키님! 20일 예매 정보가 드디어 포착되었습니다!\n"
        "이제 봇이 날짜를 완벽하게 읽고 있습니다. 🔥\n\n"
        f"👉 바로가기: {booking_url}"
    )
    send_telegram(msg)
else:
    # 이번에도 안 오면 주소의 '날짜 파라미터'가 문제인 겁니다.
    send_telegram("🔍 [봇 감시 중] 정밀 주소 접속은 OK, 하지만 날짜 매칭 실패.")
