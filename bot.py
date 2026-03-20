import requests

# 1. 사키님의 고유 정보 (검증 완료)
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    # CGV 용산아이파크몰 모바일 시간표 페이지
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # 1차 검사: 영화 제목과 IMAX 관이 있는지 확인
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            
            # 2차 검사: 사키님이 노리는 날짜들 (오늘 20일 포함!)
            target_dates = ['20260320', '20260325', '20260326', '20260327'] 
            
            for date in target_dates:
                # 페이지 소스에 해당 날짜 데이터가 있는지 확인
                if date in html:
                    return True, date
        return False, None
    except:
        return False, None

# --- 실행 부분 ---
is_open, found_date = check_imax()

if is_open:
    # 날짜 글자를 예쁘게 변환 (예: 20260320 -> 03월 20일)
    pretty_date = f"{found_date[4:6]}월 {found_date[6:8]}일"
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    
    msg = (
        f"🚨 [용아맥 정밀 알림]\n\n"
        f"사키님! {pretty_date} '프로젝트 헤일메리' 예매가 포착되었습니다!\n"
        f"지금 바로 확인하세요! 🔥\n\n"
        f"👉 바로가기: {booking_url}"
    )
    send_telegram(msg)
