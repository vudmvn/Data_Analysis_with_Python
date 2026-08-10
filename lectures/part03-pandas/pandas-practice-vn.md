# BÀI TẬP THỰC HÀNH PANDAS

**Chủ đề:** DataFrame, Series, nhập/xuất dữ liệu, làm sạch, biến đổi và phân tích dữ liệu  
**Ngôn ngữ:** Python  
**Thư viện chính:** Pandas

## Mục tiêu

Sau khi hoàn thành notebook này, người học có thể:

- Tạo và kiểm tra `Series` và `DataFrame`.
- Đọc được `shape`, `columns`, `index`, `dtypes`, `info()` và `describe()`.
- Truy xuất dữ liệu bằng `loc`, `iloc`, indexing và slicing.
- Lọc dữ liệu bằng một hoặc nhiều điều kiện.
- Sắp xếp dữ liệu và tạo cột mới.
- Đọc và ghi dữ liệu với CSV, Excel và JSON.
- Phát hiện và xử lý dữ liệu thiếu.
- Phát hiện và loại bỏ dữ liệu trùng lặp.
- Chuyển đổi kiểu dữ liệu và làm sạch chuỗi.
- Nhóm và tổng hợp dữ liệu bằng `groupby()` và `agg()`.
- Kết hợp dữ liệu bằng `merge()` và `concat()`.
- Reshape dữ liệu bằng `pivot()`, `melt()` và `pivot_table()`.
- Tính tương quan và thống kê mô tả.
- Làm việc với dữ liệu thời gian bằng `to_datetime()`, `resample()` và `rolling()`.
- Tạo biểu đồ nhanh bằng Pandas.
- Hoàn thành một bài phân tích dữ liệu tổng hợp bằng Pandas.

## Quy định làm bài

Với mỗi bài tập, trình bày theo thứ tự:

1. **Code**
2. **Output**
3. **Giải thích ngắn từ 1-3 câu**

Ngoài ra:

- Không sửa trực tiếp dữ liệu đầu vào nếu đề không yêu cầu.
- Khi lọc hoặc reshape dữ liệu, nên in `shape` của kết quả.
- Khi xử lý dữ liệu thiếu, cần kiểm tra số lượng missing values trước và sau xử lý.
- Khi merge hai bảng, cần kiểm tra số dòng trước và sau merge.
- Có thể chạy các ô **Kiểm tra tự động** sau khi hoàn thành bài.
- Với các bài I/O, các file được lưu trong thư mục làm việc hiện tại.

---

# PHẦN 0 - CHUẨN BỊ MÔI TRƯỜNG

```python
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

print("Pandas version:", pd.__version__)
```

---

# PHẦN 1 - LÀM QUEN VỚI SERIES VÀ DATAFRAME

## Bài 1. Tạo Series cơ bản

Cho:

```python
values = [10, 20, 30, 40]
```

### Yêu cầu

1. Tạo `Series` tên `s` từ `values`.
2. In `s`.
3. In `s.index`, `s.values`, `s.dtype`.
4. Tạo `Series` mới có index là `["A", "B", "C", "D"]`.
5. Truy xuất phần tử có nhãn `"C"` bằng `loc`.
6. Truy xuất phần tử ở vị trí 2 bằng `iloc`.
7. Giải thích sự khác nhau giữa `loc` và `iloc`.

### Hint

Gợi ý: dùng `pd.Series(...)`, sau đó kiểm tra `.index`, `.values`, `.dtype`; dùng `.loc[...]` cho nhãn và `.iloc[...]` cho vị trí.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
s = pd.Series(values)
print(s)
print(s.index)
print(s.values)
print(s.dtype)

s_label = pd.Series(values, index=[..., ..., ..., ...])

# Hoàn thiện:
# print(s_label.loc[...])
# print(s_label.iloc[...])
```

```python
# Viết lời giải tại đây

values = [10, 20, 30, 40]

# s = ...
# TODO
```

**Giải thích của sinh viên:**

-

### Kiểm tra tự động

```python
try:
    assert isinstance(s, pd.Series)
    assert len(s) == 4
    assert s.iloc[2] == 30
    print("Đạt yêu cầu cơ bản.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

## Bài 2. Tạo DataFrame từ dictionary

Cho:

```python
data = {
    "StudentID": ["S01", "S02", "S03", "S04"],
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Age": [20, 21, 19, 22],
    "GPA": [3.2, 3.7, 3.5, 3.8]
}
```

### Yêu cầu

1. Tạo `DataFrame` tên `df`.
2. In toàn bộ `df`.
3. In:
   - `df.shape`
   - `df.columns`
   - `df.index`
   - `df.dtypes`
4. In hai dòng đầu bằng `head()`.
5. In hai dòng cuối bằng `tail()`.
6. Giải thích ý nghĩa của `shape`.

### Hint

Gợi ý: dùng `pd.DataFrame(data)`. Các thuộc tính `shape`, `columns`, `index`, `dtypes` không cần dấu ngoặc; `head()` và `tail()` là method.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)

