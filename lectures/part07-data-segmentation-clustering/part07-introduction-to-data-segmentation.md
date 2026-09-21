# Bài giảng: Data Segmentation trong Machine Learning

## 1. Giới thiệu

Trong các bài toán Khoa học dữ liệu, một tập dữ liệu thường chứa nhiều nhóm quan sát có đặc điểm và hành vi khác nhau. Nếu phân tích toàn bộ dữ liệu như một khối đồng nhất, chúng ta có thể bỏ qua những khác biệt quan trọng giữa các nhóm.

**Data Segmentation** là quá trình chia các quan sát trong dữ liệu thành các nhóm có ý nghĩa dựa trên một hoặc nhiều đặc điểm. Mục tiêu là giúp người phân tích hiểu rõ hơn cấu trúc của dữ liệu, phát hiện các nhóm có hành vi tương đồng và từ đó đưa ra các quyết định phù hợp cho từng nhóm.

Ví dụ:

- Một doanh nghiệp bán lẻ có thể chia khách hàng thành nhóm mua thường xuyên, mua không thường xuyên và khách hàng có nguy cơ rời bỏ.
- Một ngân hàng có thể phân nhóm khách hàng theo mức độ rủi ro tín dụng.
- Một công ty logistics có thể phân nhóm đơn hàng theo khoảng cách, khối lượng và mức độ khẩn cấp.
- Một nền tảng số có thể phân nhóm người dùng theo hành vi sử dụng dịch vụ.

Trong Machine Learning, segmentation đặc biệt liên quan đến **phân cụm (clustering)**, một nhóm phương pháp học không giám sát dùng để phát hiện cấu trúc nhóm tiềm ẩn trong dữ liệu.

> **Lưu ý về thuật ngữ:** Data segmentation không nên nhầm với **data partitioning**, tức việc chia dữ liệu thành tập huấn luyện, tập validation và tập kiểm tra. Segmentation nhằm tìm hoặc xác định các nhóm có ý nghĩa trong dữ liệu; data partitioning nhằm phục vụ huấn luyện và đánh giá mô hình.

---

## 2. Mục tiêu bài học

Sau bài học này, người học có thể:

- Giải thích được khái niệm Data Segmentation.
- Phân biệt Data Segmentation với Data Partitioning và Targeting.
- Mô tả được vai trò của segmentation trong phân tích dữ liệu và Machine Learning.
- Phân biệt segmentation dựa trên quy tắc, có giám sát, không giám sát và bán giám sát.
- Mô tả được quy trình xây dựng một bài toán segmentation.
- Nhận biết một số thuật toán phổ biến như K-Means, Hierarchical Clustering, DBSCAN và Gaussian Mixture Model.
- Đánh giá kết quả segmentation bằng cả tiêu chí kỹ thuật và tiêu chí nghiệp vụ.
- Thực hiện một ví dụ phân nhóm khách hàng bằng Python và K-Means.
- Liên hệ Data Segmentation với các bài toán trong kinh doanh, kinh tế, tài chính và vận hành.

---

## 3. Data Segmentation là gì?

**Data Segmentation** là quá trình chia một tập dữ liệu thành các nhóm nhỏ hơn dựa trên các đặc điểm, hành vi hoặc tiêu chí nhất định.

Giả sử tập dữ liệu gồm $n$ quan sát:

$$
D = \{x_1, x_2, \ldots, x_n\}
$$

Segmentation tìm cách chia $D$ thành các nhóm:

$$
S_1, S_2, \ldots, S_K
$$

sao cho các quan sát trong cùng một nhóm có một số đặc điểm tương đồng và các nhóm có ý nghĩa đối với mục tiêu phân tích.

Trong bài toán phân cụm, ta thường mong muốn:

- các quan sát **trong cùng một nhóm** càng giống nhau càng tốt;
- các quan sát **thuộc các nhóm khác nhau** càng khác nhau càng tốt.

### Ví dụ: phân nhóm khách hàng

Giả sử doanh nghiệp có dữ liệu:

| Customer | Age | Annual Spending | Orders per Month |
|---|---:|---:|---:|
| A | 22 | 8 | 1 |
| B | 25 | 10 | 2 |
| C | 40 | 55 | 8 |
| D | 43 | 61 | 9 |
| E | 63 | 25 | 3 |
| F | 67 | 28 | 3 |

Một phương pháp segmentation có thể phát hiện ba nhóm:

- **Nhóm 1:** khách hàng trẻ, chi tiêu thấp;
- **Nhóm 2:** khách hàng trung niên, chi tiêu cao và mua thường xuyên;
- **Nhóm 3:** khách hàng lớn tuổi, mức chi tiêu trung bình.

