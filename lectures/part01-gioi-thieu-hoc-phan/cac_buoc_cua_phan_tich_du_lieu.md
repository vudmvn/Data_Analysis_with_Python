# Sáu bước trong quy trình phân tích dữ liệu

**Cập nhật lần cuối:** 2 tháng 8 năm 2026

## Giới thiệu bài học

Bài học này trình bày một quy trình phân tích dữ liệu gồm sáu bước, từ việc xác định vấn đề đến diễn giải kết quả và hỗ trợ ra quyết định. Nội dung được minh họa xuyên suốt bằng bộ dữ liệu Titanic để người học có thể quan sát cách một quy trình phân tích được triển khai trong thực tế bằng Python.

Bài học kết hợp giữa kiến thức khái niệm, ví dụ mã nguồn, trực quan hóa dữ liệu, câu hỏi nhanh và bài tập thực hành. Qua đó, người học không chỉ hiểu trình tự của một quy trình phân tích dữ liệu mà còn biết cách áp dụng từng bước vào một bộ dữ liệu cụ thể.

## Kiến thức và kỹ năng sẽ đạt được

Sau khi hoàn thành bài học, người học có thể:

- Giải thích được vai trò của một quy trình phân tích dữ liệu có cấu trúc.
- Xác định được vấn đề, mục tiêu và tiêu chí thành công của một bài toán phân tích.
- Nhận biết và lựa chọn được các nguồn dữ liệu phù hợp.
- Kiểm tra cấu trúc, nguồn gốc và chất lượng ban đầu của dữ liệu.
- Xử lý được một số vấn đề phổ biến như giá trị thiếu, cột không cần thiết và biến phân loại.
- Sử dụng Python, Pandas, Seaborn và Matplotlib để phân tích và trực quan hóa dữ liệu.
- Đọc và diễn giải được ma trận tương quan, biểu đồ cột, histogram và scatter plot.
- Hiểu được cách chia dữ liệu, huấn luyện mô hình và đánh giá độ chính xác ở mức cơ bản.
- Chuyển kết quả phân tích thành nhận xét, khuyến nghị và quyết định có thể thực hiện.
- Nhận thức được rằng tương quan không đồng nghĩa với quan hệ nhân quả và một chỉ số đánh giá đơn lẻ không đủ để kết luận về mô hình.

## Cấu trúc bài học

Bài học gồm các nội dung chính sau:

1. Xác định vấn đề.
2. Thu thập dữ liệu.
3. Làm sạch dữ liệu.
4. Phân tích dữ liệu.
5. Trực quan hóa kết quả.
6. Diễn giải và ra quyết định.
7. Tóm tắt toàn bộ quy trình.
8. Câu hỏi ôn tập và bài tập thực hành.

## Yêu cầu chuẩn bị

Để thực hành đầy đủ các ví dụ trong bài, người học nên có:

- Kiến thức Python cơ bản.
- Môi trường Jupyter Notebook, JupyterLab hoặc Google Colab.
- Các thư viện `pandas`, `seaborn`, `matplotlib` và `scikit-learn`.
- Hiểu biết cơ bản về DataFrame, biến số, biến phân loại và biểu đồ dữ liệu.

Có thể cài đặt các thư viện cần thiết bằng lệnh:

```bash
pip install pandas seaborn matplotlib scikit-learn
```

---



Phân tích dữ liệu là quá trình thu thập, làm sạch, tổ chức và diễn giải dữ liệu nhằm khám phá những hiểu biết hữu ích và hỗ trợ việc ra quyết định. Quy trình này được triển khai theo một cách tiếp cận có cấu trúc, trong đó:

- **Quy trình từng bước:** Chuyển đổi dữ liệu thô thành những hiểu biết có ý nghĩa.
- **Cách tiếp cận có hệ thống:** Góp phần bảo đảm độ chính xác và độ tin cậy của kết quả.
- **Ra quyết định tốt hơn:** Hỗ trợ đưa ra quyết định dựa trên dữ liệu thay vì chỉ dựa trên cảm tính.

