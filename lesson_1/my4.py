import pandas as pd

# CSVファイル読み込み（文字コードに注意）
file_path = "higashiojima.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# 並べかえ
# 価格の高い順に並べ替え
df_sorted = df.sort_values(by="取引価格（総額）", ascending=False)
print("▼ 価格の高い順に並べ替え")
print(df_sorted[["取引価格（総額）", "面積（㎡）", "建築年"]].head())

# 面積の小さい順に並べ替え
df_sorted_area = df.sort_values(by="面積（㎡）", ascending=True)
print("\n▼ 面積の小さい順に並べ替え")
print(df_sorted_area[["取引価格（総額）", "面積（㎡）", "建築年"]].head())

# ダミーで欠損を作ってみる（実際の分析準備の練習用）
df.loc[2, "取引価格（総額）"] = None
df.loc[5, "面積（㎡）"] = None
print("\n▼ 一部を欠損にしたデータ")
print(df.head(6))

# 欠損値の確認
print("\n▼ 欠損があるか確認（isnull & sum）")
print(df.isnull().sum())

# 欠損値の処理
# 事前処理として、不要カラムを削除する
df = df.drop(columns=["間取り", "建物の構造", "用途", "今後の利用目的", "都市計画", "建ぺい率（％）", "容積率（％）", "改装", "取引の事情等"], errors='ignore', axis=1)

# 方法1: 欠損行を削除
df_dropna = df.dropna()
print("\n▼ 欠損行を削除（dropna）")
print(df_dropna)
print(df_dropna.head())
## 取引価格の高い順に並べ替え
df_dropna_sorted = df_dropna.sort_values(by="取引価格（総額）", ascending=False)
print("\n▼ 取引価格の高い順に並べ替え")
print(df_dropna_sorted[["取引価格（総額）", "面積（㎡）", "建築年"]].head())
## 面積の狭い順に並び替え
df_dropna_sorted_area = df_dropna.sort_values(by="面積（㎡）", ascending=True)
print("\n▼ 面積の狭い順に並び替え")
print(df_dropna_sorted_area[["取引価格（総額）", "面積（㎡）", "建築年"]].head())

# 方法2: 平均値で補完（fillna）
mean_price = df["取引価格（総額）"].mean()
mean_area = df["面積（㎡）"].mean()
df_filled = df.copy()
df_filled["取引価格（総額）"] = df_filled["取引価格（総額）"].fillna(mean_price)
df_filled["面積（㎡）"] = df_filled["面積（㎡）"].fillna(mean_area)
print("\n▼ 平均値で補完（fillna）")
print(df_filled.head(6))
print(f"取引価格の平均: {mean_price}, 面積の平均: {mean_area}")