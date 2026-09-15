# Phát hiện và xử lý Outliers bằng Python

## Tóm tắt bài học

**Outliers** là các điểm dữ liệu khác biệt đáng kể so với phần lớn các quan sát còn lại trong tập dữ liệu. Chúng có thể xuất hiện do:

- lỗi đo lường;
- lỗi nhập dữ liệu;
- các sự kiện bất thường;
- hoặc đơn giản là biến thiên tự nhiên của dữ liệu.

Nếu không được xem xét cẩn thận, outliers có thể ảnh hưởng đến:

- thống kê mô tả;
- mối quan hệ giữa các biến;
- kết quả phân tích;
- và hiệu năng của mô hình Machine Learning.

Bài học này trình bày các phương pháp phát hiện và xử lý outliers bằng Python, tập trung vào:

1. Box Plot.
2. Scatter Plot.
3. Z-score.
4. Interquartile Range (IQR).
5. Trimming.
6. Capping.

Ví dụ minh họa sử dụng **Diabetes dataset** có sẵn trong `scikit-learn`.

---

# 1. Mục tiêu bài học

Sau bài học này, người học có thể:

- Giải thích được outlier là gì.
- Nêu được một số nguyên nhân tạo ra outliers.
- Sử dụng box plot để quan sát outliers.
- Sử dụng scatter plot để phát hiện các điểm bất thường giữa hai biến.
- Tính Z-score và dùng Z-score để phát hiện outliers.
- Tính IQR và xác định upper/lower bounds.
- Phân biệt trimming và capping.
- Viết mã Python để loại bỏ outliers.
- Viết mã Python để giới hạn giá trị cực đoan bằng capping.
- Hiểu rằng outlier không phải lúc nào cũng là dữ liệu sai.
- So sánh các phương pháp phát hiện outliers theo đặc điểm dữ liệu.

---

# 2. Outlier là gì?

Outlier là một quan sát có giá trị rất khác so với phần lớn các quan sát còn lại.

Ví dụ:

```text
10, 12, 11, 13, 12, 100
```

Giá trị:

```text
100
```

khác biệt rất lớn so với các giá trị còn lại và có thể được xem là một outlier.

Outlier có thể xuất hiện do:

```text
Measurement error
Data entry error
Unusual event
Natural variation
```

Ví dụ trong kinh doanh:

```text
Revenue
12
15
11
14
420
```

Giá trị `420` có thể là:

- lỗi nhập liệu;
- một khách hàng doanh nghiệp rất lớn;
- một giao dịch đặc biệt;
- hoặc một sự kiện bất thường.

Vì vậy:

> **Phát hiện outlier không đồng nghĩa với việc phải xóa outlier.**

---

# 3. Vì sao cần phát hiện Outliers?

Outliers có thể ảnh hưởng đến nhiều bước phân tích.

Ví dụ:

```text
10, 11, 12, 13, 100
```

Mean:

```text
29.2
```

Trong khi phần lớn dữ liệu chỉ nằm khoảng:

```text
10–13
```

Một giá trị cực đoan có thể làm:

- mean bị kéo lệch;
- standard deviation tăng;
- regression line thay đổi;
- correlation thay đổi;
- khoảng cách giữa các điểm bị ảnh hưởng.

Một số Machine Learning algorithms nhạy với outliers hơn các mô hình khác.

---

# 4. Bộ dữ liệu minh họa

Nguồn sử dụng **Diabetes dataset** từ `scikit-learn`.

```python
from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()

column_name = diabetes.feature_names

df_diabetics = pd.DataFrame(
    diabetes.data,
    columns=column_name
)

df_diabetics.head()
```

Các biến gồm:

```text
age
sex
bmi
bp
s1
s2
s3
s4
s5
s6
```

Trong bài học, các ví dụ chủ yếu tập trung vào:

```text
age
bmi
bp
```

---

# 5. Kiểm tra cấu trúc dữ liệu

Trước khi phát hiện outliers:

```python
df_diabetics.info()
```

Thống kê mô tả:

```python
df_diabetics.describe()
```

Các thống kê như:

```text
mean
std
min
25%
50%
75%
max
```

giúp quan sát sơ bộ các giá trị cực đoan.

---

# 6. Phương pháp 1 — Box Plot

Box plot biểu diễn phân phối dữ liệu dựa trên các quartiles.

Ví dụ:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(
    x=df_diabetics["bmi"]
)

plt.title("Boxplot of BMI")
plt.show()
```

Trong box plot:

- phần hộp biểu diễn vùng dữ liệu trung tâm;
- đường giữa hộp thường biểu diễn median;
- whiskers mở rộng ra hai phía;
- các điểm nằm ngoài whiskers thường được xem là potential outliers.

---

# 7. Đọc Box Plot

Một box plot thường liên quan đến:

```text
Q1
Median
Q3
IQR
Whiskers
Potential Outliers
```

Nguồn minh họa rằng các giá trị BMI lớn hơn khoảng:

```text
0.12
```

có thể được xem xét như các outliers trong biểu đồ ví dụ.

Lưu ý:

> `0.12` ở đây là một ngưỡng được chọn từ quan sát biểu đồ trong ví dụ nguồn, không phải một quy tắc chung cho mọi dataset.

---

# 8. Loại Outliers từ Box Plot bằng Threshold

Nguồn sử dụng một hàm:

```python
def removal_box_plot(
    df,
    column,
    threshold
):
    removed_outliers = df[
        df[column] <= threshold
    ]

    sns.boxplot(
        x=removed_outliers[column]
    )

    plt.title(
        f"Box Plot without Outliers of {column}"
    )

    plt.show()

    return removed_outliers
```

Sau đó đặt:

```python
threshold_value = 0.12
```

và:

```python
no_outliers = removal_box_plot(
    df_diabetics,
    "bmi",
    threshold_value
)
```

---

# 9. Ý nghĩa của Threshold Filtering

Điều kiện:

```python
df[column] <= threshold
```

có nghĩa là:

```text
Giữ các quan sát có giá trị không vượt quá threshold.
```

Ví dụ:

```python
df[
    df["bmi"] <= 0.12
]
```

sẽ loại các quan sát có:

```text
bmi > 0.12
```

### Hạn chế

Cách làm này phụ thuộc vào:

```text
threshold
```

Nếu threshold được chọn chỉ bằng mắt mà không có cơ sở thống kê hoặc nghiệp vụ, kết quả có thể thiếu nhất quán.

---

# 10. Bài tập nhỏ — Box Plot

Viết mã để:

1. Vẽ box plot cho `bp`.
2. Quan sát các điểm nằm ngoài whiskers.
3. Không xóa dữ liệu ngay.
4. Ghi nhận các giá trị cần kiểm tra thêm.

Gợi ý:

```python
sns.________(
    x=df_diabetics["bp"]
)

plt.________(
    "Boxplot of Blood Pressure"
)

plt.show()
```

---

# 11. Phương pháp 2 — Scatter Plot

Scatter plot giúp quan sát mối quan hệ giữa hai numerical variables.

Nguồn sử dụng:

```python
fig, ax = plt.subplots(
    figsize=(6, 4)
)

ax.scatter(
    df_diabetics["bmi"],
    df_diabetics["bp"]
)

ax.set_xlabel("BMI")
ax.set_ylabel("Blood Pressure")

plt.title(
    "Scatter Plot of BMI vs Blood Pressure"
)

plt.show()
```

---

# 12. Phát hiện Outlier từ Scatter Plot

Trong scatter plot, các điểm:

```text
nằm xa cụm dữ liệu chính
```

có thể được xem là potential outliers.

Ví dụ:

```text
BMI cao
Blood Pressure khác biệt đáng kể
```

có thể xuất hiện ở vùng xa phần lớn các quan sát.

Scatter plot đặc biệt hữu ích khi outlier chỉ bất thường khi xem **mối quan hệ giữa hai biến**.

---

# 13. Outlier đơn biến và đa biến

Một quan sát có thể:

- không quá bất thường nếu chỉ nhìn một biến;
- nhưng bất thường khi xét kết hợp hai biến.

Ví dụ:

```text
BMI = 0.10
BP = -0.05
```

có thể không quá cực đoan riêng lẻ.

Nhưng tổ hợp:

```text
BMI rất cao + BP rất thấp
```

có thể hiếm.

Đây là lý do scatter plot hữu ích.

---

# 14. Tìm các Outlier bằng `np.where()`

Nguồn sử dụng:

```python
import numpy as np

