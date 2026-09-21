# Tuần 08–09: Data Segmentation, K-Means, K-Means++, Elbow Method & Hierarchical Clustering

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 22 tháng 9 năm 2026

---

## 📌 Tổng quan chuyên đề

Chuyên đề này cung cấp kiến thức nền tảng và chuyên sâu về **Học không giám sát (Unsupervised Machine Learning)**, tập trung vào bốn mảng kiến thức trụ cột:
1. **Phân khúc dữ liệu (Data Segmentation):** Bản chất phân khúc khách hàng, thị trường và sản phẩm; phân biệt giữa Segmentation, Data Partitioning và Targeting; quy trình xây dựng bài toán phân khúc trong doanh nghiệp.
2. **Tổng quan Phân cụm dữ liệu (Clustering Overview):** Khám phá cấu trúc tự nhiên của dữ liệu chưa gán nhãn; phân biệt Hard vs Soft Clustering; 5 phương pháp phân cụm cốt lõi (Centroid, Density, Hierarchical, Distribution, Fuzzy); và các chỉ số đánh giá chất lượng (Silhouette, Davies-Bouldin).
3. **Các Phương pháp Dựa trên Tâm (Centroid-based Methods):** Đi sâu vào giải thuật **K-Means**, thuật toán khởi tạo thông minh **K-Means++** (Arthur & Vassilvitskii, 2007) với giới hạn xấp xỉ $O(\log K)$, **Phương pháp Khuỷu tay (Elbow Method)** dựa trên Distortion và Inertia, cùng biến thể kiên cường trước ngoại lai **K-Medoids (PAM)**.
4. **Các Phương pháp Dựa trên Tính liên kết (Connectivity-based Methods):** Khám phá toàn diện **Phân cụm Phân cấp (Hierarchical Clustering)**, bao gồm hai nhánh **Agglomerative (Bottom-Up)** và **Divisive (Top-Down)**; cấu trúc biểu đồ cây **Dendrogram** và quy tắc cắt qua nhánh dọc dài nhất tìm $K$ tối ưu; 5 tiêu chuẩn liên kết (Single, Complete, Average, Centroid, Ward); và Hệ số tương quan Cophenetic (CPCC).

---

## 🎯 Mục tiêu bài học

1. **Hiểu rõ triết lý Học không giám sát:** Khám phá tri thức tiềm ẩn từ dữ liệu chưa được dán nhãn (Unlabeled Data).
2. **Làm chủ quy trình K-Means & K-Means++:** Nắm vững giải thuật Lloyd gồm Khởi tạo $\to$ Gán cụm $\to$ Cập nhật tâm $\to$ Hội tụ; giải thích cơ chế phân phối xác suất $D(x)^2$ của K-Means++ giúp ngăn ngừa cực tiểu cục bộ.
3. **Ứng dụng thành thạo Phương pháp Khuỷu tay (Elbow Method):** Tính toán hai chỉ số **Distortion** và **Inertia**, vẽ đồ thị Elbow và xác định điểm gãy tối ưu để chọn số lượng cụm $K$.
4. **Làm chủ Phân cụm Phân cấp & Biểu đồ Dendrogram:** Hiểu rõ cơ chế xây dựng cây phân cấp lồng nhau không cần giả định $K$ ban đầu; đọc giải phẫu Dendrogram và áp dụng kỹ thuật cắt ngang qua nhánh dọc dài nhất.
5. **Nắm vững 5 tiêu chuẩn liên kết cụm (Linkage Criteria):** Single Linkage (và hiện tượng nối chuỗi Chaining Effect), Complete Linkage, Average Linkage, Centroid Linkage (và rủi ro Đảo ngược Inversion), cùng Ward's Minimum Variance Criterion.
6. **Đánh giá và so sánh đa chiều các thuật toán:** Định lượng mức độ bảo toàn khoảng cách bằng Cophenetic Correlation Coefficient (CPCC); so sánh K-Means vs Hierarchical vs DBSCAN.
7. **Thực hành với Scikit-Learn, SciPy & NumPy:** Lập trình K-Means, K-Means++, AgglomerativeClustering, tự cài đặt thuật toán Divisive Clustering đệ quy, trích xuất ma trận liên kết và biểu diễn Dendrogram.

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part07-introduction-to-data-segmentation.md](part07-introduction-to-data-segmentation.md) | `.md` | Bài giảng Tổng quan Phân khúc dữ liệu (Data Segmentation): Khái niệm, Phân loại vs Phân cụm, Quy trình phân khúc khách hàng, Phân tích RFM |
| [part07-clustering-machine-learning-vn.md](part07-clustering-machine-learning-vn.md) | `.md` | Bài giảng Tổng quan Phân cụm trong Machine Learning: Hard vs Soft, 5 phương pháp phân cụm (K-Means, DBSCAN, Hierarchical, GMM, FCM), Đánh giá Silhouette, Code Scikit-Learn & Hình ảnh minh họa |
| [part07-kmeans-elbow-kmeans-plus-plus-vn.md](part07-kmeans-elbow-kmeans-plus-plus-vn.md) | `.md` | Bài giảng Chuyên sâu Centroid-based Methods: K-Means (Lloyd), Khởi tạo thông minh K-Means++ ($O(\log K)$), Phương pháp Khuỷu tay (Elbow Method với Distortion/Inertia), K-Medoids & 8 hình ảnh minh họa |
| [part07-hierarchical-agglomerative-clustering-vn.md](part07-hierarchical-agglomerative-clustering-vn.md) | `.md` | Bài giảng Chuyên sâu Connectivity-based Methods: Hierarchical Clustering, Agglomerative (Bottom-Up) vs Divisive (Top-Down), Cấu trúc Dendrogram, 5 Linkage Criteria, CPCC, Code Scikit-Learn/SciPy & 13 hình ảnh minh họa |
| [part07-clustering-machine-learning.md](part07-clustering-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Clustering in Machine Learning |
| [part07-kmeans-elbow-kmeans-plus-plus.md](part07-kmeans-elbow-kmeans-plus-plus.md) | `.md` | Bản sao tiêu chuẩn bài học K-Means, K-Means++ & Elbow Method |
| [part07-hierarchical-agglomerative-clustering.md](part07-hierarchical-agglomerative-clustering.md) | `.md` | Bản sao tiêu chuẩn bài học Hierarchical & Agglomerative Clustering |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Tất cả 24 hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):

