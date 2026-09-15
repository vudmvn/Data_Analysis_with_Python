# Biến đổi dữ liệu trong Machine Learning (Data Transformation in Machine Learning)

## Tóm tắt bài học

**Data Transformation** là quá trình chuyển đổi dữ liệu thô sang một dạng phù hợp hơn cho phân tích và xây dựng mô hình học máy. Đây là một bước quan trọng trong pipeline Machine Learning vì dữ liệu thực tế thường:

- thiếu giá trị;
- chứa nhiễu;
- có outliers;
- có phân phối lệch;
- chứa biến phân loại;
- có thang đo rất khác nhau;
- hoặc có quá nhiều đặc trưng.

Mục tiêu của Data Transformation là làm cho dữ liệu:

- nhất quán hơn;
- phù hợp hơn với thuật toán;
- dễ học hơn;
- ít bị ảnh hưởng bởi các giá trị bất thường;
- và thể hiện tốt hơn các mẫu có ý nghĩa trong dữ liệu.

Bài học này trình bày các nhóm kỹ thuật chính:

1. Handling Missing Data.
2. Dealing with Outliers.
3. Normalization và Standardization.
4. Encoding Categorical Variables.
5. Handling Skewed Distributions.
6. Feature Engineering.
7. Dimensionality Reduction.
8. Text Data Transformation.

---

# 1. Mục tiêu bài học

Sau bài học này, người học có thể:

- Giải thích được Data Transformation là gì.
- Nêu được vai trò của Data Transformation trong Machine Learning.
- Nhận diện các nhóm kỹ thuật biến đổi dữ liệu phổ biến.
- Áp dụng các chiến lược xử lý missing values.
- Áp dụng các kỹ thuật xử lý outliers.
- Phân biệt normalization và standardization.
- Mã hóa biến phân loại bằng one-hot, label và ordinal encoding.
- Giải thích các biến đổi cho dữ liệu bị skew.
- Tạo đặc trưng mới bằng feature engineering.
- Giải thích mục đích của PCA và t-SNE.
- Mô tả các bước biến đổi dữ liệu văn bản.
- Nhận diện nguy cơ information loss, overfitting và data leakage.

---

# 2. Data Transformation là gì?

Data Transformation là quá trình:

```text
Raw Data
   ↓
Modify / Convert / Restructure
   ↓
Transformed Data
   ↓
Analysis / Machine Learning
```

Mục tiêu là chuyển dữ liệu về định dạng phù hợp hơn với yêu cầu của:

- bài toán;
- hệ thống;
- hoặc thuật toán học máy.

Ví dụ:

```text
Raw categorical value:
"North", "South", "Central"
```

có thể được chuyển thành:

```text
0/1 variables
```

để đưa vào mô hình.

---

# 3. Data Transformation trong Machine Learning

Trong Machine Learning, Data Transformation thường nằm giữa:

```text
Data Cleaning
      ↓
Data Transformation
      ↓
Model Training
```

Các vấn đề thường được xử lý gồm:

```text
Missing Values
Outliers
Different Scales
Categorical Variables
Skewed Distributions
High Dimensionality
Raw Text
```

---

# 4. Vì sao Data Transformation quan trọng?

Raw data thường đến từ nhiều nguồn khác nhau và có thể:

- không nhất quán;
- thiếu dữ liệu;
- có format khác nhau;
- có đơn vị khác nhau;
- có biến số và biến phân loại trộn lẫn.

Transformation giúp:

- cải thiện chất lượng dữ liệu;
- tăng tính tương thích với thuật toán;
- hỗ trợ feature engineering;
- tăng khả năng học pattern;
- cải thiện độ ổn định của mô hình.

---

# 5. Tổng quan các kỹ thuật Data Transformation

Nguồn bài học tập trung vào 8 nhóm kỹ thuật lớn:

```text
1. Handling Missing Data
2. Dealing with Outliers
3. Normalization and Standardization
4. Encoding Categorical Variables
5. Handling Skewed Distribution
6. Feature Engineering
7. Dimensionality Reduction
8. Text Data Transformation
```

