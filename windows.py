import tkinter as tk
from tkinter import scrolledtext
from chatbot_logic import get_response  # 你之前封装的聊天逻辑函数


class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot - S.A.M")

        # 聊天记录显示区
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", width=60, height=20)
        self.chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.chat_display.tag_config("user", foreground="blue")
        self.chat_display.tag_config("bot", foreground="green")

        # 用户输入框
        self.user_input = tk.Entry(root, width=50)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        # 发送按钮
        self.send_button = tk.Button(root, text="Send", command=self.handle_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        self.root.bind("<Return>", lambda event: self.handle_message())  # 绑定回车键发送消息

        # 初始化欢迎语
        self.add_message("S.A.M: Hi nice to meet you, I'm S.A.M")

    def add_message(self, message):
        """
        将消息添加到聊天记录显示区。
        """
        self.chat_display.configure(state="normal")
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see(tk.END)

    def handle_message(self):
        """
        处理用户输入并生成聊天机器人的回复。
        """
        user_message = self.user_input.get().strip()
        if user_message:
            # 显示用户消息
            self.add_message(f"You: {user_message}")

            # 获取机器人回复
            bot_response = get_response(user_message)
            self.add_message(f"S.A.M: {bot_response}")

            # 清空输入框
            self.user_input.delete(0, tk.END)


# 启动 Tkinter 应用
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
