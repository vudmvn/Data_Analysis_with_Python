# Giới thiệu Pandas
**Ngôn ngữ:** Tiếng Việt  
**Chủ đề:** Thao tác, làm sạch, phân tích và xử lý dữ liệu dạng bảng với Pandas

---

## 1. Giới thiệu bài học
**Pandas** is an open-source Python library designed for **data manipulation and analysis**. It is built on top of NumPy and provides high-level data structures and functions for working efficiently with structured and tabular data.

Pandas đặc biệt hữu ích cho các công việc như:

- đọc dữ liệu từ file CSV, Excel, JSON và văn bản;
- làm sạch và chuẩn bị tập dữ liệu;
- lọc và lựa chọn các quan sát;
- xử lý giá trị thiếu;
- biến đổi cột và kiểu dữ liệu;
- nhóm và tổng hợp dữ liệu;
- merge và join nhiều tập dữ liệu;
- reshape dữ liệu;
- tính thống kê mô tả;
- phân tích dữ liệu chuỗi thời gian;
- tạo trực quan hóa nhanh.

Pandas xoay quanh hai cấu trúc dữ liệu chính:

- **Series**: a one-dimensional labeled array;
- **DataFrame**: a two-dimensional labeled tabular structure.

Về mặt khái niệm, DataFrame tương tự một bảng tính Excel hoặc một bảng trong cơ sở dữ liệu, với các hàng và cột có thể có nhãn.

---

## 2. Mục tiêu học tập
Sau khi hoàn thành bài học này, người học có thể:

- Giải thích vai trò của Pandas trong Khoa học dữ liệu và phân tích dữ liệu.
- Phân biệt Pandas Series và DataFrame.
- Tạo Series và DataFrame từ các đối tượng Python và mảng NumPy.
- Kiểm tra DataFrame bằng các thuộc tính và phương thức thông dụng.
- Truy xuất hàng, cột và tập con theo nhãn và vị trí.
- Lọc dữ liệu bằng một hoặc nhiều điều kiện.
- Đọc và ghi dữ liệu CSV, Excel, JSON và văn bản.
- Xác định và xử lý giá trị thiếu.
- Loại bỏ bản ghi trùng lặp.
- Chuyển đổi kiểu dữ liệu.
- Xử lý các cột chuỗi.
- Sắp xếp và reshape DataFrame.
- Merge, join và concatenate các tập dữ liệu.
- Nhóm và tổng hợp dữ liệu.
- Tạo pivot table.
- Thực hiện phân tích thống kê mô tả.
- Tính tương quan.
- Làm việc với dữ liệu chuỗi thời gian cơ bản.
- Tạo trực quan hóa nhanh bằng các hàm vẽ của Pandas.

---

## 3. Cấu trúc bài học
Bài học được tổ chức theo các phần chính sau:

1. Basics
2. DataFrame
3. Series
4. Data Input and Output (I/O)
5. Data Cleaning
6. Operations
7. Advanced Operations
8. Review Câus
9. Practical Exercises
10. Answers and Suggested Responses

---

## 4. Điều kiện tiên quyết
Người học nên có:

- Basic Python knowledge.
- Familiarity with variables, lists, dictionaries, loops, and functions.
- Basic understanding of NumPy arrays.
- Access to Jupyter Notebook, JupyterLab, Google Colab, VS Code, or a similar environment.

---

# Phần 1. Kiến thức cơ bản
## 1.1. Pandas là gì?
Pandas là thư viện Python dùng để làm việc với dữ liệu có cấu trúc. Nó cung cấp các công cụ để làm sạch, biến đổi, phân tích dữ liệu và tích hợp với các thư viện Khoa học dữ liệu khác.

Pandas được xây dựng trên NumPy, nghĩa là nó có thể tận dụng hiệu quả của mảng số trong khi bổ sung nhãn, chỉ mục và các thao tác hướng bảng.

Tên **Pandas** được bắt nguồn từ thuật ngữ **panel data**, thường được sử dụng trong kinh tế lượng.

## 1.2. Vì sao Pandas hữu ích?
Pandas thường được sử dụng để:

- reading and writing data;
- cleaning datasets;
- xử lý giá trị thiếu;
- selecting and filtering observations;
- transforming variables;
- merging datasets;
- grouping observations;
- calculating summary statistics;
- preparing data for visualization and machine learning.

## 1.3. Cài đặt và import
Cài đặt Pandas bằng:

```bash
pip install pandas
```

Import Pandas với bí danh chuẩn:

