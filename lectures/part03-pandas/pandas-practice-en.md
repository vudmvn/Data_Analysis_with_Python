# PANDAS PRACTICE EXERCISES

**Topic:** DataFrame, Series, data input/output, cleaning, transformation, and analysis  
**Language:** Python  
**Main library:** Pandas

## Learning Objectives

After completing this notebook, learners will be able to:

- Create and inspect `Series` and `DataFrame` objects.
- Interpret `shape`, `columns`, `index`, `dtypes`, `info()`, and `describe()`.
- Access data using `loc`, `iloc`, indexing, and slicing.
- Filter data using one or multiple conditions.
- Sort data and create new columns.
- Read and write CSV, Excel, and JSON data.
- Detect and handle missing data.
- Detect and remove duplicate records.
- Convert data types and clean string data.
- Group and aggregate data using `groupby()` and `agg()`.
- Combine datasets using `merge()` and `concat()`.
- Reshape data using `pivot()`, `melt()`, and `pivot_table()`.
- Calculate correlation and descriptive statistics.
- Work with time-series data using `to_datetime()`, `resample()`, and `rolling()`.
- Create quick visualizations using Pandas.
- Complete an integrated data-analysis task using Pandas.

## Submission Guidelines

For each exercise, present your work in the following order:

1. **Code**
2. **Output**
3. **A short explanation of 1-3 sentences**

In addition:

- Do not modify the input data directly unless requested.
- When filtering or reshaping data, print the result `shape`.
- When handling missing data, check the number of missing values before and after processing.
- When merging two tables, check the number of rows before and after the merge.
- You may run the **Automated Check** cells after completing each exercise.
- For I/O exercises, files are saved in the current working directory.

---

# PART 0 - ENVIRONMENT SETUP

```python
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

print("Pandas version:", pd.__version__)
```

---

# PART 1 - GETTING STARTED WITH SERIES AND DATAFRAME

## Exercise 1. Create a Basic Series

Given:

```python
values = [10, 20, 30, 40]
```

### Requirements

1. Create a `Series` named `s` from `values`.
2. In `s`.
3. In `s.index`, `s.values`, `s.dtype`.
4. Create another `Series` with index `["A", "B", "C", "D"]`.
5. Access the element with label `"C"` using `loc`.
6. Access the element at position 2 using `iloc`.
7. Explain the difference between `loc` and `iloc`.

### Hint

Hint: use `pd.Series(...)`, then inspect `.index`, `.values`, `.dtype`; use `.loc[...]` cho label and `.iloc[...]` cho position.

### Incomplete Starter Code

```python
# Starter-code hint
s = pd.Series(values)
print(s)
print(s.index)
print(s.values)
print(s.dtype)

s_label = pd.Series(values, index=[..., ..., ..., ...])

# Complete the following:
# print(s_label.loc[...])
# print(s_label.iloc[...])
```

```python
# Write your solution here

values = [10, 20, 30, 40]

# s = ...
# TODO
```

**Student explanation:**

-

### Automated Check

```python
try:
    assert isinstance(s, pd.Series)
    assert len(s) == 4
    assert s.iloc[2] == 30
    print("Basic requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

## Exercise 2. Create a DataFrame from a Dictionary

Given:

```python
data = {
    "StudentID": ["S01", "S02", "S03", "S04"],
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Age": [20, 21, 19, 22],
    "GPA": [3.2, 3.7, 3.5, 3.8]
}
```

### Requirements

1. Create a `DataFrame` named `df`.
2. Print the entire `df`.
3. Print:
   - `df.shape`
   - `df.columns`
   - `df.index`
   - `df.dtypes`
4. Print the first two rows using `head()`.
5. Print the last two rows using `tail()`.
6. Explain meaning of `shape`.

### Hint

Hint: use `pd.DataFrame(data)`. The attributes `shape`, `columns`, `index`, and `dtypes` do not require parentheses; `head()` and `tail()` are methods.

### Incomplete Starter Code

```python
# Starter-code hint
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)

# Complete the following:
# print(df.head(...))
# print(df.tail(...))
```

```python
# Write your solution here

data = {
    "StudentID": ["S01", "S02", "S03", "S04"],
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Age": [20, 21, 19, 22],
    "GPA": [3.2, 3.7, 3.5, 3.8]
}

