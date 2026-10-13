# Code 1 Gussian NB
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score, confusion_matrix

# df = pd.read_csv('students_week5.csv')

# X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# Y = df['result']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size= 0.2, random_state= 42, stratify= Y
# )

# model = GaussianNB()
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)
# print('Accuracy:', accuracy_score(Y_test, pred))
# print(confusion_matrix(Y_test, pred))

# new_student = X_test.iloc[[0]]
# print('Pass Probability: ', model.predict_proba(new_student)[0][1].round(2))

# Code 2 All 4 Classifiers Head-to-Head

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('students_week5.csv')

X = df.drop(columns= ['student_id', 'final_score', 'result', 'performance'])
Y = df['result']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.2, random_state= 42, stratify= Y
)

models = {'Logistic Regression': LogisticRegression(max_iter= 1000),
          'SVM (RBF)': SVC(), 'KNN (K=5)': KNeighborsClassifier(5),
          "Naive Bayes": GaussianNB()}
for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(X_train, Y_train)
    print(f'{name:20s} accuracy = {pipe.score(X_test, Y_test):.3f}')