# Truy xuất và Lưu trữ Dữ liệu với Python

**Ngôn ngữ:** Tiếng Việt  
**Chủ đề:** Truy xuất, nhập, tích hợp và lưu trữ dữ liệu phục vụ phân tích dữ liệu với Python

---

## 1. Giới thiệu bài học

Trong một dự án Khoa học dữ liệu (Data Science) hoặc Học máy (Machine Learning), dữ liệu hiếm khi có sẵn dưới dạng một DataFrame hoàn chỉnh và sẵn sàng cho phân tích. Dữ liệu thường được phân tán ở nhiều nguồn và được lưu trữ dưới nhiều định dạng khác nhau.

Các nguồn dữ liệu phổ biến bao gồm:

- tệp CSV và các tệp văn bản có dấu phân cách;
- bảng tính Microsoft Excel;
- dữ liệu JSON từ Web API;
- các bảng HTML trên website;
- báo cáo và tài liệu PDF;
- cơ sở dữ liệu quan hệ;
- cơ sở dữ liệu NoSQL.

Do đó, trước khi thực hiện trực quan hóa, phân tích thống kê hoặc xây dựng mô hình Machine Learning, người phân tích cần biết cách:

- xác định và truy xuất nguồn dữ liệu;
- đọc dữ liệu vào môi trường Python;
- kiểm tra cấu trúc và chất lượng dữ liệu;
- chuyển đổi dữ liệu về định dạng phù hợp;
- tích hợp dữ liệu từ nhiều nguồn;
- lưu trữ dữ liệu và kết quả phân tích để phục vụ các bước tiếp theo.

Một quy trình Machine Learning điển hình có thể được mô tả như sau:

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

Bài học này tập trung chủ yếu vào ba nhóm công việc:

```text
Obtain Data
    +
Prepare Data
    +
Store Data
```

Đây là những bước nền tảng để chuyển dữ liệu thô thành dữ liệu có thể sử dụng cho phân tích, trực quan hóa và xây dựng mô hình.

---

## 2. Mục tiêu học tập

Sau khi hoàn thành bài học này, người học có thể:

- Giải thích vai trò của truy xuất dữ liệu (Data Access) và lưu trữ dữ liệu (Data Storage) trong quy trình Data Science.
- Phân biệt các nguồn và định dạng dữ liệu phổ biến.
- Đọc và ghi dữ liệu CSV bằng NumPy.
- Đọc và ghi dữ liệu CSV bằng Pandas.
- Sử dụng các tham số quan trọng của `pd.read_csv()`.
- Xử lý tệp CSV dung lượng lớn bằng `chunksize`.
- Đọc và ghi dữ liệu Excel với một hoặc nhiều trang tính.
- Đọc dữ liệu JSON.
- Chuyển dữ liệu JSON lồng nhau sang dạng bảng bằng `pd.json_normalize()`.
- Trích xuất bảng HTML bằng `pd.read_html()`.
- Giải thích những khó khăn khi trích xuất bảng từ tài liệu PDF.
- Kết nối và truy vấn cơ sở dữ liệu SQLite bằng Python.
- Chuyển đổi dữ liệu hai chiều giữa cơ sở dữ liệu SQL và Pandas DataFrame.
- Giải thích cấu trúc dữ liệu dạng tài liệu (document) của MongoDB.
- Thực hiện các thao tác CRUD cơ bản với PyMongo.
- Chuyển dữ liệu từ MongoDB sang Pandas DataFrame.
- Xây dựng một pipeline tích hợp dữ liệu từ nhiều nguồn.
- Lựa chọn định dạng lưu trữ phù hợp với từng yêu cầu phân tích.

---

## 3. Cấu trúc bài học

Bài học được tổ chức thành các phần sau:

1. Tổng quan về truy xuất và lưu trữ dữ liệu
2. Làm việc với CSV bằng NumPy
3. Làm việc với CSV bằng Pandas
4. Làm việc với Microsoft Excel
5. Làm việc với JSON
6. Truy xuất dữ liệu từ HTML và PDF
7. Làm việc với cơ sở dữ liệu SQLite
8. Làm việc với MongoDB và PyMongo
9. Xây dựng Data Pipeline tích hợp dữ liệu đa nguồn
10. Các nguyên tắc thực hành tốt

Trong mỗi phần, nội dung lý thuyết được kết hợp với ví dụ minh họa, bài tập thực hành và câu hỏi kiểm tra kiến thức.

---

## 4. Điều kiện tiên quyết

Để học hiệu quả nội dung này, người học nên có:

- kiến thức Python cơ bản;
- hiểu cách sử dụng biến, danh sách, dictionary, vòng lặp và hàm;
- kiến thức cơ bản về NumPy;
- kiến thức cơ bản về Pandas DataFrame;
- hiểu khái niệm hàng, cột và bảng dữ liệu;
- khả năng sử dụng Jupyter Notebook, JupyterLab, Google Colab, VS Code hoặc môi trường Python tương đương.

---

# Phần 1. Tổng quan về truy xuất và lưu trữ dữ liệu

## 1.1. Truy xuất dữ liệu là gì?

**Truy xuất dữ liệu (Data Access)** là quá trình lấy dữ liệu từ một nguồn lưu trữ và đưa dữ liệu vào môi trường phân tích.

Ví dụ, dữ liệu khách hàng được lưu trong tệp CSV có thể được đọc vào Pandas DataFrame:

```text
customers.csv
      ↓
pd.read_csv()
      ↓
DataFrame
```

Tương tự, dữ liệu trong cơ sở dữ liệu có thể được truy vấn bằng SQL trước khi chuyển sang DataFrame:

```text
SQL Database
      ↓
SQL Query
      ↓
Pandas DataFrame
```

---

## 1.2. Lưu trữ dữ liệu là gì?

**Lưu trữ dữ liệu (Data Storage)** là quá trình ghi dữ liệu hoặc kết quả phân tích vào một định dạng hoặc hệ thống lưu trữ để có thể sử dụng lại.

Ví dụ:

```text
DataFrame
    ↓
to_csv()
    ↓
report.csv
```

Hoặc:

```text
DataFrame
    ↓
to_sql()
    ↓
Database Table
```

---

## 1.3. Các nguồn dữ liệu phổ biến

