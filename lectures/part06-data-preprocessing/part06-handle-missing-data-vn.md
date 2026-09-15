# Xử lý giá trị thiếu trong Machine Learning với Python

## Tóm tắt bài học

**Missing values** xuất hiện khi một số giá trị trong tập dữ liệu không được ghi nhận hoặc không có sẵn. Chúng có thể được biểu diễn dưới nhiều dạng như `NaN`, `None`, ô trống hoặc các chuỗi đặc biệt như `"Unknown"`.

Nếu không được xử lý phù hợp, missing values có thể:

- làm giảm độ chính xác của mô hình;
- tạo ra sai lệch trong phân tích;
- làm giảm kích thước mẫu nếu loại bỏ quá nhiều dữ liệu;
- khiến một số thuật toán học máy không thể hoạt động vì yêu cầu dữ liệu đầy đủ.

Bài học này tập trung vào:

1. nguyên nhân dữ liệu bị thiếu;
2. ba loại missingness: MCAR, MAR và MNAR;
3. cách phát hiện missing values bằng Pandas;
4. các chiến lược xóa và thay thế giá trị thiếu;
5. forward fill và backward fill;
6. interpolation;
7. ưu, nhược điểm của từng phương pháp;
8. cách lựa chọn phương pháp phù hợp cho từng loại dữ liệu.

---

# 1. Mục tiêu bài học

Sau bài học này, người học có thể:

- Giải thích được missing values là gì.
- Nêu được các nguyên nhân phổ biến dẫn đến dữ liệu thiếu.
- Phân biệt được MCAR, MAR và MNAR.
- Sử dụng Pandas để phát hiện missing values.
- Nhận diện các cách biểu diễn missing values khác nhau.
- Sử dụng `dropna()` để loại bỏ dữ liệu thiếu.
- Sử dụng `fillna()` để thay thế missing values.
- Áp dụng mean, median và mode imputation.
- Áp dụng forward fill và backward fill.
- Sử dụng interpolation cho dữ liệu có tính thứ tự.
- So sánh ưu và nhược điểm của các chiến lược xử lý missing values.
- Lựa chọn phương pháp xử lý dựa trên loại biến và bản chất dữ liệu bị thiếu.

---

# 2. Missing Values là gì?

Missing values là các giá trị không được quan sát hoặc không được lưu trong dataset.

Ví dụ:

```text
Student    Marks    City
A          85       Hanoi
B          NaN      Hanoi
C          78       None
D          90       Unknown
```

Trong ví dụ này:

- `NaN` là một missing value;
- `None` có thể được Pandas hiểu là missing;
- `"Unknown"` có thể là một nhãn đặc biệt được dùng để biểu diễn thông tin không có sẵn.

Missing values có thể gây vấn đề vì nhiều phép tính và thuật toán yêu cầu dữ liệu đầy đủ.

---

# 3. Vì sao cần xử lý Missing Values?

Nguồn bài học nhấn mạnh bốn lý do chính:

- **Giữ độ chính xác của mô hình**.
- **Giảm nguy cơ bias**.
- **Duy trì kích thước mẫu**.
- **Cho phép sử dụng đúng các thuật toán Machine Learning**.

Ví dụ, nếu một biến quan trọng như:

```text
Income
```

có 30% giá trị bị thiếu, việc bỏ toàn bộ các dòng đó có thể làm mất một phần lớn dữ liệu.

Ngược lại, nếu điền giá trị không phù hợp, ta có thể làm thay đổi phân phối thật của biến.

Do đó, xử lý missing values không chỉ là thao tác kỹ thuật mà còn là một quyết định phân tích.

---

# 4. Nguyên nhân xuất hiện Missing Values

Dữ liệu có thể bị thiếu vì nhiều nguyên nhân khác nhau.

## 4.1. Technical Issues

Ví dụ:

- lỗi cảm biến;
- lỗi truyền dữ liệu;
- hệ thống bị gián đoạn;
- file bị hỏng;
- lỗi trong quá trình import dữ liệu.

---

## 4.2. Human Errors

Ví dụ:

- người nhập dữ liệu bỏ quên một trường;
- người dùng nhập form không đầy đủ;
- lỗi thao tác;
- sai sót trong quá trình tổng hợp dữ liệu.

---

## 4.3. Privacy Concerns