# TODO
```

**Student explanation:**

-

### Automated Check

```python
try:
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (4, 4)
    assert list(df.columns) == ["StudentID", "Name", "Age", "GPA"]
    print("Requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

## Exercise 3. `info()` and `describe()`

Use the `df` DataFrame from Exercise 2.

### Requirements

1. Run `df.info()`.
2. Run `df.describe()`.
3. Explain:
   - What information does `info()` provide?
   - What type of variables does `describe()` mainly summarize?
4. Calculate separately:
   - mean age;
   - GPA mean;
   - GPA maximum.

### Hint

Hint: `info()` prints structural information directly; `describe()` returns a DataFrame of summary statistics. You can use `.mean()` and `.max()` on individual columns.

### Incomplete Starter Code

```python
# Starter-code hint
df.info()

summary = df.describe()
print(summary)

# Complete the following:
# mean_age = df["Age"].____()
# mean_gpa = df["GPA"].____()
# max_gpa = df["GPA"].____()
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

# PART 2 - ACCESSING, INDEXING, FILTERING, AND SORTING

## Exercise 4. Access Columns

Use `df` from the previous part.

### Requirements

1. Select the `Name` column.
2. Select both `Name` and `GPA`.
3. Print the object types of the results from Questions 1 and 2.
4. Explain why selecting one column usually returns a `Series`, while selecting multiple columns returns a `DataFrame`.

### Hint

Hint: `df['Name']` returns Series; `df[['Name', 'GPA']]` returns DataFrame.

### Incomplete Starter Code

```python
# Starter-code hint
name_col = df["Name"]
name_gpa = df[[..., ...]]

print(type(name_col))
print(type(name_gpa))
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 5. `loc` and `iloc`

### Requirements

1. Set `StudentID` as the index using `set_index()`, and store the result as `students`.
2. Use `loc` to select student `"S02"`.
3. Use `iloc` to select the first row.
4. Use `loc` to select rows `"S01"` through `"S03"` and columns `Name` and `GPA`.
5. Use `iloc` to select the first two rows and the last two columns.
6. Print the `shape` of each result.
7. Explain the difference between label-based and position-based selection.

### Hint

Hint: use `set_index('StudentID')`, then compare `students.loc['S02']` with `students.iloc[0]`.

### Incomplete Starter Code

```python
# Starter-code hint
students = df.set_index("StudentID")

row_s02 = students.loc[...]
first_row = students.iloc[...]

subset_loc = students.loc[[..., ...], [..., ...]]
subset_iloc = students.iloc[...:..., [..., ...]]
```

```python
# Write your solution here

# students = ...
# TODO
```

**Student explanation:**

-

### Automated Check

```python
try:
    assert students.index.name == "StudentID"
    assert students.loc["S02", "Name"] == "Binh"
    assert students.iloc[0]["Name"] == "An"
    print("Requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

## Exercise 6. Filter Data with One Condition

Given:

```python
students = pd.DataFrame({
    "StudentID": ["S01", "S02", "S03", "S04", "S05", "S06"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa", "Khanh"],
    "Age": [20, 21, 19, 22, 20, 23],
    "GPA": [3.2, 3.7, 3.5, 3.8, 2.9, 3.6]
})
```

### Requirements

1. Filter students with `GPA >= 3.5`.
2. Filter students with `Age > 20`.
3. Print the `shape` of each result.
4. Keep only the `Name` and `GPA` columns in the result from Question 1.

### Hint

Hint: create a Boolean mask such as `students['GPA'] >= 3.5`, then place the mask inside `students[...]`.

### Incomplete Starter Code

```python
# Starter-code hint
high_gpa = students[students["GPA"] >= ...]
older = students[students["Age"] > ...]

result = high_gpa[[..., ...]]
```

```python
# Write your solution here

students = pd.DataFrame({
    "StudentID": ["S01", "S02", "S03", "S04", "S05", "S06"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa", "Khanh"],
    "Age": [20, 21, 19, 22, 20, 23],
    "GPA": [3.2, 3.7, 3.5, 3.8, 2.9, 3.6]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 7. Filter with Multiple Conditions

Use the `students` DataFrame.

### Requirements

1. Filter students who have:
   - `Age >= 20`
   - and `GPA >= 3.5`
2. Filter students who have:
   - `GPA < 3.0`
   - or `Age >= 22`
3. Use `~` to select students who do **not** have `GPA >= 3.5`.
4. Explain the role of:
   - `&`
   - `|`
   - `~`
5. Explain why each condition should be placed in parentheses.

### Hint

Hint: each condition should be placed in parentheses; use `&`, `|`, `~` instead of `and`, `or`, `not`.

### Incomplete Starter Code

```python
# Starter-code hint
cond1 = (students["Age"] >= ...) & (students["GPA"] >= ...)
result1 = students[cond1]

cond2 = (students["GPA"] < ...) | (students["Age"] >= ...)
result2 = students[cond2]

result3 = students[~(students["GPA"] >= ...)]
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 8. Sort Data

Use `students`.

### Requirements

1. Sort by GPA ascending.
2. Sort by GPA descending.
3. Sort by:
   - Age ascending;
   - GPA descending.
4. Print all three results.
5. Explain `ascending=[True, False]`.

### Hint

Hint: `sort_values()` accepts either one column name or a list of column names. With multiple columns, `ascending` can also be a list of Boolean values.

### Incomplete Starter Code

```python
# Starter-code hint
asc_gpa = students.sort_values("GPA", ascending=...)
desc_gpa = students.sort_values("GPA", ascending=...)

multi = students.sort_values(
    [..., ...],
    ascending=[..., ...]
)
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

# PART 3 - DATA INPUT / OUTPUT

## Exercise 9. Write and Read CSV

Given:

```python
sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})
```

### Requirements

1. Write `sales` to `sales.csv` with `index=False`.
2. Read file ando `sales_csv`.
3. In `sales_csv`.
4. Compare `shape` of `sales` and `sales_csv`.
5. Explain why `index=False` is commonly used.

### Hint

Hint: use `to_csv(..., index=False)`, then `pd.read_csv(...)`.

### Incomplete Starter Code

```python
# Starter-code hint
sales.to_csv("sales.csv", index=...)

sales_csv = pd.read_csv(...)
print(sales_csv)
```

```python
# Write your solution here

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})

# TODO
```

**Student explanation:**

-

### Automated Check

```python
try:
    assert sales_csv.shape == sales.shape
    assert list(sales_csv.columns) == list(sales.columns)
    print("Requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

## Exercise 10. Write and Read Excel

Use the `sales` DataFrame.

### Requirements

1. Write `sales` ra `sales.xlsx`.
2. Read the file back into `sales_excel`.
3. Print the data.
4. Compare it with the original DataFrame.
5. Inspect `dtypes`.

### Hint

Hint: use `to_excel()` and `pd.read_excel()`. Some environments may require the `openpyxl` package.

### Incomplete Starter Code

```python
# Starter-code hint
sales.to_excel("sales.xlsx", index=...)
sales_excel = pd.read_excel(...)

print(sales_excel)
print(sales_excel.dtypes)
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 11. JSON

Use the `sales` DataFrame.

### Requirements

1. Write the data to `sales.json` with `orient="records"`.
2. Read the JSON file back with Pandas.
3. Print the data.
4. Explain what data structure is produced by `orient="records"`.

### Hint

Hint: use `to_json(..., orient='records')` and `pd.read_json(...)`.

### Incomplete Starter Code

```python
# Starter-code hint
sales.to_json(
    "sales.json",
    orient=...
)

sales_json = pd.read_json(...)
print(sales_json)
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

# PART 4 - DATA CLEANING

## Exercise 12. Detect Missing Data

Given:

```python
df = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "Age": [20, np.nan, 22, 21, np.nan],
    "GPA": [3.2, 3.6, np.nan, 3.8, 3.1],
    "City": ["Hanoi", "Hanoi", None, "Danang", "Hanoi"]
})
```

### Requirements

1. In `df`.
2. Use `isna()` to identify missing-value positions.
3. Count missing values by column.
4. Calculate the total number of missing values in the entire DataFrame.
5. Explain the practical difference between `None` and `np.nan` in a DataFrame.

### Hint

Hint: `df.isna()` creates a Boolean mask; `df.isna().sum()` counts missing values by column; call `.sum()` one more time to get the total for the whole DataFrame.

### Incomplete Starter Code

```python
# Starter-code hint
missing_mask = df.isna()
missing_by_col = df.isna().sum()
total_missing = df.isna().sum().sum()

print(missing_mask)
print(missing_by_col)
print(total_missing)
```

```python
# Write your solution here

df = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "Age": [20, np.nan, 22, 21, np.nan],
    "GPA": [3.2, 3.6, np.nan, 3.8, 3.1],
    "City": ["Hanoi", "Hanoi", None, "Danang", "Hanoi"]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 13. `dropna()` and `fillna()`

Use the `df` DataFrame from Exercise 12.

### Requirements

1. Create `drop_rows` by removing rows with missing values.
2. Create `drop_cols` by removing columns with missing values.
3. Create `filled`:
   - `Age`: thay equal to mean;
   - `GPA`: thay equal to median;
   - `City`: thay equal to `"Unknown"`.
4. Print the number of missing values after processing.
5. Do not modify the original `df`.
6. Explain when to use `dropna()` and when to use `fillna()`.

### Hint

Hint: create a copy first with `df.copy()`. Fill each column separately so that an appropriate mean or median can be used.

### Incomplete Starter Code

```python
# Starter-code hint
drop_rows = df.dropna()
drop_cols = df.dropna(axis=...)

filled = df.copy()

filled["Age"] = filled["Age"].fillna(
    filled["Age"].____()
)

filled["GPA"] = filled["GPA"].fillna(
    filled["GPA"].____()
)

filled["City"] = filled["City"].fillna(...)

print(filled.isna().sum())
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

### Automated Check

```python
try:
    assert filled.isna().sum().sum() == 0
    assert df.isna().sum().sum() > 0
    print("Requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

## Exercise 14. Duplicate Data

Given:

```python
df = pd.DataFrame({
    "ID": [1, 2, 2, 3, 4, 4],
    "Name": ["An", "Binh", "Binh", "Chi", "Dung", "Dung"],
    "Score": [7, 8, 8, 9, 6, 6]
})
```

### Requirements

1. Use `duplicated()` to identify duplicate rows.
2. Count duplicate rows.
3. Create `clean_df` equal to `drop_duplicates()`.
4. Print `shape` before and after.
5. Explain which record `drop_duplicates()` keeps by default.

### Hint

Hint: `duplicated()` marks duplicates starting from the second occurrence by default; `drop_duplicates()` keeps the first record by default.

### Incomplete Starter Code

```python
# Starter-code hint
dup_mask = df.duplicated()
dup_count = dup_mask.sum()

clean_df = df.drop_duplicates()

print(df.shape)
print(clean_df.shape)
```

```python
# Write your solution here

df = pd.DataFrame({
    "ID": [1, 2, 2, 3, 4, 4],
    "Name": ["An", "Binh", "Binh", "Chi", "Dung", "Dung"],
    "Score": [7, 8, 8, 9, 6, 6]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 15. Convert Data Types

Given:

```python
df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Price": ["10.5", "20", "unknown", "15.75"],
    "Quantity": ["2", "3", "4", "5"]
})
```

### Requirements

1. Print `dtypes`.
2. Convert `Price` sang numeric equal to `pd.to_numeric(..., errors="coerce")`.
3. Convert `Quantity` sang `int`.
4. Print `dtypes` again.
5. Check missing values in `Price`.
6. Explain what `"unknown"` becomes and why.

### Hint

Hint: use `pd.to_numeric(..., errors='coerce')` cho column has dirty data; `astype(int)` is appropriate when you are sure there are no invalid values left.

### Incomplete Starter Code

```python
# Starter-code hint
print(df.dtypes)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors=...
)

df["Quantity"] = df["Quantity"].astype(...)

print(df.dtypes)
print(df["Price"].isna())
```

```python
# Write your solution here

df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Price": ["10.5", "20", "unknown", "15.75"],
    "Quantity": ["2", "3", "4", "5"]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 16. Clean String Data

Given:

```python
df = pd.DataFrame({
    "Name": [" An ", "BINH", " chi ", "DuNg"],
    "City": [" HANOI", "hanoi ", "DaNang", " HCM "]
})
```

### Requirements

1. Remove leading and trailing spaces from `Name` and `City`.
2. Convert `Name` to lowercase.
3. Convert `City` to uppercase.
4. Replace `"HANOI"` equal to `"HA NOI"`.
5. Print the result.
6. Do not use a Python loop.

### Hint

Hint: string methods can be chained, for example `.str.strip().str.lower()`.

### Incomplete Starter Code

```python
# Starter-code hint
df["Name"] = (
    df["Name"]
    .str.____()
    .str.____()
)

df["City"] = (
    df["City"]
    .str.____()
    .str.____()
)

df["City"] = df["City"].str.replace(
    ...,
    ...
)
```

```python
# Write your solution here

df = pd.DataFrame({
    "Name": [" An ", "BINH", " chi ", "DuNg"],
    "City": [" HANOI", "hanoi ", "DaNang", " HCM "]
})

# TODO
```

**Student explanation:**

-

---

# PART 5 - TRANSFORMATION, COMPUTATION, AND STATISTICS

## Exercise 17. Create New Columns

Given:

```python
sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})
```

### Requirements

1. Create:
   `Revenue = Quantity * Price`
2. Create:
   `PriceWithTax = Price * 1.1`
3. Print the new DataFrame.
4. Calculate sum Revenue.
5. Find Product has Revenue maximum.

### Hint

Hint: Pandas supports vectorized operations between columns; no loop is needed.

### Incomplete Starter Code

```python
# Starter-code hint
sales["Revenue"] = sales["Quantity"] * sales["Price"]
sales["PriceWithTax"] = sales["Price"] * ...

total_revenue = sales["Revenue"].____()
idx_max = sales["Revenue"].____()
top_product = sales.loc[idx_max, "Product"]
```

```python
# Write your solution here

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 18. `map()` and `apply()`

Given:

```python
students = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Score": [4.5, 7.0, 8.5, 5.0]
})
```

### Requirements

1. Create column `Status`:
   - `"Pass"` if Score >= 5;
   - `"Fail"` if Score < 5.
2. Create column `SquaredScore = Score ** 2`.
3. Implement the task using `map()` or `apply()`.
4. Print the result.
5. Explain the basic similarities and differences between `map()` and `apply()` on a Series.

### Hint

Hint: use `Series.map(lambda x: ...)` or `Series.apply(lambda x: ...)`.

### Incomplete Starter Code

```python
# Starter-code hint
students["Status"] = students["Score"].map(
    lambda x: ... if x >= ... else ...
)