Lựa chọn phương pháp phụ thuộc vào:

```text
Data Characteristics
+
Machine Learning Algorithm
+
Problem Requirements
```

---

# 6. Handling Missing Data

Missing values là một trong những vấn đề phổ biến nhất.

Ví dụ:

```text
Age    Income
25     12
NaN    15
31     NaN
```

Nếu không xử lý, mô hình có thể:

- báo lỗi;
- học sai;
- hoặc giảm hiệu quả.

---

# 7. Removing Missing Data

Có thể xóa dòng hoặc cột chứa missing values.

Ví dụ:

```python
df_clean = df.dropna()
```

Hoặc:

```python
df_clean = df.dropna(
    subset=["Age"]
)
```

Phù hợp khi:

```text
Missing Rate nhỏ
```

Không phù hợp khi:

```text
Missing Rate lớn
```

vì có thể làm mất quá nhiều dữ liệu.

---

# 8. Imputation

Imputation là thay missing values bằng giá trị ước lượng.

Các cách phổ biến:

```text
Mean
Median
Mode
Constant
```

Ví dụ:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

---

# 9. Lưu ý khi Imputation

Trước khi impute cần xem xét:

- loại dữ liệu;
- phân phối;
- outliers;
- mức độ missing;
- ảnh hưởng đến variance.

Ví dụ:

```text
Mean imputation
```

không phù hợp khi biến bị skew mạnh.

---

# 10. KNNImputer

Nguồn cũng đề cập `KNNImputer`.

Ví dụ:

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(
    n_neighbors=5
)

X_imputed = imputer.fit_transform(X)
```

Ý tưởng:

```text
Missing value
→ tìm các quan sát gần nhất
→ ước lượng từ các neighbors
```

---

# 11. Forward Fill và Backward Fill

Thường dùng trong time series.

Forward fill:

```python
df["Sales"] = df["Sales"].ffill()
```

Backward fill:

```python
df["Sales"] = df["Sales"].bfill()
```

Ý nghĩa:

```text
ffill → dùng giá trị trước đó
bfill → dùng giá trị tiếp theo
```

---

# 12. Interpolation

Interpolation ước lượng missing values từ các điểm quan sát lân cận.

Ví dụ:

```python
df["Sales"] = df["Sales"].interpolate(
    method="linear"
)
```

Linear interpolation giả định:

```text
các điểm nằm trên xu hướng tuyến tính cục bộ
```

---

# 13. Dealing with Outliers

Outlier là điểm dữ liệu khác biệt đáng kể so với phần còn lại.

Ví dụ:

```text
10
12
11
13
120
```

Giá trị:

```text
120
```

có thể là outlier.

---

# 14. Identification of Outliers

Nguồn đề cập nhiều cách:

```text
Visual Inspection
Statistical Methods
Machine Learning Methods
```

---

# 15. Visual Inspection

Có thể dùng:

```text
Box Plot
Scatter Plot
```

Ví dụ:

```python
import seaborn as sns

sns.boxplot(
    x=df["Revenue"]
)
```

Hoặc:

```python
plt.scatter(
    df["Quantity"],
    df["Revenue"]
)
```

---

# 16. Statistical Methods

Hai phương pháp chính:

```text
Z-score
IQR
```

Ví dụ Z-score:

```python
from scipy import stats
import numpy as np

z = np.abs(
    stats.zscore(
        df["Revenue"]
    )
)
```

---

# 17. Machine Learning Methods cho Outlier Detection

Nguồn đề cập:

```text
Isolation Forest
One-Class SVM
```

Ví dụ:

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

labels = model.fit_predict(
    df[["Revenue"]]
)
```

Thông thường:

```text
-1 → anomaly
 1 → normal
```

---

# 18. Removing Outliers

Outliers có thể bị loại khi:

- là lỗi đo;
- là lỗi nhập liệu;
- không thuộc population nghiên cứu.

Nhưng không nên xóa nếu outlier là tín hiệu quan trọng.

Ví dụ:

```text
Fraud Detection
```

outliers có thể chính là các fraud transactions.

