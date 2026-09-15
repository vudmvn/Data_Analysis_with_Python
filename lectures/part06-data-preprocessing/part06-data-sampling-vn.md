# Giới thiệu về Lấy mẫu dữ liệu (Introduction to Data Sampling)

## Tóm tắt bài học

**Data Sampling** là phương pháp thống kê dùng để chọn một tập con đại diện (**sample**) từ một tập dữ liệu hoặc tổng thể lớn hơn (**population**). Thay vì phân tích toàn bộ dữ liệu, nhà phân tích nghiên cứu sample và sử dụng kết quả để đưa ra nhận định hoặc kết luận về population.

Sampling đặc biệt hữu ích khi:

- dataset rất lớn;
- việc thu thập toàn bộ dữ liệu tốn nhiều thời gian;
- chi phí phân tích toàn bộ population quá cao;
- hoặc việc nghiên cứu toàn bộ population là không khả thi.

Bài học tập trung vào:

1. khái niệm population và sample;
2. quy trình Data Sampling;
3. Probability Sampling;
4. Non-Probability Sampling;
5. các yếu tố liên quan đến sample size;
6. các điều kiện để sampling hiệu quả;
7. ưu điểm và hạn chế của sampling.

---

# 1. Mục tiêu bài học

Sau bài học này, người học có thể:

- Giải thích được Data Sampling là gì.
- Phân biệt population và sample.
- Giải thích được vì sao sampling cần thiết trong Data Science.
- Mô tả các bước chính của Data Sampling.
- Phân biệt Probability Sampling và Non-Probability Sampling.
- Nhận biết Simple Random, Systematic, Stratified và Cluster Sampling.
- Nhận biết Convenience, Voluntary Response, Purposive và Snowball Sampling.
- Giải thích các yếu tố ảnh hưởng đến sample size.
- Nhận diện nguy cơ bias do sampling không phù hợp.
- Áp dụng một số cách lấy mẫu cơ bản bằng Python.

---

# 2. Data Sampling là gì?

Data Sampling là quá trình chọn một tập con từ population.

Có thể hình dung:

```text
Population
│
│  rất lớn
│
├── Data Point 1
├── Data Point 2
├── Data Point 3
├── ...
└── Data Point N
        ↓
   Sampling Method
        ↓
      Sample
        ↓
     Analysis
        ↓
Inference about Population
```

Ví dụ:

```text
Population:
100,000 khách hàng

Sample:
1,000 khách hàng
```

Nhà phân tích nghiên cứu 1,000 khách hàng để suy luận về toàn bộ 100,000 khách hàng.

---

# 3. Population và Sample

## Population

Population là toàn bộ tập hợp các đối tượng hoặc quan sát mà nghiên cứu quan tâm.

Ví dụ:

```text
Toàn bộ sinh viên của một trường đại học
Toàn bộ khách hàng của một ngân hàng
Toàn bộ giao dịch trong năm
```

---

## Sample

Sample là một phần của population được chọn để phân tích.

Ví dụ:

```text
500 sinh viên
1,000 khách hàng
10,000 giao dịch
```

Mục tiêu quan trọng là sample phải phản ánh population đủ tốt cho mục đích phân tích.

---

# 4. Vì sao Data Sampling quan trọng?

Nguồn bài học nêu bốn lý do chính.

## 4.1. Cost and Time Efficient

Phân tích toàn bộ dataset có thể:

- tốn nhiều thời gian;
- tốn tài nguyên tính toán;
- tăng chi phí xử lý.

Sampling giúp phân tích một phần dữ liệu thay vì toàn bộ population.

---

## 4.2. Feasible for Large Populations

Trong nhiều trường hợp, việc nghiên cứu toàn bộ population là:

```text
too expensive
or
impractical
```

Sampling tạo ra một tập dữ liệu nhỏ hơn và dễ quản lý hơn.

---

## 4.3. Reduces Risk of Error

Theo nguồn, sampling đúng phương pháp có thể giúp:

- hạn chế bias;
- giảm ảnh hưởng không mong muốn của một số quan sát cực đoan;
- tạo quy trình phân tích có kiểm soát hơn.

---

## 4.4. Maintains Accuracy

Một sample được lựa chọn tốt có thể phản ánh population đủ chính xác để phục vụ:

- thống kê;
- nghiên cứu;
- kiểm thử;
- phân tích dữ liệu.