# Hoàn thiện:
# print(df.head(...))
# print(df.tail(...))
```

```python
# Viết lời giải tại đây

data = {
    "StudentID": ["S01", "S02", "S03", "S04"],
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Age": [20, 21, 19, 22],
    "GPA": [3.2, 3.7, 3.5, 3.8]
}

# TODO
```

**Giải thích của sinh viên:**

-

### Kiểm tra tự động

```python
try:
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (4, 4)
    assert list(df.columns) == ["StudentID", "Name", "Age", "GPA"]
    print("Đạt yêu cầu.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

## Bài 3. `info()` và `describe()`

Dùng DataFrame `df` của Bài 2.

### Yêu cầu

1. Chạy `df.info()`.
2. Chạy `df.describe()`.
3. Giải thích:
   - `info()` cung cấp thông tin gì?
   - `describe()` chủ yếu tổng hợp loại biến nào?
4. Tính riêng:
   - tuổi trung bình;
   - GPA trung bình;
   - GPA lớn nhất.

### Hint

Gợi ý: `info()` in thông tin cấu trúc trực tiếp; `describe()` trả về một DataFrame thống kê. Có thể dùng `.mean()` và `.max()` trên từng cột.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
df.info()

summary = df.describe()
print(summary)

# Hoàn thiện:
# mean_age = df["Age"].____()
# mean_gpa = df["GPA"].____()
# max_gpa = df["GPA"].____()
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

# PHẦN 2 - TRUY XUẤT, INDEXING, FILTERING VÀ SORTING

## Bài 4. Truy xuất cột

Dùng `df` của phần trước.

### Yêu cầu

1. Lấy cột `Name`.
2. Lấy đồng thời `Name` và `GPA`.
3. In kiểu dữ liệu của kết quả ở câu 1 và câu 2.
4. Giải thích vì sao một cột thường trả về `Series`, còn nhiều cột trả về `DataFrame`.

### Hint

Gợi ý: `df['Name']` trả về Series; `df[['Name', 'GPA']]` trả về DataFrame.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
name_col = df["Name"]
name_gpa = df[[..., ...]]

print(type(name_col))
print(type(name_gpa))
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 5. `loc` và `iloc`

### Yêu cầu

1. Đặt `StudentID` làm index bằng `set_index()`, lưu thành `students`.
2. Dùng `loc` lấy sinh viên `"S02"`.
3. Dùng `iloc` lấy dòng đầu tiên.
4. Dùng `loc` lấy các dòng `"S01"` đến `"S03"` và các cột `Name`, `GPA`.
5. Dùng `iloc` lấy 2 dòng đầu và 2 cột cuối.
6. In `shape` của từng kết quả.
7. Giải thích sự khác nhau giữa selection theo nhãn và theo vị trí.

### Hint

Gợi ý: dùng `set_index('StudentID')`, sau đó so sánh `students.loc['S02']` với `students.iloc[0]`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
students = df.set_index("StudentID")

row_s02 = students.loc[...]
first_row = students.iloc[...]

subset_loc = students.loc[[..., ...], [..., ...]]
subset_iloc = students.iloc[...:..., [..., ...]]
```

```python
# Viết lời giải tại đây

# students = ...
# TODO
```

**Giải thích của sinh viên:**

-

### Kiểm tra tự động

```python
try:
    assert students.index.name == "StudentID"
    assert students.loc["S02", "Name"] == "Binh"
    assert students.iloc[0]["Name"] == "An"
    print("Đạt yêu cầu.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

## Bài 6. Lọc dữ liệu theo một điều kiện

Cho:

```python
students = pd.DataFrame({
    "StudentID": ["S01", "S02", "S03", "S04", "S05", "S06"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa", "Khanh"],
    "Age": [20, 21, 19, 22, 20, 23],
    "GPA": [3.2, 3.7, 3.5, 3.8, 2.9, 3.6]
})
```

### Yêu cầu

1. Lọc sinh viên có `GPA >= 3.5`.
2. Lọc sinh viên có `Age > 20`.
3. In `shape` của từng kết quả.
4. Chỉ giữ các cột `Name` và `GPA` trong kết quả câu 1.

### Hint

Gợi ý: tạo Boolean mask như `students['GPA'] >= 3.5`, rồi đặt mask bên trong `students[...]`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
high_gpa = students[students["GPA"] >= ...]
older = students[students["Age"] > ...]

result = high_gpa[[..., ...]]
```

```python
# Viết lời giải tại đây

students = pd.DataFrame({
    "StudentID": ["S01", "S02", "S03", "S04", "S05", "S06"],
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa", "Khanh"],
    "Age": [20, 21, 19, 22, 20, 23],
    "GPA": [3.2, 3.7, 3.5, 3.8, 2.9, 3.6]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 7. Lọc với nhiều điều kiện

Dùng DataFrame `students`.

### Yêu cầu

1. Lọc sinh viên có:
   - `Age >= 20`
   - và `GPA >= 3.5`
2. Lọc sinh viên có:
   - `GPA < 3.0`
   - hoặc `Age >= 22`
3. Dùng `~` để lấy sinh viên **không** có `GPA >= 3.5`.
4. Giải thích vai trò của:
   - `&`
   - `|`
   - `~`
5. Giải thích vì sao mỗi điều kiện nên đặt trong ngoặc.

### Hint

Gợi ý: mỗi điều kiện nên đặt trong ngoặc; dùng `&`, `|`, `~` thay cho `and`, `or`, `not`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
cond1 = (students["Age"] >= ...) & (students["GPA"] >= ...)
result1 = students[cond1]

cond2 = (students["GPA"] < ...) | (students["Age"] >= ...)
result2 = students[cond2]

result3 = students[~(students["GPA"] >= ...)]
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 8. Sắp xếp dữ liệu

Dùng `students`.

### Yêu cầu

1. Sắp xếp theo GPA tăng dần.
2. Sắp xếp theo GPA giảm dần.
3. Sắp xếp theo:
   - Age tăng dần;
   - GPA giảm dần.
4. In ba kết quả.
5. Giải thích `ascending=[True, False]`.

### Hint

Gợi ý: `sort_values()` nhận một tên cột hoặc danh sách tên cột. Với nhiều cột, `ascending` cũng có thể là danh sách Boolean.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
asc_gpa = students.sort_values("GPA", ascending=...)
desc_gpa = students.sort_values("GPA", ascending=...)

multi = students.sort_values(
    [..., ...],
    ascending=[..., ...]
)
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

# PHẦN 3 - DATA INPUT / OUTPUT

## Bài 9. Ghi và đọc CSV

Cho:

```python
sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})
```

### Yêu cầu

1. Ghi `sales` ra file `sales.csv` với `index=False`.
2. Đọc file vào `sales_csv`.
3. In `sales_csv`.
4. So sánh `shape` của `sales` và `sales_csv`.
5. Giải thích vì sao thường dùng `index=False`.

### Hint

Gợi ý: dùng `to_csv(..., index=False)` rồi `pd.read_csv(...)`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
sales.to_csv("sales.csv", index=...)

sales_csv = pd.read_csv(...)
print(sales_csv)
```

```python
# Viết lời giải tại đây

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})

# TODO
```

**Giải thích của sinh viên:**

-

### Kiểm tra tự động

```python
try:
    assert sales_csv.shape == sales.shape
    assert list(sales_csv.columns) == list(sales.columns)
    print("Đạt yêu cầu.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

## Bài 10. Ghi và đọc Excel

Dùng DataFrame `sales`.

### Yêu cầu

1. Ghi `sales` ra `sales.xlsx`.
2. Đọc lại vào `sales_excel`.
3. In dữ liệu.
4. So sánh với DataFrame ban đầu.
5. Kiểm tra `dtypes`.

### Hint

Gợi ý: dùng `to_excel()` và `pd.read_excel()`. Có thể cần package `openpyxl` trong một số môi trường.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
sales.to_excel("sales.xlsx", index=...)
sales_excel = pd.read_excel(...)

print(sales_excel)
print(sales_excel.dtypes)
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 11. JSON

Dùng DataFrame `sales`.

### Yêu cầu

1. Ghi dữ liệu thành `sales.json` với `orient="records"`.
2. Đọc lại file JSON bằng Pandas.
3. In dữ liệu.
4. Giải thích `orient="records"` tạo cấu trúc dữ liệu như thế nào.

### Hint

Gợi ý: dùng `to_json(..., orient='records')` và `pd.read_json(...)`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
sales.to_json(
    "sales.json",
    orient=...
)

sales_json = pd.read_json(...)
print(sales_json)
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

# PHẦN 4 - DATA CLEANING

## Bài 12. Phát hiện dữ liệu thiếu

Cho:

```python
df = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "Age": [20, np.nan, 22, 21, np.nan],
    "GPA": [3.2, 3.6, np.nan, 3.8, 3.1],
    "City": ["Hanoi", "Hanoi", None, "Danang", "Hanoi"]
})
```

### Yêu cầu

1. In `df`.
2. Dùng `isna()` để xác định vị trí thiếu.
3. Đếm số missing values theo từng cột.
4. Tính tổng số missing values trong toàn DataFrame.
5. Giải thích sự khác nhau giữa `None` và `np.nan` trong DataFrame ở mức thực hành.

### Hint

Gợi ý: `df.isna()` tạo mask Boolean; `df.isna().sum()` đếm theo cột; gọi `.sum()` thêm lần nữa để lấy tổng toàn bảng.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
missing_mask = df.isna()
missing_by_col = df.isna().sum()
total_missing = df.isna().sum().sum()

print(missing_mask)
print(missing_by_col)
print(total_missing)
```

```python
# Viết lời giải tại đây

df = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "Age": [20, np.nan, 22, 21, np.nan],
    "GPA": [3.2, 3.6, np.nan, 3.8, 3.1],
    "City": ["Hanoi", "Hanoi", None, "Danang", "Hanoi"]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 13. `dropna()` và `fillna()`

Dùng DataFrame `df` của Bài 12.

### Yêu cầu

1. Tạo `drop_rows` bằng cách loại các dòng có missing value.
2. Tạo `drop_cols` bằng cách loại các cột có missing value.
3. Tạo `filled`:
   - `Age`: thay bằng trung bình;
   - `GPA`: thay bằng trung vị;
   - `City`: thay bằng `"Unknown"`.
4. In số missing values sau xử lý.
5. Không sửa `df` ban đầu.
6. Giải thích khi nào nên dùng `dropna()` và khi nào nên dùng `fillna()`.

### Hint

Gợi ý: tạo bản sao trước bằng `df.copy()`. Có thể fill từng cột riêng để dùng mean/median phù hợp.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

### Kiểm tra tự động

```python
try:
    assert filled.isna().sum().sum() == 0
    assert df.isna().sum().sum() > 0
    print("Đạt yêu cầu.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

## Bài 14. Dữ liệu trùng lặp

Cho:

```python
df = pd.DataFrame({
    "ID": [1, 2, 2, 3, 4, 4],
    "Name": ["An", "Binh", "Binh", "Chi", "Dung", "Dung"],
    "Score": [7, 8, 8, 9, 6, 6]
})
```

### Yêu cầu

1. Dùng `duplicated()` để xác định dòng trùng.
2. Đếm số dòng trùng.
3. Tạo `clean_df` bằng `drop_duplicates()`.
4. In `shape` trước và sau.
5. Giải thích mặc định `drop_duplicates()` giữ bản ghi nào.

### Hint

Gợi ý: `duplicated()` đánh dấu từ lần xuất hiện thứ hai theo mặc định; `drop_duplicates()` mặc định giữ bản ghi đầu tiên.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
dup_mask = df.duplicated()
dup_count = dup_mask.sum()

clean_df = df.drop_duplicates()

print(df.shape)
print(clean_df.shape)
```

```python
# Viết lời giải tại đây

df = pd.DataFrame({
    "ID": [1, 2, 2, 3, 4, 4],
    "Name": ["An", "Binh", "Binh", "Chi", "Dung", "Dung"],
    "Score": [7, 8, 8, 9, 6, 6]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 15. Chuyển đổi kiểu dữ liệu

Cho:

```python
df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Price": ["10.5", "20", "unknown", "15.75"],
    "Quantity": ["2", "3", "4", "5"]
})
```

### Yêu cầu

1. In `dtypes`.
2. Chuyển `Price` sang numeric bằng `pd.to_numeric(..., errors="coerce")`.
3. Chuyển `Quantity` sang `int`.
4. In lại `dtypes`.
5. Kiểm tra missing values trong `Price`.
6. Giải thích `"unknown"` biến thành gì và vì sao.

### Hint

Gợi ý: dùng `pd.to_numeric(..., errors='coerce')` cho cột có dữ liệu bẩn; `astype(int)` phù hợp khi chắc chắn không còn giá trị lỗi.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Price": ["10.5", "20", "unknown", "15.75"],
    "Quantity": ["2", "3", "4", "5"]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 16. Làm sạch chuỗi

Cho:

```python
df = pd.DataFrame({
    "Name": [" An ", "BINH", " chi ", "DuNg"],
    "City": [" HANOI", "hanoi ", "DaNang", " HCM "]
})
```

### Yêu cầu

1. Loại bỏ khoảng trắng đầu/cuối của `Name` và `City`.
2. Chuyển `Name` về chữ thường.
3. Chuyển `City` về chữ hoa.
4. Thay `"HANOI"` bằng `"HA NOI"`.
5. In kết quả.
6. Không dùng vòng lặp Python.

### Hint

Gợi ý: các string methods có thể nối chuỗi: `.str.strip().str.lower()`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

df = pd.DataFrame({
    "Name": [" An ", "BINH", " chi ", "DuNg"],
    "City": [" HANOI", "hanoi ", "DaNang", " HCM "]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

# PHẦN 5 - BIẾN ĐỔI, TÍNH TOÁN VÀ THỐNG KÊ

## Bài 17. Tạo cột mới

Cho:

```python
sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})
```

### Yêu cầu

1. Tạo:
   `Revenue = Quantity * Price`
2. Tạo:
   `PriceWithTax = Price * 1.1`
3. In DataFrame mới.
4. Tính tổng Revenue.
5. Tìm Product có Revenue lớn nhất.

### Hint

Gợi ý: Pandas hỗ trợ phép toán vector hóa giữa các cột; không cần vòng lặp.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
sales["Revenue"] = sales["Quantity"] * sales["Price"]
sales["PriceWithTax"] = sales["Price"] * ...

total_revenue = sales["Revenue"].____()
idx_max = sales["Revenue"].____()
top_product = sales.loc[idx_max, "Product"]
```