outlier_indices = np.where(
    (df_diabetics["bmi"] > 0.12)
    &
    (df_diabetics["bp"] < 0.8)
)
```

`np.where()` trả về các vị trí thỏa điều kiện.

Sau đó:

```python
no_outliers = df_diabetics.drop(
    outlier_indices[0]
)
```

---

# 15. Minh họa sau khi loại Outlier

```python
fig, ax = plt.subplots(
    figsize=(6, 4)
)

ax.scatter(
    no_outliers["bmi"],
    no_outliers["bp"]
)

ax.set_xlabel("BMI")
ax.set_ylabel("Blood Pressure")

plt.show()
```

Mục tiêu là so sánh phân bố dữ liệu:

```text
Before removal
vs
After removal
```

---

# 16. Lưu ý về điều kiện trong Scatter Plot

Điều kiện:

```python
(df_diabetics["bmi"] > 0.12)
&
(df_diabetics["bp"] < 0.8)
```

là điều kiện cụ thể của ví dụ.

Nó không phải là công thức chung để phát hiện outlier.

Một dataset khác cần:

- threshold khác;
- biến khác;
- hoặc phương pháp khác.

---

# 17. Phương pháp 3 — Z-score

**Z-score** cho biết một giá trị cách mean bao nhiêu standard deviations.

Công thức:

$$
z = \frac{x-\mu}{\sigma}
$$

Trong đó:

- \(x\): giá trị quan sát;
- \(\mu\): mean;
- \(\sigma\): standard deviation.

---

# 18. Tính Z-score bằng SciPy

Nguồn sử dụng:

```python
from scipy import stats
import numpy as np

z = np.abs(
    stats.zscore(
        df_diabetics["age"]
    )
)

print(z)
```

`np.abs()` lấy trị tuyệt đối để chỉ quan tâm tới khoảng cách so với mean, bất kể phía trên hay dưới.

---

# 19. Diễn giải Z-score

Ví dụ:

```text
z = 0
```

giá trị gần mean.

```text
z = 1
```

cách mean khoảng 1 standard deviation.

```text
z = 3
```

cách mean khoảng 3 standard deviations.

Nguồn giải thích rằng ngưỡng outlier thường được đặt:

```text
3.0
```

do với phân phối chuẩn, khoảng 99.7% dữ liệu nằm trong:

```text
±3 standard deviations
```

---

# 20. Lưu ý quan trọng về ngưỡng Z-score trong nguồn

Trong phần giải thích, nguồn nói:

```text
threshold ≈ 3
```

nhưng ví dụ code trimming/capping tiếp theo sử dụng:

```python
threshold_z = 2
```

Hai giá trị này không giống nhau.

Trong bài thực hành:

- `3` có thể được xem là quy tắc phổ biến hơn đối với dữ liệu gần Gaussian;
- `2` là ngưỡng cụ thể được dùng trong ví dụ nguồn để loại nhiều điểm hơn.

Người học cần hiểu rằng:

> **Threshold là một tham số cần lựa chọn, không phải một hằng số bắt buộc.**

---

# 21. Trimming bằng Z-score

Nguồn sử dụng:

```python
threshold_z = 2

outlier_indices = np.where(
    z > threshold_z
)[0]

no_outliers = df_diabetics.drop(
    outlier_indices
)

print(
    "Original DataFrame Shape:",
    df_diabetics.shape
)