Điều quan trọng là thuật toán chỉ tạo ra các nhóm dựa trên dữ liệu. Việc gán tên như “khách hàng giá trị cao” hay “khách hàng ít hoạt động” cần dựa trên **phân tích đặc điểm của từng nhóm và kiến thức nghiệp vụ**.

---

## 4. Vì sao Data Segmentation quan trọng?

### 4.1. Hiểu cấu trúc của dữ liệu

Một giá trị trung bình của toàn bộ dữ liệu có thể che giấu sự khác biệt giữa các nhóm.

Ví dụ, doanh thu trung bình trên mỗi khách hàng là 3 triệu đồng không có nghĩa phần lớn khách hàng đều chi khoảng 3 triệu đồng. Có thể tồn tại:

- một nhóm rất lớn chỉ chi 0,5–1 triệu đồng;
- một nhóm nhỏ nhưng chi 10–20 triệu đồng.

Segmentation giúp phát hiện các cấu trúc như vậy.

### 4.2. Hỗ trợ cá nhân hóa

Các nhóm khác nhau có thể cần:

- thông điệp marketing khác nhau;
- mức giá hoặc ưu đãi khác nhau;
- sản phẩm khác nhau;
- mức độ chăm sóc khác nhau.

### 4.3. Hỗ trợ xây dựng mô hình tốt hơn

Nếu các nhóm trong dữ liệu có hành vi rất khác nhau, có thể xây dựng mô hình riêng cho từng segment.

Ví dụ:

- mô hình dự báo nhu cầu cho cửa hàng trung tâm thành phố;
- mô hình khác cho cửa hàng ngoại thành.

### 4.4. Phân bổ nguồn lực

Segmentation giúp doanh nghiệp xác định nhóm nào cần được ưu tiên.

Ví dụ:

- tập trung chăm sóc nhóm khách hàng có giá trị vòng đời cao;
- ưu tiên kiểm tra các giao dịch thuộc nhóm rủi ro cao;
- ưu tiên phương tiện cho các tuyến giao hàng có nhu cầu cao.

### 4.5. Hỗ trợ quản trị rủi ro

Trong tài chính và bảo hiểm, segmentation có thể giúp xác định:

- nhóm khách hàng có khả năng vỡ nợ cao;
- nhóm giao dịch bất thường;
- nhóm hợp đồng có mức độ rủi ro tương tự.

---

## 5. Segmentation và Data Partitioning

Hai khái niệm này thường dễ bị nhầm lẫn.

| Tiêu chí | Data Segmentation | Data Partitioning |
|---|---|---|
| Mục tiêu | Tìm hoặc tạo ra các nhóm có ý nghĩa | Chia dữ liệu để huấn luyện và đánh giá mô hình |
| Cơ sở chia | Đặc điểm, hành vi, độ tương đồng, nhãn hoặc quy tắc | Thường ngẫu nhiên, theo thời gian hoặc theo thiết kế thí nghiệm |
| Ví dụ | Phân khách hàng thành 4 nhóm hành vi | 70% train, 15% validation, 15% test |
| Thuật toán thường gặp | K-Means, Hierarchical, DBSCAN, GMM | `train_test_split`, cross-validation |
| Kết quả | Mỗi quan sát có một segment | Mỗi quan sát thuộc một tập train/validation/test |

**Không nên nói:** “chia dữ liệu thành train và test là customer segmentation”.

---

## 6. Segmentation và Targeting

Trong kinh doanh, segmentation thường đi trước targeting.

### Segmentation

Trả lời câu hỏi:

> **Trong dữ liệu hoặc thị trường tồn tại những nhóm nào?**

Ví dụ:

- nhóm khách hàng mua thường xuyên;
- nhóm nhạy cảm với giá;
- nhóm giá trị cao;
- nhóm có nguy cơ rời bỏ.

### Targeting

Trả lời câu hỏi:

> **Doanh nghiệp nên tập trung vào nhóm nào cho một mục tiêu cụ thể?**

Ví dụ:

Sau khi có bốn segment, doanh nghiệp chỉ chọn nhóm “giá trị cao nhưng có nguy cơ rời bỏ” để triển khai chương trình giữ chân.

Quy trình có thể biểu diễn:

$$
\text{Data} \rightarrow \text{Segmentation} \rightarrow \text{Profiling} \rightarrow \text{Targeting} \rightarrow \text{Action}
$$

---

## 7. Các cách tiếp cận Data Segmentation

### 7.1. Segmentation dựa trên quy tắc

Đây là cách đơn giản nhất. Các nhóm được xác định trước bằng các quy tắc nghiệp vụ.

