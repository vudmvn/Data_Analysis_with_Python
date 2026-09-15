# Làm sạch dữ liệu với Python (Data Cleaning in Python)

## Tóm tắt bài học

**Data Cleaning** là quá trình phát hiện, kiểm tra và xử lý các vấn đề chất lượng trong dữ liệu thô để dữ liệu trở nên chính xác, nhất quán và phù hợp cho phân tích. Đây là một bước nền tảng của **Data Preprocessing** và thường được thực hiện trước khi xây dựng mô hình thống kê hoặc học máy.

Trong thực tế, dữ liệu có thể chứa nhiều vấn đề như:

- giá trị thiếu;
- bản ghi trùng lặp;
- kiểu dữ liệu không đúng;
- dữ liệu ngoài phạm vi hợp lý;
- định dạng không nhất quán;
- lỗi chính tả;
- đơn vị đo không thống nhất;
- các giá trị cực đoan hoặc bất thường.

Bài học này tập trung vào cách sử dụng **Pandas**, **NumPy** và **Matplotlib** để nhận diện và xử lý các vấn đề trên một cách có hệ thống.

---

## 1. Mục tiêu bài học

Sau bài học này, người học có thể:

- Giải thích được vai trò của Data Cleaning trong Data Science.
- Nhận diện các dạng lỗi dữ liệu phổ biến.
- Kiểm tra duplicate records bằng Pandas.
- Phân biệt biến số và biến phân loại.
- Kiểm tra số lượng giá trị duy nhất trong các biến phân loại.
- Tính số lượng và tỷ lệ missing values.
- Xử lý dữ liệu thiếu bằng các chiến lược phù hợp.
- Chuẩn hóa định dạng văn bản, ngày tháng và tên nhãn.
- Phát hiện outlier bằng boxplot và các ngưỡng thống kê.
- Giải thích được vì sao không nên tự động xóa mọi outlier.
- Loại bỏ các biến không liên quan hoặc không hữu ích.
- Kiểm tra và xác thực dữ liệu sau khi làm sạch.
- Ghi chép và tổ chức một quy trình Data Cleaning có thể tái lập.

---

# 2. Data Cleaning là gì?

**Data Cleaning** là quá trình chuẩn bị dữ liệu bằng cách phát hiện và sửa các lỗi hoặc bất thường trong dữ liệu.

Có thể hình dung:

```text
Dữ liệu thô
    ↓
Kiểm tra chất lượng dữ liệu
    ↓
Phát hiện lỗi
    ↓
Làm sạch và chuẩn hóa
    ↓
Xác thực lại dữ liệu
    ↓
Dữ liệu sẵn sàng cho EDA / Machine Learning
```

Data Cleaning là một phần của quy trình rộng hơn là **Data Preprocessing**.

```text
Data Preprocessing
│
├── Data Cleaning
├── Encoding
├── Scaling
├── Feature Transformation
├── Feature Selection
└── Data Splitting
```

Vì vậy:

> **Data Cleaning tập trung vào chất lượng dữ liệu; Data Preprocessing bao gồm cả Data Cleaning và các bước biến đổi dữ liệu phục vụ mô hình.**

---

# 3. Vì sao Data Cleaning quan trọng?

Dữ liệu chưa được làm sạch có thể làm sai lệch toàn bộ quá trình phân tích.

Ví dụ:

```text
Customer_ID     Region       Revenue
C001            Hanoi        1500000
C002            Ha Noi       1800000
C003            HANOI        1700000
```

Nếu không chuẩn hóa, ba giá trị:

```text
Hanoi
Ha Noi
HANOI
```

có thể bị xem là ba nhóm khác nhau.

Một ví dụ khác:

```text
Age
25
31
28
250
```

Giá trị `250` có thể là lỗi nhập dữ liệu.

Nếu không xử lý, giá trị này có thể làm:

- tăng mean;
- tăng standard deviation;
- ảnh hưởng regression;
- ảnh hưởng distance-based algorithms.

---

# 4. Các vấn đề chất lượng dữ liệu phổ biến

## 4.1. Missing Values

Missing values là các giá trị bị thiếu.

Ví dụ:

```text
Customer    Age    Income
A           25     12
B           NaN    15
C           34     NaN
```

Nguyên nhân có thể do:

- không thu thập được dữ liệu;
- người dùng bỏ trống;
- lỗi hệ thống;
- lỗi truyền dữ liệu;
- dữ liệu không áp dụng cho đối tượng.

Missing values có thể làm giảm chất lượng phân tích hoặc gây lỗi cho thuật toán.

---

## 4.2. Duplicate Records

Duplicate records là các dòng bị lặp lại.

Ví dụ:

```text
ID    Product    Quantity
1     A          5
2     B          3
1     A          5
```

