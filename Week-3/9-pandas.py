# Pandas and data Frame
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# data = {'name': ['Ali', 'Sara', 'Zain'],
#         'marks': [85, 92, 78]}

# df = pd.DataFrame(data)
# print(df)

# data = {'name': ['Ali', 'Ahmad', 'Sara', 'Hassan'],
#         'city': ['Lahore', 'Multan', 'Faisalabad', 'Karachi'],
#         'score': [66, 77, 88, 99]}

# df = pd.DataFrame(data)
# print(df)
# print(df.shape)

# Series VS DataFrame

# s = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
# print(s)

# df = pd.DataFrame({'name': ['Ali', 'Sara', 'Zain'],
#         'marks': [85, 92, 78]})
# print(df['name'])

# s = pd.Series(['Lahore', 'Multan', 'Faisalabad', 'Karachi', 'Islamabad'], index = ['c1', 'c2', 'c3', 'c4', 'c5'])
# print(s)

# df = pd.DataFrame({'name': ['Ali', 'Sara', 'Zain'],
#         'marks': [85, 92, 78]})
# print(df['name'])
# print(df['marks'])

# # Selection & Indexding

# df = pd.DataFrame({'name': ['Ali', 'Sara', 'Zain', 'Ahmad', 'Hassan'],
#         'marks': [85, 92, 78, 69, 55]})

# print(df[df['marks'] > 75])

# print(df[['name','marks']])

# # Data Frame operaton (sort, unique, apply)

# df = pd.DataFrame({'name': ['Ali', 'Sara', 'Zain', 'Ahmad', 'Hassan'],
#         'marks': [85, 92, 78, 69, 55]})
# df['grade'] = df['marks'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')

# print(df.sort_values('marks', ascending=False))



# df = pd.DataFrame({'name': ['Ali', 'Sara', 'Zain', 'Ahmad', 'Hassan'],
#         'marks': [85, 92, 78, 69, 55]})
# df['rank'] = df['marks'].apply(lambda x: 'High' if x >= 80 else 'Loww')

# print(df.sort_values('marks', ascending=False))

# print(df.value_counts('marks', ascending=False))

# # Handling Missing Values

# df = pd.DataFrame({'a': [1,2,None], 'b': [4,None,6]})

# print(df.isnull())
# print(df.fillna(0))


# df = pd.DataFrame({'a': [2,3,None], 'b': [6,None,8]})

# print(df.isnull())
# print(df.fillna(0))
# print(df.dropna())

# # GroupBy

# sales = pd.DataFrame({'dept': ['IT', 'IT', 'HR', 'HR'],
#                       'sales': [100, 150,80,90]})

# print(sales.groupby('dept')['sales'].prod())
# print(sales.groupby('dept')['sales'].sum())



# sales = pd.DataFrame({'categories': ['IT', 'IT', 'HR', 'HR'],
#                       'sales': [100, 150,80,90]})

# print(sales.groupby('categories')['sales'].mean())

# print(sales.groupby('categories')['sales'].count())


#  # Merging & Concatenate


# a = pd.DataFrame({'id':[1,2,3], 'name': ['Ali', 'Zain', 'Hassan']})
# b = pd.DataFrame({'id':[1,2,4], 'marks': [80, 75, 65]})

# print(pd.merge(a,b, on = 'id', how = 'inner'))



# a = pd.DataFrame({'id':[1,2,3], 'name': ['Ali', 'Zain', 'Hassan']})
# b = pd.DataFrame({'id':[1,2,4], 'marks': [80, 75, 65]})

# print(pd.merge(a,b, on = 'id', how = 'left'))


# a = pd.DataFrame({'id':[1,2,3], 'name': ['Ali', 'Zain', 'Hassan']})
# b = pd.DataFrame({'id':[1,2,4], 'marks': [80, 75, 65]})

# print(pd.concat(a,b, on = 'id'))


# a = pd.DataFrame({'id':[1,2,3], 'name': ['Ali', 'Zain', 'Hassan']})
# b = pd.DataFrame({'id':[1,2,4], 'marks': [80, 75, 65]})

# print(pd.concat([a,b]))


# Pandas Plaoting

# df = pd.DataFrame({'dept': ['IT', 'HR', 'Sales'],
#                       'revenue': [100, 150,80]})
# df.plot(x = 'dept', y ='revenue', kind = 'bar')
# plt.show()


# df = pd.DataFrame({'month':['Jan', 'Feb', 'Mar', 'Apr'],
#                    'sales':[2000, 3000, 1000, 4000]})

# df.plot(x = 'month', y = 'sales', kind = 'line')
# plt.show()

# df = pd.DataFrame({'month':['Jan', 'Feb', 'Mar', 'Apr'],
#                    'sales':[2000, 3000, 1000, 4000]})

# df.plot(x = 'month', y = 'sales', kind = 'bar')
# plt.show()


# Seaborn

# df = pd.DataFrame({'dept': ['IT', 'HR', 'Sales'],
#                       'revenue': [100, 150,80]})

# sns.boxplot(x = 'dept', y = 'revenue', data = df)
# plt.show()


# df = pd.DataFrame({
#     'exam_score': [45, 52, 58, 60, 65, 67, 70, 72, 75, 78,
#                    80, 82, 85, 88, 90, 92, 95, 98]
# })

# sns.histplot(data=df, x='exam_score', bins=6)

# plt.show()


# df = pd.DataFrame({
#     'dept': ['IT', 'IT', 'IT',
#              'HR', 'HR', 'HR',
#              'Sales', 'Sales', 'Sales'],
#     'revenue': [100, 120, 150,
#                 130, 150, 170,
#                 70, 80, 100]
# })

# sns.boxplot(x='dept', y='revenue', data=df)

# plt.show()

# df = pd.DataFrame({'age':[20,25,30,35],
#                     'income':[30,40,55,65],
#                     'score':[70,75,80,85]})

# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.show()


df = pd.DataFrame({
    'hours_studied': [2, 4, 5, 7, 8, 10],
    'attendance': [60, 65, 70, 80, 85, 95],
    'assignments': [3, 4, 5, 6, 8, 9],
    'exam_score': [55, 60, 65, 72, 80, 90]
})

sns.heatmap(df.corr(), annot=True, cmap= 'coolwarm')
plt.show()