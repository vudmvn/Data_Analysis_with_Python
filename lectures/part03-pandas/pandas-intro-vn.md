# Giới thiệu Pandas
**Ngôn ngữ:** Tiếng Việt  

**Chủ đề:** Thao tác, làm sạch, phân tích và xử lý dữ liệu dạng bảng với Pandas

---

## 1. Giới thiệu bài học
**Pandas** là một thư viện Python mã nguồn mở được thiết kế cho **thao tác và phân tích dữ liệu**. Pandas được xây dựng trên NumPy và cung cấp các cấu trúc dữ liệu cùng các hàm cấp cao để làm việc hiệu quả với dữ liệu có cấu trúc và dữ liệu dạng bảng.

Pandas đặc biệt hữu ích cho các công việc như:

- đọc dữ liệu từ các file CSV, Excel, JSON và văn bản;
- làm sạch và chuẩn bị tập dữ liệu;
- lọc và lựa chọn các quan sát;
- xử lý giá trị thiếu;
- biến đổi cột và kiểu dữ liệu;
- nhóm và tổng hợp dữ liệu;
- merge và join nhiều tập dữ liệu;
- reshape dữ liệu;
- tính các thống kê mô tả;
- phân tích dữ liệu chuỗi thời gian;
- tạo trực quan hóa nhanh.

Pandas xoay quanh hai cấu trúc dữ liệu chính:

- **Series**: mảng một chiều có nhãn;
- **DataFrame**: cấu trúc dạng bảng hai chiều có nhãn.

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

1. Kiến thức cơ bản
2. DataFrame
3. Series
4. Nhập và xuất dữ liệu (I/O)
5. Làm sạch dữ liệu
6. Các thao tác
7. Các thao tác nâng cao
8. Câu hỏi ôn tập
9. Bài tập thực hành
10. Đáp án và gợi ý trả lời

---

## 4. Điều kiện tiên quyết
Người học nên có:

- Kiến thức Python cơ bản.
- Quen thuộc với biến, list, dictionary, vòng lặp và hàm.
- Hiểu biết cơ bản về mảng NumPy.
- Có môi trường như Jupyter Notebook, JupyterLab, Google Colab, VS Code hoặc tương tự.

---

# Phần 1. Kiến thức cơ bản
## 1.1. Pandas là gì?
Pandas là thư viện Python dùng để làm việc với dữ liệu có cấu trúc. Nó cung cấp các công cụ để làm sạch, biến đổi, phân tích dữ liệu và tích hợp với các thư viện Khoa học dữ liệu khác.

Pandas được xây dựng trên NumPy, nghĩa là nó có thể tận dụng hiệu quả của mảng số trong khi bổ sung nhãn, chỉ mục và các thao tác hướng bảng.

Tên **Pandas** được bắt nguồn từ thuật ngữ **panel data**, thường được sử dụng trong kinh tế lượng.

## 1.2. Vì sao Pandas hữu ích?
Pandas thường được sử dụng để:

- đọc và ghi dữ liệu;
- làm sạch tập dữ liệu;
- xử lý giá trị thiếu;
- lựa chọn và lọc các quan sát;
- biến đổi biến;
- merge các tập dữ liệu;
- nhóm các quan sát;
- tính thống kê tổng hợp;
- chuẩn bị dữ liệu cho trực quan hóa và học máy.

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

## 1.4. Những điểm quan trọng
- **DataFrame** là cấu trúc hai chiều có nhãn, gồm hàng và cột.
- **Series** là mảng một chiều có nhãn.
- Pandas hoạt động chặt chẽ với NumPy, Matplotlib và Scikit-learn.
- Có thể xử lý giá trị thiếu bằng các phương thức như `.dropna()` và `.fillna()`.

## 1.5. Kiểm tra nhanh
**Câu 1.** Bí danh nào thường được sử dụng cho Pandas?

A. `pn`  
B. `pd`  
C. `ps`  
D. `pa`

**Câu 2.** Cấu trúc Pandas nào là hai chiều?

A. `Series`  
B. `tuple`  
C. `DataFrame`  
D. `ndarray`

## Bài tập
### Bài tập 1.1. Kiểm tra môi trường
Run:

```python
import pandas as pd

print(pd.__version__)
```

Record:

