import pandas as pd

# CSVファイル読み込み
file_path = "higashiojima.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# DataFrameの基本情報確認
print(df.head())    # 先頭5件
print(df.tail())    # 最後5件
print(df.shape)   # 行数・列数
print(df.columns)  # カラム名
print(df.info())    # データ型など
print(df.describe())  # 統計量
