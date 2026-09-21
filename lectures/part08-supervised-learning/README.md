# Tuần 10–13: Supervised Machine Learning, Linear Regression, Logistic Regression & Decision Trees

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 21 tháng 9 năm 2026

---

## 📌 Tổng quan chuyên đề

Chuyên đề này bao quát toàn bộ nền tảng **Học máy có giám sát (Supervised Machine Learning)** trong phân tích dữ liệu kinh doanh và kinh tế số, đi sâu nghiên cứu ba trụ cột thuật toán cốt lõi:
1. **Tổng quan Học có giám sát (Supervised ML Overview):** Khái niệm, Phân loại vs Hồi quy, Pipeline 5 bước, và 8 thuật toán tiêu biểu.
2. **Hồi quy tuyến tính (Linear Regression):** Dự báo biến mục tiêu liên tục, phương pháp OLS, Gradient Descent, 7 giả định Gauss-Markov và điều chuẩn Ridge/Lasso.
3. **Hồi quy Logistic (Logistic Regression):** Dự báo biến mục tiêu phân loại nhị phân và đa lớp, chuyển đổi xác suất qua hàm Sigmoid và Softmax, tối ưu bằng Ước lượng Hợp lý Cực đại (MLE).
4. **Cây quyết định (Decision Trees):** Phân chia đệ quy theo các quy tắc logic *if-else*, đo lường độ thuần khiết qua Entropy, Information Gain, Gini Impurity, và kỹ thuật cắt tỉa cây chống quá khớp.

---

## 🎯 Mục tiêu bài học

1. **Hiểu rõ nguyên lý:** Nắm vững cơ chế học từ dữ liệu có gán nhãn (Labeled Data) và tối thiểu hóa sai số hàm mất mát (Loss Minimization).
2. **Phân biệt hai dạng bài toán:**
   - **Classification:** Dự báo biến mục tiêu rời rạc (mua hàng / không mua, gian lận / hợp lệ, phân loại tế bào ung thư).
   - **Regression:** Dự báo biến mục tiêu liên tục (dự báo tốc độ gió, giá nhà, doanh thu).
3. **Quy trình 5 bước chuẩn:** Thu thập nhãn $\to$ Chia dữ liệu Train/Val/Test $\to$ Huấn luyện mô hình $\to$ Đánh giá chỉ số $\to$ Triển khai & Dự báo.
4. **Chuyên sâu Linear Regression:**
   - Đường hồi quy phù hợp nhất (Best-Fit Line), Phần dư (Residuals) và phương pháp Bình phương tối thiểu (OLS).
   - Tối ưu hóa hàm chi phí (MSE) bằng thuật toán Gradient Descent.
   - Hồi quy đơn biến (Simple) và Hồi quy đa biến (Multiple).
   - Kiểm định 7 giả định nền tảng (Linearity, Homoscedasticity, Normality, Multicollinearity, v.v.).
   - Đo lường hiệu năng ($MAE, MSE, RMSE, R^2, R^2_{\text{adj}}$) và các kỹ thuật điều chuẩn (Ridge $L_2$, Lasso $L_1$, Elastic Net).
5. **Chuyên sâu Logistic Regression:**
   - Hàm Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$ và chuyển đổi xác suất.
   - Tỷ số Khả dĩ (Odds), hàm Logit $\ln(p / (1-p))$ và ý nghĩa hệ số $w_j$.
   - Ước lượng Hợp lý Cực đại (MLE) và hàm mất mát Binary Cross-Entropy (Log Loss).
   - 3 phân loại: Binomial (Nhị phân), Multinomial (Đa lớp với Softmax) và Ordinal (Thứ bậc).
   - Đánh giá mô hình qua Ma trận nhầm lẫn (Confusion Matrix), Precision, Recall, F1-Score, ROC-AUC và PR-AUC.
6. **Chuyên sâu Decision Trees:**
   - Cấu trúc cây: Nút gốc (Root), Nút quyết định (Decision Node), Nhánh (Branch), Nút lá (Leaf).
   - Tiêu chuẩn phân chia: Entropy, Information Gain (ID3), Gini Impurity (CART), và Variance Reduction (Hồi quy).
   - Khắc phục hiện tượng Quá khớp (Overfitting) qua Cắt tỉa sớm (Pre-pruning) và Cắt tỉa sau (Post-pruning / `ccp_alpha`).
