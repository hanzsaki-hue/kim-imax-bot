import requests

# 1. 텔레그램 정보
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_msg(text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(url, params={'chat_id': chat_id, 'text': text})

def check_imax():
    # PC 버전 데이터 주소 (차단 확률이 낮음)
    base_url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?theatercode=0013&date="
    
    # 사키님의 진짜 목표 날짜들!
    target_dates = [
        ('20260325', '3월 25일(수)'),
        ('20260326', '3월 26일(목)'),
        ('20260327', '3월 27일(금)')
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'http://www.cgv.co.kr/theaters/'
    }

    try:
        for date_code, date_name in target_dates:
            # 각 날짜별로 PC 버전 페이지를 긁어옵니다.
            res = requests.get(base_url + date_code, headers=headers, timeout=15)
            html = res.text
            
            # 0w0i0n0g0 프로젝트에서도 검증된 '핵심 단어' 체크
            if '헤일메리' in html and 'IMAX' in html:
                return True, date_name
        return False, None
    except:
        return False, None

# --- 실행 부분 ---
is_open, found_date = check_imax()

if is_open:
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        f"🚨 [용아맥 실전 오픈!]\n\n"
        f"사키님! 기다리시던 {found_date} 예매가 포착되었습니다!\n"
        f"지금 즉시 예매하세요! 🔥\n\n"
        f"👉 링크: {booking_url}"
    )
    send_msg(msg)
