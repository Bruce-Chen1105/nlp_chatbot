from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from pre_processing import pStemmer
from intent_matching import train_intent_model, predict_intent
from small_talk import stResponse
from question_answering import qaResponse

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 请替换为您的秘密密钥

# 示例用户数据，实际应用中请从数据库获取
USERS = {
    'user1': 'password1',
    'user2': 'password2'
}

# 预加载意图匹配模型
vectorizer, classifier = train_intent_model("data/COMP3074-CW1-Intent-Dataset.csv")

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if USERS.get(username) == password:
            session['logged_in'] = True
            session['username'] = username
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': '用户名或密码错误。'})
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/chat', methods=['POST'])
def chat():
    if not session.get('logged_in'):
        return jsonify({'response': '请先登录。', 'intent': 'Error'})
    
    user_input = request.form.get('message', '')
    intent = predict_intent(pStemmer(user_input), vectorizer, classifier)

    if intent == "Small Talk":
        response = stResponse(user_input)
    elif intent == "Question":
        response = qaResponse(user_input)
    else:
        response = "S.A.M: GRRRRRRRRR 我无法理解你的意思 :/ 请重试。"
    
    return jsonify({'response': response, 'intent': intent})

if __name__ == '__main__':
    app.run(debug=True)