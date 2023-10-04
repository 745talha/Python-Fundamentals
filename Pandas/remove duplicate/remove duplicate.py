#houseprice file get from https://www.kaggle.com/datasets/yasserh/housing-prices-dataset/   and added duplicate values for testing

import pandas as pd

df = pd.read_csv('houseprice.csv')
new_df=df.drop_duplicates()
print(new_df)
print(new_df.head(10))

