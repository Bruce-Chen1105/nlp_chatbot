from flask import Flask, request, render_template, jsonify
from pre_processing import pStemmer
from intent_matching import train_intent_model, predict_intent
from small_talk import stResponse
from question_answering import qaResponse

app = Flask(__name__)

# 预加载意图匹配模型
vectorizer, classifier = train_intent_model("data/COMP3074-CW1-Intent-Dataset.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message', '')
    intent = predict_intent(user_input, vectorizer, classifier)

    if intent == "Small Talk":
        response = stResponse(user_input)
    elif intent == "Question":
        response = qaResponse(user_input)
    else:
        response = "S.A.M: GRRRRRRRRR 我无法理解你的意思 :/ 请重试。"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)