# LAB — Pandas for Business, Economic, and Supply Chain Analysis

**Format:** Worked examples + student coding exercises  
**Main library:** Pandas  
**Supporting library:** NumPy  
**Context:** Sales, pricing, customers, inflation, inventory, procurement, suppliers, logistics, forecasting, and supply-chain performance

## Learning Design

Each section contains:

1. **Worked Example** — sample code demonstrating the main Pandas idea.
2. **Your Turn** — a related exercise that students must code independently.
3. **Business / Economic / Supply Chain Context** — why the task matters in practice.
4. **Tasks** — required outputs and variable names.
5. **Hints** — suggested Pandas methods and operations.
6. **Interpretation** — a short managerial, economic, or supply-chain explanation.

## Rules

- Use **Pandas** as the main library.
- NumPy may be used when it naturally supports Pandas operations.
- Do not use explicit `for` loops unless explicitly requested.
- Do not hard-code final numerical answers.
- Keep the required variable names.
- After filtering, grouping, merging, or reshaping, inspect the result using `shape`, `head()`, or both.
- When handling missing values, compare missing-value counts before and after processing.
- When merging datasets, compare the number of rows before and after the merge.

## Learning Objectives

After completing this lab, students will be able to:

1. Represent business, economic, and supply-chain data using Pandas `Series` and `DataFrame`.
2. Inspect tabular data using `head()`, `shape`, `columns`, `dtypes`, `info()`, and `describe()`.
3. Select observations using `loc`, `iloc`, column selection, and Boolean filtering.
4. Create new business variables using vectorized column operations.
5. Read and write CSV, Excel, and JSON data.
6. Detect and handle missing values and duplicate records.
7. Clean text data and convert data types.
8. Sort, rank, and select top-performing business entities.
9. Group and aggregate data using `groupby()` and `agg()`.
10. Build pivot tables for managerial reporting.
11. Merge customer, order, supplier, procurement, and logistics datasets.
12. Analyze inventory and stockout risk.
13. Evaluate supplier and logistics performance.
14. Work with time-series business data using datetime indexing, `resample()`, and `rolling()`.
15. Calculate correlations and create quick visualizations.
16. Translate Pandas outputs into short managerial, economic, and supply-chain interpretations.

## Pandas Knowledge and Skills Used in This Lab

### DataFrame and Series

Students will practice:

- `pd.Series()`
- `pd.DataFrame()`
- `shape`
- `columns`
- `index`
- `dtypes`
- `head()`
- `tail()`
- `info()`
- `describe()`

### Indexing and Filtering

Students will use:

- `df["column"]`
- `df[["col1", "col2"]]`
- `loc`
- `iloc`
- Boolean masks
- Multiple conditions using `&`, `|`, and `~`

### Data Transformation

Students will practice:

- Creating calculated columns
- Vectorized arithmetic
- `assign()`
- `map()`
- `apply()`
- `astype()`
- `pd.to_numeric()`
- String methods using `.str`

### Data Cleaning

Students will use:

- `isna()`
- `isna().sum()`
- `dropna()`
- `fillna()`
- `duplicated()`
- `drop_duplicates()`

### Sorting and Ranking

Students will practice:

- `sort_values()`
- `nlargest()`
- `nsmallest()`
- `rank()`

### Grouping and Aggregation

Students will use:

- `groupby()`
- `sum()`
- `mean()`
- `count()`
- `min()`
- `max()`
- `agg()`
- `reset_index()`

### Merging and Reshaping

Students will use:

- `pd.merge()`
- `pd.concat()`
- `pivot()`
- `pd.pivot_table()`
- `pd.melt()`

### Time-Series Analysis

Students will practice:

- `pd.to_datetime()`
- `set_index()`
- `sort_index()`
- `resample()`
- `rolling()`

### Business and Supply-Chain Analysis

Students will evaluate:

- Revenue and profit
- Customer value
- Regional sales
- Inflation-adjusted values
- Inventory coverage
- Stockout risk
- Supplier quality and lead time
- Procurement spend
- Delivery performance
- Forecast errors
- Supply-chain KPIs

---

# Part 0 — Setup

```python
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

print("Pandas version:", pd.__version__)
```

---

# Section 1 — Sales and Revenue Analysis

## Worked Example 1.1 — Create and Inspect a Sales DataFrame

```python
example_sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Units": [100, 120, 110, 140],
    "Price": [10.0, 10.0, 11.0, 11.5]
})

example_sales["Revenue"] = (
    example_sales["Units"] *
    example_sales["Price"]
)

print(example_sales)
print("Shape:", example_sales.shape)
print(example_sales.dtypes)
```

## Your Turn 1.1 — Twelve-Month Sales Performance

### Business Context

A retail manager wants to evaluate monthly product performance over one year. The manager needs revenue, average monthly performance, and the strongest sales month.

### Exercise Description

In this exercise, you will create a Pandas DataFrame, calculate revenue, inspect the dataset, and identify the month with the highest revenue.

The task emphasizes **DataFrame creation**, **calculated columns**, **aggregation**, and **row selection**.

Use:

```python
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

units_sold = [
    420, 460, 440, 500, 540, 525,
    575, 610, 590, 650, 690, 720
]

unit_price = [
    12.0, 12.0, 12.5, 12.5, 13.0, 13.0,
    13.5, 13.5, 14.0, 14.0, 14.5, 14.5
]
```

### Tasks

Create:

- `sales_df`
- column `Revenue`
- `annual_revenue`
- `average_monthly_revenue`
- `best_month_row`

Print:

- `sales_df.head()`
- `sales_df.shape`
- `sales_df.dtypes`
- required results

### Hints

- `pd.DataFrame({...})`
- `df["Revenue"] = ...`
- `df["Revenue"].sum()`
- `df["Revenue"].mean()`
- `df.loc[df["Revenue"].idxmax()]`

```python
# STUDENT CODE — 1.1

# sales_df = pd.DataFrame({
#     "Month": ...,
#     "Units": ...,
#     "Price": ...
# })

# sales_df["Revenue"] = ...
# annual_revenue = ...
# average_monthly_revenue = ...
# best_month_row = ...

# Print the required results.
```

### Interpretation

Write 2–3 sentences explaining whether annual performance appears to improve over the year and which month contributes the highest revenue.

---

## Worked Example 1.2 — Filter High-Performance Months

```python
example_sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [1000, 1250, 1100, 1500]
})

high_months = example_sales[
    example_sales["Revenue"] >= 1200
]

print(high_months)
```

## Your Turn 1.2 — Identify High-Revenue Months

### Business Context

Managers often focus on months that exceed a performance threshold so they can investigate promotions, seasonality, or demand conditions.

### Tasks

Using `sales_df`, create:

- `high_revenue_months` where Revenue is above the annual monthly average;
- `high_revenue_high_volume` where:
  - Revenue is above average;
  - Units are at least 600.

### Hints

- Boolean filtering
- `df["Revenue"] > average_monthly_revenue`
- Combine conditions with `&`

```python
# STUDENT CODE — 1.2

# high_revenue_months = ...
# high_revenue_high_volume = ...

# Print shapes and results.
```

### Interpretation

Explain why filtering on both revenue and volume may provide a different managerial signal than filtering on revenue alone.

---

# Section 2 — Customer and Market Analysis

## Worked Example 2.1 — Customer Segmentation with Boolean Conditions

```python
customers = pd.DataFrame({
    "Customer": ["C1", "C2", "C3", "C4"],
    "Orders": [3, 10, 6, 12],
    "AnnualSpend": [500, 2500, 1300, 4200]
})

vip = customers[
    (customers["Orders"] >= 8) &
    (customers["AnnualSpend"] >= 2000)
]

print(vip)
```

