# Data Access and Storage with Python

**Language:** English  
**Topic:** Accessing, importing, integrating, and storing data for data analysis with Python

---

## 1. Lesson Introduction

In a Data Science or Machine Learning project, data is rarely available in a complete DataFrame that is immediately ready for analysis. In practice, data is often distributed across multiple sources and stored in different formats.

Common data sources include:

- CSV files and other delimited text files;
- Microsoft Excel workbooks;
- JSON data returned by Web APIs;
- HTML tables published on websites;
- PDF reports and documents;
- relational databases;
- NoSQL databases.

Therefore, before performing visualization, statistical analysis, or Machine Learning modeling, an analyst needs to know how to:

- identify and access data sources;
- load data into a Python environment;
- inspect data structure and quality;
- transform data into appropriate formats;
- integrate data from multiple sources;
- store data and analytical results for subsequent use.

A typical Machine Learning workflow can be represented as follows:

```text
Define Purpose
      ↓
Obtain Data
      ↓
Explore & Clean Data
      ↓
Determine ML Task
      ↓
Choose ML Methods
      ↓
Train and Evaluate
      ↓
Deploy
```

This lesson focuses primarily on three groups of activities:

```text
Obtain Data
    +
Prepare Data
    +
Store Data
```

These activities provide the foundation for transforming raw data into data that can be used for analysis, visualization, and modeling.

---

## 2. Learning Objectives

After completing this lesson, learners should be able to:

- Explain the role of Data Access and Data Storage in the Data Science workflow.
- Distinguish among common data sources and formats.
- Read and write CSV data using NumPy.
- Read and write CSV data using Pandas.
- Use important parameters of `pd.read_csv()`.
- Process large CSV files using `chunksize`.
- Read and write Excel workbooks containing one or multiple worksheets.
- Read JSON data.
- Convert nested JSON structures into tabular form using `pd.json_normalize()`.
- Extract HTML tables using `pd.read_html()`.
- Explain the difficulties involved in extracting tables from PDF documents.
- Connect to and query SQLite databases using Python.
- Transfer data between SQL databases and Pandas DataFrames.
- Explain the document-oriented structure of MongoDB.
- Perform basic CRUD operations using PyMongo.
- Convert MongoDB data into Pandas DataFrames.
- Build a data pipeline that integrates multiple data sources.
- Select an appropriate storage format for different analytical requirements.

---

## 3. Lesson Structure

The lesson is organized into the following sections:

1. Overview of Data Access and Storage
2. Working with CSV Files Using NumPy
3. Working with CSV Files Using Pandas
4. Working with Microsoft Excel
5. Working with JSON
6. Accessing Data from HTML and PDF
7. Working with SQLite Databases
8. Working with MongoDB and PyMongo
9. Building a Multi-Source Data Pipeline
10. Best Practices

Each section combines conceptual explanations, examples, exercises, and knowledge-check questions.

---

## 4. Prerequisites

To follow this lesson effectively, learners should have:

- basic Python knowledge;
- familiarity with variables, lists, dictionaries, loops, and functions;
- basic knowledge of NumPy;
- basic knowledge of Pandas DataFrames;
- an understanding of rows, columns, and tabular data;
- access to Jupyter Notebook, JupyterLab, Google Colab, VS Code, or a similar Python environment.

---

# Part 1. Overview of Data Access and Storage

## 1.1. What Is Data Access?

**Data Access** is the process of retrieving data from a storage source and bringing it into an analytical environment.

For example, customer data stored in a CSV file can be loaded into a Pandas DataFrame:

```text
customers.csv
      ↓
pd.read_csv()
      ↓
DataFrame
```

Similarly, data stored in a database can first be queried using SQL and then transferred into a DataFrame:

```text
SQL Database
      ↓
SQL Query
      ↓
Pandas DataFrame
```

---

## 1.2. What Is Data Storage?

**Data Storage** is the process of saving data or analytical results in a format or storage system so that they can be reused later.

For example:

```text
DataFrame
    ↓
to_csv()
    ↓
report.csv
```

Or:

```text
DataFrame
    ↓
to_sql()
    ↓
Database Table
```

---

## 1.3. Common Data Sources

| Data Source Type | Examples |
|---|---|
| Flat files | CSV, TSV |
| Spreadsheets | Excel |
| Semi-structured data | JSON |
| Web data | HTML |
| Documents | PDF |
| Relational databases | SQLite, PostgreSQL, MySQL |
| NoSQL databases | MongoDB |

---

## 1.4. Structured and Semi-Structured Data

Tabular data such as:

```text
CustomerID | Name | City | Revenue
```

has a clearly defined row-and-column structure and is therefore referred to as **structured data**.

In contrast, JSON can contain nested objects and lists:

```python
{
    "customer": {
        "name": "An",
        "city": "Hanoi"
    },
    "orders": [
        {"product": "A"},
        {"product": "B"}
    ]
}
```

This type of data has a flexible and hierarchical structure and is commonly classified as **semi-structured data**.

### Exercise

Classify the following data sources into the appropriate categories:

1. `sales.csv`
2. `customers.xlsx`
3. JSON data returned by a Web API
4. `company.db`
5. MongoDB
6. A financial report in PDF format

