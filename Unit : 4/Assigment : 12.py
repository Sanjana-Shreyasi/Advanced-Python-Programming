#Assigment : 12 ; Unit : 4

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. load the dataset

df = pd.read_csv("customer_churn.csv")

print("First 5 records:")
print(df.head())


# 2. basic information about the dataset

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()


# 3. check missing values

print("\nMissing values:")
print(df.isnull().sum())


# 4. check and remove duplicate records

print("\nDuplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()


# 5. handle missing values

# fill numerical values with mean

num_columns = df.select_dtypes(include=np.number).columns

for col in num_columns:
    df[col] = df[col].fillna(df[col].mean())

# fill categorical values with mode

cat_columns = df.select_dtypes(include="object").columns

for col in cat_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# 6. summary statistics

print("\nSummary statistics:")
print(df.describe())


# 7. find average age of customers

print("\nAverage age:")
print(np.mean(df["Age"]))


# 8. find average monthly charges

print("\nAverage monthly charges:")
print(np.mean(df["MonthlyCharges"]))


# 9. find average customer tenure

print("\nAverage tenure:")
print(np.mean(df["Tenure"]))


# 10. count customers based on churn

print("\nCustomer churn count:")
print(df["Churn"].value_counts())


# 11. calculate churn percentage

churn_percent = df["Churn"].value_counts(normalize=True) * 100

print("\nChurn percentage:")
print(churn_percent)


# 12. show customer churn using bar graph

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of customers")
plt.show()


# 13. show age distribution

plt.hist(df["Age"], bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of customers")
plt.show()


# 14. show monthly charges distribution

plt.hist(df["MonthlyCharges"], bins=10)

plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly charges")
plt.ylabel("Number of customers")
plt.show()


# 15. compare churn based on contract

contract_churn = pd.crosstab(df["Contract"], df["Churn"])

print("\nChurn based on contract:")
print(contract_churn)

contract_churn.plot(kind="bar")

plt.title("Churn Based on Contract")
plt.xlabel("Contract type")
plt.ylabel("Number of customers")
plt.xticks(rotation=0)
plt.show()


# 16. compare churn based on internet service

internet_churn = pd.crosstab(df["InternetService"], df["Churn"])

print("\nChurn based on internet service:")
print(internet_churn)

internet_churn.plot(kind="bar")

plt.title("Churn Based on Internet Service")
plt.xlabel("Internet service")
plt.ylabel("Number of customers")
plt.xticks(rotation=0)
plt.show()


# 17. find average monthly charges based on churn

average_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage charges based on churn:")
print(average_charges)

average_charges.plot(kind="bar")

plt.title("Average Monthly Charges Based on Churn")
plt.xlabel("Churn")
plt.ylabel("Average monthly charges")
plt.xticks(rotation=0)
plt.show()


# 18. find correlation between numerical columns

num_columns = df.select_dtypes(include=np.number).columns

correlation = df[num_columns].corr()

print("\nCorrelation between numerical columns:")
print(correlation)

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)),
           correlation.columns, rotation=45)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Correlation Matrix")
plt.show()


# 19. save the cleaned dataset

df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully")

#Output
'''First 5 records:
  CustomerID  Gender   Age  Tenure  MonthlyCharges  TotalCharges        Contract InternetService Churn
0    CUST001    Male  35.0      32           60.45       1902.06  Month-to-month     Fiber optic    No
1    CUST002  Female  43.0      71          108.78       7557.37        Two year             DSL   Yes
2    CUST003    Male  61.0      59          105.09       6373.08  Month-to-month     Fiber optic    No
3    CUST004    Male  51.0      28          113.56       3030.42  Month-to-month     Fiber optic   Yes
4    CUST005    Male  27.0      66           98.53       6438.35        One year     Fiber optic    No


Shape of dataset:
(102, 9)


Column names:
Index(['CustomerID', 'Gender', 'Age', 'Tenure', 'MonthlyCharges',
       'TotalCharges', 'Contract', 'InternetService', 'Churn'],
      dtype='object')


Dataset information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 102 entries, 0 to 101
Data columns (total 9 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   CustomerID       102 non-null    object
 1   Gender           102 non-null    object
 2   Age              101 non-null    float64
 3   Tenure           102 non-null    int64
 4   MonthlyCharges   100 non-null    float64
 5   TotalCharges     102 non-null    float64
 6   Contract         102 non-null    object
 7   InternetService  100 non-null    object
 8   Churn            102 non-null    object
dtypes: float64(3), int64(1), object(5)
memory usage: 7.3+ KB


Missing values:
CustomerID         0
Gender             0
Age                1
Tenure             0
MonthlyCharges     2
TotalCharges       0
Contract           0
InternetService    2
Churn              0


Duplicate records:
2


Missing values after cleaning:
CustomerID         0
Gender             0
Age                0
Tenure             0
MonthlyCharges     0
TotalCharges       0
Contract           0
InternetService    0
Churn              0


Summary statistics:
              Age      Tenure  MonthlyCharges  TotalCharges
count  100.000000  100.000000      100.000000    100.000000
mean    43.939394   36.610000       70.256939   2622.314900
std     14.410867   22.585816       28.791512   2159.684502
min     18.000000    1.000000       20.520000      0.000000
25%     31.750000   19.000000       48.282500    920.927500
50%     43.969697   37.000000       68.615000   2260.040000
75%     56.000000   57.250000       94.507500   3508.445000
max     70.000000   72.000000      119.460000   8175.240000


Average age:
43.93939393939394


Average monthly charges:
70.25693877551019


Average tenure:
36.61


Customer churn count:
Churn
No     60
Yes    40
Name: count, dtype: int64


Churn percentage:
Churn
No     60.0
Yes    40.0
Name: proportion, dtype: float64


Churn based on contract:
Churn           No  Yes
Contract
Month-to-month  26   28
One year        22    5
Two year        12    7


Churn based on internet service:
Churn            No  Yes
InternetService
DSL              17   14
Fiber optic      28   18
No               15    8


Average charges based on churn:
Churn
No     67.191949
Yes    74.854423
Name: MonthlyCharges, dtype: float64


Correlation between numerical columns:
                     Age    Tenure  MonthlyCharges  TotalCharges
Age             1.000000 -0.124690       -0.160918     -0.121472
Tenure         -0.124690  1.000000        0.080082      0.828392
MonthlyCharges -0.160918  0.080082        1.000000      0.535457
TotalCharges   -0.121472  0.828392        0.535457      1.000000


Cleaned dataset saved successfully'''