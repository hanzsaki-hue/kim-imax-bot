import requests

token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(url, params=params)

def check_imax():
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        # 블로그 권장: 브라우저처럼 보이게 헤더 설정
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        # 1. 영화 제목 핵심 키워드 확인
        if '헤일메리' in html and 'IMAX' in html:
            
            # 2. 블로그의 핵심 비법: data-date 속성을 직접 조준
            # 오늘(20)과 목표일(25, 26, 27)
            target_dates = ['20260320', '20260325', '20260326', '20260327']
            
            for date in target_dates:
                # 'data-date="20260320"' 이라는 정확한 형식이 HTML에 있는지 확인
                if f'data-date="{date}"' in html:
                    return True, date
                    
        return False, None
    except:
        return False, None

# --- 실행 ---
is_open, found_date = check_imax()

if is_open:
    # 예: 20260320 -> 20일
    day_only = found_date[-2:]
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    
    msg = (
        f"🚨 [용아맥 실전 탐지 성공!]\n\n"
        f"사키님! {day_only}일 예매 데이터가 포착되었습니다!\n"
        f"지금 바로 CGV로 달려가세요! 🎬\n\n"
        f"👉 링크: {booking_url}"
    )
    send_telegram(msg)
