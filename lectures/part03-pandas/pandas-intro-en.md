# Introduction to Pandas
**Language:** English  
**Topic:** Data manipulation, cleaning, analysis, and tabular data processing with Pandas

---

## 1. Lesson Introduction
**Pandas** is an open-source Python library designed for **data manipulation and analysis**. It is built on top of NumPy and provides high-level data structures and functions for working efficiently with structured and tabular data.

Pandas is especially useful for tasks such as:

- reading data from CSV, Excel, JSON, and text files;
- cleaning and preparing datasets;
- filtering and selecting observations;
- handling missing values;
- transforming columns and data types;
- grouping and aggregating data;
- merging and joining multiple datasets;
- reshaping data;
- calculating descriptive statistics;
- analyzing time-series data;
- creating quick visualizations.

Pandas revolves around two primary data structures:

- **Series**: a one-dimensional labeled array;
- **DataFrame**: a two-dimensional labeled tabular structure.

A DataFrame is conceptually similar to an Excel worksheet or a database table, with rows and columns that can have labels.

---

## 2. Learning Outcomes
After completing this lesson, learners will be able to:

- Explain the role of Pandas in Data Science and data analysis.
- Distinguish between a Pandas Series and DataFrame.
- Create Series and DataFrames from Python objects and NumPy arrays.
- Inspect a DataFrame using common attributes and methods.
- Access rows, columns, and subsets using labels and positions.
- Filter data using one or multiple conditions.
- Read and write CSV, Excel, JSON, and text-based datasets.
- Identify and handle missing values.
- Remove duplicate records.
- Convert data types.
- Manipulate string columns.
- Sort and reshape DataFrames.
- Merge, join, and concatenate datasets.
- Group and aggregate data.
- Create pivot tables.
- Perform descriptive statistical analysis.
- Calculate correlation.
- Work with basic time-series data.
- Create quick visualizations using Pandas plotting functions.

---

## 3. Lesson Structure
The lesson is organized into the following main sections:

1. Basics
2. DataFrame
3. Series
4. Data Input and Output (I/O)
5. Data Cleaning
6. Operations
7. Advanced Operations
8. Review Questions
9. Practical Exercises
10. Answers and Suggested Responses

---

## 4. Prerequisites
Learners should have:

- Basic Python knowledge.
- Familiarity with variables, lists, dictionaries, loops, and functions.
- Basic understanding of NumPy arrays.
- Access to Jupyter Notebook, JupyterLab, Google Colab, VS Code, or a similar environment.

---

# Part 1. Basics
## 1.1. What Is Pandas?
Pandas is a Python library for working with structured data. It provides tools for data cleaning, transformation, analysis, and integration with other data-science libraries.

Pandas is built on top of NumPy, which means it can take advantage of efficient numerical arrays while providing labels, indexes, and table-oriented operations.

The name **Pandas** is derived from the term **panel data**, which is commonly used in econometrics.

## 1.2. Why Is Pandas Useful?
Pandas is commonly used for:

- reading and writing data;
- cleaning datasets;
- handling missing values;
- selecting and filtering observations;
- transforming variables;
- merging datasets;
- grouping observations;
- calculating summary statistics;
- preparing data for visualization and machine learning.

## 1.3. Installation and Import
Install Pandas using:

```bash
pip install pandas
```

Import Pandas using the standard alias:

```python
import pandas as pd
```

Check the installed version:

```python
import pandas as pd

print(pd.__version__)
```

### Mini Exercise — `pd.__version__`

Complete the command to print the installed Pandas version.

```python
# version = ...
# print(version)
```

**Hint:** use `pd.__version__`.

## 1.4. Important Facts
- A **DataFrame** is a two-dimensional labeled structure with rows and columns.
- A **Series** is a one-dimensional labeled array.
- Pandas works closely with NumPy, Matplotlib, and Scikit-learn.
- Missing values can be handled with methods such as `.dropna()` and `.fillna()`.

## 1.5. Quick Check
**Question 1.** Which alias is conventionally used for Pandas?

A. `pn`  
B. `pd`  
C. `ps`  
D. `pa`

**Question 2.** Which Pandas structure is two-dimensional?

A. `Series`  
B. `tuple`  
C. `DataFrame`  
D. `ndarray`

## Exercises
### Exercise 1.1. Check Your Environment
Run:

```python
import pandas as pd

print(pd.__version__)
```

Record:

1. the Pandas version;
2. the standard Pandas alias;
3. one reason Pandas is useful in data analysis.

### Exercise 1.2. Series or DataFrame?
Decide whether each case is more naturally represented by a Series or DataFrame:

1. a list of monthly sales values;
2. a student table containing ID, name, age, and GPA;
3. one column of product prices;
4. a dataset containing 1,000 customers and 12 attributes.

---

# Part 2. DataFrame
## 2.1. What Is a DataFrame?
A **DataFrame** is a two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled rows and columns.

A DataFrame can contain different data types across columns.

