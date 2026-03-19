import requests

# 1. 사키님의 진짜 토큰과 단톡방 주소를 직접 넣었습니다.
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    print(response.json()) # 결과 확인용 로그

def check_imax():
    # CGV 용산아이파크몰 페이지 확인
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        # 오늘(20일)은 영화가 이미 열려있으니 '헤일메리'와 'IMAX' 글자는 무조건 있습니다.
        # 복잡한 날짜 조건 다 빼고 이 두 글자만 있으면 True!
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            return True
        return False
    except:
        return False

# 실행 부분
if check_imax():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 테스트] 드디어 연결되었습니다!\n\n"
        "사키님! 이 메시지가 보이면 이제 맘 편히 주무셔도 됩니다.\n"
        f"예매 링크: {booking_url}"
    )
    send_telegram(msg)