---

# 5. Ví dụ thực tế

Giả sử doanh nghiệp có:

```text
5,000,000 giao dịch
```

Nếu mục tiêu chỉ là kiểm tra sơ bộ:

```text
phân phối doanh thu
tỷ lệ hoàn đơn
giá trị đơn hàng trung bình
```

ta có thể lấy một sample:

```text
50,000 giao dịch
```

thay vì xử lý toàn bộ 5 triệu giao dịch trong giai đoạn khám phá ban đầu.

---

# 6. Quy trình Data Sampling

Nguồn trình bày sáu bước:

```text
1. Identify the Target Dataset
2. Determine Sample Size
3. Choose a Sampling Method
4. Collect the Sample
5. Analyze the Sample
6. Generalize to the Population
```

---

# 7. Bước 1 — Xác định Target Dataset

Trước tiên cần xác định:

```text
Population là gì?
```

Ví dụ:

```text
Tất cả khách hàng mua hàng trong năm 2026
```

hoặc:

```text
Tất cả đơn giao hàng tại Hà Nội trong quý III
```

Nếu target population được định nghĩa không rõ, sample có thể không phục vụ đúng câu hỏi nghiên cứu.

---

# 8. Bước 2 — Xác định Sample Size

Sample size là:

```text
số lượng observations trong sample
```

Ví dụ:

```text
Population = 50,000 khách hàng
Sample Size = 1,000 khách hàng
```

Sample quá nhỏ có thể không phản ánh được population.

Sample quá lớn có thể làm mất lợi ích về thời gian và chi phí.

---

# 9. Bước 3 — Chọn Sampling Method

Nguồn đề cập nhiều phương pháp như:

```text
Random Sampling
Systematic Sampling
Stratified Sampling
Cluster Sampling
Snowball Sampling
```

Phương pháp phù hợp phụ thuộc vào:

- mục tiêu nghiên cứu;
- đặc điểm dữ liệu;
- khả năng tiếp cận population.

---

# 10. Bước 4 — Thu thập Sample

Sau khi chọn phương pháp, cần thực hiện việc lấy mẫu theo đúng quy tắc.

Ví dụ:

```text
Random Sampling
→ random select records

Systematic Sampling
→ select every kth record
```

---

# 11. Bước 5 — Phân tích Sample

Sau khi có sample:

```text
Descriptive Statistics
Visualization
Statistical Analysis
Machine Learning
```

có thể được áp dụng.

Ví dụ:

```python
sample.describe()
```

---

# 12. Bước 6 — Suy luận cho Population

Mục tiêu cuối cùng là dùng kết quả từ sample để:

```text
draw conclusions
or
make predictions
```

cho population.

Điều này chỉ đáng tin cậy khi sample được lựa chọn phù hợp.

---

# 13. Hai nhóm Sampling chính

Nguồn chia Data Sampling thành:

```text
1. Probability Sampling
2. Non-Probability Sampling
```

Điểm khác biệt chính nằm ở cách observations được chọn.

---

# 14. Probability Sampling

Trong Probability Sampling:

> Mỗi data point có một xác suất được chọn **biết trước và khác 0**.

Mục tiêu là tạo sample có khả năng đại diện tốt cho population.

Nguồn trình bày bốn phương pháp:

```text
Simple Random Sampling
Systematic Sampling
Stratified Sampling
Cluster Sampling
```

---

# 15. Simple Random Sampling

Trong Simple Random Sampling:

```text
mỗi data point
→ có cơ hội được chọn như nhau
```

Ví dụ nguồn sử dụng hình ảnh:

```text
tung đồng xu
→ head hoặc tail có xác suất ngang nhau
```

Trong dataset:

```text
Population = 10,000 rows
Sample = random 500 rows
```

---

# 16. Simple Random Sampling bằng Pandas

Ví dụ minh họa bổ sung bằng Python:

```python
sample = df.sample(
    n=500,
    random_state=42
)
```

Hoặc lấy 10% dữ liệu:

```python
sample = df.sample(
    frac=0.10,
    random_state=42
)
```

`random_state` giúp tái lập kết quả.

---

# 17. Ưu điểm của Simple Random Sampling

- dễ hiểu;
- dễ triển khai;
- tránh việc người nghiên cứu chủ động chọn observations;
- phù hợp khi population tương đối đồng nhất.

---

