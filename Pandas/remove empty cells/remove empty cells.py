#houseprice file get from https://www.kaggle.com/datasets/yasserh/housing-prices-dataset/ and remove values from some cells for testing
import pandas as pd

df = pd.read_csv('houseprice.csv')

new_df = df.dropna()

print(new_df)
print(new_df.head(10))
