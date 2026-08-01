# Phân tích dữ liệu khám phá

**Cập nhật lần cuối:** 22 tháng 6 năm 2026

Phân tích dữ liệu khám phá, thường được gọi là **Exploratory Data Analysis (EDA)**, là một bước quan trọng trong quá trình phân tích dữ liệu. EDA giúp người phân tích khám phá, tóm tắt và trực quan hóa dữ liệu để:

- Hiểu cấu trúc của bộ dữ liệu.
- Phát hiện các mẫu hình và xu hướng.
- Xác định các giá trị bất thường.
- Kiểm tra các giả định ban đầu.
- Đánh giá mối quan hệ giữa các biến.
- Chuẩn bị dữ liệu trước khi áp dụng mô hình thống kê hoặc học máy.

<p align="center">
  <img src="images/image-15.png" alt="alt text" />
</p>

### Câu hỏi nhanh

**Câu 1.** Mục tiêu chính của EDA là gì?

A. Chỉ xây dựng mô hình học máy  
B. Khám phá và hiểu dữ liệu trước khi mô hình hóa  
C. Chỉ lưu trữ dữ liệu  
D. Thay thế hoàn toàn bước làm sạch dữ liệu  

**Câu 2. Đúng hay sai?** EDA thường được thực hiện trước khi xây dựng mô hình thống kê hoặc học máy.

---
<p align="center">
  <img src="images/image-16.png" alt="alt text" />
</p>
# Tầm quan trọng của EDA

EDA đóng vai trò quan trọng vì giúp người phân tích hiểu rõ bộ dữ liệu trước khi đưa ra kết luận hoặc xây dựng mô hình.

## Những lợi ích chính

- Cung cấp cái nhìn rõ ràng về số lượng biến, kiểu dữ liệu và phân phối dữ liệu.
- Phát hiện các mẫu hình và mối quan hệ giữa các biến.
- Xác định lỗi dữ liệu và các giá trị ngoại lệ có thể ảnh hưởng đến kết quả.
- Làm nổi bật những đặc trưng quan trọng cho việc xây dựng mô hình.
- Hỗ trợ lựa chọn phương pháp mô hình hóa phù hợp.

### Ví dụ

Một bộ dữ liệu khách hàng có thể chứa các biến như tuổi, thu nhập, khu vực sinh sống và mức chi tiêu. EDA có thể giúp phát hiện:

- Nhóm khách hàng nào có mức chi tiêu cao nhất.
- Thu nhập có liên quan đến mức chi tiêu hay không.
- Có những giá trị thu nhập bất thường nào không.
- Một số biến có quá nhiều dữ liệu thiếu hay không.

### Câu hỏi nhanh

**Câu 1.** EDA có thể hỗ trợ lựa chọn mô hình bằng cách nào?

A. Xác định đặc điểm và cấu trúc của dữ liệu  
B. Loại bỏ toàn bộ dữ liệu  
C. Thay thế việc đánh giá mô hình  
D. Chỉ tăng số lượng biến  

**Câu 2.** Nội dung nào sau đây có thể được phát hiện bằng EDA?

A. Giá trị ngoại lệ  
B. Mối quan hệ giữa các biến  
C. Kiểu dữ liệu không phù hợp  
D. Tất cả các phương án trên  

**Câu 3. Tình huống.** Một cột dữ liệu chứa 70% giá trị thiếu. EDA có thể giúp người phân tích đưa ra quyết định gì?

---

# Các loại phân tích dữ liệu khám phá

EDA thường được chia thành ba loại chính:

1. Phân tích đơn biến.
2. Phân tích hai biến.
3. Phân tích đa biến.

---
<p align="center">
  <img src="images/image-17.png" alt="alt text" />
</p>

## 1. Phân tích đơn biến

Phân tích đơn biến nghiên cứu một biến tại một thời điểm nhằm hiểu đặc điểm và phân phối của biến đó.

### Các kỹ thuật phổ biến

- **Histogram:** Thể hiện cách các giá trị số được phân phối.
- **Box plot:** Thể hiện độ phân tán và hỗ trợ phát hiện giá trị ngoại lệ.
- **Bar chart:** Thường được sử dụng cho biến phân loại.
- **Thống kê mô tả:** Bao gồm trung bình, trung vị, yếu vị, độ lệch chuẩn và các phân vị.

### Ví dụ

Với biến `age`, người phân tích có thể:

- Tính tuổi trung bình và trung vị.
- Vẽ histogram để quan sát phân phối.
- Vẽ box plot để phát hiện độ tuổi bất thường.
- Kiểm tra phân phối có bị lệch hay không.

### Câu hỏi nhanh

**Câu 1.** Phân tích đơn biến nghiên cứu bao nhiêu biến tại một thời điểm?