Ví dụ:

```text
Nếu annual_spending >= 50 triệu  -> High Value
Nếu annual_spending từ 20-50 triệu -> Medium Value
Nếu annual_spending < 20 triệu -> Low Value
```

Ưu điểm:

- dễ hiểu;
- dễ triển khai;
- phù hợp khi tổ chức đã có tiêu chuẩn nghiệp vụ rõ ràng.

Hạn chế:

- phụ thuộc mạnh vào ngưỡng do con người đặt ra;
- khó phát hiện các cấu trúc mới trong dữ liệu;
- có thể bỏ qua tương tác giữa nhiều biến.

---

### 7.2. Unsupervised Segmentation

Trong **học không giám sát**, dữ liệu không có sẵn nhãn segment. Thuật toán phải phát hiện các nhóm dựa trên độ tương đồng giữa các quan sát.

Đây là cách tiếp cận phổ biến trong **customer segmentation**.

Một số thuật toán thường dùng:

- K-Means;
- Hierarchical Clustering;
- DBSCAN;
- Gaussian Mixture Model.

Ví dụ:

```text
Dữ liệu khách hàng
        |
        v
Age, Income, Spending, Frequency
        |
        v
Chuẩn hóa dữ liệu
        |
        v
Clustering
        |
        v
Cluster 0   Cluster 1   Cluster 2
        |
        v
Phân tích đặc điểm và đặt tên segment
```

---

### 7.3. Supervised Segmentation

Trong cách tiếp cận có giám sát, các nhóm hoặc lớp đã được xác định trong dữ liệu huấn luyện.

Ví dụ, doanh nghiệp đã có nhãn:

- `VIP`;
- `Regular`;
- `At Risk`.

Khi đó bài toán thực chất gần với **classification**: học từ các khách hàng đã biết nhãn để gán segment cho khách hàng mới.

Các thuật toán có thể sử dụng:

- Decision Tree;
- Logistic Regression;
- Random Forest;
- Support Vector Machine;
- Neural Network.

Điểm khác biệt quan trọng:

- **Unsupervised segmentation:** tìm ra nhóm chưa biết trước.
- **Supervised segmentation:** dự đoán nhóm đã được định nghĩa trước.

---

### 7.4. Semi-supervised Segmentation

Semi-supervised segmentation sử dụng:

- một lượng nhỏ dữ liệu có nhãn;
- một lượng lớn dữ liệu chưa có nhãn.

Cách tiếp cận này hữu ích khi việc gán nhãn tốn kém.

Ví dụ:

Một ngân hàng có 500 khách hàng đã được chuyên gia phân nhóm thủ công nhưng có 100.000 khách hàng chưa được gán nhóm. Semi-supervised learning có thể tận dụng cả hai phần dữ liệu.

---

## 8. Các thuật toán phân cụm thường dùng

## 8.1. K-Means

K-Means chia dữ liệu thành $K$ cụm.

Mục tiêu của K-Means là giảm tổng khoảng cách bình phương từ các điểm đến tâm cụm:

$$
J = \sum_{k=1}^{K}\sum_{x_i \in C_k} \|x_i-\mu_k\|^2
$$

trong đó:

- $C_k$ là cụm thứ $k$;
- $\mu_k$ là tâm của cụm $k$.

### Quy trình cơ bản

1. Chọn số cụm $K$.
2. Khởi tạo $K$ tâm cụm.
3. Gán mỗi quan sát vào tâm gần nhất.
4. Tính lại tâm của từng cụm.
5. Lặp bước 3–4 cho đến khi kết quả ổn định.

### Ưu điểm

- đơn giản;
- nhanh;
- dễ triển khai;
- phù hợp với dữ liệu lớn.

### Hạn chế

- cần chọn trước $K$;
- nhạy với thang đo của biến;
- nhạy với outlier;
- hoạt động tốt hơn khi các cụm tương đối “tròn” và có kích thước tương đương.

---

## 8.2. Hierarchical Clustering

Hierarchical Clustering xây dựng cấu trúc phân cấp giữa các quan sát hoặc cụm.

Cách phổ biến là **agglomerative clustering**:

1. ban đầu mỗi quan sát là một cụm;
2. tìm hai cụm gần nhau nhất;
3. gộp chúng;
4. tiếp tục cho đến khi còn một cụm.

Kết quả thường được biểu diễn bằng **dendrogram**.

Phương pháp này hữu ích khi:

- muốn quan sát quan hệ phân cấp;
- chưa chắc chắn về số lượng cụm;
- kích thước dữ liệu không quá lớn.

---

## 8.3. DBSCAN