print(
    "DataFrame Shape after Removing Outliers:",
    no_outliers.shape
)
```

Kết quả trong nguồn:

```text
Original DataFrame Shape: (442, 10)
DataFrame Shape after Removing Outliers: (426, 10)
```

---

# 22. Trimming là gì?

**Trimming** nghĩa là:

```text
xác định outliers
→ xóa các dòng chứa outliers
```

Ưu điểm:

- đơn giản;
- trực tiếp;
- giảm ảnh hưởng của extreme values.

Nhược điểm:

- giảm sample size;
- có thể làm mất thông tin;
- có thể tạo bias nếu outliers là hợp lệ.

---

# 23. Capping bằng Z-score

Nguồn sử dụng:

```python
threshold_z = 2

df_capped = df_diabetics.copy()

df_capped["age"] = np.where(
    z > threshold_z,
    df_diabetics["age"].mean()
    + threshold_z
    * df_diabetics["age"].std(),
    df_diabetics["age"]
)

print(
    "Original DataFrame Shape:",
    df_diabetics.shape
)

print(
    "DataFrame Shape after Capping Outliers:",
    df_capped.shape
)
```

Kết quả:

```text
Original DataFrame Shape: (442, 10)
DataFrame Shape after Capping Outliers: (442, 10)
```

---

# 24. Capping là gì?

**Capping** giữ nguyên các dòng dữ liệu nhưng thay các giá trị cực đoan bằng một giới hạn.

Ví dụ:

```text
Original values:
10, 12, 11, 100
```

Capping tại:

```text
20
```

cho:

```text
10, 12, 11, 20
```

Khác với trimming:

```text
Trimming → mất dòng
Capping  → giữ dòng
```

---

# 25. So sánh Trimming và Capping

| Nội dung | Trimming | Capping |
|---|---|---|
| Xóa dòng | Có | Không |
| Giữ sample size | Không | Có |
| Giảm ảnh hưởng cực đoan | Có | Có |
| Có thể mất thông tin | Cao hơn | Thấp hơn |
| Thay đổi giá trị gốc | Xóa record | Có |

---

# 26. Điểm cần lưu ý với đoạn Capping theo Z-score

Đoạn code nguồn:

```python
np.where(
    z > threshold_z,
    mean + threshold_z * std,
    age
)
```

thay mọi outlier được phát hiện bởi:

```text
một upper cap
```

Nguồn không minh họa riêng việc capping phía dưới cho Z-score.

Nếu dataset có cả extreme low và extreme high values, cần phân biệt hai phía khi thiết kế quy tắc capping.

---

# 27. Phương pháp 4 — Interquartile Range (IQR)

IQR là khoảng giữa quartile thứ nhất và quartile thứ ba.

Công thức:

$$
IQR = Q_3 - Q_1
$$

Trong đó:

```text
Q1 = 25th percentile
Q3 = 75th percentile
```

IQR mô tả độ rộng của 50% dữ liệu trung tâm.

---

# 28. Tính IQR bằng NumPy

Nguồn:

```python
Q1 = np.percentile(
    df_diabetics["bmi"],
    25,
    method="midpoint"
)

Q3 = np.percentile(
    df_diabetics["bmi"],
    75,
    method="midpoint"
)

IQR = Q3 - Q1

print(IQR)
```

Kết quả nguồn:

```text
0.06520763046978838
```

---

# 29. Xác định Upper và Lower Bounds

Công thức:

$$
Upper = Q_3 + 1.5 \times IQR
$$

$$
Lower = Q_1 - 1.5 \times IQR
$$

Trong Python:

```python
upper = Q3 + 1.5 * IQR
lower = Q1 - 1.5 * IQR
```

---

# 30. Đếm Outliers phía trên

```python
upper_array = np.array(
    df_diabetics["bmi"] >= upper
)

print(
    "Upper Bound:",
    upper
)

print(
    upper_array.sum()
)
```

---

# 31. Đếm Outliers phía dưới

```python
lower_array = np.array(
    df_diabetics["bmi"] <= lower
)

print(
    "Lower Bound:",
    lower
)

