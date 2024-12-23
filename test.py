import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from pre_processing import pStemmer

def train_and_evaluate_intent_model(csv_path):
    # 读取数据集
    df = pd.read_csv(csv_path)
    intents = df['Intent']
    queries = df['Query']
    queries = [pStemmer(query) for query in queries]

    X = queries
    y = intents

    # 拆分数据集为训练集和测试集（80%训练，20%测试）
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # 初始化 CountVectorizer
    vectorizer = CountVectorizer()

    # 拟合并转换训练数据
    X_train_vect = vectorizer.fit_transform(X_train)

    # 转换测试数据
    X_test_vect = vectorizer.transform(X_test)

    # 初始化并训练逻辑回归模型
    classifier = LogisticRegression(max_iter=1000, solver='liblinear')
    classifier.fit(X_train_vect, y_train)

    # 在测试集上进行预测
    y_pred = classifier.predict(X_test_vect)

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"模型准确率: {accuracy:.2f}")

    # 打印详细的分类报告
    print("\n分类报告：")
    print(classification_report(y_test, y_pred))

    # 打印混淆矩阵
    print("混淆矩阵：")
    print(confusion_matrix(y_test, y_pred))

    return vectorizer, classifier

if __name__ == '__main__':
    train_and_evaluate_intent_model("data/COMP3074-CW1-Intent-Dataset.csv")
    # 可以选择将训练好的模型和向量器保存以供后续使用