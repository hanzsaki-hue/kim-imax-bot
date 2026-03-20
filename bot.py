import requests

# 1. 정보 설정
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # '프로젝트 헤일메리'와 'IMAX'가 있는지 먼저 확인
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            
            # 봇이 절대 놓치지 않게 날짜 형식을 다양하게 준비 (오늘 20일 포함)
            # CGV가 어떤 형식을 쓰더라도 이 중 하나에는 걸립니다.
            dates_to_check = [
                ('20260320', '3월 20일'), 
                ('20260325', '3월 25일'), 
                ('20260326', '3월 26일'), 
                ('20260327', '3월 27일')
            ]
            
            for code, name in dates_to_check:
                # 1. 20260320 형식 찾기
                # 2. 혹은 그냥 "20"이라는 숫자가 포함된 예매 버튼 찾기
                if code in html or f'data-date="{code}"' in html or f'PlayDate="{code}"' in html:
                    return True, name
        return False, None
    except:
        return False, None

# --- 실행 ---
is_open, found_date_name = check_imax()

if is_open:
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        f"🚨 [용아맥 정밀 탐지 성공]\n\n"
        f"사키님! {found_date_name} 예매가 포착되었습니다!\n"
        f"지금 바로 예매하세요! 🔥\n\n"
        f"👉 링크: {booking_url}"
    )
    send_telegram(msg)