A. Một biến  
B. Hai biến  
C. Ba biến  
D. Không có biến nào  

**Câu 2.** Biểu đồ nào phù hợp để quan sát phân phối của một biến số?

A. Histogram  
B. Biểu đồ mạng  
C. Bản đồ nhiệt  
D. Biểu đồ Gantt  

**Câu 3.** Box plot thường được sử dụng để làm gì?

A. Kiểm tra kết nối mạng  
B. Phát hiện giá trị ngoại lệ và quan sát độ phân tán  
C. Tải dữ liệu  
D. Chuyển đổi kiểu dữ liệu  

---

## 2. Phân tích hai biến

Phân tích hai biến xem xét mối quan hệ giữa hai biến để hiểu cách chúng tương tác hoặc thay đổi cùng nhau.

### Các kỹ thuật phổ biến

- **Scatter plot:** Thể hiện mối quan hệ giữa hai biến số.
- **Hệ số tương quan:** Đo cường độ và chiều của mối quan hệ tuyến tính giữa hai biến.
- **Cross-tabulation:** Biểu diễn mối quan hệ giữa hai biến phân loại.
- **Line graph:** So sánh hai biến theo thời gian để nhận diện xu hướng.
- **Hiệp phương sai:** Thể hiện cách hai biến thay đổi cùng nhau.

### Ví dụ

Với biến `age` và `income`, người phân tích có thể:

- Vẽ scatter plot để quan sát mối quan hệ.
- Tính hệ số tương quan.
- Kiểm tra xem thu nhập có xu hướng tăng theo tuổi hay không.
- Phát hiện các quan sát khác biệt rõ rệt.

### Câu hỏi nhanh

**Câu 1.** Kỹ thuật nào phù hợp để xem mối quan hệ giữa hai biến số?

A. Scatter plot  
B. Bar chart một biến  
C. Histogram một biến  
D. Bảng tần số đơn  

**Câu 2.** Hệ số tương quan dùng để đo:

A. Số lượng dòng dữ liệu  
B. Mức độ và chiều của mối quan hệ giữa hai biến  
C. Số giá trị thiếu  
D. Kích thước tệp  

**Câu 3. Đúng hay sai?** Tương quan cao luôn chứng minh một biến gây ra biến còn lại.

---

## 3. Phân tích đa biến

Phân tích đa biến nghiên cứu từ ba biến trở lên nhằm hiểu các mối quan hệ phức tạp trong bộ dữ liệu.

### Các kỹ thuật phổ biến

- **Pair plot:** Thể hiện đồng thời mối quan hệ giữa nhiều biến.
- **Principal Component Analysis (PCA):** Giảm số chiều dữ liệu nhưng cố gắng giữ lại phần thông tin quan trọng.
- **Spatial analysis:** Phân tích các mẫu hình địa lý dựa trên bản đồ và dữ liệu vị trí.
- **Ma trận tương quan:** Giúp quan sát nhiều mối quan hệ giữa các biến số.
- **Phân nhóm và phân loại:** Có thể được sử dụng để phát hiện cấu trúc phức tạp trong dữ liệu.

### Ví dụ

Trong dữ liệu khách hàng, người phân tích có thể xem xét đồng thời:

- Tuổi.
- Thu nhập.
- Tần suất mua hàng.
- Tổng mức chi tiêu.

Qua đó, người phân tích có thể xác định các nhóm khách hàng có đặc điểm tương tự.

### Câu hỏi nhanh

**Câu 1.** Phân tích đa biến thường xem xét:

A. Một biến  
B. Hai biến  
C. Ba biến trở lên  
D. Không có biến nào  

**Câu 2.** PCA thường được sử dụng để:

A. Tăng số dòng dữ liệu  
B. Giảm số chiều dữ liệu  
C. Xóa toàn bộ biến số  
D. Chuyển biểu đồ thành bảng  

**Câu 3.** Pair plot có tác dụng gì?

A. Hiển thị mối quan hệ giữa nhiều cặp biến  
B. Chỉ hiển thị một giá trị  
C. Chỉ xử lý dữ liệu văn bản  
D. Kiểm tra quyền truy cập dữ liệu  

---

# Công cụ thực hiện EDA

EDA có thể được thực hiện bằng nhiều công cụ khác nhau.

## Python

Các thư viện phổ biến gồm:

- **Pandas:** Xử lý và thao tác dữ liệu.
- **Matplotlib:** Tạo biểu đồ cơ bản.
- **Seaborn:** Tạo trực quan hóa thống kê.
- **Plotly:** Tạo biểu đồ tương tác.

## R

Các gói phổ biến gồm:

- **ggplot2:** Trực quan hóa dữ liệu.
- **dplyr:** Biến đổi và thao tác dữ liệu.
- **tidyr:** Tổ chức và định dạng dữ liệu.