<p align="center">
  <img src="images/image-4-v1.png" alt="alt text" />
</p>

### Câu hỏi nhanh

**Câu 1.** Mục tiêu chính của một quy trình phân tích dữ liệu có cấu trúc là gì?

A. Chỉ lưu trữ dữ liệu  
B. Chuyển dữ liệu thô thành thông tin có ý nghĩa  
C. Loại bỏ hoàn toàn vai trò của con người  
D. Chỉ tạo biểu đồ  

**Câu 2. Đúng hay sai?** Một quy trình phân tích dữ liệu có hệ thống giúp tăng độ chính xác và độ tin cậy của kết quả.

---

# Các bước trong quy trình phân tích dữ liệu

## 1. Xác định vấn đề

Trước khi bắt đầu bất kỳ hoạt động phân tích nào, cần xác định rõ vấn đề cần giải quyết. Bước này bao gồm việc làm rõ câu hỏi, mục tiêu hoặc cơ hội phân tích, đồng thời bảo đảm rằng mục tiêu phân tích phù hợp với kỳ vọng của các bên liên quan.

Một vấn đề được xác định rõ giúp toàn bộ quá trình phân tích tập trung, phù hợp và tránh thu thập những dữ liệu không cần thiết.

### Các công việc chính

- Xác định vấn đề cốt lõi hoặc cơ hội cần phân tích.
- Thiết lập mục tiêu rõ ràng và kết quả mong đợi.
- Tìm hiểu bối cảnh, nhu cầu của các bên liên quan và các ràng buộc.
- Xác định tiêu chí thành công để đánh giá hiệu quả của quá trình phân tích.

### Ví dụ

Một công ty nhận thấy doanh số trong ba tháng gần đây giảm đáng kể. Thay vì đặt câu hỏi chung chung như “Vì sao doanh số giảm?”, nhóm phân tích có thể cụ thể hóa thành:

- Doanh số giảm ở sản phẩm nào?
- Khu vực nào có mức giảm lớn nhất?
- Doanh số giảm ở nhóm khách hàng nào?
- Mức giảm có liên quan đến giá bán, tồn kho hay hoạt động marketing không?

### Câu hỏi nhanh

**Câu 1.** Vì sao cần xác định vấn đề trước khi thu thập dữ liệu?

A. Để giảm dung lượng tệp  
B. Để bảo đảm quá trình phân tích tập trung và phù hợp  
C. Để tránh sử dụng biểu đồ  
D. Để loại bỏ toàn bộ dữ liệu định tính  

**Câu 2.** Nội dung nào sau đây thuộc bước xác định vấn đề?

A. Xử lý giá trị thiếu  
B. Xác định tiêu chí thành công  
C. Huấn luyện mô hình  
D. Vẽ biểu đồ nhiệt  

**Câu 3. Tình huống.** Một trường đại học muốn tìm hiểu nguyên nhân sinh viên bỏ học. Hãy đề xuất hai câu hỏi phân tích cụ thể hơn.

---

## 2. Thu thập dữ liệu

Sau khi xác định được vấn đề, bước tiếp theo là thu thập dữ liệu từ các nguồn phù hợp. Dữ liệu có thể được lấy từ cơ sở dữ liệu nội bộ, API, khảo sát, kỹ thuật thu thập dữ liệu từ trang web hoặc các bộ dữ liệu công khai như Kaggle.

Việc thu thập đúng dữ liệu giúp quá trình phân tích dựa trên thông tin đầy đủ, chính xác và có liên quan.

### Các công việc chính

- Bảo đảm dữ liệu thu thập có liên quan, chính xác và đầy đủ.
- Thu thập dữ liệu từ nhiều nguồn để làm phong phú quá trình phân tích.
- Ghi lại nguồn gốc và cấu trúc của từng bộ dữ liệu để tăng tính minh bạch.
- Xem xét tần suất cập nhật, định dạng và yêu cầu làm mới dữ liệu.

