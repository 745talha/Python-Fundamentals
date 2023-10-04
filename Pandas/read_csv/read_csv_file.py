#houseprice file get from https://www.kaggle.com/datasets/yasserh/housing-prices-dataset/
import pandas as pd

df = pd.read_csv('houseprice.csv')
#print dataframe
print(df)

#using to_string() to print the entire DataFrame.
print(df.to_string())