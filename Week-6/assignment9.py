"""
Assignment 9 - Loan Approval Prediction with a Decision Tree.

Flow: load -> inspect -> clean/encode -> split -> train -> evaluate
      -> predict a new applicant and print the decision path.

Improvements over the basic version
    * the tree depth / leaf size / criterion are chosen with 5-fold
      cross-validation (the original depth=3 gini tree is one of the candidates)
    * encoding is done with lookup tables shared by training and prediction
"""

from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.tree import DecisionTreeClassifier

SEED = 42
URL = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/Loan-Approval-Prediction.csv"
LOCAL_FILE = "Loan-Approval-Prediction.csv"          # offline fallback

FILL_WITH_MODE = ["Gender", "Married", "Dependents", "Education",
                  "Self_Employed", "Credit_History", "Loan_Amount_Term"]
ENCODING = {
    "Gender": {"Male": 0, "Female": 1},
    "Married": {"No": 0, "Yes": 1},
    "Education": {"Not Graduate": 0, "Graduate": 1},
    "Self_Employed": {"No": 0, "Yes": 1},
    "Property_Area": {"Rural": 0, "Semiurban": 1, "Urban": 2},
    "Loan_Status": {"N": 0, "Y": 1},
}


def load_data():
    try:
        return pd.read_csv(URL)
    except Exception:
        if Path(LOCAL_FILE).exists():
            print(f"(no internet - using local copy '{LOCAL_FILE}')")
            return pd.read_csv(LOCAL_FILE)
        raise SystemExit(f"Could not download the dataset. Save it as '{LOCAL_FILE}' "
                         f"next to this script and run again.")


def preprocess(df):
    df = df.drop("Loan_ID", axis=1)
    for col in FILL_WITH_MODE:
        df[col] = df[col].fillna(df[col].mode()[0])
    df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
    df["Dependents"] = df["Dependents"].replace("3+", "3").astype(int)
    for col, mapping in ENCODING.items():
        df[col] = df[col].map(mapping)
    return df


def ask(prompt, choices=None, cast=str):
    """input() helper that re-asks until the value is valid."""
    while True:
        raw = input(prompt).strip()
        try:
            value = cast(raw)
        except ValueError:
            print("Invalid number, try again.")
            continue
        if choices is None or value in choices:
            return value
        print("Please enter one of:", ", ".join(map(str, choices)))


def main():
    df = load_data()
    print("Dataset loaded successfully!")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nDataset Shape:")
    print(df.shape)
    print("\nColumn Names:")
    print(df.columns.tolist())
    print("\nDataset Information:")
    df.info()
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    df = preprocess(df)
    print("\nData after preprocessing:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values After Preprocessing:")
    print(df.isnull().sum())

    X, y = df.drop("Loan_Status", axis=1), df["Loan_Status"]
    print("\nFeatures:")
    print(X.columns.tolist())
    print("\nTarget:")
    print("Loan_Status")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=SEED, stratify=y)
    print("\nTraining Data Shape:")
    print(X_train.shape)
    print("\nTesting Data Shape:")
    print(X_test.shape)

    # tree settings are chosen silently by cross-validation (depth 3 / gini is in the grid)
    search = GridSearchCV(
        DecisionTreeClassifier(random_state=SEED),
        {"criterion": ["gini", "entropy"],
         "max_depth": [2, 3, 4, 5, 6],
         "min_samples_leaf": [1, 5, 10, 20]},
        cv=StratifiedKFold(5, shuffle=True, random_state=SEED),
        scoring="accuracy", n_jobs=-1,
    ).fit(X_train, y_train)
    model = search.best_estimator_

    print("\nDecision Tree model trained successfully!")

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("MODEL ACCURACY")
    print("Accuracy:", accuracy)
    print("Accuracy (%):", accuracy * 100)
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, y_pred))
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, y_pred, target_names=["Loan Rejected", "Loan Approved"]))

    # ------------------------------------------------------ new applicant
    print("LOAN APPROVAL PREDICTION")
    print("\nEnter applicant information:")

    applicant = {
        "Gender": ENCODING["Gender"][ask("Gender (Male/Female): ", ENCODING["Gender"])],
        "Married": ENCODING["Married"][ask("Married (Yes/No): ", ENCODING["Married"])],
        "Dependents": ask("Dependents (0/1/2/3): ", {0, 1, 2, 3}, int),
        "Education": ENCODING["Education"][ask("Education (Graduate/Not Graduate): ",
                                                ENCODING["Education"])],
        "Self_Employed": ENCODING["Self_Employed"][ask("Self Employed (Yes/No): ",
                                                        ENCODING["Self_Employed"])],
        "ApplicantIncome": ask("Applicant Income: ", cast=float),
        "CoapplicantIncome": ask("Co-applicant Income: ", cast=float),
        "LoanAmount": ask("Loan Amount: ", cast=float),
        "Loan_Amount_Term": ask("Loan Amount Term: ", cast=float),
        "Credit_History": ask("Credit History (1 = Good, 0 = Bad): ", {0.0, 1.0}, float),
        "Property_Area": ENCODING["Property_Area"][ask("Property Area (Rural/Semiurban/Urban): ",
                                                       ENCODING["Property_Area"])],
    }
    user_data = pd.DataFrame([applicant])[X.columns]
    prediction = model.predict(user_data)[0]

    print("\nDecision Path:")
    path = model.decision_path(user_data)
    leaf = model.apply(user_data)[0]
    tree = model.tree_
    for node in path.indices[path.indptr[0]:path.indptr[1]]:
        if node == leaf:
            continue
        print(f"{X.columns[tree.feature[node]]} <= {tree.threshold[node]:.2f}")

    print("LOAN PREDICTION RESULT")
    if prediction == 1:
        print("LOAN APPROVED")
        print("According to the Decision Tree model, the applicant is likely to get the loan.")
    else:
        print("LOAN REJECTED")
        print("According to the Decision Tree model, the applicant is unlikely to get the loan.")


if __name__ == "__main__":
    main()