```python
# Viết lời giải tại đây

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Quantity": [2, 5, 3, 4],
    "Price": [10.0, 8.0, 12.0, 7.5]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 18. `map()` và `apply()`

Cho:

```python
students = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Score": [4.5, 7.0, 8.5, 5.0]
})
```

### Yêu cầu

1. Tạo cột `Status`:
   - `"Pass"` nếu Score >= 5;
   - `"Fail"` nếu Score < 5.
2. Tạo cột `SquaredScore = Score ** 2`.
3. Thực hiện bằng `map()` hoặc `apply()`.
4. In kết quả.
5. Giải thích điểm giống nhau và khác nhau ở mức cơ bản giữa `map()` và `apply()` trên Series.

### Hint

Gợi ý: dùng `Series.map(lambda x: ...)` hoặc `Series.apply(lambda x: ...)`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
students["Status"] = students["Score"].map(
    lambda x: ... if x >= ... else ...
)

students["SquaredScore"] = students["Score"].apply(
    lambda x: ...
)
```

```python
# Viết lời giải tại đây

students = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Score": [4.5, 7.0, 8.5, 5.0]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 19. Chuẩn hóa dữ liệu

Cho:

```python
df = pd.DataFrame({
    "Value": [10, 20, 30, 40, 50]
})
```

### Yêu cầu

1. Tạo cột `MinMax` theo công thức min-max.
2. Tạo cột `ZScore`.
3. Kiểm tra min của `MinMax` bằng 0.
4. Kiểm tra max của `MinMax` bằng 1.
5. Kiểm tra mean của `ZScore` xấp xỉ 0.
6. Giải thích khác nhau giữa min-max normalization và z-score standardization.

### Hint

Gợi ý: min-max dùng `(x-min)/(max-min)`; z-score dùng `(x-mean)/std`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

df = pd.DataFrame({
    "Value": [10, 20, 30, 40, 50]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 20. Thống kê mô tả

Cho:

```python
df = pd.DataFrame({
    "Sales": [100, 120, 90, 150, 130, 110],
    "Cost": [70, 80, 60, 100, 85, 75]
})
```

### Yêu cầu

1. Chạy `describe()`.
2. Tính riêng:
   - mean;
   - median;
   - min;
   - max;
   - std.
3. Tạo cột `Profit = Sales - Cost`.
4. Tính mean và max của Profit.
5. Viết nhận xét ngắn.

### Hint

Gợi ý: dùng `describe()` cho tổng quan và phép toán vector hóa để tạo `Profit`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
print(df.describe())

df["Profit"] = df["Sales"] - df["Cost"]

mean_profit = df["Profit"].____()
max_profit = df["Profit"].____()
```

