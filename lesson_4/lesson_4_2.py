# === 4.2: モデルの学習 ===
import joblib

# 学習用データとモデルの読み込み
X_train = joblib.load("../output/X_train.pkl")
y_train = joblib.load("../output/y_train.pkl")
model = joblib.load("../output/random_forest_model.pkl")

# モデルを学習
model.fit(X_train, y_train)

# 学習済みモデルを保存
joblib.dump(model, "../output/random_forest_trained.pkl")

print("✅ モデルの学習が完了しました！")