---

# 19. Transforming Outliers

Nguồn đề cập các biến đổi:

```text
Log Transformation
Square Root Transformation
Box-Cox Transformation
```

Ví dụ log:

```python
df["Revenue_log"] = np.log1p(
    df["Revenue"]
)
```

---

# 20. Truncation

Truncation giới hạn extreme values bằng thresholds.

Ví dụ:

```python
df["Revenue"] = df["Revenue"].clip(
    lower=lower,
    upper=upper
)
```

Ý tưởng:

```text
Extreme value
→ replace bằng boundary
```

---

# 21. Binning và Discretization

Binning chuyển continuous values thành các nhóm rời rạc.

Ví dụ:

```text
Age
18–25
26–40
41–60
60+
```

---

# 22. KBinsDiscretizer

```python
from sklearn.preprocessing import KBinsDiscretizer

kbins = KBinsDiscretizer(
    n_bins=4,
    encode="ordinal",
    strategy="quantile"
)

age_bins = kbins.fit_transform(
    df[["Age"]]
)
```

---

# 23. Normalization

Normalization thường đưa dữ liệu về khoảng:

```text
[0, 1]
```

Công thức:

\[
x_i' =
\frac{x_i - \min(X)}
{\max(X) - \min(X)}
\]

---

# 24. MinMaxScaler

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)
```

---

# 25. Vì sao dùng Normalization?

Nếu các feature có thang đo rất khác nhau:

```text
Age: 18–80
Income: 5,000,000–100,000,000
```

thuật toán dựa trên khoảng cách có thể bị `Income` chi phối.

Normalization giúp đưa các biến về scale tương tự.

---

# 26. Standardization

Standardization đưa feature về:

```text
Mean ≈ 0
Std ≈ 1
```

Công thức:

\[
x_i' =
\frac{x_i-\mu}
{\sigma}
\]

---

# 27. StandardScaler

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_std = scaler.fit_transform(
    X_train
)

X_test_std = scaler.transform(
    X_test
)
```

---

# 28. So sánh Normalization và Standardization

| Nội dung | Normalization | Standardization |
|---|---|---|
| Dựa trên | Min/Max | Mean/Std |
| Khoảng | Thường [0,1] | Không cố định |
| Mean = 0 | Không | Có |
| Std = 1 | Không | Có |
| Nhạy outlier | Cao | Có |
| Dùng nhiều với | k-NN, NN | SVM, Logistic, PCA |

---

# 29. Lưu ý về Fit và Transform

Sai:

```python
scaler.fit_transform(X)
```

trước khi chia train/test.

Đúng:

```python
scaler.fit(X_train)

X_train_scaled = scaler.transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)
```

Quy tắc:

> **Chỉ fit transformation trên training data.**

---

# 30. Encoding Categorical Variables

Nhiều thuật toán yêu cầu numerical input.

Ví dụ:

```text
Vehicle
Car
Bike
Bicycle
```

cần được mã hóa.

Nguồn trình bày:

```text
One-Hot Encoding
Label Encoding
Ordinal Encoding
```

---

# 31. One-Hot Encoding

One-hot encoding tạo một binary feature cho mỗi category.

Ví dụ:

```text
Vehicle = Car
```

thành:

```text
is_car = 1
is_bike = 0
is_bicycle = 0
```

---

# 32. OneHotEncoder

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(
    handle_unknown="ignore"
)

encoded = encoder.fit_transform(
    df[["Vehicle"]]
)
```

---

# 33. Label Encoding

Label Encoding gán số cho category.

Ví dụ:

```text
small  → 0
medium → 1
large  → 2
```

Trong scikit-learn:

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["Size_Code"] = le.fit_transform(
    df["Size"]
)
```

---

# 34. Ordinal Encoding

Ordinal Encoding dùng khi category có thứ tự.

Ví dụ:

```text
High School
Bachelor
Master
```

có thể mã hóa:

```text
0
1
2
```

---

# 35. Khi nào không nên dùng Label Encoding?

Nếu biến:

```text
Color = Red, Blue, Green
```