Nếu dòng thứ ba là một bản ghi lặp không hợp lệ, tổng số lượng sản phẩm A sẽ bị tính sai.

Duplicate có thể xuất hiện khi:

- nhập dữ liệu nhiều lần;
- merge dữ liệu sai;
- hệ thống ghi lại giao dịch nhiều lần;
- dữ liệu được sao chép từ nhiều nguồn.

---

## 4.3. Incorrect Data Types

Ví dụ:

```text
Age = "25"
```

thay vì:

```text
Age = 25
```

Hoặc:

```text
Date = "12/03/2026"
```

nhưng được lưu dưới dạng `object` thay vì `datetime`.

Sai kiểu dữ liệu có thể gây:

- lỗi tính toán;
- lỗi sorting;
- lỗi filtering;
- lỗi mô hình hóa.

---

## 4.4. Outliers and Anomalies

Outlier là giá trị nằm xa phần lớn các giá trị còn lại.

Ví dụ:

```text
Order_Value
150
180
170
160
12000
```

`12000` có thể là:

- một giao dịch đặc biệt lớn;
- giao dịch doanh nghiệp;
- lỗi nhập liệu;
- sai đơn vị.

Do đó, **outlier cần được điều tra trước khi xử lý**.

---

## 4.5. Inconsistent Formats

Ví dụ ngày tháng:

```text
2026-09-01
01/09/2026
Sep 1, 2026
```

Ví dụ tên thành phố:

```text
Hanoi
Ha Noi
HÀ NỘI
```

Ví dụ đơn vị:

```text
Weight = 50 kg
Weight = 50000 g
```

Nếu không chuẩn hóa, phân tích có thể sai.

---

## 4.6. Spelling and Typographical Errors

Ví dụ:

```text
Region
North
Nort
Nroth
north
```

Các lỗi này đặc biệt phổ biến trong:

- survey;
- CRM;
- form nhập liệu;
- dữ liệu nhập thủ công.

---

# 5. Quy trình Data Cleaning tổng quát

Một quy trình làm sạch dữ liệu có thể gồm:

```text
1. Assess Data Quality
2. Remove Irrelevant Data
3. Fix Structural Errors
4. Handle Missing Data
5. Standardize / Normalize Structure
6. Identify and Manage Outliers
7. Validate Cleaned Data
8. Document Cleaning Decisions
```

Các bước này không nhất thiết luôn thực hiện đúng một thứ tự cứng nhắc. Trong thực tế, Data Cleaning thường là quá trình lặp.

---

# 6. Bước 1 — Import thư viện và nạp dữ liệu

Ví dụ sử dụng bộ dữ liệu Titanic.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("Titanic-Dataset.csv")

df.head()
```

Kiểm tra cấu trúc:

```python
df.info()
```

Kiểm tra kích thước:

```python
df.shape
```

### Câu hỏi tự kiểm tra

1. `df.head()` cho biết điều gì?
2. `df.info()` có thể giúp phát hiện những vấn đề nào?
3. Vì sao nên kiểm tra dữ liệu trước khi thực hiện bất kỳ bước làm sạch nào?

---

# 7. Bước 2 — Đánh giá chất lượng dữ liệu

Trước khi sửa dữ liệu, cần xác định dữ liệu đang có vấn đề gì.

Một số câu hỏi quan trọng:

- Có missing values không?
- Có duplicate records không?
- Kiểu dữ liệu đã đúng chưa?
- Có giá trị ngoài phạm vi hợp lý không?
- Có nhãn categorical không nhất quán không?
- Có cột không cần thiết không?
- Có đơn vị đo không thống nhất không?

Một kiểm tra ban đầu:

```python
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
```

---

# 8. Bước 3 — Kiểm tra duplicate records

## 8.1. `duplicated()`

```python
df.duplicated()
```

Kết quả là một Series kiểu Boolean:

```text
False
False
True
False
...
```

`True` biểu thị dòng được xem là duplicate.

Đếm tổng số dòng trùng:

```python
df.duplicated().sum()
```

---

## 8.2. Xem các dòng duplicate

```python
duplicate_rows = df[df.duplicated()]

duplicate_rows
```

---

## 8.3. Loại bỏ duplicate

```python
df = df.drop_duplicates()
```

Hoặc:

```python
df.drop_duplicates(inplace=True)
```

### Cẩn trọng

Hai dòng giống nhau hoàn toàn không phải lúc nào cũng là lỗi.

Ví dụ trong dữ liệu giao dịch:

```text
Customer    Product    Quantity
A           Coffee     2
A           Coffee     2
```

có thể là hai giao dịch khác nhau.

Nếu có biến:

```text
Transaction_ID
```

thì có thể xác định rõ hơn.

Ví dụ:

```python
df.duplicated(subset=["Transaction_ID"]).sum()
```

### Tự kiểm tra

Nếu hai dòng giống nhau về sản phẩm và số lượng nhưng có `Transaction_ID` khác nhau, có nên xóa một dòng không?

---

# 9. Bước 4 — Xác định kiểu dữ liệu

Có thể dùng:

```python
df.dtypes
```

Hoặc phân nhóm các biến:

```python
cat_col = [
    col for col in df.columns
    if df[col].dtype == "object"
]

