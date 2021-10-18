import pandas as pd

df = pd.read_csv(r'data\hacker_news.csv')

first_5_rows = df.head()
print(first_5_rows)

last_5_rows = df.tail()
print(last_5_rows)