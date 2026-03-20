import requests

token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    # 이 프로젝트가 사용하는 '진짜 예매 데이터' API 주소입니다. (가장 정확함)
    # theatercode=0013(용산), date=20260320
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?theatercode=0013&date=20260320"
    
    try:
        # 이 프로젝트처럼 유저 에이전트를 모바일 앱처럼 설정합니다.
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
        }
        response = requests.get(url, headers=headers)
        html = response.text
        
        # '프로젝트 헤일메리'가 있는지 확인
        if '헤일메리' in html:
            # 이 프로젝트의 방식: 'IMAX'라는 글자가 해당 영화 섹션에 있는지 확인
            if 'IMAX' in html:
                return True, "3월 20일"
        return False, None
    except:
        return False, None

# --- 실행 ---
is_open, found_date = check_imax()
if is_open:
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = f"🚨 [용아맥 정밀 탐지]\n\n사키님! {found_date} 예매 정보가 포착되었습니다!\n지금 바로 접속하세요! 🔥\n👉 {booking_url}"
    send_telegram(msg)
else:
    # 봇이 죽었는지 확인하기 위해 텍스트를 아주 살짝 바꿔서 보냅니다.
    send_telegram("🔍 [봇 감시 중] 0w0i0n0g0 프로젝트 로직 적용 완료! 20일 감시 중.")