students["SquaredScore"] = students["Score"].apply(
    lambda x: ...
)
```

```python
# Write your solution here

students = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Score": [4.5, 7.0, 8.5, 5.0]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 19. Normalize Data

Given:

```python
df = pd.DataFrame({
    "Value": [10, 20, 30, 40, 50]
})
```

### Requirements

1. Create a `MinMax` column using the min-max formula.
2. Create column `ZScore`.
3. Check that the minimum of `MinMax` equals 0.
4. Check that the maximum of `MinMax` equals 1.
5. Check that the mean of `ZScore` is approximately 0.
6. Explain difference keepa min-max normalization and z-score standardization.

### Hint

Hint: min-max use `(x-min)/(max-min)`; z-score use `(x-mean)/std`.

### Incomplete Starter Code

```python
# Starter-code hint
x = df["Value"]

df["MinMax"] = (
    (x - x.____()) /
    (x.____() - x.____())
)

df["ZScore"] = (
    (x - x.____()) /
    x.____()
)
```

```python
# Write your solution here

df = pd.DataFrame({
    "Value": [10, 20, 30, 40, 50]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 20. Descriptive Statistics

Given:

```python
df = pd.DataFrame({
    "Sales": [100, 120, 90, 150, 130, 110],
    "Cost": [70, 80, 60, 100, 85, 75]
})
```

### Requirements

1. Run `describe()`.
2. Calculate separately:
   - mean;
   - median;
   - min;
   - max;
   - std.
3. Create column `Profit = Sales - Cost`.
4. Calculate mean and max of Profit.
5. Write a short comment.

### Hint

Hint: use `describe()` for an overview and vectorized arithmetic to create `Profit`.

### Incomplete Starter Code

```python
# Starter-code hint
print(df.describe())