```python
# Viết lời giải tại đây

df = pd.DataFrame({
    "Sales": [100, 120, 90, 150, 130, 110],
    "Cost": [70, 80, 60, 100, 85, 75]
})

# TODO
```

**Nhận xét của sinh viên:**

-

---

# PHẦN 6 - GROUPBY, AGGREGATION VÀ RESHAPING

## Bài 21. `groupby()` cơ bản

Cho:

```python
sales = pd.DataFrame({
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Product": ["A", "A", "B", "B", "A", "B"],
    "Sales": [100, 120, 90, 150, 130, 110]
})
```

### Yêu cầu

1. Tính tổng Sales theo Region.
2. Tính mean Sales theo Region.
3. Tính tổng Sales theo Product.
4. In tất cả kết quả.
5. Giải thích `groupby()` làm gì về mặt logic.

### Hint

Gợi ý: mẫu cơ bản là `df.groupby('key')['value'].aggregation()`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
sum_region = sales.groupby("Region")["Sales"].____()
mean_region = sales.groupby("Region")["Sales"].____()
sum_product = sales.groupby("Product")["Sales"].____()
```

```python
# Viết lời giải tại đây

sales = pd.DataFrame({
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Product": ["A", "A", "B", "B", "A", "B"],
    "Sales": [100, 120, 90, 150, 130, 110]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 22. `agg()` với nhiều phép tổng hợp

Dùng DataFrame `sales`.

### Yêu cầu

1. Group theo `Region`.
2. Với cột `Sales`, tính:
   - count;
   - sum;
   - mean;
   - min;
   - max.
3. Lưu thành `summary`.
4. In `summary`.
5. Giải thích vì sao `agg()` hữu ích.

### Hint

Gợi ý: dùng `.agg(['count', 'sum', 'mean', 'min', 'max'])` trên cột sau `groupby()`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
summary = (
    sales
    .groupby("Region")["Sales"]
    .agg([...])
)

print(summary)
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

### Kiểm tra tự động

```python
try:
    assert "sum" in summary.columns
    assert "mean" in summary.columns
    assert summary.shape[0] == 2
    print("Đạt yêu cầu.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

## Bài 23. Group theo nhiều cột

Dùng `sales`.

### Yêu cầu

1. Group theo `Region` và `Product`.
2. Tính tổng Sales.
3. Chuyển kết quả về DataFrame bằng `reset_index()`.
4. In kết quả.
5. Giải thích ý nghĩa của MultiIndex trước khi dùng `reset_index()`.

### Hint

Gợi ý: truyền danh sách nhiều cột cho `groupby([...])`; dùng `reset_index()` để biến các khóa group trở lại thành cột.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
summary2 = (
    sales
    .groupby([..., ...])["Sales"]
    .____()
    .reset_index()
)
```

```python
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 24. Pivot table

Dùng DataFrame `sales`.

### Yêu cầu

Tạo pivot table:

- rows: `Region`;
- columns: `Product`;
- values: `Sales`;
- aggregation: `sum`.

Sau đó:

1. in pivot table;
2. tính tổng từng hàng;
3. giải thích pivot table giúp đọc dữ liệu như thế nào.

### Hint

Gợi ý: dùng `pd.pivot_table()` với `values`, `index`, `columns`, `aggfunc`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 25. `pivot()` và `melt()`

Cho:

```python
df = pd.DataFrame({
    "Date": ["2026-01", "2026-01", "2026-02", "2026-02"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 120, 130, 150]
})
```

### Yêu cầu

1. Dùng `pivot()` chuyển dữ liệu thành dạng wide:
   - index: Date
   - columns: Product
   - values: Sales
2. Dùng `reset_index()`.
3. Dùng `melt()` chuyển ngược về dạng long.
4. In các `shape`.
5. Giải thích sự khác nhau giữa long format và wide format.

### Hint

Gợi ý: `pivot()` chuyển long → wide; `pd.melt()` thường dùng sau `reset_index()` để wide → long.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

df = pd.DataFrame({
    "Date": ["2026-01", "2026-01", "2026-02", "2026-02"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 120, 130, 150]
})

# TODO
```

**Giải thích của sinh viên:**

-

---

# PHẦN 7 - MERGE, JOIN VÀ CONCAT

## Bài 26. Inner merge

Cho:

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

### Yêu cầu

1. Inner merge theo `CustomerID`.
2. In kết quả.
3. So sánh số dòng của:
   - customers;
   - orders;
   - merged.
4. Giải thích vì sao `C03`, `C04`, `C05` có thể không xuất hiện trong inner merge.

### Hint

Gợi ý: `pd.merge(left, right, on='CustomerID', how='inner')` chỉ giữ khóa có mặt ở cả hai bảng.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
merged = pd.merge(
    customers,
    orders,
    on=...,
    how=...
)

print(merged)
```

```python
# Viết lời giải tại đây

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

**Giải thích của sinh viên:**

-

---

## Bài 27. Left, right và outer merge

Dùng `customers` và `orders`.

### Yêu cầu

1. Thực hiện:
   - left merge;
   - right merge;
   - outer merge.
2. In `shape` của từng kết quả.
3. Tìm khách hàng chưa có đơn hàng từ left merge.
4. Tìm đơn hàng không có thông tin khách hàng từ right hoặc outer merge.
5. Giải thích khác nhau giữa 4 loại join:
   - inner;
   - left;
   - right;
   - outer.

### Hint

Gợi ý: lặp lại `pd.merge()` với `how='left'`, `'right'`, `'outer'`; dùng `isna()` để tìm bản ghi không match.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 28. `concat()`

Cho:

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

### Yêu cầu

1. Ghép `df1`, `df2` theo hàng.
2. Dùng `ignore_index=True`.
3. Tạo một DataFrame khác có cột `Category` và concat theo cột.
4. In `shape`.
5. Giải thích khác nhau giữa `concat()` và `merge()`.

### Hint

Gợi ý: `pd.concat([df1, df2], axis=0, ignore_index=True)` ghép theo hàng; `axis=1` ghép theo cột.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

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

**Giải thích của sinh viên:**

-

---

# PHẦN 8 - TƯƠNG QUAN, TIME SERIES VÀ VISUALIZATION

## Bài 29. Correlation

Cho:

```python
df = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50, 60],
    "Sales": [100, 120, 145, 170, 210, 230],
    "Price": [20, 19, 18, 18, 17, 16]
})
```

### Yêu cầu

1. Tính ma trận tương quan.
2. Tính riêng correlation giữa:
   - Advertising và Sales;
   - Price và Sales.
3. Tìm cặp biến có tương quan dương mạnh nhất.
4. Viết nhận xét ngắn.
5. Giải thích vì sao correlation không đồng nghĩa với causation.

### Hint

Gợi ý: dùng `df.corr(numeric_only=True)` và `Series.corr(other_series)`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
corr_matrix = df.corr(numeric_only=True)

ad_sales = df["Advertising"].corr(
    df["Sales"]
)

price_sales = df["Price"].corr(
    df["Sales"]
)
```

```python
# Viết lời giải tại đây

df = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50, 60],
    "Sales": [100, 120, 145, 170, 210, 230],
    "Price": [20, 19, 18, 18, 17, 16]
})

