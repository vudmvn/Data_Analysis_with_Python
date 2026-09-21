# Tuần 08–09: Data Segmentation & Clustering in Machine Learning (Phân khúc & Phân cụm Dữ liệu)

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 22 tháng 9 năm 2026

---

## 📌 Tổng quan chuyên đề

Chuyên đề này cung cấp kiến thức nền tảng và chuyên sâu về **Học không giám sát (Unsupervised Machine Learning)**, tập trung vào hai mảng kiến thức trụ cột:
1. **Phân khúc dữ liệu (Data Segmentation):** Bản chất phân khúc khách hàng, thị trường và sản phẩm; phân biệt giữa Segmentation, Data Partitioning và Targeting; quy trình xây dựng bài toán phân khúc trong doanh nghiệp.
2. **Phân cụm dữ liệu (Clustering in Machine Learning):** Khám phá cấu trúc tự nhiên của dữ liệu chưa gán nhãn; 5 phương pháp phân cụm cốt lõi (Centroid-based, Density-based, Hierarchical, Distribution-based, Fuzzy); các chỉ số đánh giá chất lượng phân cụm (Silhouette, WCSS, Davies-Bouldin); và ứng dụng thực tiễn trong phân tích kinh doanh.

---

## 🎯 Mục tiêu bài học

1. **Hiểu rõ triết lý Học không giám sát:** Khám phá tri thức tiềm ẩn từ dữ liệu chưa được dán nhãn (Unlabeled Data).
2. **Làm chủ 5 phương pháp phân cụm cốt lõi:**
   - **Centroid-based (K-Means & K-Medoids):** Dựa trên tâm cụm và cực tiểu hóa khoảng cách bình phương nội cụm.
   - **Density-based (DBSCAN & OPTICS):** Dựa trên mật độ lân cận $(\epsilon, \text{MinPts})$, nhận diện cụm hình dạng bất kỳ và tự lọc nhiễu.
   - **Hierarchical (Agglomerative & Divisive):** Xây dựng cây phân cấp Dendrogram và quan sát quan hệ đa tầng.
   - **Distribution-based (GMM):** Phân phối hỗn hợp Gauss nhiều chiều với thuật toán EM.
   - **Fuzzy Clustering (FCM):** Phân cụm mờ với mức độ thành viên mượt mà.
3. **Phân biệt Hard Clustering vs Soft Clustering:** Nắm vững ranh giới giữa việc gán dứt khoát 1 điểm vào 1 nhóm và việc mô hình hóa xác suất thành viên đa cụm.
4. **Đánh giá chất lượng phân cụm khoa học:**
   - Đánh giá nội tại: Phương pháp Khuỷu tay (Elbow Method với WCSS), Hệ số Silhouette (Silhouette Score), Chỉ số Davies-Bouldin, Calinski-Harabasz.
   - Đánh giá ngoại tại: Adjusted Rand Index (ARI), Normalized Mutual Information (NMI).
5. **Thực hành với Scikit-Learn & NumPy:** Tự cài đặt K-Means từ đầu bằng NumPy, thực hiện phân khúc khách hàng đa biến (Customer Segmentation) và khảo sát ảnh hưởng của việc chuẩn hóa thang đo (`StandardScaler`).

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part07-introduction-to-data-segmentation.md](part07-introduction-to-data-segmentation.md) | `.md` | Bài giảng Tổng quan Phân khúc dữ liệu (Data Segmentation): Khái niệm, Phân loại vs Phân cụm, Quy trình phân khúc khách hàng, Phân tích RFM |
| [part07-clustering-machine-learning-vn.md](part07-clustering-machine-learning-vn.md) | `.md` | Bài giảng Chuyên sâu Phân cụm trong Machine Learning: Hard vs Soft, 5 phương pháp phân cụm (K-Means, DBSCAN, Hierarchical, GMM, FCM), Đánh giá Silhouette, Code Scikit-Learn & Hình ảnh minh họa |
| [part07-clustering-machine-learning.md](part07-clustering-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Clustering in Machine Learning |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Các hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):
- `clustering-overview.png`: Sơ đồ khái niệm phân cụm dữ liệu chưa gán nhãn thành 3 cụm riêng biệt.
- `hard-vs-soft-clustering.png`: So sánh đối chiếu trực quan giữa Phân cụm cứng (Hard Clustering) và Phân cụm mờ/mềm (Soft Clustering).
- `centroid-based-kmeans.png`: Minh họa cơ chế dịch chuyển tâm cụm (Centroids) và gom nhóm thành viên của K-Means.

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Clustering in Machine Learning](https://www.geeksforgeeks.org/machine-learning/clustering-in-machine-learning/)
- [Scikit-Learn Official User Guide – Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [Hastie, Tibshirani & Friedman – The Elements of Statistical Learning (Chapter 14: Unsupervised Learning)](https://hastie.su.domains/ElemStatLearn/)
