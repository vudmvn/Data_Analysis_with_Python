# Tuần 10: Supervised Machine Learning & Linear Regression

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 21 tháng 9 năm 2026

---

## 📌 Tổng quan tuần học

Tuần học này mở đầu chuyên đề **Học máy (Machine Learning)** trong phân tích dữ liệu kinh doanh và kinh tế số, tập trung vào mô hình học có giám sát (Supervised Learning) với hai bài toán cốt lõi: **Phân loại (Classification)** và **Hồi quy (Regression)**, đi sâu nghiên cứu thuật toán nền tảng **Hồi quy tuyến tính (Linear Regression)**.

---

## 🎯 Mục tiêu bài học

1. **Hiểu rõ nguyên lý:** Nắm vững cơ chế học từ dữ liệu có gán nhãn (Labeled Data) và tối thiểu hóa sai số hàm mất mát (Loss Minimization).
2. **Phân biệt hai dạng bài toán:**
   - **Classification:** Dự báo biến mục tiêu rời rạc (mua hàng / không mua, gian lận / hợp lệ, phân loại tế bào ung thư).
   - **Regression:** Dự báo biến mục tiêu liên tục (dự báo tốc độ gió, giá nhà, doanh thu).
3. **Quy trình 5 bước chuẩn:** Thu thập nhãn $\to$ Chia dữ liệu Train/Val/Test $\to$ Huấn luyện mô hình $\to$ Đánh giá chỉ số $\to$ Triển khai & Dự báo.
4. **Hệ thống thuật toán tiêu biểu:** Nắm vững và so sánh 8 thuật toán kinh điển: Linear Regression, Logistic Regression, Decision Trees, Random Forests, SVM, KNN, Gradient Boosting, và Naive Bayes.
5. **Chuyên sâu Linear Regression:**
   - Đường hồi quy phù hợp nhất (Best-Fit Line), Phần dư (Residuals) và phương pháp Bình phương tối thiểu (OLS).
   - Tối ưu hóa hàm chi phí (MSE) bằng thuật toán Gradient Descent.
   - Hồi quy đơn biến (Simple) và Hồi quy đa biến (Multiple).
   - Kiểm định 7 giả định nền tảng (Linearity, Homoscedasticity, Normality, Multicollinearity, v.v.).
   - Đo lường hiệu năng ($MAE, MSE, RMSE, R^2, R^2_{\text{adj}}$) và các kỹ thuật điều chuẩn (Ridge $L_2$, Lasso $L_1$, Elastic Net).
6. **Thực hành với Scikit-Learn:** Xây dựng pipeline xử lý dữ liệu và huấn luyện mô hình dự báo hoàn chỉnh bằng Python.

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part08-supervised-machine-learning-vn.md](part08-supervised-machine-learning-vn.md) | `.md` | Bài giảng Tổng quan Supervised Machine Learning: Khái niệm, Phân loại vs Hồi quy, Pipeline 5 bước, 8 thuật toán, Ứng dụng & Code mẫu Scikit-Learn |
| [part08-linear-regression-vn.md](part08-linear-regression-vn.md) | `.md` | Bài giảng Chuyên sâu Hồi quy Tuyến tính (Linear Regression): Best-Fit Line, OLS, Gradient Descent, 7 Giả định, Đo lường, Điều chuẩn Ridge/Lasso, Code Scikit-Learn & 9 hình ảnh minh họa |
| [part08-supervised-machine-learning.md](part08-supervised-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Supervised Learning |
| [part08-linear-regression.md](part08-linear-regression.md) | `.md` | Bản sao tiêu chuẩn bài học Linear Regression |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Tất cả các hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):
- `introduction-to-linear-regression.png`: Sơ đồ khái niệm biến phụ thuộc $Y$ và biến độc lập $X$.
- `how-linear-regression-works.png`: Đường hồi quy phù hợp nhất (Best-Fit Line).
- `observed-value-residual-error.png`: Giá trị quan sát, giá trị dự báo và phần dư.
- `gradient-descent-cost-function.png`: Mặt cong hàm chi phí và các bước hạ độ dốc.
- `types-of-linear-regression.png`: Phân loại hồi quy đơn biến vs đa biến.
- `linearity-assumption.png`: Minh họa giả định tính tuyến tính.
- `homoscedasticity-assumption.png`: So sánh Homoscedasticity vs Heteroscedasticity.
- `challenges-in-linear-regression.png`: Các thách thức và bẫy sai lầm thường gặp.
- `real-world-use-cases.png`: 5 lĩnh vực ứng dụng kinh doanh thực tế.

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Supervised Machine Learning](https://www.geeksforgeeks.org/machine-learning/supervised-machine-learning/)
- [GeeksforGeeks – Linear Regression in Machine Learning](http://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)
- [Scikit-Learn Official User Guide](https://scikit-learn.org/stable/supervised_learning.html)