Example:

```python
import pandas as pd

data = {
    "Name": ["An", "Binh", "Chi"],
    "Age": [20, 21, 19],
    "GPA": [3.2, 3.6, 3.4]
}

df = pd.DataFrame(data)

print(df)
```

### Mini Exercise — `pd.DataFrame()`

Create a DataFrame named `products` with columns `Product`, `Price`, and `Stock`.

```python
# products = pd.DataFrame({
#     "Product": [...],
#     "Price": [...],
#     "Stock": [...]
# })

# print(products)
```

**Hint:** all columns must contain the same number of values.

## 2.2. Key Commands for Creating and Inspecting DataFrames
| Command | Meaning |
|---|---|
| `pd.DataFrame(data)` | Create a DataFrame from a dictionary, list, NumPy array, or similar object. |
| `df.head()` | Display the first rows. |
| `df.tail()` | Display the last rows. |
| `df.shape` | Return the number of rows and columns. |
| `df.columns` | Return column labels. |
| `df.index` | Return row labels. |
| `df.dtypes` | Return data types of columns. |
| `df.info()` | Display a structural summary of the DataFrame. |
| `df.describe()` | Return descriptive statistics for numerical columns. |

## 2.3. Inspecting a DataFrame
```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
```

Use:

```python
df.info()
```

### Mini Exercise — `head()`, `shape`, `columns`, `dtypes`, `info()`

Complete the inspection commands.

```python
# print(df.head(...))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# df.info()
```

Then state the number of rows and columns.

to inspect:

- number of rows;
- number of columns;
- column names;
- missing values;
- data types.

## 2.4. DataFrame Index
Pandas assigns a default integer index if no index is provided.

```python
print(df.index)
```

### Mini Exercise — `index`

Inspect the DataFrame index.

```python
# current_index = ...
# print(current_index)
```

State whether it is a default integer index or a custom index.

A custom index can be specified:

```python
df = pd.DataFrame(
    data,
    index=["S01", "S02", "S03"]
)

print(df)
```

## 2.5. Accessing Columns
Select one column:

```python
print(df["Name"])
```

Select multiple columns:

```python
print(df[["Name", "GPA"]])
```

### Mini Exercise — Column Selection

Select:

1. only `Age`;
2. both `Name` and `Age`.

```python
# age = df[...]
# name_age = df[[..., ...]]

# print(age)
# print(name_age)
```

## 2.6. Accessing Rows with `loc` and `iloc`
`loc` selects data by **label**.

```python
print(df.loc["S01"])
```

`iloc` selects data by **integer position**.

```python
print(df.iloc[0])
```

### Mini Exercise — `loc` and `iloc`

Complete the selections.

```python
# by_label = df.loc[...]
# by_position = df.iloc[...]

# print(by_label)
# print(by_position)
```

**Question:** Which command uses labels and which uses integer positions?

This distinction is fundamental:

- `loc` → label-based selection;
- `iloc` → position-based selection.

## 2.7. Slicing DataFrames
```python
print(df.iloc[0:2])
```

Select specific rows and columns:

```python
print(df.loc[["S01", "S02"], ["Name", "GPA"]])
```

or:

```python
print(df.iloc[0:2, [0, 2]])
```

### Mini Exercise — Slicing

Select:

1. the first two rows;
2. the first two rows and columns `Name` and `GPA`.

```python
# first_two = df.iloc[...]
# subset = df.loc[..., [...]]

# print(first_two)
# print(subset)
```

## 2.8. Filtering DataFrames
Filter rows:

```python
selected = df[df["GPA"] >= 3.4]

print(selected)
```

### Mini Exercise — Boolean Filtering

Filter rows where `GPA >= 3.5`.

```python
# high_gpa = df[df["GPA"] >= ...]
# print(high_gpa)
```

## 2.9. Filtering with Multiple Conditions
```python
selected = df[
    (df["Age"] >= 20) &
    (df["GPA"] >= 3.4)
]

print(selected)
```

### Mini Exercise — Multiple Conditions

Filter students with `Age >= 20` and `GPA >= 3.5`.

```python
# selected = df[
#     (df["Age"] >= ...) &
#     (df["GPA"] >= ...)
# ]

# print(selected)
```

Use:

- `&` for AND;
- `|` for OR;
- `~` for NOT.

Each condition should normally be placed inside parentheses.

## 2.10. Sorting a DataFrame
Sort by one column:

```python
df_sorted = df.sort_values("GPA")
```

Descending order:

```python
df_sorted = df.sort_values(
    "GPA",
    ascending=False
)
```

Sort by multiple columns:

```python
df_sorted = df.sort_values(
    ["Age", "GPA"],
    ascending=[True, False]
)
```

## 2.11. Merging, Joining, and Concatenating
Concatenate DataFrames:

```python
combined = pd.concat(
    [df1, df2],
    axis=0
)
```

Merge on a key:

```python
result = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="inner"
)
```