| Nhóm dữ liệu | Ví dụ |
|---|---|
| Tệp phẳng (Flat files) | CSV, TSV |
| Bảng tính (Spreadsheet) | Excel |
| Dữ liệu bán cấu trúc | JSON |
| Dữ liệu Web | HTML |
| Tài liệu | PDF |
| Cơ sở dữ liệu quan hệ | SQLite, PostgreSQL, MySQL |
| Cơ sở dữ liệu NoSQL | MongoDB |

---

## 1.4. Dữ liệu có cấu trúc và dữ liệu bán cấu trúc

Dữ liệu dạng bảng như sau:

```text
CustomerID | Name | City | Revenue
```

có cấu trúc rõ ràng theo hàng và cột, do đó được gọi là **dữ liệu có cấu trúc (structured data)**.

Trong khi đó, JSON có thể chứa các đối tượng và danh sách lồng nhau:

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

Loại dữ liệu này có cấu trúc linh hoạt và mang tính phân cấp, thường được xếp vào nhóm **dữ liệu bán cấu trúc (semi-structured data)**.

### Bài tập

Phân loại các nguồn dữ liệu sau vào nhóm phù hợp:

1. `sales.csv`
2. `customers.xlsx`
3. Dữ liệu JSON được trả về từ Web API
4. `company.db`
5. MongoDB
6. Báo cáo tài chính dạng PDF

Các nhóm cần sử dụng gồm:

- tệp phẳng;
- bảng tính;
- dữ liệu bán cấu trúc;
- cơ sở dữ liệu quan hệ;
- cơ sở dữ liệu NoSQL;
- tài liệu.

### Kiểm tra kiến thức

**Câu 1.** Định dạng nào sau đây thường được xem là tệp phẳng?

A. CSV  
B. MongoDB  
C. SQLite  
D. PDF

**Câu 2.** Định dạng nào hỗ trợ tự nhiên các đối tượng và danh sách lồng nhau?

A. JSON  
B. CSV  
C. TSV  
D. Ma trận số

### Bài tập thực hành 1

Xét tình huống sau:

> Một doanh nghiệp lưu thông tin khách hàng trong CSV, danh mục sản phẩm trong Excel, đơn hàng trực tuyến dưới dạng JSON từ Web API và dữ liệu nhân viên trong SQLite.

Thực hiện các yêu cầu sau:

1. Xác định loại dữ liệu của từng nguồn.
2. Đề xuất hàm hoặc thư viện Python phù hợp để đọc từng nguồn.
3. Đề xuất một định dạng phù hợp để lưu bảng dữ liệu phân tích cuối cùng và giải thích lựa chọn của bạn.

---

# Phần 2. Làm việc với CSV bằng NumPy

## 2.1. Đọc dữ liệu bằng `np.loadtxt()`

Hàm `np.loadtxt()` phù hợp với các tệp dữ liệu có đặc điểm:

- chủ yếu chứa dữ liệu số;
- có cấu trúc đơn giản;
- không chứa hoặc chỉ chứa rất ít giá trị thiếu.

Ví dụ:

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

Có thể tính giá trị trung bình của từng cột bằng:

```python
print(
    np.mean(data, axis=0)
)
```

### Bài tập — `np.loadtxt()`

Hoàn thiện đoạn chương trình sau để đọc dữ liệu từ `sales.csv`, trong đó các giá trị được phân cách bằng dấu phẩy:

```python
# data = np.loadtxt(
#     "sales.csv",
#     delimiter=...
# )

# print(data.shape)
```

Sau khi chạy chương trình, xác định số hàng và số cột của dữ liệu.

---

## 2.2. Xử lý giá trị thiếu bằng `np.genfromtxt()`

So với `np.loadtxt()`, hàm `np.genfromtxt()` linh hoạt hơn khi dữ liệu chứa giá trị thiếu.

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

Trong ví dụ trên, các ô dữ liệu thiếu được thay bằng `0.0`.

### Bài tập — `np.genfromtxt()`

Đọc dữ liệu từ `temperature.csv` và thay mọi giá trị thiếu bằng `-1`.

```python
# data = np.genfromtxt(
#     "temperature.csv",
#     delimiter=",",
#     skip_header=1,
#     filling_values=...
# )
```

Sau đó, in dữ liệu để kiểm tra kết quả.

---

## 2.3. Ghi dữ liệu bằng `np.savetxt()`

Hàm `np.savetxt()` cho phép lưu một mảng NumPy vào tệp văn bản.

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

Trong đó, `fmt="%.2f"` quy định mỗi số được ghi với hai chữ số sau dấu thập phân.

### Bài tập — `np.savetxt()`

Cho mảng:

```python
arr = np.array([
    [10.234, 20.567],
    [30.456, 40.123],
    [50.789, 60.345]
])
```

Hãy lưu mảng trên vào tệp:

```text
numeric_output.csv
```

với các yêu cầu:

- các giá trị được phân cách bằng dấu phẩy;
- mỗi giá trị được ghi với hai chữ số sau dấu thập phân;
- hai cột có tiêu đề `A` và `B`.

---

## 2.4. Các hàm chính

| Hàm | Công dụng |
|---|---|
| `np.loadtxt()` | Đọc dữ liệu số từ tệp văn bản có cấu trúc đơn giản |
| `np.genfromtxt()` | Đọc dữ liệu số và hỗ trợ xử lý giá trị thiếu |
| `np.savetxt()` | Ghi mảng NumPy ra tệp văn bản |

### Kiểm tra kiến thức

**Câu 1.** Hàm nào phù hợp hơn khi tệp dữ liệu số có giá trị thiếu?

A. `np.genfromtxt()`  
B. `np.mean()`  
C. `np.arange()`  
D. `np.reshape()`

**Câu 2.** Hàm nào dùng để ghi một mảng NumPy ra tệp văn bản?

A. `np.savetxt()`  
B. `np.savecsv()`  
C. `np.write()`  
D. `np.export()`

### Bài tập thực hành 2

Tạo tệp `monthly_sales.csv` với nội dung:

```text
Month,Revenue,Cost
1,120,80
2,150,
3,180,110
4,,130
```

Thực hiện:

1. Đọc dữ liệu bằng `np.genfromtxt()`.
2. Thay các giá trị thiếu bằng `0`.
3. Tính giá trị trung bình của `Revenue` và `Cost`.
4. Lưu dữ liệu sau xử lý vào một tệp CSV mới bằng `np.savetxt()`.

---

# Phần 3. Làm việc với CSV bằng Pandas