Một số thông tin có thể không được cung cấp vì lý do bảo mật hoặc riêng tư.

Ví dụ:

```text
Income
Health information
Personal identifiers
```

---

## 4.4. Data Processing Issues

Missing values cũng có thể xuất hiện trong quá trình:

- merge dữ liệu;
- chuyển đổi định dạng;
- lọc dữ liệu;
- xử lý dữ liệu từ nhiều nguồn.

---

# 5. Vì sao cần hiểu nguyên nhân dữ liệu bị thiếu?

Hai dataset có cùng tỷ lệ missing values nhưng có thể cần cách xử lý hoàn toàn khác nhau.

Ví dụ:

```text
Income bị thiếu
```

Trường hợp 1:

- thiếu ngẫu nhiên do lỗi hệ thống.

Trường hợp 2:

- người có thu nhập cao có xu hướng không khai báo.

Hai trường hợp này có bản chất khác nhau và có thể tạo ra mức độ bias khác nhau.

Vì vậy, việc hiểu **cơ chế missingness** rất quan trọng.

---

# 6. Ba loại Missing Values

Nguồn bài học chia missing values thành ba loại chính:

1. MCAR
2. MAR
3. MNAR

---

# 7. MCAR — Missing Completely at Random

**MCAR** xảy ra khi việc thiếu dữ liệu hoàn toàn ngẫu nhiên và không liên quan tới bất kỳ biến nào trong dataset.

Ví dụ:

```text
Một số bản ghi bị mất do lỗi truyền dữ liệu ngẫu nhiên.
```

Nếu việc mất dữ liệu thực sự là ngẫu nhiên, các quan sát còn lại vẫn có thể tương đối đại diện cho toàn bộ mẫu.

---

# 8. MAR — Missing at Random

**MAR** xảy ra khi việc thiếu dữ liệu phụ thuộc vào các biến khác đã quan sát được, nhưng không phụ thuộc trực tiếp vào chính giá trị bị thiếu.

Ví dụ:

```text
Income bị thiếu nhiều hơn ở nhóm sinh viên.
```

Ở đây:

```text
Missing Income
```

có liên hệ với:

```text
Occupation = Student
```

là một biến đã quan sát được.

---

# 9. MNAR — Missing Not at Random

**MNAR** xảy ra khi việc thiếu dữ liệu có liên quan trực tiếp đến chính giá trị bị thiếu.

Ví dụ từ nguồn:

```text
Người có thu nhập cao có xu hướng không báo cáo thu nhập.
```

Khi đó:

```text
Income missing
```

phụ thuộc vào:

```text
Income itself
```

Đây thường là dạng khó xử lý hơn vì missingness mang thông tin.

---

# 10. So sánh MCAR, MAR và MNAR

| Loại | Missing phụ thuộc vào | Ví dụ |
|---|---|---|
| MCAR | Không phụ thuộc vào biến nào | Lỗi truyền dữ liệu ngẫu nhiên |
| MAR | Biến khác đã quan sát được | Thu nhập thiếu nhiều ở nhóm sinh viên |
| MNAR | Chính giá trị bị thiếu | Thu nhập cao ít được khai báo |

Điểm quan trọng:

> Cùng là missing values nhưng cách xử lý có thể khác nhau tùy cơ chế thiếu dữ liệu.

---

# 11. Biểu diễn Missing Values trong Dataset

Missing values có thể xuất hiện dưới nhiều dạng.

## 11.1. Blank Cells

Ví dụ trong Excel hoặc CSV:

```text
Name,Age,City
A,25,Hanoi
B,,Hanoi
C,31,
```

---

## 11.2. Special Values

Ví dụ:

```text
NA
NaN
NULL
-999
```

---

## 11.3. Codes hoặc Flags

Ví dụ:

```text
MISSING
UNKNOWN
NOT AVAILABLE
```

Một bước quan trọng của Data Cleaning là chuẩn hóa các cách biểu diễn này.

---

# 12. Các hàm Pandas hữu ích

Nguồn bài học đề cập các hàm sau:

| Hàm | Mục đích |
|---|---|
| `.isnull()` | Phát hiện missing values |
| `.notnull()` | Phát hiện non-missing values |
| `.info()` | Tóm tắt dataset và số lượng non-null |
| `.isna()` | Tương đương `isnull()` |
| `dropna()` | Xóa dòng hoặc cột chứa missing values |
| `fillna()` | Điền missing values |
| `replace()` | Thay thế một số giá trị |
| `drop_duplicates()` | Xóa duplicate rows |
| `unique()` | Xem các giá trị duy nhất |

