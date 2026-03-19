import requests

# 1. 정보 설정 (개인 톡 성공했던 그 토큰과 단톡방 주소!)
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
        
        # 봇이 헷갈리지 않게 날짜 형식을 아주 다양하게 준비했습니다.
        # 오늘(20일) 테스트용과 목표 날짜(25, 26, 27일)를 모두 넣었어요.
        target_dates = [
            '20', '03/20', '03.20', '3월 20', # 오늘 테스트용 (무조건 걸려야 함)
            '25', '03/25', '03.25', '3월 25', 
            '26', '03/26', '03.26', '3월 26',
            '27', '03/27', '03.27', '3월 27'
        ]
        
        # '프로젝트 헤일메리'와 'IMAX'가 있는지 먼저 확인
        if '프로젝트 헤일메리' in html and 'IMAX' in html:
            for date in target_dates:
                # 페이지 소스 안에 해당 날짜 문구가 하나라도 있으면 발사!
                if date in html:
                    return True
        return False
    except:
        return False

# 실행 부분
if check_imax():
    booking_url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    msg = (
        "🚨 [용아맥 알림] 프로젝트 헤일메리 예매 확인!\n\n"
        "사키님! 설정하신 날짜의 예매가 열린 것 같습니다!\n"
        f"👉 바로가기: {booking_url}"
    )
    send_telegram(msg)