## 3.1. Đọc CSV bằng `pd.read_csv()`

Pandas cung cấp hàm `pd.read_csv()` để đọc dữ liệu dạng bảng từ tệp CSV.

```python
import pandas as pd

df = pd.read_csv(
    "customers.csv"
)

print(df.head())
```

Pandas đặc biệt phù hợp khi dữ liệu chứa:

- chuỗi văn bản;
- ngày và thời gian;
- nhiều kiểu dữ liệu khác nhau;
- giá trị thiếu;
- tên cột và chỉ mục.

### Bài tập — `pd.read_csv()`

Đọc tệp `students.csv` vào DataFrame có tên `students`.

```python
# students = pd.read_csv(...)
```

Sau đó hiển thị năm dòng đầu tiên.

---

## 3.2. Xác định ký tự phân cách bằng `sep`

Không phải mọi tệp dữ liệu đều sử dụng dấu phẩy làm ký tự phân cách.

Ví dụ, tệp sử dụng dấu chấm phẩy:

```python
df = pd.read_csv(
    "data.csv",
    sep=";"
)
```

Với tệp TSV, các trường thường được phân cách bằng ký tự tab:

```python
df = pd.read_csv(
    "data.tsv",
    sep="\t"
)
```

### Bài tập — `sep`

Đọc tệp `sales_semicolon.csv`, trong đó các trường được phân cách bằng dấu `;`.

```python
# df = pd.read_csv(
#     "sales_semicolon.csv",
#     sep=...
# )
```

---

## 3.3. Chỉ đọc các cột cần thiết bằng `usecols`

Tham số `usecols` cho phép lựa chọn các cột cần đọc ngay trong quá trình nhập dữ liệu.

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

Việc chỉ đọc các cột cần thiết có thể:

- giảm lượng bộ nhớ RAM sử dụng;
- rút ngắn thời gian đọc dữ liệu;
- loại bỏ sớm các biến không cần thiết cho bài toán phân tích.

### Bài tập — `usecols`

Đọc tệp `orders.csv` nhưng chỉ lấy ba cột:

```text
OrderID
CustomerID
Amount
```

---

## 3.4. Xác định kiểu dữ liệu bằng `dtype`

Pandas có thể tự suy luận kiểu dữ liệu, nhưng trong nhiều trường hợp người phân tích cần quy định kiểu dữ liệu một cách tường minh.

```python
df = pd.read_csv(
    "customers.csv",
    dtype={
        "customer_id": str,
        "age": "Int64"
    }
)
```

Các trường như:

- CustomerID;
- StudentID;
- ProductID;
- PostalCode;

thường đóng vai trò là mã định danh, không phải đại lượng số học. Vì vậy, lưu chúng dưới dạng chuỗi thường phù hợp hơn.

### Bài tập — `dtype`

Đọc `students.csv` với các yêu cầu:

```text
StudentID → str
Age → Int64
```

Sau đó sử dụng `dtypes` để kiểm tra kết quả.

---

## 3.5. Chuyển dữ liệu ngày tháng bằng `parse_dates`

Có thể yêu cầu Pandas chuyển trực tiếp một hoặc nhiều cột sang kiểu ngày tháng khi đọc dữ liệu.

```python
df = pd.read_csv(
    "orders.csv",
    parse_dates=["OrderDate"]
)
```

Kiểm tra kiểu dữ liệu bằng:

```python
print(df.dtypes)
```

### Bài tập — `parse_dates`

Đọc `sales.csv` và chuyển cột `Date` sang kiểu datetime ngay trong quá trình nhập dữ liệu.

---

## 3.6. Xác định giá trị thiếu bằng `na_values`

Trong dữ liệu thực tế, giá trị thiếu có thể được biểu diễn bằng nhiều ký hiệu khác nhau.

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

Pandas sẽ chuyển các ký hiệu này thành giá trị thiếu chuẩn.

### Bài tập — `na_values`

Đọc một tệp trong đó ba ký hiệu sau đều được xem là giá trị thiếu:

```text
NULL
?
-
```

Sau khi đọc, sử dụng `isna().sum()` để kiểm tra số lượng giá trị thiếu của từng cột.

---

## 3.7. Mã hóa ký tự

Khi làm việc với dữ liệu tiếng Việt, UTF-8 là lựa chọn phổ biến.

```python
df = pd.read_csv(
    "customers.csv",
    encoding="utf-8"
)
```

Khi xuất CSV để mở bằng Microsoft Excel trên Windows, có thể sử dụng:

```python
df.to_csv(
    "customers_clean.csv",
    index=False,
    encoding="utf-8-sig"
)
```

---

## 3.8. Kiểm tra dữ liệu sau khi nhập

Sau khi đọc dữ liệu, nên kiểm tra ngay cấu trúc và chất lượng của DataFrame.

Các lệnh thường sử dụng gồm:

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

Các lệnh trên giúp xác định:

- số hàng và số cột;
- tên cột;
- kiểu dữ liệu;
- số giá trị không thiếu;
- số lượng giá trị thiếu.

### Bài tập

Hoàn thiện các lệnh dưới đây để kiểm tra DataFrame `df`:

```python
# print(df.head())
# print(df....)
# df....
# print(df.isna().sum())
```

Sau đó xác định:

1. Số hàng của DataFrame.
2. Số cột của DataFrame.
3. Kiểu dữ liệu của từng cột.
4. Số lượng giá trị thiếu theo từng cột.

---

## 3.9. Đọc dữ liệu lớn bằng `chunksize`

Khi tệp CSV có dung lượng lớn hơn bộ nhớ khả dụng, việc đọc toàn bộ dữ liệu vào một DataFrame có thể không khả thi.

Tham số `chunksize` cho phép đọc dữ liệu theo từng khối:

```python
chunks = pd.read_csv(
    "transactions.csv",
    chunksize=100000
)
```

Có thể duyệt qua từng khối dữ liệu:

```python
for chunk in chunks:
    print(chunk.shape)
```

Ví dụ tính tổng doanh thu mà không cần đưa toàn bộ tệp vào RAM:

```python
total = 0

for chunk in pd.read_csv(
    "transactions.csv",
    chunksize=100000
):
    total += chunk["Amount"].sum()

print(total)
```

### Bài tập — `chunksize`

Hoàn thiện chương trình để tính tổng cột `Sales` của `large_sales.csv`, trong đó dữ liệu được đọc theo từng khối 50.000 dòng.

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