print(
    lower_array.sum()
)
```

Các quan sát:

```text
bmi >= upper
```

hoặc:

```text
bmi <= lower
```

được xem là potential outliers theo quy tắc IQR trong ví dụ.

---

# 32. Vì sao IQR hữu ích?

Nguồn nhấn mạnh rằng IQR:

- là phương pháp phổ biến;
- đáng tin cậy;
- hoạt động tốt ngay cả khi dữ liệu bị skew.

Khác với Z-score, IQR không phụ thuộc trực tiếp vào:

```text
mean
standard deviation
```

mà sử dụng:

```text
quartiles
```

---

# 33. Trimming bằng IQR

Nguồn sử dụng:

```python
Q1 = df_diabetes["bmi"].quantile(
    0.25
)

Q3 = df_diabetes["bmi"].quantile(
    0.75
)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

Tìm indices:

```python
upper_array = np.where(
    df_diabetes["bmi"] >= upper
)[0]

lower_array = np.where(
    df_diabetes["bmi"] <= lower
)[0]
```

Loại:

```python
df_diabetes.drop(
    index=upper_array,
    inplace=True
)

df_diabetes.drop(
    index=lower_array,
    inplace=True
)
```

---

# 34. Kết quả Trimming bằng IQR

Nguồn báo cáo:

```text
Old Shape: (442, 10)
New Shape: (439, 10)
```

Tức là:

```text
442 - 439 = 3
```

quan sát đã bị loại trong ví dụ này.

---

# 35. Capping bằng IQR

Nguồn sử dụng:

```python
df_capped = df_diabetes.copy()

df_capped["bmi"] = np.where(
    df_capped["bmi"] > upper,
    upper,
    df_capped["bmi"]
)

df_capped["bmi"] = np.where(
    df_capped["bmi"] < lower,
    lower,
    df_capped["bmi"]
)

print(
    "Shape after Capping:",
    df_capped.shape
)
```

---

# 36. Lưu ý về ví dụ Capping IQR trong nguồn

Trong nguồn, `df_capped` được tạo từ:

```python
df_diabetes
```

sau khi `df_diabetes` đã được trimming.

Do đó output:

```text
Shape after Capping: (439, 10)
```

phản ánh dataset đã mất ba dòng ở bước trước.

Nếu muốn minh họa **capping thuần túy** trên dataset gốc, cần tạo bản sao trước khi trimming.

Điểm này cần được lưu ý khi đọc kết quả.

---

# 37. Minh họa Capping IQR độc lập

Để minh họa đúng ý tưởng capping mà không xóa dòng trước:

```python
df_capped_only = df_diabetics.copy()

Q1 = df_capped_only["bmi"].quantile(
    0.25
)

Q3 = df_capped_only["bmi"].quantile(
    0.75
)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_capped_only["bmi"] = (
    df_capped_only["bmi"]
    .clip(
        lower=lower,
        upper=upper
    )
)

print(
    df_capped_only.shape
)
```

Nếu chỉ capping:

```text
số dòng không đổi
```

Đây là phần giải thích bổ sung để làm rõ sự khác nhau giữa trimming và capping.

---

# 38. So sánh Z-score và IQR

| Nội dung | Z-score | IQR |
|---|---|---|
| Dựa trên | Mean và Std | Q1, Q3 |
| Nhạy với extreme values | Có | Ít hơn |
| Phù hợp dữ liệu gần Gaussian | Tốt | Có thể dùng |
| Phù hợp dữ liệu skew | Kém hơn | Tốt hơn |
| Threshold phổ biến | \(|z| > 3\) | ngoài \(Q1-1.5IQR\), \(Q3+1.5IQR\) |

Không có phương pháp nào luôn tốt nhất cho mọi dataset.

---

# 39. So sánh các phương pháp phát hiện Outlier

| Phương pháp | Loại | Ưu điểm | Hạn chế |
|---|---|---|---|
| Box Plot | Visualization | Nhanh, dễ quan sát | Chủ yếu univariate |
| Scatter Plot | Visualization | Thấy outlier giữa hai biến | Khó dùng với nhiều biến |
| Z-score | Statistical | Đơn giản, rõ ràng | Phụ thuộc mean/std |
| IQR | Statistical | Robust hơn với skew | Vẫn là quy tắc heuristic |