không có thứ tự tự nhiên, mã hóa:

```text
Red = 0
Blue = 1
Green = 2
```

có thể làm mô hình hiểu nhầm rằng:

```text
Green > Blue > Red
```

Trong trường hợp đó, one-hot thường phù hợp hơn.

---

# 36. Handling Skewed Distribution

Skewed distribution là phân phối không đối xứng.

Ví dụ:

```text
Income
Revenue
Transaction Amount
```

thường right-skewed.

Nguồn đề cập:

```text
Log Transformation
Square Root Transformation
Box-Cox
Yeo-Johnson
Quantile Transformation
```

---

# 37. Log Transformation

Phù hợp với dữ liệu right-skewed.

Ví dụ:

```python
df["Revenue_log"] = np.log1p(
    df["Revenue"]
)
```

`log1p(x)` tính:

\[
\log(1+x)
\]

giúp xử lý cả giá trị bằng 0.

---

# 38. Square Root Transformation

```python
df["Revenue_sqrt"] = np.sqrt(
    df["Revenue"]
)
```

Tác động nhẹ hơn log transformation.

Phù hợp với:

```text
moderately right-skewed data
```

---

# 39. Box-Cox Transformation

Nguồn mô tả Box-Cox là biến đổi dùng parameter:

```text
λ
```

để tìm dạng transformation phù hợp.

Ví dụ:

```python
from scipy.stats import boxcox

transformed, lam = boxcox(
    df["Revenue"]
)
```

Lưu ý:

```text
Box-Cox yêu cầu dữ liệu dương.
```

---

# 40. Yeo-Johnson Transformation

Yeo-Johnson tương tự Box-Cox nhưng linh hoạt hơn.

Có thể hoạt động với:

```text
positive values
zero
negative values
```

Ví dụ:

```python
from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(
    method="yeo-johnson"
)

X_transformed = pt.fit_transform(
    X_train
)
```

---

# 41. Quantile Transformation

Quantile Transformation ánh xạ dữ liệu dựa trên percentile.

Ví dụ:

```python
from sklearn.preprocessing import QuantileTransformer

qt = QuantileTransformer(
    output_distribution="normal"
)

X_q = qt.fit_transform(
    X_train
)
```

---

# 42. Feature Engineering

Feature Engineering là quá trình:

```text
create new features
or
modify existing features
```

để thể hiện pattern tốt hơn.

---

# 43. Polynomial Features

Polynomial features giúp mô hình tuyến tính biểu diễn nonlinear relationships.

Ví dụ:

```text
x
x²
x³
```

Trong sklearn:

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X)
```

---

# 44. Interaction Terms

Interaction term kết hợp hai feature.

Ví dụ:

```text
Length
Width
```

tạo:

```text
Area = Length × Width
```

Python:

```python
df["Area"] = (
    df["Length"]
    * df["Width"]
)
```

---

# 45. Domain-Specific Features

Nguồn nhấn mạnh việc tạo feature cần hiểu domain.

Ví dụ kinh doanh:

```text
Revenue = Quantity × Unit_Price
```

Ví dụ khách hàng:

```text
Average_Order_Value
Customer_Tenure
Purchase_Frequency
```

Những feature này có thể mang nhiều ý nghĩa hơn dữ liệu thô ban đầu.

---

# 46. Dimensionality Reduction

Dimensionality Reduction giảm số lượng features nhưng cố gắng giữ lại thông tin quan trọng.

Mục tiêu:

- giảm computational complexity;
- giảm nguy cơ overfitting;
- giúp visualization;
- giảm redundancy.

Nguồn tập trung vào:

```text
PCA
t-SNE
```

---

# 47. PCA

Principal Component Analysis biến đổi dữ liệu nhiều chiều thành các principal components.

Quy trình khái quát:

```text
Standardize Data
      ↓
Covariance Matrix
      ↓
Eigenvalues / Eigenvectors
      ↓
Principal Components
      ↓
Lower-dimensional Representation
```

---

# 48. PCA với scikit-learn

```python
from sklearn.decomposition import PCA