```python
import pandas as pd
```

Kiểm tra phiên bản đã cài:

```python
import pandas as pd

print(pd.__version__)
```

### Bài tập ngắn — `pd.__version__`

Hoàn thiện lệnh để in phiên bản Pandas đã cài đặt.

```python
# version = ...
# print(version)
```

**Gợi ý:** sử dụng `pd.__version__`.

## 1.4. Những điểm quan trọng
- **DataFrame** là cấu trúc hai chiều có nhãn, gồm hàng và cột.
- **Series** là mảng một chiều có nhãn.
- Pandas hoạt động chặt chẽ với NumPy, Matplotlib và Scikit-learn.
- Có thể xử lý giá trị thiếu bằng các phương thức như `.dropna()` và `.fillna()`.

## 1.5. Kiểm tra nhanh
**Câu 1.** Which alias is conventionally used for Pandas?

A. `pn`  
B. `pd`  
C. `ps`  
D. `pa`

**Câu 2.** Which Pandas structure is two-dimensional?

A. `Series`  
B. `tuple`  
C. `DataFrame`  
D. `ndarray`

## Bài tập
### Bài tập 1.1. Check Your Environment
Run:

```python
import pandas as pd

print(pd.__version__)
```

Record:

1. the Pandas version;
2. the standard Pandas alias;
3. one reason Pandas is useful in data analysis.

### Bài tập 1.2. Series or DataFrame?
Decide whether each case is more naturally represented by a Series or DataFrame:

1. a list of monthly sales values;
2. a student table containing ID, name, age, and GPA;
3. one column of product prices;
4. a dataset containing 1,000 customers and 12 attributes.

---

# Phần 2. DataFrame
## 2.1. DataFrame là gì?
**DataFrame** là cấu trúc dữ liệu dạng bảng hai chiều, có thể thay đổi kích thước, có thể chứa nhiều kiểu dữ liệu khác nhau và có nhãn cho hàng và cột.

Các cột khác nhau trong DataFrame có thể chứa các kiểu dữ liệu khác nhau.

Ví dụ:

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

### Bài tập ngắn — `pd.DataFrame()`

Tạo DataFrame tên `products` với các cột `Product`, `Price` và `Stock`.

```python
# products = pd.DataFrame({
#     "Product": [...],
#     "Price": [...],
#     "Stock": [...]
# })

# print(products)
```

**Gợi ý:** tất cả các cột phải có cùng số lượng giá trị.

## 2.2. Các lệnh chính để tạo và kiểm tra DataFrame
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

## 2.3. Kiểm tra DataFrame
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

### Bài tập ngắn — `head()`, `shape`, `columns`, `dtypes`, `info()`

Hoàn thiện các lệnh kiểm tra dữ liệu.

```python
# print(df.head(...))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# df.info()
```

Sau đó cho biết số hàng và số cột.

to inspect:

- number of rows;
- number of columns;
- column names;
- missing values;
- data types.

## 2.4. Chỉ mục của DataFrame
Pandas tự gán chỉ mục số nguyên mặc định nếu không cung cấp index.

```python
print(df.index)
```

### Bài tập ngắn — `index`

Kiểm tra index của DataFrame.

```python
# current_index = ...
# print(current_index)
```

Cho biết đây là index số nguyên mặc định hay index tùy chỉnh.

Có thể chỉ định index tùy chỉnh:

```python
df = pd.DataFrame(
    data,
    index=["S01", "S02", "S03"]
)

print(df)
```

## 2.5. Truy xuất cột
Chọn một cột:

```python
print(df["Name"])
```

Chọn nhiều cột:

```python
print(df[["Name", "GPA"]])
```

### Bài tập ngắn — Chọn cột

Chọn:

1. chỉ cột `Age`;
2. cả `Name` và `Age`.

```python
# age = df[...]
# name_age = df[[..., ...]]

# print(age)
# print(name_age)
```

## 2.6. Truy xuất hàng bằng `loc` và `iloc`
`loc` chọn dữ liệu theo **nhãn**.

```python
print(df.loc["S01"])
```

`iloc` chọn dữ liệu theo **vị trí số nguyên**.

```python
print(df.iloc[0])
```

### Bài tập ngắn — `loc` và `iloc`

Hoàn thiện các lệnh chọn dữ liệu.

```python
# by_label = df.loc[...]
# by_position = df.iloc[...]

# print(by_label)
# print(by_position)
```

**Câu hỏi:** Lệnh nào sử dụng nhãn và lệnh nào sử dụng vị trí số nguyên?

