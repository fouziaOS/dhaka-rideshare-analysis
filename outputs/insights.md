# Key Insights — Dhaka Ride-Sharing Analysis

- Dataset: 600 trips across 8 Dhaka areas.
- Highest total earnings area: **Uttara** (35,260 BDT).
- Most expensive vehicle on average: **Car** (427 BDT per trip).
- Busiest hour of the day: **8:00**.
- Correlation between distance and fare: **0.84** (fare mainly follows distance).
- Average trip rating: **4.32 / 5**.

## Machine Learning — prediction model
Predict the ride fare (`fare_bdt`) from distance, duration, hour, surge, vehicle and area.

| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.881 | 79.57 BDT |
| Random Forest | 0.925 | 63.15 BDT |

**Best model: Random Forest.** Random Forest predicts a fare within about **63 BDT** of the real fare on average (R² = 0.925).

Run it yourself: `python src/ml_model.py` (needs scikit-learn, already in `requirements.txt`).
Results are saved in `outputs/tables/model_results.csv`.
