项目主要内容

  该项目是一个基于Flask框架的聊天机器人应用，旨在通过自然语言处理技术与用户进行交互。项目的主要功能包括用户登录、意图识别、问答系统和小型对话功能。用户可以通过输入问题与聊天机器人进行对话，机器人会根据用户的输入返回相应的回答。具体内容如下：

用户认证模块：

  实现用户的注册、登录和登出功能。用户通过输入用户名和密码进行身份验证，成功后可以访问聊天界面。系统会在用户登录后保存会话信息，确保用户在会话期间的状态保持。

意图识别模块：

  通过训练逻辑回归模型来识别用户输入的意图。使用CountVectorizer[23]将用户的查询转换为特征向量，并利用LogisticRegression进行分类。意图包括“小型对话”、“问题解答”和“错误处理”等。

问答系统模块：

  使用TF-IDF向量化技术和余弦相似度计算来实现问答功能。系统会根据用户的查询在预先准备的问答数据集中寻找最相似的问题，并返回相应的答案。该模块能够处理多种类型的问题，提供准确的回答。

小型对话功能模块：

  通过读取小型对话数据集，机器人能够进行简单的对话，增强用户体验。该功能使得聊天机器人不仅能回答问题，还能进行轻松的闲聊，提升互动性。

前端交互模块：

  使用Vue.js构建动态用户界面，用户可以通过输入框发送消息，系统会实时返回响应。前端设计注重用户体验，确保界面简洁、易用，并支持多种设备的访问。

数据存储与管理：

  项目中使用CSV文件存储问答数据和意图数据，便于后续的更新和维护。可以通过简单的文件操作实现数据的增删改查。

项目思路

用户认证：

  使用Flask的会话管理功能，提供用户登录和登出功能。用户通过输入用户名和密码进行身份验证，成功后可以访问聊天界面。系统会在用户登录后保存会话信息，确保用户在会话期间的状态保持。

意图识别：

  通过训练逻辑回归模型来识别用户输入的意图。使用CountVectorizer[23]将用户的查询转换为特征向量，并利用LogisticRegression进行分类。意图包括“小型对话”和“问题解答”。

问答系统：

  使用TF-IDF向量化技术和余弦相似度计算来实现问答功能。系统会根据用户的查询在预先准备的问答数据集中寻找最相似的问题，并返回相应的答案。

小型对话功能：

  通过读取小型对话数据集，机器人能够进行简单的对话，增强用户体验。

前端交互：

  使用Vue.js[24]构建动态用户界面，用户可以通过输入框发送消息，系统会实时返回响应。

数据库：mysql


运行方式：

  pip安装必要的库：nltk,sklearn,numpy,pandas,flask等

  更改数据库链接中的用户名(root)和密码(123456) 

  运行app.py即可