# TODO
```

**Nhận xét của sinh viên:**

-

---

## Bài 30. Chuyển đổi ngày tháng

Cho:

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

### Yêu cầu

1. In `dtypes` ban đầu.
2. Chuyển `Date` thành datetime bằng `pd.to_datetime()`.
3. In lại `dtypes`.
4. Tạo các cột:
   - Year;
   - Month;
   - Day.
5. Đặt `Date` làm index.
6. Sắp xếp theo thời gian.

### Hint

Gợi ý: dùng `pd.to_datetime()`, sau đó có thể truy cập `.dt.year`, `.dt.month`, `.dt.day` trước khi đặt Date làm index.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

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

**Giải thích của sinh viên:**

-

---

## Bài 31. Resampling time series

Tạo dữ liệu:

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

### Yêu cầu

1. Tính tổng Sales theo tuần.
2. Tính mean Sales theo tuần.
3. Tính tổng Sales theo tháng.
4. In kết quả.
5. Giải thích resampling thay đổi mức độ chi tiết thời gian như thế nào.

### Hint

Gợi ý: sau khi Date là DatetimeIndex, dùng `.resample('W')` hoặc `.resample('ME')` rồi aggregate.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
weekly_sum = df["Sales"].resample(...).____()
weekly_mean = df["Sales"].resample(...).____()
monthly_sum = df["Sales"].resample(...).____()
```