df["Profit"] = df["Sales"] - df["Cost"]

mean_profit = df["Profit"].____()
max_profit = df["Profit"].____()
```

```python
# Write your solution here

df = pd.DataFrame({
    "Sales": [100, 120, 90, 150, 130, 110],
    "Cost": [70, 80, 60, 100, 85, 75]
})

# TODO
```

**Student comments:**

-

---

# PART 6 - GROUPBY, AGGREGATION, AND RESHAPING

## Exercise 21. Basic `groupby()`

Given:

```python
sales = pd.DataFrame({
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Product": ["A", "A", "B", "B", "A", "B"],
    "Sales": [100, 120, 90, 150, 130, 110]
})
```

### Requirements

1. Calculate sum Sales by Region.
2. Calculate mean Sales by Region.
3. Calculate sum Sales by Product.
4. Print all results.
5. Explain what `groupby()` does conceptually.

### Hint

Hint: the basic pattern is `df.groupby('key')['value'].aggregation()`.

### Incomplete Starter Code

```python
# Starter-code hint
sum_region = sales.groupby("Region")["Sales"].____()
mean_region = sales.groupby("Region")["Sales"].____()
sum_product = sales.groupby("Product")["Sales"].____()
```

```python
# Write your solution here

sales = pd.DataFrame({
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Product": ["A", "A", "B", "B", "A", "B"],
    "Sales": [100, 120, 90, 150, 130, 110]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 22. `agg()` with Multiple Aggregations

Use the `sales` DataFrame.

### Requirements

1. Group by `Region`.
2. For the `Sales` column, calculate:
   - count;
   - sum;
   - mean;
   - min;
   - max.
3. Store the result as `summary`.
4. Print `summary`.
5. Explain why `agg()` useful.

### Hint

Hint: use `.agg(['count', 'sum', 'mean', 'min', 'max'])` on the column after `groupby()`.

### Incomplete Starter Code

```python
# Starter-code hint
summary = (
    sales
    .groupby("Region")["Sales"]
    .agg([...])
)

print(summary)
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

### Automated Check

```python
try:
    assert "sum" in summary.columns
    assert "mean" in summary.columns
    assert summary.shape[0] == 2
    print("Requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

## Exercise 23. Group by Multiple Columns

Use `sales`.

### Requirements

1. Group by `Region` and `Product`.
2. Calculate sum Sales.
3. Convert the result back to a DataFrame using `reset_index()`.
4. Print the result.
5. Explain the meaning of the MultiIndex before using `reset_index()`.

### Hint

Hint: pass a list of multiple columns to `groupby([...])`; use `reset_index()` to turn the grouping keys back into regular columns.

### Incomplete Starter Code

```python
# Starter-code hint
summary2 = (
    sales
    .groupby([..., ...])["Sales"]
    .____()
    .reset_index()
)
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 24. Pivot Table

Use the `sales` DataFrame.

### Requirements

Create pivot table:

- rows: `Region`;
- columns: `Product`;
- values: `Sales`;
- aggregation: `sum`.

Then:

1. in pivot table;
2. calculate the sum of each row;
3. explain how the pivot table makes the data easier to read.

### Hint

Hint: use `pd.pivot_table()` with `values`, `index`, `columns`, and `aggfunc`.

### Incomplete Starter Code

```python
# Starter-code hint
pivot = pd.pivot_table(
    sales,
    values=...,
    index=...,
    columns=...,
    aggfunc=...
)

row_total = pivot.sum(axis=...)
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 25. `pivot()` and `melt()`

Given:

```python
df = pd.DataFrame({
    "Date": ["2026-01", "2026-01", "2026-02", "2026-02"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 120, 130, 150]
})
```

### Requirements

1. Use `pivot()` to convert the data to wide format:
   - index: Date
   - columns: Product
   - values: Sales
2. Use `reset_index()`.
3. Use `melt()` to convert it back to long format.
4. Print the `shape` values.
5. Explain the difference between long format and wide format.

### Hint

Hint: `pivot()` converts long → wide; `pd.melt()` is commonly used after `reset_index()` to convert wide → long.

### Incomplete Starter Code

```python
# Starter-code hint
wide = df.pivot(
    index=...,
    columns=...,
    values=...
)

wide_reset = wide.reset_index()

long = pd.melt(
    wide_reset,
    id_vars=...,
    var_name=...,
    value_name=...
)
```

```python
# Write your solution here

df = pd.DataFrame({
    "Date": ["2026-01", "2026-01", "2026-02", "2026-02"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 120, 130, 150]
})

# TODO
```

**Student explanation:**

-

---

# PART 7 - MERGE, JOIN, AND CONCAT

## Exercise 26. Inner Merge

Given:

```python
customers = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04"],
    "Name": ["An", "Binh", "Chi", "Dung"]
})

orders = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04"],
    "CustomerID": ["C01", "C02", "C02", "C05"],
    "Amount": [100, 200, 150, 300]
})
```

### Requirements

1. Inner merge by `CustomerID`.
2. Print the result.
3. Compare the number of rows in:
   - customers;
   - orders;
   - merged.
4. Explain why `C03`, `C04`, and `C05` may not appear in the inner merge.

### Hint

Hint: `pd.merge(left, right, on='CustomerID', how='inner')` keeps only keys that appear in both tables.

### Incomplete Starter Code

```python
# Starter-code hint
merged = pd.merge(
    customers,
    orders,
    on=...,
    how=...
)

print(merged)
```

```python
# Write your solution here

customers = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04"],
    "Name": ["An", "Binh", "Chi", "Dung"]
})

orders = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04"],
    "CustomerID": ["C01", "C02", "C02", "C05"],
    "Amount": [100, 200, 150, 300]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 27. Left, Right, and Outer Merge

Use `customers` and `orders`.

### Requirements

1. Perform:
   - left merge;
   - right merge;
   - outer merge.
2. Print the `shape` of each result.
3. Find customers without orders from the left merge.
4. Find orders without customer information from the right or outer merge.
5. Explain the differences among the four join types:
   - inner;
   - left;
   - right;
   - outer.

### Hint

Hint: repeat `pd.merge()` with `how='left'`, `'right'`, and `'outer'`; use `isna()` to find unmatched records.

### Incomplete Starter Code

```python
# Starter-code hint
left_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how=...
)

right_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how=...
)

outer_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how=...
)