# 18. Hạn chế của Simple Random Sampling

Nếu population có các nhóm rất khác nhau, sample ngẫu nhiên có thể:

```text
không chứa đủ observations
của một số nhóm nhỏ
```

Ví dụ:

```text
Region A = 90%
Region B = 9%
Region C = 1%
```

Một random sample nhỏ có thể chứa rất ít observations từ Region C.

---

# 19. Systematic Sampling

Systematic Sampling chọn observations theo khoảng cách đều trên một danh sách đã sắp xếp.

Ví dụ nguồn:

```text
10 records
→ chọn mỗi record thứ 2

2, 4, 6, 8, 10
```

---

# 20. Ý tưởng của Systematic Sampling

Nếu:

```text
Population size = N
Sample size = n
```

ta có thể sử dụng khoảng:

```text
k ≈ N / n
```

Sau đó chọn observations theo bước nhảy `k`.

---

# 21. Systematic Sampling bằng Python

Ví dụ minh họa:

```python
k = 10

systematic_sample = df.iloc[
    ::k
]
```

Lệnh trên lấy:

```text
row 0
row 10
row 20
row 30
...
```

---

# 22. Lưu ý với Systematic Sampling

Nếu dữ liệu có pattern tuần hoàn trùng với khoảng `k`, sample có thể bị bias.

Ví dụ:

```text
mỗi record thứ 10
```

nhưng dataset cũng có một cấu trúc lặp lại theo chu kỳ 10 records.

---

# 23. Stratified Sampling

Stratified Sampling chia population thành các nhóm gọi là:

```text
strata
```

dựa trên một đặc điểm chung.

Sau đó sample được chọn từ **mỗi stratum**.

Ví dụ nguồn:

```text
Employees
→ Male
→ Female
→ sample từ từng nhóm
```

---

# 24. Vì sao dùng Stratified Sampling?

Stratified Sampling phù hợp khi:

```text
Population có các nhóm quan trọng
và cần bảo đảm mỗi nhóm xuất hiện trong sample
```

Ví dụ:

```text
Customer Segment
Region
Gender
Product Category
```

---

# 25. Ví dụ Stratified Sampling

Population:

```text
North   50%
Central 20%
South   30%
```

Nếu sample có 1,000 observations, proportional stratified sample có thể gồm:

```text
North   500
Central 200
South   300
```

---

# 26. Stratified Sampling bằng scikit-learn

Ví dụ minh họa:

```python
from sklearn.model_selection import train_test_split

sample, _ = train_test_split(
    df,
    train_size=0.20,
    stratify=df["Region"],
    random_state=42
)
```

Mục tiêu:

```text
giữ tỷ lệ Region
gần với dataset gốc
```

---

# 27. Cluster Sampling

Cluster Sampling chia population thành các clusters.

Sau đó:

```text
chọn ngẫu nhiên một số clusters
```

và nghiên cứu toàn bộ hoặc một phần observations bên trong các clusters đã chọn.

Ví dụ nguồn:

```text
chọn ngẫu nhiên các nhóm người dùng
từ các mobile networks
```

---

# 28. Ví dụ Cluster Sampling

Giả sử:

```text
Population = học sinh toàn thành phố
```

Thay vì random từng học sinh:

```text
1. xem mỗi trường là một cluster
2. chọn ngẫu nhiên một số trường
3. khảo sát học sinh trong các trường đó
```

---

# 29. So sánh Stratified và Cluster Sampling

Hai phương pháp đều sử dụng groups nhưng mục tiêu khác nhau.

```text
Stratified:
lấy sample từ tất cả strata

Cluster:
chọn một số clusters rồi lấy sample trong clusters đó
```

Ví dụ:

```text
Stratified:
North + Central + South đều xuất hiện

Cluster:
chỉ chọn một số chi nhánh / khu vực
```

---

# 30. Probability Sampling — Tóm tắt

| Phương pháp | Ý tưởng chính |
|---|---|
| Simple Random | Chọn ngẫu nhiên observations |
| Systematic | Chọn mỗi observation thứ k |
| Stratified | Chia strata và lấy sample từ từng strata |
| Cluster | Chọn một số clusters |

---

# 31. Non-Probability Sampling

Trong Non-Probability Sampling:

```text
selection is not random
```

Người nghiên cứu hoặc participants ảnh hưởng trực tiếp đến việc ai được đưa vào sample.