Use the following categories:

- flat file;
- spreadsheet;
- semi-structured data;
- relational database;
- NoSQL database;
- document.

### Knowledge Check

**Question 1.** Which of the following formats is commonly considered a flat file?

A. CSV  
B. MongoDB  
C. SQLite  
D. PDF

**Question 2.** Which format naturally supports nested objects and lists?

A. JSON  
B. CSV  
C. TSV  
D. Numerical matrix

### Practical Exercise 1

Consider the following scenario:

> A company stores customer information in CSV files, product data in Excel, online orders as JSON returned by a Web API, and employee data in SQLite.

Complete the following tasks:

1. Identify the data type of each source.
2. Propose an appropriate Python function or library for reading each source.
3. Propose a suitable format for storing the final analytical dataset and explain your choice.

---

# Part 2. Working with CSV Files Using NumPy

## 2.1. Reading Data with `np.loadtxt()`

The `np.loadtxt()` function is suitable for files that:

- mainly contain numerical data;
- have a simple structure;
- contain no missing values or very few missing values.

Example:

```python
import numpy as np

data = np.loadtxt(
    "matrix_data.csv",
    delimiter=",",
    skiprows=1
)

print(data)
print(data.shape)
```

The mean of each column can be calculated using:

```python
print(
    np.mean(data, axis=0)
)
```

### Exercise — `np.loadtxt()`

Complete the following program to read data from `sales.csv`, where values are separated by commas:

```python
# data = np.loadtxt(
#     "sales.csv",
#     delimiter=...
# )

# print(data.shape)
```

After running the program, determine the number of rows and columns.

---

## 2.2. Handling Missing Values with `np.genfromtxt()`

Compared with `np.loadtxt()`, the `np.genfromtxt()` function is more flexible when the dataset contains missing values.

```python
data = np.genfromtxt(
    "numeric_data.csv",
    delimiter=",",
    skip_header=1,
    filling_values=0.0,
    dtype=float
)

print(data)
```

In this example, missing values are replaced with `0.0`.

### Exercise — `np.genfromtxt()`

Read data from `temperature.csv` and replace all missing values with `-1`.

```python
# data = np.genfromtxt(
#     "temperature.csv",
#     delimiter=",",
#     skip_header=1,
#     filling_values=...
# )
```

Then print the data to verify the result.

---

## 2.3. Writing Data with `np.savetxt()`

The `np.savetxt()` function can be used to save a NumPy array to a text file.

```python
output = np.random.randn(5, 3)

np.savetxt(
    "output.csv",
    output,
    delimiter=",",
    fmt="%.2f",
    header="A,B,C",
    comments=""
)
```

The argument `fmt="%.2f"` specifies that each number should be written with two decimal places.

### Exercise — `np.savetxt()`

Given the array:

```python
arr = np.array([
    [10.234, 20.567],
    [30.456, 40.123],
    [50.789, 60.345]
])
```

Save it to:

```text
numeric_output.csv
```

with the following requirements:

- values are separated by commas;
- each value is written with two decimal places;
- the two columns are named `A` and `B`.

---

## 2.4. Main Functions

| Function | Purpose |
|---|---|
| `np.loadtxt()` | Read numerical data from simple structured text files |
| `np.genfromtxt()` | Read numerical data with support for missing values |
| `np.savetxt()` | Write NumPy arrays to text files |

### Knowledge Check

**Question 1.** Which function is more suitable when a numerical data file contains missing values?

A. `np.genfromtxt()`  
B. `np.mean()`  
C. `np.arange()`  
D. `np.reshape()`

**Question 2.** Which function is used to write a NumPy array to a text file?

A. `np.savetxt()`  
B. `np.savecsv()`  
C. `np.write()`  
D. `np.export()`

### Practical Exercise 2

Create a file named `monthly_sales.csv` with the following content:

```text
Month,Revenue,Cost
1,120,80
2,150,
3,180,110
4,,130
```

Complete the following tasks:

1. Read the data using `np.genfromtxt()`.
2. Replace missing values with `0`.
3. Calculate the mean values of `Revenue` and `Cost`.
4. Save the processed numerical data to a new CSV file using `np.savetxt()`.

---

# Part 3. Working with CSV Files Using Pandas

## 3.1. Reading CSV Files with `pd.read_csv()`

Pandas provides the `pd.read_csv()` function for reading tabular data from CSV files.

```python
import pandas as pd

df = pd.read_csv(
    "customers.csv"
)

print(df.head())
```

Pandas is particularly suitable when the dataset contains:

- text;
- dates and times;
- multiple data types;
- missing values;
- column labels and indexes.

### Exercise — `pd.read_csv()`

Read `students.csv` into a DataFrame named `students`.

```python
# students = pd.read_csv(...)
```

Then display the first five rows.

---

## 3.2. Specifying the Delimiter with `sep`

Not every delimited file uses a comma as the separator.

For example, a semicolon-delimited file can be read using:

```python
df = pd.read_csv(
    "data.csv",
    sep=";"
)
```

For TSV files, fields are usually separated by tab characters:

```python
df = pd.read_csv(
    "data.tsv",
    sep="\t"
)
```

### Exercise — `sep`

