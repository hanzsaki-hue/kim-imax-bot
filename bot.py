import requests

token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    print(response.json()) # 깃허브 로그에 성공/실패 이유가 남습니다

def check_imax():
    url = "http://m.cgv.co.kr/WebApp/Reservation/TimeTable.aspx?theatercode=0013"
    try:
        response = requests.get(url)
        html = response.text
        
        # '3월'이라는 글자는 오늘 날짜 페이지에 무조건 있습니다.
        # 이게 안 걸리면 CGV 서버 접속 자체가 안 된 거예요.
        if '프로젝트 헤일메리' in html and 'IMAX' in html and '3월' in html:
            return True
        return False
    except:
        return False

if check_imax():
    msg = "🚨 [용아맥 단톡방 성공] 사키님! 드디어 단톡방 연결에 성공했습니다! 🎬"
    send_telegram(msg)