Nguồn trình bày:

```text
Convenience Sampling
Voluntary Response Sampling
Purposive Sampling
Snowball Sampling
```

---

# 32. Convenience Sampling

Convenience Sampling chọn dữ liệu dựa trên:

```text
ease of access
```

Ví dụ nguồn:

```text
chọn dữ liệu tuyển dụng IT
gần đây và dễ tiếp cận nhất
```

Ưu điểm:

- nhanh;
- dễ;
- chi phí thấp.

Nhược điểm:

- dễ bị bias;
- có thể không đại diện population.

---

# 33. Voluntary Response Sampling

Participants tự quyết định có tham gia hay không.

Ví dụ nguồn:

```text
khảo sát nhóm máu
→ chỉ những người tự nguyện trả lời
```

Vấn đề:

```text
người phản hồi
có thể khác
người không phản hồi
```

nên sample có thể bị self-selection bias.

---

# 34. Purposive Sampling

Purposive Sampling chọn observations theo một mục đích cụ thể.

Ví dụ nguồn:

```text
khảo sát các khu vực nông thôn
để nghiên cứu nhu cầu giáo dục
```

Người nghiên cứu chủ động chọn sample có đặc điểm cần thiết.

---

# 35. Snowball Sampling

Snowball Sampling để participants hiện tại giới thiệu thêm participants khác.

Ví dụ nguồn:

```text
một người dân trong khu ổ chuột
→ giới thiệu người tiếp theo
→ sample tăng dần
```

Phương pháp này hữu ích khi population:

```text
khó tiếp cận
khó xác định danh sách đầy đủ
```

---

# 36. Non-Probability Sampling — Tóm tắt

| Phương pháp | Cách chọn |
|---|---|
| Convenience | Dễ tiếp cận |
| Voluntary Response | Người tham gia tự nguyện |
| Purposive | Chọn theo mục đích |
| Snowball | Người tham gia giới thiệu thêm người khác |

---

# 37. Probability vs Non-Probability Sampling

| Nội dung | Probability | Non-Probability |
|---|---|---|
| Random selection | Có | Không bắt buộc |
| Selection probability | Biết trước | Thường không biết |
| Generalization | Tốt hơn khi thiết kế đúng | Hạn chế hơn |
| Bias risk | Thường thấp hơn | Có thể cao hơn |
| Chi phí | Có thể cao | Thường thấp hơn |

---

# 38. Sample Size là gì?

Sample size là:

```text
số lượng observations
được chọn từ population
```

Ví dụ:

```text
Population = 100,000
Sample Size = 1,500
```

Sample size ảnh hưởng tới mức độ sample phản ánh population.

---

# 39. Các bước xác định Sample Size

Nguồn nêu bốn yếu tố/bước:

1. Xác định population size.
2. Xác định confidence level.
3. Xác định margin of error.
4. Xem xét standard deviation.

---

# 40. Population Size

Population size là:

```text
tổng số observations
trong population
```

Ví dụ:

```text
N = 50,000 customers
```

---

# 41. Confidence Level

Confidence level biểu diễn mức độ tin cậy mong muốn của kết quả suy luận.

Nguồn nhấn mạnh rằng đây là một yếu tố quan trọng khi xác định sample size.

---

# 42. Margin of Error

Margin of error thể hiện:

```text
mức sai số chấp nhận được
```

Trong thiết kế sampling, margin nhỏ hơn thường đòi hỏi sample lớn hơn.

---

# 43. Standard Deviation

Standard deviation phản ánh mức độ phân tán của dữ liệu.

Dữ liệu biến động lớn thường yêu cầu nhiều observations hơn để sample phản ánh population ổn định.

---

# 44. Quan hệ khái quát về Sample Size

Có thể ghi nhớ:

```text
Confidence cao hơn
→ thường cần sample lớn hơn

Margin of error nhỏ hơn
→ thường cần sample lớn hơn

Variability lớn hơn
→ thường cần sample lớn hơn
```

Nguồn không cung cấp một công thức sample-size cụ thể trong phần này.

---

# 45. Effective Data Sampling

Nguồn đưa ra bốn yếu tố cần quan tâm:

```text
Statistical Regularity
Data Accuracy
Stratification Clarity
Sufficient Sample Size
```

---

# 46. Statistical Regularity

Theo nguồn, dataset đủ lớn giúp sampling ổn định hơn và tăng khả năng sample phản ánh population.