1. the Pandas version;
2. the standard Pandas alias;
3. one reason Pandas is useful in data analysis.

### Bài tập 1.2. Series hay DataFrame?
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

## 2.2. Các lệnh chính để tạo và kiểm tra DataFrame
| Lệnh | Ý nghĩa |
| --- | --- |
| `pd.DataFrame(data)` | Tạo DataFrame từ dictionary, list, mảng NumPy hoặc đối tượng tương tự. |
| `df.head()` | Hiển thị các hàng đầu. |
| `df.tail()` | Hiển thị các hàng cuối. |
| `df.shape` | Trả về số hàng và số cột. |
| `df.columns` | Trả về nhãn cột. |
| `df.index` | Trả về nhãn hàng. |
| `df.dtypes` | Trả về kiểu dữ liệu của các cột. |
| `df.info()` | Hiển thị tóm tắt cấu trúc của DataFrame. |
| `df.describe()` | Trả về thống kê mô tả cho các cột số. |

## 2.3. Kiểm tra DataFrame
```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
```

Sử dụng:

```python
df.info()
```

để kiểm tra:

- số hàng;
- số cột;
- tên cột;
- giá trị thiếu;
- kiểu dữ liệu.

## 2.4. Chỉ mục của DataFrame
Pandas tự gán chỉ mục số nguyên mặc định nếu không cung cấp index.

```python
print(df.index)
```

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

## 2.6. Truy xuất hàng bằng `loc` và `iloc`
`loc` selects data by **label**.

```python
print(df.loc["S01"])
```

`iloc` selects data by **integer position**.

```python
print(df.iloc[0])
```

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

## 2.8. Lọc DataFrame
Lọc hàng:

```python
selected = df[df["GPA"] >= 3.4]

print(selected)
```

## 2.9. Lọc với nhiều điều kiện
```python
selected = df[
    (df["Age"] >= 20) &
    (df["GPA"] >= 3.4)
]

print(selected)
```

Sử dụng:

- `&` cho AND;
- `|` cho OR;
- `~` cho NOT.

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

## 2.13. Kiểm tra nhanh
**Câu 1.** Lệnh nào tạo DataFrame?

A. `pd.DataFrame()`  
B. `pd.SeriesFrame()`  
C. `np.DataFrame()`  
D. `df.create()`

**Câu 2.** Bộ chọn nào dựa trên nhãn?

A. `iloc`  
B. `loc`  
C. `shape`  
D. `head`

## Bài tập
### Bài tập 2.1. Tạo DataFrame sinh viên
Tạo DataFrame với các cột:

- `StudentID`;
- `Name`;
- `Age`;
- `GPA`.

Use at least five students.

Then display:

1. ba hàng đầu;
2. the DataFrame shape;
3. the column names;
4. the column data types.

### Bài tập 2.2. `loc` và `iloc`
Sử dụng DataFrame sinh viên:

1. select the first row using `iloc`;
2. set `StudentID` as the index;
3. select one student using `loc`;
4. select only `Name` and `GPA`.

### Bài tập 2.3. Lọc dữ liệu
Filter students who:

1. have GPA greater than or equal to 3.5;
2. are at least 20 years old;
3. satisfy both conditions.

### Bài tập 2.4. Sắp xếp
Sắp xếp sinh viên:

1. by GPA ascending;
2. by GPA descending;
3. by Age ascending and GPA descending.

### Bài tập 2.5. Merge
Tạo một DataFrame khác gồm:

- `StudentID`;
- `Major`.

Merge nó với DataFrame sinh viên bằng `StudentID`.

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

Tạo Series với nhãn tùy chỉnh:

```python
s = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

print(s)
```

## 3.3. Các lệnh chính cho Series
| Lệnh | Ý nghĩa |
| --- | --- |
| `pd.Series(data)` | Tạo Series. |
| `s.index` | Trả về index của Series. |
| `s.values` | Trả về các giá trị bên dưới. |
| `s.dtype` | Trả về kiểu dữ liệu. |
| `s.loc[label]` | Truy xuất theo nhãn. |
| `s.iloc[position]` | Truy xuất theo vị trí số nguyên. |

## 3.4. Truy xuất phần tử
```python
print(s.loc["A"])
print(s.iloc[0])
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

Pandas căn chỉnh Series theo nhãn index trước khi thực hiện phép toán.

## 3.6. Tạo Series từ mảng NumPy
```python
import numpy as np