customers_without_orders = left_merge[
    left_merge["OrderID"].____()
]
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 28. `concat()`

Given:

```python
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Value": [10, 20]
})

df2 = pd.DataFrame({
    "ID": [3, 4],
    "Value": [30, 40]
})
```

### Requirements

1. Concatenate `df1` and `df2` by rows.
2. Use `ignore_index=True`.
3. Create another DataFrame with a `Category` column and concatenate by columns.
4. In `shape`.
5. Explain difference keepa `concat()` and `merge()`.

### Hint

Hint: `pd.concat([df1, df2], axis=0, ignore_index=True)` concatenates by rows; `axis=1` concatenates by columns.

### Incomplete Starter Code

```python
# Starter-code hint
rows = pd.concat(
    [df1, df2],
    axis=...,
    ignore_index=...
)

category = pd.DataFrame({
    "Category": [...]
})

cols = pd.concat(
    [..., ...],
    axis=...
)
```

```python
# Write your solution here

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Value": [10, 20]
})

df2 = pd.DataFrame({
    "ID": [3, 4],
    "Value": [30, 40]
})

# TODO
```

**Student explanation:**

-

---

# PART 8 - CORRELATION, TIME SERIES, AND VISUALIZATION

## Exercise 29. Correlation

Given:

```python
df = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50, 60],
    "Sales": [100, 120, 145, 170, 210, 230],
    "Price": [20, 19, 18, 18, 17, 16]
})
```