num_col = [
    col for col in df.columns
    if df[col].dtype != "object"
]

print("Categorical columns:", cat_col)
print("Numerical columns:", num_col)
```

Một cách tổng quát hơn:

```python
cat_col = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

num_col = df.select_dtypes(
    include=np.number
).columns.tolist()
```

### Lưu ý

Không phải mọi cột số đều là biến số theo nghĩa phân tích.

Ví dụ:

```text
Customer_ID = 1001, 1002, 1003
```

được lưu dưới dạng integer nhưng thực chất là **identifier**, không phải biến định lượng.

---

# 10. Bước 5 — Kiểm tra số lượng giá trị duy nhất

Đối với categorical variables:

```python
df[cat_col].nunique()
```

Có thể xem trực tiếp giá trị:

```python
df["Embarked"].unique()
```

Đếm tần suất:

```python
df["Embarked"].value_counts(dropna=False)
```

Việc này giúp phát hiện:

```text
"S"
"s"
"Southampton"
" Southhampton "
```

có thể đang đại diện cho cùng một nhóm.

---

# 11. Bước 6 — Chuẩn hóa dữ liệu văn bản

Giả sử:

```text
Region
 Hanoi
HANOI
hanoi
Ha Noi
```

Có thể xử lý:

```python
df["Region"] = (
    df["Region"]
    .str.strip()
    .str.lower()
)
```

Kết quả:

```text
hanoi
hanoi
hanoi
ha noi
```

Nếu cần gộp nhãn:

```python
df["Region"] = df["Region"].replace({
    "ha noi": "hanoi",
    "hn": "hanoi"
})
```

Một số hàm hữu ích:

```python
.str.strip()
.str.lower()
.str.upper()
.str.title()
.str.replace()
```

### Bài tập nhỏ

Cho:

```text
Payment_Method

 Cash
cash
CASH
Credit Card
credit card
```

Viết mã để chuẩn hóa về:

```text
cash
credit card
```

---

# 12. Bước 7 — Chuẩn hóa tên cột

Tên cột có thể chứa khoảng trắng hoặc viết không thống nhất.

Ví dụ:

```text
Customer Name
Order Value
Region-Code
```

Có thể chuẩn hóa:

```python
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)
```

Kết quả:

```text
customer_name
order_value
region_code
```

Điều này giúp code dễ đọc và nhất quán hơn.

---

# 13. Bước 8 — Chuẩn hóa ngày tháng

Giả sử cột `Date` được lưu dưới dạng string.

```python
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)
```

`errors="coerce"` sẽ biến giá trị không thể chuyển đổi thành:

```text
NaT
```

Sau đó có thể kiểm tra:

```python
df["Date"].isna().sum()
```

### Ví dụ

```python
df["Date"].dt.year
df["Date"].dt.month
df["Date"].dt.day
```

### Lợi ích

Sau khi chuyển về datetime, có thể:

- lọc theo thời gian;
- tính chênh lệch ngày;
- nhóm theo tháng;
- tạo biến thời gian.

---

# 14. Bước 9 — Kiểm tra Missing Values

## 14.1. Số lượng missing

```python
df.isnull().sum()
```

Hoặc:

```python
df.isna().sum()
```

---

## 14.2. Tỷ lệ missing

```python
missing_percent = (
    df.isnull().sum()
    / df.shape[0]
    * 100
)