Sự khác biệt này rất quan trọng:

- `loc` → label-based selection;
- `iloc` → position-based selection.

## 2.7. Slicing DataFrame
```python
print(df.iloc[0:2])
```

Chọn các hàng và cột cụ thể:

```python
print(df.loc[["S01", "S02"], ["Name", "GPA"]])
```

hoặc:

```python
print(df.iloc[0:2, [0, 2]])
```

### Bài tập ngắn — Slicing

Chọn:

1. hai hàng đầu tiên;
2. hai hàng đầu tiên và các cột `Name`, `GPA`.

```python
# first_two = df.iloc[...]
# subset = df.loc[..., [...]]

# print(first_two)
# print(subset)
```

## 2.8. Lọc DataFrame
Lọc các hàng:

```python
selected = df[df["GPA"] >= 3.4]

print(selected)
```

### Bài tập ngắn — Lọc Boolean

Lọc các hàng có `GPA >= 3.5`.

```python
# high_gpa = df[df["GPA"] >= ...]
# print(high_gpa)
```

## 2.9. Lọc với nhiều điều kiện
```python
selected = df[
    (df["Age"] >= 20) &
    (df["GPA"] >= 3.4)
]

print(selected)
```

### Bài tập ngắn — Nhiều điều kiện

Lọc sinh viên có `Age >= 20` và `GPA >= 3.5`.

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

Thông thường, mỗi điều kiện nên được đặt trong dấu ngoặc.

## 2.10. Sắp xếp DataFrame
Sắp xếp theo một cột:

```python
df_sorted = df.sort_values("GPA")
```

Thứ tự giảm dần:

```python
df_sorted = df.sort_values(
    "GPA",
    ascending=False
)
```

Sắp xếp theo nhiều cột:

```python
df_sorted = df.sort_values(
    ["Age", "GPA"],
    ascending=[True, False]
)
```

## 2.11. Merge, Join và Concatenate
Ghép nối các DataFrame:

```python
combined = pd.concat(
    [df1, df2],
    axis=0
)
```

Merge theo khóa:

```python
result = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="inner"
)
```

Các kiểu join phổ biến:

- `inner`;
- `left`;
- `right`;
- `outer`.

## 2.12. Pivot Table
Pivot table tóm tắt dữ liệu theo các nhóm phân loại.

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

### Bài tập ngắn — `pd.pivot_table()`

Tạo pivot table với Revenue trung bình theo Region và Product.

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

## 2.13. Kiểm tra nhanh
**Câu 1.** Which command creates a DataFrame?

A. `pd.DataFrame()`  
B. `pd.SeriesFrame()`  
C. `np.DataFrame()`  
D. `df.create()`

**Câu 2.** Which selector is label-based?

A. `iloc`  
B. `loc`  
C. `shape`  
D. `head`

## Bài tập
### Bài tập 2.1. Create a Dữ liệu sinh viênFrame
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

### Bài tập 2.2. `loc` and `iloc`
Using the student DataFrame:

1. select the first row using `iloc`;
2. set `StudentID` as the index;
3. select one student using `loc`;
4. select only `Name` and `GPA`.

### Bài tập 2.3. Filtering
Filter students who:

1. have GPA greater than or equal to 3.5;
2. are at least 20 years old;
3. satisfy both conditions.

### Bài tập 2.4. Sorting
Sort the students:

1. by GPA ascending;
2. by GPA descending;
3. by Age ascending and GPA descending.

### Bài tập 2.5. Merge
Create another DataFrame containing:

- `StudentID`;
- `Major`.

Merge it with the student DataFrame using `StudentID`.

---

# Phần 3. Series
## 3.1. Series là gì?
**Series** là mảng một chiều có nhãn, có thể chứa số nguyên, chuỗi, số thực, đối tượng Python và các kiểu dữ liệu khác.

Có thể xem Series như:

- one labeled column of a table;
- a mapping from index labels to values.

## 3.2. Tạo Series
```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

### Bài tập ngắn — `pd.Series()`

Tạo Series chứa `[12, 18, 25]` với các nhãn `["A", "B", "C"]`.

```python
# prices = pd.Series(
#     [...],
#     index=[...]
# )

# print(prices)
```

Tạo Series với nhãn tùy chỉnh:

```python
s = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

