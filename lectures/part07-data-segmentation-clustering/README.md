# Tuần 08–09: Data Segmentation, K-Means, Hierarchical, Density-based (DBSCAN/OPTICS) & Distribution-based (GMM/EM) Clustering

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 22 tháng 9 năm 2026

---

## 📌 Tổng quan chuyên đề

Chuyên đề này cung cấp kiến thức nền tảng và chuyên sâu về **Học không giám sát (Unsupervised Machine Learning)**, hoàn thiện trọn vẹn năm trường phái phân cụm trụ cột:
1. **Phân khúc dữ liệu (Data Segmentation):** Bản chất phân khúc khách hàng, thị trường và sản phẩm; phân biệt giữa Segmentation, Data Partitioning và Targeting; quy trình xây dựng bài toán phân khúc trong doanh nghiệp.
2. **Tổng quan Phân cụm dữ liệu (Clustering Overview):** Khám phá cấu trúc tự nhiên của dữ liệu chưa gán nhãn; phân biệt Hard vs Soft Clustering; 5 phương pháp phân cụm cốt lõi (Centroid, Density, Hierarchical, Distribution, Fuzzy); và các chỉ số đánh giá chất lượng (Silhouette, Davies-Bouldin).
3. **Các Phương pháp Dựa trên Tâm (Centroid-based Methods):** Đi sâu vào giải thuật **K-Means**, thuật toán khởi tạo thông minh **K-Means++** (Arthur & Vassilvitskii, 2007) với giới hạn xấp xỉ $O(\log K)$, **Phương pháp Khuỷu tay (Elbow Method)** dựa trên Distortion và Inertia, cùng biến thể kiên cường trước ngoại lai **K-Medoids (PAM)**.
4. **Các Phương pháp Dựa trên Tính liên kết (Connectivity-based Methods):** Khám phá toàn diện **Phân cụm Phân cấp (Hierarchical Clustering)**, bao gồm hai nhánh **Agglomerative (Bottom-Up)** và **Divisive (Top-Down)**; cấu trúc biểu đồ cây **Dendrogram** và quy tắc cắt qua nhánh dọc dài nhất tìm $K$ tối ưu; 5 tiêu chuẩn liên kết (Single, Complete, Average, Centroid, Ward); và Hệ số tương quan Cophenetic (CPCC).
5. **Các Phương pháp Dựa trên Mật độ (Density-based Methods):** Làm chủ **DBSCAN** với hai siêu tham số $(\epsilon, \text{MinPts})$, phân loại 3 nhóm điểm (Core, Border, Noise), kỹ thuật tìm $\epsilon$ bằng đồ thị K-Distance; và thuật toán **OPTICS** khắc phục bài toán đa mật độ thông qua Core Distance, Reachability Distance, Biểu đồ Khả năng tiếp cận (**Reachability Plot**) cùng cơ chế trích xuất đa tầng $\xi$-steep.
6. **Các Phương pháp Dựa trên Phân phối (Distribution-based Methods):** Làm chủ **Mô hình Hỗn hợp Gauss (Gaussian Mixture Model - GMM)** và thuật toán **Expectation-Maximization (EM)**; phân cụm mềm (Soft Assignment) với ma trận trách nhiệm $\gamma_{nk}$; 4 dạng ma trận hiệp phương sai (`spherical`, `diag`, `tied`, `full`); tiêu chuẩn thông tin AIC/BIC; và chứng minh K-Means là trường hợp giới hạn của GMM.

---

## 🎯 Mục tiêu bài học

