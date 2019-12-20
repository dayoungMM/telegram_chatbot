from decouple import config
import requests

token = config('TELEGRAM_BOT_TOKEN')
url = 'https://api.telegram.org/bot'
ngrok_url = 'https://ff83fec2.ngrok.io'
data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}').text
print(data)