arr = np.array([5, 10, 15])
s = pd.Series(arr)

print(s)
```

## 3.7. Kiểm tra nhanh
**Câu 1.** Pandas Series là:

A. a two-dimensional table  
B. a one-dimensional labeled array  
C. a database server  
D. a plotting package

**Câu 2.** Thuộc tính nào trả về nhãn của Series?

A. `shape`  
B. `index`  
C. `columns`  
D. `describe`

## Bài tập
### Bài tập 3.1. Tạo Series
Tạo Series gồm năm mức giá sản phẩm, sử dụng ID sản phẩm làm nhãn index.

Then print:

1. the Series;
2. its index;
3. its values;
4. its data type.

### Bài tập 3.2. Truy xuất giá trị Series
Sử dụng Series từ Bài tập 3.1:

1. select one value using `loc`;
2. select one value using `iloc`;
3. explain the difference.

### Bài tập 3.3. Căn chỉnh Series
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

Giải thích vì sao một số vị trí chứa giá trị thiếu.

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

Useful options:

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
| Lệnh | Vai trò |
| --- | --- |
| `pd.read_csv()` | Đọc file CSV hoặc file văn bản có dấu phân cách. |
| `df.to_csv()` | Ghi file CSV. |
| `pd.read_excel()` | Đọc file Excel. |
| `df.to_excel()` | Ghi file Excel. |
| `pd.read_json()` | Đọc file JSON. |
| `df.to_json()` | Ghi file JSON. |

## 4.10. Kiểm tra nhanh
**Câu 1.** Hàm nào đọc file CSV?

A. `pd.read_csv()`  
B. `pd.open_csv()`  
C. `pd.load_table_only()`  
D. `df.csv_read()`

**Câu 2.** Tham số nào thường được dùng để không xuất index của DataFrame?

A. `index=False`  
B. `index=True`  
C. `header=None`  
D. `drop_index=True`

## Bài tập
### Bài tập 4.1. CSV
Tạo DataFrame có ít nhất năm hàng và lưu thành:

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

- giá trị thiếu;
- các hàng trùng lặp;
- inconsistent data types;
- các cột rỗng;
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

## 5.3. Loại bỏ giá trị thiếu
Loại bỏ các hàng chứa giá trị thiếu:

```python
clean_df = df.dropna()
```

Loại bỏ các cột chứa giá trị thiếu:

```python
clean_df = df.dropna(axis=1)
```

## 5.4. Điền giá trị thiếu
Điền tất cả giá trị thiếu:

```python
filled = df.fillna(0)
```

Điền giá trị thiếu của một cột bằng trung bình:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

Điền biến phân loại:

```python
df["City"] = df["City"].fillna(
    "Unknown"
)
```

## 5.5. Loại bỏ dữ liệu trùng lặp
Phát hiện trùng lặp:

```python
print(df.duplicated())
```

Loại bỏ các hàng trùng:

```python
df = df.drop_duplicates()
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

Chuyển chuỗi thành giá trị số:

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

Các giá trị không hợp lệ được chuyển thành `NaN`, sau đó có thể được xử lý rõ ràng.

## 5.10. Các lệnh làm sạch dữ liệu chính
| Lệnh | Ý nghĩa |
| --- | --- |
| `df.isna()` | Phát hiện giá trị thiếu. |
| `df.isna().sum()` | Đếm giá trị thiếu. |
| `df.dropna()` | Loại bỏ quan sát bị thiếu. |
| `df.fillna(value)` | Thay thế giá trị thiếu. |
| `df.duplicated()` | Phát hiện trùng lặp. |
| `df.drop_duplicates()` | Loại bỏ các hàng trùng lặp. |
| `df.astype(type)` | Chuyển đổi kiểu dữ liệu. |
| `pd.to_numeric()` | Chuyển giá trị sang dạng số. |
| `df.drop()` | Xóa hàng hoặc cột. |
| `Series.str.*` | Áp dụng các phương thức xử lý chuỗi. |

## 5.11. Kiểm tra nhanh
**Câu 1.** Phương thức nào loại bỏ các hàng chứa giá trị thiếu?

