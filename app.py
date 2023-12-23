from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 讀取 .env 文件中的環境變量


app = Flask(__name__)

# 設置你的 OpenAI API 密鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_input = "請使用繁體廣東話回答: " + user_input
        try:
            # 使用 ChatGPT 3.5 模型生成回應
            gpt_response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": user_input}]
            )
            response = gpt_response['choices'][0]['message']['content']
        except Exception as e:
            response = str(e)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)