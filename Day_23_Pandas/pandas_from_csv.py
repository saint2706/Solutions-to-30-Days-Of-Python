from pathlib import Path

import pandas as pd

resource_dir = Path(__file__).resolve().parent
data_path = resource_dir.parent / "data" / "hacker_news.csv"

df = pd.read_csv(data_path)

first_5_rows = df.head()
# print(first_5_rows)

last_5_rows = df.tail()
# print(last_5_rows)

title_series = df.iloc[:, 2]
# print(title_series)

# print(df.shape)

python_title = df.loc[df["title"].str.contains("Python", case=False)]
# print(python_title)

js_title = df.loc[df["title"].str.contains("JavaScript", case=False)]
# print(js_title)

# print(df.describe())