round(missing_percent, 2)
```

Có thể sắp xếp:

```python
missing_percent.sort_values(
    ascending=False
)
```

---

# 15. Missing Data không chỉ là `NaN`

Một số hệ thống lưu missing bằng:

```text
"Unknown"
"N/A"
"?"
"-"
999
-1
0
```

Do đó cần kết hợp:

- thống kê;
- hiểu ngữ cảnh;
- data dictionary;
- domain knowledge.

Ví dụ:

```python
df["Income"].value_counts(dropna=False)
```

Nếu phát hiện:

```text
Income = -1
```

cần xác định đây là giá trị thực hay mã hóa cho missing.

---

# 16. Bước 10 — Xử lý Missing Values

Không có một chiến lược duy nhất cho mọi trường hợp.

## 16.1. Loại bỏ dòng

```python
df.dropna()
```

Hoặc chỉ theo một số cột:

```python
df.dropna(
    subset=["Embarked"]
)
```

Phù hợp khi số dòng thiếu nhỏ.

---

## 16.2. Loại bỏ cột

Ví dụ:

```python
df = df.drop(
    columns=["Cabin"]
)
```

Trong ví dụ Titanic, các cột như:

```text
Name
Ticket
Cabin
```

có thể được loại khỏi một bài toán mô hình hóa đơn giản nếu chúng không phục vụ mục tiêu phân tích hoặc có quá nhiều missing values.

Tuy nhiên, quyết định này phụ thuộc vào mục tiêu phân tích.

---

## 16.3. Điền bằng mean

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

---

## 16.4. Điền bằng median

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

Median thường phù hợp hơn khi phân phối lệch hoặc có outlier.

---

## 16.5. Điền bằng mode

Phù hợp cho categorical variable:

```python
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)
```

---

## 16.6. Điền bằng nhãn đặc biệt

Ví dụ:

```python
df["Name"] = df["Name"].fillna(
    "Unknown"
)
```

Điều này giữ lại thông tin rằng giá trị ban đầu bị thiếu.

---

# 17. Có nên dùng `fillna(mean)` cho mọi biến?

Không.

Ví dụ:

```text
Income
```

có thể dùng mean hoặc median.

Nhưng:

```text
Region
```

không thể điền bằng mean.

Với:

```text
Customer_ID
```

việc điền bằng trung bình thường không có ý nghĩa.

Vì vậy, phải dựa vào **loại biến** và **ý nghĩa biến**.

---

# 18. Bước 11 — Loại bỏ dữ liệu không liên quan

Một số cột không đóng góp cho mục tiêu phân tích.

Ví dụ với mô hình dự đoán sống sót Titanic:

```text
PassengerId
```

thường chỉ là mã định danh.

Nếu mục tiêu chỉ là dự đoán:

```text
Survived
```

có thể không cần dùng `PassengerId`.

Loại bỏ:

```python
df = df.drop(
    columns=["PassengerId"]
)
```

### Nhưng cần cẩn trọng

Không nên xóa biến chỉ vì "trông có vẻ không quan trọng".

Một cột như:

```text
Cabin
```

có thể chứa thông tin về vị trí hành khách trên tàu.

Vì vậy, quyết định xóa biến cần gắn với:

- mục tiêu;
- tỷ lệ missing;
- ý nghĩa nghiệp vụ;
- khả năng tạo feature mới.

---

# 19. Bước 12 — Phát hiện Outlier bằng Boxplot

```python
import matplotlib.pyplot as plt

plt.boxplot(
    df["Age"].dropna(),
    vert=False
)

