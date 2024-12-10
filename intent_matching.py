# intent_matching.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from pre_processing import pStemmer

def train_intent_model(csv_path):
    df = pd.read_csv("data/COMP3074-CW1-Intent-Dataset.csv")
    intents = df['Intent']
    queries = df['Query']
    queries = [pStemmer(query) for query in queries]

    # Create a list of input and output pairs for the text classifier
    X = queries
    y = intents

    # Create a bag of words representation of the text data
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create the logistic regression text classifier
    classifier = LogisticRegression()

    # Train the classifier on the training data
    classifier.fit(X_train, y_train)

    return vectorizer, classifier

def predict_intent(user_input, vectorizer, classifier):
    user_input_processed = pStemmer(user_input)
    user_input_vectorized = vectorizer.transform([user_input_processed])
    prediction = classifier.predict(user_input_vectorized)
    return prediction[0]