1. **Hiểu rõ triết lý Học không giám sát:** Khám phá tri thức tiềm ẩn từ dữ liệu chưa được dán nhãn (Unlabeled Data).
2. **Làm chủ quy trình K-Means & K-Means++:** Nắm vững giải thuật Lloyd gồm Khởi tạo $\to$ Gán cụm $\to$ Cập nhật tâm $\to$ Hội tụ; giải thích cơ chế phân phối xác suất $D(x)^2$ của K-Means++ giúp ngăn ngừa cực tiểu cục bộ.
3. **Ứng dụng thành thạo Phương pháp Khuỷu tay (Elbow Method):** Tính toán hai chỉ số **Distortion** và **Inertia**, vẽ đồ thị Elbow và xác định điểm gãy tối ưu để chọn số lượng cụm $K$.
4. **Làm chủ Phân cụm Phân cấp & Biểu đồ Dendrogram:** Hiểu rõ cơ chế xây dựng cây phân cấp lồng nhau không cần giả định $K$ ban đầu; đọc giải phẫu Dendrogram và áp dụng kỹ thuật cắt ngang qua nhánh dọc dài nhất.
5. **Nắm vững 5 tiêu chuẩn liên kết cụm (Linkage Criteria):** Single Linkage (và hiện tượng nối chuỗi Chaining Effect), Complete Linkage, Average Linkage, Centroid Linkage (và rủi ro Đảo ngược Inversion), cùng Ward's Minimum Variance Criterion.
6. **Làm chủ Phân cụm Dựa trên Mật độ (DBSCAN & OPTICS):** Nhận diện cụm phi cầu có hình dạng bất kỳ, tự động cô lập điểm nhiễu (Outliers); xác định $\epsilon$ bằng đồ thị K-Distance; giải mã Reachability Plot và phân cụm dữ liệu đa mật độ.
7. **Làm chủ Phân cụm Dựa trên Phân phối (GMM & EM):** Hiểu sâu mô hình phân cụm mềm (Soft Clustering), 2 bước luân phiên E-step và M-step của thuật toán EM, 4 dạng ma trận hiệp phương sai và kỹ thuật chọn $K$ bằng tiêu chuẩn thông tin BIC/AIC.
8. **Đánh giá và so sánh toàn diện 5 trường phái:** K-Means vs Hierarchical vs DBSCAN vs OPTICS vs GMM.
9. **Thực hành với Scikit-Learn, SciPy & NumPy:** Xây dựng mô hình K-Means, K-Means++, AgglomerativeClustering, DBSCAN, OPTICS, GaussianMixture, tự cài đặt thuật toán EM bằng NumPy thuần và ứng dụng tách nền video, phân khúc khách hàng.

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part07-clustering-algorithms-vn.pdf](part07-clustering-algorithms-vn.pdf) | `.pdf` | **Slide bài giảng Beamer**: Giới thiệu phân cụm, so sánh 5 trường phái thuật toán, cây quyết định và các chỉ số thẩm định (18 trang) |
| [part07-clustering-algorithms-vn.tex](part07-clustering-algorithms-vn.tex) | `.tex` | Mã nguồn LaTeX Beamer của bộ slide bài giảng phân cụm |
| [part07-clustering-practice-vn.ipynb](part07-clustering-practice-vn.ipynb) | `.ipynb` | **Jupyter Notebook Thực hành Toàn diện**: Tóm tắt lý thuyết & Cheatsheet, 4 bài toán tính tay chi tiết, trực quan hóa chuyên sâu (Voronoi, Dendrogram, K-Distance, GMM Elip), và 5 bài Lab điền khuyết kèm assert test tự động |
| [part07-introduction-to-data-segmentation.md](part07-introduction-to-data-segmentation.md) | `.md` | Bài giảng Tổng quan Phân khúc dữ liệu (Data Segmentation): Khái niệm, Phân loại vs Phân cụm, Quy trình phân khúc khách hàng, Phân tích RFM |
| [part07-clustering-machine-learning-vn.md](part07-clustering-machine-learning-vn.md) | `.md` | Bài giảng Tổng quan Phân cụm trong Machine Learning: Hard vs Soft, 5 phương pháp phân cụm (K-Means, DBSCAN, Hierarchical, GMM, FCM), Đánh giá Silhouette, Code Scikit-Learn & Hình ảnh minh họa |
| [part07-kmeans-elbow-kmeans-plus-plus-vn.md](part07-kmeans-elbow-kmeans-plus-plus-vn.md) | `.md` | Bài giảng Chuyên sâu Centroid-based Methods: K-Means (Lloyd), Khởi tạo thông minh K-Means++ ($O(\log K)$), Phương pháp Khuỷu tay (Elbow Method với Distortion/Inertia), K-Medoids & 8 hình ảnh minh họa |
| [part07-hierarchical-agglomerative-clustering-vn.md](part07-hierarchical-agglomerative-clustering-vn.md) | `.md` | Bài giảng Chuyên sâu Connectivity-based Methods: Hierarchical Clustering, Agglomerative (Bottom-Up) vs Divisive (Top-Down), Cấu trúc Dendrogram, 5 Linkage Criteria, CPCC, Code Scikit-Learn/SciPy & 13 hình ảnh minh họa |
| [part07-density-based-clustering-dbscan-optics-vn.md](part07-density-based-clustering-dbscan-optics-vn.md) | `.md` | Bài giảng Chuyên sâu Density-based Methods: DBSCAN (Epsilon, MinPts, Core/Border/Noise, K-Distance graph) & OPTICS (Core Distance, Reachability Distance, Reachability Plot, Xi-steep extraction), Code Scikit-Learn & 8 hình ảnh minh họa |
| [part07-distribution-based-clustering-gmm-em-vn.md](part07-distribution-based-clustering-gmm-em-vn.md) | `.md` | Bài giảng Chuyên sâu Distribution-based Methods: Gaussian Mixture Models (GMM), Thuật toán Expectation-Maximization (EM), Phân cụm mềm $\gamma_{nk}$, 4 Covariance Types, AIC/BIC, Code NumPy/Scikit-Learn & 9 hình ảnh minh họa |
| [part07-clustering-machine-learning.md](part07-clustering-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Clustering in Machine Learning |
| [part07-kmeans-elbow-kmeans-plus-plus.md](part07-kmeans-elbow-kmeans-plus-plus.md) | `.md` | Bản sao tiêu chuẩn bài học K-Means, K-Means++ & Elbow Method |
| [part07-hierarchical-agglomerative-clustering.md](part07-hierarchical-agglomerative-clustering.md) | `.md` | Bản sao tiêu chuẩn bài học Hierarchical & Agglomerative Clustering |
| [part07-density-based-clustering-dbscan-optics.md](part07-density-based-clustering-dbscan-optics.md) | `.md` | Bản sao tiêu chuẩn bài học DBSCAN & OPTICS |
| [part07-distribution-based-clustering-gmm-em.md](part07-distribution-based-clustering-gmm-em.md) | `.md` | Bản sao tiêu chuẩn bài học GMM & EM Algorithm |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Tất cả 41 hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):

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