## 3.10. Ghi DataFrame ra CSV

Sử dụng phương thức `to_csv()`:

```python
df.to_csv(
    "clean_data.csv",
    index=False,
    encoding="utf-8-sig"
)
```

`index=False` ngăn Pandas ghi chỉ mục của DataFrame thành một cột bổ sung trong tệp.

---

## 3.11. Các tham số và hàm chính

| Hàm hoặc tham số | Công dụng |
|---|---|
| `pd.read_csv()` | Đọc CSV hoặc tệp văn bản có dấu phân cách |
| `usecols=` | Chỉ đọc các cột cần thiết |
| `dtype=` | Quy định kiểu dữ liệu |
| `parse_dates=` | Chuyển các cột sang kiểu ngày tháng |
| `na_values=` | Xác định các ký hiệu biểu diễn giá trị thiếu |
| `chunksize=` | Đọc dữ liệu theo từng khối |
| `df.to_csv()` | Ghi DataFrame ra CSV |

### Kiểm tra kiến thức

**Câu 1.** Tham số nào cho phép chỉ đọc một số cột được lựa chọn?

A. `usecols`  
B. `keepcols`  
C. `columns_only`  
D. `filter_columns`

**Câu 2.** Tham số nào đặc biệt hữu ích khi xử lý tệp CSV rất lớn?

A. `chunksize`  
B. `batch=True`  
C. `split=True`  
D. `large=True`

**Câu 3.** Vì sao một cột ID thường nên được đọc dưới dạng `str`?

A. Vì nó biểu diễn mã định danh chứ không phải đại lượng số học.  
B. Để có thể tính trung bình.  
C. Để biến nó thành biến liên tục.  
D. Để làm tăng giá trị của trường ID.

### Bài tập thực hành 3

Tạo một tệp `customers.csv` gồm các cột:

- CustomerID;
- Name;
- City;
- Age;
- SignupDate;
- TotalSpent.

Trong dữ liệu, chủ động đưa vào:

- một số giá trị `NA`;
- một số giá trị `-`;
- các CustomerID có dạng `001`, `002`, ...

Thực hiện:

1. Đọc `CustomerID` dưới dạng `str`.
2. Chuyển `SignupDate` sang datetime trong quá trình đọc.
3. Xem `NA` và `-` là giá trị thiếu.
4. Chỉ đọc năm cột cần thiết cho phân tích.
5. Kiểm tra dữ liệu bằng `head()`, `shape`, `info()` và `isna().sum()`.
6. Xuất kết quả sang `customers_clean.csv`.

---

# Phần 4. Làm việc với Microsoft Excel

## 4.1. Đọc một trang tính

Pandas sử dụng `pd.read_excel()` để đọc dữ liệu Excel.

```python
df = pd.read_excel(
    "products.xlsx",
    sheet_name="Products",
    engine="openpyxl"
)
```

Tham số `sheet_name` xác định trang tính cần đọc.

### Bài tập — `read_excel()`

Đọc trang tính `Inventory` từ tệp `warehouse.xlsx` vào DataFrame `inventory`.

---

## 4.2. Đọc toàn bộ các trang tính

Có thể đọc toàn bộ workbook bằng:

```python
workbook = pd.read_excel(
    "products.xlsx",
    sheet_name=None
)

print(workbook.keys())
```

Kết quả trả về là một dictionary, trong đó:

- key là tên trang tính;
- value là DataFrame tương ứng.

Ví dụ:

```python
products = workbook["Products"]
```

### Bài tập

Đọc toàn bộ các trang tính trong `business.xlsx`.

Sau đó:

1. In danh sách tên các trang tính.
2. In số hàng và số cột của DataFrame tương ứng với từng trang tính.

---

## 4.3. Ghi nhiều DataFrame vào một workbook

`pd.ExcelWriter()` cho phép ghi nhiều DataFrame vào các trang tính khác nhau của cùng một tệp Excel.

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

### Bài tập — `ExcelWriter`

Xuất hai DataFrame `customers` và `orders` vào tệp:

```text
business_report.xlsx
```

trong đó mỗi DataFrame được lưu ở một trang tính riêng.

---

## 4.4. Các hàm chính

| Hàm hoặc tham số | Công dụng |
|---|---|
| `pd.read_excel()` | Đọc dữ liệu Excel |
| `sheet_name=` | Lựa chọn trang tính |
| `sheet_name=None` | Đọc toàn bộ các trang tính |
| `df.to_excel()` | Ghi DataFrame vào Excel |
| `pd.ExcelWriter()` | Ghi nhiều DataFrame vào cùng một workbook |

### Kiểm tra kiến thức

**Câu 1.** Khi sử dụng `sheet_name=None`, `pd.read_excel()` trả về đối tượng nào?

A. Dictionary chứa các DataFrame  
B. Chỉ DataFrame của trang tính đầu tiên  
C. Một mảng NumPy  
D. Một chuỗi ký tự

**Câu 2.** Đối tượng nào phù hợp để ghi nhiều DataFrame vào nhiều trang tính trong cùng một workbook?

A. `pd.ExcelWriter`  
B. `pd.ExcelReaderOnly`  
C. `pd.MultiSheet`  
D. `open_csv`

### Bài tập thực hành 4

Tạo tệp:

```text
business_data.xlsx
```

gồm ba trang tính:

- Customers;
- Products;
- Sales.

Thực hiện:

1. Đọc toàn bộ workbook.
2. In danh sách tên các trang tính.
3. Xác định số hàng và số cột của từng trang tính.
4. Tính tổng giá trị `Sales`.
5. Xuất một workbook mới gồm:
   - `Sales_Detail`;
   - `Sales_Summary`.

---

# Phần 5. Làm việc với JSON

## 5.1. JSON là gì?

JSON (*JavaScript Object Notation*) là định dạng dữ liệu phổ biến trong:

- Web API;
- hệ thống thương mại điện tử;
- microservices;
- cơ sở dữ liệu NoSQL.

Ví dụ:

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

## 5.2. Đọc JSON dạng bảng

Với JSON có cấu trúc tương đối phẳng, có thể sử dụng:

```python
df = pd.read_json(
    "customers.json"
)
```

### Bài tập — `pd.read_json()`

Đọc `products.json` vào DataFrame `products` và hiển thị năm dòng đầu tiên.

---

## 5.3. JSON lồng nhau

