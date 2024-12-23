from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from pre_processing import pStemmer
from intent_matching import train_intent_model, predict_intent
from small_talk import stResponse
from question_answering import qaResponse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 请替换为您的秘密密钥
# 修改为 MySQL 数据库连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/chatbot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# 创建数据库表
with app.app_context():
    db.create_all()

# 预加载意图匹配模型
vectorizer, classifier = train_intent_model("data/COMP3074-CW1-Intent-Dataset.csv")

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # 如果未登录，重定向到登录页面
    return render_template('index.html')  # 如果已登录，返回主页

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        user = User.query.filter_by(username=username).first()  # 查询用户

        if user and check_password_hash(user.password, password):  # 验证密码
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # 检查用户名是否已存在
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'success': False, 'message': '用户名已存在，请选择其他用户名。'})

        hashed_password = generate_password_hash(password)  # 哈希密码

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': '注册成功！'})
    return render_template('register.html')  # 返回注册页面

if __name__ == '__main__':
    app.run(debug=True)