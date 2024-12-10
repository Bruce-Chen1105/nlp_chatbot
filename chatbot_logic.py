from pre_processing import pStemmer
from intent_matching import intentMatching
from small_talk import stResponse
from question_answering import qaResponse

def get_response(user_message):
    """
    根据用户输入生成聊天机器人的回复。
    """
    stoplist = ['bye', 'goodbye']

    # 退出判断
    if user_message.lower() in stoplist:
        return "ByeBye"

    # 意图匹配
    intent = intentMatching(pStemmer(user_message))
    print(f"Detected Intent: {intent}")  # 调试用

    # 根据意图生成回复
    if intent == "Small Talk":
        return stResponse(user_message)
    elif intent == "Question":
        return qaResponse(user_message)
    else:
        return "GRRRRRRRRR I can't work out what you mean :/ REBOOT... REBOOT..."