## Your Turn 2.1 — Identify High-Value Customers

### Business Context

A company wants to identify high-value customers for loyalty programs and personalized offers.

Use:

```python
customer_df = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08"],
    "Orders": [2, 8, 5, 12, 3, 9, 6, 15],
    "AnnualSpend": [450, 2200, 1400, 3900, 700, 2600, 1800, 5200],
    "Returns": [0, 1, 0, 2, 1, 0, 3, 1]
})
```

### Tasks

Create:

- `high_value_customers`
- `high_value_low_return`
- `top_3_customers`

Conditions for `high_value_customers`:

- Orders >= 8
- AnnualSpend >= 2000

Conditions for `high_value_low_return`:

- high-value conditions;
- Returns <= 1.

### Hints

- Boolean filtering
- `.nlargest(3, "AnnualSpend")`

```python
# STUDENT CODE — 2.1

# high_value_customers = ...
# high_value_low_return = ...
# top_3_customers = ...

# Print results.
```

### Interpretation

Explain why a company may prefer a customer with slightly lower spending but fewer returns.

---

## Worked Example 2.2 — Customer Ranking

```python
customers["SpendRank"] = (
    customers["AnnualSpend"]
    .rank(ascending=False)
)

print(customers)
```

## Your Turn 2.2 — Rank Customer Value

### Tasks

Add:

- `SpendRank`
- `OrderRank`

Sort the DataFrame by:

1. AnnualSpend descending;
2. Orders descending.

Create:

- `customer_ranking`

### Hints

- `.rank(ascending=False)`
- `.sort_values([...], ascending=[False, False])`

```python
# STUDENT CODE — 2.2

# customer_df["SpendRank"] = ...
# customer_df["OrderRank"] = ...
# customer_ranking = ...

# Print results.
```

---

# Section 3 — Economic Analysis: Prices and Inflation

## Worked Example 3.1 — Inflation-Adjusted Sales

```python
economic_df = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "NominalSales": [100, 110, 121],
    "CPI": [100, 105, 110]
})

economic_df["RealSales"] = (
    economic_df["NominalSales"] *
    100 /
    economic_df["CPI"]
)

print(economic_df)
```

## Your Turn 3.1 — Nominal vs. Real Business Growth

### Economic Context

Nominal business growth may be partly driven by inflation. Analysts therefore adjust financial values using a price index to measure real growth.

Use:

```python
economic_df = pd.DataFrame({
    "Year": [2022, 2023, 2024, 2025, 2026],
    "NominalSales": [100, 108, 117, 126, 140],
    "CPI": [100, 103, 107, 112, 118]
})
```

### Tasks

Create columns:

- `RealSales`
- `NominalGrowthPct`
- `RealGrowthPct`
- `GrowthGap`

Use `pct_change()` for growth rates.

Create:

- `largest_gap_year`

### Hints

- `df["NominalSales"] * 100 / df["CPI"]`
- `.pct_change() * 100`
- `.abs()`
- `.idxmax()`
- `.loc[...]`

```python
# STUDENT CODE — 3.1

# economic_df["RealSales"] = ...
# economic_df["NominalGrowthPct"] = ...
# economic_df["RealGrowthPct"] = ...
# economic_df["GrowthGap"] = ...
# largest_gap_year = ...

# Print results.
```

### Interpretation

Explain the difference between nominal growth and real growth and why the distinction matters for business planning.

---

# Section 4 — Data Cleaning for Business Data

## Worked Example 4.1 — Missing Values

```python
example_df = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Price": [10.0, np.nan, 15.0]
})

print(example_df.isna().sum())

example_df["Price"] = (
    example_df["Price"]
    .fillna(example_df["Price"].median())
)

print(example_df)
```

## Your Turn 4.1 — Clean a Messy Sales Dataset

### Business Context

Operational data often contain missing prices, inconsistent text labels, incorrect numeric formats, and duplicate rows.