Read `sales_semicolon.csv`, in which fields are separated by `;`.

```python
# df = pd.read_csv(
#     "sales_semicolon.csv",
#     sep=...
# )
```

---

## 3.3. Reading Selected Columns with `usecols`

The `usecols` argument allows selected columns to be loaded directly during data import.

```python
df = pd.read_csv(
    "customers.csv",
    usecols=[
        "customer_id",
        "city",
        "total_spent"
    ]
)
```

Reading only the required columns can:

- reduce memory usage;
- shorten loading time;
- remove unnecessary variables early in the analytical process.

### Exercise — `usecols`

Read `orders.csv` but load only the following three columns:

```text
OrderID
CustomerID
Amount
```

---

## 3.4. Specifying Data Types with `dtype`

Pandas can infer data types automatically, but in many situations the analyst should specify them explicitly.

```python
df = pd.read_csv(
    "customers.csv",
    dtype={
        "customer_id": str,
        "age": "Int64"
    }
)
```

Fields such as:

- CustomerID;
- StudentID;
- ProductID;
- PostalCode;

usually represent identifiers rather than numerical measurements. Therefore, storing them as strings is often more appropriate.

### Exercise — `dtype`

Read `students.csv` with the following data types:

```text
StudentID → str
Age → Int64
```

Then use `dtypes` to verify the result.

---

## 3.5. Parsing Dates with `parse_dates`

Pandas can convert one or more columns directly to datetime during import.

```python
df = pd.read_csv(
    "orders.csv",
    parse_dates=["OrderDate"]
)
```

Check the data types using:

```python
print(df.dtypes)
```

### Exercise — `parse_dates`

Read `sales.csv` and convert the `Date` column to datetime during the import process.

---

## 3.6. Defining Missing Values with `na_values`

In real datasets, missing values may be represented using many different symbols.

```python
df = pd.read_csv(
    "customers.csv",
    na_values=[
        "NA",
        "N/A",
        "-",
        "missing"
    ]
)
```

Pandas converts these symbols into standard missing values.

### Exercise — `na_values`

Read a file in which the following symbols should all be treated as missing values:

```text
NULL
?
-
```

After loading the data, use `isna().sum()` to inspect the number of missing values in each column.

---

## 3.7. Character Encoding

UTF-8 is commonly used when working with Vietnamese or other non-ASCII text.

```python
df = pd.read_csv(
    "customers.csv",
    encoding="utf-8"
)
```

When exporting CSV files intended for Microsoft Excel on Windows, the following encoding can be useful:

```python
df.to_csv(
    "customers_clean.csv",
    index=False,
    encoding="utf-8-sig"
)
```

---

## 3.8. Inspecting Data After Import

After reading a dataset, its structure and quality should be inspected immediately.

Common commands include:

```python
df.head()
```

```python
df.shape
```

```python
df.info()
```

```python
df.dtypes
```

```python
df.isna().sum()
```

These commands help identify:

- the number of rows and columns;
- column names;
- data types;
- non-missing values;
- missing-value counts.

### Exercise

Complete the commands below to inspect the DataFrame `df`:

```python
# print(df.head())
# print(df....)
# df....
# print(df.isna().sum())
```

Then determine:

1. The number of rows.
2. The number of columns.
3. The data type of each column.
4. The number of missing values in each column.

---

## 3.9. Reading Large Datasets with `chunksize`

When a CSV file is larger than the available memory, loading the entire dataset into a single DataFrame may not be feasible.

The `chunksize` argument allows data to be processed incrementally.

```python
chunks = pd.read_csv(
    "transactions.csv",
    chunksize=100000
)
```

Each chunk can then be processed separately:

```python
for chunk in chunks:
    print(chunk.shape)
```

For example, total revenue can be calculated without loading the entire file into RAM:

```python
total = 0

for chunk in pd.read_csv(
    "transactions.csv",
    chunksize=100000
):
    total += chunk["Amount"].sum()

print(total)
```

### Exercise — `chunksize`

Complete the following program to calculate the total value of the `Sales` column in `large_sales.csv`, reading the data in chunks of 50,000 rows.

```python
# total_sales = 0

# for chunk in pd.read_csv(
#     "large_sales.csv",
#     chunksize=...
# ):
#     total_sales += ...

# print(total_sales)
```

---

## 3.10. Writing a DataFrame to CSV

Use the `to_csv()` method:

```python
df.to_csv(
    "clean_data.csv",
    index=False,
    encoding="utf-8-sig"
)
```

The argument `index=False` prevents the DataFrame index from being written as an additional column.

---

## 3.11. Main Functions and Arguments

| Function or Argument | Purpose |
|---|---|
| `pd.read_csv()` | Read CSV or other delimited text files |
| `usecols=` | Read only selected columns |
| `dtype=` | Specify data types |
| `parse_dates=` | Convert columns to datetime |
| `na_values=` | Define missing-value symbols |
| `chunksize=` | Read data incrementally |
| `df.to_csv()` | Write a DataFrame to CSV |

### Knowledge Check

**Question 1.** Which argument allows only selected columns to be read?

A. `usecols`  
B. `keepcols`  
C. `columns_only`  
D. `filter_columns`

**Question 2.** Which argument is especially useful for processing very large CSV files?

