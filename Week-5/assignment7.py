"""
Assignment 7 - SVM and KNN on Spam Detection and Disease Diagnosis.

Printed output is the same as the original assignment. Accuracy is higher because
  * the scaler is fitted on the TRAIN data only (never re-fitted on the test set)
  * spam uses all message features, not only six
  * C (SVM) is picked silently with 5-fold cross-validation
  * KNN uses distance-weighted votes on the spam data
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

SEED = 42
CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
K_VALUES = [1, 3, 5, 7, 9, 15, 25]

SPAM = dict(knn_weights="distance", file="spam_detection_dataset.csv", target="spam", features=None,
            plot=("word_freq_free", "word_freq_win", "Word Frequency Free", "Word Frequency Win"))
DISEASE = dict(knn_weights="uniform", file="disease_diagnosis.csv", target="diagnosis",
               features=["glucose", "bmi", "age", "blood_pressure", "cholesterol"],
               plot=("glucose", "bmi", "Glucose", "BMI"))


def load_split(cfg):
    df = pd.read_csv(cfg["file"])
    features = cfg["features"] or [c for c in df.columns if c != cfg["target"]]
    X, y = df[features], df[cfg["target"]]
    return (df, *train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y))


def scatter(df, cfg, title):
    x_col, y_col, x_label, y_label = cfg["plot"]
    colours = df[cfg["target"]]
    if not pd.api.types.is_numeric_dtype(colours):
        colours = LabelEncoder().fit_transform(colours)
    plt.scatter(df[x_col], df[y_col], c=colours)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def run_svm(cfg, title):
    df, X_train, X_test, y_train, y_test = load_split(cfg)
    for kernel in ["linear", "rbf"]:
        pipe = make_pipeline(StandardScaler(), SVC(kernel=kernel))
        best = GridSearchCV(pipe, {"svc__C": [0.1, 1, 10, 100], "svc__gamma": ["scale", 0.01, 0.1, 0.5]
                                   if kernel == "rbf" else ["scale"]},
                            cv=CV, n_jobs=-1).fit(X_train, y_train)
        print(f"SMV({kernel}) accuracy: {best.score(X_test, y_test): 3f}")
    scatter(df, cfg, title)


def run_knn(cfg, title):
    df, X_train, X_test, y_train, y_test = load_split(cfg)
    raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
    print("KNN without scaling:", raw.score(X_test, y_test))
    for k in K_VALUES:
        knn = make_pipeline(StandardScaler(),
                            KNeighborsClassifier(n_neighbors=k, weights=cfg["knn_weights"])).fit(X_train, y_train)
        print(f"K={k:>2}: accuracy = {knn.score(X_test, y_test):.3f}")
    scatter(df, cfg, title)


if __name__ == "__main__":
    # Spam Detection - SVM, Disease Diagnosis - SVM, Spam Detection - KNN, Disease Diagnosis - KNN
    run_svm(SPAM, "Spam Detection - SVM Data")
    run_svm(DISEASE, "Disease Diagnosis - KNN Data")
    run_knn(SPAM, "Spam Detection - KNN Data")
    run_knn(DISEASE, "Disease Diagnosis - KNN Data")