### Requirements

1. Calculate the correlation matrix.
2. Calculate the correlations separately between:
   - Advertising and Sales;
   - Price and Sales.
3. Find the pair of variables with the strongest positive correlation.
4. Write a short comment.
5. Explain why correlation does not imply causation.

### Hint

Hint: use `df.corr(numeric_only=True)` and `Series.corr(other_series)`.

### Incomplete Starter Code

```python
# Starter-code hint
corr_matrix = df.corr(numeric_only=True)

ad_sales = df["Advertising"].corr(
    df["Sales"]
)

price_sales = df["Price"].corr(
    df["Sales"]
)
```

```python
# Write your solution here

df = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50, 60],
    "Sales": [100, 120, 145, 170, 210, 230],
    "Price": [20, 19, 18, 18, 17, 16]
})

# TODO
```

**Student comments:**

-

---

## Exercise 30. Convert Dates

Given:

```python
df = pd.DataFrame({
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04"
    ],
    "Sales": [100, 120, 90, 150]
})
```

### Requirements

1. Print the initial `dtypes`.
2. Convert `Date` to datetime using `pd.to_datetime()`.
3. Print `dtypes` again.
4. Create the following columns:
   - Year;
   - Month;
   - Day.
5. Set `Date` as the index.
6. Sort chronologically.

### Hint

Hint: use `pd.to_datetime()`, then access `.dt.year`, `.dt.month`, and `.dt.day` before setting Date as the index.

### Incomplete Starter Code

```python
# Starter-code hint
df["Date"] = pd.to_datetime(
    df["Date"]
)

df["Year"] = df["Date"].dt.____
df["Month"] = df["Date"].dt.____
df["Day"] = df["Date"].dt.____

df = df.set_index(...)
df = df.sort_index()
```

```python
# Write your solution here

df = pd.DataFrame({
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04"
    ],
    "Sales": [100, 120, 90, 150]
})

# TODO
```

**Student explanation:**

-

---

## Exercise 31. Resample Time Series

Create the data:

```python
dates = pd.date_range(
    start="2026-01-01",
    periods=30,
    freq="D"
)

df = pd.DataFrame({
    "Date": dates,
    "Sales": np.arange(100, 130)
}).set_index("Date")
```

### Requirements

1. Calculate sum Sales by week.
2. Calculate mean Sales by week.
3. Calculate sum Sales by month.
4. Print the result.
5. Explain how resampling changes the time granularity.

### Hint

Hint: after `Date` becomes a `DatetimeIndex`, use `.resample('W')` or `.resample('ME')`, then aggregate.

### Incomplete Starter Code

```python
# Starter-code hint
weekly_sum = df["Sales"].resample(...).____()
weekly_mean = df["Sales"].resample(...).____()
monthly_sum = df["Sales"].resample(...).____()
```

