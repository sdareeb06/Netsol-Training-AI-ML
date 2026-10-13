# EDA Guided Practice

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# df = sns.load_dataset('tips')
# print(df)
# print(df.shape)
# print(df.head())
# print(df.dtypes)

# print(df.describe())

# df.value_counts()
# print(df['day'].value_counts())

# sns.histplot(x = 'total_bill', data = df)
# sns.histplot(df['total_bill'])
# plt.show()

# p = df.groupby('day')['total_bill'].mean()

# print(p)

# print('The Highest average bill: ', p.max())


# df.plot(kind = 'scatter', x = 'total_bill', y = 'tip')
# sns.scatterplot(x = 'total_bill', y = 'tip', data = df)
# plt.show()


# a = df[['total_bill', 'tip', 'size']]
# sns.heatmap(a.corr(), annot=True, cmap= 'coolwarm')
# plt.show()


df = pd.read_csv('Books_Data_Clean.csv')
# print(df)

# a = df.isnull()
# print(a)

# print(df.fillna(0))
# print(df.dropna())

# sns.histplot(x = 'units sold', data = df)
# sns.histplot(df['units sold'])
# plt.show()

# p = df.groupby('genre')['units sold'].mean()

# print(p)

# print('The Highest average bill: ', p.max())


# df.plot(kind = 'scatter', x = 'units sold', y = 'genre')
# sns.scatterplot(x = 'units sold', y = 'genre', data = df)
# plt.show()


a = df[['units sold', 'sales rank']]
sns.heatmap(a.corr(), annot=True, cmap= 'coolwarm')
plt.show()

