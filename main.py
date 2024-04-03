import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('clean_churn.csv')
# Histogram of Credit Score
plt.hist(df['CreditScore'], bins=10)
plt.title('Histogram of Credit Score')
plt.xlabel('Credit Score')
plt.ylabel('Frequency')
plt.show()
# Pie Chart of Geography
category_counts = df['Geography'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Geography Distribution')
plt.show()
# Pie Chart of Gender
category_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.show()
# Histogram of Age
plt.hist(df['Age'], bins=10)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
# Histogram of Tenure
plt.hist(df['Tenure'], bins=10)
plt.title('Histogram of Tenure')
plt.xlabel('Tenure')
plt.ylabel('Frequency')
plt.show()
# Pie Chart of Tenure
category_counts = df['Tenure'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Tenure Distribution')
plt.show()
# Histogram of Balance
plt.hist(df['Balance'], bins=10)
plt.title('Histogram of Balance')
plt.xlabel('Balance')
plt.ylabel('Frequency')
plt.show()
# Pie Chart of Number of Products
category_counts = df['NumOfProducts'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Number of Products')
plt.show()
# Pie Chart of Whether Has Credit Card
labels1 = ['Yes' if value == 1 else 'No' for value in df['HasCrCard']]
yes_count1 = labels1.count('Yes')
no_count1 = labels1.count('No')
pie_values1 = [yes_count1, no_count1]
pie_labels1 = ['Yes', 'No']
plt.figure(figsize=(8, 8))
plt.pie(pie_values1, labels=pie_labels1, autopct='%1.1f%%', startangle=140)
plt.title('Whether Has Credit Card')
plt.show()
# Pie Chart of Whether Is Active Member
labels2 = ['Yes' if value == 1 else 'No' for value in df['IsActiveMember']]
yes_count2 = labels2.count('Yes')
no_count2 = labels2.count('No')
pie_values2 = [yes_count2, no_count2]
pie_labels2 = ['Yes', 'No']
plt.figure(figsize=(8, 8))
plt.pie(pie_values2, labels=pie_labels2, autopct='%1.1f%%', startangle=140)
plt.title('Whether Is Active Member')
plt.show()
# Histogram of estimated salary
plt.hist(df['EstimatedSalary'], bins=10)
plt.title('Histogram of Estimated Salary')
plt.xlabel('Estimated Salary')
plt.ylabel('Frequency')
plt.show()
# Pie Chart of Whether Exits
labels3 = ['Yes' if value == 1 else 'No' for value in df['Exited']]
yes_count3 = labels3.count('Yes')
no_count3 = labels3.count('No')
pie_values3 = [yes_count3, no_count3]
pie_labels3 = ['Yes', 'No']
plt.figure(figsize=(8, 8))
plt.pie(pie_values3, labels=pie_labels3, autopct='%1.1f%%', startangle=140)
plt.title('Whether Exits')
plt.show()
# Heatmap
corr = df.corr()
sns.heatmap(corr, annot=False)
plt.title('Heatmap')
plt.show()