DBSCAN là phương pháp phân cụm dựa trên mật độ.

Ý tưởng:

- vùng có nhiều điểm gần nhau tạo thành cluster;
- điểm nằm ở khu vực quá thưa có thể được coi là **noise/outlier**.

Ưu điểm:

- không cần chỉ định trực tiếp số cụm;
- có thể phát hiện cluster có hình dạng phức tạp;
- phát hiện điểm nhiễu.

Hạn chế:

- nhạy với các tham số;
- khó sử dụng khi mật độ các cluster rất khác nhau.

---

## 8.4. Gaussian Mixture Model

Gaussian Mixture Model (GMM) giả định dữ liệu được tạo ra từ hỗn hợp nhiều phân phối Gaussian.

Khác với K-Means thường gán cứng mỗi quan sát vào một cluster, GMM có thể đưa ra xác suất:

$$
P(C_k \mid x_i)
$$

Ví dụ:

```text
Khách hàng A:
- Segment 1: 0.10
- Segment 2: 0.75
- Segment 3: 0.15
```

Điều này hữu ích khi ranh giới giữa các segment không rõ ràng.

---

## 9. Quy trình thực hiện một bài toán Data Segmentation

### Bước 1. Xác định mục tiêu

Không nên bắt đầu bằng câu hỏi:

> “Có thể chạy K-Means trên dữ liệu này không?”

Nên bắt đầu bằng câu hỏi nghiệp vụ:

> “Doanh nghiệp muốn hiểu điều gì và sẽ làm gì với các segment?”

Ví dụ:

- phân nhóm khách hàng để thiết kế chương trình loyalty;
- phân nhóm cửa hàng để lập chính sách tồn kho;
- phân nhóm nhà cung cấp để quản trị rủi ro;
- phân nhóm sản phẩm để thiết kế chính sách replenishment.

---

### Bước 2. Xác định đơn vị phân tích

Mỗi dòng dữ liệu đại diện cho gì?

Có thể là:

- khách hàng;
- sản phẩm;
- cửa hàng;
- đơn hàng;
- doanh nghiệp;
- giao dịch;
- nhà cung cấp.

Đây là quyết định rất quan trọng.

---

### Bước 3. Chọn biến dùng để segmentation

Ví dụ với khách hàng:

- `Recency`: số ngày từ lần mua gần nhất;
- `Frequency`: số lần mua;
- `Monetary`: tổng giá trị mua;
- `AverageOrderValue`;
- tỷ lệ sử dụng coupon;
- tỷ lệ trả hàng.

Không nên đưa vào tất cả các biến chỉ vì chúng có sẵn.

---

### Bước 4. Tiền xử lý dữ liệu

Các bước thường gặp:

- xử lý missing values;
- xử lý outlier;
- encoding biến categorical;
- chuẩn hóa biến số;
- loại bỏ biến không cần thiết;
- tạo thêm các biến có ý nghĩa nghiệp vụ.

### Tại sao scaling quan trọng?

Giả sử ta sử dụng hai biến:

- `Annual Income`: từ 100 đến 1.000 triệu đồng;
- `Purchase Frequency`: từ 1 đến 20.

Nếu dùng khoảng cách Euclidean trực tiếp, `Annual Income` có thể chi phối gần như toàn bộ khoảng cách.

Do đó thường cần chuẩn hóa:

$$
z_i = \frac{x_i-\bar{x}}{s}
$$

---

### Bước 5. Chọn thuật toán

Ví dụ:

| Đặc điểm dữ liệu | Thuật toán có thể cân nhắc |
|---|---|
| Muốn cách làm đơn giản, dễ giải thích | K-Means |
| Muốn xem cấu trúc phân cấp | Hierarchical Clustering |
| Có nhiều điểm nhiễu | DBSCAN |
| Muốn xác suất thuộc từng nhóm | Gaussian Mixture Model |

Không có thuật toán tốt nhất cho mọi dữ liệu.

---

### Bước 6. Chọn số lượng cluster

Với K-Means, cần xác định $K$.

Hai công cụ thường dùng:

- **Elbow Method**;
- **Silhouette Score**.

Tuy nhiên, không nên chọn $K$ chỉ dựa trên một chỉ số toán học. Các segment còn phải:

- giải thích được;
- đủ lớn để sử dụng;
- ổn định;
- có ý nghĩa nghiệp vụ;
- dẫn tới hành động cụ thể.

---

### Bước 7. Đánh giá segmentation

Có thể đánh giá theo hai nhóm tiêu chí.

#### Tiêu chí kỹ thuật

