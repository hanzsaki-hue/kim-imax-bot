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
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        # 1. '프로젝트 헤일메리'가 있는지 확인 (제목이 다를 수 있으니 '헤일메리'만 검색)
        if '헤일메리' in html:
            # 2. 날짜 정밀 검사
            # '20260320' 뿐만 아니라 '20'이라는 숫자만 있어도 일단 찾도록 범위를 넓힙니다.
            target_dates = [
                ('20260320', '3월 20일'),
                ('20260325', '3월 25일'),
                ('20260326', '3월 26일'),
                ('20260327', '3월 27일')
            ]
            
            for code, name in target_dates:
                # CGV 소스 코드에서 날짜를 나타내는 여러 패턴을 다 뒤집니다.
                if code in html or f'date="{code[-2:]}"' in html or f'data-date="{code}"' in html:
                    return True, name
        return False, None
    except:
        return False, None

# --- 실행 ---
is_open, found_date = check_imax()

if is_open:
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = f"🚨 [용아맥 정밀 탐지]\n\n사키님! {found_date} 예매가 포착되었습니다!\n지금 바로 접속하세요! 🔥\n👉 {booking_url}"
    send_telegram(msg)
else:
    # [중요] 만약 영화를 못 찾았다면, 봇이 살아있다는 걸 보여주기 위해 테스트 메시지 한 번만 쏩니다.
    # 성공하면 이 아래 줄은 나중에 지워주세요!
    send_telegram("🔍 [봇 감시 중] 코드는 잘 돌아가는데, 홈페이지에서 날짜를 아직 못 찾았어요.")
