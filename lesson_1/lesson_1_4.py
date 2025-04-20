import pandas as pd

# ファイル読み込み
file_path = "lesson_1.csv"
df = pd.read_csv(file_path, encoding="utf-8-sig")
df.columns = df.columns.str.replace("\ufeff", "")  # BOM対策

# --- 並び替え（sort_values） ---
# 価格の高い順に並び替え
df_sorted = df.sort_values(by="取引価格（総額）", ascending=False)
print("▼ 価格の高い順に並び替え")
print(df_sorted[["取引価格（総額）", "面積（㎡）"]].head())

# 面積の小さい順に並び替え
df_sorted_area = df.sort_values(by="面積（㎡）", ascending=True)
print("\n▼ 面積の小さい順に並び替え")
print(df_sorted_area[["取引価格（総額）", "面積（㎡）"]].head())

# --- ダミーで欠損を作ってみる（実際の分析準備の練習用） ---
df.loc[2, "取引価格（総額）"] = None
df.loc[5, "面積（㎡）"] = None
print("\n▼ 一部を欠損にしたデータ")
print(df.head(6))

# --- 欠損値の確認 ---
print("\n▼ 欠損があるか確認（isnull & sum）")
print(df.isnull().sum())

# --- 欠損値の処理 ---
# 方法①: 欠損行を削除
df_dropna = df.dropna()
print("\n▼ 欠損行を削除（dropna）")
print(df_dropna.head())

# 方法②: 平均値で補完（fillna）
mean_price = df["取引価格（総額）"].mean()
mean_area = df["面積（㎡）"].mean()

df_filled = df.copy()
df_filled["取引価格（総額）"] = df_filled["取引価格（総額）"].fillna(mean_price)
df_filled["面積（㎡）"] = df_filled["面積（㎡）"].fillna(mean_area)
print("\n▼ 平均値で補完（fillna）")
print(df_filled.head(6))