- Within-cluster similarity;
- Between-cluster separation;
- Silhouette Score;
- Davies-Bouldin Index;
- độ ổn định khi thay đổi mẫu dữ liệu.

#### Tiêu chí nghiệp vụ

- **Interpretability:** có giải thích được từng segment không?
- **Actionability:** có thể triển khai hành động khác nhau cho từng nhóm không?
- **Measurability:** có đo lường được quy mô và đặc điểm của nhóm không?
- **Substantiality:** nhóm có đủ lớn hoặc đủ giá trị để quan tâm không?
- **Stability:** nhóm có tồn tại tương đối ổn định theo thời gian không?

Một clustering có Silhouette Score cao nhưng không có ý nghĩa nghiệp vụ vẫn có thể là một segmentation không hữu ích.

---

### Bước 8. Profiling và đặt tên các segment

Sau khi mô hình tạo cluster, cần tính các đặc trưng của từng cluster.

Ví dụ:

| Segment | Spending | Frequency | Recency | Diễn giải |
|---|---:|---:|---:|---|
| 0 | Cao | Cao | Thấp | Loyal High-Value |
| 1 | Thấp | Thấp | Cao | Inactive |
| 2 | Trung bình | Cao | Trung bình | Frequent Value Seekers |

Tên segment **không phải kết quả trực tiếp của thuật toán**. Tên được đặt sau khi phân tích đặc trưng của từng cluster.

---

### Bước 9. Sử dụng segment trong ra quyết định

Segmentation chỉ tạo ra giá trị khi được chuyển thành hành động.

Ví dụ:

```text
Segment              Hành động
------------------------------------------------
High Value            Loyalty / premium service
Price Sensitive       Coupon / promotion
Inactive              Reactivation campaign
New Customer          Onboarding
High Risk             Manual review / monitoring
```

---

### Bước 10. Theo dõi và cập nhật

Hành vi của khách hàng và môi trường kinh doanh thay đổi theo thời gian.

Do đó cần kiểm tra:

- tỷ trọng mỗi segment có thay đổi không;
- đặc trưng cluster có thay đổi không;
- khách hàng có chuyển từ segment này sang segment khác không;
- mô hình có cần huấn luyện lại không.

---

## 10. Ví dụ Python: Customer Segmentation bằng K-Means

Giả sử doanh nghiệp có dữ liệu khách hàng gồm:

- `annual_spending`: tổng chi tiêu hàng năm;
- `purchase_frequency`: số lần mua hàng trong năm;
- `recency`: số ngày kể từ lần mua gần nhất.

### 10.1. Tạo dữ liệu mẫu

```python
import pandas as pd

data = {
    "customer_id": range(1, 13),
    "annual_spending": [
        12, 15, 10, 14,
        70, 80, 75, 90,
        35, 40, 38, 42
    ],
    "purchase_frequency": [
        2, 3, 2, 4,
        15, 18, 16, 20,
        8, 9, 7, 10
    ],
    "recency": [
        90, 75, 120, 80,
        5, 8, 4, 6,
        30, 25, 40, 20
    ]
}

df = pd.DataFrame(data)
df
```

---

### 10.2. Chọn biến dùng để phân nhóm

```python
features = [
    "annual_spending",
    "purchase_frequency",
    "recency"
]

X = df[features]
```

Không sử dụng `customer_id` để clustering vì đây chỉ là biến định danh.

---

### 10.3. Chuẩn hóa dữ liệu

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Sau bước này, các biến được đưa về thang đo có thể so sánh được.

---

### 10.4. Huấn luyện K-Means

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)
```

Xem kết quả:

```python
df
```

---

### 10.5. Phân tích đặc điểm của các cluster

```python
cluster_profile = (
    df.groupby("cluster")[features]
      .mean()
      .round(2)
)

cluster_profile
```

Ta không nên chỉ nhìn vào số `cluster = 0`, `1`, `2`.

Cần trả lời:

- cluster nào chi tiêu cao?
- cluster nào mua thường xuyên?
- cluster nào lâu chưa quay lại?
- cluster nào có thể coi là khách hàng trung thành?
- cluster nào cần chương trình reactivation?

---

### 10.6. Đánh giá bằng Silhouette Score

```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X_scaled, df["cluster"])

print("Silhouette Score:", round(score, 3))
```

Silhouette Score nằm trong khoảng gần $[-1,1]$:

- gần $1$: các cluster tương đối tách biệt;
- gần $0$: các cluster chồng lấn;
- giá trị âm: nhiều quan sát có thể đã được gán vào cluster không phù hợp.

Không nên sử dụng Silhouette Score như tiêu chí duy nhất để chọn mô hình.

---

## 11. Chọn số cluster bằng Elbow Method

Có thể thử nhiều giá trị $K$ và quan sát `inertia`.

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertias = []

for k in range(2, 9):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    model.fit(X_scaled)
    inertias.append(model.inertia_)

plt.plot(range(2, 9), inertias, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()
```

