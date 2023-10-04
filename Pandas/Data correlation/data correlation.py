#houseprice file get from https://www.kaggle.com/datasets/yasserh/housing-prices-dataset/
import pandas as pd

df = pd.read_csv('houseprice.csv')
print("Dataset")
print(df)
print("Dataset columns correlatin")
print(df.corr())