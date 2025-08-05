import pandas as pd

# CSVファイル読み込み（文字コードに注意）
file_path = "higashiojima.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# カラムの追加
df["単価（円/㎡）"] = df["取引価格（総額）"] / df["面積（㎡）"]
print("▼ 単価（円/㎡）カラムの追加")
print(df[["取引価格（総額）", "面積（㎡）", "単価（円/㎡）"]].head())
print("単価を小数第2位までのフォーマットに変更")
df["単価（円/㎡）"] = df["単価（円/㎡）"].apply(lambda x: f"{x:,.2f}")
df["取引価格（総額）"] = df["取引価格（総額）"].apply(lambda x: f"{x:,}")
print("▼ 単価（円/㎡）のフォーマット変更後")
print(df[["取引価格（総額）", "面積（㎡）", "単価（円/㎡）"]].head())

# データ型をfloatからintに変更する
df["単価（円/㎡）"] = df["単価（円/㎡）"].str.replace(",", "").astype(float).astype(int)
print("▼ 単価（円/㎡）のデータ型をintに変更")
print(df[["取引価格（総額）", "面積（㎡）", "単価（円/㎡）"]].head())
df["単価（円/㎡）"] = df["単価（円/㎡）"].apply(lambda x: f"{x:,}")
print("▼ 面積（㎡）のフォーマット変更後")
print(df[["取引価格（総額）", "面積（㎡）", "単価（円/㎡）"]].head())

# 結果をCSVファイルに保存
output_file_path = "higashiojima_with_unit_price.csv"
df.to_csv(f"../output/{output_file_path}", index=False, encoding="utf-8-sig")
print(f"結果を {output_file_path} に保存しました。")