### Câu hỏi nhanh

**Câu 1.** Thư viện Python nào thường được sử dụng để thao tác dữ liệu dạng bảng?

A. Pandas  
B. Matplotlib  
C. Plotly  
D. Seaborn  

**Câu 2.** Công cụ nào phù hợp để tạo biểu đồ tương tác trong Python?

A. Plotly  
B. Pandas  
C. NumPy  
D. pathlib  

**Câu 3.** Trong R, gói nào thường được sử dụng để trực quan hóa dữ liệu?

A. ggplot2  
B. dplyr  
C. tidyr  
D. readr  

---

# Các bước thực hiện EDA

EDA gồm một chuỗi bước giúp người phân tích hiểu dữ liệu, phát hiện vấn đề và chuẩn bị dữ liệu cho các phân tích tiếp theo.

<p align="center">
  <img src="images/image-18.png" alt="alt text" />
</p>

---

## Bước 1. Hiểu vấn đề và dữ liệu

Bước đầu tiên là hiểu rõ vấn đề cần giải quyết và ý nghĩa của dữ liệu hiện có.

### Các câu hỏi cần đặt ra

- Mục tiêu hoặc vấn đề cần giải quyết là gì?
- Các biến trong bộ dữ liệu là gì?
- Mỗi biến đại diện cho điều gì?
- Dữ liệu gồm những loại nào: số, phân loại, văn bản hay thời gian?
- Có vấn đề hoặc hạn chế nào về chất lượng dữ liệu không?

### Ví dụ

Nếu mục tiêu là dự báo khách hàng rời bỏ dịch vụ, cần xác định:

- Biến mục tiêu là gì?
- Các biến đầu vào nào có thể liên quan?
- Dữ liệu được thu thập trong khoảng thời gian nào?
- Có sự mất cân bằng giữa nhóm rời bỏ và không rời bỏ hay không?

### Câu hỏi nhanh

**Câu 1.** Vì sao cần hiểu ý nghĩa của từng biến?

A. Để diễn giải dữ liệu đúng bối cảnh  
B. Để tăng số lượng biến  
C. Để thay thế bước thu thập dữ liệu  
D. Để tránh trực quan hóa  

**Câu 2.** Câu hỏi nào phù hợp ở bước này?

A. Biến nào là biến mục tiêu?  
B. Dữ liệu có những kiểu nào?  
C. Bộ dữ liệu có hạn chế gì?  
D. Tất cả các phương án trên  

---

## Bước 2. Nhập và kiểm tra dữ liệu

Sau khi hiểu vấn đề, dữ liệu được tải vào Python, R hoặc công cụ tương ứng để kiểm tra ban đầu.

### Các công việc chính

- Tải bộ dữ liệu đúng cách.
- Kiểm tra số dòng và số cột.
- Xác định các giá trị thiếu.
- Kiểm tra kiểu dữ liệu của từng biến.
- Tìm lỗi, giá trị không hợp lệ hoặc quan sát bất thường.

### Ví dụ với Python

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
```

### Giải thích

- `head()` hiển thị các dòng đầu tiên.
- `shape` cho biết số dòng và số cột.
- `info()` cung cấp thông tin về kiểu dữ liệu.
- `isnull().sum()` đếm số giá trị thiếu trong từng cột.

### Câu hỏi nhanh

**Câu 1.** Thuộc tính nào cho biết số dòng và số cột của DataFrame?

A. `df.shape`  
B. `df.head()`  
C. `df.info()`  
D. `df.columns()`  

**Câu 2.** Lệnh nào giúp kiểm tra kiểu dữ liệu của các cột?

A. `df.info()`  
B. `df.plot()`  
C. `df.sort_values()`  
D. `df.drop()`  

**Câu 3.** Vì sao cần kiểm tra dữ liệu ngay sau khi nhập?

---

## Bước 3. Xử lý dữ liệu thiếu

Dữ liệu thiếu xuất hiện phổ biến trong các bộ dữ liệu thực tế và có thể ảnh hưởng đến chất lượng phân tích.

### Các công việc chính

- Xác định nguyên nhân dữ liệu bị thiếu.
- Quyết định loại bỏ hay điền dữ liệu thiếu.
- Chọn phương pháp điền phù hợp.
- Đánh giá mức độ không chắc chắn sau khi xử lý.

### Một số phương pháp xử lý

- Điền bằng trung bình.
- Điền bằng trung vị.
- Điền bằng yếu vị.
- Sử dụng hồi quy.
- Sử dụng KNN.
- Sử dụng cây quyết định.
- Loại bỏ dòng hoặc cột trong trường hợp phù hợp.

### Ví dụ

```python
df["age"] = df["age"].fillna(
    df["age"].median()
)

