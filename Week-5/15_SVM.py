# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score

# df = pd.read_csv('students_week5.csv')
# X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# Y = df['result']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X,Y, test_size = 0.2, random_state= 42, stratify=Y
# )

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.fit_transform(X_test)

# for kernel in ['linear', 'rbf']:
#     model = SVC(kernel=kernel, C = 1.0)
#     model.fit(X_train, Y_train)
#     acc = accuracy_score(Y_test, model.predict(X_test))
#     print(f'SVM ({kernel}) accuracy: {acc:3f}')

# Spam
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv('spam_detection_dataset.csv')
features = [
    "word_freq_free",
    "word_freq_win",
    "word_freq_offer",
    "num_links",
    "num_exclamation",
    "message_length"
]

X = df[features]
Y = df["spam"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.2, random_state = 42, stratify = Y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


for kernel in ['linear', 'rbf']:
    model = SVC(kernel= kernel, C = 1.0)
    model.fit(X_train, Y_train)
    acc = accuracy_score(Y_test, model.predict(X_test))
    print(f'SMV({kernel}) accuracy: {acc: 3f}')

plt.scatter(
    df["word_freq_free"],
    df["word_freq_win"],
    c=df["spam"]
)

plt.xlabel("Word Frequency Free")
plt.ylabel("Word Frequency Win")
plt.title("Spam Detection - SVM Data")

plt.show()

# Disease

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('disease_diagnosis.csv')
X = df[['glucose', 'bmi', 'age', 'blood_pressure', 'cholesterol']]

Y = df['diagnosis']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.2, random_state = 42, stratify = Y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


for kernel in ['linear', 'rbf']:
    model = SVC(kernel= kernel, C = 1.0)
    model.fit(X_train, Y_train)
    acc = accuracy_score(Y_test, model.predict(X_test))
    print(f'SMV({kernel}) accuracy: {acc: 3f}')

encoder = LabelEncoder()

df["diagnosis_encoded"] = encoder.fit_transform(df["diagnosis"])


plt.scatter(
    df["glucose"],
    df["bmi"],
    c=df["diagnosis_encoded"]
)

plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Disease Diagnosis - KNN Data")

plt.show()



# KNN 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
Y = df['result']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state= 42, stratify=Y
)


raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, Y_train)
print('KNN without scaling:', accuracy_score(Y_test, raw.predict(X_test)))
scaler = StandardScaler()
X_train_s, X_test_s = scaler.fit_transform(X_train), scaler.transform(X_test)

for k in [1,3,5,7,9,15,25]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, Y_train)
    acc = accuracy_score(Y_test, knn.predict(X_test_s))
    print(f'K={k:>2}": accuracy = {acc:.3f}')


# Spam

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv('spam_detection_dataset.csv')
features = [
    "word_freq_free",
    "word_freq_win",
    "word_freq_offer",
    "num_links",
    "num_exclamation",
    "message_length"
]

X = df[features]
Y = df["spam"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state= 42, stratify=Y
)


raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, Y_train)
print('KNN without scaling:', accuracy_score(Y_test, raw.predict(X_test)))
scaler = StandardScaler()
X_train_s, X_test_s = scaler.fit_transform(X_train), scaler.transform(X_test)

for k in [1,3,5,7,9,15,25]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, Y_train)
    acc = accuracy_score(Y_test, knn.predict(X_test_s))
    print(f'K={k:>2}: accuracy = {acc:.3f}')

plt.scatter(
    df["word_freq_free"],
    df["word_freq_win"],
    c=df["spam"]
)

plt.xlabel("Word Frequency Free")
plt.ylabel("Word Frequency Win")
plt.title("Spam Detection - KNN Data")

plt.show()


# Disease

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('disease_diagnosis.csv')
X = df[['glucose', 'bmi', 'age', 'blood_pressure', 'cholesterol']]

Y = df['diagnosis']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state= 42, stratify=Y
)


raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, Y_train)
print('KNN without scaling:', accuracy_score(Y_test, raw.predict(X_test)))
scaler = StandardScaler()
X_train_s, X_test_s = scaler.fit_transform(X_train), scaler.transform(X_test)

for k in [1,3,5,7,9,15,25]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, Y_train)
    acc = accuracy_score(Y_test, knn.predict(X_test_s))
    print(f'K={k:>2}: accuracy = {acc:.3f}')

encoder = LabelEncoder()

df["diagnosis_encoded"] = encoder.fit_transform(df["diagnosis"])

plt.scatter(
    df["glucose"],
    df["bmi"],
    c=df["diagnosis_encoded"]
)

plt.xlabel("Glucose")
plt.ylabel("BMI")

plt.title("Disease Diagnosis - KNN Data")

plt.show()