### Ví dụ sử dụng bộ dữ liệu Titanic

```python
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")
titanic.head()
```

### Kết quả minh họa

Bộ dữ liệu Titanic được tích hợp sẵn trong thư viện Seaborn. Lệnh `head()` hiển thị một số dòng đầu tiên để người phân tích kiểm tra nhanh cấu trúc dữ liệu.

<p align="center">
  <img src="images/image-5-v1.png" alt="alt text" />
</p>

> **Lưu ý:** Trong bài giảng này, bộ dữ liệu Titanic được sử dụng làm ví dụ xuyên suốt cho các bước làm sạch, phân tích, trực quan hóa và xây dựng mô hình.

### Câu hỏi nhanh

**Câu 1.** Nguồn nào sau đây có thể được sử dụng để thu thập dữ liệu?

A. Cơ sở dữ liệu nội bộ  
B. API  
C. Khảo sát  
D. Tất cả các phương án trên  

**Câu 2.** Vì sao cần ghi lại nguồn gốc của dữ liệu?

A. Để tăng tính minh bạch và khả năng kiểm tra  
B. Để làm cho dữ liệu lớn hơn  
C. Để tránh làm sạch dữ liệu  
D. Để thay thế bước phân tích  

**Câu 3.** Hàm nào được sử dụng để tải bộ dữ liệu Titanic trong ví dụ?

A. `pd.read_csv()`  
B. `sns.load_dataset()`  
C. `plt.load()`  
D. `np.loadtxt()`  

---

## 3. Làm sạch dữ liệu

Dữ liệu thô hiếm khi có thể được sử dụng trực tiếp cho phân tích. Bước làm sạch dữ liệu bao gồm xử lý giá trị thiếu, loại bỏ dữ liệu trùng lặp, chuẩn hóa định dạng và chuyển đổi các biến phân loại sang dạng số.

Dữ liệu được chuẩn bị tốt giúp nâng cao độ tin cậy và độ chính xác của các kết quả phân tích.

### Các công việc chính

- Điền hoặc loại bỏ giá trị thiếu theo cách phù hợp.
- Chuẩn hóa, biến đổi hoặc điều chỉnh thang đo của các biến khi cần thiết.
- Loại bỏ các cột không liên quan, dư thừa hoặc thiếu nhất quán.
- Bảo đảm kiểu dữ liệu và định dạng phù hợp với quá trình phân tích hoặc xây dựng mô hình.

### Kiểm tra và xử lý dữ liệu thiếu

```python
print(titanic.isnull().sum())

titanic["age"].fillna(
    titanic["age"].median(),
    inplace=True
)

titanic["embarked"].fillna(
    titanic["embarked"].mode()[0],
    inplace=True
)
```

Trong đoạn mã trên:

- `isnull().sum()` đếm số giá trị thiếu trong từng cột.
- Giá trị thiếu của cột `age` được thay bằng trung vị.
- Giá trị thiếu của cột `embarked` được thay bằng giá trị xuất hiện phổ biến nhất.

### Loại bỏ các cột không sử dụng

```python
titanic.drop(
    [
        "deck",
        "embark_town",
        "alive",
        "class",
        "who",
        "adult_male"
    ],
    axis=1,
    inplace=True
)
```

### Chuyển đổi biến phân loại

```python
titanic["sex"] = titanic["sex"].map({
    "male": 0,
    "female": 1
})

titanic["embarked"] = titanic["embarked"].map({
    "C": 0,
    "Q": 1,
    "S": 2
})

titanic.head()
```

<p align="center">
  <img src="images/image-6.png" alt="alt text" />
</p>

### Câu hỏi nhanh

**Câu 1.** Lệnh nào dùng để đếm số giá trị thiếu trong từng cột?