```python
# Write your solution here

dates = pd.date_range(
    start="2026-01-01",
    periods=30,
    freq="D"
)

df = pd.DataFrame({
    "Date": dates,
    "Sales": np.arange(100, 130)
}).set_index("Date")

# TODO
```

**Student explanation:**

-

---

## Exercise 32. Rolling Statistics

Use the time series from Exercise 31.

### Requirements

1. Create `MA3`: a 3-day moving average.
2. Create `MA7`: a 7-day moving average.
3. Print the first 10 rows.
4. Count the `NaN` values in `MA3` and `MA7`.
5. Explain why the first values are missing.

### Hint

Hint: `rolling(window=k).mean()` requires enough `k` observations, so the first values may be `NaN`.

### Incomplete Starter Code

```python
# Starter-code hint
df["MA3"] = (
    df["Sales"]
    .rolling(window=...)
    .____()
)

df["MA7"] = (
    df["Sales"]
    .rolling(window=...)
    .____()
)

print(df[["Sales", "MA3", "MA7"]].head(10))
```

```python
# Write your solution here

# TODO
```

**Student explanation:**

-

---

## Exercise 33. Quick Visualization with Pandas

Given:

```python
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 90, 150, 170],
    "Advertising": [10, 15, 8, 20, 25]
})
```

### Requirements

Create:

1. line chart of Sales by Month;
2. bar chart of Sales;
3. histogram of Sales;
4. scatter plot keepa Advertising and Sales.

Each chart should include:

- title;
- xlabel;
- ylabel.

### Hint

Hint: use `df.plot(...)` or `Series.plot(...)`; pass `kind`, `x`, `y`, and `title`.

### Incomplete Starter Code

```python
# Starter-code hint
df.plot(
    x=...,
    y=...,
    kind="line",
    title=...
)

df.plot(
    x=...,
    y=...,
    kind="bar",
    title=...
)

df["Sales"].plot(
    kind=...,
    title=...
)

df.plot(
    x=...,
    y=...,
    kind=...,
    title=...
)
```

```python
# Write your solution here

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 90, 150, 170],
    "Advertising": [10, 15, 8, 20, 25]
})

# TODO
```

**Student comments:**

-

---

# PART 9 - INTEGRATED EXERCISE

## Exercise 34. Analyze Sales Data with Pandas

Given:

```python
sales = pd.DataFrame({
    "OrderID": [
        "O01", "O02", "O03", "O04",
        "O05", "O06", "O07", "O08",
        "O09", "O10"
    ],
    "Date": [
        "2026-01-02", "2026-01-05", "2026-01-07",
        "2026-01-10", "2026-01-12", "2026-01-15",
        "2026-01-18", "2026-01-20", "2026-01-23",
        "2026-01-28"
    ],
    "Region": [
        "North", "South", "North", "Central",
        "South", "North", "Central", "South",
        "North", "Central"
    ],
    "Product": [
        "A", "B", "A", "C", "B",
        "C", "A", "C", "B", "A"
    ],
    "Quantity": [2, 5, 3, 4, 2, 6, 5, 3, 4, 2],
    "Price": [
        10.0, 8.0, 10.0, 12.0, np.nan,
        12.0, 10.0, 12.0, 8.0, 10.0
    ]
})
```

### Requirements

Do not use a Python loop to process rows one by one:

1. Print:
   - `shape`;
   - `dtypes`;
   - `info()`.
2. Convert `Date` sang datetime.
3. Count missing values.
4. Replace missing `Price` values with the median `Price`.
5. Create:
   `Revenue = Quantity * Price`.
6. Calculate:
   - sum Revenue;
   - mean Revenue;
   - max Revenue.
7. Filter orders whose Revenue is greater than mean Revenue.
8. Calculate sum Revenue by Region.
9. Calculate sum Revenue by Product.
10. Group by `Region` and calculate:
    - count;
    - sum;
    - mean Revenue.
11. Create pivot table:
    - index: Region;
    - columns: Product;
    - values: Revenue;
    - aggfunc: sum.
12. Find OrderID has Revenue maximum.
13. Sort the data by Revenue in descending order.
14. Set Date as the index and calculate weekly Revenue totals.
15. Create a 3-period moving average of Revenue.
16. Create a Revenue-by-Date chart.
17. Write 3-5 comments about the results.

### Hint

Hint: follow the pipeline in sequence: inspect → datetime → missing → fill → Revenue → filter → groupby → pivot → sort → time index → resample/rolling → plot.

### Incomplete Starter Code