### Nhóm 4: Density-based Clustering – DBSCAN & OPTICS (8 ảnh)
- `dbscan-density-concept.png`: Khái niệm lân cận Epsilon ($\epsilon$), ngưỡng mật độ MinPts và các vùng liên thông mật độ.
- `dbscan-core-border-noise.png`: Sơ đồ phân loại 3 nhóm điểm dữ liệu trong DBSCAN: Core Points, Border Points và Noise Points.
- `dbscan-density-connected.png`: Minh họa các quan hệ hình học: Tiếp cận trực tiếp theo mật độ, Tiếp cận theo mật độ và Liên thông mật độ.
- `dbscan-cluster-result.png`: Đồ thị kết quả phân cụm tự nhiên của DBSCAN trên tập dữ liệu tổng hợp.
- `dbscan-vs-kmeans-comparison.png`: Bảng so sánh trực quan 3x3 giữa K-Means (Centroid-based) và DBSCAN (Density-based) trên 3 hình thái dữ liệu thách thức (Moons, Circles, Blobs+Noise).
- `dbscan-k-distance-elbow.png`: Phương pháp Đồ thị K-Distance (K-NN Distance Plot) tìm điểm uốn (Knee/Elbow) xác định Epsilon ($\epsilon$) tối ưu.
- `optics-clustering-structure.png`: Minh họa cấu trúc phân cụm và trích xuất cụm của thuật toán OPTICS.
- `optics-reachability-multilevel.png`: Biểu đồ Khả năng tiếp cận (Reachability Plot) đa tầng, so sánh trích xuất tự động $\xi$ và các lát cắt $\epsilon$ phẳng.

### Nhóm 5: Distribution-based Clustering – GMM & EM Algorithm (9 ảnh)
- `gmm-distribution-concept.png`: Mô hình hỗn hợp Gauss tổng hợp từ các phân phối xác suất thành phần đa đỉnh.
- `gmm-clustering-visualization.png`: Phân tách tập dữ liệu thành các cụm thành phần Gauss trong không gian.
- `gmm-process-workflow.png`: Sơ đồ khối tổng thể chu trình huấn luyện GMM bằng thuật toán Expectation-Maximization.
- `em-expectation-step.png`: Cơ chế Bước E (Expectation Step) tính toán ma trận trách nhiệm hậu nghiệm $\gamma_{nk}$.
- `em-maximization-update.png`: Cơ chế Bước M (Maximization Step) cập nhật trọng số $\pi_k$, kỳ vọng $\mu_k$ và hiệp phương sai $\Sigma_k$.
- `em-density-components.png`: Đồ thị phân rã hàm mật độ xác suất của các thành phần sau khi hội tụ.
- `em-log-likelihood-convergence.png`: Đồ thị đường cong hội tụ đơn điệu tăng của hàm Log-Likelihood qua các epoch huấn luyện.
- `em-fitted-density-result.png`: So sánh đường cong mật độ lý thuyết ước lượng bởi GMM với biểu đồ tần suất (Histogram) thực nghiệm.
- `gmm-covariance-types.png`: Khảo sát trực quan 4 dạng ma trận hiệp phương sai (`spherical`, `diag`, `tied`, `full`) với các đường elip mức tin cậy $1\sigma, 2\sigma, 3\sigma$.

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Gaussian Mixture Model](https://www.geeksforgeeks.org/gaussian-mixture-model/)
- [GeeksforGeeks – Expectation-Maximization Algorithm - ML](https://www.geeksforgeeks.org/ml-expectation-maximization-algorithm/)
- [GeeksforGeeks – DBSCAN Clustering in ML - Density based clustering](https://www.geeksforgeeks.org/dbscan-clustering-in-ml-density-based-clustering/)
- [GeeksforGeeks – Ordering Points To Identify Cluster Structure (OPTICS) using Sklearn](https://www.geeksforgeeks.org/ordering-points-to-identify-cluster-structure-optics-using-sklearn/)
- [GeeksforGeeks – Hierarchical Clustering in Machine Learning](https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/)
- [Scikit-Learn Official User Guide – Gaussian Mixture Models](https://scikit-learn.org/stable/modules/mixture.html)
- [Dempster et al. (1977) – Maximum Likelihood from Incomplete Data via the EM Algorithm](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1977.tb01600.x)
- [Bishop, C. M. (2006) – Pattern Recognition and Machine Learning (Chapter 9: Mixture Models and EM)](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/)
