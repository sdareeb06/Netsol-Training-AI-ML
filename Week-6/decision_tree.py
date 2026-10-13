# Decision Tree

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
Y = df['result']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

for depth in [3, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, Y_train)
    print(f'max_depth={depth}: train = {tree.score(X_train, Y_train):.3f}'
           f' | test = {tree.score(X_test, Y_test):.3f}')

small_tree = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_train, Y_train)
print(export_text(small_tree, feature_names=list(X.columns)))


# Random Forest

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
Y = df['result']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
forest = RandomForestClassifier(n_estimators=200, random_state=42)
forest.fit(X_train, Y_train)
print(f'Random Forest test accuracy:', round(forest.score(X_test, Y_test), 3))

importances = pd.Series(forest.feature_importances_, index=X.columns)
print(importances.sort_values(ascending=False).round(3))