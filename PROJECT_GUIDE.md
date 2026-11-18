# PROJECT GUIDE — Dhaka Ride-Sharing Analysis

A complete explanation of this project for beginners: what it is, what every file
and column means, how the code works step by step, and how to explain it in a viva.

## 1. What is this project?
Analyzing 600 ride-sharing trips in Dhaka — fares, traffic, peak hours and earnings by area. It is a full data-analysis workflow: create data → clean and explore it →
group and summarize → draw charts → write honest insights. Dataset size: 600 trips.

## 2. Files in this project
- `README.md` — project summary with the key results and chart images.
- `PROJECT_GUIDE.md` — this guide.
- `requirements.txt` — the Python libraries needed (pandas, numpy, matplotlib).
- `src/generate_dataset.py` — builds the dataset with NumPy random numbers (fixed seed = same data every run).
- `src/analysis.py` — the main analysis code.
- `data/rideshare_trips.csv` — the dataset (created by generate_dataset.py).
- `dhaka-rideshare-analysis.ipynb` — the same analysis as a Jupyter notebook.
- `outputs/charts/` — chart images:
- `avg_fare_by_vehicle.png`
- `distance_vs_fare.png`
- `earnings_by_area.png`
- `trips_by_hour.png`
- `outputs/tables/` — summary tables (CSV):
- `avg_duration_by_area.csv`
- `avg_fare_by_vehicle.csv`
- `correlation_matrix.csv`
- `earnings_by_area.csv`
- `trips_by_hour.csv`
- `outputs/insights.md` — the key findings in plain words.

## 3. Dataset columns explained
| Column | Meaning |
|---|---|
| date | Trip date |
| hour | Hour of day (0–23) |
| area | Pickup area in Dhaka |
| vehicle | Bike / Car / CNG |
| distance_km | Trip distance in km |
| duration_min | Trip duration in minutes |
| fare_bdt | Fare paid in BDT |
| surge_multiplier | Surge pricing multiplier |
| rating | Passenger rating (1–5) |

## 4. How to run it (step by step)
1. Open a terminal inside this project folder.
2. Install the libraries: `pip install -r requirements.txt`
3. Create the data: `python src/generate_dataset.py`
4. Run the analysis: `python src/analysis.py`
5. Look inside `outputs/` — charts, tables and insights are created there.
6. Or open `dhaka-rideshare-analysis.ipynb` in Jupyter and run the cells one by one.

## 5. How the code works
**generate_dataset.py** — sets a fixed NumPy seed, chooses categories with realistic
probabilities, builds numeric columns from related formulas (so the data behaves like
real life), assembles a Pandas DataFrame and saves it as CSV.

**analysis.py** — loads the CSV with Pandas, then:
1. `groupby(...)` summaries → saved as tables in `outputs/tables/`.
2. A correlation matrix for the numeric columns.
3. Four Matplotlib charts → saved in `outputs/charts/`.
4. The most important numbers are written into `outputs/insights.md`.

## 6. Key results
# Key Insights — Dhaka Ride-Sharing Analysis

- Dataset: 600 trips across 8 Dhaka areas.
- Highest total earnings area: **Uttara** (35,260 BDT).
- Most expensive vehicle on average: **Car** (427 BDT per trip).
- Busiest hour of the day: **8:00**.
- Correlation between distance and fare: **0.84** (fare mainly follows distance).
- Average trip rating: **4.32 / 5**.

## 7. How to read the charts
- **Bar charts** compare groups (which group is biggest / most expensive / slowest).
- **Line charts** show change over time or hour — look for peaks.
- **Histograms** show how values are spread (most common range, rare extremes).
- **Scatter plots** show relationships between two numbers — an upward or downward
  cloud means the two move together (check the correlation value in the tables).

## 8. Viva / interview questions
**Q: Why is the fare highest in peak hours?**
A: Surge pricing: demand is high and traffic is slow at 8–9 AM and 5–7 PM, so the multiplier rises to 1.2–1.8×.

**Q: Which correlation is the strongest here?**
A: Distance vs fare — fare is calculated mainly from distance, so the correlation is close to 1.

**Q: How could a driver earn more?**
A: Work peak hours in high-demand areas like the top-earning area in this dataset.

## 9. Honest note
The data is synthetic (computer-generated with realistic patterns), made for learning
and portfolio demonstration. The workflow, code and analysis method are exactly what
would be used with real data.