Common join types:

- `inner`;
- `left`;
- `right`;
- `outer`.

## 2.12. Pivot Tables
A pivot table summarizes data across categories.

```python
pivot = pd.pivot_table(
    sales,
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print(pivot)
```

### Mini Exercise — `pd.pivot_table()`

Create a pivot table with mean Revenue by Region and Product.

```python
# pivot_mean = pd.pivot_table(
#     sales,
#     values="Revenue",
#     index=...,
#     columns=...,
#     aggfunc=...
# )

# print(pivot_mean)
```

## 2.13. Quick Check
**Question 1.** Which command creates a DataFrame?

A. `pd.DataFrame()`  
B. `pd.SeriesFrame()`  
C. `np.DataFrame()`  
D. `df.create()`

**Question 2.** Which selector is label-based?

A. `iloc`  
B. `loc`  
C. `shape`  
D. `head`

## Exercises
### Exercise 2.1. Create a Student DataFrame
Create a DataFrame with columns:

- `StudentID`;
- `Name`;
- `Age`;
- `GPA`.

Use at least five students.

Then display:

1. the first three rows;
2. the DataFrame shape;
3. the column names;
4. the column data types.

### Exercise 2.2. `loc` and `iloc`
Using the student DataFrame:

1. select the first row using `iloc`;
2. set `StudentID` as the index;
3. select one student using `loc`;
4. select only `Name` and `GPA`.

### Exercise 2.3. Filtering
Filter students who:

1. have GPA greater than or equal to 3.5;
2. are at least 20 years old;
3. satisfy both conditions.

### Exercise 2.4. Sorting
Sort the students:

1. by GPA ascending;
2. by GPA descending;
3. by Age ascending and GPA descending.

### Exercise 2.5. Merge
Create another DataFrame containing:

- `StudentID`;
- `Major`.

Merge it with the student DataFrame using `StudentID`.

---

# Part 3. Series
## 3.1. What Is a Series?
A **Series** is a one-dimensional labeled array capable of storing integers, strings, floating-point numbers, Python objects, and other data types.

A Series can be viewed as:

- one labeled column of a table;
- a mapping from index labels to values.

## 3.2. Creating a Series
```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

### Mini Exercise — `pd.Series()`

Create a Series containing `[12, 18, 25]` with labels `["A", "B", "C"]`.

```python
# prices = pd.Series(
#     [...],
#     index=[...]
# )

# print(prices)
```

Create a Series with custom labels:

```python
s = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

print(s)
```

## 3.3. Key Series Commands
| Command | Meaning |
|---|---|
| `pd.Series(data)` | Create a Series. |
| `s.index` | Return the Series index. |
| `s.values` | Return underlying values. |
| `s.dtype` | Return the data type. |
| `s.loc[label]` | Access by label. |
| `s.iloc[position]` | Access by integer position. |

## 3.4. Accessing Elements
```python
print(s.loc["A"])
print(s.iloc[0])
```

### Mini Exercise — Series `loc` and `iloc`

Retrieve label `"B"` and position `2`.

```python
# value_by_label = s.loc[...]
# value_by_position = s.iloc[...]
```

## 3.5. Binary Operations on Series
```python
a = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

b = pd.Series(
    [1, 2, 3],
    index=["A", "B", "C"]
)

print(a + b)
```

### Mini Exercise — Series Alignment

Predict the output before running:

```python
x = pd.Series([10, 20, 30], index=["A", "B", "C"])
y = pd.Series([1, 2, 3], index=["B", "C", "D"])

# result = x + y
# print(result)
```

Explain why unmatched labels produce missing values.

Pandas aligns Series by index labels before performing arithmetic.

## 3.6. Create a Series from a NumPy Array
```python
import numpy as np

arr = np.array([5, 10, 15])
s = pd.Series(arr)

print(s)
```

## 3.7. Quick Check
**Question 1.** A Pandas Series is:

A. a two-dimensional table  
B. a one-dimensional labeled array  
C. a database server  
D. a plotting package

**Question 2.** Which attribute returns Series labels?

A. `shape`  
B. `index`  
C. `columns`  
D. `describe`

## Exercises
### Exercise 3.1. Create a Series
Create a Series containing five product prices with custom product IDs as index labels.

Then print:

1. the Series;
2. its index;
3. its values;
4. its data type.

### Exercise 3.2. Access Series Values
Using the Series from Exercise 3.1:

1. select one value using `loc`;
2. select one value using `iloc`;
3. explain the difference.

### Exercise 3.3. Series Alignment
Create:

```python
a = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