print(s)
```

## 3.3. Các lệnh chính cho Series
| Command | Meaning |
|---|---|
| `pd.Series(data)` | Create a Series. |
| `s.index` | Return the Series index. |
| `s.values` | Return underlying values. |
| `s.dtype` | Return the data type. |
| `s.loc[label]` | Access by label. |
| `s.iloc[position]` | Access by integer position. |

## 3.4. Truy xuất phần tử
```python
print(s.loc["A"])
print(s.iloc[0])
```

### Bài tập ngắn — Series `loc` và `iloc`

Truy xuất nhãn `"B"` và vị trí `2`.

```python
# value_by_label = s.loc[...]
# value_by_position = s.iloc[...]
```

## 3.5. Phép toán nhị phân trên Series
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

### Bài tập ngắn — Căn chỉnh Series

Dự đoán kết quả trước khi chạy:

```python
x = pd.Series([10, 20, 30], index=["A", "B", "C"])
y = pd.Series([1, 2, 3], index=["B", "C", "D"])

# result = x + y
# print(result)
```

Giải thích vì sao các nhãn không khớp tạo ra giá trị thiếu.

Pandas căn chỉnh Series theo nhãn index trước khi thực hiện phép toán.

## 3.6. Tạo Series từ mảng NumPy
```python
import numpy as np

arr = np.array([5, 10, 15])
s = pd.Series(arr)

print(s)
```

## 3.7. Kiểm tra nhanh
**Câu 1.** A Pandas Series is:

A. a two-dimensional table  
B. a one-dimensional labeled array  
C. a database server  
D. a plotting package

**Câu 2.** Which attribute returns Series labels?

A. `shape`  
B. `index`  
C. `columns`  
D. `describe`

## Bài tập
### Bài tập 3.1. Create a Series
Create a Series containing five product prices with custom product IDs as index labels.

Then print:

1. the Series;
2. its index;
3. its values;
4. its data type.

### Bài tập 3.2. Access Series Values
Using the Series from Exercise 3.1:

1. select one value using `loc`;
2. select one value using `iloc`;
3. explain the difference.

### Bài tập 3.3. Series Alignment
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

# Phần 4. Nhập và xuất dữ liệu (I/O)
## 4.1. Vì sao I/O quan trọng?
Dữ liệu thực tế hiếm khi bắt đầu trực tiếp bên trong chương trình Python. Pandas cung cấp các hàm để nhập dữ liệu từ file và xuất kết quả đã xử lý.

Các định dạng phổ biến gồm:

- CSV;
- Excel;
- JSON;
- text files;
- SQL databases.

## 4.2. Đọc file CSV
```python
df = pd.read_csv("data.csv")
```

Một số tùy chọn hữu ích:

```python
df = pd.read_csv(
    "data.csv",
    sep=",",
    header=0,
    encoding="utf-8"
)
```

## 4.3. Ghi file CSV
```python
df.to_csv(
    "output.csv",
    index=False
)
```

`index=False` ngăn index của DataFrame được ghi thành một cột bổ sung.

## 4.4. Đọc file Excel
```python
df = pd.read_excel(
    "data.xlsx",
    sheet_name="Sheet1"
)
```

## 4.5. Ghi file Excel
```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

## 4.6. Đọc file JSON
```python
df = pd.read_json("data.json")
```

### Bài tập ngắn — `pd.read_json()`

Đọc `customers.json` vào `customer_df`.

```python
# customer_df = pd.read_json(...)
```

## 4.7. Ghi file JSON
```python
df.to_json(
    "output.json",
    orient="records"
)
```

## 4.8. Đọc file văn bản
Các file văn bản có dấu phân cách có cấu trúc thường có thể được đọc bằng `read_csv()`:

```python
df = pd.read_csv(
    "data.txt",
    sep="\t"
)
```

## 4.9. Các lệnh I/O chính
| Command | Role |
|---|---|
| `pd.read_csv()` | Read CSV or delimited text files. |
| `df.to_csv()` | Write CSV files. |
| `pd.read_excel()` | Read Excel files. |
| `df.to_excel()` | Write Excel files. |
| `pd.read_json()` | Read JSON files. |
| `df.to_json()` | Write JSON files. |

## 4.10. Kiểm tra nhanh
**Câu 1.** Which function reads a CSV file?

A. `pd.read_csv()`  
B. `pd.open_csv()`  
C. `pd.load_table_only()`  
D. `df.csv_read()`

**Câu 2.** Which argument commonly prevents the DataFrame index from being exported?

A. `index=False`  
B. `index=True`  
C. `header=None`  
D. `drop_index=True`

## Bài tập
### Bài tập 4.1. CSV
Create a DataFrame with at least five rows and save it as:

```text
students.csv
```