Ta tìm vị trí mà việc tăng $K$ không còn làm giảm mạnh inertia. Vị trí đó thường được gọi là **elbow**.

Tuy nhiên:

> Elbow Method chỉ hỗ trợ lựa chọn $K$; quyết định cuối cùng cần kết hợp với khả năng diễn giải và mục tiêu nghiệp vụ.

---

## 12. Ứng dụng của Data Segmentation

### 12.1. Marketing và bán lẻ

Phân nhóm khách hàng theo:

- hành vi mua;
- giá trị đơn hàng;
- mức độ trung thành;
- phản ứng với khuyến mại;
- kênh mua hàng.

Ứng dụng:

- personalized promotion;
- customer retention;
- recommendation;
- loyalty program.

---

### 12.2. Tài chính – ngân hàng

Phân nhóm khách hàng theo:

- thu nhập;
- lịch sử tín dụng;
- dư nợ;
- hành vi giao dịch;
- mức độ rủi ro.

Ứng dụng:

- risk management;
- product recommendation;
- fraud monitoring;
- thiết kế sản phẩm tài chính.

---

### 12.3. Supply Chain và Logistics

Có thể phân nhóm:

**Khách hàng**

- theo nhu cầu;
- vị trí;
- mức độ ưu tiên;
- độ biến động đơn hàng.

**Sản phẩm**

- theo doanh số;
- tốc độ quay vòng;
- độ biến động nhu cầu;
- giá trị tồn kho.

**Nhà cung cấp**

- theo chi phí;
- lead time;
- reliability;
- quality.

**Đơn hàng**

- theo khối lượng;
- khoảng cách;
- thời gian giao;
- mức độ khẩn cấp.

Kết quả segmentation có thể hỗ trợ:

- chính sách tồn kho;
- thiết kế tuyến giao hàng;
- lựa chọn mức dịch vụ;
- phân bổ nguồn lực;
- quản trị nhà cung cấp.

---

### 12.4. Healthcare

Phân nhóm bệnh nhân theo:

- mức độ rủi ro;
- triệu chứng;
- lịch sử điều trị;
- đáp ứng với thuốc.

Segmentation có thể hỗ trợ cá nhân hóa chăm sóc và phân bổ nguồn lực y tế.

---

### 12.5. Text và Image Segmentation

Khái niệm segmentation còn xuất hiện ở những dạng dữ liệu khác.

**Text segmentation**

Chia văn bản thành:

- câu;
- đoạn;
- chủ đề;
- vùng nội dung.

**Image segmentation**

Chia ảnh thành các vùng hoặc đối tượng có ý nghĩa.

Ví dụ:

- đường;
- xe;
- người;
- tòa nhà;
- vùng tổn thương trong ảnh y khoa.

Cần lưu ý rằng **image segmentation** là một bài toán riêng trong Computer Vision và không hoàn toàn giống customer segmentation dựa trên clustering.

---

## 13. Lợi ích của Data Segmentation

Một quy trình segmentation tốt có thể mang lại:

1. **Hiểu dữ liệu tốt hơn**  
   Phát hiện các nhóm và mẫu hành vi khó quan sát khi xem toàn bộ dữ liệu.

2. **Cá nhân hóa**  
   Điều chỉnh sản phẩm, nội dung hoặc dịch vụ theo từng nhóm.

3. **Phân bổ nguồn lực hiệu quả**  
   Tập trung nguồn lực vào những segment quan trọng.

4. **Hỗ trợ dự báo và Machine Learning**  
   Có thể xây dựng mô hình riêng cho các nhóm có cấu trúc khác nhau.

5. **Quản trị rủi ro**  
   Phát hiện các nhóm có đặc điểm rủi ro cao.

6. **Hỗ trợ ra quyết định**  
   Biến dữ liệu thành các nhóm dễ hiểu và có thể hành động.

---

## 14. Những thách thức thường gặp

### 14.1. Chọn biến không phù hợp

Nếu sử dụng các biến không liên quan tới mục tiêu, cluster có thể tồn tại về mặt toán học nhưng không có ý nghĩa nghiệp vụ.

### 14.2. Không chuẩn hóa dữ liệu

Các biến có thang đo lớn có thể chi phối khoảng cách.

### 14.3. Chọn số cluster tùy ý

Không nên chọn $K=3$ chỉ vì muốn có ba nhóm “Low–Medium–High”.