b = pd.Series(
    [1, 2, 3],
    index=["B", "C", "D"]
)
```

Calculate:

```python
a + b
```

Explain why some positions contain missing values.

---

# Part 4. Data Input and Output (I/O)
## 4.1. Why I/O Matters
Real-world data rarely start inside a Python program. Pandas provides functions for importing data from files and exporting processed results.

Common formats include:

- CSV;
- Excel;
- JSON;
- text files;
- SQL databases.

## 4.2. Reading CSV Files
```python
df = pd.read_csv("data.csv")
```

Useful options:

```python
df = pd.read_csv(
    "data.csv",
    sep=",",
    header=0,
    encoding="utf-8"
)
```

## 4.3. Writing CSV Files
```python
df.to_csv(
    "output.csv",
    index=False
)
```

`index=False` prevents the DataFrame index from being written as an extra column.

## 4.4. Reading Excel Files
```python
df = pd.read_excel(
    "data.xlsx",
    sheet_name="Sheet1"
)
```

## 4.5. Writing Excel Files
```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

## 4.6. Reading JSON Files
```python
df = pd.read_json("data.json")
```

### Mini Exercise — `pd.read_json()`

Read `customers.json` into `customer_df`.

```python
# customer_df = pd.read_json(...)
```

## 4.7. Writing JSON Files
```python
df.to_json(
    "output.json",
    orient="records"
)
```

## 4.8. Reading Text Files
Text files with structured delimiters can often be read with `read_csv()`:

```python
df = pd.read_csv(
    "data.txt",
    sep="\t"
)
```

## 4.9. Key I/O Commands
| Command | Role |
|---|---|
| `pd.read_csv()` | Read CSV or delimited text files. |
| `df.to_csv()` | Write CSV files. |
| `pd.read_excel()` | Read Excel files. |
| `df.to_excel()` | Write Excel files. |
| `pd.read_json()` | Read JSON files. |
| `df.to_json()` | Write JSON files. |

## 4.10. Quick Check
**Question 1.** Which function reads a CSV file?

A. `pd.read_csv()`  
B. `pd.open_csv()`  
C. `pd.load_table_only()`  
D. `df.csv_read()`

**Question 2.** Which argument commonly prevents the DataFrame index from being exported?

A. `index=False`  
B. `index=True`  
C. `header=None`  
D. `drop_index=True`

## Exercises
### Exercise 4.1. CSV
Create a DataFrame with at least five rows and save it as:

```text
students.csv
```

Then read the file back into another DataFrame.

### Exercise 4.2. Excel
Save the same DataFrame to:

```text
students.xlsx
```

with `index=False`.

### Exercise 4.3. JSON
Export the DataFrame to JSON using:

```python
orient="records"
```

Then inspect the generated structure.

---

# Part 5. Data Cleaning
## 5.1. Why Data Cleaning Matters
Real-world datasets may contain:

- missing values;
- duplicate rows;
- inconsistent data types;
- empty columns;
- inconsistent text;
- mixed data formats.

Data cleaning aims to improve accuracy, consistency, and usability before analysis.

## 5.2. Detect Missing Values
```python
print(df.isna())
```

Count missing values:

```python
print(df.isna().sum())
```

### Mini Exercise — `isna()` and `isna().sum()`

Count missing values by column and in the whole DataFrame.

```python
# missing_by_column = df.isna().____()
# total_missing = df.isna().____().____()
```

## 5.3. Remove Missing Values
Remove rows containing missing values:

```python
clean_df = df.dropna()
```

Remove columns containing missing values:

```python
clean_df = df.dropna(axis=1)
```

### Mini Exercise — `dropna()`

Create one DataFrame with incomplete rows removed and another with incomplete columns removed.

```python
# rows_complete = df.dropna()
# cols_complete = df.dropna(axis=...)
```

## 5.4. Fill Missing Values
Fill all missing values:

```python
filled = df.fillna(0)
```

Fill one column with its mean:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

Fill a categorical variable:

```python
df["City"] = df["City"].fillna(
    "Unknown"
)
```

## 5.5. Remove Duplicates
Detect duplicates:

```python
print(df.duplicated())
```

Remove duplicate rows:

```python
df = df.drop_duplicates()
```

### Mini Exercise — `duplicated()` and `drop_duplicates()`

```python
# duplicate_mask = df.duplicated()
# duplicate_count = duplicate_mask.____()
# clean_df = df.____()
```

## 5.6. Change Data Types
Inspect data types:

```python
print(df.dtypes)
```

Convert a column:

```python
df["Age"] = df["Age"].astype(int)
```

### Mini Exercise — `astype()`

Convert `Quantity` to integer.

```python
# df["Quantity"] = df["Quantity"].astype(...)
```

Convert strings to numeric values:

```python
df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)
```

## 5.7. Drop Rows or Columns
```python
df = df.drop(
    columns=["UnusedColumn"]
)
```

Drop rows by index:

```python
df = df.drop(
    index=[0, 2]
)
```

## 5.8. String Manipulation
Convert to lowercase:

```python
df["Name"] = df["Name"].str.lower()
```

Remove surrounding spaces:

```python
df["Name"] = df["Name"].str.strip()
```

Replace text:

```python
df["City"] = df["City"].str.replace(
    "HN",
    "Hanoi"
)
```

