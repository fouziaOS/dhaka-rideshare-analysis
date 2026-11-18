"""Main analysis: tables, charts and insights. Run from the project root: python src/analysis.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
os.makedirs("outputs/charts", exist_ok=True); os.makedirs("outputs/tables", exist_ok=True)
df = pd.read_csv("data/rideshare_trips.csv")
# Tables
df.groupby("vehicle")["fare_bdt"].agg(["count", "mean"]).round(2).to_csv("outputs/tables/avg_fare_by_vehicle.csv")
df.groupby("area")["fare_bdt"].agg(["count", "mean", "sum"]).round(2).to_csv("outputs/tables/earnings_by_area.csv")
df.groupby("hour").size().rename("trips").to_csv("outputs/tables/trips_by_hour.csv")
df.groupby("area")["duration_min"].mean().round(2).rename("avg_duration_min").to_csv("outputs/tables/avg_duration_by_area.csv")
corr = df[["distance_km", "duration_min", "fare_bdt", "rating"]].corr().round(2)
corr.to_csv("outputs/tables/correlation_matrix.csv")
# Charts
plt.figure(figsize=(8, 4.5)); df.groupby("vehicle")["fare_bdt"].mean().plot(kind="bar", color="#2e75b6")
plt.title("Average Fare by Vehicle"); plt.ylabel("Fare (BDT)"); plt.tight_layout(); plt.savefig("outputs/charts/avg_fare_by_vehicle.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("hour").size().plot(kind="line", marker="o", color="#2e75b6")
plt.title("Trips by Hour of Day"); plt.xlabel("Hour"); plt.ylabel("Trips"); plt.tight_layout(); plt.savefig("outputs/charts/trips_by_hour.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("area")["fare_bdt"].sum().sort_values().plot(kind="barh", color="#548235")
plt.title("Total Earnings by Area"); plt.xlabel("BDT"); plt.tight_layout(); plt.savefig("outputs/charts/earnings_by_area.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.scatter(df["distance_km"], df["fare_bdt"], alpha=0.4, color="#7030a0")
plt.title("Distance vs Fare"); plt.xlabel("Distance (km)"); plt.ylabel("Fare (BDT)"); plt.tight_layout(); plt.savefig("outputs/charts/distance_vs_fare.png"); plt.close()
# Insights
top_area = df.groupby("area")["fare_bdt"].sum().idxmax()
top_veh = df.groupby("vehicle")["fare_bdt"].mean().idxmax()
peak_hour = int(df.groupby("hour").size().idxmax())
c = df["distance_km"].corr(df["fare_bdt"])
ins = f"""# Key Insights — Dhaka Ride-Sharing Analysis

- Dataset: {len(df)} trips across {df['area'].nunique()} Dhaka areas.
- Highest total earnings area: **{top_area}** ({df.groupby('area')['fare_bdt'].sum().max():,.0f} BDT).
- Most expensive vehicle on average: **{top_veh}** ({df.groupby('vehicle')['fare_bdt'].mean().max():,.0f} BDT per trip).
- Busiest hour of the day: **{peak_hour}:00**.
- Correlation between distance and fare: **{c:.2f}** (fare mainly follows distance).
- Average trip rating: **{df['rating'].mean():.2f} / 5**.
"""
open("outputs/insights.md", "w").write(ins)
print(ins)