---

# 40. Khi nào nên loại Outlier?

Có thể cân nhắc trimming khi:

- xác định rõ là lỗi nhập liệu;
- lỗi thiết bị;
- sai đơn vị;
- quan sát nằm ngoài population nghiên cứu;
- có lý do nghiệp vụ thuyết phục.

Ví dụ:

```text
Age = 350
```

trong dữ liệu khách hàng cá nhân.

---

# 41. Khi nào không nên loại Outlier?

Không nên tự động xóa nếu outlier có thể là:

- sự kiện hiếm nhưng hợp lệ;
- khách hàng VIP;
- fraud;
- giao dịch lớn;
- trường hợp quan trọng của bài toán.

Ví dụ:

```text
Fraud detection
```

Nếu xóa các giao dịch bất thường, ta có thể xóa chính đối tượng muốn phát hiện.

---

# 42. Khi nào Capping hữu ích?

Capping có thể phù hợp khi:

- muốn giữ sample size;
- extreme values hợp lệ nhưng quá ảnh hưởng;
- cần hạn chế tác động của một số điểm cực đoan.

Ví dụ:

```text
Income
Revenue
Transaction Amount
```

---

# 43. Outlier Detection cần Domain Knowledge

Giả sử:

```text
Monthly Revenue = 500 million
```

Nếu phần lớn doanh nghiệp chỉ có:

```text
10–50 million
```

giá trị 500 million có thể là outlier.

Nhưng trong dataset có doanh nghiệp lớn:

```text
500 million
```

có thể hoàn toàn hợp lệ.

Do đó:

```text
Statistical Detection
+
Domain Knowledge
=
Better Decision
```

---

# 44. Quy trình xử lý Outliers đề xuất

```text
1. Understand the variable
2. Visualize the distribution
3. Detect potential outliers
4. Check data quality
5. Check business meaning
6. Decide:
   - keep
   - trim
   - cap
7. Re-check distribution
8. Document the decision
```

---

# 45. Ví dụ tổng hợp với BMI

## Bước 1 — Box Plot

```python
sns.boxplot(
    x=df_diabetics["bmi"]
)

plt.show()
```

## Bước 2 — IQR

```python
Q1 = df_diabetics["bmi"].quantile(
    0.25
)

Q3 = df_diabetics["bmi"].quantile(
    0.75
)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

## Bước 3 — Xác định Outliers

```python
outliers = df_diabetics[
    (df_diabetics["bmi"] < lower)
    |
    (df_diabetics["bmi"] > upper)
]

outliers
```

## Bước 4 — Trimming

```python
df_trimmed = df_diabetics[
    (df_diabetics["bmi"] >= lower)
    &
    (df_diabetics["bmi"] <= upper)
].copy()
```

## Bước 5 — Capping

```python
df_capped = df_diabetics.copy()

df_capped["bmi"] = (
    df_capped["bmi"]
    .clip(
        lower=lower,
        upper=upper
    )
)
```

---

# 46. Kiểm tra sau khi xử lý Outliers

Sau trimming:

```python
print(
    df_diabetics.shape
)

print(
    df_trimmed.shape
)
```

Sau capping:

```python
print(
    df_capped.shape
)
```

Vẽ lại:

```python
sns.boxplot(
    x=df_capped["bmi"]
)

plt.show()
```

Có thể so sánh:

```text
Before
After trimming
After capping
```

---

# 47. Những sai lầm phổ biến

## 47.1. Xóa mọi điểm ngoài whiskers

Sai vì các điểm đó chỉ là:

```text
potential outliers
```

---

## 47.2. Chọn threshold tùy ý

Ví dụ:

```text
BMI > 0.12
```

chỉ phù hợp với ví dụ cụ thể nếu có lý do.

---

## 47.3. Dùng Z-score cho dữ liệu rất skew

Mean và standard deviation có thể bị extreme values ảnh hưởng.

---

## 47.4. Không kiểm tra số dòng bị mất

Sau trimming cần kiểm tra:

```python
before = len(df)
after = len(df_trimmed)