## 5.9. Detect Mixed Data Types
Mixed data types can cause problems during analysis.

```python
df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
)
```

Invalid values are converted to `NaN`, which can then be handled explicitly.

## 5.10. Key Cleaning Commands
| Command | Meaning |
|---|---|
| `df.isna()` | Detect missing values. |
| `df.isna().sum()` | Count missing values. |
| `df.dropna()` | Remove missing observations. |
| `df.fillna(value)` | Replace missing values. |
| `df.duplicated()` | Detect duplicates. |
| `df.drop_duplicates()` | Remove duplicate rows. |
| `df.astype(type)` | Convert data type. |
| `pd.to_numeric()` | Convert values to numeric form. |
| `df.drop()` | Remove rows or columns. |
| `Series.str.*` | Apply string-processing methods. |

## 5.11. Quick Check
**Question 1.** Which method removes rows containing missing values?

A. `dropna()`  
B. `fillna()`  
C. `duplicated()`  
D. `astype()`

**Question 2.** Which method removes duplicate rows?

A. `drop_duplicates()`  
B. `dropna()`  
C. `sort_values()`  
D. `merge()`

## Exercises
### Exercise 5.1. Missing Values
Create:

```python
df = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Age": [20, None, 22, 21],
    "GPA": [3.2, 3.6, None, 3.8]
})
```

Do the following:

1. identify missing values;
2. count missing values by column;
3. fill missing `Age` values using the column mean;
4. fill missing `GPA` values using the column median.

### Exercise 5.2. Duplicates
Add a duplicated row to a DataFrame.

Then:

1. detect duplicates;
2. count duplicates;
3. remove them.

### Exercise 5.3. Data Types
Create:

```python
df = pd.DataFrame({
    "Price": ["10", "20", "unknown", "40"]
})
```

Convert `Price` to numeric using:

```python
pd.to_numeric(..., errors="coerce")
```

Explain what happens to `"unknown"`.

### Exercise 5.4. String Cleaning
Given:

```python
df = pd.DataFrame({
    "Name": [" An ", "BINH", " chi "]
})
```

Clean the column so that:

- surrounding spaces are removed;
- all names are lowercase.

---

# Part 6. Operations
## 6.1. Data Processing and Manipulation
Pandas supports column-level transformations and calculations.

Create a new column:

```python
df["Total"] = (
    df["Quantity"] * df["Price"]
)
```

Modify an existing column:

```python
df["Price"] = df["Price"] * 1.1
```

### Mini Exercise — Calculated Column

Create `Revenue = Quantity × Price`.

```python
# df["Revenue"] = df["Quantity"] * df["Price"]
# total_revenue = df["Revenue"].____()
```

## 6.2. Applying Functions
Use `map()` on a Series:

```python
df["Status"] = df["Score"].map(
    lambda x: "Pass" if x >= 5 else "Fail"
)
```

Use `apply()`:

```python
df["Squared"] = df["Value"].apply(
    lambda x: x ** 2
)
```

## 6.3. Normalization
Min-max normalization:

```python
df["Normalized"] = (
    (df["Value"] - df["Value"].min()) /
    (df["Value"].max() - df["Value"].min())
)
```

Z-score standardization:

```python
df["Z"] = (
    (df["Value"] - df["Value"].mean()) /
    df["Value"].std()
)
```

## 6.4. Descriptive Analysis
```python
print(df.describe())
```

Individual statistics:

```python
print(df["Sales"].mean())
print(df["Sales"].median())
print(df["Sales"].min())
print(df["Sales"].max())
print(df["Sales"].std())
```

### Mini Exercise — Descriptive Statistics

```python
# sales_mean = df["Sales"].____()
# sales_median = df["Sales"].____()
# sales_min = df["Sales"].____()
# sales_max = df["Sales"].____()
# sales_std = df["Sales"].____()
```

## 6.5. Grouping with `groupby()`
```python
summary = df.groupby(
    "Region"
)["Sales"].mean()

print(summary)
```

### Mini Exercise — `groupby()`

Calculate total Sales by Region.

```python
# region_total = (
#     df.groupby("Region")["Sales"].____()
# )
```

Multiple aggregations:

```python
summary = df.groupby(
    "Region"
)["Sales"].agg(
    ["count", "sum", "mean"]
)

print(summary)
```

### Mini Exercise — `agg()`

For each Region, calculate `count`, `sum`, `mean`, `min`, and `max`.

```python
# region_stats = (
#     df.groupby("Region")["Sales"]
#     .agg([...])
# )
```

## 6.6. Group by Multiple Columns
```python
summary = df.groupby(
    ["Region", "Product"]
)["Sales"].sum()
```

## 6.7. Joins and Merges
```python
result = pd.merge(
    left,
    right,
    on="ID",
    how="left"
)
```

Common join types:

- inner;
- left;
- right;
- outer.

## 6.8. Reshaping
Use `pivot()`:

```python
wide = df.pivot(
    index="Date",
    columns="Product",
    values="Sales"
)
```

Use `melt()`:

```python
long = pd.melt(
    wide.reset_index(),
    id_vars="Date"
)
```

## 6.9. Pivot Tables
```python
table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)
```

## 6.10. Key Operations
| Command | Meaning |
|---|---|
| `df["new"] = ...` | Create or transform a column. |
| `Series.map()` | Map values to new values. |
| `Series.apply()` | Apply a function to Series elements. |
| `df.describe()` | Descriptive statistics. |
| `df.groupby()` | Group observations. |
| `.agg()` | Apply multiple aggregation functions. |
| `pd.merge()` | Merge DataFrames. |
| `pd.concat()` | Concatenate DataFrames. |
| `df.pivot()` | Reshape long data to wide format. |
| `pd.melt()` | Reshape wide data to long format. |
| `pd.pivot_table()` | Create a summarized pivot table. |

## 6.11. Quick Check
**Question 1.** Which method groups observations by categories?

A. `groupby()`  
B. `dropna()`  
C. `astype()`  
D. `sort_index()`

**Question 2.** Which function combines DataFrames using a key column?

A. `pd.merge()`  
B. `pd.mean()`  
C. `pd.reshape()`  
D. `pd.filter_rows()`

## Exercises
### Exercise 6.1. Create a Calculated Column
Given:

```python
df = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Quantity": [2, 3, 5],
    "Price": [10, 20, 8]
})
```

Create:

```text
Revenue = Quantity × Price
```

### Exercise 6.2. Normalize Data
Create a numerical column and calculate:

1. min-max normalization;
2. z-score standardization.

### Exercise 6.3. Group and Aggregate
Create a sales DataFrame containing:

- Region;
- Product;
- Sales.

Calculate:

1. total sales by Region;
2. mean sales by Region;
3. count, sum, and mean using `.agg()`.

### Exercise 6.4. Merge
Create:

```text
customers(CustomerID, Name)
orders(OrderID, CustomerID, Amount)
```

Perform:

1. inner merge;
2. left merge.

Explain the difference.

### Exercise 6.5. Pivot Table
Create a pivot table showing:

- rows: Region;
- columns: Product;
- values: Sales;
- aggregation: sum.

---

# Part 7. Advanced Operations
## 7.1. Correlation
Correlation measures association between numerical variables.

```python
print(df.corr(
    numeric_only=True
))
```

Correlation between selected columns:

```python
print(
    df["Advertising"].corr(
        df["Sales"]
    )
)
```

Correlation does not by itself imply causation.

## 7.2. Data Visualization with Pandas
Pandas provides quick plotting methods built on top of Matplotlib.

Line plot:

```python
df.plot(
    x="Month",
    y="Sales",
    kind="line"
)
```

Bar chart:

```python
df.plot(
    x="Product",
    y="Sales",
    kind="bar"
)
```

Histogram:

```python
df["Sales"].plot(
    kind="hist"
)
```

Scatter plot:

```python
df.plot(
    x="Advertising",
    y="Sales",
    kind="scatter"
)
```

## 7.3. Time-Series Data
Convert a column to datetime:

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

Set Date as the index:

```python
df = df.set_index("Date")
```

Sort chronologically:

```python
df = df.sort_index()
```

### Mini Exercise — Datetime Pipeline

```python
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index(...)
# df = df.sort_index()
```

## 7.4. Extract Date Components
```python
df["Year"] = df.index.year
df["Month"] = df.index.month
df["Day"] = df.index.day
```

### Mini Exercise — Datetime Components

```python
# df["Year"] = df.index.____
# df["Month"] = df.index.____
# df["Day"] = df.index.____
```

## 7.5. Resampling Time Series
Monthly totals:

```python
monthly = df["Sales"].resample(
    "ME"
).sum()
```

Weekly mean:

```python
weekly = df["Sales"].resample(
    "W"
).mean()
```

## 7.6. Rolling Statistics
Moving average:

```python
df["MovingAvg"] = (
    df["Sales"]
    .rolling(window=3)
    .mean()
)
```

## 7.7. Key Advanced Commands
| Command | Meaning |
|---|---|
| `df.corr()` | Calculate correlation matrix. |
| `Series.corr()` | Calculate correlation between two Series. |
| `df.plot()` | Create quick visualizations. |
| `pd.to_datetime()` | Convert values to datetime. |
| `df.set_index()` | Set a column as the index. |
| `df.resample()` | Aggregate time-series data by time intervals. |
| `Series.rolling()` | Calculate rolling-window statistics. |

## 7.8. Quick Check
**Question 1.** Which function converts a column to datetime?

A. `pd.to_datetime()`  
B. `pd.date_convert_only()`  
C. `df.datetime()`  
D. `pd.time_series()`

**Question 2.** Which method calculates a correlation matrix?

A. `corr()`  
B. `merge()`  
C. `dropna()`  
D. `pivot()`