pca = PCA(
    n_components=2
)

X_pca = pca.fit_transform(
    X_scaled
)
```

---

# 49. Ý nghĩa của PCA

PCA cố gắng giữ:

```text
maximum variance
```

trong số ít dimensions hơn.

Ví dụ:

```text
20 features
→
2 principal components
```

có thể dùng để visualization.

---

# 50. t-SNE

t-SNE là phương pháp giảm chiều tập trung vào việc bảo toàn:

```text
local relationships
```

giữa các data points.

Nó thường được dùng cho:

```text
Visualization
```

hơn là trực tiếp thay thế feature engineering cho production model.

---

# 51. Text Data Transformation

Raw text thường không thể đưa trực tiếp vào nhiều ML algorithms.

Nguồn đề cập:

```text
Text Cleaning
Tokenization
Stopword Removal
Stemming
Lemmatization
TF-IDF
Word Embeddings
```

---

# 52. Text Cleaning

Ví dụ raw text:

```text
"<p>Hello!!! WORLD</p>"
```

có thể được xử lý:

```text
hello world
```

Các bước có thể gồm:

- loại HTML;
- punctuation;
- special characters;
- chuyển lowercase.

---

# 53. Tokenization

Tokenization chia văn bản thành tokens.

Ví dụ:

```text
"This is a statement"
```

thành:

```text
"This"
"is"
"a"
"statement"
```

---

# 54. Stopword Removal

Stopwords là các từ thường xuất hiện nhưng có thể ít mang nội dung.

Ví dụ:

```text
and
or
the
```

Việc loại bỏ phụ thuộc vào task NLP cụ thể.

---

# 55. Stemming

Stemming đưa từ về stem gần đúng.

Ví dụ:

```text
sleeping
→
sleep
```

---

# 56. Lemmatization

Lemmatization dùng ý nghĩa ngôn ngữ để đưa về lemma.

Ví dụ:

```text
worse
→
bad
```

---

# 57. TF-IDF

TF-IDF đo mức độ quan trọng của một term trong một document so với collection.

Khái niệm:

```text
TF = Term Frequency
IDF = Inverse Document Frequency
```

Từ xuất hiện nhiều trong một document nhưng ít trong các document khác có thể có trọng số cao.

---

# 58. TF-IDF bằng scikit-learn

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X_text = vectorizer.fit_transform(
    documents
)
```

---

# 59. Word Embeddings

Word Embeddings biểu diễn từ bằng vectors trong không gian nhiều chiều.

Ý tưởng:

```text
similar words
→
vectors gần nhau
```

Ví dụ:

```text
king
queen
man
woman
```

có thể có các quan hệ hình học trong vector space.

---

# 60. Ưu điểm của Data Transformation

Nguồn nêu các lợi ích:

- cải thiện model performance;
- xử lý missing data;
- giúp optimization convergence tốt hơn;
- hỗ trợ dimensionality reduction;
- tạo feature hữu ích hơn.

---

# 61. Hạn chế của Data Transformation

Nguồn cũng chỉ ra các rủi ro:

```text
Information Loss
Overfitting
Data Leakage
Increased Complexity
Assumption Violation
```

---

# 62. Information Loss

Nếu transformation quá mạnh:

```text
useful information
→
lost
```

Ví dụ:

- xóa quá nhiều rows;
- binning quá thô;
- giảm chiều quá mức.

---

# 63. Risk of Overfitting

Feature engineering quá phức tạp có thể tạo:

```text
too many derived features
```

Mô hình có thể học quá sát training data.

---

# 64. Data Leakage

Nguồn nhấn mạnh transformation áp dụng không đúng có thể gây leakage.

Ví dụ sai:

```python
scaler.fit_transform(X)
```

trước khi chia train/test.

Hoặc:

```python
imputer.fit(X)
```

trên toàn bộ dataset.

---

# 65. Quy trình đúng để tránh Data Leakage

```text
Raw Data
   ↓
Train/Test Split
   ↓
Fit Transformation on Train
   ↓
Transform Train
   ↓
Transform Test using same fitted parameters
   ↓
Train Model
   ↓
Evaluate
```

