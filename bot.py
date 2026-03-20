import requests
from bs4 import BeautifulSoup

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
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 블로그 팁: 모든 영화 제목을 가져와서 공백을 제거하고 비교합니다.
        movies = soup.select('.info-movie > a > strong')
        
        for movie in movies:
            title = movie.get_text().strip() # 앞뒤 공백 제거
            
            if '프로젝트 헤일메리' in title:
                # 해당 영화 근처에 'IMAX' 글자가 있는지 확인
                parent = movie.find_parent('div', class_='col-times')
                if 'IMAX' in str(parent):
                    # 블로그 팁: 날짜 버튼 데이터 확인
                    # 오늘(20)과 목표일(25, 26, 27)이 예매 가능한 버튼으로 있는지 확인
                    days = soup.select('.date-list li')
                    for day in days:
                        date_val = day.get('data-date') # 예: 20260320
                        if date_val in ['20260320', '20260325', '20260326', '20260327']:
                            return True, date_val
        return False, None
    except:
        return False, None

# 실행
is_open, found_date = check_imax()
if is_open:
    pretty_date = f"{found_date[4:6]}월 {found_date[6:8]}일"
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = f"🚨 [용아맥 정밀 탐지]\n\n사키님! {pretty_date} 예매가 포착되었습니다!\n지금 바로 접속하세요! 🔥\n👉 {booking_url}"
    send_telegram(msg)