Then read the file back into another DataFrame.

### Bài tập 4.2. Excel
Save the same DataFrame to:

```text
students.xlsx
```

with `index=False`.

### Bài tập 4.3. JSON
Export the DataFrame to JSON using:

```python
orient="records"
```

Then inspect the generated structure.

---

# Phần 5. Làm sạch dữ liệu
## 5.1. Vì sao làm sạch dữ liệu quan trọng?
Các tập dữ liệu thực tế có thể chứa:

- missing values;
- duplicate rows;
- inconsistent data types;
- empty columns;
- inconsistent text;
- mixed data formats.

Làm sạch dữ liệu nhằm cải thiện độ chính xác, tính nhất quán và khả năng sử dụng trước khi phân tích.

## 5.2. Phát hiện giá trị thiếu
```python
print(df.isna())
```

Đếm giá trị thiếu:

```python
print(df.isna().sum())
```

### Bài tập ngắn — `isna()` và `isna().sum()`

Đếm số giá trị thiếu theo từng cột và trong toàn bộ DataFrame.

```python
# missing_by_column = df.isna().____()
# total_missing = df.isna().____().____()
```

## 5.3. Loại bỏ giá trị thiếu
Loại bỏ các hàng chứa giá trị thiếu:

```python
clean_df = df.dropna()
```

Loại bỏ các cột chứa giá trị thiếu:

```python
clean_df = df.dropna(axis=1)
```

### Bài tập ngắn — `dropna()`

Tạo một DataFrame loại bỏ các hàng thiếu dữ liệu và một DataFrame khác loại bỏ các cột thiếu dữ liệu.

```python
# rows_complete = df.dropna()
# cols_complete = df.dropna(axis=...)
```

## 5.4. Điền giá trị thiếu
Điền tất cả giá trị thiếu:

```python
filled = df.fillna(0)
```

Điền một cột bằng giá trị trung bình:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

Điền giá trị cho biến phân loại:

```python
df["City"] = df["City"].fillna(
    "Unknown"
)
```

## 5.5. Loại bỏ dữ liệu trùng lặp
Phát hiện dữ liệu trùng lặp:

```python
print(df.duplicated())
```

Loại bỏ các hàng trùng:

```python
df = df.drop_duplicates()
```

### Bài tập ngắn — `duplicated()` and `drop_duplicates()`

```python
# duplicate_mask = df.duplicated()
# duplicate_count = duplicate_mask.____()
# clean_df = df.____()
```

## 5.6. Thay đổi kiểu dữ liệu
Kiểm tra kiểu dữ liệu:

```python
print(df.dtypes)
```

Chuyển đổi một cột:

```python
df["Age"] = df["Age"].astype(int)
```

### Bài tập ngắn — `astype()`

Chuyển `Quantity` sang kiểu số nguyên.

```python
# df["Quantity"] = df["Quantity"].astype(...)
```

Chuyển chuỗi sang giá trị số:

```python
df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)
```

## 5.7. Xóa hàng hoặc cột
```python
df = df.drop(
    columns=["UnusedColumn"]
)
```

Xóa hàng theo index:

```python
df = df.drop(
    index=[0, 2]
)
```

## 5.8. Xử lý chuỗi
Chuyển thành chữ thường:

```python
df["Name"] = df["Name"].str.lower()
```

Loại bỏ khoảng trắng đầu/cuối:

```python
df["Name"] = df["Name"].str.strip()
```

Thay thế văn bản:

```python
df["City"] = df["City"].str.replace(
    "HN",
    "Hanoi"
)
```

## 5.9. Phát hiện kiểu dữ liệu hỗn hợp
Kiểu dữ liệu hỗn hợp có thể gây vấn đề trong quá trình phân tích.

```python
df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
)
```

Các giá trị không hợp lệ được chuyển thành `NaN`, sau đó có thể xử lý rõ ràng.

## 5.10. Các lệnh làm sạch dữ liệu chính
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

## 5.11. Kiểm tra nhanh
**Câu 1.** Which method removes rows containing missing values?

A. `dropna()`  
B. `fillna()`  
C. `duplicated()`  
D. `astype()`

**Câu 2.** Which method removes duplicate rows?

A. `drop_duplicates()`  
B. `dropna()`  
C. `sort_values()`  
D. `merge()`

## Bài tập
### Bài tập 5.1. Missing Values
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

### Bài tập 5.2. Duplicates
Add a duplicated row to a DataFrame.

Then:

1. detect duplicates;
2. count duplicates;
3. remove them.