df["city"] = df["city"].fillna(
    df["city"].mode()[0]
)
```

### Lưu ý

Loại bỏ dữ liệu thiếu có thể làm giảm kích thước mẫu và gây thiên lệch. Ngược lại, việc điền dữ liệu cũng có thể làm thay đổi phân phối ban đầu. Vì vậy, cần xem xét nguyên nhân thiếu dữ liệu và bối cảnh của bài toán.

### Câu hỏi nhanh

**Câu 1.** Vì sao không nên tự động xóa mọi dòng có dữ liệu thiếu?

A. Có thể làm giảm dữ liệu và gây thiên lệch  
B. Vì dữ liệu thiếu luôn chính xác  
C. Vì không thể xóa dòng trong Pandas  
D. Vì mọi giá trị thiếu đều bằng 0  

**Câu 2.** Phương pháp nào phù hợp để điền dữ liệu số bị lệch và có ngoại lệ?

A. Trung vị  
B. Giá trị lớn nhất  
C. Số ngẫu nhiên  
D. Tên cột  

**Câu 3. Đúng hay sai?** Sau khi điền dữ liệu thiếu, mọi sự không chắc chắn đều được loại bỏ hoàn toàn.

---

## Bước 4. Khám phá đặc điểm dữ liệu

Sau khi xử lý dữ liệu thiếu, cần xem xét các đặc điểm chính của dữ liệu.

### Các nội dung cần kiểm tra

- Phân phối dữ liệu.
- Giá trị trung bình, trung vị và yếu vị.
- Độ lệch chuẩn.
- Độ lệch của phân phối.
- Độ nhọn của phân phối.
- Giá trị ngoại lệ và điểm bất thường.

### Ví dụ với Python

```python
print(df.describe())
print(df["income"].skew())
print(df["income"].kurt())
```

### Giải thích

- `describe()` cung cấp các thống kê mô tả cơ bản.
- `skew()` đo mức độ bất đối xứng của phân phối.
- `kurt()` đo độ nhọn của phân phối.

### Câu hỏi nhanh

**Câu 1.** Đại lượng nào đo mức độ phân tán của dữ liệu?

A. Độ lệch chuẩn  
B. Tên cột  
C. Số dòng  
D. Kiểu tệp  

**Câu 2.** Skewness được sử dụng để đo:

A. Độ bất đối xứng của phân phối  
B. Số giá trị thiếu  
C. Độ dài tên biến  
D. Số nhóm dữ liệu  

**Câu 3.** Vì sao cần quan sát cả trung bình và trung vị?

---

## Bước 5. Biến đổi dữ liệu

Biến đổi dữ liệu giúp đưa dữ liệu về định dạng phù hợp hơn cho phân tích hoặc mô hình hóa.

### Các kỹ thuật phổ biến

- Chuẩn hóa hoặc điều chỉnh thang đo.
- Min-max scaling.
- Standardization.
- One-hot encoding.
- Label encoding.
- Biến đổi logarit.
- Biến đổi căn bậc hai.
- Tạo biến mới.
- Tổng hợp hoặc nhóm dữ liệu.

### Ví dụ chuẩn hóa min-max

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["age", "income"]] = scaler.fit_transform(
    df[["age", "income"]]
)
```

### Ví dụ mã hóa one-hot

```python
df = pd.get_dummies(
    df,
    columns=["city"],
    drop_first=True
)
```

### Ví dụ tạo biến mới

```python
df["revenue_per_order"] = (
    df["total_revenue"] / df["number_of_orders"]
)
```

### Câu hỏi nhanh

**Câu 1.** One-hot encoding thường được sử dụng cho:

A. Biến phân loại  
B. Tệp hình ảnh  
C. Dữ liệu thiếu  
D. Giá trị ngoại lệ  

**Câu 2.** Min-max scaling thường đưa dữ liệu về khoảng:

A. Từ 0 đến 1  
B. Từ 10 đến 100  
C. Từ âm vô cùng đến dương vô cùng  
D. Chỉ các số nguyên  

**Câu 3.** Tạo biến mới từ các biến hiện có được gọi là gì?

A. Feature engineering  
B. Data deletion  
C. File conversion  
D. Data duplication  

---

## Bước 6. Trực quan hóa mối quan hệ dữ liệu

Trực quan hóa giúp phát hiện các mẫu hình và mối quan hệ khó nhận ra chỉ bằng bảng số.

### Biểu đồ cho dữ liệu phân loại

- Bar chart.
- Pie chart.
- Count plot.

### Biểu đồ cho dữ liệu số

- Histogram.
- Box plot.
- Density plot.

### Biểu đồ cho mối quan hệ

- Scatter plot.
- Line chart.
- Heatmap.
- Pair plot.