```python
# Starter-code hint

# 1. Inspect
print(sales.shape)
print(sales.dtypes)
sales.info()

# 2. Date
sales["Date"] = pd.to_datetime(...)

# 3-4. Missing values
print(sales.isna().sum())
sales["Price"] = sales["Price"].fillna(
    sales["Price"].____()
)

# 5. Revenue
sales["Revenue"] = ...

# 6. Summary
total_revenue = sales["Revenue"].____()
mean_revenue = sales["Revenue"].____()
max_revenue = sales["Revenue"].____()

# 7. Filter
high_orders = sales[
    sales["Revenue"] > ...
]

# 8-10. Groupby
revenue_region = ...
revenue_product = ...

region_summary = (
    sales
    .groupby("Region")["Revenue"]
    .agg([...])
)

# 11. Pivot
pivot = pd.pivot_table(
    sales,
    values=...,
    index=...,
    columns=...,
    aggfunc=...
)

# 12. Largest order
idx = sales["Revenue"].____()
largest_order = sales.loc[idx, "OrderID"]

# 13. Sort
sorted_sales = sales.sort_values(
    ...,
    ascending=...
)

# 14-16. Time series
ts = sales.set_index("Date").sort_index()
weekly = ts["Revenue"].resample(...).____()
ts["MA3"] = ts["Revenue"].rolling(window=...).____()

# ts[["Revenue", "MA3"]].plot()
```

```python
# Write your solution here

sales = pd.DataFrame({
    "OrderID": [
        "O01", "O02", "O03", "O04",
        "O05", "O06", "O07", "O08",
        "O09", "O10"
    ],
    "Date": [
        "2026-01-02", "2026-01-05", "2026-01-07",
        "2026-01-10", "2026-01-12", "2026-01-15",
        "2026-01-18", "2026-01-20", "2026-01-23",
        "2026-01-28"
    ],
    "Region": [
        "North", "South", "North", "Central",
        "South", "North", "Central", "South",
        "North", "Central"
    ],
    "Product": [
        "A", "B", "A", "C", "B",
        "C", "A", "C", "B", "A"
    ],
    "Quantity": [2, 5, 3, 4, 2, 6, 5, 3, 4, 2],
    "Price": [
        10.0, 8.0, 10.0, 12.0, np.nan,
        12.0, 10.0, 12.0, 8.0, 10.0
    ]
})

# TODO
```

**Student comments:**

-
-
-
-
-

### Automated Check

```python
try:
    assert "Revenue" in sales.columns
    assert sales["Price"].isna().sum() == 0
    assert pd.api.types.is_datetime64_any_dtype(sales["Date"])
    assert sales["Revenue"].notna().all()
    print("Basic requirements satisfied.")
except Exception as e:
    print("Not yet satisfied:", e)
```

---

# PART 10 - INTEGRATED MERGE EXERCISE

## Exercise 35. Analyze Customers and Orders

Given:

```python
customers = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04", "C05"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "City": ["Hanoi", "Hanoi", "Danang", "HCM", "Hanoi"]
})

orders = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06"],
    "CustomerID": ["C01", "C02", "C01", "C03", "C02", "C06"],
    "Amount": [100, 200, 150, 120, 180, 300]
})
```

### Requirements

1. Inner merge the two tables.
2. Perform a left merge starting from `customers`.
3. Outer merge.
4. Identify customers who have not made a purchase.
5. Identify orders with no matching customer.
6. Calculate sum Amount by customer.
7. Calculate sum Amount by City.
8. Find the customer with the highest spending.
9. Create a table containing:
   - CustomerID;
   - Name;
   - TotalAmount.
10. Write a short comment.

### Hint

Hint: merge first, then use `groupby()` on `Amount`. To retain customers without orders, start with a left merge from the customers table.

### Incomplete Starter Code

```python
# Starter-code hint

inner = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how=...
)

left = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how=...
)

outer = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how=...
)

customers_without_orders = left[
    left["OrderID"].____()
]

orders_without_customers = outer[
    outer["Name"].____()
]

total_by_customer = (
    inner.groupby(
        ["CustomerID", "Name"]
    )["Amount"]
    .____()
    .reset_index()
)

total_by_city = (
    inner.groupby("City")["Amount"]
    .____()
)
```

```python
# Write your solution here

customers = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04", "C05"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "City": ["Hanoi", "Hanoi", "Danang", "HCM", "Hanoi"]
})

orders = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06"],
    "CustomerID": ["C01", "C02", "C01", "C03", "C02", "C06"],
    "Amount": [100, 200, 150, 120, 180, 300]
})

# TODO
```

**Student comments:**

-
-
-

---

# SELF-ASSESSMENT AFTER THE PRACTICE SESSION

Check the skills you have completed:

- [ ] Create `Series` and `DataFrame` objects.
- [ ] Interpret `shape`, `columns`, `index`, and `dtypes`.
- [ ] Use `head()`, `tail()`, `info()`, and `describe()`.
- [ ] Distinguish `loc` from `iloc`.
- [ ] Filter data using one or multiple conditions.
- [ ] Sort data using `sort_values()`.
- [ ] Read and ghi CSV, Excel and JSON.
- [ ] Detect missing data using `isna()`.
- [ ] Handle missing values using `dropna()` and `fillna()`.
- [ ] Detect and remove duplicates.
- [ ] Convert data types.
- [ ] Clean string data.
- [ ] Create new columns and apply functions.
- [ ] Perform normalization and standardization.
- [ ] Use `groupby()` and `agg()`.
- [ ] Create pivot table.
- [ ] Use `pivot()` and `melt()`.
- [ ] Distinguish `merge()` from `concat()`.
- [ ] Perform inner, left, right, and outer joins.
- [ ] Calculate correlation.
- [ ] Convert datetime data.
- [ ] Use `resample()` and `rolling()`.
- [ ] Create visualization nhanh equal to Pandas.
- [ ] Complete the integrated data-analysis exercise.