Use:

```python
messy_sales = pd.DataFrame({
    "OrderID": ["O01", "O02", "O02", "O03", "O04", "O05"],
    "Product": [" Basic ", "PREMIUM", "PREMIUM", "standard", "Basic", " enterprise "],
    "Quantity": ["2", "3", "3", "4", "unknown", "5"],
    "Price": [10.0, 25.0, 25.0, np.nan, 10.0, 40.0]
})
```

### Tasks

Create:

- `missing_before`
- cleaned `Product`
- numeric `Quantity`
- filled `Price`
- `clean_sales`
- `missing_after`

Required cleaning:

1. remove exact duplicates;
2. strip spaces from Product;
3. convert Product to title case;
4. convert Quantity using `pd.to_numeric(errors="coerce")`;
5. fill missing Quantity using median;
6. fill missing Price using median.

### Hints

- `.drop_duplicates()`
- `.str.strip()`
- `.str.title()`
- `pd.to_numeric(..., errors="coerce")`
- `.fillna(...)`

```python
# STUDENT CODE — 4.1

# missing_before = ...

# clean_sales = messy_sales.copy()
# clean_sales = ...

# clean_sales["Product"] = ...
# clean_sales["Quantity"] = ...
# clean_sales["Quantity"] = ...
# clean_sales["Price"] = ...

# missing_after = ...

# Print before/after shapes and missing counts.
```

### Interpretation

Explain how unclean data could distort revenue, demand, or inventory analysis.

---

# Section 5 — Grouping and Regional Business Performance

## Worked Example 5.1 — Grouped Sales

```python
example = pd.DataFrame({
    "Region": ["North", "South", "North", "South"],
    "Sales": [100, 120, 150, 130]
})

region_summary = (
    example
    .groupby("Region")["Sales"]
    .agg(["count", "sum", "mean"])
)

print(region_summary)
```

## Your Turn 5.1 — Regional Sales Performance

### Business Context

A national company wants to compare sales performance across regions and products.

Use:

```python
regional_sales = pd.DataFrame({
    "Region": [
        "North", "North", "South", "South",
        "Central", "Central", "North", "South"
    ],
    "Product": [
        "A", "B", "A", "B",
        "A", "B", "A", "B"
    ],
    "Revenue": [120, 180, 150, 210, 110, 160, 140, 190],
    "Units": [12, 15, 14, 18, 10, 13, 11, 16]
})
```

### Tasks

Create:

- `region_summary`
- `product_summary`
- `region_product_summary`

For `region_summary`, calculate:

- count;
- sum Revenue;
- mean Revenue;
- sum Units.

### Hints

- `.groupby("Region")`
- `.agg(...)`
- `.groupby(["Region", "Product"])`
- `.reset_index()`

```python
# STUDENT CODE — 5.1

# region_summary = ...
# product_summary = ...
# region_product_summary = ...

# Print all results.
```

### Interpretation

Identify which region appears strongest and explain whether revenue alone is sufficient to assess performance.

---

## Worked Example 5.2 — Pivot Table

```python
pivot = pd.pivot_table(
    regional_sales,
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print(pivot)
```

## Your Turn 5.2 — Management Reporting Table

### Tasks

Create:

- `revenue_pivot`
- `units_pivot`

Add:

- a `Total` column to `revenue_pivot`.

### Hints

- `pd.pivot_table()`
- `.sum(axis=1)`

```python
# STUDENT CODE — 5.2

# revenue_pivot = ...
# units_pivot = ...
# revenue_pivot["Total"] = ...

# Print results.
```

---

# Section 6 — Inventory and Stockout Analysis

## Worked Example 6.1 — Inventory Coverage

```python
inventory = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Inventory": [100, 80, 150],
    "DailyDemand": [10, 20, 15]
})

inventory["DaysCover"] = (
    inventory["Inventory"] /
    inventory["DailyDemand"]
)

print(inventory)
```

