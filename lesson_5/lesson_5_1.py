# === 5.1: y_test と y_pred の読み込み ===
import joblib

# 保存済みの予測結果と正解データを読み込み
y_test = joblib.load("../output/y_test.pkl")
y_pred = joblib.load("../output/y_pred.pkl")

# 確認出力
print("✅ y_test, y_pred の読み込み完了")
print("▼ y_test の先頭5件:")
print(y_test[:5].values)
print("▼ y_pred の先頭5件:")
print(y_pred[:5])