---

# 66. Pipeline trong scikit-learn

Dùng Pipeline giúp giảm lỗi preprocessing.

Ví dụ:

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="median"
            )
        ),
        (
            "scaler",
            StandardScaler()
        ),
        (
            "model",
            LogisticRegression(
                max_iter=1000
            )
        )
    ]
)
```

Huấn luyện:

```python
pipeline.fit(
    X_train,
    y_train
)
```

---

# 67. ColumnTransformer

Khi dataset có:

```text
numeric variables
+
categorical variables
```

có thể dùng `ColumnTransformer`.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numeric_cols
        ),
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_cols
        )
    ]
)
```

---

# 68. Ví dụ quy trình Data Transformation tổng hợp

Giả sử dataset khách hàng:

```text
Age
Income
Region
Customer_Type
Monthly_Spending
Churn
```

Có thể áp dụng:

```text
Age
→ median imputation
→ standardization

Income
→ median imputation
→ log transform
→ standardization

Region
→ mode imputation
→ one-hot encoding

Customer_Type
→ mode
→ one-hot encoding
```

---

# 69. Data Transformation không phải càng nhiều càng tốt

Không nên nghĩ:

```text
more transformations
=
better model
```

Transformation chỉ nên được áp dụng khi:

- có vấn đề rõ ràng;
- có lý do thống kê;
- có lý do nghiệp vụ;
- hoặc mô hình thực sự cần.

---

# 70. Quy trình lựa chọn Transformation

```text
1. Understand data
2. Explore distribution
3. Identify problem
4. Choose transformation
5. Fit on training data
6. Transform validation/test
7. Evaluate model
8. Keep only useful transformations
```

---

# 71. Bài tập thực hành 1 — Missing Data

Cho:

```python
data = {
    "Age": [
        25,
        30,
        np.nan,
        42,
        38
    ],
    "Income": [
        20,
        np.nan,
        40,
        80,
        60
    ]
}

df = pd.DataFrame(data)
```

Yêu cầu:

1. Kiểm tra missing values.
2. Impute `Age` bằng median.
3. Impute `Income` bằng mean.
4. So sánh trước và sau.

---

# 72. Bài tập thực hành 2 — Outlier Transformation

Cho:

```python
revenue = pd.Series(
    [10, 12, 15, 18, 300]
)
```

Yêu cầu:

1. Vẽ box plot.
2. Tính log transform.
3. So sánh original vs log-transformed.
4. Nhận xét ảnh hưởng của giá trị 300.

---

# 73. Bài tập thực hành 3 — Scaling

Cho:

```python
df = pd.DataFrame({
    "Age": [20, 30, 40, 50],
    "Income": [
        5_000_000,
        10_000_000,
        20_000_000,
        50_000_000
    ]
})
```

Thực hiện:

```text
MinMaxScaler
StandardScaler
```

Sau đó so sánh kết quả.

---

# 74. Bài tập thực hành 4 — Encoding

Cho:

```text
Education
High School
Bachelor
Master
```

Hãy:

1. Mã hóa bằng Label Encoding.
2. Mã hóa bằng Ordinal Encoding.
3. Giải thích tại sao Ordinal Encoding phù hợp hơn.

---

# 75. Bài tập thực hành 5 — Feature Engineering

Cho:

```text
Length
Width
Price
```

Tạo:

```text
Area = Length × Width
```

Sau đó thảo luận:

```text
Area
```

có thể hữu ích hơn từng biến riêng lẻ trong bài toán dự đoán giá nhà như thế nào.

---

# 76. Tự kiểm tra

### Câu 1

Data Transformation là gì?

A. Chỉ là xóa missing values  
B. Quá trình chuyển dữ liệu sang dạng phù hợp hơn cho phân tích và modeling  
C. Chỉ là scaling  
D. Chỉ là encoding

---

### Câu 2

Kỹ thuật nào phù hợp với categorical variables?

A. One-Hot Encoding  
B. PCA  
C. Z-score  
D. IQR

---