```python
# Viết lời giải tại đây

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

**Giải thích của sinh viên:**

-

---

## Bài 32. Rolling statistics

Dùng time series ở Bài 31.

### Yêu cầu

1. Tạo `MA3`: moving average 3 ngày.
2. Tạo `MA7`: moving average 7 ngày.
3. In 10 dòng đầu.
4. Đếm số `NaN` trong `MA3` và `MA7`.
5. Giải thích vì sao các giá trị đầu tiên bị thiếu.

### Hint

Gợi ý: `rolling(window=k).mean()` cần đủ `k` quan sát nên các phần tử đầu có thể là `NaN`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

# TODO
```

**Giải thích của sinh viên:**

-

---

## Bài 33. Visualization nhanh với Pandas

Cho:

```python
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 90, 150, 170],
    "Advertising": [10, 15, 8, 20, 25]
})
```

### Yêu cầu

Tạo:

1. line chart của Sales theo Month;
2. bar chart của Sales;
3. histogram của Sales;
4. scatter plot giữa Advertising và Sales.

Mỗi biểu đồ cần có:

- title;
- xlabel;
- ylabel.

### Hint

Gợi ý: dùng `df.plot(...)` hoặc `Series.plot(...)`; truyền `kind`, `x`, `y`, `title`.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh
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
# Viết lời giải tại đây

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 90, 150, 170],
    "Advertising": [10, 15, 8, 20, 25]
})