A. `dropna()`  
B. `fillna()`  
C. `duplicated()`  
D. `astype()`

**Câu 2.** Phương thức nào loại bỏ các hàng trùng?

A. `drop_duplicates()`  
B. `dropna()`  
C. `sort_values()`  
D. `merge()`

## Bài tập
### Bài tập 5.1. Giá trị thiếu
Create:

```python
df = pd.DataFrame({
    "Name": ["An", "Binh", "Chi", "Dung"],
    "Age": [20, None, 22, 21],
    "GPA": [3.2, 3.6, None, 3.8]
})
```

Do the following:

1. xác định giá trị thiếu;
2. đếm giá trị thiếu theo cột;
3. fill missing `Age` values using the column mean;
4. fill missing `GPA` values using the column median.

### Bài tập 5.2. Dữ liệu trùng lặp
Add a duplicated row to a DataFrame.

Then:

1. detect duplicates;
2. count duplicates;
3. remove them.

### Bài tập 5.3. Kiểu dữ liệu
Create:

```python
df = pd.DataFrame({
    "Price": ["10", "20", "unknown", "40"]
})
```

Chuyển `Price` sang numeric bằng:

```python
pd.to_numeric(..., errors="coerce")
```

Giải thích điều gì xảy ra với `"unknown"`.

### Bài tập 5.4. Làm sạch chuỗi
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

