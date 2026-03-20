import requests

# 1. 사키님의 검증된 정보
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    # CGV 모바일 시간표 주소
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        # 브라우저인 척 하기 (블로그 팁)
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        # 1. 영화 제목이 있는지 확인 (공백 문제 해결을 위해 핵심 단어만 찾기)
        if '프로젝트' in html and '헤일메리' in html and 'IMAX' in html:
            
            # 2. 날짜 정밀 검사 (블로그들에서 공통으로 말한 패턴들)
            # 오늘(20)이 포함되어 있으니 지금 바로 알람이 와야 합니다.
            target_dates = ['20260320', '20260325', '20260326', '20260327']
            
            for date in target_dates:
                # CGV 소스 코드 안에 날짜 데이터가 박혀있는지 확인
                if date in html:
                    return True, date
                    
        return False, None
    except:
        return False, None

# --- 실행 부분 ---
is_open, found_date = check_imax()

if is_open:
    pretty_date = f"{found_date[4:6]}월 {found_date[6:8]}일"
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    
    msg = (
        f"🚨 [용아맥 정밀 탐지 성공]\n\n"
        f"사키님! {pretty_date} 예매가 포착되었습니다!\n"
        f"지금 바로 접속하세요! 🔥\n\n"
        f"👉 바로가기: {booking_url}"
    )
    send_telegram(msg)

# 실행
is_open, found_date = check_imax()
if is_open:
    pretty_date = f"{found_date[4:6]}월 {found_date[6:8]}일"
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = f"🚨 [용아맥 정밀 탐지]\n\n사키님! {pretty_date} 예매가 포착되었습니다!\n지금 바로 접속하세요! 🔥\n👉 {booking_url}"
    send_telegram(msg)