### Bài tập 5.3. Data Types
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

### Bài tập 5.4. String Cleaning
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

# Phần 6. Các thao tác
## 6.1. Xử lý và thao tác dữ liệu
Pandas hỗ trợ biến đổi và tính toán ở mức cột.

Tạo cột mới:

```python
df["Total"] = (
    df["Quantity"] * df["Price"]
)
```

Thay đổi cột hiện có:

```python
df["Price"] = df["Price"] * 1.1
```

### Bài tập ngắn — Calculated Column

Tạo `Revenue = Quantity × Price`.

```python
# df["Revenue"] = df["Quantity"] * df["Price"]
# total_revenue = df["Revenue"].____()
```

## 6.2. Áp dụng hàm
Dùng `map()` trên Series:

```python
df["Status"] = df["Score"].map(
    lambda x: "Pass" if x >= 5 else "Fail"
)
```

Dùng `apply()`:

```python
df["Squared"] = df["Value"].apply(
    lambda x: x ** 2
)
```

## 6.3. Chuẩn hóa
Chuẩn hóa min-max:

```python
df["Normalized"] = (
    (df["Value"] - df["Value"].min()) /
    (df["Value"].max() - df["Value"].min())
)
```

Chuẩn hóa Z-score:

```python
df["Z"] = (
    (df["Value"] - df["Value"].mean()) /
    df["Value"].std()
)
```

## 6.4. Phân tích mô tả
```python
print(df.describe())
```

Các thống kê riêng lẻ:

```python
print(df["Sales"].mean())
print(df["Sales"].median())
print(df["Sales"].min())
print(df["Sales"].max())
print(df["Sales"].std())
```

### Bài tập ngắn — Descriptive Statistics

```python
# sales_mean = df["Sales"].____()
# sales_median = df["Sales"].____()
# sales_min = df["Sales"].____()
# sales_max = df["Sales"].____()
# sales_std = df["Sales"].____()
```

## 6.5. Nhóm dữ liệu bằng `groupby()`
```python
summary = df.groupby(
    "Region"
)["Sales"].mean()

print(summary)
```

### Bài tập ngắn — `groupby()`

Tính tổng Sales theo Region.

```python
# region_total = (
#     df.groupby("Region")["Sales"].____()
# )
```

Nhiều phép tổng hợp:

```python
summary = df.groupby(
    "Region"
)["Sales"].agg(
    ["count", "sum", "mean"]
)

print(summary)
```

### Bài tập ngắn — `agg()`

Với mỗi Region, tính `count`, `sum`, `mean`, `min` và `max`.

```python
# region_stats = (
#     df.groupby("Region")["Sales"]
#     .agg([...])
# )
```

## 6.6. Nhóm theo nhiều cột
```python
summary = df.groupby(
    ["Region", "Product"]
)["Sales"].sum()
```

## 6.7. Join và Merge
```python
result = pd.merge(
    left,
    right,
    on="ID",
    how="left"
)
```

Các kiểu join phổ biến:

- inner;
- left;
- right;
- outer.

## 6.8. Reshape dữ liệu
Dùng `pivot()`:

```python
wide = df.pivot(
    index="Date",
    columns="Product",
    values="Sales"
)
```

Dùng `melt()`:

```python
long = pd.melt(
    wide.reset_index(),
    id_vars="Date"
)
```

## 6.9. Pivot Table
```python
table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)
```

## 6.10. Các thao tác chính
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

## 6.11. Kiểm tra nhanh
**Câu 1.** Which method groups observations by categories?

A. `groupby()`  
B. `dropna()`  
C. `astype()`  
D. `sort_index()`

**Câu 2.** Which function combines DataFrames using a key column?

A. `pd.merge()`  
B. `pd.mean()`  
C. `pd.reshape()`  
D. `pd.filter_rows()`

## Bài tập
### Bài tập 6.1. Create a Calculated Column
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

### Bài tập 6.2. Normalize Data
Create a numerical column and calculate:

1. min-max normalization;
2. z-score standardization.

### Bài tập 6.3. Group and Aggregate
Create a sales DataFrame containing:

- Region;
- Product;
- Sales.

Calculate:

1. total sales by Region;
2. mean sales by Region;
3. count, sum, and mean using `.agg()`.

### Bài tập 6.4. Merge
Create:

```text
customers(CustomerID, Name)
orders(OrderID, CustomerID, Amount)
```

Perform:

1. inner merge;
2. left merge.

Explain the difference.

### Bài tập 6.5. Pivot Table
Create a pivot table showing:

- rows: Region;
- columns: Product;
- values: Sales;
- aggregation: sum.

---

# Phần 7. Các thao tác nâng cao
## 7.1. Tương quan
Tương quan đo lường mức độ liên hệ giữa các biến số.

```python
print(df.corr(
    numeric_only=Đúng
))
```

Tương quan giữa các cột được chọn:

```python
print(
    df["Advertising"].corr(
        df["Sales"]
    )
)
```

Bản thân tương quan không hàm ý quan hệ nhân quả.

## 7.2. Trực quan hóa dữ liệu với Pandas
Pandas cung cấp các phương thức vẽ nhanh được xây dựng trên Matplotlib.

Biểu đồ đường:

```python
df.plot(
    x="Month",
    y="Sales",
    kind="line"
)
```

Biểu đồ cột:

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

Biểu đồ phân tán:

```python
df.plot(
    x="Advertising",
    y="Sales",
    kind="scatter"
)
```

## 7.3. Dữ liệu chuỗi thời gian
Chuyển một cột sang datetime:

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

Đặt Date làm index:

```python
df = df.set_index("Date")
```

Sắp xếp theo thời gian:

```python
df = df.sort_index()
```

### Bài tập ngắn — Datetime Pipeline

```python
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index(...)
# df = df.sort_index()
```

## 7.4. Trích xuất thành phần ngày tháng
```python
df["Year"] = df.index.year
df["Month"] = df.index.month
df["Day"] = df.index.day
```

### Bài tập ngắn — Datetime Components

```python
# df["Year"] = df.index.____
# df["Month"] = df.index.____
# df["Day"] = df.index.____
```

## 7.5. Resampling chuỗi thời gian
Tổng theo tháng:

```python
monthly = df["Sales"].resample(
    "ME"
).sum()
```

Trung bình theo tuần:

```python
weekly = df["Sales"].resample(
    "W"
).mean()
```

## 7.6. Thống kê rolling
Trung bình trượt:

```python
df["MovingAvg"] = (
    df["Sales"]
    .rolling(window=3)
    .mean()
)
```

## 7.7. Các lệnh nâng cao chính
| Command | Meaning |
|---|---|
| `df.corr()` | Calculate correlation matrix. |
| `Series.corr()` | Calculate correlation between two Series. |
| `df.plot()` | Create quick visualizations. |
| `pd.to_datetime()` | Convert values to datetime. |
| `df.set_index()` | Set a column as the index. |
| `df.resample()` | Aggregate time-series data by time intervals. |
| `Series.rolling()` | Calculate rolling-window statistics. |

## 7.8. Kiểm tra nhanh
**Câu 1.** Which function converts a column to datetime?

A. `pd.to_datetime()`  
B. `pd.date_convert_only()`  
C. `df.datetime()`  
D. `pd.time_series()`

**Câu 2.** Which method calculates a correlation matrix?

A. `corr()`  
B. `merge()`  
C. `dropna()`  
D. `pivot()`

## Bài tập
### Bài tập 7.1. Correlation
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

### Bài tập 7.2. Visualization
Using a sales DataFrame, create:

1. a line chart;
2. a bar chart;
3. a histogram;
4. a scatter plot.

### Bài tập 7.3. Time-Series Index
Create a DataFrame with columns:

- `Date`;
- `Sales`.

Then:

1. convert `Date` to datetime;
2. set `Date` as index;
3. sort by date.

### Bài tập 7.4. Resampling
Using daily sales data:

1. calculate weekly total sales;
2. calculate monthly average sales.

### Bài tập 7.5. Moving Average
Calculate a 3-period moving average for a `Sales` Series.

---

# Phần 8. Câu hỏi ôn tập
## 8.1. Câu hỏi trắc nghiệm
**Câu 1.** What is the main purpose of Pandas?

A. Data manipulation and analysis  
B. Operating-system administration  
C. Web-server management  
D. Computer graphics only

**Câu 2.** Which Pandas structure is one-dimensional?

A. `DataFrame`  
B. `Series`  
C. `ndarray` only  
D. `pivot`

**Câu 3.** Which selector is based on integer position?

A. `loc`  
B. `iloc`  
C. `index`  
D. `columns`

**Câu 4.** Which function reads a CSV file?

A. `pd.read_csv()`  
B. `pd.csv_open()`  
C. `pd.load_csv_only()`  
D. `df.read()`

**Câu 5.** Which method replaces missing values?

A. `fillna()`  
B. `drop_duplicates()`  
C. `sort_values()`  
D. `merge()`