---

# 13. Tạo DataFrame mẫu

Nguồn sử dụng dữ liệu mẫu sau:

```python
import pandas as pd
import numpy as np

data = {
    "School ID": [
        101, 102, 103, np.nan,
        105, 106, 107, 108
    ],
    "Name": [
        "A", "B", "C", "D",
        "E", "F", "G", "H"
    ],
    "Address": [
        "123 Main St",
        "456 Oak Ave",
        "789 Pine Ln",
        "101 Elm St",
        np.nan,
        "222 Maple Rd",
        "444 Cedar Blvd",
        "555 Birch Dr"
    ],
    "City": [
        "Mumbai",
        "Delhi",
        "Bengaluru",
        "Chennai",
        "Kolkata",
        np.nan,
        "Pune",
        "Jaipur"
    ],
    "Subject": [
        "Math",
        "English",
        "Science",
        "Math",
        "History",
        "Math",
        "Science",
        "English"
    ],
    "Marks": [
        85, 92, 78, 89,
        np.nan, 95, 80, 88
    ],
    "Rank": [
        2, 1, 4, 3,
        8, 1, 5, 3
    ],
    "Grade": [
        "B", "A", "C", "B",
        "D", "A", "C", "B"
    ]
}

df = pd.DataFrame(data)

print(df)
```

Các cột có missing values gồm:

```text
School ID
Address
City
Marks
```

---

# 14. Phát hiện Missing Values

## 14.1. `isnull()`

```python
df.isnull()
```

Kết quả là DataFrame Boolean:

```text
True  → missing
False → có dữ liệu
```

---

## 14.2. Đếm Missing Values theo cột

```python
df.isnull().sum()
```

Hoặc:

```python
df.isna().sum()
```

---

## 14.3. Tính tỷ lệ Missing Values

```python
missing_percent = (
    df.isna().sum()
    / len(df)
    * 100
)

print(missing_percent)
```

---

## 14.4. Kiểm tra non-missing values

```python
df.notnull()
```

Hoặc đếm:

```python
df.notnull().sum()
```

---

# 15. Bài tập nhỏ — Phát hiện Missing Values

Với DataFrame `df`, hãy:

1. Đếm số missing values trong từng cột.
2. Tính tỷ lệ phần trăm missing.
3. Liệt kê các cột có ít nhất một missing value.
4. Liệt kê các dòng có ít nhất một missing value.

Gợi ý:

```python
df.________().sum()

df.columns[
    df.________().any()
]

df[
    df.________().any(axis=1)
]
```

---

# 16. Chiến lược 1 — Xóa các dòng có Missing Values

Phương pháp đơn giản nhất là loại bỏ các dòng chứa missing values.

```python
df_cleaned = df.dropna()

print(df_cleaned)
```

Ưu điểm:

- đơn giản;
- nhanh;
- tạo ra dataset hoàn chỉnh.

Nhược điểm:

- mất dữ liệu;
- giảm kích thước mẫu;
- có thể tạo bias nếu missingness không ngẫu nhiên.

---

# 17. Khi nào có thể dùng `dropna()`?

Có thể cân nhắc khi:

- tỷ lệ missing rất nhỏ;
- số lượng dữ liệu đủ lớn;
- các dòng bị thiếu không có đặc điểm hệ thống;
- việc loại bỏ không làm thay đổi đáng kể mẫu.

Ví dụ:

```text
10,000 records
5 records bị thiếu
```

việc loại 5 dòng có thể ít ảnh hưởng.

Nhưng nếu:

```text
1,000 records
300 records bị thiếu
```

thì loại bỏ có thể gây mất nhiều thông tin.

---

# 18. `dropna()` theo một cột cụ thể

Ví dụ:

```python
df2 = df.dropna(
    subset=["Marks"]
)
```

Chỉ những dòng có `Marks` bị thiếu mới bị loại.

---

# 19. Xóa cột có quá nhiều Missing Values

Ví dụ:

```python
df2 = df.drop(
    columns=["Address"]
)
```

Có thể cân nhắc khi:

