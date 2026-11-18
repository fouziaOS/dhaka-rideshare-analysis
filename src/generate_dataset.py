"""Generate the dataset for this project (synthetic data, NumPy seed-based)."""
import numpy as np, pandas as pd, os
rng = np.random.default_rng(42)
os.makedirs("data", exist_ok=True)
n = 600
areas = ["Uttara", "Mirpur", "Dhanmondi", "Gulshan", "Banani", "Motijheel", "Mohammadpur", "Badda"]
area_p = [0.16, 0.15, 0.14, 0.12, 0.10, 0.13, 0.11, 0.09]
vehicles = ["Bike", "Car", "CNG"]
veh_p = [0.45, 0.35, 0.20]
base_rate = {"Bike": 28, "Car": 55, "CNG": 40}
area = rng.choice(areas, n, p=area_p)
vehicle = rng.choice(vehicles, n, p=veh_p)
dates = pd.date_range("2025-01-01", periods=180, freq="D")
date = rng.choice(dates, n)
_hp = np.array([0.01,0.01,0.01,0.01,0.02,0.03,0.05,0.07,0.08,0.07,0.05,0.05,0.05,0.05,0.04,0.04,0.05,0.07,0.08,0.07,0.05,0.03,0.02,0.01]); hour = rng.choice(range(24), n, p=_hp/_hp.sum())
distance = np.round(rng.gamma(2.2, 2.6, n), 2)
peak = np.isin(hour, [8, 9, 17, 18, 19])
speed = np.where(peak, rng.normal(13, 3, n), rng.normal(24, 5, n)).clip(6, 45)
duration = np.round(distance / speed * 60 + rng.normal(3, 1.5, n), 1).clip(4, None)
surge = np.where(peak, rng.uniform(1.2, 1.8, n), rng.uniform(1.0, 1.15, n)).round(2)
fare = np.round(np.array([base_rate[v] for v in vehicle]) * distance * surge + 30, 2)
rating = np.round((4.6 - 0.012 * duration + rng.normal(0, 0.35, n)).clip(2.5, 5.0), 1)
df = pd.DataFrame({"date": pd.Series(date).dt.date, "hour": hour, "area": area, "vehicle": vehicle,
                   "distance_km": distance, "duration_min": duration, "fare_bdt": fare,
                   "surge_multiplier": surge, "rating": rating})
df.to_csv("data/rideshare_trips.csv", index=False)
print("Saved", len(df), "trips")