### 14.4. Quá phụ thuộc vào chỉ số kỹ thuật

Một segmentation tốt cần vừa:

- hợp lý về mặt dữ liệu;
- vừa hữu ích về mặt nghiệp vụ.

### 14.5. Cluster không ổn định

Kết quả có thể thay đổi khi:

- dữ liệu thay đổi;
- khởi tạo thuật toán thay đổi;
- tập biến thay đổi.

### 14.6. Gán ý nghĩa quá mức cho cluster

Thuật toán chỉ phát hiện các nhóm dựa trên dữ liệu đầu vào.

Không nên tự động kết luận:

> “Cluster 2 là khách hàng trung thành”

nếu chưa phân tích đặc điểm của cluster đó.

### 14.7. Segmentation bị lỗi thời

Hành vi khách hàng có thể thay đổi. Segment cần được theo dõi và cập nhật.

### 14.8. Vấn đề đạo đức và fairness

Một segmentation có thể tạo ra quyết định bất lợi nếu sử dụng các thuộc tính nhạy cảm hoặc các biến đại diện gián tiếp cho chúng.

Do đó cần xem xét:

- mục đích sử dụng;
- quyền riêng tư;
- fairness;
- khả năng giải thích;
- tác động của quyết định lên các nhóm khác nhau.

---

## 15. Những lỗi thường gặp khi thực hiện Customer Segmentation

### Lỗi 1: Đưa `customer_id` vào K-Means

ID chỉ là mã định danh và khoảng cách giữa hai ID không có ý nghĩa nghiệp vụ.

### Lỗi 2: Chạy K-Means trực tiếp trên dữ liệu chưa scale

Điều này có thể khiến biến có giá trị lớn nhất quyết định gần như toàn bộ kết quả.

### Lỗi 3: Chỉ chạy một giá trị $K$

Nên thử nhiều $K$ và so sánh kết quả.

### Lỗi 4: Chỉ báo cáo cluster number

Báo cáo:

```text
Customer A -> Cluster 0
Customer B -> Cluster 2
```

chưa đủ.

Cần bổ sung **cluster profiling**.

### Lỗi 5: Có cluster nhưng không có hành động

Segmentation không tạo ra giá trị nếu doanh nghiệp không biết sẽ làm gì khác nhau với từng nhóm.

---

## 16. Quy trình Data Segmentation trong một dự án Data Science

Một quy trình thực tế có thể được tóm tắt:

```text
1. Business Problem
        |
        v
2. Define Unit of Analysis
        |
        v
3. Select / Engineer Features
        |
        v
4. Clean and Scale Data
        |
        v
5. Select Segmentation Method
        |
        v
6. Train / Create Segments
        |
        v
7. Evaluate Segments
        |
        v
8. Profile and Interpret
        |
        v
9. Define Business Actions
        |
        v
10. Monitor and Update
```

Segmentation vì vậy không chỉ là thao tác chạy một thuật toán clustering mà là một **quy trình phân tích hoàn chỉnh**.

---

## 17. Ví dụ tình huống kinh doanh

### Tình huống

Một sàn thương mại điện tử có dữ liệu của 50.000 khách hàng.

Các biến gồm:

- `orders_12m`: số đơn trong 12 tháng;
- `revenue_12m`: doanh thu;
- `days_since_last_order`: số ngày từ đơn gần nhất;
- `discount_ratio`: tỷ lệ đơn có sử dụng khuyến mại;
- `return_ratio`: tỷ lệ trả hàng.

### Câu hỏi

Doanh nghiệp muốn thiết kế chương trình chăm sóc khách hàng khác nhau.

### Hướng tiếp cận

**Bước 1:** Xác định khách hàng là đơn vị phân tích.

**Bước 2:** Kiểm tra missing values và outliers.

**Bước 3:** Chuẩn hóa các biến.

**Bước 4:** Thử K-Means với $K = 2,3,\ldots,8$.

**Bước 5:** So sánh Elbow và Silhouette Score.

**Bước 6:** Phân tích trung bình của các biến trong từng cluster.

Giả sử thu được:

| Segment | Orders | Revenue | Recency | Discount Ratio | Diễn giải |
|---|---:|---:|---:|---:|---|
| A | Cao | Cao | Thấp | Thấp | Loyal High Value |
| B | Cao | Trung bình | Thấp | Cao | Promotion Driven |
| C | Thấp | Thấp | Cao | Trung bình | Inactive |
| D | Thấp | Trung bình | Thấp | Thấp | New / Potential |

**Bước 7:** Thiết kế chính sách:

- A: loyalty và premium service;
- B: tối ưu khuyến mại;
- C: reactivation campaign;
- D: onboarding và cross-selling.

