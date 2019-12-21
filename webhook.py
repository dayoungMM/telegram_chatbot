from decouple import config
import requests

token = config('TELEGRAM_BOT_TOKEN')
url = 'https://api.telegram.org/bot'
paw_url = 'https://dayoungmmmmmm.pythonanywhere.com' #pythonanywhere.com에 url을 만들어서 paw_url로 연결
# ngrok_url = '<ngrok_url 주소>'  # ngrok_url로 webhook주소를 설정하고 싶은 경우
data = requests.get(f'{url}{token}/setwebhook?url={paw_url}/{token}').text  #get 방식으로 텔레그램 서버에 request
#초기에 한번 텔레그램 서버에 request하면 setwebhook?url이 자동 저장되어있어서 다음부터 알아서 그 url로 실행된다
print(data)