# TODO
```

**Nhận xét của sinh viên:**

-

---

# PHẦN 9 - BÀI TỔNG HỢP

## Bài 34. Phân tích dữ liệu bán hàng bằng Pandas

Cho:

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

### Yêu cầu

Không dùng vòng lặp Python để xử lý từng dòng:

1. In:
   - `shape`;
   - `dtypes`;
   - `info()`.
2. Chuyển `Date` sang datetime.
3. Đếm missing values.
4. Thay `Price` thiếu bằng median Price.
5. Tạo:
   `Revenue = Quantity * Price`.
6. Tính:
   - tổng Revenue;
   - mean Revenue;
   - max Revenue.
7. Lọc các đơn có Revenue lớn hơn mean Revenue.
8. Tính tổng Revenue theo Region.
9. Tính tổng Revenue theo Product.
10. Group theo `Region`, tính:
    - count;
    - sum;
    - mean Revenue.
11. Tạo pivot table:
    - index: Region;
    - columns: Product;
    - values: Revenue;
    - aggfunc: sum.
12. Tìm OrderID có Revenue lớn nhất.
13. Sắp xếp dữ liệu theo Revenue giảm dần.
14. Đặt Date làm index và tính tổng Revenue theo tuần.
15. Tạo moving average 3 đơn vị thời gian của Revenue.
16. Tạo biểu đồ Revenue theo Date.
17. Viết từ 3-5 nhận xét về kết quả.

### Hint

Gợi ý: thực hiện tuần tự theo pipeline: inspect → datetime → missing → fill → Revenue → filter → groupby → pivot → sort → time index → resample/rolling → plot.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh

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
# Viết lời giải tại đây

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

**Nhận xét của sinh viên:**

-
-
-
-
-

### Kiểm tra tự động

```python
try:
    assert "Revenue" in sales.columns
    assert sales["Price"].isna().sum() == 0
    assert pd.api.types.is_datetime64_any_dtype(sales["Date"])
    assert sales["Revenue"].notna().all()
    print("Đạt yêu cầu cơ bản.")