7. **Thực hành với Scikit-Learn:** Xây dựng pipeline xử lý dữ liệu và huấn luyện mô hình phân loại & hồi quy hoàn chỉnh bằng Python.

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part08-supervised-machine-learning-vn.md](part08-supervised-machine-learning-vn.md) | `.md` | Bài giảng Tổng quan Supervised Machine Learning: Khái niệm, Phân loại vs Hồi quy, Pipeline 5 bước, 8 thuật toán, Ứng dụng & Code mẫu Scikit-Learn |
| [part08-linear-regression-vn.md](part08-linear-regression-vn.md) | `.md` | Bài giảng Chuyên sâu Hồi quy Tuyến tính (Linear Regression): Best-Fit Line, OLS, Gradient Descent, 7 Giả định, Đo lường, Điều chuẩn Ridge/Lasso, Code Scikit-Learn & 9 hình ảnh minh họa |
| [part08-logistic-regression-vn.md](part08-logistic-regression-vn.md) | `.md` | Bài giảng Chuyên sâu Hồi quy Logistic (Logistic Regression): Sigmoid, Odds, Logit, MLE, Log Loss, Softmax đa lớp, Ma trận nhầm lẫn, ROC-AUC & 4 hình ảnh minh họa |
| [part08-decision-tree-vn.md](part08-decision-tree-vn.md) | `.md` | Bài giảng Chuyên sâu Cây Quyết định (Decision Tree): Cấu trúc cây, Entropy, Information Gain, Gini Impurity, CART, Cắt tỉa Pruning, Code Scikit-Learn & 7 hình ảnh minh họa |
| [part08-supervised-machine-learning.md](part08-supervised-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Supervised Learning |
| [part08-linear-regression.md](part08-linear-regression.md) | `.md` | Bản sao tiêu chuẩn bài học Linear Regression |
| [part08-logistic-regression.md](part08-logistic-regression.md) | `.md` | Bản sao tiêu chuẩn bài học Logistic Regression |
| [part08-decision-tree.md](part08-decision-tree.md) | `.md` | Bản sao tiêu chuẩn bài học Decision Tree |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Tất cả 20 hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):

### Nhóm 1: Hồi quy tuyến tính (Linear Regression - 9 ảnh)
- `introduction-to-linear-regression.png`: Sơ đồ khái niệm biến phụ thuộc $Y$ và biến độc lập $X$.
- `how-linear-regression-works.png`: Đường hồi quy phù hợp nhất (Best-Fit Line).
- `observed-value-residual-error.png`: Giá trị quan sát, giá trị dự báo và phần dư.
- `gradient-descent-cost-function.png`: Mặt cong hàm chi phí và các bước hạ độ dốc.
- `types-of-linear-regression.png`: Phân loại hồi quy đơn biến vs đa biến.
- `linearity-assumption.png`: Minh họa giả định tính tuyến tính.
- `homoscedasticity-assumption.png`: So sánh Homoscedasticity vs Heteroscedasticity.
- `challenges-in-linear-regression.png`: Các thách thức và bẫy sai lầm thường gặp.
- `real-world-use-cases.png`: 5 lĩnh vực ứng dụng kinh doanh thực tế.

### Nhóm 2: Hồi quy Logistic (Logistic Regression - 4 ảnh)
- `logistic-regression-overview.png`: Tổng quan mô hình phân loại Logistic Regression.
- `what-is-logistic-regression.png`: Đường cong chữ S (Sigmoid Curve) nén miền xác suất $[0, 1]$.
- `logistic-regression-vs-linear-regression.png`: So sánh trực quan giữa Linear Regression và Logistic Regression.
- `types-of-logistic-regression.png`: 3 phân loại: Binomial, Multinomial và Ordinal.

### Nhóm 3: Cây quyết định (Decision Trees - 7 ảnh)
- `decision-tree-structure.png`: Cấu trúc phân cấp hình cây (Root, Decision Nodes, Branches, Leaves).
- `decision-tree-overview.png`: Tổng quan mô hình ra quyết định.
- `working-of-decision-tree.png`: Quy trình phân tách dữ liệu từng bước.
- `splitting-criteria-decision-tree.png`: Các tiêu chuẩn phân chia: Entropy, Information Gain, Gini Index.
- `customer-purchase-scenario.png`: Kịch bản phân loại ý định mua sắm của khách hàng.
- `customer-demographics-tree.png`: Cây quyết định kết hợp thuộc tính nhân khẩu học và hành vi.
- `applications-of-decision-trees.png`: Các lĩnh vực ứng dụng thực tiễn của Decision Trees.

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Supervised Machine Learning](https://www.geeksforgeeks.org/machine-learning/supervised-machine-learning/)
- [GeeksforGeeks – Linear Regression in Machine Learning](http://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)
- [GeeksforGeeks – Understanding Logistic Regression](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/)
- [GeeksforGeeks – Decision Tree in Machine Learning](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/)
- [Scikit-Learn Official User Guide](https://scikit-learn.org/stable/supervised_learning.html)
