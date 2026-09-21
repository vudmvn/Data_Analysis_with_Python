# Tuần 08–09: Data Segmentation, K-Means, K-Means++, Elbow Method & Clustering

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 22 tháng 9 năm 2026

---

## 📌 Tổng quan chuyên đề

Chuyên đề này cung cấp kiến thức nền tảng và chuyên sâu về **Học không giám sát (Unsupervised Machine Learning)**, tập trung vào ba mảng kiến thức trụ cột:
1. **Phân khúc dữ liệu (Data Segmentation):** Bản chất phân khúc khách hàng, thị trường và sản phẩm; phân biệt giữa Segmentation, Data Partitioning và Targeting; quy trình xây dựng bài toán phân khúc trong doanh nghiệp.
2. **Tổng quan Phân cụm dữ liệu (Clustering Overview):** Khám phá cấu trúc tự nhiên của dữ liệu chưa gán nhãn; phân biệt Hard vs Soft Clustering; 5 phương pháp phân cụm cốt lõi (Centroid, Density, Hierarchical, Distribution, Fuzzy); và các chỉ số đánh giá chất lượng (Silhouette, Davies-Bouldin).
3. **Các Phương pháp Dựa trên Tâm (Centroid-based Methods):** Đi sâu vào giải thuật **K-Means**, thuật toán khởi tạo thông minh **K-Means++** (Arthur & Vassilvitskii, 2007) với giới hạn xấp xỉ $O(\log K)$, **Phương pháp Khuỷu tay (Elbow Method)** dựa trên Distortion và Inertia, cùng biến thể kiên cường trước ngoại lai **K-Medoids (PAM)**.

---

## 🎯 Mục tiêu bài học

1. **Hiểu rõ triết lý Học không giám sát:** Khám phá tri thức tiềm ẩn từ dữ liệu chưa được dán nhãn (Unlabeled Data).
2. **Làm chủ quy trình K-Means & K-Means++:** Nắm vững giải thuật Lloyd gồm Khởi tạo $\to$ Gán cụm $\to$ Cập nhật tâm $\to$ Hội tụ; giải thích cơ chế phân phối xác suất $D(x)^2$ của K-Means++ giúp ngăn ngừa cực tiểu cục bộ.
3. **Ứng dụng thành thạo Phương pháp Khuỷu tay (Elbow Method):** Tính toán hai chỉ số **Distortion** và **Inertia**, vẽ đồ thị Elbow và xác định điểm gãy tối ưu để chọn số lượng cụm $K$.
4. **Phân biệt Hard Clustering vs Soft Clustering:** Nắm vững ranh giới giữa việc gán dứt khoát 1 điểm vào 1 nhóm và việc mô hình hóa xác suất thành viên đa cụm.
5. **Nắm vững 5 phương pháp phân cụm cốt lõi:** Centroid-based (K-Means), Density-based (DBSCAN), Hierarchical (Dendrogram), Distribution-based (GMM), và Fuzzy (FCM).
6. **Thực hành với Scikit-Learn & NumPy:** Lập trình K-Means bằng Scikit-Learn, khảo sát tham số `init='k-means++'` và `n_init`, phân khúc khách hàng đa biến (Customer Segmentation) và trực quan hóa các ô Voronoi.

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part07-introduction-to-data-segmentation.md](part07-introduction-to-data-segmentation.md) | `.md` | Bài giảng Tổng quan Phân khúc dữ liệu (Data Segmentation): Khái niệm, Phân loại vs Phân cụm, Quy trình phân khúc khách hàng, Phân tích RFM |
| [part07-clustering-machine-learning-vn.md](part07-clustering-machine-learning-vn.md) | `.md` | Bài giảng Tổng quan Phân cụm trong Machine Learning: Hard vs Soft, 5 phương pháp phân cụm (K-Means, DBSCAN, Hierarchical, GMM, FCM), Đánh giá Silhouette, Code Scikit-Learn & Hình ảnh minh họa |
| [part07-kmeans-elbow-kmeans-plus-plus-vn.md](part07-kmeans-elbow-kmeans-plus-plus-vn.md) | `.md` | Bài giảng Chuyên sâu Centroid-based Methods: K-Means (Lloyd), Khởi tạo thông minh K-Means++ ($O(\log K)$), Phương pháp Khuỷu tay (Elbow Method với Distortion/Inertia), K-Medoids & 8 hình ảnh minh họa |
| [part07-clustering-machine-learning.md](part07-clustering-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Clustering in Machine Learning |
| [part07-kmeans-elbow-kmeans-plus-plus.md](part07-kmeans-elbow-kmeans-plus-plus.md) | `.md` | Bản sao tiêu chuẩn bài học K-Means, K-Means++ & Elbow Method |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Tất cả 11 hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):

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

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Clustering in Machine Learning](https://www.geeksforgeeks.org/machine-learning/clustering-in-machine-learning/)
- [GeeksforGeeks – K-means Clustering Introduction](https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/)
- [GeeksforGeeks – Elbow Method for Optimal Value of k in KMeans](https://www.geeksforgeeks.org/machine-learning/elbow-method-for-optimal-value-of-k-in-kmeans/)
- [Arthur & Vassilvitskii (2007) – k-means++: The Advantages of Careful Seeding](https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf)
- [Scikit-Learn Official User Guide – K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
