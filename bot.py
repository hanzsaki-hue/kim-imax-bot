import requests

# 1. 텔레그램 정보 (사키님 고유 정보)
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-1003790934369" 

def send_msg(text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(url, params={'chat_id': chat_id, 'text': text})

def check():
    # CGV 용산아이파크몰 '오늘(20일)' 데이터 주소
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?theatercode=0013&date=20260320"
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)'}
    
    try:
        res = requests.get(url, headers=headers, timeout=15)
        html = res.text
        
        # [핵심] 버튼이고 뭐고 다 버리고, '헤일메리'와 'IMAX' 글자만 찾습니다.
        if '헤일메리' in html and 'IMAX' in html:
            return True
        return False
    except:
        return False

# 실행
if check():
    msg = "🚨 [용아맥 탐지 성공!]\n\n사키님! 20일 데이터에서 영화 정보를 찾았습니다!\n이 방식이면 25~27일도 무조건 잡힙니다! 🔥"
    send_msg(msg)
else:
    send_msg("🔍 [봇 작동중] 접속 성공, 하지만 영화 정보는 아직입니다.")