except Exception as e:
    print("Chưa đạt:", e)
```

---

# PHẦN 10 - BÀI TỔNG HỢP MERGE

## Bài 35. Phân tích khách hàng và đơn hàng

Cho:

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

### Yêu cầu

1. Inner merge hai bảng.
2. Left merge từ `customers`.
3. Outer merge.
4. Xác định khách hàng chưa mua hàng.
5. Xác định đơn hàng không tìm thấy khách hàng.
6. Tính tổng Amount theo khách hàng.
7. Tính tổng Amount theo City.
8. Tìm khách hàng chi tiêu lớn nhất.
9. Tạo bảng gồm:
   - CustomerID;
   - Name;
   - TotalAmount.
10. Viết nhận xét ngắn.

### Hint

Gợi ý: merge trước, sau đó dùng `groupby()` trên Amount. Để giữ khách hàng chưa mua hàng, bắt đầu từ left merge với bảng customers.

### Câu lệnh chưa hoàn thiện

```python
# Gợi ý khung lệnh

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
# Viết lời giải tại đây

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

**Nhận xét của sinh viên:**

-
-
-

---

# TỰ ĐÁNH GIÁ SAU BÀI THỰC HÀNH

Đánh dấu các nội dung đã thực hiện được:

- [ ] Tạo được `Series` và `DataFrame`.
- [ ] Đọc được `shape`, `columns`, `index`, `dtypes`.
- [ ] Sử dụng được `head()`, `tail()`, `info()`, `describe()`.
- [ ] Phân biệt được `loc` và `iloc`.
- [ ] Lọc dữ liệu với một và nhiều điều kiện.
- [ ] Sắp xếp dữ liệu bằng `sort_values()`.
- [ ] Đọc và ghi CSV, Excel và JSON.
- [ ] Phát hiện dữ liệu thiếu bằng `isna()`.
- [ ] Xử lý missing values bằng `dropna()` và `fillna()`.
- [ ] Phát hiện và loại bỏ duplicate.
- [ ] Chuyển đổi kiểu dữ liệu.
- [ ] Làm sạch dữ liệu chuỗi.
- [ ] Tạo cột mới và áp dụng hàm.
- [ ] Thực hiện normalization và standardization.
- [ ] Dùng `groupby()` và `agg()`.
- [ ] Tạo pivot table.
- [ ] Dùng `pivot()` và `melt()`.
- [ ] Phân biệt `merge()` và `concat()`.
- [ ] Thực hiện inner, left, right và outer join.
- [ ] Tính correlation.
- [ ] Chuyển đổi dữ liệu datetime.
- [ ] Dùng `resample()` và `rolling()`.
- [ ] Tạo visualization nhanh bằng Pandas.
- [ ] Hoàn thành bài phân tích dữ liệu tổng hợp.