plt.xlabel("Age")
plt.title("Boxplot of Age")
plt.show()
```

Boxplot thường biểu diễn:

```text
Q1
Median
Q3
Whiskers
Potential outliers
```

---

# 20. Outlier không nhất thiết là lỗi

Một điểm vượt khỏi boxplot whisker chỉ là một quan sát **bất thường theo quy tắc thống kê**.

Nó không tự động có nghĩa là:

```text
invalid data
```

Ví dụ:

- khách hàng VIP;
- đơn hàng B2B;
- doanh nghiệp rất lớn;
- giao dịch gian lận;
- một hành khách cao tuổi.

Trong nhiều bài toán, outliers chính là đối tượng cần nghiên cứu.

---

# 21. Bước 13 — Phát hiện Outlier bằng Mean ± 2 Standard Deviations

Nguồn ví dụ sử dụng:

\[
Lower = \mu - 2\sigma
\]

\[
Upper = \mu + 2\sigma
\]

Trong Python:

```python
mean = df["Age"].mean()
std = df["Age"].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
```

Lọc:

```python
df_clean = df[
    (df["Age"] >= lower_bound) &
    (df["Age"] <= upper_bound)
]
```

### Hạn chế

Phương pháp này phù hợp hơn khi dữ liệu tương đối đối xứng và không quá lệch.

Nếu phân phối bị skew mạnh, mean và standard deviation có thể bị outlier ảnh hưởng đáng kể.

---

# 22. Phương pháp IQR để phát hiện Outlier

Một phương pháp phổ biến khác:

\[
IQR = Q_3 - Q_1
\]

\[
Lower = Q_1 - 1.5 \times IQR
\]

\[
Upper = Q_3 + 1.5 \times IQR
\]

Python:

```python
q1 = df["Age"].quantile(0.25)
q3 = df["Age"].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["Age"] < lower) |
    (df["Age"] > upper)
]
```

IQR thường ít nhạy với extreme values hơn phương pháp dùng mean và standard deviation.

---

# 23. Các cách xử lý Outlier

Tùy bài toán, có thể:

### Giữ nguyên

Nếu giá trị hợp lệ và quan trọng.

### Loại bỏ

Nếu xác định là lỗi hoặc không đại diện cho đối tượng nghiên cứu.

### Capping

Giới hạn giá trị ở một ngưỡng.

Ví dụ:

```python
df["Income"] = df["Income"].clip(
    lower=lower,
    upper=upper
)
```

### Log transformation

```python
df["Income_log"] = np.log1p(
    df["Income"]
)
```

### Phân tích riêng

Ví dụ chia:

```text
regular customers
high-value customers
```

---

# 24. Bước 14 — Sửa sai đơn vị đo

Giả sử:

```text
Weight
70 kg
65000 g
80 kg
```

Cần chuyển về cùng đơn vị.

Ví dụ:

```python
df.loc[
    df["unit"] == "g",
    "weight"
] = (
    df.loc[
        df["unit"] == "g",
        "weight"
    ] / 1000
)
```

Sau đó:

```python
df["unit"] = "kg"
```

Không thống nhất đơn vị có thể tạo ra outlier giả.

---

# 25. Bước 15 — Kiểm tra phạm vi hợp lệ

Dựa vào domain knowledge.

Ví dụ:

```text
Age < 0
Age > 120
```

có thể cần điều tra.

Kiểm tra:

```python
df[
    (df["Age"] < 0) |
    (df["Age"] > 120)
]
```

Ví dụ rating:

```text
Score phải nằm trong [0, 100]
```

Kiểm tra:

```python
invalid_score = df[
    ~df["Score"].between(0, 100)
]
```

---

# 26. Bước 16 — Data Validation

Sau khi làm sạch, cần kiểm tra lại.

Ví dụ:

```python
df.isnull().sum()
```

```python
df.duplicated().sum()
```

```python
df.dtypes
```

```python
df.describe()
```

```python
df["Region"].value_counts()
```

Có thể tạo các assertions:

```python
assert df.duplicated().sum() == 0
```

```python
assert df["Age"].between(
    0, 120
).all()
```

Assertions giúp phát hiện lỗi khi pipeline chạy lại với dữ liệu mới.

---

# 27. Data Validation và Domain Knowledge

Một giá trị có thể hợp lệ về mặt kỹ thuật nhưng vô lý về nghiệp vụ.

Ví dụ:

```text
Quantity = 10000
```

có thể hợp lệ trong bán buôn nhưng bất thường trong bán lẻ.

Hoặc:

```text
Delivery_Time = 0
```

có thể đúng cho đơn hàng nhận tại cửa hàng nhưng sai đối với giao hàng liên tỉnh.

Do đó, validation nên kết hợp:

```text
Technical rules
+
Business rules
+
Domain knowledge
```

---

# 28. Ví dụ làm sạch dữ liệu Titanic

## 28.1. Đọc dữ liệu

```python
import pandas as pd
import numpy as np

df = pd.read_csv(
    "Titanic-Dataset.csv"
)

df.head()
```

---

## 28.2. Kiểm tra duplicate

```python
print(
    df.duplicated().sum()
)
```

---

## 28.3. Xác định categorical và numerical columns

```python
cat_col = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

num_col = df.select_dtypes(
    include=np.number
).columns.tolist()

print(cat_col)
print(num_col)
```

---

## 28.4. Kiểm tra unique values

```python
df[cat_col].nunique()
```

---

## 28.5. Missing percentage

```python
missing_percent = round(
    (
        df.isnull().sum()
        / df.shape[0]
    ) * 100,
    2
)

missing_percent
```

---

## 28.6. Loại một số cột

```python
df1 = df.drop(
    columns=[
        "Name",
        "Ticket",
        "Cabin"
    ]
)
```

---

## 28.7. Xử lý missing `Embarked`

```python
df1.dropna(
    subset=["Embarked"],
    inplace=True
)
```

---

## 28.8. Xử lý missing `Age`

```python
df1["Age"] = df1["Age"].fillna(
    df1["Age"].mean()
)
```

Trong thực hành khác, có thể cân nhắc median:

```python
df1["Age"] = df1["Age"].fillna(
    df1["Age"].median()
)
```

---

## 28.9. Kiểm tra outlier `Age`

```python
plt.boxplot(
    df1["Age"],
    vert=False
)

plt.xlabel("Age")
plt.title("Boxplot of Age")
plt.show()
```

---

## 28.10. Tạo ngưỡng

```python
mean = df1["Age"].mean()
std = df1["Age"].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std
```

---

## 28.11. Lọc dữ liệu

```python
df2 = df1[
    (df1["Age"] >= lower_bound) &
    (df1["Age"] <= upper_bound)
].copy()
```

### Lưu ý

Trong một phân tích thực tế, không nên loại các hành khách lớn tuổi chỉ vì họ nằm ngoài ngưỡng thống kê nếu tuổi của họ là hợp lệ.

---

# 29. Tách biến đầu vào và biến mục tiêu

Ví dụ:

```python
X = df2[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked"
    ]
]