Điểm quan trọng là sample cần được chọn theo một quy trình nhất quán.

---

# 47. Data Accuracy

Sampling không thể sửa một dataset gốc bị sai.

Nếu population data chứa:

```text
wrong records
duplicate data
incorrect values
```

sample vẫn có thể chứa các lỗi đó.

Do đó:

```text
Data Quality
→ trước
Sampling
```

là một nguyên tắc quan trọng.

---

# 48. Stratification Clarity

Khi dùng Stratified Sampling, cần xác định strata rõ ràng.

Ví dụ:

```text
Region
North
Central
South
```

Các groups phải có ý nghĩa trong mục tiêu nghiên cứu.

---

# 49. Sufficient Sample Size

Sample quá nhỏ có thể:

- không ổn định;
- bỏ sót subgroups;
- dẫn đến kết luận sai.

Do đó cần chọn sample size đủ lớn cho mục tiêu phân tích.

---

# 50. Sampling Bias

Sampling bias xảy ra khi sample không đại diện tốt cho population.

Ví dụ:

```text
Population:
tất cả khách hàng

Sample:
chỉ khách hàng mua online
```

Nếu dùng sample trên để kết luận cho toàn bộ khách hàng, kết quả có thể bị bias.

---

# 51. Ví dụ Sampling Bias

Giả sử khảo sát mức hài lòng bằng:

```text
online survey
```

nhưng nhóm khách hàng lớn tuổi ít sử dụng internet.

Sample có thể chứa quá ít khách hàng lớn tuổi.

Khi đó:

```text
sample distribution
≠
population distribution
```

---

# 52. Sampling trong Machine Learning

Sampling cũng được sử dụng trong Machine Learning để:

- tạo tập training nhỏ hơn;
- tạo validation subset;
- kiểm tra nhanh mô hình;
- xử lý datasets rất lớn.

Ví dụ:

```python
df_small = df.sample(
    frac=0.20,
    random_state=42
)
```

---

# 53. Sampling và Train/Test Split

Train/test split cũng là một dạng chia dữ liệu.

Ví dụ:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )
)
```

Nếu target không cân bằng, có thể dùng:

```python
stratify=y
```

để giữ tỷ lệ các classes.

---

# 54. Ví dụ Stratified Train/Test Split

```python
X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=42
    )
)
```

Điều này giúp:

```text
class distribution in train
≈
class distribution in test
```

---

# 55. Ví dụ kinh doanh — Khảo sát khách hàng

Population:

```text
100,000 khách hàng
```

Các vùng:

```text
North   45%
Central 20%
South   35%
```

Nếu muốn khảo sát:

```text
customer satisfaction
```

Stratified Sampling có thể giúp sample giữ được cơ cấu vùng.

---

# 56. Ví dụ kinh doanh — Kiểm toán giao dịch

Population:

```text
2,000,000 transactions
```

Nếu kiểm tra thủ công toàn bộ là không khả thi.

Có thể chọn:

```text
random sample
```

hoặc:

```text
stratified sample
```

theo:

```text
transaction value
branch
risk category
```

tùy mục tiêu kiểm tra.

---

# 57. Ví dụ Supply Chain

Population:

```text
tất cả deliveries trong năm
```

Có thể stratify theo:

```text
Region
Carrier
Product Type
Delivery Priority
```

để sample chứa đủ các nhóm quan trọng.

---

# 58. Ưu điểm của Data Sampling

Nguồn nêu các ưu điểm:

- phân tích nhanh hơn;
- hỗ trợ ra quyết định nhanh hơn;
- giảm computational effort;
- giảm chi phí thu thập và xử lý;
- vẫn có thể tạo kết quả đáng tin cậy nếu phương pháp phù hợp.

---

# 59. Hạn chế của Data Sampling

Nguồn nêu các hạn chế:

- sample có thể khác population;
- cluster sampling có thể phức tạp;
- sampling thiết kế kém làm giảm accuracy;
- sample nhỏ hoặc biased có thể dẫn đến kết luận sai.

---

# 60. Những sai lầm phổ biến khi Sampling

## 60.1. Sample quá nhỏ

Có thể không phản ánh population.

---

## 60.2. Chỉ lấy dữ liệu dễ tiếp cận

Có thể tạo convenience bias.

---

## 60.3. Bỏ qua các nhóm nhỏ

Ví dụ:

```text
minority customer segments
```

có thể không xuất hiện đủ trong random sample nhỏ.

---

## 60.4. Chọn phương pháp không phù hợp

Ví dụ:

```text
population có nhiều strata quan trọng
```

nhưng chỉ sử dụng random sample rất nhỏ.

---

## 60.5. Generalize quá mức

Không nên suy luận mạnh cho population nếu sample:

- biased;
- quá nhỏ;
- hoặc không đúng target population.

---

# 61. Quy trình Sampling đề xuất

```text
1. Define Population
2. Define Analysis Goal
3. Check Data Quality
4. Determine Sample Size
5. Choose Sampling Method
6. Draw Sample
7. Check Sample Distribution
8. Analyze Sample
9. Generalize Carefully
10. Document Sampling Design
```

---

# 62. Kiểm tra Sample sau khi lấy

Sau khi sampling, nên so sánh sample và population.

Ví dụ:

```python
df["Region"].value_counts(
    normalize=True
)
```

và:

```python
sample["Region"].value_counts(
    normalize=True
)
```

So sánh:

```text
Population Distribution
vs
Sample Distribution
```

---

# 63. So sánh Mean

Ví dụ:

```python
print(
    df["Revenue"].mean()
)

