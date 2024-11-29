import pandas as pd
import numpy as np
data_path = '/mnt/data/AB_NYC_2019.csv'
data = pd.read_csv(r'D:\Desktop\task2\data.csv')
print("Data preview:\n", data.head())
print("\nData Information:\n")
print(data.info())
print("\nMissing Values:\n", data.isnull().sum())
data = data.dropna(subset=['name', 'host_name'])
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())
print("\nNumber of duplicate rows:", data.duplicated().sum())
data = data.drop_duplicates()
data['neighbourhood'] = data['neighbourhood'].str.lower()
data['room_type'] = data['room_type'].str.lower()
data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
data = remove_outliers(data, 'price')
print("\nFinal Missing Values Check:\n", data.isnull().sum())
print("\nFinal Dataset Shape:", data.shape)
print("\nData Summary:\n", data.describe())
cleaned_data_path = 'AB_NYC_2019_cleaned.csv'
data.to_csv(cleaned_data_path, index=False)
print("\nCleaned data saved to:", cleaned_data_path)

