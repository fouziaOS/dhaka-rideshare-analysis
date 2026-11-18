"""Machine Learning: predict the ride fare (fare_bdt).

Features: distance, duration, hour, surge + one-hot vehicle and area.
Models compared: Linear Regression and Random Forest.
Run from the project root:  python src/ml_model.py
"""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error

df = pd.read_csv("data/rideshare_trips.csv")
X = pd.get_dummies(df[["distance_km", "duration_min", "hour", "surge_multiplier", "vehicle", "area"]], columns=["vehicle", "area"])
y = df["fare_bdt"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rows = []
preds = {}
for name, model in [("Linear Regression", LinearRegression()),
                    ("Random Forest", RandomForestRegressor(n_estimators=200, random_state=42))]:
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    preds[name] = p
    rows.append({"model": name, "R2": round(r2_score(y_test, p), 3),
                 "RMSE (BDT)": round(root_mean_squared_error(y_test, p), 2)})
    print(name, "-> R2:", rows[-1]["R2"], "| RMSE:", rows[-1]["RMSE (BDT)"], "BDT")

pd.DataFrame(rows).to_csv("outputs/tables/model_results.csv", index=False)
plt.figure(figsize=(6.5, 6)); plt.scatter(y_test, preds["Random Forest"], alpha=0.45, color="#2e75b6")
lims = [y_test.min(), y_test.max()]; plt.plot(lims, lims, "r--")
plt.title("Actual vs Predicted Fare (Random Forest)"); plt.xlabel("Actual fare (BDT)"); plt.ylabel("Predicted fare (BDT)")
plt.tight_layout(); plt.savefig("outputs/charts/actual_vs_predicted_fare.png"); plt.close()
print("Saved outputs/tables/model_results.csv and outputs/charts/actual_vs_predicted_fare.png")