## Exercises
### Exercise 7.1. Correlation
Create:

```python
df = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50],
    "Sales": [100, 120, 150, 170, 210]
})
```

Calculate:

1. the full correlation matrix;
2. the correlation between `Advertising` and `Sales`.

### Exercise 7.2. Visualization
Using a sales DataFrame, create:

1. a line chart;
2. a bar chart;
3. a histogram;
4. a scatter plot.

### Exercise 7.3. Time-Series Index
Create a DataFrame with columns:

- `Date`;
- `Sales`.

Then:

1. convert `Date` to datetime;
2. set `Date` as index;
3. sort by date.

### Exercise 7.4. Resampling
Using daily sales data:

1. calculate weekly total sales;
2. calculate monthly average sales.

### Exercise 7.5. Moving Average
Calculate a 3-period moving average for a `Sales` Series.

---

# Part 8. Review Questions
## 8.1. Multiple-Choice Questions
**Question 1.** What is the main purpose of Pandas?

A. Data manipulation and analysis  
B. Operating-system administration  
C. Web-server management  
D. Computer graphics only

**Question 2.** Which Pandas structure is one-dimensional?

A. `DataFrame`  
B. `Series`  
C. `ndarray` only  
D. `pivot`

**Question 3.** Which selector is based on integer position?

A. `loc`  
B. `iloc`  
C. `index`  
D. `columns`

**Question 4.** Which function reads a CSV file?

A. `pd.read_csv()`  
B. `pd.csv_open()`  
C. `pd.load_csv_only()`  
D. `df.read()`

**Question 5.** Which method replaces missing values?

A. `fillna()`  
B. `drop_duplicates()`  
C. `sort_values()`  
D. `merge()`

**Question 6.** Which method removes duplicate rows?

A. `drop_duplicates()`  
B. `fillna()`  
C. `groupby()`  
D. `pivot()`

**Question 7.** Which method groups observations?

A. `groupby()`  
B. `describe()`  
C. `drop()`  
D. `astype()`

**Question 8.** Which function merges two DataFrames using a common key?

A. `pd.merge()`  
B. `pd.mean()`  
C. `pd.Series()`  
D. `pd.plot()`

**Question 9.** Which function converts values to datetime?

A. `pd.to_datetime()`  
B. `pd.to_numeric()`  
C. `pd.read_date()`  
D. `pd.datetime_only()`

**Question 10.** Which method calculates correlation?

A. `corr()`  
B. `join()`  
C. `head()`  
D. `fillna()`

## 8.2. True/False Questions
**Question 1.** A DataFrame is two-dimensional.  
**Question 2.** A Series is a one-dimensional labeled array.  
**Question 3.** `loc` is based only on integer position.  
**Question 4.** `iloc` is position-based.  
**Question 5.** `dropna()` can be used to remove missing values.  
**Question 6.** `fillna()` can replace missing values.  
**Question 7.** `groupby()` can be followed by aggregation functions.  
**Question 8.** `pd.merge()` can perform inner and left joins.  
**Question 9.** `pd.to_datetime()` can convert text dates to datetime values.  
**Question 10.** Correlation automatically proves causation.

## 8.3. Short-Answer Questions
**Question 1.** Explain the difference between a Series and a DataFrame.

**Question 2.** Explain the difference between `loc` and `iloc`.

**Question 3.** Give two methods for handling missing values.

**Question 4.** Explain the difference between `pd.concat()` and `pd.merge()`.

**Question 5.** What is the purpose of `groupby()`?

**Question 6.** Why is data-type conversion important in data cleaning?

**Question 7.** Explain what a pivot table does.

**Question 8.** State one use of `pd.to_datetime()`.

---

# Part 9. Practical Exercises
## Exercise 1. Student Data
Create a DataFrame with at least 10 students containing:

- StudentID;
- Name;
- Age;
- Major;
- GPA.

Perform:

1. inspection with `head()`, `shape`, `info()`, and `describe()`;
2. filtering for GPA >= 3.5;
3. sorting by GPA descending;
4. selecting rows using `loc` and `iloc`.

## Exercise 2. Missing Data
Add missing values to the student dataset.

Then:

1. count missing values;
2. fill missing Age with mean Age;
3. fill missing GPA with median GPA;
4. remove rows with missing Name.

## Exercise 3. CSV and Excel
Export the cleaned student dataset to:

```text
students.csv
students.xlsx
```

Read both files back into Pandas.

## Exercise 4. Sales Analysis
Create a sales dataset containing:

- Date;
- Region;
- Product;
- Quantity;
- Price.

Create:

```text
Revenue = Quantity × Price
```

Then calculate:

1. total revenue;
2. revenue by Region;
3. revenue by Product;
4. average revenue by Region;
5. a Region × Product pivot table.

## Exercise 5. Merge
Create a customer table:

```text
CustomerID, Name, City
```

and an order table:

```text
OrderID, CustomerID, Amount
```