## Your Turn 6.1 — Inventory Coverage and Stockout Risk

### Supply Chain Context

Inventory managers need to know how long current stock can cover expected demand. Low days-of-cover indicates higher stockout risk.

Use:

```python
inventory_df = pd.DataFrame({
    "SKU": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "Inventory": [500, 180, 420, 90, 650, 220],
    "DailyDemand": [40, 30, 35, 25, 50, 28],
    "LeadTimeDays": [8, 6, 10, 5, 12, 7]
})
```

### Tasks

Create columns:

- `DaysCover`
- `LeadTimeDemand`
- `ReorderRisk`

Define `ReorderRisk` as:

```text
Inventory < LeadTimeDemand
```

Create:

- `at_risk_skus`
- `lowest_cover_skus`

where `lowest_cover_skus` contains the three SKUs with the lowest `DaysCover`.

### Hints

- vectorized division
- `Inventory < LeadTimeDemand`
- `.nsmallest(3, "DaysCover")`

```python
# STUDENT CODE — 6.1

# inventory_df["DaysCover"] = ...
# inventory_df["LeadTimeDemand"] = ...
# inventory_df["ReorderRisk"] = ...

# at_risk_skus = ...
# lowest_cover_skus = ...

# Print results.
```

### Interpretation

Explain why comparing inventory only with current demand can be misleading when replenishment lead time is long.

---

# Section 7 — Supplier Performance

## Worked Example 7.1 — Supplier Score

```python
suppliers = pd.DataFrame({
    "Supplier": ["S1", "S2", "S3"],
    "Quality": [95, 90, 98],
    "LeadTime": [8, 6, 10]
})

suppliers["LeadTimeScore"] = (
    1 -
    (suppliers["LeadTime"] - suppliers["LeadTime"].min()) /
    (suppliers["LeadTime"].max() - suppliers["LeadTime"].min())
)

print(suppliers)
```

## Your Turn 7.1 — Supplier Evaluation

### Supply Chain Context

Procurement decisions often depend on several competing indicators such as cost, quality, lead time, and delivery reliability.

Use:

```python
supplier_df = pd.DataFrame({
    "Supplier": ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"],
    "UnitCost": [12.5, 11.8, 13.0, 12.2, 11.5],
    "QualityScore": [92, 88, 97, 94, 85],
    "LeadTimeDays": [8, 6, 10, 7, 5],
    "OnTimeRate": [0.94, 0.90, 0.98, 0.95, 0.87]
})
```

### Tasks

Create normalized columns:

- `CostScore` — lower cost is better;
- `QualityNorm` — higher is better;
- `LeadTimeScore` — lower lead time is better;
- `OnTimeNorm` — higher is better.

Use weights:

```python
weights = {
    "CostScore": 0.30,
    "QualityNorm": 0.25,
    "LeadTimeScore": 0.20,
    "OnTimeNorm": 0.25
}
```

Create:

- `SupplierScore`
- `supplier_ranking`

### Hints

For a benefit KPI:

```python
(x - x.min()) / (x.max() - x.min())
```

For a cost KPI:

```python
1 - normalized_value
```

Sort:

```python
.sort_values("SupplierScore", ascending=False)
```

```python
# STUDENT CODE — 7.1

# supplier_df["CostScore"] = ...
# supplier_df["QualityNorm"] = ...
# supplier_df["LeadTimeScore"] = ...
# supplier_df["OnTimeNorm"] = ...

# supplier_df["SupplierScore"] = ...
# supplier_ranking = ...

# Print ranking.
```

### Interpretation

Explain why the supplier with the lowest unit cost may not receive the highest overall score.

---

# Section 8 — Procurement Spend Analysis

## Worked Example 8.1 — Merge Purchase Orders with Suppliers

