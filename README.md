# NYC Airbnb Data Mining (2019)

> *Exploring New York City's 2019 Airbnb market with pandas: pricing, host activity, and review patterns across neighbourhoods.*

---

## Project Overview

This project performs **data mining and exploratory analysis** on the 2019 New York City Airbnb open dataset (~49,000 listings) using Python and pandas. It answers a set of structured business questions about the NYC short-term rental market — median pricing by borough, listing concentration by host, neighbourhood-level price summaries — and builds a reusable filtering function plus a price-category visualization.

The analysis works entirely with pandas filtering, grouping, and aggregation, finishing with a combined bar-and-line chart that compares listing volume against review activity across price tiers.

---

## Assignment Background

This project fulfils the **Data Mining in Python** assignment, which uses the public *New York City Airbnb Open Data (2019)* (originally from Kaggle). The brief is organized into four tasks:

1. **Provide values:** (a) median price for listings in Manhattan, (b) count of entire homes/apartments in SoHo, and (c) number of hosts in Williamsburg with more than two entire-home listings.
2. **Write a filtering function** that takes a neighbourhood, minimum price, and minimum number of reviews; returns the filtered listings (columns `host_name`, `neighbourhood`, `price`, `number_of_reviews`); prints "No matching results" when empty; prints the top 10 listings by review count; and reports total listings and unique hosts. Then apply it to Hell's Kitchen (price > $150, ≥ 5 reviews).
3. **Build a neighbourhood summary table** (minimum price = 50, minimum reviews = 5) giving the total listings and average price per neighbourhood, and identify the highest- and lowest-priced neighbourhoods.
4. **Summarize by price category** (Low < $100, Medium $100–200, High > $200) with total listings and average reviews per category, then visualize with a bar chart (listing counts) and a secondary-axis line plot (average reviews) on one figure.

---

## Methodology

The analysis is implemented as a single pandas script following the four-task structure.

**Task 1 — Direct queries.** Boolean masking and `.median()` / `.shape` for the Manhattan, SoHo, and Williamsburg questions; the Williamsburg host question uses a `groupby('host_id')` count filtered to hosts with more than two entire-home listings.

**Task 2 — Reusable filter function.** `hotel_review()` filters by neighbourhood, minimum price, and minimum reviews (with optional strict/inclusive bounds), returns the four required columns, handles the empty case, prints the top 10 by review count, and reports total listings and unique hosts. It is then applied to Hell's Kitchen.

**Task 3 — Neighbourhood summary.** The Task 2 function is reused inside a loop over every unique neighbourhood to build a summary DataFrame of total listings and average price, from which the highest- and lowest-average-price neighbourhoods are extracted via `idxmax` / `idxmin`.

**Task 4 — Price-category summary and visualization.** A `category_price()` helper labels each listing Low / Medium / High; a `groupby` aggregates total listings and average reviews per category; and matplotlib renders a dual-axis figure (bar chart for counts, line plot for average reviews).

---

## Technologies Used

- **Language:** Python 3
- **Libraries:**
  - `pandas` — data loading, filtering, grouping, aggregation
  - `numpy` — numerical support
  - `matplotlib` — dual-axis bar + line visualization

---

## Repository Structure

```
nyc-airbnb-data-mining/
├── src/
│   └── airbnb_data_mining.py            # Main analysis script (Tasks 1–4)
├── data/
│   └── Airbnb_ratings_NYC_2019.csv      # NYC Airbnb 2019 dataset
├── outputs/
│   └── Hotel_Summary_by_price_category.png   # Task 4 visualization
├── docs/
│   └── Assignment_Python_AirBnb.pdf     # Assignment brief
├── requirements.txt
├── .gitignore
└── README.md
```

> **Note:** This structure is a recommendation — adjust paths to match your arrangement. The script currently reads `Airbnb_ratings_NYC_2019.csv` from the working directory, so update the path if you move it into `data/` (see Limitations).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tatiana-Tongwa/nyc-airbnb-data-mining.git
   cd nyc-airbnb-data-mining
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Ensure `Airbnb_ratings_NYC_2019.csv` is in the working directory (or update the path in the script), then run:

```bash
python src/airbnb_data_mining.py
```

The script prints the Task 1 values and Task 2/3 results to the console and displays the Task 4 figure. The Hell's Kitchen filter and the neighbourhood loop print their summaries as they run.

---

## Results and Findings

**Task 4 — Listings and reviews by price category.** The dual-axis chart shows that **Low**-priced listings (under $100) are the most numerous, followed by Medium ($100–200), with **High** (> $200) the smallest group. Average review counts are highest for the Low and Medium tiers and noticeably lower for High-priced listings — the more expensive listings tend to accumulate fewer reviews on average.

![Hotel summary by price category](outputs/Hotel_Summary_by_price_category.png)

> The exact numerical answers for Tasks 1–3 (median Manhattan price, SoHo entire-home count, Williamsburg host count, Hell's Kitchen totals, and the highest/lowest-price neighbourhoods) are printed at runtime by the script. They are produced directly from the dataset rather than hard-coded here, so re-running reproduces them.

---

## Limitations

- **Hard-coded file path.** The script reads `Airbnb_ratings_NYC_2019.csv` from the working directory; adjust if you adopt the `data/` layout.
- **Task 3 reuses the verbose Task 2 function inside a loop**, so building the neighbourhood summary prints a large volume of per-neighbourhood output to the console. This is functional but noisy; a quieter aggregation path would be cleaner.
- **Terminology.** The dataset is Airbnb listings; the code and assignment refer to them as "hotels," kept for consistency with the brief.
- **No missing-value handling** is applied to `price` or `number_of_reviews` before aggregation; the dataset is generally clean, but edge cases aren't explicitly guarded.
- The analysis is descriptive — it answers the assignment's specific questions and does not attempt predictive modelling.

---

## Future Improvements

- Parameterize the dataset path (command-line argument or config) instead of hard-coding it.
- Add a `quiet=True` option to the Task 2 function so Task 3 can aggregate without printing each neighbourhood.
- Convert to a Jupyter notebook so the Task 1–3 values and the Task 4 chart are visible inline on GitHub.
- Add light data validation (missing/zero prices, duplicate listings) before aggregation.
- Extend the exploration with borough-level comparisons, room-type breakdowns, or a simple price-vs-reviews correlation.

---

## Contributors

- **Tatiana Nanette Tongwa**

---

## License

 MIT License