A. `titanic.head()`  
B. `titanic.isnull().sum()`  
C. `titanic.describe()`  
D. `titanic.drop()`  

**Câu 2.** Trong ví dụ, giá trị thiếu của cột `age` được thay thế bằng:

A. Giá trị nhỏ nhất  
B. Giá trị lớn nhất  
C. Trung vị  
D. Số 0  

**Câu 3.** Vì sao cột `sex` được chuyển thành giá trị số?

A. Để giảm số lượng dòng  
B. Để dữ liệu phù hợp hơn với các thuật toán phân tích hoặc mô hình hóa  
C. Để thay đổi giới tính của hành khách  
D. Để tạo biểu đồ tròn  

**Câu 4. Đúng hay sai?** Có thể loại bỏ mọi cột chứa giá trị thiếu mà không cần xem xét bối cảnh.

---

## 4. Phân tích dữ liệu

Phân tích dữ liệu là bước cốt lõi, trong đó người phân tích tìm kiếm mẫu hình, xu hướng và mối quan hệ trong dữ liệu. Tùy theo mục tiêu, bước này có thể sử dụng thống kê mô tả, phân tích tương quan hoặc các mô hình học máy.

### Các công việc chính

- Tính các đại lượng thống kê như trung bình, trung vị, yếu vị và phương sai.
- Xác định tương quan, xu hướng và điểm bất thường.
- Áp dụng các mô hình như hồi quy, phân cụm hoặc phân loại.
- So sánh kết quả với kỳ vọng hoặc giả thuyết ban đầu.