Dữ liệu JSON thực tế thường có nhiều cấp.

Ví dụ:

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

Để phân tích bằng Pandas, ta có thể chuyển cấu trúc trên thành bảng:

| order_id | customer_id | city | sku | qty |
|---|---|---|---|---:|
| O001 | C001 | Hanoi | P001 | 2 |
| O001 | C001 | Hanoi | P002 | 1 |

---

## 5.4. Làm phẳng dữ liệu bằng `pd.json_normalize()`

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

Trong đó:

- `record_path` xác định danh sách lồng nhau cần mở rộng thành các dòng;
- `meta` xác định các thuộc tính ở cấp cha cần được giữ lại.

### Bài tập — `pd.json_normalize()`

Cho dữ liệu:

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

Sử dụng `pd.json_normalize()` để tạo một DataFrame gồm hai dòng, trong đó mỗi dòng tương ứng với một sản phẩm trong đơn hàng.

### Kiểm tra kiến thức

**Câu 1.** Hàm nào có thể đọc trực tiếp dữ liệu JSON dạng tương đối phẳng?

A. `pd.read_json()`  
B. `pd.read_csv()`  
C. `pd.read_html()`  
D. `pd.read_pdf()`

**Câu 2.** Vai trò của `record_path` trong `pd.json_normalize()` là gì?

A. Xác định danh sách lồng nhau cần mở rộng thành các dòng  
B. Đổi tên cột  
C. Ghi dữ liệu ra JSON  
D. Xóa giá trị thiếu

### Bài tập thực hành 5

Tạo dữ liệu JSON mô phỏng ba đơn hàng.

Mỗi đơn hàng gồm:

- OrderID;
- OrderDate;
- Customer;
- Items.

Trong đó, `Customer` gồm:

- CustomerID;
- City.

Mỗi phần tử trong `Items` gồm:

- ProductID;
- Quantity;
- UnitPrice.

Thực hiện:

1. Đọc dữ liệu JSON.
2. Chuyển mỗi mặt hàng thành một dòng trong DataFrame.
3. Giữ lại các thuộc tính `OrderID`, `OrderDate`, `CustomerID` và `City`.
4. Tạo cột:

```text
Revenue = Quantity × UnitPrice
```

5. Tính tổng Revenue theo City.

---

# Phần 6. Truy xuất dữ liệu từ HTML và PDF

## 6.1. Đọc bảng HTML

`pd.read_html()` có thể phát hiện các phần tử `<table>` và chuyển chúng thành DataFrame.

```python
tables = pd.read_html(
    "financial_quotes.html"
)

print(
    len(tables)
)
```

Kết quả là một danh sách DataFrame.

Ví dụ truy cập bảng đầu tiên:

```python
stocks = tables[0]
```

### Bài tập — `pd.read_html()`

Đọc `market_data.html`.

Thực hiện:

1. Xác định số bảng có trong tệp.
2. Hiển thị bảng đầu tiên.
3. Kiểm tra số hàng và số cột của bảng.

---

## 6.2. Vì sao trích xuất dữ liệu từ PDF khó hơn CSV?

CSV được thiết kế để biểu diễn dữ liệu dạng bảng.

Ngược lại, PDF chủ yếu được thiết kế để:

- hiển thị nội dung;
- bảo toàn bố cục;
- phục vụ in ấn.

Do đó, quá trình:

```text
CSV → DataFrame
```

thường trực tiếp hơn:

```text
PDF → DataFrame
```

Với PDF, cấu trúc hàng và cột mà người đọc nhìn thấy không phải lúc nào cũng được lưu dưới dạng bảng rõ ràng bên trong tệp.

---

## 6.3. Trích xuất bảng bằng `pdfplumber`

Một thư viện có thể sử dụng để trích xuất bảng từ PDF là `pdfplumber`.

```python
import pdfplumber

with pdfplumber.open(
    "report.pdf"
) as pdf:

    page = pdf.pages[0]

    tables = page.extract_tables()
```

Có thể chuyển một bảng đã trích xuất thành DataFrame:

```python
table = tables[0]

df = pd.DataFrame(
    table[1:],
    columns=table[0]
)
```

Sau khi trích xuất, cần kiểm tra cẩn thận dữ liệu trước khi phân tích.

### Bài tập

Sau khi chuyển một bảng PDF thành DataFrame `df`, sử dụng các lệnh phù hợp để kiểm tra:

```python
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna().sum())
```

Xác định xem:

1. tiêu đề cột đã đúng hay chưa;
2. số hàng và số cột có hợp lý hay không;
3. có giá trị thiếu hay không.

### Kiểm tra kiến thức

**Câu 1.** Hàm Pandas nào có thể đọc các phần tử `<table>` trong HTML?

A. `pd.read_html()`  
B. `pd.read_web()`  
C. `pd.read_table_html_only()`  
D. `pd.scrape()`

**Câu 2.** Vì sao việc trích xuất dữ liệu từ PDF thường khó hơn CSV?

A. Vì PDF chủ yếu được thiết kế cho việc trình bày trực quan thay vì lưu trữ dữ liệu phân tích có cấu trúc.  
B. Vì PDF chỉ chứa dữ liệu số.  
C. Vì PDF không thể chứa bảng.  
D. Vì Python không thể mở tệp PDF.

### Bài tập thực hành 6

Cho một tệp HTML gồm:

- bảng giá sản phẩm;
- bảng tỷ giá ngoại tệ.

Thực hiện:

1. Đọc cả hai bảng vào Pandas.
2. Kiểm tra cấu trúc của từng bảng.
3. Lưu mỗi bảng vào một trang tính riêng trong cùng một tệp Excel.

Với một bảng được trích xuất từ PDF:

1. Chuyển bảng sang DataFrame.
2. Kiểm tra tiêu đề cột.
3. Kiểm tra giá trị thiếu.
4. Xác định các thao tác làm sạch cần thực hiện trước khi phân tích.

---

# Phần 7. Làm việc với cơ sở dữ liệu SQLite

## 7.1. SQLite là gì?

SQLite là một hệ quản trị cơ sở dữ liệu quan hệ gọn nhẹ. Toàn bộ cơ sở dữ liệu có thể được lưu trong một tệp, chẳng hạn:

```text
company.db
```

Python cung cấp module `sqlite3` trong thư viện chuẩn:

```python
import sqlite3
```

---