**Câu 6.** Which method removes duplicate rows?

A. `drop_duplicates()`  
B. `fillna()`  
C. `groupby()`  
D. `pivot()`

**Câu 7.** Which method groups observations?

A. `groupby()`  
B. `describe()`  
C. `drop()`  
D. `astype()`

**Câu 8.** Which function merges two DataFrames using a common key?

A. `pd.merge()`  
B. `pd.mean()`  
C. `pd.Series()`  
D. `pd.plot()`

**Câu 9.** Which function converts values to datetime?

A. `pd.to_datetime()`  
B. `pd.to_numeric()`  
C. `pd.read_date()`  
D. `pd.datetime_only()`

**Câu 10.** Which method calculates correlation?

A. `corr()`  
B. `join()`  
C. `head()`  
D. `fillna()`

## 8.2. Câu hỏi Đúng/Sai
**Câu 1.** A DataFrame is two-dimensional.  
**Câu 2.** A Series is a one-dimensional labeled array.  
**Câu 3.** `loc` is based only on integer position.  
**Câu 4.** `iloc` is position-based.  
**Câu 5.** `dropna()` can be used to remove missing values.  
**Câu 6.** `fillna()` can replace missing values.  
**Câu 7.** `groupby()` can be followed by aggregation functions.  
**Câu 8.** `pd.merge()` can perform inner and left joins.  
**Câu 9.** `pd.to_datetime()` can convert text dates to datetime values.  
**Câu 10.** Correlation automatically proves causation.

## 8.3. Câu hỏi trả lời ngắn
**Câu 1.** Explain the difference between a Series and a DataFrame.

**Câu 2.** Explain the difference between `loc` and `iloc`.

**Câu 3.** Give two methods for handling missing values.

**Câu 4.** Explain the difference between `pd.concat()` and `pd.merge()`.

**Câu 5.** What is the purpose of `groupby()`?

**Câu 6.** Why is data-type conversion important in data cleaning?

**Câu 7.** Explain what a pivot table does.

**Câu 8.** State one use of `pd.to_datetime()`.

---

# Phần 9. Bài tập thực hành
## Exercise 1. Dữ liệu sinh viên
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

## Exercise 2. Dữ liệu thiếu
Add missing values to the student dataset.

Then:

1. count missing values;
2. fill missing Age with mean Age;
3. fill missing GPA with median GPA;
4. remove rows with missing Name.

## Exercise 3. CSV và Excel
Export the cleaned student dataset to:

```text
students.csv
students.xlsx
```

Read both files back into Pandas.

## Exercise 4. Phân tích doanh số
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

## Exercise 7. Chuỗi thời gian
Create daily sales data for at least 30 days.

Then:

1. convert Date to datetime;
2. set Date as index;
3. calculate weekly total sales;
4. calculate a 7-day moving average;
5. create a line plot.

---

# Phần 10. Đáp án và gợi ý trả lời
## Đáp án phần kiểm tra nhanh
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

## Đáp án trắc nghiệm
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

## Đáp án Đúng/Sai
1. Đúng  
2. Đúng  
3. Sai  
4. Đúng  
5. Đúng  
6. Đúng  
7. Đúng  
8. Đúng  
9. Đúng  
10. Sai

## Gợi ý trả lời ngắn
**Câu 1.** A Series is a one-dimensional labeled array, while a DataFrame is a two-dimensional labeled table with rows and columns.

**Câu 2.** `loc` selects observations using labels, while `iloc` selects observations using integer positions.

**Câu 3.** Missing values can be removed using `dropna()` or replaced using `fillna()`.

**Câu 4.** `pd.concat()` combines DataFrames along an axis, while `pd.merge()` combines them using matching key columns.

**Câu 5.** `groupby()` splits data into groups based on categorical values so that aggregation or transformation can be applied to each group.

**Câu 6.** Correct data types are required for valid numerical operations, comparisons, sorting, aggregation, and modeling.

**Câu 7.** A pivot table summarizes a numerical variable across one or more categorical dimensions.

**Câu 8.** `pd.to_datetime()` converts date-like strings or values into Pandas datetime objects so that time-based operations can be performed.

---

# Lời giải gợi ý cho một số bài thực hành
## Exercise 1. Dữ liệu sinh viên
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

## Exercise 2. Dữ liệu thiếu
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

## Exercise 3. CSV và Excel
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

## Exercise 4. Phân tích doanh số
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

## Exercise 7. Chuỗi thời gian
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