A. `chunksize`  
B. `batch=True`  
C. `split=True`  
D. `large=True`

**Question 3.** Why should an ID column often be read as `str`?

A. Because it represents an identifier rather than a numerical measurement.  
B. To calculate its mean.  
C. To make it continuous.  
D. To increase its value.

### Practical Exercise 3

Create a file named `customers.csv` containing:

- CustomerID;
- Name;
- City;
- Age;
- SignupDate;
- TotalSpent.

Include:

- several `NA` values;
- several `-` values;
- CustomerID values such as `001`, `002`, and so on.

Complete the following tasks:

1. Read `CustomerID` as `str`.
2. Parse `SignupDate` as datetime during import.
3. Treat `NA` and `-` as missing values.
4. Read only five columns required for analysis.
5. Inspect the dataset using `head()`, `shape`, `info()`, and `isna().sum()`.
6. Export the result to `customers_clean.csv`.

---

# Part 4. Working with Microsoft Excel

## 4.1. Reading a Worksheet

Pandas uses `pd.read_excel()` to read Excel data.

```python
df = pd.read_excel(
    "products.xlsx",
    sheet_name="Products",
    engine="openpyxl"
)
```

The `sheet_name` argument specifies the worksheet to be read.

### Exercise — `read_excel()`

Read the `Inventory` worksheet from `warehouse.xlsx` into a DataFrame named `inventory`.

---

## 4.2. Reading All Worksheets

An entire workbook can be read using:

```python
workbook = pd.read_excel(
    "products.xlsx",
    sheet_name=None
)

print(workbook.keys())
```

The result is a dictionary where:

- each key is a worksheet name;
- each value is the corresponding DataFrame.

For example:

```python
products = workbook["Products"]
```

### Exercise

Read all worksheets from `business.xlsx`.

Then:

1. Print the worksheet names.
2. Print the number of rows and columns of each corresponding DataFrame.

---

## 4.3. Writing Multiple DataFrames to One Workbook

`pd.ExcelWriter()` can be used to write multiple DataFrames to different worksheets within the same Excel file.

```python
with pd.ExcelWriter(
    "report.xlsx",
    engine="openpyxl"
) as writer:

    df_products.to_excel(
        writer,
        sheet_name="Products",
        index=False
    )

    df_sales.to_excel(
        writer,
        sheet_name="Sales",
        index=False
    )
```

### Exercise — `ExcelWriter`

Export the DataFrames `customers` and `orders` to:

```text
business_report.xlsx
```

with each DataFrame stored in a separate worksheet.

---

## 4.4. Main Functions

| Function or Argument | Purpose |
|---|---|
| `pd.read_excel()` | Read Excel data |
| `sheet_name=` | Select a worksheet |
| `sheet_name=None` | Read all worksheets |
| `df.to_excel()` | Write a DataFrame to Excel |
| `pd.ExcelWriter()` | Write multiple DataFrames to one workbook |

### Knowledge Check

**Question 1.** What does `pd.read_excel()` return when `sheet_name=None` is used?

A. A dictionary of DataFrames  
B. Only the first worksheet  
C. A NumPy array  
D. A string

**Question 2.** Which object is suitable for writing multiple DataFrames to multiple worksheets in the same workbook?

A. `pd.ExcelWriter`  
B. `pd.ExcelReaderOnly`  
C. `pd.MultiSheet`  
D. `open_csv`

### Practical Exercise 4

Create:

```text
business_data.xlsx
```

with three worksheets:

- Customers;
- Products;
- Sales.

Then:

1. Read the entire workbook.
2. Print all worksheet names.
3. Determine the number of rows and columns in each worksheet.
4. Calculate total `Sales`.
5. Export a new workbook containing:
   - `Sales_Detail`;
   - `Sales_Summary`.

---

# Part 5. Working with JSON

## 5.1. What Is JSON?

JSON (*JavaScript Object Notation*) is a widely used data format in:

- Web APIs;
- e-commerce systems;
- microservices;
- NoSQL databases.

Example:

```json
[
    {
        "customer_id": "C001",
        "city": "Hanoi"
    },
    {
        "customer_id": "C002",
        "city": "Danang"
    }
]
```

---

## 5.2. Reading Tabular JSON Data

For relatively flat JSON structures, use:

```python
df = pd.read_json(
    "customers.json"
)
```

### Exercise — `pd.read_json()`

Read `products.json` into a DataFrame named `products` and display the first five rows.

---

## 5.3. Nested JSON

Real-world JSON data often contains multiple levels of nesting.

Example:

```python
{
    "order_id": "O001",

    "customer": {
        "customer_id": "C001",
        "city": "Hanoi"
    },

    "items": [
        {
            "sku": "P001",
            "qty": 2
        },
        {
            "sku": "P002",
            "qty": 1
        }
    ]
}
```

For analysis in Pandas, the structure can be converted into a table:

| order_id | customer_id | city | sku | qty |
|---|---|---|---|---:|
| O001 | C001 | Hanoi | P001 | 2 |
| O001 | C001 | Hanoi | P002 | 1 |

---

## 5.4. Flattening Data with `pd.json_normalize()`

