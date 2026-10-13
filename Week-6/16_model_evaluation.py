# Code 1 — Metrics & Threshold

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, precision_score, recall_score,
                             f1_score, roc_auc_score)
 
df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
 
prob = model.predict_proba(X_test)[:, 1]          # chance of Pass
for threshold in [0.5, 0.3, 0.7]:
    pred = (prob >= threshold).astype(int)        # our own cut-off
    print(f'threshold {threshold}: precision={precision_score(y_test, pred):.2f}'
          f'  recall={recall_score(y_test, pred):.2f}  f1={f1_score(y_test, pred):.2f}')
print(confusion_matrix(y_test, (prob >= 0.5).astype(int)))
print('ROC-AUC:', round(roc_auc_score(y_test, prob), 3))


# Code 2 — Class Imbalance

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score
 
df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = (df['performance'] == 2).astype(int)    # 1 = High performer (only ~20%)
print('Share of High performers:', round(y.mean(), 2))
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
 
models = {'Dummy (always 0)': DummyClassifier(strategy='most_frequent'),
          'Logistic': make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
          'Logistic balanced': make_pipeline(StandardScaler(),
              LogisticRegression(max_iter=1000, class_weight='balanced'))}
for name, m in models.items():
    pred = m.fit(X_train, y_train).predict(X_test)
    print(f'{name:18s} acc={accuracy_score(y_test, pred):.2f}'
          f'  recall={recall_score(y_test, pred):.2f}  f1={f1_score(y_test, pred):.2f}')


# Code 3 — Cross-Validation & GridSearchCV

import pandas as pd
from sklearn.model_selection import (train_test_split, cross_val_score,
                                     GridSearchCV, StratifiedKFold)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
 
df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
 
# 1. Cross-validation: 5 practice tests on TRAIN data only
scores = cross_val_score(make_pipeline(StandardScaler(), SVC()), X_train, y_train, cv=cv)
print('SVM 5 folds:', scores.round(3), '| mean:', round(scores.mean(), 3))
 
# 2. GridSearchCV: try every setting, keep the best CV score
settings = {'max_depth': [2, 3, 4, 5, 6, 8], 'min_samples_leaf': [1, 5, 10, 20]}
grid = GridSearchCV(DecisionTreeClassifier(random_state=42), settings, cv=cv)
grid.fit(X_train, y_train)
print('Best:', grid.best_params_, '| CV:', round(grid.best_score_, 3),
      '| final test:', round(grid.score(X_test, y_test), 3))
