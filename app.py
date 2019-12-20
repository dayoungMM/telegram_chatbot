from flask import Flask , render_template, request
from decouple import config
import requests

app = Flask(__name__)
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = 'https://api.telegram.org/bot'

@app.route('/')
def hello():
    return "Hello World"

@app.route('/write')
def write():
    return render_template('write.html')
@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html') 

@app.route(f'/{token}', methods=["POST"]) #post방식일때 무조건 실행
def telegram():
    # chat_id = request.get_json.
    return "ok", 200


if __name__ == ("__main__"):
    app.run(debug=True)