```python
df_items = pd.json_normalize(
    orders,
    record_path=["items"],
    meta=[
        "order_id",
        ["customer", "customer_id"],
        ["customer", "city"]
    ]
)
```

In this example:

- `record_path` specifies the nested list to expand into rows;
- `meta` specifies parent-level attributes to retain.

### Exercise — `pd.json_normalize()`

Given:

```python
orders = [
    {
        "OrderID": "O01",
        "Customer": {
            "ID": "C01",
            "City": "Hanoi"
        },
        "Items": [
            {"Product": "A", "Qty": 2},
            {"Product": "B", "Qty": 1}
        ]
    }
]
```

Use `pd.json_normalize()` to create a DataFrame containing two rows, with each row representing one item in the order.

### Knowledge Check

**Question 1.** Which function can directly read relatively flat JSON data?

A. `pd.read_json()`  
B. `pd.read_csv()`  
C. `pd.read_html()`  
D. `pd.read_pdf()`

**Question 2.** What is the purpose of `record_path` in `pd.json_normalize()`?

A. To identify the nested list to expand into rows  
B. To rename columns  
C. To write data to JSON  
D. To remove missing values

### Practical Exercise 5

Create JSON data representing three orders.

Each order should contain:

- OrderID;
- OrderDate;
- Customer;
- Items.

The `Customer` object should contain:

- CustomerID;
- City.

Each item in `Items` should contain:

- ProductID;
- Quantity;
- UnitPrice.

Complete the following tasks:

1. Read the JSON data.
2. Convert each item into a separate DataFrame row.
3. Retain `OrderID`, `OrderDate`, `CustomerID`, and `City`.
4. Create:

```text
Revenue = Quantity × UnitPrice
```

5. Calculate total Revenue by City.

---

# Part 6. Accessing Data from HTML and PDF

## 6.1. Reading HTML Tables

`pd.read_html()` can detect HTML `<table>` elements and convert them into DataFrames.

```python
tables = pd.read_html(
    "financial_quotes.html"
)

print(
    len(tables)
)
```

The result is a list of DataFrames.

For example, the first table can be accessed using:

```python
stocks = tables[0]
```

### Exercise — `pd.read_html()`

Read `market_data.html`.

Then:

1. Determine the number of tables in the file.
2. Display the first table.
3. Inspect the number of rows and columns.

---

## 6.2. Why Is PDF Extraction More Difficult Than CSV Import?

CSV is designed to represent tabular data.

In contrast, PDF is primarily designed to:

- display content;
- preserve layout;
- support printing.

Therefore, the process:

```text
CSV → DataFrame
```

is usually more direct than:

```text
PDF → DataFrame
```

In PDF files, rows and columns that appear visually may not be stored internally as explicit table structures.

---

## 6.3. Extracting Tables with `pdfplumber`

One library that can be used to extract tables from PDF documents is `pdfplumber`.

```python
import pdfplumber

with pdfplumber.open(
    "report.pdf"
) as pdf:

    page = pdf.pages[0]

    tables = page.extract_tables()
```

An extracted table can then be converted to a DataFrame:

```python
table = tables[0]

df = pd.DataFrame(
    table[1:],
    columns=table[0]
)
```

Extracted data should always be inspected carefully before further analysis.

### Exercise

After converting a PDF table into a DataFrame named `df`, use appropriate commands to inspect:

```python
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna().sum())
```

Determine whether:

1. the column headers are correct;
2. the number of rows and columns is reasonable;
3. missing values are present.

### Knowledge Check

**Question 1.** Which Pandas function can read HTML `<table>` elements?

A. `pd.read_html()`  
B. `pd.read_web()`  
C. `pd.read_table_html_only()`  
D. `pd.scrape()`

**Question 2.** Why is extracting data from PDF usually more difficult than importing CSV data?

A. Because PDF is designed primarily for visual presentation rather than structured analytical storage.  
B. Because PDF contains only numbers.  
C. Because PDF cannot contain tables.  
D. Because Python cannot open PDF files.

### Practical Exercise 6

Given an HTML file containing:

- a product-price table;
- a foreign-exchange table.

Complete the following tasks:

1. Read both tables into Pandas.
2. Inspect the structure of each table.
3. Save each table to a separate worksheet in the same Excel workbook.

For a table extracted from a PDF:

1. Convert the table to a DataFrame.
2. Inspect the column headers.
3. Inspect missing values.
4. Identify the cleaning operations required before analysis.

---

# Part 7. Working with SQLite Databases

## 7.1. What Is SQLite?

SQLite is a lightweight relational database management system. An entire database can be stored in a single file such as:

```text
company.db
```

Python provides the `sqlite3` module as part of the standard library:

```python
import sqlite3
```

---

## 7.2. Connecting to a Database

Create a database connection:

```python
conn = sqlite3.connect(
    "company.db"
)

cursor = conn.cursor()
```

The `conn` object represents the database connection, while the `cursor` is used to execute SQL statements.

### Exercise

Complete the code below to connect to `sales.db` and create a cursor:

```python
# conn = sqlite3.connect(...)
# cursor = ...
```

---

## 7.3. Executing SQL Queries

The following example retrieves employees whose salary is at least 30 million:

```python
cursor.execute(
    """
    SELECT emp_id, full_name, salary
    FROM employees
    WHERE salary >= ?
    """,
    (30000000,)
)

rows = cursor.fetchall()
```

`fetchall()` returns all rows that satisfy the query.

### Exercise

Write an SQL query that retrieves employees who belong to the `Sales` department.

---

## 7.4. Parameterized Queries

When query values come from Python variables or user input, parameterized queries should be used.

```python
cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)
```

This approach separates the SQL query structure from the values supplied to the query and helps reduce security risks associated with direct string concatenation.

### Exercise

Write a parameterized query that retrieves orders satisfying:

```text
Amount >= target_amount
```

where `target_amount` is a Python variable.

---

## 7.5. Reading SQL Results into Pandas

Pandas can directly read the result of an SQL query:

```python
query = """
SELECT
    emp_id,
    full_name,
    salary
FROM employees
"""

df = pd.read_sql_query(
    query,
    conn
)
```

The result is returned as a DataFrame.

### Exercise

Read the following fields from the `orders` table into a DataFrame:

```text
OrderID
CustomerID
Amount
```

---

## 7.6. Combining Tables with JOIN

Example:

```sql
SELECT
    e.emp_id,
    e.full_name,
    d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;
```

The result can then be read directly into Pandas:

```python
df = pd.read_sql_query(
    query,
    conn
)
```

---

## 7.7. Writing a DataFrame to SQLite

Pandas provides the `to_sql()` method:

```python
df.to_sql(
    name="sales_summary",
    con=conn,
    if_exists="replace",
    index=False
)
```

Common values of `if_exists` include:

- `fail`: raise an error if the table already exists;
- `replace`: replace the existing table;
- `append`: add rows to the existing table.

### Exercise — `to_sql()`

Save the DataFrame `summary` to the SQLite table:

```text
monthly_summary
```

and replace the existing table if it already exists.

---

## 7.8. Main Functions

| Function | Purpose |
|---|---|
| `sqlite3.connect()` | Open a connection to SQLite |
| `cursor.execute()` | Execute an SQL statement |
| `fetchall()` | Retrieve all query results |
| `pd.read_sql_query()` | Convert SQL query results to a DataFrame |
| `df.to_sql()` | Write a DataFrame to an SQL table |

### Knowledge Check

**Question 1.** Which Python standard-library module supports SQLite?

A. `sqlite3`  
B. `sqlpandas`  
C. `sqlitepro`  
D. `pysqlserver`

**Question 2.** Which function converts SQL query results directly into a DataFrame?

A. `pd.read_sql_query()`  
B. `pd.sql_to_df()`  
C. `pd.read_db_table_only()`  
D. `pd.load_database()`

**Question 3.** What is an important advantage of parameterized queries?

A. They separate SQL structure from parameter values and help reduce SQL injection risk.  
B. They always make every query faster.  
C. They eliminate the need for database tables.  
D. They automatically convert SQL to JSON.

### Practical Exercise 7

Create the database:

```text
sales.db
```

with two tables:

```text
customers(CustomerID, Name, City)

orders(OrderID, CustomerID, Amount)
```

Complete the following tasks:

1. Query all orders.
2. Combine `orders` and `customers` using a `JOIN`.
3. Filter customers located in Hanoi.
4. Load the result into a Pandas DataFrame.
5. Calculate total `Amount` by `City`.
6. Store the summary in:

```text
city_sales_summary
```

---

# Part 8. Working with MongoDB and PyMongo

## 8.1. What Is MongoDB?

MongoDB is a document-oriented NoSQL database management system.

In a relational database, data is commonly organized as:

```text
Table
 └── Row
```

In MongoDB, data is organized as:

```text
Collection
 └── Document
```

---

## 8.2. Document Structure

Example of an order document:

```python
{
    "order_id": "ORD001",

    "customer": {
        "name": "An",
        "city": "Hanoi"
    },

    "items": [
        {
            "product": "Laptop",
            "qty": 1
        }
    ]
}
```

A document can contain:

- scalar values;
- nested objects;
- lists;
- multiple levels of hierarchy.

---

## 8.3. Connecting to MongoDB

PyMongo provides the `MongoClient` class for connecting to MongoDB.

```python
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["retail_db"]

orders = db["orders"]
```

---

## 8.4. CRUD Operations

CRUD refers to four basic operations:

```text
Create
Read
Update
Delete
```

### Creating Data

```python
orders.insert_one(
    sample_order
)
```

### Reading One Document

```python
orders.find_one({
    "order_id": "ORD001"
})
```

### Filtering Multiple Documents

```python
orders.find({
    "total_amount": {
        "$gte": 1000000
    }
})
```

### Updating a Document

```python
orders.update_one(
    {"order_id": "ORD001"},
    {
        "$set": {
            "status": "REFUNDED"
        }
    }
)
```

### Deleting Documents

```python
orders.delete_many({
    "status": "CANCELLED"
})
```

### Exercise — CRUD

Write PyMongo commands to:

1. Insert a new order.
2. Find all orders with `status="PAID"`.
3. Update one order to `status="SHIPPED"`.

---

## 8.5. Converting MongoDB Data to Pandas

Query results can first be converted into a list of documents:

```python
documents = list(
    orders.find()
)
```

