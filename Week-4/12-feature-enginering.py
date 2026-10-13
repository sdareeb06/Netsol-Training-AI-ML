# Feature Enginering 
import pandas as pd
import numpy as np
from sklearn.pipeline import pipeline
from sklearn.linear_model import LinearRegrastion
from sklearn.preprocessing import StandardScaler
# df = pd.DataFrame({'height_cm': [170, 100, 160],
#                    'weight_kg': [65, 80, 55]})
# df['bmi'] = df['weight_kg'] / (df['height_cm']**2)
# print(df)

# df = pd.DataFrame({'price': [170, 100, 160],
#                    'quantity': [5, 7, 4]})
# df['total_cost'] = df['price'] * (df['quantity'])
# print(df)


# df = pd.DataFrame({'total_income': [17000, 10000, 160000],
#                    'total_expenses': [50000, 70000, 40000]})
# df['savings_rate'] =( df['total_income'] - (df['total_expenses']) / df['total_income']) *100
# print(df)


# Feature Selection & Binning

# df = pd. DataFrame({'study_hrs': [1,2,3,4,5],
#                     'slepp_hrs': [8,7,6,8,7],
#                     'marks': [50,55,65,70,85]})
# print(df.corr()['marks'])

# ages = pd.Series([5,17,25,45,68,80])
# print(pd.cut(ages,bins = [0,12,19,56,100],
#              labels = ['Child', 'Teen', 'Adult', 'Seniors']))

# df = pd.DataFrame({
#     'study_hrs': [1, 2, 3, 4, 5],
#     'sleep_hrs': [8, 7, 6, 8, 7],
#     'screen_time': [6, 5, 4, 3, 2],
#     'attendance': [60, 65, 70, 80, 90]
# })
# print(df.corr()['attendence'])

grades = pd.Series([20,30,40,50,60,70,80,90,])
print(pd.cut(grades,bins = [0,33,60,80,100],
             labels = ['Fail', 'Pass', 'Merit', 'Distinction']))

# ETL & Batch & Stream Processing
# OLTP  And OLAP
# ETL Script likhni hai

# Automatic With Skelearn Pipeline

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([40, 45, 52, 60, 68, 75, 82, 90])

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('regression', LinearRegression())
])

pipe.fit(x, y)

predict = pipe.predict([[9]])

print(predict[0])


# Sure — here is a complete solution for the task using a small dataset, `StandardScaler`, and `LinearRegression` inside an `sklearn` `Pipeline`.


import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Small dataset
# Features: [hours_studied, hours_slept]
X = np.array([
    [1, 7],
    [2, 6],
    [3, 8],
    [4, 7],
    [5, 6],
    [6, 8],
    [7, 7],
    [8, 6],
    [9, 8],
    [10, 7]
])

# Target: exam score
y = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

# Train the pipeline
pipeline.fit(X_train, y_train)

# Evaluate on test data
score = pipeline.score(X_test, y_test)
print("R² score:", score)

# Predict one new value
# Example: student studied 6 hours and slept 7 hours
new_student = np.array([[6, 7]])

prediction = pipeline.predict(new_student)

print("Predicted exam score:", prediction[0])


 ### Why use a Pipeline?

#  The pipeline automatically performs:

# ```
# Input data
#     ↓
# StandardScaler
#     ↓
# LinearRegression
#     ↓
# Prediction


#  So you **don't need to manually scale the training and test data separately**.

 ### What could go wrong if you scale training and test data separately?

#  For example, doing this independently:


scaler_train = StandardScaler()
X_train_scaled = scaler_train.fit_transform(X_train)

scaler_test = StandardScaler()
X_test_scaled = scaler_test.fit_transform(X_test)  


#  means the test data gets a **different mean and standard deviation** from the training data. The model was trained using one scaling system but evaluated using another.

#  The correct approach is:


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # ✅


#  A `Pipeline` handles this automatically and also helps prevent accidentally fitting preprocessing on the test data.

