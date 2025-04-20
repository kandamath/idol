# === 4.3: テストデータで予測 ===
import joblib
import numpy as np

# テストデータと学習済みモデルの読み込み
X_test = joblib.load("../output/X_test.pkl")
model = joblib.load("../output/random_forest_trained.pkl")

# 予測
y_pred = model.predict(X_test)

# 小数第2位まで四捨五入
y_pred = np.round(y_pred, 2)

# 予測結果を保存
joblib.dump(y_pred, "../output/y_pred.pkl")

# 確認
print("✅ 予測が完了しました！")
print("▼ 予測結果の一部:")
print(y_pred[:5])