- cột thiếu quá nhiều;
- biến không quan trọng;
- khó hoặc không thể impute hợp lý.

Tuy nhiên, tỷ lệ missing cao không tự động có nghĩa là phải xóa cột.

---

# 20. Chiến lược 2 — Imputation

**Imputation** là quá trình thay missing values bằng các giá trị ước lượng.

Mục tiêu:

- giữ lại số lượng quan sát;
- tránh mất dữ liệu;
- tạo dataset có thể dùng cho phân tích hoặc modeling.

Nguồn bài học trình bày các phương pháp:

- mean;
- median;
- mode;
- forward fill;
- backward fill;
- interpolation.

---

# 21. Mean Imputation

Điền missing values bằng mean:

```python
mean_imputation = df["Marks"].fillna(
    df["Marks"].mean()
)

print(mean_imputation)
```

Ví dụ:

```text
Marks = 85, 92, 78, 89, NaN, 95, 80, 88
```

Missing value sẽ được thay bằng mean của các giá trị còn lại.

---

# 22. Ưu và nhược điểm của Mean Imputation

Ưu điểm:

- đơn giản;
- nhanh;
- dễ hiểu;
- phù hợp với biến số trong một số trường hợp.

Nhược điểm:

- không sử dụng mối quan hệ với các biến khác;
- có thể làm giảm variability;
- có thể làm thay đổi phân phối thật;
- nhạy với outliers.

---

# 23. Median Imputation

```python
median_imputation = df["Marks"].fillna(
    df["Marks"].median()
)
```

Median là giá trị ở giữa khi dữ liệu được sắp xếp.

Median thường phù hợp hơn mean khi dữ liệu:

- lệch;
- có extreme values;
- có outliers.

---

# 24. Mode Imputation

```python
mode_imputation = df["Marks"].fillna(
    df["Marks"].mode().iloc[0]
)
```

`.mode()` trả về một Series vì một biến có thể có nhiều mode.

`.iloc[0]` lấy mode đầu tiên.

Mode đặc biệt hữu ích với categorical variables.

Ví dụ:

```python
df["City"] = df["City"].fillna(
    df["City"].mode().iloc[0]
)
```

---

# 25. So sánh Mean, Median và Mode

| Phương pháp | Phù hợp với | Ghi chú |
|---|---|---|
| Mean | Biến số tương đối cân đối | Nhạy với outliers |
| Median | Biến số lệch hoặc có outliers | Robust hơn mean |
| Mode | Biến phân loại hoặc biến rời rạc | Dùng giá trị xuất hiện nhiều nhất |

Không nên sử dụng một phương pháp cho tất cả các cột.

---

# 26. Ví dụ lựa chọn Imputation

Giả sử có các biến:

```text
Age
Income
Region
Customer_Type
```

Có thể cân nhắc:

```text
Age          → median
Income       → median
Region       → mode
Customer_Type→ mode
```

Quyết định cuối cùng vẫn phụ thuộc vào dữ liệu cụ thể.

---

# 27. Hạn chế chung của Simple Imputation

Nguồn bài học nhấn mạnh rằng mean, median và mode imputation:

> không xét đến mối quan hệ giữa các biến.

Ví dụ, nếu `Marks` phụ thuộc mạnh vào:

```text
Subject
Grade
Rank
```

thì điền một mean chung cho toàn bộ học sinh có thể không phản ánh đúng dữ liệu.

---

# 28. Chiến lược 3 — Forward Fill

Forward fill sử dụng giá trị hợp lệ gần nhất trước đó.

Theo ví dụ nguồn:

```python
forward_fill = df["Marks"].fillna(
    method="ffill"
)

print(forward_fill)
```

Ý tưởng:

```text
85
92
78
89
NaN
95
```

sẽ thành:

```text
85
92
78
89
89
95
```

Missing value được thay bằng giá trị trước đó.

---

# 29. Khi nào Forward Fill hữu ích?

Nguồn bài học cho rằng forward fill phù hợp với dữ liệu:

- có thứ tự;
- time series;
- các quan sát liên tiếp có mối liên hệ.

Ví dụ:

```text
Date        Temperature
Day 1       30
Day 2       31
Day 3       NaN
Day 4       32
```

Forward fill có thể dùng giá trị Day 2 để điền Day 3.

---

# 30. Hạn chế của Forward Fill