### Phân tích ma trận tương quan

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
sns.heatmap(
    titanic.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Ma trận tương quan")
plt.show()
```
<p align="center">
  <img src="images/image-7.png" alt="alt text" />
</p>

Biểu đồ nhiệt giúp quan sát mức độ tương quan giữa các biến số trong bộ dữ liệu.

### Phân tích tỷ lệ sống sót theo hạng vé

```python
sns.barplot(
    x="pclass",
    y="survived",
    data=titanic
)
plt.title("Tỷ lệ sống sót theo hạng hành khách")
plt.show()
```

<p align="center">
  <img src="images/image-8.png" alt="alt text" />
</p>

Biểu đồ cột cho phép so sánh tỷ lệ sống sót trung bình giữa các nhóm hạng hành khách.



### Câu hỏi nhanh

**Câu 1.** Ma trận tương quan được sử dụng để làm gì?

A. Kiểm tra kiểu tệp  
B. Xem xét mối quan hệ giữa các biến  
C. Xóa dữ liệu trùng lặp  
D. Tải dữ liệu từ API  

**Câu 2.** Biểu đồ `barplot` trong ví dụ được sử dụng để so sánh:

A. Tuổi và giá vé  
B. Hạng hành khách và tỷ lệ sống sót  
C. Giới tính và cảng lên tàu  
D. Số lượng cột và số lượng dòng  

**Câu 3.** Mô hình nào sau đây có thể được sử dụng trong bước phân tích dữ liệu?

A. Hồi quy  
B. Phân cụm  
C. Phân loại  
D. Tất cả các phương án trên  

**Câu 4. Tình huống.** Nếu hai biến có tương quan cao, có thể kết luận chắc chắn rằng biến này gây ra biến kia hay không?

---

## 5. Trực quan hóa kết quả

Trực quan hóa giúp làm cho dữ liệu phức tạp trở nên dễ hiểu hơn. Biểu đồ, đồ thị và bảng điều khiển có thể làm nổi bật các xu hướng, mẫu hình và điểm bất thường quan trọng.

Một trực quan hóa tốt không chỉ đẹp mà còn phải rõ ràng, trực quan và hỗ trợ hành động.

### Các nguyên tắc chính

- Chọn loại biểu đồ phù hợp như histogram, biểu đồ phân tán, biểu đồ cột hoặc biểu đồ nhiệt.
- Làm nổi bật rõ ràng các xu hướng, mẫu hình và điểm bất thường.
- Giữ biểu đồ đơn giản, dễ hiểu và có khả năng hỗ trợ quyết định.
- Có thể kết hợp nhiều biểu đồ trong bảng điều khiển để cung cấp cái nhìn toàn diện.

### Biểu đồ số lượng hành khách sống sót

```python
sns.countplot(
    x="survived",
    data=titanic
)
plt.title("Số lượng hành khách theo trạng thái sống sót")
plt.show()
```

<p align="center">
  <img src="images/image-9.png" alt="alt text" />
</p>
### Biểu đồ phân phối độ tuổi

```python
sns.histplot(
    titanic["age"],
    kde=True
)
plt.title("Phân phối độ tuổi")
plt.show()
```
<p align="center">
  <img src="images/image-1-v1.png" alt="alt text" />
</p>
### Biểu đồ phân tán giữa tuổi và giá vé

```python
sns.scatterplot(
    x="age",
    y="fare",
    hue="survived",
    data=titanic
)
plt.title("Mối quan hệ giữa giá vé và độ tuổi theo trạng thái sống sót")
plt.show()
```

<p align="center">
  <img src="images/image-10.png" alt="alt text" />
</p>

### Câu hỏi nhanh

**Câu 1.** Loại biểu đồ nào phù hợp để thể hiện phân phối của biến `age`?

A. Histogram  
B. Biểu đồ mạng  
C. Biểu đồ Gantt  
D. Bản đồ địa lý  

**Câu 2.** Tham số `hue="survived"` trong biểu đồ phân tán có tác dụng gì?

A. Xóa cột `survived`  
B. Phân biệt các điểm dữ liệu theo trạng thái sống sót  
C. Thay đổi kích thước hình  
D. Tính giá trị trung bình  

**Câu 3. Đúng hay sai?** Một biểu đồ càng chứa nhiều chi tiết thì luôn càng hiệu quả.

**Câu 4.** Vì sao cần chọn loại biểu đồ phù hợp với câu hỏi phân tích?

---

## 6. Diễn giải và ra quyết định

Bước cuối cùng là chuyển kết quả phân tích thành những hiểu biết có thể hành động. Việc diễn giải đòi hỏi đặt kết quả vào đúng bối cảnh, truyền đạt rõ ràng và đưa ra các quyết định dựa trên dữ liệu.

Sau khi quyết định được triển khai, cần tiếp tục theo dõi kết quả và điều chỉnh khi cần thiết.

### Các công việc chính

- Giải thích kết quả trong bối cảnh của vấn đề ban đầu.
- Đưa ra khuyến nghị có thể thực hiện dựa trên các hiểu biết thu được.
- Truyền đạt kết quả rõ ràng đến các bên liên quan.
- Theo dõi kết quả và lặp lại quá trình để cải tiến liên tục.

### Ví dụ xây dựng mô hình dự báo sống sót

Đoạn mã dưới đây minh họa việc chia dữ liệu thành tập huấn luyện và tập kiểm định, xây dựng mô hình `RandomForestClassifier`, sau đó đánh giá độ chính xác.

```python
X = titanic.drop("survived", axis=1)
y = titanic["survived"]

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_val)

accuracy = accuracy_score(
    y_val,
    y_pred
)