print(before - after)
```

---

## 47.5. Không ghi lại quyết định

Quy trình phải ghi:

```text
Column
Method
Threshold
Number removed/capped
Reason
```

---

# 48. Bài tập thực hành 1 — Box Plot

Dùng Diabetes dataset.

Yêu cầu:

1. Vẽ box plot cho `age`.
2. Vẽ box plot cho `bp`.
3. Vẽ box plot cho `bmi`.
4. Nhận xét biến nào có potential outliers rõ nhất.

---

# 49. Bài tập thực hành 2 — Scatter Plot

Vẽ:

```text
bmi vs bp
```

Sau đó:

1. Quan sát cụm dữ liệu chính.
2. Xác định các điểm nằm xa cụm.
3. Không xóa ngay.
4. Ghi nhận các điều kiện có thể dùng để kiểm tra.

---

# 50. Bài tập thực hành 3 — Z-score

Hoàn thiện:

```python
from scipy import stats
import numpy as np

z = np.abs(
    stats.________(
        df_diabetics["age"]
    )
)

threshold_z = ________

outlier_indices = np.where(
    z > threshold_z
)[0]
```

Yêu cầu:

1. Thử `threshold_z = 2`.
2. Thử `threshold_z = 3`.
3. So sánh số outliers.

---

# 51. Bài tập thực hành 4 — IQR

Hoàn thiện:

```python
Q1 = df_diabetics["bmi"].quantile(
    ________
)

Q3 = df_diabetics["bmi"].quantile(
    ________
)

IQR = ________