---

## 18. Tự kiểm tra

### Câu 1

Data Segmentation khác Data Partitioning như thế nào?

### Câu 2

Tại sao cần chuẩn hóa dữ liệu trước khi sử dụng K-Means?

### Câu 3

Trong customer segmentation không có nhãn có sẵn, bài toán thuộc:

A. Supervised Learning  
B. Unsupervised Learning  
C. Reinforcement Learning  
D. Time Series Forecasting

### Câu 4

Thuật toán nào sau đây yêu cầu xác định số cluster $K$ trước khi chạy trong cách sử dụng cơ bản?

A. K-Means  
B. DBSCAN  
C. Cả hai luôn luôn yêu cầu $K$  
D. Không thuật toán nào

### Câu 5

Vì sao không nên sử dụng `customer_id` như một biến đầu vào cho K-Means?

### Câu 6

Silhouette Score cao có đảm bảo segmentation hữu ích trong kinh doanh không? Giải thích.

### Câu 7

Sau khi K-Means tạo `cluster = 0, 1, 2`, bước quan trọng tiếp theo là gì?

### Câu 8

Segmentation và targeting khác nhau như thế nào?

---

## 19. Bài tập thực hành

### Bài tập 1. Segmentation theo quy tắc

Cho DataFrame gồm:

```python
import pandas as pd

df = pd.DataFrame({
    "customer": ["A", "B", "C", "D", "E"],
    "annual_spending": [8, 25, 55, 72, 18]
})
```

Hãy tạo biến `segment` theo quy tắc:

- `< 20`: `Low Value`;
- từ `20` đến dưới `50`: `Medium Value`;
- `>= 50`: `High Value`.

---

### Bài tập 2. Chuẩn hóa dữ liệu

Cho hai biến:

```python
annual_spending = [10, 20, 50, 80, 100]
purchase_frequency = [1, 2, 5, 8, 10]
```

Hãy:

1. tạo DataFrame;
2. sử dụng `StandardScaler`;
3. so sánh dữ liệu trước và sau khi chuẩn hóa.

---

### Bài tập 3. Customer Segmentation bằng K-Means

Sử dụng một tập dữ liệu khách hàng gồm các biến:

- annual spending;
- purchase frequency;
- recency.

Yêu cầu:

1. kiểm tra dữ liệu;
2. chọn feature;
3. scale dữ liệu;
4. thử $K=2,3,4,5$;
5. tính Silhouette Score;
6. chọn một giá trị $K$;
7. tạo cluster;
8. lập bảng profiling;
9. đặt tên cho từng segment;
10. đề xuất một hành động kinh doanh cho mỗi segment.

---

### Bài tập 4. Segmentation trong Supply Chain

Một doanh nghiệp có dữ liệu 1.000 SKU:

- annual demand;
- demand variability;
- unit value;
- lead time;
- stockout frequency.

Hãy đề xuất:

1. mục tiêu segmentation;
2. các biến nên sử dụng;
3. thuật toán phù hợp;
4. cách đánh giá cluster;
5. chính sách tồn kho có thể áp dụng cho từng nhóm.

---

## 20. Tóm tắt

Data Segmentation là quá trình chia dữ liệu thành các nhóm có ý nghĩa để hỗ trợ phân tích và ra quyết định.

Các ý chính:

- Segmentation không giống train/validation/test partitioning.
- Trong dữ liệu bảng và phân tích khách hàng, segmentation thường gắn với clustering.
- Có thể thực hiện segmentation bằng quy tắc, supervised learning, unsupervised learning hoặc semi-supervised learning.
- K-Means là phương pháp phổ biến nhưng không phải lựa chọn duy nhất.
- Chuẩn hóa dữ liệu và lựa chọn feature có ảnh hưởng lớn đến kết quả.
- Không nên đánh giá segmentation chỉ bằng metric kỹ thuật.
- Kết quả cần được profiling, diễn giải và gắn với hành động nghiệp vụ.
- Segment cần được theo dõi và cập nhật khi dữ liệu thay đổi.

---

## Tài liệu tham khảo

1. GeeksforGeeks. **What is Data Segmentation in Machine Learning?** Updated 23 July 2025.  
   https://www.geeksforgeeks.org/machine-learning/what-is-data-segmentation-in-machine-learning/

2. Shmueli, G., Bruce, P. C., Deokar, A. V., & Patel, N. R. (2023).  
   *Machine Learning for Business Analytics: Concepts, Techniques and Applications in RapidMiner*. Wiley.  
   Đặc biệt: Chapter 16 — Cluster Analysis.