Forward fill có thể không phù hợp khi:

- khoảng missing quá dài;
- dữ liệu thay đổi nhanh;
- thứ tự dòng không có ý nghĩa;
- giá trị trước không liên quan tới giá trị sau.

Ví dụ:

```text
Customer 1
Customer 2
Customer 3
```

nếu các customer độc lập nhau, dùng giá trị của Customer 2 để điền cho Customer 3 có thể không hợp lý.

---

# 31. Chiến lược 4 — Backward Fill

Backward fill sử dụng giá trị hợp lệ tiếp theo.

```python
backward_fill = df["Marks"].fillna(
    method="bfill"
)

print(backward_fill)
```

Ví dụ:

```text
85
92
78
89
NaN
95
```

sẽ thành:

```text
85
92
78
89
95
95
```

---

# 32. Forward Fill và Backward Fill

| Phương pháp | Nguồn giá trị điền |
|---|---|
| Forward Fill | Giá trị hợp lệ trước đó |
| Backward Fill | Giá trị hợp lệ tiếp theo |

Cả hai đều tận dụng tính thứ tự của dữ liệu.

---

# 33. Chiến lược 5 — Interpolation

Interpolation ước lượng missing values dựa trên xu hướng của các điểm xung quanh.

Nguồn bài học sử dụng hai dạng:

- linear interpolation;
- quadratic interpolation.

---

# 34. Linear Interpolation

```python
linear_interpolation = df["Marks"].interpolate(
    method="linear"
)

print(linear_interpolation)
```

Linear interpolation giả định một đường thẳng giữa hai điểm dữ liệu lân cận.

Ví dụ:

```text
10
20
NaN
40
```

linear interpolation có thể ước lượng:

```text
30
```

---

# 35. Quadratic Interpolation

```python
quadratic_interpolation = df["Marks"].interpolate(
    method="quadratic"
)

print(quadratic_interpolation)
```

Quadratic interpolation sử dụng quan hệ dạng đường cong bậc hai qua các điểm lân cận.

Phương pháp này có thể mô tả xu hướng phi tuyến tốt hơn linear interpolation trong một số trường hợp.

---

# 36. Ưu và nhược điểm của Interpolation

Ưu điểm:

- tận dụng xu hướng dữ liệu;
- có thể bảo toàn pattern tốt hơn simple imputation;
- phù hợp với dữ liệu có thứ tự.

Nhược điểm:

- giả định tồn tại một dạng pattern;
- kết quả phụ thuộc vào phương pháp interpolation;
- có thể không phù hợp nếu dữ liệu không có thứ tự;
- có thể phức tạp hơn mean/median imputation.

---

# 37. Khi nào Interpolation phù hợp?

Ví dụ tốt:

```text
Time Series
Sensor Data
Temperature
Sales by Time
Traffic Volume
```

Ví dụ không phù hợp:

```text
Danh sách khách hàng độc lập không có thứ tự
```

Nếu dòng 10 và dòng 11 là hai người khác nhau, việc nội suy từ một người sang người khác thường không có ý nghĩa.

---

# 38. So sánh các chiến lược xử lý Missing Values

| Phương pháp | Ưu điểm | Hạn chế |
|---|---|---|
| Drop rows | Đơn giản, dataset đầy đủ | Mất dữ liệu, có thể bias |
| Mean | Nhanh, dễ dùng | Nhạy outlier, giảm variability |
| Median | Robust hơn mean | Không dùng quan hệ giữa biến |
| Mode | Phù hợp categorical | Có thể làm tăng quá mức nhóm phổ biến |
| Forward fill | Giữ tính liên tục | Không phù hợp gap lớn |
| Backward fill | Đơn giản với ordered data | Dùng thông tin phía sau |
| Interpolation | Bám theo trend | Phụ thuộc giả định về pattern |

---

# 39. Chọn phương pháp nào?

Không có một phương pháp đúng cho mọi dataset.

Có thể dùng quy trình:

```text
1. Xác định biến nào bị thiếu
2. Đo tỷ lệ missing
3. Xác định loại biến
4. Hiểu nguyên nhân missing
5. Xác định dữ liệu có thứ tự hay không
6. Chọn phương pháp phù hợp
7. Kiểm tra lại phân phối sau xử lý
```

---

