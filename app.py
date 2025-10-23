from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML 템플릿을 코드 안에 바로 작성 (간단 예시용)
HTML_PAGE = """
<!doctype html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <title>간단한 챗봇</title>
    <style>
        body { font-family: 'Pretendard', sans-serif; margin: 40px; background: #f5f5f5; }
        .chat-box { background: white; border-radius: 10px; padding: 20px; width: 400px; margin: 0 auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .message { margin: 10px 0; }
        .user { text-align: right; color: #007bff; }
        .bot { text-align: left; color: #333; }
        form { display: flex; margin-top: 20px; }
        input[type=text] { flex: 1; padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
        button { margin-left: 10px; padding: 10px 15px; border: none; border-radius: 5px; background: #007bff; color: white; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="chat-box">
        <h2>💬 간단한 챗봇</h2>
        {% if user_text %}
            <div class="message user"><b>당신:</b> {{ user_text }}</div>
            <div class="message bot"><b>챗봇:</b> {{ bot_response }}</div>
        {% endif %}
        <form method="post">
            <input type="text" name="user_text" placeholder="메시지를 입력하세요..." autofocus required>
            <button type="submit">보내기</button>
        </form>
    </div>
</body>
</html>
"""

def get_bot_response(user_text):
    """간단한 규칙 기반 응답 함수"""
    user_text = user_text.strip()

    if "안녕" in user_text:
        return "안녕하세요! 만나서 반가워요 😊"
    elif "이름" in user_text:
        return "저는 Flask로 만든 간단한 챗봇이에요!"
    elif "날씨" in user_text:
        return "오늘은 맑고 기분 좋은 날이에요 ☀️"
    elif "종료" in user_text:
        return "대화를 종료하려면 브라우저를 닫으시면 됩니다 👋"
    else:
        return "그건 아직 잘 모르겠어요 😅"

@app.route("/", methods=["GET", "POST"])
def chat():
    user_text = None
    bot_response = None

    if request.method == "POST":
        user_text = request.form["user_text"]
        bot_response = get_bot_response(user_text)

    return render_template_string(HTML_PAGE, user_text=user_text, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
🚀 실행 방법
Flask 설치

bash
코드 복사
pip install flask
app.py 파일 실행

bash
코드 복사
python app.py