Perform:

1. inner merge;
2. left merge;
3. identify customers without orders.

## Exercise 6. Data Cleaning
Create a messy dataset containing:

- missing values;
- duplicate records;
- spaces in names;
- mixed numeric/text values.

Clean the dataset using:

- `isna()`;
- `fillna()`;
- `dropna()`;
- `drop_duplicates()`;
- `.str.strip()`;
- `pd.to_numeric()`.

## Exercise 7. Time Series
Create daily sales data for at least 30 days.

Then:

1. convert Date to datetime;
2. set Date as index;
3. calculate weekly total sales;
4. calculate a 7-day moving average;
5. create a line plot.

---

# Part 10. Answers and Suggested Responses
## Quick Check Answers
### Basics
1. B — `pd`  
2. C — `DataFrame`

### DataFrame
1. A — `pd.DataFrame()`  
2. B — `loc`

### Series
1. B — a one-dimensional labeled array  
2. B — `index`

### I/O
1. A — `pd.read_csv()`  
2. A — `index=False`

### Data Cleaning
1. A — `dropna()`  
2. A — `drop_duplicates()`

### Operations
1. A — `groupby()`  
2. A — `pd.merge()`

### Advanced Operations
1. A — `pd.to_datetime()`  
2. A — `corr()`

## Multiple-Choice Answers
1. A  
2. B  
3. B  
4. A  
5. A  
6. A  
7. A  
8. A  
9. A  
10. A

## True/False Answers
1. True  
2. True  
3. False  
4. True  
5. True  
6. True  
7. True  
8. True  
9. True  
10. False

## Suggested Short Answers
**Question 1.** A Series is a one-dimensional labeled array, while a DataFrame is a two-dimensional labeled table with rows and columns.

**Question 2.** `loc` selects observations using labels, while `iloc` selects observations using integer positions.

**Question 3.** Missing values can be removed using `dropna()` or replaced using `fillna()`.

**Question 4.** `pd.concat()` combines DataFrames along an axis, while `pd.merge()` combines them using matching key columns.

**Question 5.** `groupby()` splits data into groups based on categorical values so that aggregation or transformation can be applied to each group.

**Question 6.** Correct data types are required for valid numerical operations, comparisons, sorting, aggregation, and modeling.

**Question 7.** A pivot table summarizes a numerical variable across one or more categorical dimensions.

**Question 8.** `pd.to_datetime()` converts date-like strings or values into Pandas datetime objects so that time-based operations can be performed.

---

# Suggested Solutions to Selected Practical Exercises
## Exercise 1. Student Data
```python
import pandas as pd

students = pd.DataFrame({
    "StudentID": ["S01", "S02", "S03", "S04", "S05"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "Age": [20, 21, 19, 22, 20],
    "Major": ["DS", "AI", "DS", "AI", "DS"],
    "GPA": [3.2, 3.7, 3.5, 3.8, 3.1]
})

print(students.head())
print(students.shape)
students.info()
print(students.describe())

high_gpa = students[
    students["GPA"] >= 3.5
]

sorted_students = students.sort_values(
    "GPA",
    ascending=False
)

print(high_gpa)
print(sorted_students)
```

## Exercise 2. Missing Data
```python
students["Age"] = students["Age"].fillna(
    students["Age"].mean()
)

students["GPA"] = students["GPA"].fillna(
    students["GPA"].median()
)

students = students.dropna(
    subset=["Name"]
)
```

## Exercise 3. CSV and Excel
```python
students.to_csv(
    "students.csv",
    index=False
)

students.to_excel(
    "students.xlsx",
    index=False
)

df_csv = pd.read_csv(
    "students.csv"
)

df_excel = pd.read_excel(
    "students.xlsx"
)
```

## Exercise 4. Sales Analysis
```python
sales["Revenue"] = (
    sales["Quantity"] *
    sales["Price"]
)

print(sales["Revenue"].sum())

print(
    sales.groupby("Region")["Revenue"].sum()
)

print(
    sales.groupby("Product")["Revenue"].sum()
)

print(
    sales.groupby("Region")["Revenue"].mean()
)

pivot = pd.pivot_table(
    sales,
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print(pivot)
```

## Exercise 5. Merge
```python
inner_result = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="inner"
)

left_result = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="left"
)

customers_without_orders = (
    left_result[
        left_result["OrderID"].isna()
    ]
)
```

## Exercise 6. Data Cleaning
```python
print(df.isna().sum())

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

df = df.drop_duplicates()

df["Name"] = (
    df["Name"]
    .str.strip()
    .str.lower()
)

df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
)
```

## Exercise 7. Time Series
```python
df["Date"] = pd.to_datetime(
    df["Date"]
)

df = df.set_index("Date")

weekly_sales = df["Sales"].resample(
    "W"
).sum()

df["MA7"] = (
    df["Sales"]
    .rolling(window=7)
    .mean()
)

df[["Sales", "MA7"]].plot()
```