```python
supplier_master = pd.DataFrame({
    "SupplierID": ["S1", "S2"],
    "SupplierName": ["Alpha", "Beta"]
})

purchase_orders = pd.DataFrame({
    "PO": ["P1", "P2", "P3"],
    "SupplierID": ["S1", "S2", "S1"],
    "Amount": [1000, 1500, 1200]
})

merged = pd.merge(
    purchase_orders,
    supplier_master,
    on="SupplierID",
    how="left"
)

print(merged)
```

## Your Turn 8.1 — Procurement Spend by Supplier

### Supply Chain Context

Procurement managers often store supplier master data and purchase-order transactions in separate tables. These must be merged before spend analysis.

Use:

```python
supplier_master = pd.DataFrame({
    "SupplierID": ["S01", "S02", "S03", "S04"],
    "SupplierName": ["Alpha", "Beta", "Gamma", "Delta"],
    "Country": ["VN", "TH", "CN", "VN"]
})

purchase_orders = pd.DataFrame({
    "PO": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"],
    "SupplierID": ["S01", "S02", "S01", "S03", "S02", "S05", "S04"],
    "Amount": [12000, 15000, 9000, 22000, 8000, 7000, 14000]
})
```

### Tasks

Create:

- `po_supplier`
- `unmatched_orders`
- `supplier_spend`
- `country_spend`

Use a left merge from purchase orders.

### Hints

- `pd.merge(..., how="left")`
- unmatched supplier:
  - `SupplierName.isna()`
- `.groupby(...)["Amount"].sum()`

```python
# STUDENT CODE — 8.1

# po_supplier = ...
# unmatched_orders = ...
# supplier_spend = ...
# country_spend = ...

# Print shapes and results.
```

### Interpretation

Explain why unmatched supplier IDs are a data-quality issue in procurement reporting.

---

# Section 9 — Logistics and Delivery Performance

## Worked Example 9.1 — Delivery Delay

```python
delivery = pd.DataFrame({
    "Order": ["O1", "O2", "O3"],
    "PromisedDays": [3, 4, 2],
    "ActualDays": [3, 6, 2]
})

delivery["DelayDays"] = (
    delivery["ActualDays"] -
    delivery["PromisedDays"]
)

delivery["OnTime"] = (
    delivery["DelayDays"] <= 0
)

print(delivery)
```

## Your Turn 9.1 — Logistics Service-Level Analysis

### Supply Chain Context

Delivery reliability directly affects customer satisfaction and supply-chain performance. Managers need both overall service levels and carrier-level comparisons.

Use:

```python
delivery_df = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06", "O07", "O08"],
    "Carrier": ["A", "A", "B", "B", "C", "C", "A", "B"],
    "PromisedDays": [3, 4, 3, 5, 2, 4, 3, 4],
    "ActualDays": [3, 6, 4, 5, 2, 7, 2, 5],
    "ShippingCost": [20, 30, 25, 35, 18, 32, 22, 28]
})
```

### Tasks

Create columns:

- `DelayDays`
- `OnTime`

Create:

- `overall_on_time_rate`
- `carrier_summary`

For each carrier, calculate:

- number of deliveries;
- mean DelayDays;
- on-time rate;
- mean ShippingCost.

### Hints

- Boolean columns can be averaged because `True = 1`, `False = 0`.
- `.groupby("Carrier").agg(...)`
- Named aggregation syntax may be useful.

```python
# STUDENT CODE — 9.1

# delivery_df["DelayDays"] = ...
# delivery_df["OnTime"] = ...

# overall_on_time_rate = ...

# carrier_summary = ...

# Print results.
```

### Interpretation

Discuss the trade-off between delivery performance and shipping cost.

---

# Section 10 — Time-Series Sales and Forecasting

## Worked Example 10.1 — Monthly Resampling

```python
dates = pd.date_range(
    "2026-01-01",
    periods=10,
    freq="D"
)

daily = pd.DataFrame({
    "Date": dates,
    "Sales": np.arange(100, 110)
})

daily = daily.set_index("Date")

weekly = daily["Sales"].resample("W").sum()

print(weekly)
```