## 6.5. Nhóm dữ liệu bằng `groupby()`
```python
summary = df.groupby(
    "Region"
)["Sales"].mean()

print(summary)
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
| Lệnh | Ý nghĩa |
| --- | --- |
| `df["new"] = ...` | Tạo hoặc biến đổi cột. |
| `Series.map()` | Ánh xạ giá trị sang giá trị mới. |
| `Series.apply()` | Áp dụng hàm cho các phần tử Series. |
| `df.describe()` | Thống kê mô tả. |
| `df.groupby()` | Nhóm các quan sát. |
| `.agg()` | Áp dụng nhiều hàm tổng hợp. |
| `pd.merge()` | Merge các DataFrame. |
| `pd.concat()` | Ghép nối các DataFrame. |
| `df.pivot()` | Chuyển dữ liệu dạng long sang wide. |
| `pd.melt()` | Chuyển dữ liệu dạng wide sang long. |
| `pd.pivot_table()` | Tạo pivot table tổng hợp. |

## 6.11. Kiểm tra nhanh
**Câu 1.** Phương thức nào nhóm các quan sát theo nhóm phân loại?

A. `groupby()`  
B. `dropna()`  
C. `astype()`  
D. `sort_index()`

**Câu 2.** Hàm nào kết hợp DataFrame bằng cột khóa?

A. `pd.merge()`  
B. `pd.mean()`  
C. `pd.reshape()`  
D. `pd.filter_rows()`

## Bài tập
### Bài tập 6.1. Tạo cột tính toán
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

### Bài tập 6.2. Chuẩn hóa dữ liệu
Tạo một cột số và tính:

1. min-max normalization;
2. z-score standardization.

### Bài tập 6.3. Nhóm và tổng hợp
Tạo DataFrame doanh số gồm:

- Region;
- Product;
- Sales.

Calculate:

1. total sales by Region;
2. doanh số trung bình theo Region;
3. count, sum và mean bằng `.agg()`.

### Bài tập 6.4. Merge
Create:

```text
customers(CustomerID, Name)
orders(OrderID, CustomerID, Amount)
```

Perform:

1. inner merge;
2. left merge.

Giải thích sự khác nhau.

### Bài tập 6.5. Pivot Table
Tạo pivot table với:

- hàng: Region;
- cột: Product;
- values: Sales;
- aggregation: sum.

---

# Phần 7. Các thao tác nâng cao
## 7.1. Tương quan
Tương quan đo lường mức độ liên hệ giữa các biến số.

```python
print(df.corr(
    numeric_only=True
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

## 7.4. Trích xuất thành phần ngày tháng
```python
df["Year"] = df.index.year
df["Month"] = df.index.month
df["Day"] = df.index.day
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
| Lệnh | Ý nghĩa |
| --- | --- |
| `df.corr()` | Tính ma trận tương quan. |
| `Series.corr()` | Tính tương quan giữa hai Series. |
| `df.plot()` | Tạo trực quan hóa nhanh. |
| `pd.to_datetime()` | Chuyển giá trị sang datetime. |
| `df.set_index()` | Đặt một cột làm index. |
| `df.resample()` | Tổng hợp dữ liệu chuỗi thời gian theo khoảng thời gian. |
| `Series.rolling()` | Tính thống kê theo cửa sổ rolling. |

## 7.8. Kiểm tra nhanh
**Câu 1.** Hàm nào chuyển một cột sang datetime?

A. `pd.to_datetime()`  
B. `pd.date_convert_only()`  
C. `df.datetime()`  
D. `pd.time_series()`

**Câu 2.** Phương thức nào tính ma trận tương quan?

A. `corr()`  
B. `merge()`  
C. `dropna()`  
D. `pivot()`

## Bài tập
### Bài tập 7.1. Tương quan
Create:

```python
df = pd.DataFrame({
    "Advertising": [10, 20, 30, 40, 50],
    "Sales": [100, 120, 150, 170, 210]
})
```

Calculate:

1. toàn bộ ma trận tương quan;
2. tương quan giữa `Advertising` và `Sales`.

### Bài tập 7.2. Trực quan hóa
Sử dụng DataFrame doanh số, tạo:

1. a line chart;
2. a bar chart;
3. a histogram;
4. a scatter plot.

### Bài tập 7.3. Index chuỗi thời gian
Tạo DataFrame với các cột:

- `Date`;
- `Sales`.

Then:

1. convert `Date` to datetime;
2. set `Date` as index;
3. sort by date.

### Bài tập 7.4. Resampling
Sử dụng dữ liệu doanh số hằng ngày:

1. calculate weekly total sales;
2. calculate monthly average sales.

### Bài tập 7.5. Trung bình trượt
Tính trung bình trượt 3 kỳ cho Series `Sales`.

---

# Phần 8. Câu hỏi ôn tập
## 8.1. Câu hỏi trắc nghiệm
**Câu 1.** Mục đích chính của Pandas là gì?

A. Thao tác và phân tích dữ liệu  
B. Quản trị hệ điều hành  
C. Quản lý web server  
D. Chỉ đồ họa máy tính

**Câu 2.** Cấu trúc Pandas nào là một chiều?

A. `DataFrame`  
B. `Series`  
C. `ndarray` only  
D. `pivot`

**Câu 3.** Bộ chọn nào dựa trên vị trí số nguyên?

A. `loc`  
B. `iloc`  
C. `index`  
D. `columns`

**Câu 4.** Hàm nào đọc file CSV?

A. `pd.read_csv()`  
B. `pd.csv_open()`  
C. `pd.load_csv_only()`  
D. `df.read()`

**Câu 5.** Phương thức nào thay thế giá trị thiếu?

A. `fillna()`  
B. `drop_duplicates()`  
C. `sort_values()`  
D. `merge()`

**Câu 6.** Phương thức nào loại bỏ các hàng trùng?

A. `drop_duplicates()`  
B. `fillna()`  
C. `groupby()`  
D. `pivot()`

**Câu 7.** Phương thức nào nhóm các quan sát?

A. `groupby()`  
B. `describe()`  
C. `drop()`  
D. `astype()`

**Câu 8.** Hàm nào merge hai DataFrame bằng khóa chung?

A. `pd.merge()`  
B. `pd.mean()`  
C. `pd.Series()`  
D. `pd.plot()`

**Câu 9.** Hàm nào chuyển giá trị sang datetime?

A. `pd.to_datetime()`  
B. `pd.to_numeric()`  
C. `pd.read_date()`  
D. `pd.datetime_only()`

**Câu 10.** Phương thức nào tính tương quan?

A. `corr()`  
B. `join()`  
C. `head()`  
D. `fillna()`

## 8.2. Câu hỏi Đúng/Sai
**Câu 1.** DataFrame là cấu trúc hai chiều.  
**Câu 2.** Series là mảng một chiều có nhãn.  
**Câu 3.** `loc` chỉ dựa trên vị trí số nguyên.  
**Câu 4.** `iloc` dựa trên vị trí.  
**Câu 5.** Có thể dùng `dropna()` để loại bỏ giá trị thiếu.  
**Câu 6.** `fillna()` có thể thay thế giá trị thiếu.  
**Câu 7.** Có thể kết hợp `groupby()` với các hàm tổng hợp.  
**Câu 8.** `pd.merge()` có thể thực hiện inner join và left join.  
**Câu 9.** `pd.to_datetime()` có thể chuyển ngày dạng văn bản sang datetime.  
**Câu 10.** Tương quan tự động chứng minh quan hệ nhân quả.

## 8.3. Câu hỏi trả lời ngắn
**Câu 1.** Giải thích sự khác nhau giữa Series và DataFrame.

**Câu 2.** Giải thích sự khác nhau giữa `loc` và `iloc`.

**Câu 3.** Nêu hai phương thức xử lý giá trị thiếu.

**Câu 4.** Giải thích sự khác nhau giữa `pd.concat()` và `pd.merge()`.

**Câu 5.** Mục đích của `groupby()` là gì?

**Câu 6.** Vì sao chuyển đổi kiểu dữ liệu quan trọng trong làm sạch dữ liệu?

**Câu 7.** Giải thích chức năng của pivot table.

**Câu 8.** Nêu một ứng dụng của `pd.to_datetime()`.

---

# Phần 9. Bài tập thực hành
## Bài tập 1. Dữ liệu sinh viên
Tạo DataFrame có ít nhất 10 sinh viên gồm:

- StudentID;
- Name;
- Age;
- Major;
- GPA.

Perform:

1. inspection with `head()`, `shape`, `info()`, and `describe()`;
2. filtering for GPA >= 3.5;
3. sorting by GPA descending;
4. chọn hàng bằng `loc` và `iloc`.

## Bài tập 2. Dữ liệu thiếu
Thêm giá trị thiếu vào tập dữ liệu sinh viên.

Then:

1. đếm giá trị thiếu;
2. điền Age bị thiếu bằng Age trung bình;
3. điền GPA bị thiếu bằng GPA trung vị;
4. loại bỏ các hàng có Name bị thiếu.

## Bài tập 3. CSV và Excel
Export the cleaned student dataset to:

```text
students.csv
students.xlsx
```

Đọc lại cả hai file bằng Pandas.

## Bài tập 4. Phân tích doanh số
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

## Bài tập 5. Merge
Tạo bảng khách hàng:

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

## Bài tập 6. Làm sạch dữ liệu
Tạo tập dữ liệu chưa sạch gồm:

- giá trị thiếu;
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

## Bài tập 7. Chuỗi thời gian
Tạo dữ liệu doanh số hằng ngày trong ít nhất 30 ngày.

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
**Câu 1.** Series là mảng một chiều có nhãn, trong khi DataFrame là bảng hai chiều có nhãn gồm hàng và cột.

**Câu 2.** `loc` chọn các quan sát bằng nhãn, trong khi `iloc` chọn bằng vị trí số nguyên.

**Câu 3.** Có thể loại bỏ giá trị thiếu bằng `dropna()` hoặc thay thế bằng `fillna()`.

**Câu 4.** `pd.concat()` kết hợp DataFrame theo một trục, trong khi `pd.merge()` kết hợp chúng bằng các cột khóa khớp nhau.

**Câu 5.** `groupby()` chia dữ liệu thành các nhóm dựa trên giá trị phân loại để có thể áp dụng phép tổng hợp hoặc biến đổi cho từng nhóm.

**Câu 6.** Kiểu dữ liệu đúng là cần thiết để thực hiện hợp lệ các phép toán số, so sánh, sắp xếp, tổng hợp và mô hình hóa.

**Câu 7.** Pivot table tóm tắt một biến số theo một hoặc nhiều chiều phân loại.

**Câu 8.** `pd.to_datetime()` chuyển chuỗi hoặc giá trị dạng ngày thành đối tượng datetime của Pandas để có thể thực hiện các thao tác theo thời gian.

---

# Lời giải gợi ý cho một số bài thực hành
## Bài tập 1. Dữ liệu sinh viên
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

## Bài tập 2. Dữ liệu thiếu
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

## Bài tập 3. CSV và Excel
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

## Bài tập 4. Phân tích doanh số
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

## Bài tập 5. Merge
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

## Bài tập 6. Làm sạch dữ liệu
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

## Bài tập 7. Chuỗi thời gian
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