## 7.2. Kết nối đến cơ sở dữ liệu

Tạo kết nối:

```python
conn = sqlite3.connect(
    "company.db"
)

cursor = conn.cursor()
```

Đối tượng `conn` đại diện cho kết nối đến database, trong khi `cursor` được sử dụng để thực thi các câu lệnh SQL.

### Bài tập

Hoàn thiện đoạn mã để kết nối đến `sales.db` và tạo một cursor:

```python
# conn = sqlite3.connect(...)
# cursor = ...
```

---

## 7.3. Thực hiện truy vấn SQL

Ví dụ truy vấn các nhân viên có mức lương từ 30 triệu đồng trở lên:

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

`fetchall()` trả về toàn bộ các dòng thỏa mãn truy vấn.

### Bài tập

Viết truy vấn SQL để lấy thông tin các nhân viên thuộc phòng `Sales`.

---

## 7.4. Truy vấn có tham số

Khi giá trị truy vấn đến từ biến Python hoặc dữ liệu người dùng, nên sử dụng truy vấn có tham số.

```python
cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)
```

Cách viết này tách phần cấu trúc của câu lệnh SQL khỏi giá trị được truyền vào và giúp tránh các lỗi bảo mật do nối chuỗi trực tiếp.

### Bài tập

Viết một truy vấn có tham số để lấy các đơn hàng thỏa mãn:

```text
Amount >= target_amount
```

trong đó `target_amount` là một biến Python.

---

## 7.5. Đọc kết quả SQL vào Pandas

Pandas có thể đọc trực tiếp kết quả của một truy vấn SQL:

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

Kết quả được trả về dưới dạng DataFrame.

### Bài tập

Đọc ba trường sau từ bảng `orders` vào DataFrame:

```text
OrderID
CustomerID
Amount
```

---

## 7.6. Kết hợp nhiều bảng bằng JOIN

Ví dụ:

```sql
SELECT
    e.emp_id,
    e.full_name,
    d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;
```

Kết quả truy vấn có thể được đọc trực tiếp vào Pandas:

```python
df = pd.read_sql_query(
    query,
    conn
)
```

---

## 7.7. Ghi DataFrame vào SQLite

Pandas cung cấp phương thức `to_sql()`:

```python
df.to_sql(
    name="sales_summary",
    con=conn,
    if_exists="replace",
    index=False
)
```

Tham số `if_exists` có ba lựa chọn thường dùng:

- `fail`: báo lỗi nếu bảng đã tồn tại;
- `replace`: thay thế bảng cũ;
- `append`: bổ sung dữ liệu vào bảng hiện có.

### Bài tập — `to_sql()`

Lưu DataFrame `summary` vào bảng:

```text
monthly_summary
```

trong SQLite, với yêu cầu thay thế bảng cũ nếu bảng đã tồn tại.

---

## 7.8. Các hàm chính

| Hàm | Công dụng |
|---|---|
| `sqlite3.connect()` | Mở kết nối đến SQLite |
| `cursor.execute()` | Thực thi câu lệnh SQL |
| `fetchall()` | Lấy toàn bộ kết quả truy vấn |
| `pd.read_sql_query()` | Chuyển kết quả truy vấn thành DataFrame |
| `df.to_sql()` | Ghi DataFrame vào bảng SQL |

### Kiểm tra kiến thức

**Câu 1.** Module nào của thư viện chuẩn Python hỗ trợ SQLite?

A. `sqlite3`  
B. `sqlpandas`  
C. `sqlitepro`  
D. `pysqlserver`

**Câu 2.** Hàm nào chuyển trực tiếp kết quả truy vấn SQL thành DataFrame?

A. `pd.read_sql_query()`  
B. `pd.sql_to_df()`  
C. `pd.read_db_table_only()`  
D. `pd.load_database()`

**Câu 3.** Ưu điểm quan trọng của truy vấn có tham số là gì?

A. Tách cấu trúc câu lệnh SQL khỏi giá trị tham số và giúp giảm nguy cơ SQL Injection.  
B. Làm cho mọi truy vấn luôn chạy nhanh hơn.  
C. Loại bỏ nhu cầu sử dụng bảng.  
D. Tự động chuyển SQL sang JSON.

### Bài tập thực hành 7

Tạo database:

```text
sales.db
```

gồm hai bảng:

```text
customers(CustomerID, Name, City)

orders(OrderID, CustomerID, Amount)
```

Thực hiện:

1. Truy vấn toàn bộ đơn hàng.
2. Kết hợp `orders` và `customers` bằng `JOIN`.
3. Lọc các khách hàng tại Hanoi.
4. Đọc kết quả vào Pandas DataFrame.
5. Tính tổng `Amount` theo `City`.
6. Lưu bảng tổng hợp vào:

```text
city_sales_summary
```

---

# Phần 8. Làm việc với MongoDB và PyMongo

## 8.1. MongoDB là gì?

MongoDB là một hệ quản trị cơ sở dữ liệu NoSQL hướng tài liệu.

Trong cơ sở dữ liệu quan hệ, dữ liệu thường được tổ chức theo:

```text
Table
 └── Row
```

Trong MongoDB, dữ liệu được tổ chức theo:

```text
Collection
 └── Document
```

---

## 8.2. Cấu trúc document

Ví dụ một document đơn hàng:

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

Một document có thể chứa:

- các giá trị đơn;
- đối tượng lồng nhau;
- danh sách;
- nhiều cấp cấu trúc.

---

## 8.3. Kết nối MongoDB

PyMongo cung cấp lớp `MongoClient` để kết nối đến MongoDB.

```python
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["retail_db"]

orders = db["orders"]
```

---

## 8.4. Các thao tác CRUD

CRUD bao gồm bốn nhóm thao tác cơ bản:

```text
Create
Read
Update
Delete
```

### Thêm dữ liệu

```python
orders.insert_one(
    sample_order
)
```

### Đọc một document

```python
orders.find_one({
    "order_id": "ORD001"
})
```

### Lọc nhiều document

```python
orders.find({
    "total_amount": {
        "$gte": 1000000
    }
})
```

### Cập nhật document

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

### Xóa document

```python
orders.delete_many({
    "status": "CANCELLED"
})
```

### Bài tập — CRUD

Viết các lệnh PyMongo để:

1. Thêm một đơn hàng mới.
2. Tìm tất cả đơn hàng có `status="PAID"`.
3. Cập nhật một đơn hàng sang `status="SHIPPED"`.