# 40. Ví dụ quyết định theo loại dữ liệu

## Biến số, tương đối cân đối

```text
Age
```

Có thể thử:

```text
Mean
```

---

## Biến số, lệch

```text
Income
```

Có thể ưu tiên:

```text
Median
```

---

## Biến phân loại

```text
Region
```

Có thể dùng:

```text
Mode
```

hoặc nhãn:

```text
Unknown
```

---

## Time Series

```text
Daily Sales
```

Có thể cân nhắc:

```text
Forward fill
Backward fill
Interpolation
```

---

# 41. Kiểm tra Missing Values sau khi xử lý

Luôn kiểm tra lại:

```python
df.isna().sum()
```

Nếu muốn xác nhận không còn missing:

```python
print(
    df.isna().sum().sum()
)
```

Nếu kết quả là:

```text
0
```

thì không còn missing values theo cách Pandas nhận diện.

---

# 42. Missing Values có thể được mã hóa sai

Ví dụ:

```text
Age
25
31
999
28
```

Nếu `999` thực chất có nghĩa là missing thì:

```python
df.isna().sum()
```

sẽ không phát hiện được.

Có thể chuẩn hóa:

```python
df["Age"] = df["Age"].replace(
    999,
    np.nan
)
```

Sau đó:

```python
df.isna().sum()
```

---

# 43. Dùng `replace()` để chuẩn hóa Missing Codes

Ví dụ:

```python
df = df.replace(
    [
        "Unknown",
        "UNKNOWN",
        "N/A",
        "NULL",
        -999
    ],
    np.nan
)
```

Sau đó dataset có một cách biểu diễn missing nhất quán.

---

# 44. Ví dụ trong bối cảnh kinh doanh

Giả sử có dữ liệu khách hàng:

```text
Customer_ID
Age
Income
Region
Monthly_Spending
Churn
```

Một số vấn đề:

```text
Age thiếu 2%
Income thiếu 20%
Region thiếu 1%
Monthly_Spending thiếu 5%
```

Có thể đặt câu hỏi:

- `Age` thiếu ngẫu nhiên hay có liên quan tới nhóm tuổi?
- `Income` thiếu có phải do khách hàng không muốn khai báo?
- `Region` có thể điền bằng mode không?
- `Monthly_Spending` có tính thứ tự theo thời gian hay chỉ là giá trị tổng hợp?

Cùng một tỷ lệ missing nhưng cách xử lý có thể khác nhau.

---

# 45. Ví dụ trong dữ liệu chuỗi thời gian

Dữ liệu:

```text
Date        Sales
01-01       100
01-02       110
01-03       NaN
01-04       130
```

Có thể dùng:

```python
df["Sales_linear"] = (
    df["Sales"]
    .interpolate(method="linear")
)
```

Kết quả dự kiến:

```text
100
110
120
130
```

Trong trường hợp này interpolation có ý nghĩa vì `Date` tạo ra thứ tự thời gian.

---

# 46. Ví dụ trong dữ liệu học sinh

Dữ liệu:

```text
Subject    Marks
Math       85
English    90
Science    NaN
History    70
```

Nếu các dòng không có quan hệ thứ tự, forward fill:

```text
Science = 90
```

không nhất thiết hợp lý.

Có thể cân nhắc:

- median của `Marks`;
- mean theo nhóm;
- một mô hình imputation khác.

Điểm quan trọng là lựa chọn phương pháp phải dựa trên cấu trúc dữ liệu.

---

# 47. Tác động của xử lý Missing Values

Nguồn bài học nêu bốn tác động chính.

## 47.1. Improved Data Quality

Dataset có ít missing values hơn và nhất quán hơn.

---

## 47.2. Enhanced Model Performance

Nhiều mô hình hoạt động tốt hơn khi được huấn luyện trên dữ liệu đầy đủ.

---

## 47.3. Preservation of Data Integrity

Imputation hoặc removal hợp lý giúp duy trì dữ liệu ở trạng thái phù hợp cho phân tích.

---

## 47.4. Reduced Bias

Xử lý đúng missing values giúp hạn chế sai lệch trong phân tích và mô hình hóa.

---

# 48. Những sai lầm phổ biến

## 48.1. Xóa tất cả các dòng có Missing Values

Có thể làm mất quá nhiều dữ liệu.

---

## 48.2. Luôn dùng Mean