### Câu 3

Normalization thường đưa dữ liệu về khoảng nào?

A. `[0,1]`  
B. `[-100,100]`  
C. Không xác định  
D. `[1,10]`

---

### Câu 4

Standardization thường tạo dữ liệu có:

A. min = 0, max = 1  
B. mean ≈ 0, std ≈ 1  
C. median = 0  
D. Q1 = Q3

---

### Câu 5

Biến đổi nào phù hợp cho right-skewed data?

A. Log transformation  
B. One-hot encoding  
C. PCA  
D. Label encoding

---

### Câu 6

Box-Cox khác Yeo-Johnson ở điểm nào?

---

### Câu 7

Interaction term là gì?

---

### Câu 8

PCA được dùng để làm gì?

---

### Câu 9

TF-IDF dùng với loại dữ liệu nào?

---

### Câu 10

Data leakage trong transformation có thể xảy ra như thế nào?

---

# 77. Bài tập tổng hợp — Xây dựng Data Transformation Pipeline

Cho dataset:

```text
customers.csv
```

với các cột:

```text
Customer_ID
Age
Income
Region
Education
Monthly_Spending
Tenure
Churn
```

Yêu cầu:

1. Đọc dữ liệu.
2. Kiểm tra missing values.
3. Kiểm tra outliers.
4. Kiểm tra skewness.
5. Tách:
   - numerical features;
   - categorical features.
6. Chia train/test.
7. Impute numerical features.
8. Impute categorical features.
9. Log transform `Income` nếu bị right-skew.
10. Standardize numerical variables.
11. One-hot encode `Region`.
12. Ordinal encode `Education`.
13. Tạo feature:
   - `Spending_per_Month_of_Tenure`.
14. Dùng `ColumnTransformer`.
15. Dùng `Pipeline`.
16. Huấn luyện một classifier.
17. Đánh giá trên test set.
18. Giải thích cách pipeline tránh data leakage.

---

# 78. Checklist Data Transformation

```text
□ Tôi đã hiểu cấu trúc dữ liệu chưa?
□ Tôi đã kiểm tra missing values chưa?
□ Tôi đã kiểm tra outliers chưa?
□ Tôi đã kiểm tra skewness chưa?
□ Tôi đã xác định biến số và biến phân loại chưa?
□ Tôi đã chọn scaling phù hợp chưa?
□ Tôi đã chọn encoding phù hợp chưa?
□ Tôi đã cân nhắc feature engineering chưa?
□ Tôi có thực sự cần dimensionality reduction không?
□ Tôi đã fit transformation chỉ trên training set chưa?
□ Tôi đã dùng cùng transformation cho test/new data chưa?
□ Tôi đã kiểm tra nguy cơ data leakage chưa?
□ Tôi đã đánh giá tác động của transformation lên model chưa?
```

---

# 79. Tóm tắt bài học

Các điểm cần ghi nhớ:

- **Data Transformation** giúp chuyển raw data sang dạng phù hợp hơn cho Machine Learning.
- Các nhóm kỹ thuật chính gồm:
  - missing data handling;
  - outlier handling;
  - normalization/standardization;
  - categorical encoding;
  - skewness transformation;
  - feature engineering;
  - dimensionality reduction;
  - text transformation.
- Không có một transformation phù hợp cho mọi dataset.
- Lựa chọn transformation phải dựa trên:
  - đặc điểm dữ liệu;
  - thuật toán;
  - mục tiêu phân tích.
- Simple transformations có thể cải thiện đáng kể model performance.
- Transformation quá mạnh có thể gây:
  - information loss;
  - overfitting;
  - complexity.
- Fit transformation trên toàn bộ dataset có thể gây **data leakage**.
- Cách làm an toàn là:
  - split data;
  - fit trên training;
  - transform validation/test bằng cùng các tham số đã học.
- `Pipeline` và `ColumnTransformer` giúp tổ chức preprocessing nhất quán.

---

## Tài liệu tham khảo

GeeksforGeeks. *Data Transformation in Machine Learning*. Last Updated: 23 Jul, 2025.