The documents can then be flattened using:

```python
df = pd.json_normalize(
    documents
)
```

MongoDB's `_id` field usually has the `ObjectId` type. When exporting to CSV or Excel, it can be converted to a string:

```python
df["_id"] = (
    df["_id"]
    .astype(str)
)
```

### Exercise

Retrieve all orders with status `PAID` from MongoDB and convert the results into a Pandas DataFrame.

### Knowledge Check

**Question 1.** MongoDB stores records as:

A. Documents  
B. Excel worksheets  
C. NumPy matrices  
D. CSV rows only

**Question 2.** Which method is used to retrieve multiple documents?

A. `find()`  
B. `find_one_only_all()`  
C. `select()`  
D. `read_many()`

**Question 3.** Which Pandas function is useful when converting nested MongoDB documents into tabular form?

A. `pd.json_normalize()`  
B. `pd.read_csv()`  
C. `pd.crosstab()`  
D. `pd.cut()`

### Practical Exercise 8

Create a collection named `customer_orders` containing at least five documents.

Each document should contain:

- OrderID;
- Customer;
- Items;
- TotalAmount;
- Status.

Complete the following tasks:

1. Insert the documents into the collection.
2. Find orders with `TotalAmount >= 1_000_000`.
3. Find orders with `Status="PAID"`.
4. Update the status of one order.
5. Convert the query results into a Pandas DataFrame.
6. Calculate the total revenue of all `PAID` orders.

---

# Part 9. Building a Multi-Source Data Pipeline

## 9.1. Scenario

A company stores data in multiple sources:

```text
customers.csv
products.xlsx
orders.json
company.db
```

The objective is to integrate these sources into a unified dataset for analysis.

---

## 9.2. Integration Workflow

A general data pipeline can be represented as follows:

```text
CSV ───────┐
           │
Excel ─────┤
           ↓
JSON ──→ Data Ingestion
           ↓
SQL ───────┘
      Data Cleaning
           ↓
      Transformation
           ↓
        Merge
           ↓
   Analytics Dataset
      ↙          ↘
   SQLite       Excel
```

---

## 9.3. Reading Data from Multiple Sources

Read customer data from CSV:

```python
customers = pd.read_csv(
    "customers.csv"
)
```

Read product data from Excel:

```python
products = pd.read_excel(
    "products.xlsx",
    sheet_name="Products"
)
```

Read order data from JSON:

```python
import json

with open(
    "orders.json",
    "r",
    encoding="utf-8"
) as f:
    orders = json.load(f)
```

---

## 9.4. Flattening JSON Data

```python
items = pd.json_normalize(
    orders,
    record_path=["items"],
    meta=[
        "order_id",
        ["customer", "customer_id"]
    ]
)
```

Each item in an order becomes a separate row.

---

## 9.5. Creating Analytical Variables

For example, calculate revenue for each order line:

```python
items["Revenue"] = (
    items["Quantity"]
    * items["Price"]
)
```

---

## 9.6. Integrating Data with `merge()`

Merge product information:

```python
df = items.merge(
    products,
    on="ProductID",
    how="left"
)
```

Merge customer information:

```python
df = df.merge(
    customers,
    on="CustomerID",
    how="left"
)
```

### Exercise

After each `merge()`, use:

```python
# print(df.shape)
# print(df.isna().sum())
```

Then:

1. Compare the DataFrame dimensions before and after merging.
2. Inspect newly created missing values.
3. Explain why a `left join` may produce missing values in columns obtained from the right-hand DataFrame.

---

## 9.7. Creating KPI Summaries

For example, calculate revenue and number of orders by region:

```python
region_summary = (
    df
    .groupby("Region")
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("OrderID", "nunique")
    )
    .reset_index()
)
```

---

## 9.8. Storing Analytical Data in SQLite

```python
conn = sqlite3.connect(
    "analytics.db"
)

df.to_sql(
    "order_analytics",
    conn,
    if_exists="replace",
    index=False
)

conn.close()
```

---

## 9.9. Exporting a Multi-Sheet Excel Report

```python
with pd.ExcelWriter(
    "dashboard.xlsx"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Details",
        index=False
    )

    region_summary.to_excel(
        writer,
        sheet_name="Region_KPI",
        index=False
    )
```

### Knowledge Check

**Question 1.** Which step should normally be completed before integrating multiple sources with `merge()`?

A. Reading and inspecting each data source  
B. Model deployment  
C. Neural-network training  
D. Feature-importance analysis

**Question 2.** Why should missing values be inspected after a `merge()` operation?

A. Because some keys may not have a matching record in the other data source.  
B. Because `merge()` always deletes some rows.  
C. Because Pandas always inserts empty columns.  
D. Because `merge()` converts all numerical values to strings.

### Practical Exercise 9 — Multi-Source Data Integration Project

Use:

```text
customers.csv
products.xlsx
orders.json
```

to build a DataFrame named:

```text
order_analytics
```

containing:

- OrderID;
- CustomerID;
- CustomerName;
- City;
- ProductID;
- Category;
- Quantity;
- UnitPrice;
- Revenue.

Complete the following tasks:

1. Read each data source.
2. Inspect structure and data types.
3. Flatten the order data stored in JSON.
4. Integrate the datasets using `merge()`.
5. Identify unmatched records.
6. Calculate Revenue.
7. Calculate:
   - total Revenue;
   - Revenue by Category;
   - Revenue by City;
   - number of orders by City.
8. Store the detailed dataset in SQLite.
9. Export KPI summaries to a multi-sheet Excel workbook.

---

# Part 10. Best Practices

## 10.1. Read Only the Required Columns

If a file contains many columns but only a subset is required for analysis, select those columns during import.

```python
pd.read_csv(
    "large.csv",
    usecols=[
        "CustomerID",
        "Sales"
    ]
)
```

This can reduce both loading time and memory consumption.

### Exercise

A CSV file contains 100 columns, but the analysis requires only:

```text
Date
StoreID
ProductID
Sales
```

Write a `pd.read_csv()` command that imports only these four columns.

---

## 10.2. Inspect Data Immediately After Import

A basic inspection workflow can include:

```python
df.head()
df.shape
df.info()
df.isna().sum()
```

These commands help detect structural, data-type, and missing-value problems early.

### Exercise

Write a Python code block using at least four Pandas commands to inspect a DataFrame immediately after it is loaded from a file.

---

## 10.3. Inspect Data After Integration

After a `merge()`, inspect the resulting data again:

```python
df.isna().sum()
```

New missing values may appear when keys from two data sources do not match.

---

## 10.4. Control Data Types

Inspect data types using:

```python
df.dtypes
```

Do not assume that every field containing digits represents a numerical quantity. For example, `CustomerID = "001"` is an identifier and should often be stored as a string.

---

## 10.5. Process Large Files Incrementally

For large CSV files, use:

```python
pd.read_csv(
    "large.csv",
    chunksize=100000
)
```

This allows the dataset to be processed sequentially without loading the entire file into RAM.

---

## 10.6. Use Context Managers

When working with files, use the `with` statement:

```python
with open(
    "data.json",
    encoding="utf-8"
) as f:
    ...
```

Similarly, when creating Excel reports:

```python
with pd.ExcelWriter(
    "report.xlsx"
) as writer:
    ...
```

This ensures that resources are properly closed after the operation is completed.

---

## 10.7. Use Parameterized SQL Queries

Do not directly concatenate external values into SQL statements.

Instead, use parameterized queries so that data values remain separate from the SQL query structure.

---

## 10.8. Select an Appropriate Storage Format

There is no single storage format that is best for every situation.

| Requirement | Suitable Format |
|---|---|
| Exchange simple tabular data | CSV |
| Create multi-sheet management reports | Excel |
| Exchange data through Web APIs | JSON |
| Store relational data and perform queries | SQL |
| Store flexible nested documents | MongoDB |
| Store large tabular datasets efficiently for reuse | Parquet |
| Extract tables published on websites | HTML |
| Distribute fixed-layout reports | PDF |

### Knowledge Check

**Question 1.** Which technique is appropriate when a CSV file is larger than the available RAM?

A. Reading the file in chunks  
B. Converting all values to strings  
C. Creating a second copy of the file  
D. Using only `head()`

**Question 2.** Why should ID fields often be stored as strings?

A. Because their digits usually represent labels or identifiers rather than quantities.  
B. Because strings use no memory.  
C. Because numerical values cannot be used for IDs.  
D. Because Pandas requires every ID to be a string.

**Question 3.** Which format is especially common for exchanging data through Web APIs?

A. JSON  
B. PDF  
C. XLS  
D. SQLite

### Practical Exercise 10 — Selecting a Storage Solution

For each of the following situations, choose an appropriate storage format and explain your reasoning:

1. Sending a simple tabular dataset to a colleague.
2. Creating a management report with multiple worksheets.
3. Exchanging data between a Web API and an application.
4. Storing transactional data that must support SQL queries.
5. Storing data with multiple nested fields and objects.
6. Storing a large tabular dataset for efficient reuse in later analytical tasks.

---

# Summary

A general workflow for working with data from multiple sources can be represented as follows:

```text
Source
   ↓
Read
   ↓
Inspect
   ↓
Clean
   ↓
Transform
   ↓
Integrate
   ↓
Analyze
   ↓
Store / Report
```

The main tools introduced in this lesson are:

| Data Source | Python Tools |
|---|---|
| CSV | `pd.read_csv()`, `to_csv()` |
| Numerical text files with NumPy | `loadtxt()`, `genfromtxt()`, `savetxt()` |
| Excel | `read_excel()`, `ExcelWriter()` |
| JSON | `read_json()`, `json_normalize()` |
| HTML | `read_html()` |
| PDF | `pdfplumber` |
| SQLite | `sqlite3`, `read_sql_query()`, `to_sql()` |
| MongoDB | `pymongo`, `json_normalize()` |

Data access, preparation, and storage skills provide the foundation for the broader Data Science workflow:

```text
Data Acquisition
      ↓
Data Preparation
      ↓
Exploratory Analysis
      ↓
Visualization
      ↓
Machine Learning
      ↓
Deployment
```

An analytical or Machine Learning model can only perform effectively when its input data is accessed correctly, inspected carefully, transformed consistently, and stored in a format appropriate for the intended use.