print(
    sample["Revenue"].mean()
)
```

Sample không cần giống population hoàn toàn, nhưng sự khác biệt lớn có thể là tín hiệu cần kiểm tra.

---

# 64. Bài tập thực hành 1 — Simple Random Sampling

Cho DataFrame `df` gồm 10,000 observations.

Yêu cầu:

1. Lấy random sample 500 rows.
2. Dùng `random_state=42`.
3. Kiểm tra `shape`.
4. So sánh mean của `Revenue` giữa sample và population.

Gợi ý:

```python
sample = df.________(
    n=________,
    random_state=42
)
```

---

# 65. Bài tập thực hành 2 — Systematic Sampling

Cho dataset 1,000 rows.

Yêu cầu:

1. Chọn mỗi observation thứ 10.
2. Lưu vào `systematic_sample`.
3. Kiểm tra sample size.

Gợi ý:

```python
systematic_sample = df.iloc[
    ________
]
```

---

# 66. Bài tập thực hành 3 — Stratified Sampling

Dataset có cột:

```text
Region
```

với:

```text
North
Central
South
```

Yêu cầu:

1. Tính tỷ lệ Region trong population.
2. Lấy sample 20%.
3. Giữ tỷ lệ Region.
4. So sánh distribution.

---

# 67. Bài tập thực hành 4 — Sampling Bias

Giả sử population gồm:

```text
Young customers    60%
Older customers    40%
```

Nhưng sample gồm:

```text
Young customers    90%
Older customers    10%
```

Câu hỏi:

1. Sample có đại diện population không?
2. Kết luận về hành vi khách hàng có thể bị ảnh hưởng như thế nào?
3. Phương pháp sampling nào có thể cải thiện tình huống?

---

# 68. Bài tập thực hành 5 — Chọn Sampling Method

Chọn phương pháp phù hợp cho từng tình huống:

### Trường hợp A

Muốn mọi customer có cơ hội được chọn như nhau.

### Trường hợp B

Muốn mỗi region đều được đại diện đúng tỷ lệ.

### Trường hợp C

Không có danh sách population đầy đủ và participants giới thiệu người tiếp theo.

### Trường hợp D

Chọn mỗi transaction thứ 100 trong database.

### Trường hợp E

Chọn những respondents dễ tiếp cận nhất.

---

# 69. Tự kiểm tra

### Câu 1

Data Sampling là gì?

A. Xóa dữ liệu  
B. Chọn một tập con đại diện từ population  
C. Scaling dữ liệu  
D. Encoding dữ liệu

---

### Câu 2

Probability Sampling có đặc điểm gì?

A. Mỗi observation có probability được chọn biết trước và khác 0  
B. Chỉ chọn observations dễ tiếp cận  
C. Không dùng random selection  
D. Chỉ dùng cho dữ liệu nhỏ

---

### Câu 3

Phương pháp nào chọn observations theo khoảng đều?

A. Stratified  
B. Systematic  
C. Snowball  
D. Purposive

---

### Câu 4

Phương pháp nào chia population thành strata?

A. Stratified Sampling  
B. Cluster Sampling  
C. Convenience Sampling  
D. Snowball Sampling

---

### Câu 5

Snowball Sampling hoạt động như thế nào?

---

### Câu 6

Convenience Sampling có rủi ro chính gì?

---

### Câu 7

Sample size chịu ảnh hưởng bởi những yếu tố nào theo nguồn?

---

### Câu 8

Tại sao cần kiểm tra data quality trước khi sampling?

---

### Câu 9

Stratified Sampling và Cluster Sampling khác nhau như thế nào?

---

### Câu 10

Tại sao một sample biased có thể dẫn đến kết luận sai?

---

# 70. Bài tập tổng hợp — Sampling dữ liệu khách hàng

Cho file:

```text
customers.csv
```

gồm:

```text
Customer_ID
Age
Region
Customer_Type
Annual_Spending
Churn
```

Yêu cầu:

1. Đọc dữ liệu.
2. Kiểm tra kích thước population.
3. Kiểm tra missing values.
4. Kiểm tra phân phối `Region`.
5. Kiểm tra phân phối `Customer_Type`.
6. Lấy Simple Random Sample 10%.
7. Lấy Systematic Sample.
8. Lấy Stratified Sample theo `Region`.
9. So sánh:
   - sample size;
   - mean Annual_Spending;
   - tỷ lệ Region;
   - tỷ lệ Churn.
10. Nhận xét phương pháp nào giữ cấu trúc population tốt nhất trong trường hợp này.
11. Giải thích liệu kết quả từ sample có thể generalize cho population hay không.

---

# 71. Yêu cầu báo cáo

Người học cần trình bày:

## Phần 1 — Population

Ví dụ:

```text
Population size: 50,000
```

---

## Phần 2 — Sampling Design

Ví dụ:

```text
Method: Stratified Sampling
Stratification Variable: Region
Sample Size: 5,000
```

---

## Phần 3 — Sample vs Population

So sánh:

```text
Region Distribution
Mean Spending
Churn Rate
```

---

## Phần 4 — Nhận xét

Trả lời:

```text
Sample có đại diện population không?
Có dấu hiệu sampling bias không?
Có thể generalize kết quả không?
```

---

# 72. Checklist Data Sampling

```text
□ Tôi đã xác định target population chưa?
□ Tôi đã kiểm tra data quality chưa?
□ Tôi đã xác định sample size chưa?
□ Tôi đã chọn sampling method phù hợp chưa?
□ Tôi có cần probability sampling không?
□ Population có strata quan trọng không?
□ Tôi đã kiểm tra sample distribution chưa?
□ Sample có dấu hiệu bias không?
□ Sample size có đủ lớn không?
□ Tôi có đang generalize vượt quá dữ liệu không?
□ Tôi đã ghi lại sampling design chưa?
```

---

# 73. Tóm tắt bài học

Các điểm cần ghi nhớ:

- **Data Sampling** là quá trình chọn một sample từ population.
- Sampling giúp:
  - giảm chi phí;
  - giảm thời gian;
  - giảm computational effort;
  - giúp phân tích population lớn trở nên khả thi.
- Quy trình sampling gồm:
  - xác định target dataset;
  - sample size;
  - sampling method;
  - collect sample;
  - analyze;
  - generalize.
- Hai nhóm chính là:
  - Probability Sampling;
  - Non-Probability Sampling.
- Probability Sampling gồm:
  - Simple Random;
  - Systematic;
  - Stratified;
  - Cluster.
- Non-Probability Sampling gồm:
  - Convenience;
  - Voluntary Response;
  - Purposive;
  - Snowball.
- Sample size phụ thuộc vào các yếu tố như:
  - population size;
  - confidence level;
  - margin of error;
  - variability.
- Sampling tốt cần:
  - data quality;
  - strata rõ ràng;
  - sample size phù hợp;
  - sampling design phù hợp.
- Sample không đại diện có thể tạo sampling bias và dẫn tới kết luận sai.

---

## Tài liệu tham khảo

GeeksforGeeks. *Introduction to Data Sampling*. Last Updated: 28 Apr, 2026.

---

## Ghi chú về ví dụ Python

Các ví dụ Python trong bài được bổ sung để minh họa cách triển khai các khái niệm sampling trong thực hành. Nội dung khái niệm và phân loại sampling bám theo nguồn GeeksforGeeks được cung cấp.