Không phù hợp với:

- categorical variables;
- dữ liệu lệch;
- dữ liệu có outliers.

---

## 48.3. Dùng Forward Fill cho dữ liệu không có thứ tự

Nếu các dòng độc lập nhau, việc lấy giá trị từ dòng trước có thể vô nghĩa.

---

## 48.4. Không chuẩn hóa Missing Codes

Nếu:

```text
NaN
Unknown
-999
NULL
```

đều đại diện cho missing nhưng không được chuẩn hóa, kết quả kiểm tra sẽ sai.

---

## 48.5. Không kiểm tra lại sau khi Imputation

Sau khi xử lý nên kiểm tra:

```text
missing count
distribution
mean
median
minimum
maximum
```

---

# 49. Bài tập thực hành 1 — Phát hiện Missing Values

Cho DataFrame:

```python
data = {
    "Customer_ID": [1, 2, 3, 4, 5],
    "Age": [25, np.nan, 31, 40, np.nan],
    "Income": [10, 15, np.nan, 30, 25],
    "Region": [
        "North",
        "South",
        np.nan,
        "North",
        "Central"
    ]
}

df = pd.DataFrame(data)
```

Yêu cầu:

1. In dataset.
2. Đếm missing values theo cột.
3. Tính tỷ lệ missing.
4. Xác định dòng có missing.

---

# 50. Bài tập thực hành 2 — Mean, Median, Mode

Với DataFrame ở trên:

1. Điền `Age` bằng median.
2. Điền `Income` bằng mean.
3. Điền `Region` bằng mode.
4. Kiểm tra lại missing values.

Gợi ý:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].________()
)

df["Income"] = df["Income"].fillna(
    df["Income"].________()
)

df["Region"] = df["Region"].fillna(
    df["Region"].________().iloc[0]
)
```

---

# 51. Bài tập thực hành 3 — Forward và Backward Fill

Cho:

```python
sales = pd.Series(
    [100, 120, np.nan, np.nan, 160]
)
```

Hãy tạo:

```text
sales_ffill
sales_bfill
```

Sau đó so sánh kết quả.

Câu hỏi:

- Phương pháp nào dùng giá trị 120 để điền?
- Phương pháp nào dùng giá trị 160 để điền?
- Nếu hai giá trị thiếu đại diện cho hai tháng liên tiếp, phương pháp nào có thể hợp lý hơn?

---

# 52. Bài tập thực hành 4 — Interpolation

Cho:

```python
temperature = pd.Series(
    [20, 22, np.nan, 26, 28]
)
```

Thực hiện linear interpolation.

Dự đoán giá trị tại vị trí bị thiếu trước khi chạy code.

---

# 53. Bài tập thực hành 5 — Chuẩn hóa Missing Codes

Cho:

```python
data = {
    "Income": [
        20,
        "Unknown",
        35,
        -999,
        "NULL"
    ]
}

