# === 6.1: comparison.csv を読み込み ===
import pandas as pd

df = pd.read_csv("../output/comparison.csv")
print("✅ comparison.csv の読み込み完了")
print(df.head())