print(f"Độ chính xác của mô hình: {accuracy:.4f}")
```

### Kết quả

```text
Độ chính xác của mô hình: 0.8101
```

> **Lưu ý:** Đoạn mã trong nguồn sử dụng `train_test_split`, `RandomForestClassifier` và `accuracy_score`. Các đối tượng này cần được nhập từ thư viện phù hợp trước khi chạy.

### Diễn giải kết quả

Độ chính xác `0.8101` cho biết mô hình dự đoán đúng khoảng 81,01% số quan sát trong tập kiểm định. Tuy nhiên, không nên chỉ dựa vào độ chính xác để đánh giá mô hình. Trong các bài toán thực tế, cần xem xét thêm những chỉ số khác và đặt kết quả trong bối cảnh của vấn đề ban đầu.

### Câu hỏi nhanh

**Câu 1.** Mục tiêu của bước diễn giải là gì?

A. Chỉ trình bày các con số  
B. Chuyển kết quả phân tích thành hiểu biết và hành động  
C. Xóa toàn bộ dữ liệu  
D. Thay đổi vấn đề ban đầu  

**Câu 2.** Giá trị độ chính xác `0.8101` tương ứng với khoảng bao nhiêu phần trăm?

A. 8,101%  
B. 18,01%  
C. 81,01%  
D. 810,1%  

**Câu 3.** Vì sao cần tiếp tục theo dõi kết quả sau khi đưa ra quyết định?

A. Để kiểm tra quyết định có hiệu quả hay không và điều chỉnh khi cần  
B. Để làm tăng số lượng cột  
C. Để tránh trao đổi với các bên liên quan  
D. Để không cần phân tích lại  

**Câu 4. Đúng hay sai?** Chỉ số độ chính xác luôn đủ để đánh giá đầy đủ một mô hình phân loại.

---

# Tóm tắt quy trình

| Bước | Nội dung chính | Câu hỏi trọng tâm |
|---|---|---|
| **1. Xác định vấn đề** | Làm rõ mục tiêu, bối cảnh và tiêu chí thành công | Chúng ta cần giải quyết vấn đề gì? |
| **2. Thu thập dữ liệu** | Thu thập dữ liệu phù hợp từ các nguồn đáng tin cậy | Cần dữ liệu nào và lấy từ đâu? |
| **3. Làm sạch dữ liệu** | Xử lý giá trị thiếu, dữ liệu dư thừa và định dạng | Dữ liệu đã sẵn sàng để phân tích chưa? |
| **4. Phân tích dữ liệu** | Tìm mẫu hình, xu hướng và mối quan hệ | Dữ liệu cho thấy điều gì? |
| **5. Trực quan hóa kết quả** | Trình bày kết quả bằng biểu đồ và bảng điều khiển | Làm thế nào để kết quả dễ hiểu? |
| **6. Diễn giải và ra quyết định** | Chuyển kết quả thành khuyến nghị và hành động | Kết quả có ý nghĩa gì và cần làm gì tiếp theo? |

---

# Câu hỏi ôn tập cuối bài

## Phần A. Câu hỏi trắc nghiệm

**Câu 1.** Bước đầu tiên trong quy trình phân tích dữ liệu là:

A. Làm sạch dữ liệu  
B. Xác định vấn đề  
C. Trực quan hóa dữ liệu  
D. Huấn luyện mô hình  

**Câu 2.** Nội dung nào sau đây thuộc bước thu thập dữ liệu?

A. Xác định nguồn dữ liệu  
B. Xử lý giá trị thiếu  
C. Tính ma trận tương quan  
D. Đánh giá độ chính xác của mô hình  

**Câu 3.** Trung vị thường được sử dụng để:

A. Đổi tên cột  
B. Điền giá trị thiếu cho biến số  
C. Tạo API  
D. Vẽ biểu đồ phân tán  

**Câu 4.** Công cụ nào được sử dụng để trực quan hóa ma trận tương quan trong ví dụ?

A. `sns.heatmap()`  
B. `sns.load_dataset()`  
C. `pd.DataFrame()`  
D. `model.fit()`  

**Câu 5.** Loại biểu đồ nào được sử dụng để biểu diễn phân phối độ tuổi?

A. Histogram  
B. Biểu đồ tròn  
C. Biểu đồ Gantt  
D. Bản đồ nhiệt địa lý  

**Câu 6.** Giá trị `test_size=0.2` có nghĩa là:

A. 20% dữ liệu được sử dụng làm tập kiểm định  
B. 20% dữ liệu bị xóa  
C. Có 20 biến đầu vào  
D. Mô hình có độ chính xác 20%  

**Câu 7.** Độ chính xác `0.8101` tương đương:

A. 0,8101%  
B. 8,101%  
C. 81,01%  
D. 810,1%  

**Câu 8.** Bước nào chuyển kết quả phân tích thành khuyến nghị?

A. Thu thập dữ liệu  
B. Làm sạch dữ liệu  
C. Diễn giải và ra quyết định  
D. Chỉ trực quan hóa dữ liệu  

## Phần B. Câu hỏi đúng/sai

**Câu 1.** Cần xác định mục tiêu trước khi thu thập dữ liệu.

**Câu 2.** Dữ liệu thô luôn có thể được sử dụng trực tiếp để xây dựng mô hình.

**Câu 3.** Ma trận tương quan có thể giúp nhận diện mối quan hệ giữa các biến.

**Câu 4.** Tương quan cao luôn chứng minh quan hệ nhân quả.

**Câu 5.** Trực quan hóa dữ liệu có thể hỗ trợ truyền đạt kết quả đến các bên liên quan.

**Câu 6.** Sau khi đưa ra quyết định, không cần theo dõi kết quả.

## Phần C. Câu hỏi tự luận ngắn

**Câu 1.** Trình bày sáu bước chính của quy trình phân tích dữ liệu.

**Câu 2.** Vì sao xác định vấn đề được xem là bước quan trọng đầu tiên?

**Câu 3.** Nêu ba vấn đề thường gặp trong dữ liệu thô.

**Câu 4.** Phân biệt phân tích dữ liệu và trực quan hóa dữ liệu.

**Câu 5.** Vì sao kết quả của mô hình cần được diễn giải trong bối cảnh thực tế?

## Phần D. Bài tập thực hành

### Bài 1. Khảo sát bộ dữ liệu

Sử dụng bộ dữ liệu Titanic và thực hiện các yêu cầu sau:

1. Hiển thị năm dòng đầu tiên.
2. Xác định số dòng và số cột.
3. Kiểm tra kiểu dữ liệu của từng cột.
4. Đếm số giá trị thiếu trong từng cột.
5. Viết nhận xét ngắn về chất lượng dữ liệu.

### Bài 2. Làm sạch dữ liệu

Thực hiện các yêu cầu sau:

1. Điền giá trị thiếu của cột `age` bằng trung vị.
2. Điền giá trị thiếu của cột `embarked` bằng yếu vị.
3. Loại bỏ các cột không cần thiết.
4. Chuyển đổi cột `sex` thành giá trị số.
5. Kiểm tra lại dữ liệu sau khi xử lý.

### Bài 3. Phân tích và trực quan hóa

Thực hiện các yêu cầu sau:

1. Tính thống kê mô tả cho các cột số.
2. Vẽ biểu đồ phân phối độ tuổi.
3. So sánh tỷ lệ sống sót theo hạng hành khách.
4. Vẽ biểu đồ phân tán giữa tuổi và giá vé.
5. Viết ít nhất ba nhận xét từ các biểu đồ.

### Bài 4. Diễn giải kết quả

Giả sử một mô hình dự đoán sống sót đạt độ chính xác 81,01%.

1. Giải thích ý nghĩa của kết quả này.
2. Nêu hai lý do vì sao không nên chỉ sử dụng độ chính xác.
3. Đề xuất thêm hai chỉ số đánh giá mô hình.
4. Nêu một hạn chế đạo đức hoặc thực tiễn khi sử dụng mô hình.

---

# Đáp án và gợi ý trả lời

<details>
<summary><strong>Nhấn để hiển thị đáp án</strong></summary>

## Đáp án câu hỏi nhanh — Phần mở đầu

### Câu 1

B. Chuyển dữ liệu thô thành thông tin có ý nghĩa.

### Câu 2

Đúng.

## Đáp án câu hỏi nhanh — Bước 1

### Câu 1

B. Để bảo đảm quá trình phân tích tập trung và phù hợp.

### Câu 2

B. Xác định tiêu chí thành công.

### Câu 3

Ví dụ:

- Những nhóm sinh viên nào có tỷ lệ bỏ học cao nhất?
- Kết quả học tập, hoàn cảnh tài chính hoặc mức độ tham gia học tập có liên quan đến nguy cơ bỏ học hay không?

## Đáp án câu hỏi nhanh — Bước 2

### Câu 1

D. Tất cả các phương án trên.

### Câu 2

A. Để tăng tính minh bạch và khả năng kiểm tra.

### Câu 3

B. `sns.load_dataset()`.

## Đáp án câu hỏi nhanh — Bước 3

### Câu 1

B. `titanic.isnull().sum()`.

### Câu 2

C. Trung vị.

### Câu 3

B. Để dữ liệu phù hợp hơn với các thuật toán phân tích hoặc mô hình hóa.

### Câu 4

Sai. Cần xem xét ý nghĩa của cột, tỷ lệ thiếu và mục tiêu phân tích trước khi quyết định loại bỏ.

## Đáp án câu hỏi nhanh — Bước 4

### Câu 1

B. Xem xét mối quan hệ giữa các biến.

### Câu 2

B. Hạng hành khách và tỷ lệ sống sót.

### Câu 3

D. Tất cả các phương án trên.

### Câu 4

Không. Tương quan không đồng nghĩa với quan hệ nhân quả.

## Đáp án câu hỏi nhanh — Bước 5

### Câu 1

A. Histogram.

### Câu 2

B. Phân biệt các điểm dữ liệu theo trạng thái sống sót.

### Câu 3

Sai. Biểu đồ quá nhiều chi tiết có thể gây khó hiểu.

### Câu 4

Vì mỗi loại biểu đồ phù hợp với một loại dữ liệu và một mục tiêu truyền đạt khác nhau.

## Đáp án câu hỏi nhanh — Bước 6

### Câu 1

B. Chuyển kết quả phân tích thành hiểu biết và hành động.

### Câu 2

C. 81,01%.

### Câu 3

A. Để kiểm tra quyết định có hiệu quả hay không và điều chỉnh khi cần.

### Câu 4

Sai. Cần xem xét thêm các chỉ số khác và bối cảnh của bài toán.

## Đáp án ôn tập cuối bài

### Phần A

1. B  
2. A  
3. B  
4. A  
5. A  
6. A  
7. C  
8. C  

### Phần B

1. Đúng.  
2. Sai.  
3. Đúng.  
4. Sai.  
5. Đúng.  
6. Sai.  

### Phần C

**Câu 1.** Sáu bước gồm xác định vấn đề, thu thập dữ liệu, làm sạch dữ liệu, phân tích dữ liệu, trực quan hóa kết quả, diễn giải và ra quyết định.

**Câu 2.** Vì bước này xác định mục tiêu, phạm vi, dữ liệu cần thiết và tiêu chí đánh giá thành công.

**Câu 3.** Ví dụ: giá trị thiếu, dữ liệu trùng lặp, định dạng không nhất quán, giá trị ngoại lệ hoặc kiểu dữ liệu không phù hợp.

**Câu 4.** Phân tích dữ liệu tập trung tìm mẫu hình và rút ra kết luận; trực quan hóa tập trung trình bày dữ liệu hoặc kết quả dưới dạng hình ảnh dễ hiểu.

**Câu 5.** Vì cùng một kết quả thống kê có thể mang ý nghĩa khác nhau trong các bối cảnh khác nhau. Việc diễn giải cần gắn với mục tiêu, đối tượng và các ràng buộc thực tế.

### Phần D

Đây là các bài tập thực hành mở. Kết quả phụ thuộc vào cách triển khai, phiên bản dữ liệu và lựa chọn xử lý của người học. Bài làm cần trình bày rõ mã lệnh, kết quả và nhận xét.

</details>