---

## 8.5. Chuyển dữ liệu MongoDB sang Pandas

Kết quả truy vấn có thể được chuyển thành danh sách các document:

```python
documents = list(
    orders.find()
)
```

Sau đó làm phẳng dữ liệu bằng:

```python
df = pd.json_normalize(
    documents
)
```

Trường `_id` của MongoDB thường có kiểu `ObjectId`. Khi cần xuất sang CSV hoặc Excel, có thể chuyển trường này thành chuỗi:

```python
df["_id"] = (
    df["_id"]
    .astype(str)
)
```

### Bài tập

Lấy tất cả đơn hàng có trạng thái `PAID` từ MongoDB và chuyển kết quả thành Pandas DataFrame.

### Kiểm tra kiến thức

**Câu 1.** MongoDB lưu các bản ghi dưới dạng nào?

A. Document  
B. Trang tính Excel  
C. Ma trận NumPy  
D. Chỉ các dòng CSV

**Câu 2.** Phương thức nào dùng để truy vấn nhiều document?

A. `find()`  
B. `find_one_only_all()`  
C. `select()`  
D. `read_many()`

**Câu 3.** Hàm Pandas nào hữu ích khi chuyển các document MongoDB có cấu trúc lồng nhau sang dạng bảng?

A. `pd.json_normalize()`  
B. `pd.read_csv()`  
C. `pd.crosstab()`  
D. `pd.cut()`

### Bài tập thực hành 8

Tạo collection `customer_orders` gồm ít nhất năm document.

Mỗi document chứa:

- OrderID;
- Customer;
- Items;
- TotalAmount;
- Status.

Thực hiện:

1. Thêm các document vào collection.
2. Tìm các đơn hàng có `TotalAmount >= 1_000_000`.
3. Tìm các đơn hàng có `Status="PAID"`.
4. Cập nhật trạng thái của một đơn hàng.
5. Chuyển kết quả truy vấn sang Pandas DataFrame.
6. Tính tổng doanh thu của các đơn hàng có trạng thái `PAID`.

---

# Phần 9. Xây dựng Data Pipeline tích hợp dữ liệu đa nguồn

## 9.1. Tình huống

Một doanh nghiệp lưu dữ liệu tại nhiều nguồn:

```text
customers.csv
products.xlsx
orders.json
company.db
```

Mục tiêu là tích hợp các nguồn này thành một tập dữ liệu thống nhất phục vụ phân tích.

---

## 9.2. Quy trình tích hợp

Một pipeline tổng quát có thể được mô tả như sau:

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

## 9.3. Đọc dữ liệu từ các nguồn

Đọc khách hàng từ CSV:

```python
customers = pd.read_csv(
    "customers.csv"
)
```

Đọc sản phẩm từ Excel:

```python
products = pd.read_excel(
    "products.xlsx",
    sheet_name="Products"
)
```

Đọc đơn hàng từ JSON:

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

## 9.4. Làm phẳng dữ liệu JSON

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

Mỗi mặt hàng trong đơn hàng được chuyển thành một dòng riêng.

---

## 9.5. Tạo biến phân tích

Ví dụ tính doanh thu của từng dòng sản phẩm:

```python
items["Revenue"] = (
    items["Quantity"]
    * items["Price"]
)
```

---

## 9.6. Tích hợp dữ liệu bằng `merge()`

Ghép thông tin sản phẩm:

```python
df = items.merge(
    products,
    on="ProductID",
    how="left"
)
```

Ghép thông tin khách hàng:

```python
df = df.merge(
    customers,
    on="CustomerID",
    how="left"
)
```

### Bài tập

Sau mỗi phép `merge()`, sử dụng:

```python
# print(df.shape)
# print(df.isna().sum())
```

Thực hiện:

1. So sánh kích thước DataFrame trước và sau khi merge.
2. Kiểm tra các giá trị thiếu mới xuất hiện.
3. Giải thích vì sao `left join` có thể tạo ra các giá trị thiếu ở các cột lấy từ bảng bên phải.

---

## 9.7. Xây dựng các chỉ số KPI

Ví dụ tính doanh thu và số đơn hàng theo khu vực:

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

## 9.8. Lưu dữ liệu phân tích vào SQLite

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

## 9.9. Xuất báo cáo Excel nhiều trang tính

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

### Kiểm tra kiến thức

**Câu 1.** Bước nào nên được thực hiện trước khi tích hợp nhiều nguồn bằng `merge()`?

A. Đọc và kiểm tra từng nguồn dữ liệu  
B. Triển khai mô hình  
C. Huấn luyện mạng nơ-ron  
D. Tính feature importance

**Câu 2.** Vì sao cần kiểm tra giá trị thiếu sau khi thực hiện `merge()`?

A. Vì một số khóa có thể không tìm thấy bản ghi tương ứng ở nguồn dữ liệu còn lại.  
B. Vì `merge()` luôn xóa một phần dữ liệu.  
C. Vì Pandas luôn tự động thêm cột rỗng.  
D. Vì `merge()` chuyển toàn bộ dữ liệu số thành chuỗi.

### Bài tập thực hành 9 — Dự án tích hợp dữ liệu

Sử dụng:

```text
customers.csv
products.xlsx
orders.json
```

để xây dựng DataFrame:

```text
order_analytics
```

gồm các trường:

- OrderID;
- CustomerID;
- CustomerName;
- City;
- ProductID;
- Category;
- Quantity;
- UnitPrice;
- Revenue.

Thực hiện:

1. Đọc từng nguồn dữ liệu.
2. Kiểm tra cấu trúc và kiểu dữ liệu.
3. Làm phẳng dữ liệu đơn hàng từ JSON.
4. Tích hợp dữ liệu bằng `merge()`.
5. Xác định các bản ghi không tìm thấy khóa tương ứng.
6. Tính Revenue.
7. Tính:
   - tổng Revenue;
   - Revenue theo Category;
   - Revenue theo City;
   - số đơn hàng theo City.
8. Lưu dữ liệu chi tiết vào SQLite.
9. Xuất các bảng KPI vào một tệp Excel nhiều trang tính.

---

# Phần 10. Các nguyên tắc thực hành tốt

## 10.1. Chỉ đọc các cột cần thiết

Nếu tệp dữ liệu có nhiều cột nhưng bài toán chỉ sử dụng một số biến, nên giới hạn các cột ngay trong quá trình đọc.