### Nhóm 1: Tổng quan Phân cụm (Clustering Overview - 3 ảnh)
- `clustering-overview.png`: Sơ đồ khái niệm phân cụm dữ liệu chưa gán nhãn thành các nhóm tự nhiên.
- `hard-vs-soft-clustering.png`: So sánh đối chiếu trực quan giữa Phân cụm cứng (Hard Clustering) và Phân cụm mờ/mềm (Soft Clustering).
- `centroid-based-kmeans.png`: Minh họa cơ chế dịch chuyển tâm cụm (Centroids) và gom nhóm thành viên của K-Means.

### Nhóm 2: K-Means, K-Means++ & Elbow Method (8 ảnh)
- `kmeans-step1-initial.png`: Bước 1 - Tập dữ liệu chưa gán nhãn ban đầu trong không gian 2D.
- `kmeans-step2-centroids.png`: Bước 2 - Khởi tạo ngẫu nhiên $K$ tâm cụm ban đầu.
- `kmeans-step3-assignment.png`: Bước 3 - Gán từng điểm dữ liệu vào tâm cụm gần nhất theo khoảng cách Euclidean.
- `kmeans-step4-convergence.png`: Bước 4 - Cập nhật trọng tâm cụm và đạt trạng thái hội tụ ổn định.
- `elbow-method-curve.png`: Biểu đồ trực quan hóa nguyên lý đường cong khuỷu tay tìm $K$ tối ưu.
- `elbow-distortion-plot.png`: Đồ thị biến thiên của độ biến dạng (Distortion) theo các giá trị $K$.
- `elbow-inertia-plot.png`: Đồ thị biến thiên của quán tính (Inertia / WCSS) theo các giá trị $K$.
- `kmeans-clusters-visualization.png`: Trực quan hóa phân cụm hoàn chỉnh sau khi lựa chọn $K$ tối ưu.

### Nhóm 3: Hierarchical & Agglomerative Clustering (13 ảnh)
- `types-of-hierarchical-clustering.png`: Sơ đồ phân nhánh hai hướng tiếp cận Phân cụm phân cấp: Agglomerative (Bottom-Up) và Divisive (Top-Down).
- `bottom-up-agglomerative.png`: Mô hình quy trình phân cụm tích tụ từ $N$ cụm đơn lẻ đến 1 siêu cụm duy nhất.
- `agglomerative-hierarchical-steps.png`: Minh họa từng bước sáp nhập các cụm lân cận trong Agglomerative Clustering.
- `top-down-divisive.png`: Mô hình quy trình phân cụm phân tách từ 1 cụm tổng thể phân rã đệ quy xuống $N$ cụm đơn lẻ.
- `divisive-hierarchical-steps.png`: Minh họa từng bước phân tách đệ quy trong Divisive Clustering.
- `dendrogram-explanation.png`: Khái niệm và giải phẫu cấu trúc biểu đồ cây Dendrogram (lá, cành ngang, khoảng cách sáp nhập).
- `dendrogram-plot.png`: Mẫu đồ thị Dendrogram minh họa trực quan liên kết cụm.
- `longest-path-dendrogram.png`: Kỹ thuật xác định số cụm tối ưu $K$ bằng đường cắt ngang qua nhánh dọc dài nhất.
- `distance-metrics.png`: Giới thiệu 4 tiêu chuẩn liên kết khoảng cách cụm: Min, Max, Group Average, Ward's method.
- `group-average-linkage.png`: Sơ đồ so sánh chi tiết hình học giữa các tiêu chuẩn liên kết khoảng cách cụm.
- `download-agglomerative-plot.png`: Đồ thị thực nghiệm phân cụm Agglomerative Clustering và biểu đồ Dendrogram bằng Scikit-Learn & SciPy.
- `download-divisive-plot.png`: Đồ thị thực nghiệm phân cụm Divisive Clustering và Dendrogram bằng Python.
- `hierarchical-applications.png`: Tổng hợp các miền ứng dụng thực tiễn đột phá của Phân cụm phân cấp trong đời sống và công nghệ.

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Hierarchical Clustering in Machine Learning](https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/)
- [GeeksforGeeks – Hierarchical Clustering in Data Mining](https://www.geeksforgeeks.org/hierarchical-clustering-in-data-mining/)
- [GeeksforGeeks – Clustering in Machine Learning](https://www.geeksforgeeks.org/machine-learning/clustering-in-machine-learning/)
- [GeeksforGeeks – K-means Clustering Introduction](https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/)
- [GeeksforGeeks – Elbow Method for Optimal Value of k in KMeans](https://www.geeksforgeeks.org/machine-learning/elbow-method-for-optimal-value-of-k-in-kmeans/)
- [Scikit-Learn Official User Guide – Hierarchical Clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
- [SciPy Hierarchy Module](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)