## Your Turn 10.1 — Daily to Weekly Sales

### Business Context

Daily sales can be noisy. Weekly aggregation gives managers a higher-level view for planning and reporting.

Use:

```python
dates = pd.date_range(
    start="2026-01-01",
    periods=60,
    freq="D"
)

daily_sales = pd.DataFrame({
    "Date": dates,
    "Sales": 100 + np.arange(60) * 1.5
})
```

### Tasks

1. set `Date` as the index;
2. create `weekly_sales`;
3. create `monthly_sales`;
4. create a 7-day moving average column `MA7`.

### Hints

- `.set_index("Date")`
- `.resample("W").sum()`
- `.resample("ME").sum()`
- `.rolling(window=7).mean()`

```python
# STUDENT CODE — 10.1

# daily_sales = ...
# weekly_sales = ...
# monthly_sales = ...
# daily_sales["MA7"] = ...

# Print results.
```

---

## Worked Example 10.2 — Forecast Error in a DataFrame

```python
forecast_df = pd.DataFrame({
    "Actual": [100, 120, 110],
    "Forecast": [98, 125, 108]
})

forecast_df["Error"] = (
    forecast_df["Actual"] -
    forecast_df["Forecast"]
)

forecast_df["AbsoluteError"] = (
    forecast_df["Error"].abs()
)

print(forecast_df)
```

## Your Turn 10.2 — Compare Forecast Accuracy

### Business / Supply Chain Context

Forecast accuracy affects inventory, production, procurement, and logistics planning.

Use:

```python
forecast_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
    "Actual": [120, 135, 128, 150, 160, 172, 168, 180],
    "ForecastA": [118, 132, 134, 147, 158, 169, 171, 176],
    "ForecastB": [125, 138, 127, 155, 166, 175, 165, 185]
})
```

### Tasks

Create columns for both methods:

- `ErrorA`
- `ErrorB`
- `AbsErrorA`
- `AbsErrorB`
- `APE_A`
- `APE_B`

Create:

- `mae_a`
- `mae_b`
- `mape_a`
- `mape_b`

### Hints

- `.abs()`
- `.mean()`
- percentage error:
  ```python
  abs(error / actual) * 100
  ```

```python
# STUDENT CODE — 10.2

# forecast_df["ErrorA"] = ...
# forecast_df["ErrorB"] = ...
# forecast_df["AbsErrorA"] = ...
# forecast_df["AbsErrorB"] = ...
# forecast_df["APE_A"] = ...
# forecast_df["APE_B"] = ...

# mae_a = ...
# mae_b = ...
# mape_a = ...
# mape_b = ...

# Print all required results.
```

### Interpretation

State which forecasting method is better under MAE and MAPE and explain why forecast accuracy matters for inventory planning.

---

# Section 11 — Supply Chain KPI Dashboard

## Worked Example 11.1 — KPI Summary

```python
kpi_df = pd.DataFrame({
    "Warehouse": ["W1", "W2", "W3"],
    "FillRate": [0.95, 0.90, 0.97],
    "InventoryTurns": [8, 6, 9]
})

print(
    kpi_df.describe()
)
```

## Your Turn 11.1 — Warehouse Performance

### Supply Chain Context

A supply-chain manager evaluates warehouses using multiple KPIs that capture service, inventory efficiency, and cost.

Use:

```python
warehouse_df = pd.DataFrame({
    "Warehouse": ["North DC", "South DC", "Central DC", "East DC"],
    "FillRate": [0.96, 0.91, 0.94, 0.89],
    "InventoryTurns": [8.5, 6.2, 7.8, 5.9],
    "OrderCycleDays": [2.8, 3.6, 3.0, 4.1],
    "CostPerOrder": [4.8, 4.2, 5.1, 3.9]
})
```

### Tasks