### Ví dụ với Python

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df["income"], kde=True)
plt.title("Phân phối thu nhập")
plt.show()
```

```python
sns.scatterplot(
    x="age",
    y="income",
    data=df
)
plt.title("Mối quan hệ giữa tuổi và thu nhập")
plt.show()
```

```python
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)
plt.title("Ma trận tương quan")
plt.show()
```

### Câu hỏi nhanh

**Câu 1.** Biểu đồ nào phù hợp để quan sát mối quan hệ giữa hai biến số?

A. Scatter plot  
B. Pie chart  
C. Bar chart một biến  
D. Bảng tần số  

**Câu 2.** Heatmap thường được sử dụng để:

A. Trình bày ma trận tương quan  
B. Xóa dữ liệu thiếu  
C. Tải dữ liệu từ API  
D. Chuyển kiểu dữ liệu  

**Câu 3.** Vì sao trực quan hóa có thể phát hiện vấn đề mà bảng số không thể hiện rõ?

---

## Bước 7. Xử lý giá trị ngoại lệ

Giá trị ngoại lệ là những quan sát khác biệt đáng kể so với phần lớn dữ liệu.

### Nguyên nhân có thể

- Lỗi nhập liệu.
- Lỗi đo lường.
- Sai định dạng.
- Biến động thực tế hiếm gặp.
- Sự kiện bất thường nhưng hợp lệ.

### Phương pháp phát hiện

- Khoảng tứ phân vị IQR.
- Z-score.
- Box plot.
- Phân tích theo kiến thức miền.

### Phương pháp xử lý

- Giữ nguyên nếu giá trị hợp lệ.
- Sửa nếu có lỗi nhập liệu.
- Giới hạn giá trị bằng capping.
- Biến đổi dữ liệu.
- Loại bỏ khi giá trị rõ ràng không chính xác hoặc gây hại cho phân tích.

### Ví dụ phát hiện ngoại lệ bằng IQR

```python
Q1 = df["income"].quantile(0.25)
Q3 = df["income"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["income"] < lower_bound) |
    (df["income"] > upper_bound)
]
```

### Câu hỏi nhanh

**Câu 1.** Giá trị ngoại lệ có thể xuất hiện do:

A. Lỗi nhập liệu  
B. Biến động thực tế  
C. Lỗi đo lường  
D. Tất cả các phương án trên  

**Câu 2.** Phương pháp nào thường dùng để phát hiện giá trị ngoại lệ?

A. IQR  
B. Z-score  
C. Box plot  
D. Tất cả các phương án trên  

**Câu 3. Đúng hay sai?** Mọi giá trị ngoại lệ đều phải bị loại bỏ.

---

## Bước 8. Truyền đạt kết quả và hiểu biết

Bước cuối cùng của EDA là trình bày rõ ràng kết quả phân tích để người khác có thể hiểu và sử dụng.

### Nội dung cần trình bày

- Mục tiêu và phạm vi phân tích.
- Bối cảnh của bài toán.
- Phương pháp đã sử dụng.
- Các mẫu hình và xu hướng chính.
- Các giá trị bất thường.
- Hạn chế của dữ liệu.
- Các đề xuất cho bước tiếp theo.

### Nguyên tắc truyền đạt

- Sử dụng biểu đồ phù hợp.
- Tránh đưa quá nhiều thông tin vào một hình.
- Làm nổi bật những phát hiện quan trọng.
- Giải thích kết quả bằng ngôn ngữ dễ hiểu.
- Nêu rõ hạn chế và mức độ không chắc chắn.

### Câu hỏi nhanh

**Câu 1.** Nội dung nào nên xuất hiện trong báo cáo EDA?

A. Mục tiêu phân tích  
B. Phát hiện chính  
C. Hạn chế dữ liệu  
D. Tất cả các phương án trên  

**Câu 2.** Vì sao cần nêu hạn chế của dữ liệu?

A. Để người đọc hiểu phạm vi và độ tin cậy của kết quả  
B. Để làm báo cáo dài hơn  
C. Để tránh trình bày biểu đồ  
D. Để loại bỏ trách nhiệm phân tích  

**Câu 3.** Một báo cáo EDA tốt nên sử dụng ngôn ngữ như thế nào?

A. Rõ ràng và dễ hiểu  
B. Chỉ sử dụng thuật ngữ phức tạp  
C. Không cần giải thích biểu đồ  
D. Chỉ trình bày mã nguồn  

---

# Ứng dụng của EDA

EDA được sử dụng rộng rãi trong nhiều lĩnh vực.

## Phân tích thị trường và phân khúc khách hàng

EDA giúp nhận diện nhóm khách hàng, hành vi mua hàng và xu hướng thị trường.

## Đánh giá rủi ro trong tài chính và bảo hiểm

EDA hỗ trợ phát hiện các mẫu giao dịch bất thường, yếu tố rủi ro và nhóm khách hàng có xác suất vỡ nợ cao.

## Kiểm soát chất lượng trong sản xuất

EDA giúp phát hiện lỗi sản phẩm, sự thay đổi trong quy trình và nguyên nhân gây sai lệch chất lượng.

## Phân tích dữ liệu y tế và dự báo bệnh

EDA hỗ trợ khám phá yếu tố nguy cơ, xu hướng bệnh và các mối quan hệ giữa triệu chứng, điều trị và kết quả sức khỏe.

## Hệ thống gợi ý và tối ưu hóa sản phẩm

EDA giúp hiểu hành vi người dùng, mức độ tương tác và sở thích để cải thiện hệ thống gợi ý.

### Câu hỏi nhanh

**Câu 1.** Phát hiện giao dịch bất thường là ứng dụng phổ biến của EDA trong lĩnh vực nào?

A. Tài chính  
B. Thiết kế đồ họa  
C. Kiến trúc  
D. Âm nhạc  

**Câu 2.** Trong sản xuất, EDA có thể hỗ trợ:

A. Phát hiện lỗi sản phẩm  
B. Theo dõi biến động quy trình  
C. Kiểm soát chất lượng  
D. Tất cả các phương án trên  

**Câu 3. Tình huống.** Một nền tảng thương mại điện tử muốn cải thiện hệ thống gợi ý sản phẩm. EDA có thể được sử dụng như thế nào?

---

# Tóm tắt nội dung

| Nội dung | Mục tiêu chính | Công cụ hoặc kỹ thuật |
|---|---|---|
| **Phân tích đơn biến** | Hiểu một biến | Histogram, box plot, bar chart |
| **Phân tích hai biến** | Hiểu mối quan hệ giữa hai biến | Scatter plot, tương quan, bảng chéo |
| **Phân tích đa biến** | Hiểu quan hệ giữa nhiều biến | Pair plot, PCA, ma trận tương quan |
| **Xử lý dữ liệu thiếu** | Giảm ảnh hưởng của dữ liệu không đầy đủ | Mean, median, mode, KNN |
| **Khám phá đặc điểm** | Hiểu phân phối và độ biến động | Trung bình, trung vị, độ lệch chuẩn |
| **Biến đổi dữ liệu** | Chuẩn bị dữ liệu cho phân tích | Scaling, encoding, transformation |
| **Xử lý ngoại lệ** | Phát hiện và đánh giá điểm bất thường | IQR, Z-score, box plot |
| **Truyền đạt kết quả** | Chuyển kết quả thành hiểu biết | Biểu đồ, báo cáo, bảng điều khiển |

---

# Câu hỏi ôn tập cuối bài

## Phần A. Câu hỏi trắc nghiệm

**Câu 1.** EDA thường được thực hiện vào thời điểm nào?

A. Trước khi xây dựng mô hình  
B. Chỉ sau khi triển khai mô hình  
C. Sau khi xóa dữ liệu  
D. Không liên quan đến mô hình  

**Câu 2.** Phân tích đơn biến tập trung vào:

A. Một biến  
B. Hai biến  
C. Ba biến  
D. Toàn bộ mô hình  

**Câu 3.** Biểu đồ nào phù hợp để phát hiện giá trị ngoại lệ?

A. Box plot  
B. Pie chart  
C. Line chart  
D. Bản đồ  

**Câu 4.** Kỹ thuật nào phù hợp để nghiên cứu mối quan hệ giữa hai biến số?

A. Scatter plot  
B. Histogram  
C. Bar chart một biến  
D. Bảng tần số đơn  

**Câu 5.** PCA được sử dụng chủ yếu để:

A. Giảm số chiều dữ liệu  
B. Tăng số dòng dữ liệu  
C. Xóa dữ liệu thiếu  
D. Tạo tệp CSV  

**Câu 6.** Phương pháp nào có thể sử dụng để xử lý dữ liệu thiếu?

A. Trung vị  
B. KNN  
C. Hồi quy  
D. Tất cả các phương án trên  

**Câu 7.** Skewness đo:

A. Độ bất đối xứng của phân phối  
B. Số dòng dữ liệu  
C. Số giá trị duy nhất  
D. Độ dài tên cột  

**Câu 8.** One-hot encoding được sử dụng cho:

A. Biến phân loại  
B. Giá trị ngoại lệ  
C. Tệp hình ảnh  
D. Dữ liệu thời gian  

**Câu 9.** IQR thường được sử dụng để:

A. Phát hiện giá trị ngoại lệ  
B. Tạo biến mục tiêu  
C. Tải dữ liệu  
D. Đổi tên cột  

**Câu 10.** Bước cuối cùng trong EDA là:

A. Truyền đạt kết quả và hiểu biết  
B. Nhập dữ liệu  
C. Tạo dữ liệu thiếu  
D. Xóa toàn bộ biến  

## Phần B. Câu hỏi đúng/sai

**Câu 1.** EDA chỉ bao gồm việc vẽ biểu đồ.

**Câu 2.** Tương quan không đồng nghĩa với quan hệ nhân quả.

**Câu 3.** Mọi giá trị ngoại lệ đều là lỗi dữ liệu.

**Câu 4.** Trung vị thường ít bị ảnh hưởng bởi ngoại lệ hơn trung bình.

**Câu 5.** Việc điền dữ liệu thiếu có thể làm thay đổi phân phối dữ liệu.

**Câu 6.** Pair plot có thể thể hiện mối quan hệ giữa nhiều biến.

**Câu 7.** Báo cáo EDA nên nêu cả hạn chế của dữ liệu.

## Phần C. Câu hỏi tự luận

**Câu 1.** Trình bày mục tiêu của EDA.

**Câu 2.** Phân biệt phân tích đơn biến, hai biến và đa biến.

**Câu 3.** Trình bày các bước chính trong quy trình EDA.

**Câu 4.** Vì sao không nên tự động loại bỏ mọi giá trị ngoại lệ?

**Câu 5.** Nêu ba phương pháp xử lý dữ liệu thiếu.

**Câu 6.** Vì sao trực quan hóa đóng vai trò quan trọng trong EDA?

## Phần D. Bài tập thực hành

### Bài 1. Kiểm tra bộ dữ liệu

Sử dụng một bộ dữ liệu bất kỳ và thực hiện:

1. Hiển thị năm dòng đầu tiên.
2. Xác định số dòng và số cột.
3. Kiểm tra kiểu dữ liệu.
4. Đếm số giá trị thiếu.
5. Xác định số lượng giá trị duy nhất trong từng cột.

### Bài 2. Phân tích đơn biến

Chọn một biến số và một biến phân loại:

1. Tính thống kê mô tả.
2. Vẽ histogram cho biến số.
3. Vẽ box plot cho biến số.
4. Vẽ bar chart cho biến phân loại.
5. Viết nhận xét về phân phối và ngoại lệ.

### Bài 3. Phân tích hai biến

Thực hiện:

1. Vẽ scatter plot giữa hai biến số.
2. Tính hệ số tương quan.
3. Lập bảng chéo giữa hai biến phân loại.
4. Viết nhận xét về mối quan hệ quan sát được.

### Bài 4. Phân tích đa biến

Thực hiện:

1. Vẽ pair plot cho ít nhất bốn biến.
2. Tạo ma trận tương quan.
3. Xác định những cặp biến có tương quan mạnh.
4. Giải thích vì sao không thể kết luận quan hệ nhân quả chỉ từ tương quan.

### Bài 5. Xử lý dữ liệu thiếu và ngoại lệ

Thực hiện:

1. Xác định các cột có dữ liệu thiếu.
2. Đề xuất phương pháp xử lý.
3. Phát hiện ngoại lệ bằng IQR.
4. So sánh kết quả trước và sau xử lý.
5. Giải thích lý do giữ lại hoặc loại bỏ ngoại lệ.

---

# Đáp án và gợi ý trả lời

<details>
<summary><strong>Nhấn để hiển thị đáp án</strong></summary>

## Đáp án câu hỏi nhanh — Phần mở đầu

### Câu 1

B. Khám phá và hiểu dữ liệu trước khi mô hình hóa.

### Câu 2

Đúng.

## Đáp án câu hỏi nhanh — Tầm quan trọng của EDA

### Câu 1

A. Xác định đặc điểm và cấu trúc của dữ liệu.

### Câu 2

D. Tất cả các phương án trên.

### Câu 3

EDA có thể giúp đánh giá xem cột đó còn đủ giá trị sử dụng hay không, có nên điền dữ liệu, loại bỏ cột hoặc tìm nguồn dữ liệu khác.

## Đáp án câu hỏi nhanh — Phân tích đơn biến

### Câu 1

A. Một biến.

### Câu 2

A. Histogram.

### Câu 3

B. Phát hiện giá trị ngoại lệ và quan sát độ phân tán.

## Đáp án câu hỏi nhanh — Phân tích hai biến

### Câu 1

A. Scatter plot.

### Câu 2

B. Mức độ và chiều của mối quan hệ giữa hai biến.

### Câu 3

Sai. Tương quan không chứng minh quan hệ nhân quả.

## Đáp án câu hỏi nhanh — Phân tích đa biến

### Câu 1

C. Ba biến trở lên.

### Câu 2

B. Giảm số chiều dữ liệu.

### Câu 3

A. Hiển thị mối quan hệ giữa nhiều cặp biến.

## Đáp án câu hỏi nhanh — Công cụ

### Câu 1

A. Pandas.

### Câu 2

A. Plotly.

### Câu 3

A. ggplot2.

## Đáp án câu hỏi nhanh — Bước 1

### Câu 1

A. Để diễn giải dữ liệu đúng bối cảnh.

### Câu 2

D. Tất cả các phương án trên.

## Đáp án câu hỏi nhanh — Bước 2

### Câu 1

A. `df.shape`.

### Câu 2

A. `df.info()`.

### Câu 3

Để phát hiện sớm lỗi nhập dữ liệu, kiểu dữ liệu không phù hợp, giá trị thiếu và các quan sát bất thường.

## Đáp án câu hỏi nhanh — Bước 3

### Câu 1

A. Có thể làm giảm dữ liệu và gây thiên lệch.

### Câu 2

A. Trung vị.

### Câu 3

Sai. Dữ liệu sau khi điền vẫn có thể chứa mức độ không chắc chắn.

## Đáp án câu hỏi nhanh — Bước 4

### Câu 1

A. Độ lệch chuẩn.

### Câu 2

A. Độ bất đối xứng của phân phối.

### Câu 3

Vì trung bình dễ bị ảnh hưởng bởi ngoại lệ, trong khi trung vị bền vững hơn. So sánh hai đại lượng giúp hiểu rõ hơn hình dạng phân phối.

## Đáp án câu hỏi nhanh — Bước 5

### Câu 1

A. Biến phân loại.

### Câu 2

A. Từ 0 đến 1.

### Câu 3

A. Feature engineering.

## Đáp án câu hỏi nhanh — Bước 6

### Câu 1

A. Scatter plot.

### Câu 2

A. Trình bày ma trận tương quan.

### Câu 3

Vì biểu đồ có thể làm nổi bật xu hướng, cụm dữ liệu, điểm bất thường và mối quan hệ khó nhận biết từ bảng số.

## Đáp án câu hỏi nhanh — Bước 7

### Câu 1

D. Tất cả các phương án trên.

### Câu 2

D. Tất cả các phương án trên.

### Câu 3

Sai. Cần đánh giá nguyên nhân và ý nghĩa của ngoại lệ trước khi xử lý.

## Đáp án câu hỏi nhanh — Bước 8

### Câu 1

D. Tất cả các phương án trên.

### Câu 2

A. Để người đọc hiểu phạm vi và độ tin cậy của kết quả.

### Câu 3

A. Rõ ràng và dễ hiểu.

## Đáp án câu hỏi nhanh — Ứng dụng

### Câu 1

A. Tài chính.

### Câu 2

D. Tất cả các phương án trên.

### Câu 3

EDA có thể được sử dụng để khám phá lịch sử mua hàng, sản phẩm thường được mua cùng nhau, mức độ tương tác, nhóm người dùng và xu hướng sở thích.

## Đáp án ôn tập cuối bài

### Phần A

1. A  
2. A  
3. A  
4. A  
5. A  
6. D  
7. A  
8. A  
9. A  
10. A  

### Phần B

1. Sai.  
2. Đúng.  
3. Sai.  
4. Đúng.  
5. Đúng.  
6. Đúng.  
7. Đúng.  

### Phần C

**Câu 1.** EDA giúp hiểu cấu trúc dữ liệu, phát hiện mẫu hình, ngoại lệ, lỗi dữ liệu và mối quan hệ trước khi xây dựng mô hình.

**Câu 2.** Phân tích đơn biến xem một biến; phân tích hai biến xem mối quan hệ giữa hai biến; phân tích đa biến nghiên cứu từ ba biến trở lên.

**Câu 3.** Các bước gồm hiểu vấn đề, nhập và kiểm tra dữ liệu, xử lý dữ liệu thiếu, khám phá đặc điểm, biến đổi dữ liệu, trực quan hóa, xử lý ngoại lệ và truyền đạt kết quả.

**Câu 4.** Vì ngoại lệ có thể là lỗi nhưng cũng có thể là biến động thực tế có ý nghĩa.

**Câu 5.** Có thể điền bằng trung bình, trung vị, yếu vị, hồi quy, KNN hoặc loại bỏ trong trường hợp phù hợp.

**Câu 6.** Trực quan hóa giúp phát hiện xu hướng, cụm dữ liệu, ngoại lệ và truyền đạt kết quả dễ hiểu hơn.

### Phần D

Đây là các bài tập thực hành mở. Bài làm cần trình bày rõ mã lệnh, kết quả, biểu đồ và nhận xét. Các quyết định xử lý dữ liệu phải được giải thích dựa trên đặc điểm của bộ dữ liệu và mục tiêu phân tích.

</details>