lower = ________
upper = ________
```

Sau đó đếm số outliers.

---

# 52. Bài tập thực hành 5 — Trimming vs Capping

Tạo hai DataFrames:

```text
df_trimmed
df_capped
```

Yêu cầu:

1. Dùng cùng IQR bounds.
2. Với `df_trimmed`, loại outliers.
3. Với `df_capped`, dùng `clip()`.
4. So sánh shape.
5. So sánh mean và standard deviation của `bmi`.

---

# 53. Tự kiểm tra

### Câu 1

Outlier là gì?

A. Mọi giá trị lớn hơn mean  
B. Điểm dữ liệu khác biệt đáng kể so với phần lớn dữ liệu  
C. Mọi missing value  
D. Mọi giá trị âm

---

### Câu 2

Box plot dùng thành phần nào để mô tả phân phối?

A. Quartiles  
B. Regression coefficients  
C. Confusion matrix  
D. Probability threshold

---

### Câu 3

Scatter plot đặc biệt hữu ích khi nào?

A. Chỉ có một categorical variable  
B. Muốn quan sát mối quan hệ giữa hai numerical variables  
C. Muốn xử lý missing values  
D. Muốn encode categories

---

### Câu 4

Z-score biểu diễn điều gì?

A. Số lượng missing values  
B. Khoảng cách so với mean theo đơn vị standard deviation  
C. Khoảng cách giữa Q1 và Q3  
D. Giá trị median

---

### Câu 5

IQR được tính như thế nào?

A.

$$
Q1 + Q3
$$

B.

$$
Q3 - Q1
$$

C.

$$
Mean - Median
$$

D.

$$
Std^2
$$

---

### Câu 6

Trimming khác capping như thế nào?

---

### Câu 7

Nguồn giải thích ngưỡng Z-score phổ biến là bao nhiêu?

---

### Câu 8

Trong code ví dụ Z-score của nguồn, `threshold_z` lại được đặt bằng bao nhiêu?

---

### Câu 9

Vì sao IQR thường phù hợp hơn Z-score với dữ liệu bị skew?

---

### Câu 10

Tại sao không nên tự động xóa mọi outlier?

---

# 54. Bài tập tổng hợp — Phát hiện Outliers trong dữ liệu bán hàng

Cho dataset:

```text
sales.csv
```

với các cột:

```text
Order_ID
Quantity
Unit_Price
Revenue
Delivery_Time
```

Yêu cầu:

1. Đọc dữ liệu.
2. Chạy `describe()`.
3. Vẽ box plot cho:
   - `Quantity`
   - `Unit_Price`
   - `Revenue`
   - `Delivery_Time`
4. Vẽ scatter plot:
   - `Quantity` vs `Revenue`
   - `Unit_Price` vs `Revenue`
5. Tính Z-score cho `Revenue`.
6. Đếm outliers với:
   - threshold 2
   - threshold 3
7. Tính IQR cho `Revenue`.
8. Xác định lower/upper bounds.
9. Tạo:
   - `sales_trimmed`
   - `sales_capped`
10. So sánh shape.
11. So sánh mean/median/std trước và sau.
12. Viết nhận xét về việc nên:
   - giữ;
   - trim;
   - hay cap các outliers.

---

# 55. Yêu cầu báo cáo

Người học cần trình bày:

## Phần 1 — Phát hiện

Ví dụ:

```text
Revenue:
- Box plot cho thấy 8 potential outliers
- Z-score > 3: 4 records
- IQR rule: 7 records
```

## Phần 2 — So sánh phương pháp

```text
Box Plot
Scatter Plot
Z-score
IQR
```

## Phần 3 — Quyết định xử lý

Ví dụ:

```text
2 records là lỗi nhập liệu → remove
5 records là khách hàng lớn hợp lệ → keep/cap tùy mục tiêu
```

## Phần 4 — Kiểm tra tác động

So sánh:

```text
mean
median
std
sample size
```

---

# 56. Checklist phát hiện và xử lý Outliers

```text
□ Tôi đã hiểu ý nghĩa của biến chưa?
□ Tôi đã xem describe() chưa?
□ Tôi đã vẽ box plot chưa?
□ Tôi đã xem scatter plot nếu có hai biến liên quan chưa?
□ Tôi đã thử Z-score khi phù hợp chưa?
□ Tôi đã thử IQR chưa?
□ Tôi đã kiểm tra threshold chưa?
□ Tôi đã xác minh outlier có phải lỗi không?
□ Tôi đã cân nhắc trimming vs capping chưa?
□ Tôi đã kiểm tra sample size sau trimming chưa?
□ Tôi đã kiểm tra phân phối sau xử lý chưa?
□ Tôi đã ghi lại quyết định chưa?
```

---

# 57. Tóm tắt bài học

Các điểm cần ghi nhớ:

- Outlier là điểm dữ liệu khác biệt đáng kể so với phần lớn dataset.
- Outliers có thể đến từ lỗi hoặc từ biến thiên tự nhiên.
- Box plot là công cụ trực quan phổ biến để nhận diện potential outliers.
- Scatter plot hữu ích để phát hiện điểm bất thường khi xét hai biến cùng lúc.
- Z-score đo khoảng cách giữa một quan sát và mean theo standard deviation.
- Nguồn giải thích ngưỡng phổ biến là `3`, nhưng ví dụ code sử dụng `2`.
- IQR được tính bằng:

$$
IQR = Q_3 - Q_1
$$

- IQR bounds thường được xác định bởi:

$$
Lower = Q_1 - 1.5IQR
$$

$$
Upper = Q_3 + 1.5IQR
$$

- **Trimming** xóa các dòng chứa outlier.
- **Capping** giữ dòng nhưng giới hạn extreme values.
- Không nên tự động xóa mọi outlier.
- Quyết định xử lý cần kết hợp:
  - phương pháp thống kê;
  - trực quan hóa;
  - domain knowledge.
- Sau khi xử lý cần kiểm tra lại:
  - shape;
  - phân phối;
  - mean;
  - median;
  - standard deviation.

---

## Tài liệu tham khảo

GeeksforGeeks. *Detect and Remove the Outliers using Python*. Last Updated: 7 Apr, 2026.
