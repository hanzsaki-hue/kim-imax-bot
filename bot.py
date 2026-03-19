import requests

# 사키님의 정보를 직접 입력합니다 (테스트용)
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "-5022610945" 

def send_telegram(message):
    # 텔레그램 서버로 직접 요청을 보냅니다
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    print(response.json()) # 결과가 로그에 남습니다

# 영화 상관없이 무조건 메시지를 쏩니다
msg = "🚨 [용아맥 최종 테스트] 프로젝트 헤일메리! 사키님, 여자친구분 이 메시지가 보이면 드디어 성공입니다!"
send_telegram(msg)

