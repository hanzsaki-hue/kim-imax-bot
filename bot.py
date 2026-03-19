import requests

# 1. 사키님의 진짜 토큰과 개인 ID를 직접 넣었습니다.
token = "8586869049:AAHr9gr2LmutAHDAWBYBOXmBLDO0m_11Z2U"
chat_id = "7083498727" 

def send_telegram(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    # 실행 결과를 깃허브 로그에 남깁니다 (디버깅용)
    print(response.json()) 

# 무조건 사키님 개인 톡으로 발사!
msg = "🚨 [개인 톡 성공] 사키님! 이 메시지가 보이면 봇 열쇠(토큰)는 완벽합니다! 이제 단톡방 주소만 맞추면 끝이에요!"
send_telegram(msg)