```python
pd.read_csv(
    "large.csv",
    usecols=[
        "CustomerID",
        "Sales"
    ]
)
```

Điều này giúp giảm thời gian đọc và lượng RAM sử dụng.

### Bài tập

Một tệp CSV có 100 cột nhưng bài toán chỉ cần:

```text
Date
StoreID
ProductID
Sales
```

Viết lệnh `pd.read_csv()` để chỉ nhập bốn cột trên.

---

## 10.2. Kiểm tra dữ liệu ngay sau khi nhập

Một quy trình kiểm tra cơ bản có thể gồm:

```python
df.head()
df.shape
df.info()
df.isna().sum()
```

Các lệnh này giúp phát hiện sớm các vấn đề về cấu trúc, kiểu dữ liệu và giá trị thiếu.

### Bài tập

Viết một đoạn chương trình sử dụng ít nhất bốn lệnh Pandas để kiểm tra một DataFrame ngay sau khi đọc từ tệp.

---

## 10.3. Kiểm tra dữ liệu sau khi tích hợp

Sau phép `merge()`, cần kiểm tra lại dữ liệu:

```python
df.isna().sum()
```

Giá trị thiếu mới có thể xuất hiện nếu khóa ở hai nguồn dữ liệu không khớp nhau.

---

## 10.4. Kiểm soát kiểu dữ liệu

Kiểm tra:

```python
df.dtypes
```

Không nên giả định rằng mọi cột chứa chữ số đều là biến số học. Một trường như `CustomerID = "001"` là mã định danh và thường nên được lưu dưới dạng chuỗi.

---

## 10.5. Xử lý tệp lớn theo từng khối

Với tệp CSV có kích thước lớn, có thể sử dụng:

```python
pd.read_csv(
    "large.csv",
    chunksize=100000
)
```

Cách tiếp cận này cho phép xử lý dữ liệu tuần tự mà không cần tải toàn bộ tệp vào RAM.

---

## 10.6. Sử dụng context manager

Khi làm việc với tệp, nên sử dụng cú pháp `with`:

```python
with open(
    "data.json",
    encoding="utf-8"
) as f:
    ...
```

Tương tự khi tạo báo cáo Excel:

```python
with pd.ExcelWriter(
    "report.xlsx"
) as writer:
    ...
```

Cách viết này giúp tài nguyên được đóng đúng cách sau khi hoàn thành thao tác.

---

## 10.7. Sử dụng truy vấn SQL có tham số

Không nên nối trực tiếp dữ liệu đầu vào vào câu lệnh SQL.

Thay vào đó, nên sử dụng truy vấn có tham số để tách giá trị dữ liệu khỏi cấu trúc câu lệnh SQL.

---

## 10.8. Lựa chọn định dạng lưu trữ phù hợp

Không có một định dạng lưu trữ duy nhất phù hợp với mọi bài toán.

| Yêu cầu | Định dạng phù hợp |
|---|---|
| Trao đổi dữ liệu bảng đơn giản | CSV |
| Báo cáo quản trị nhiều trang tính | Excel |
| Trao đổi dữ liệu với Web API | JSON |
| Lưu dữ liệu quan hệ và thực hiện truy vấn | SQL |
| Lưu dữ liệu document có cấu trúc linh hoạt | MongoDB |
| Lưu tập dữ liệu bảng lớn để tái sử dụng hiệu quả | Parquet |
| Trích xuất bảng đã công bố trên website | HTML |
| Phân phối báo cáo có bố cục cố định | PDF |

### Kiểm tra kiến thức

**Câu 1.** Kỹ thuật nào phù hợp khi một tệp CSV lớn hơn dung lượng RAM?

A. Đọc dữ liệu theo từng khối  
B. Chuyển toàn bộ dữ liệu thành chuỗi  
C. Tạo thêm một bản sao của tệp  
D. Chỉ sử dụng `head()`

**Câu 2.** Vì sao các trường ID thường nên được lưu dưới dạng chuỗi?

A. Vì các chữ số của chúng thường biểu diễn nhãn hoặc mã định danh, không phải đại lượng.  
B. Vì chuỗi không sử dụng bộ nhớ.  
C. Vì dữ liệu số không thể lưu ID.  
D. Vì Pandas bắt buộc mọi ID phải là chuỗi.

**Câu 3.** Định dạng nào đặc biệt phổ biến khi trao đổi dữ liệu qua Web API?

A. JSON  
B. PDF  
C. XLS  
D. SQLite

### Bài tập thực hành 10 — Lựa chọn phương án lưu trữ

Với mỗi tình huống sau, hãy lựa chọn một định dạng lưu trữ phù hợp và giải thích lý do:

1. Gửi một bảng dữ liệu đơn giản cho đồng nghiệp.
2. Tạo báo cáo quản trị gồm nhiều trang tính.
3. Trao đổi dữ liệu giữa Web API và ứng dụng.
4. Lưu dữ liệu giao dịch cần thực hiện các truy vấn SQL.
5. Lưu dữ liệu có nhiều trường và đối tượng lồng nhau.
6. Lưu một tập dữ liệu bảng có kích thước lớn để sử dụng lại trong các bước phân tích sau.

---

# Tổng kết

Quy trình tổng quát khi làm việc với dữ liệu từ nhiều nguồn có thể được mô tả như sau:

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

Các công cụ chính được giới thiệu trong bài:

| Nguồn dữ liệu | Công cụ Python |
|---|---|
| CSV | `pd.read_csv()`, `to_csv()` |
| Tệp số với NumPy | `loadtxt()`, `genfromtxt()`, `savetxt()` |
| Excel | `read_excel()`, `ExcelWriter()` |
| JSON | `read_json()`, `json_normalize()` |
| HTML | `read_html()` |
| PDF | `pdfplumber` |
| SQLite | `sqlite3`, `read_sql_query()`, `to_sql()` |
| MongoDB | `pymongo`, `json_normalize()` |

Các kỹ năng truy xuất, chuẩn bị và lưu trữ dữ liệu tạo nền tảng cho toàn bộ quy trình Data Science:

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

Một mô hình phân tích hoặc Machine Learning chỉ có thể hoạt động hiệu quả khi dữ liệu đầu vào được truy xuất đúng, kiểm tra đầy đủ, chuyển đổi nhất quán và lưu trữ theo cách phù hợp với mục tiêu sử dụng.