y = df2["Survived"]
```

Đây là bước chuyển từ **Data Cleaning** sang **Data Preprocessing và Modeling**.

---

# 30. Data Cleaning và Scaling

Nguồn thực hành tiếp tục với Min-Max Scaling.

Ví dụ:

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(
    feature_range=(0, 1)
)

num_col_ = [
    col for col in X.columns
    if X[col].dtype != "object"
]
```

Tuy nhiên, trong một workflow học máy chuẩn:

```text
Data Cleaning
      ↓
Train/Test Split
      ↓
Fit Scaler on Training Data
      ↓
Transform Train and Test
```

Không nên fit scaler trên toàn bộ dữ liệu trước khi chia train/test nếu mục tiêu là xây dựng mô hình dự đoán.

Nội dung scaling được trình bày chi tiết hơn trong bài **Data Preprocessing in Python**.

---

# 31. Data Cleaning có phải chỉ là xóa dữ liệu?

Không.

Một quy trình Data Cleaning tốt có thể bao gồm:

```text
detect
correct
standardize
impute
validate
document
```

Trong nhiều trường hợp, việc **sửa** dữ liệu tốt hơn việc xóa.

Ví dụ:

```text
"Hanoi "
```

nên được sửa thành:

```text
"Hanoi"
```

thay vì xóa cả bản ghi.

---

# 32. Các chiến lược Data Cleaning tốt

## 32.1. Hiểu dữ liệu

Trước khi xử lý, cần hiểu:

- nguồn dữ liệu;
- cách dữ liệu được thu thập;
- đơn vị đo;
- ý nghĩa biến;
- quy tắc nghiệp vụ.

---

## 32.2. Ghi chép quy trình

Nên ghi rõ:

- cột nào bị loại;
- missing được xử lý ra sao;
- outlier được xử lý thế nào;
- nhãn nào được gộp;
- đơn vị nào được đổi.

Ví dụ:

```text
Age:
- missing → median
- invalid Age < 0 → set as missing

Region:
- strip spaces
- convert to lowercase
- "ha noi" → "hanoi"
```

---

## 32.3. Ưu tiên vấn đề nghiêm trọng

Ví dụ:

```text
ID duplicate
wrong currency unit
incorrect target label
```

cần xử lý trước lỗi viết hoa/thường.

---

## 32.4. Tự động hóa khi phù hợp

Các bước lặp có thể viết thành hàm:

```python
def clean_text_column(series):
    return (
        series
        .str.strip()
        .str.lower()
    )
```

Áp dụng:

```python
df["Region"] = clean_text_column(
    df["Region"]
)
```

---

## 32.5. Kết hợp với chuyên gia nghiệp vụ

Một Data Scientist có thể phát hiện:

```text
Revenue = -500
```

nhưng chuyên gia nghiệp vụ mới có thể giải thích:

```text
đây là khoản hoàn tiền
```

Do đó, dữ liệu bất thường không phải lúc nào cũng là dữ liệu sai.

---

## 32.6. Theo dõi chất lượng dữ liệu liên tục

Data Cleaning không chỉ xảy ra một lần.

Trong hệ thống thực tế:

```text
New Data
   ↓
Quality Checks
   ↓
Cleaning Rules
   ↓
Validation
   ↓
Analytics / ML
```

Các quy tắc làm sạch nên được kiểm tra định kỳ.

---

# 33. Những lỗi thường gặp khi Data Cleaning

## 33.1. Xóa duplicate mà không kiểm tra khóa

Sai:

```python
df.drop_duplicates()
```

mà không hiểu mỗi dòng đại diện cho gì.

---

## 33.2. Dùng mean cho tất cả missing values

Không phù hợp với categorical variables hoặc skewed data.

---

## 33.3. Xóa mọi outlier

Có thể làm mất:

- khách hàng quan trọng;
- rare events;
- fraud cases;
- các nhóm có giá trị cao.

---

## 33.4. Sửa dữ liệu nhưng không ghi lại quy tắc

Sau này rất khó:

- tái lập kết quả;
- audit;
- xử lý dữ liệu mới.

---

## 33.5. Không kiểm tra lại sau cleaning

Sau khi sửa dữ liệu cần xác nhận:

```text
missing?
duplicate?
invalid range?
wrong dtype?
unexpected category?
```

---

# 34. Ví dụ trong bối cảnh kinh doanh