1. inspect with `describe()`;
2. create normalized KPI columns;
3. reverse cost-type KPIs:
   - OrderCycleDays;
   - CostPerOrder;
4. use weights:
   - FillRate: 0.35
   - InventoryTurns: 0.25
   - OrderCycleDays: 0.20
   - CostPerOrder: 0.20
5. create `PerformanceScore`;
6. create `warehouse_ranking`.

### Hints

Benefit KPI:

```python
(x - x.min()) / (x.max() - x.min())
```

Cost KPI:

```python
1 - normalized_value
```

### Student Code

```python
# STUDENT CODE — 11.1

# warehouse_df["FillRateNorm"] = ...
# warehouse_df["TurnsNorm"] = ...
# warehouse_df["CycleScore"] = ...
# warehouse_df["CostScore"] = ...

# warehouse_df["PerformanceScore"] = ...

# warehouse_ranking = ...

# Print ranking.
```

### Interpretation

Explain why a warehouse with the lowest cost may still rank poorly overall.

---

# Section 12 — Integrated Supply Chain Analysis

## Your Turn 12.1 — End-to-End Order Analysis

### Supply Chain Context

A manager wants to connect customer orders, product information, and delivery performance to understand revenue, margin, and service quality in one integrated dataset.

Use:

```python
orders = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06"],
    "CustomerID": ["C01", "C02", "C01", "C03", "C04", "C02"],
    "ProductID": ["P1", "P2", "P2", "P3", "P1", "P3"],
    "Quantity": [2, 1, 3, 2, 4, 1]
})

products = pd.DataFrame({
    "ProductID": ["P1", "P2", "P3"],
    "Price": [20.0, 35.0, 50.0],
    "UnitCost": [12.0, 21.0, 32.0]
})

delivery = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06"],
    "Carrier": ["A", "B", "A", "C", "B", "C"],
    "PromisedDays": [3, 4, 3, 5, 4, 3],
    "ActualDays": [3, 5, 2, 7, 4, 4]
})
```

### Tasks

Create an integrated DataFrame `order_analysis` by:

1. merging orders with products;
2. merging the result with delivery;
3. creating:
   - `Revenue`;
   - `TotalCost`;
   - `Contribution`;
   - `DelayDays`;
   - `OnTime`.
4. calculate:
   - total Revenue;
   - total Contribution;
   - overall on-time rate.
5. create:
   - `product_summary`;
   - `carrier_summary`;
   - `customer_summary`.
6. identify:
   - highest-revenue product;
   - customer with highest contribution;
   - carrier with best on-time rate.

### Hints

- `pd.merge()`
- Revenue:
  ```python
  Quantity * Price
  ```
- Contribution:
  ```python
  Revenue - TotalCost
  ```
- `groupby()` + `agg()`
- `idxmax()`

```python
# STUDENT CODE — 12.1

# order_analysis = pd.merge(...)
# order_analysis = pd.merge(...)

# order_analysis["Revenue"] = ...
# order_analysis["TotalCost"] = ...
# order_analysis["Contribution"] = ...
# order_analysis["DelayDays"] = ...
# order_analysis["OnTime"] = ...

# total_revenue = ...
# total_contribution = ...
# overall_on_time_rate = ...

# product_summary = ...
# carrier_summary = ...
# customer_summary = ...

# Print all required results.
```

### Interpretation

Write 4–6 sentences explaining the most important business and supply-chain findings from the integrated analysis.

---

# Final Reflection

1. Which section best demonstrated DataFrame creation and inspection?
2. Which section best demonstrated Boolean filtering?
3. Which section best demonstrated `groupby()` and aggregation?
4. Which section best demonstrated merging multiple datasets?
5. Which section was most relevant to Business or Economics?
6. Which section was most relevant to Supply Chain Management?
7. Which Pandas operation do you expect to use most frequently in real-world data analysis?
8. What is one danger of making managerial decisions from a DataFrame without first checking data quality?
