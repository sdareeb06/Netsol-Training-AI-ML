"""
Assignment 8 - Spam detection with Naive Bayes (and Logistic Regression)

Part 1 (main)     : Enron e-mail spam  -> TF-IDF + MultinomialNB, then a
                    predict_spam() helper.   Needs  enron_spam_data.csv
Part 2 (optional) : Logistic Regression on the same TF-IDF features
Part 3 (numeric)  : spam_detection_dataset.csv -> GaussianNB and a
                    head-to-head of 4 classifiers.

Part 3 also runs automatically when enron_spam_data.csv is not present,
so the script always prints something useful.
"""

import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix,
                             f1_score, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

SEED = 42
ENRON_FILE = "enron_spam_data.csv"
NUMERIC_FILE = "spam_detection_dataset.csv"

RUN_LOGISTIC_REGRESSION = False      # Part 2 (was commented out in the original)
RUN_NUMERIC_DEMO = False             # Part 3 (forced on if the Enron file is missing)


# ----------------------------------------------------------------- text part
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)       # links
    text = re.sub(r"\S+@\S+", "", text)              # e-mail addresses
    text = re.sub(r"[^a-zA-Z\s]", " ", text)         # digits / symbols
    return re.sub(r"\s+", " ", text).strip()


def load_enron(path):
    df = pd.read_csv(path)[["Subject", "Message", "Spam/Ham"]]
    df["text"] = (df["Subject"].fillna("") + " " + df["Message"].fillna("")).apply(clean_text)
    df["spam"] = df["Spam/Ham"].map({"spam": 1, "ham": 0})
    return df.dropna(subset=["spam"])


def make_vectorizer():
    # unigrams + bigrams, sub-linear tf and rare-word removal give cleaner features
    return TfidfVectorizer(stop_words="english", ngram_range=(1, 2),
                           sublinear_tf=True, min_df=2, max_features=50000)


def naive_bayes_spam(df):
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["spam"], test_size=0.2, random_state=SEED, stratify=df["spam"])

    vectorizer = make_vectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = MultinomialNB(alpha=0.1).fit(X_train_tfidf, y_train)
    pred = model.predict(X_test_tfidf)

    print("Accuracy:", accuracy_score(y_test, pred))
    print("\nClassification Report:")
    print(classification_report(y_test, pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, pred))

    def predict_spam(message):
        features = vectorizer.transform([clean_text(message)])
        return "Spam" if model.predict(features)[0] == 1 else "Ham"

    email = "Congratulations! You have won a free prize. Click here now!"
    print("\nPrediction:", predict_spam(email))
    return X_train_tfidf, X_test_tfidf, y_train, y_test


def logistic_regression_spam(X_train, X_test, y_train, y_test):
    model = LogisticRegression(max_iter=1000, C=10).fit(X_train, y_train)
    pred = model.predict(X_test)
    cm = confusion_matrix(y_test, pred)

    print("=" * 50)
    print("Logistic Regression Results")
    print("=" * 50)
    print(f"Accuracy  : {accuracy_score(y_test, pred):.3f}")
    print(f"Precision : {precision_score(y_test, pred):.3f}")
    print(f"Recall    : {recall_score(y_test, pred):.3f}")
    print(f"F1-Score  : {f1_score(y_test, pred):.3f}")
    print("\nConfusion Matrix:")
    print(cm)
    print("\nConfusion Matrix Details:")
    print("TN =", cm[0][0])
    print("FP =", cm[0][1])
    print("FN =", cm[1][0])
    print("TP =", cm[1][1])


# -------------------------------------------------------------- numeric part
def numeric_spam_demo():
    df = pd.read_csv(NUMERIC_FILE)
    X, y = df.drop("spam", axis=1), df["spam"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED, stratify=y)

    model = GaussianNB().fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))

    print("\nAll 4 classifiers head-to-head")
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "SVM (linear)": SVC(kernel="linear", C=10),
        "KNN (K=5)": KNeighborsClassifier(5),
        "Naive Bayes": GaussianNB(),
    }
    for name, clf in models.items():
        pipe = make_pipeline(StandardScaler(), clf).fit(X_train, y_train)
        print(f"{name:20s} accuracy = {pipe.score(X_test, y_test):.3f}")


# ---------------------------------------------------------------------- main
if __name__ == "__main__":
    enron_available = Path(ENRON_FILE).exists()

    if enron_available:
        data = load_enron(ENRON_FILE)
        splits = naive_bayes_spam(data)
        if RUN_LOGISTIC_REGRESSION:
            print()
            logistic_regression_spam(*splits)
    else:
        print(f"'{ENRON_FILE}' not found - running the numeric spam dataset instead.\n")

    if RUN_NUMERIC_DEMO or not enron_available:
        numeric_spam_demo()