df = pd.DataFrame(data)
```

Yêu cầu:

1. Chuyển `"Unknown"`, `"NULL"` và `-999` thành `np.nan`.
2. Chuyển `Income` về numeric.
3. Đếm missing values.
4. Chọn một phương pháp imputation phù hợp.

---

# 54. Tự kiểm tra

### Câu 1

Missing values có thể xuất hiện dưới dạng nào?

A. `NaN`  
B. `None`  
C. `"Unknown"`  
D. Tất cả các đáp án trên

---

### Câu 2

MCAR có nghĩa là gì?

A. Missing phụ thuộc vào chính giá trị bị thiếu  
B. Missing hoàn toàn ngẫu nhiên  
C. Missing phụ thuộc vào một biến đã quan sát được

---

### Câu 3

Ví dụ nào gần với MNAR nhất?

A. Dữ liệu bị mất vì lỗi truyền mạng ngẫu nhiên  
B. Thu nhập bị thiếu nhiều hơn ở sinh viên  
C. Người thu nhập cao có xu hướng không khai báo thu nhập

---

### Câu 4

Lệnh nào dùng để đếm missing values?

A.

```python
df.isna().sum()
```

B.

```python
df.countna()
```

C.

```python
df.missing()
```

---

### Câu 5

Nhược điểm lớn của `dropna()` là gì?

---

### Câu 6

Median imputation thường phù hợp hơn mean khi nào?

---

### Câu 7

Mode imputation thường phù hợp với loại biến nào?

---

### Câu 8

Forward fill khác backward fill như thế nào?

---

### Câu 9

Interpolation đặc biệt phù hợp với dạng dữ liệu nào?

---

### Câu 10

Tại sao `"Unknown"` không phải lúc nào cũng được Pandas tự động nhận diện là missing?

---

# 55. Bài tập tổng hợp — Missing Values trong dữ liệu khách hàng

Cho dataset:

```text
customer_data.csv
```

với các cột:

```text
Customer_ID
Age
Income
Region
Monthly_Spending
Join_Date
Churn
```

Yêu cầu:

1. Đọc dữ liệu.
2. Kiểm tra `info()`.
3. Đếm missing values.
4. Tính missing percentage.
5. Kiểm tra các missing codes như:
   - `"Unknown"`
   - `"NULL"`
   - `-999`
6. Chuẩn hóa về `np.nan`.
7. Xác định biến số và biến phân loại.
8. Đề xuất cách xử lý missing cho từng biến.
9. Thực hiện imputation phù hợp.
10. Kiểm tra lại missing values.
11. So sánh thống kê mô tả trước và sau imputation.
12. Giải thích vì sao phương pháp được chọn là phù hợp.

---

# 56. Yêu cầu báo cáo cho bài tập tổng hợp

Người học cần trình bày:

## Phần 1 — Missing Profile

Ví dụ:

```text
Age: 3.2%
Income: 18.7%
Region: 1.4%
Monthly_Spending: 7.1%
```

## Phần 2 — Cơ chế Missingness

Đưa ra nhận định ban đầu:

```text
MCAR?
MAR?
MNAR?
```

và giải thích.

## Phần 3 — Chiến lược xử lý

Ví dụ:

```text
Age → median
Income → median
Region → mode
Monthly_Spending → interpolation nếu có thứ tự thời gian
```

## Phần 4 — Kiểm tra sau xử lý

So sánh:

```text
mean
median
std
distribution
missing count
```

trước và sau imputation.

---

# 57. Checklist xử lý Missing Values

```text
□ Tôi đã xác định những cột bị thiếu chưa?
□ Tôi đã tính tỷ lệ missing chưa?
□ Tôi đã kiểm tra các missing codes đặc biệt chưa?
□ Tôi đã xác định loại biến chưa?
□ Tôi đã xem xét MCAR/MAR/MNAR chưa?
□ Tôi đã cân nhắc xóa so với imputation chưa?
□ Tôi đã chọn mean/median/mode phù hợp chưa?
□ Tôi chỉ dùng ffill/bfill khi dữ liệu có thứ tự chưa?
□ Tôi chỉ dùng interpolation khi có pattern hợp lý chưa?
□ Tôi đã kiểm tra dữ liệu sau xử lý chưa?
```

---

# 58. Tóm tắt bài học

Các điểm cần nhớ:

- Missing values có thể được biểu diễn bằng `NaN`, `None`, ô trống hoặc các special codes.
- Nguyên nhân missing có thể đến từ kỹ thuật, con người, privacy hoặc data processing.
- Ba loại missingness quan trọng là:
  - MCAR;
  - MAR;
  - MNAR.
- `isnull()` và `isna()` dùng để phát hiện missing values.
- `dropna()` loại bỏ dữ liệu thiếu nhưng có thể làm giảm sample size.
- `fillna()` hỗ trợ nhiều chiến lược imputation.
- Mean, median và mode là các phương pháp đơn giản, nhanh nhưng không xét quan hệ giữa các biến.
- Forward fill dùng giá trị trước đó.
- Backward fill dùng giá trị tiếp theo.
- Interpolation dùng pattern giữa các điểm dữ liệu để ước lượng giá trị thiếu.
- Không có một phương pháp xử lý missing values phù hợp cho mọi dataset.
- Lựa chọn phương pháp cần dựa vào:
  - nguyên nhân missing;
  - loại biến;
  - tỷ lệ missing;
  - cấu trúc dữ liệu;
  - mục tiêu phân tích.
- Sau khi xử lý, luôn cần kiểm tra lại dataset.

---

## Tài liệu tham khảo

GeeksforGeeks. *Handling Missing Values in Machine Learning*. Last Updated: 3 Dec, 2025.
