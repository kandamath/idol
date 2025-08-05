import pandas as pd
# CSVファイル読み込み（文字コードに注意）
file_path = "higashiojima.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# 特定の列だけ抽出
df1 = df["取引価格（総額）"]
# 金額を3桁区切りにする
df1 = df1.apply(lambda x: f"{x:,}")
# print(df["取引価格（総額）"])
print(df1)

# 条件フィルタリング（例：価格が5000万円以上）
filtered = df[df["取引価格（総額）"] >= 50000000]
# 金額を3桁区切りにする
filtered["取引価格（総額）"] = filtered["取引価格（総額）"].apply(lambda x: f"{x:,}")
print(filtered)

# 複数条件（かつ・または）
filtered2 = df[
    (df["取引価格（総額）"] >= 50000000) &
    (df["最寄駅：距離（分）"] <= 10)
]
print(filtered2)