Giả sử có dữ liệu bán hàng:

```text
Order_ID
Customer_ID
Region
Order_Date
Product
Quantity
Unit_Price
Revenue
```

Một số lỗi:

```text
Order_ID duplicate
Region = "Ha Noi", "Hanoi", " HANOI "
Order_Date dùng nhiều format
Quantity = -2
Unit_Price missing
Revenue không bằng Quantity × Unit_Price
```

Một quy trình cleaning có thể là:

```text
1. Kiểm tra duplicate Order_ID
2. Chuẩn hóa Region
3. Convert Order_Date → datetime
4. Kiểm tra Quantity > 0
5. Impute hoặc điều tra Unit_Price missing
6. Kiểm tra Revenue
7. Validate lại dữ liệu
```

---

# 35. Bài tập thực hành ngắn

## Bài 1 — Duplicate records

Cho DataFrame `df`.

Viết mã:

1. Đếm duplicate rows.
2. Hiển thị duplicate rows.
3. Loại duplicate rows.
4. Kiểm tra lại.

Gợi ý:

```python
df.________().sum()

df[
    df.________()
]

df = df.________()
```

---

## Bài 2 — Missing values

Viết mã để:

1. Tính số missing values.
2. Tính tỷ lệ missing.
3. Sắp xếp tỷ lệ missing giảm dần.

Gợi ý:

```python
missing = df.________().sum()

missing_percent = (
    missing / ________
) * 100
```

---

## Bài 3 — Chuẩn hóa văn bản

Cho cột:

```text
Region
" Hanoi "
"HANOI"
"ha noi"
"Ho Chi Minh"
"HO CHI MINH "
```

Hãy:

1. Loại khoảng trắng thừa.
2. Chuyển về lowercase.
3. Gộp `"ha noi"` thành `"hanoi"`.

---

## Bài 4 — Kiểm tra phạm vi

Cho:

```text
Age
18
25
-2
31
150
45
```

Viết mã tìm các giá trị không nằm trong:

```text
0 ≤ Age ≤ 120
```

---

## Bài 5 — Outlier

Cho cột `Revenue`.

Hãy:

1. Tính Q1.
2. Tính Q3.
3. Tính IQR.
4. Tính lower/upper bounds.
5. Hiển thị potential outliers.
6. Không xóa chúng ngay; viết một câu giải thích cần kiểm tra điều gì trước khi quyết định.

---

# 36. Tự kiểm tra

### Câu 1

Data Cleaning là gì?

A. Quá trình huấn luyện mô hình  
B. Quá trình sửa và chuẩn hóa các vấn đề chất lượng dữ liệu  
C. Quá trình trực quan hóa dữ liệu  
D. Quá trình chỉ xóa outlier

---

### Câu 2

Lệnh nào dùng để phát hiện duplicate rows?

A. `df.unique()`  
B. `df.duplicated()`  
C. `df.repeat()`  
D. `df.isna()`

---

### Câu 3

Lệnh nào cho biết tỷ lệ missing values theo cột?

A.

```python
df.isna().mean() * 100
```

B.

```python
df.describe() * 100
```

C.

```python
df.mean().isna()
```

---

### Câu 4

Outlier có luôn là dữ liệu sai không?

A. Có  
B. Không

---

### Câu 5

Nếu cột `Region` có:

```text
Hanoi
HANOI
 hanoi
```

vấn đề chính là gì?

A. Missing data  
B. Inconsistent format  
C. Duplicate columns  
D. Wrong target

---

### Câu 6

Tại sao cần hiểu domain trước khi xóa outlier?

---

### Câu 7

Nếu `Revenue = Quantity × Unit_Price`, ta có thể sử dụng quan hệ này để làm gì trong Data Cleaning?

---

### Câu 8

Vì sao identifier như `Customer_ID` thường không nên được xem như numerical feature thông thường?

---

### Câu 9

Khi nào median có thể phù hợp hơn mean trong missing-value imputation?

---

### Câu 10

Tại sao cần kiểm tra lại dữ liệu sau khi làm sạch?

---

# 37. Bài tập tổng hợp — Cleaning dữ liệu bán hàng

Cho file:

```text
sales.csv
```

với các cột:

```text
Order_ID
Customer_ID
Region
Order_Date
Product
Quantity
Unit_Price
Revenue
Payment_Method
```

Thực hiện:

1. Đọc dữ liệu.
2. Kiểm tra `shape`.
3. Kiểm tra `info()`.
4. Đếm duplicate rows.
5. Kiểm tra duplicate `Order_ID`.
6. Chuẩn hóa tên cột.
7. Chuẩn hóa `Region`.
8. Chuẩn hóa `Payment_Method`.
9. Convert `Order_Date` sang datetime.
10. Tính missing percentage.
11. Xử lý missing values phù hợp.
12. Kiểm tra `Quantity <= 0`.
13. Kiểm tra outlier của `Revenue`.
14. Kiểm tra:

\[
Revenue \approx Quantity \times Unit\_Price
\]

15. Kiểm tra lại duplicate, missing và kiểu dữ liệu.
16. Xuất dữ liệu sạch:

```python
df.to_csv(
    "sales_clean.csv",
    index=False
)
```

---

# 38. Yêu cầu báo cáo cho bài tập tổng hợp

Người học cần trình bày:

### Phần 1 — Vấn đề dữ liệu

Liệt kê các vấn đề đã phát hiện.

Ví dụ:

```text
- 12 duplicate Order_ID
- 3 cách viết khác nhau của Hanoi
- 4.8% Unit_Price missing
- 5 Quantity âm
- 7 Revenue bất thường
```

### Phần 2 — Quyết định cleaning

Ví dụ:

```text
- duplicate Order_ID → kiểm tra và giữ bản ghi hợp lệ
- Region → chuẩn hóa lowercase và mapping
- Unit_Price → median theo Product
- Quantity âm → điều tra transaction type
```

### Phần 3 — Validation

Báo cáo trạng thái dữ liệu sau cleaning.

---

# 39. Checklist Data Cleaning

Trước khi kết thúc cleaning, có thể kiểm tra:

```text
□ Dữ liệu có duplicate không?
□ Primary key có unique không?
□ Missing values đã được xử lý hợp lý chưa?
□ Data types đã đúng chưa?
□ Date format đã thống nhất chưa?
□ Category labels có nhất quán không?
□ Units có nhất quán không?
□ Có invalid values không?
□ Có outlier cần điều tra không?
□ Các business rules có được thỏa mãn không?
□ Các thay đổi đã được ghi lại chưa?
□ Dữ liệu đã được validation lại chưa?
```

---

# 40. Ưu điểm của Data Cleaning

- Tăng độ chính xác của phân tích.
- Giảm lỗi và dữ liệu không nhất quán.
- Cải thiện chất lượng mô hình.
- Hỗ trợ EDA rõ ràng hơn.
- Làm cho dữ liệu đáng tin cậy hơn.
- Giúp phát hiện vấn đề trong quy trình thu thập dữ liệu.
- Tạo nền tảng tốt cho machine learning.

---

# 41. Hạn chế và chi phí của Data Cleaning

Data Cleaning cũng có các thách thức:

- tốn thời gian;
- yêu cầu hiểu dữ liệu;
- cần domain knowledge;
- có thể làm mất thông tin nếu xử lý quá mạnh;
- khó tự động hóa hoàn toàn;
- cần bảo trì khi nguồn dữ liệu thay đổi.

Một quy trình cleaning quá mạnh có thể:

```text
remove too much data
→ dataset không còn đại diện
→ model học kém
```

Vì vậy, mục tiêu không phải là tạo ra dữ liệu "đẹp hoàn hảo", mà là tạo ra dữ liệu **đáng tin cậy và phù hợp với mục tiêu phân tích**.

---

# 42. Tóm tắt bài học

Các điểm cần ghi nhớ:

- **Data Cleaning là một phần của Data Preprocessing.**
- Mục tiêu của Data Cleaning là cải thiện chất lượng dữ liệu.
- Các vấn đề phổ biến gồm:
  - missing values;
  - duplicates;
  - wrong data types;
  - inconsistent formats;
  - spelling errors;
  - outliers;
  - invalid values.
- `duplicated()` và `drop_duplicates()` dùng để kiểm tra và xử lý bản ghi trùng.
- `isna()` / `isnull()` giúp phát hiện missing values.
- `nunique()` và `value_counts()` rất hữu ích với categorical variables.
- Dữ liệu văn bản cần được chuẩn hóa về khoảng trắng, chữ hoa/thường và nhãn.
- Ngày tháng nên được chuyển sang `datetime`.
- Outlier cần được **phát hiện và đánh giá**, không tự động xóa.
- Mean ± standard deviation và IQR là hai cách phát hiện potential outliers.
- Domain knowledge rất quan trọng trong Data Cleaning.
- Sau khi cleaning, luôn cần **validation**.
- Quy trình cleaning nên được ghi chép và tự động hóa khi phù hợp.
- Scaling là một bước preprocessing liên quan nhưng không phải trọng tâm cốt lõi của Data Cleaning.

---

## Tài liệu tham khảo

1. GeeksforGeeks. *Data Cleaning*. Last Updated: 28 Apr, 2026.
2. Pandas Documentation: missing data, duplicates, string operations, datetime handling.
3. Scikit-learn Documentation: preprocessing and data transformation.
