# Tuần 10–14: Supervised Machine Learning, Linear Regression, Logistic Regression, Decision Trees, Random Forest, SVM, KNN & Naive Bayes

**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Giảng viên:** TS. Vũ Đức Minh – Khoa Khoa học dữ liệu và Trí tuệ nhân tạo (NEU)  
**Cập nhật lần cuối:** 22 tháng 9 năm 2026

---

## 📌 Tổng quan chuyên đề

Chuyên đề này bao quát toàn bộ nền tảng **Học máy có giám sát (Supervised Machine Learning)** trong phân tích dữ liệu kinh doanh và kinh tế số, đi sâu nghiên cứu toàn bộ 8 thuật toán kinh điển:
1. **Tổng quan Học có giám sát (Supervised ML Overview):** Khái niệm, Phân loại vs Hồi quy, Pipeline 5 bước, và 8 thuật toán tiêu biểu.
2. **Hồi quy tuyến tính (Linear Regression):** Dự báo biến mục tiêu liên tục, phương pháp OLS, Gradient Descent, 7 giả định Gauss-Markov và điều chuẩn Ridge/Lasso.
3. **Hồi quy Logistic (Logistic Regression):** Dự báo biến mục tiêu phân loại nhị phân và đa lớp, chuyển đổi xác suất qua hàm Sigmoid và Softmax, tối ưu bằng Ước lượng Hợp lý Cực đại (MLE).
4. **Cây quyết định (Decision Trees):** Phân chia đệ quy theo các quy tắc logic *if-else*, đo lường độ thuần khiết qua Entropy, Information Gain, Gini Impurity, và kỹ thuật cắt tỉa cây chống quá khớp.
5. **Hồi quy Rừng ngẫu nhiên (Random Forest Regression):** Phương pháp học máy kết hợp (Ensemble Learning), kỹ thuật Bagging (Bootstrap Aggregation), không gian con đặc trưng ngẫu nhiên (Random Subspace), đánh giá Out-of-Bag (OOB), và hàm dự báo bậc thang phi tuyến.
6. **Máy vector hỗ trợ (Support Vector Machine - SVM):** Tối ưu hóa siêu phẳng phân tách với lề cực đại (Maximal Margin), xử lý nhiễu bằng Lề mềm (Soft Margin, tham số $C$, Hinge Loss), và Bí quyết Kernel (Kernel Trick: Linear, RBF, Polynomial) trong không gian chiều cao.
7. **Thuật toán K láng giềng gần nhất (K-Nearest Neighbors - KNN):** Phương pháp học dựa trên cá thể (Instance-based Learning), giải thuật học lười (Lazy Learner), các độ đo khoảng cách (Euclidean, Manhattan, Minkowski, Cosine), kỹ thuật trọng số khoảng cách và đối phó với Lời nguyền số chiều (Curse of Dimensionality).
8. **Bộ phân loại Naive Bayes (Naive Bayes Classifiers):** Mô hình xác suất tạo sinh (Generative Model), Định lý Bayes, giả định độc lập có điều kiện, kỹ thuật làm mịn Laplace (Laplace Smoothing), chống tràn số dưới qua Log-Likelihood, và các biến thể GaussianNB, MultinomialNB, BernoulliNB.

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
7. **Chuyên sâu Random Forest Regression:**
   - Nguyên lý Bagging và Random Subspace giúp triệt tiêu phương sai mà không làm tăng độ chệch.
   - Bản chất toán học xác suất của tập mẫu Out-of-Bag ($1/e \approx 36.8\%$) và kiểm định OOB Score.
   - Đo lường độ quan trọng của đặc trưng (Feature Importance) qua MDI và PFI.
   - Trực quan hóa đường cong bậc thang phân giải cao và phân tích cấu trúc cây con với `plot_tree`.
8. **Chuyên sâu Support Vector Machine (SVM):**
   - Hình học siêu phẳng $w^Tx + b = 0$, Support Vectors, và độ rộng lề $2/\|w\|$.
   - Lề cứng (Hard Margin) vs Lề mềm (Soft Margin với $\zeta_i$ và tham số phạt $C$).
   - Cơ chế hàm mất mát Hinge Loss $\max(0, 1 - yf(x))$.
   - Bí quyết Kernel (Kernel Trick) ánh xạ phi tuyến lên không gian chiều cao không qua tính tọa độ tường minh (Linear, RBF/Gaussian, Polynomial).
   - Phân loại đa lớp OvR, OvO và vai trò tối thượng của chuẩn hóa thang đo (`StandardScaler`).
9. **Chuyên sâu K-Nearest Neighbors (KNN):**
   - Nguyên lý học dựa trên mẫu (Instance-based), giải thuật học lười (Lazy Learner).
   - Các độ đo khoảng cách hình học: Euclidean ($L_2$), Manhattan ($L_1$), Minkowski ($L_p$), Cosine, Hamming.
   - Đánh đổi Bias-Variance qua siêu tham số $K$, phương pháp Elbow và chọn số lẻ tránh hòa phiếu.
   - Trọng số theo khoảng cách (Distance-Weighted KNN) và kiểm soát Lời nguyền số chiều (Curse of Dimensionality).
10. **Chuyên sâu Naive Bayes:**
    - Cấu trúc Định lý Bayes: Prior, Likelihood, Evidence, Posterior.
    - Giả định độc lập có điều kiện và quy tắc Maximum A Posteriori (MAP).
    - Khắc phục hiện tượng Zero Probability bằng kỹ thuật Làm mịn Laplace ($\alpha=1$).
    - 4 biến thể chuyên dụng: GaussianNB, MultinomialNB, BernoulliNB, ComplementNB.
11. **Thực hành với Scikit-Learn:** Xây dựng pipeline xử lý dữ liệu và huấn luyện mô hình phân loại & hồi quy hoàn chỉnh bằng Python.

---

## 📚 Danh mục tài liệu học tập

| Tệp tài liệu | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| [part08-supervised-machine-learning-vn.md](part08-supervised-machine-learning-vn.md) | `.md` | Bài giảng Tổng quan Supervised Machine Learning: Khái niệm, Phân loại vs Hồi quy, Pipeline 5 bước, 8 thuật toán, Ứng dụng & Code mẫu Scikit-Learn |
| [part08-linear-regression-vn.md](part08-linear-regression-vn.md) | `.md` | Bài giảng Chuyên sâu Hồi quy Tuyến tính (Linear Regression): Best-Fit Line, OLS, Gradient Descent, 7 Giả định, Đo lường, Điều chuẩn Ridge/Lasso, Code Scikit-Learn & 9 hình ảnh minh họa |
| [part08-logistic-regression-vn.md](part08-logistic-regression-vn.md) | `.md` | Bài giảng Chuyên sâu Hồi quy Logistic (Logistic Regression): Sigmoid, Odds, Logit, MLE, Log Loss, Softmax đa lớp, Ma trận nhầm lẫn, ROC-AUC & 4 hình ảnh minh họa |
| [part08-decision-tree-vn.md](part08-decision-tree-vn.md) | `.md` | Bài giảng Chuyên sâu Cây Quyết định (Decision Tree): Cấu trúc cây, Entropy, Information Gain, Gini Impurity, CART, Cắt tỉa Pruning, Code Scikit-Learn & 7 hình ảnh minh họa |
| [part08-random-forest-regression-vn.md](part08-random-forest-regression-vn.md) | `.md` | Bài giảng Chuyên sâu Hồi quy Rừng ngẫu nhiên (Random Forest Regression): Bagging, Feature Randomness, OOB Score ($36.8\%$), Feature Importance, Code Scikit-Learn Position Salaries & 4 hình ảnh minh họa |
| [part08-support-vector-machine-vn.md](part08-support-vector-machine-vn.md) | `.md` | Bài giảng Chuyên sâu Máy Vector Hỗ trợ (Support Vector Machine - SVM): Hyperplane, Support Vectors, Lề cứng/mềm, Hinge Loss, Kernel Trick (RBF/Poly), Code Scikit-Learn Breast Cancer & 9 hình ảnh minh họa |
| [part08-knn-vn.md](part08-knn-vn.md) | `.md` | Bài giảng Chuyên sâu K Láng giềng Gần nhất (K-Nearest Neighbors - KNN): Lazy Learner, Độ đo khoảng cách Euclidean/Manhattan, Lựa chọn $K$, Trọng số khoảng cách, Lời nguyền số chiều, Code Scikit-Learn & 4 hình ảnh minh họa |
| [part08-naive-bayes-vn.md](part08-naive-bayes-vn.md) | `.md` | Bài giảng Chuyên sâu Thuật toán Naive Bayes: Định lý Bayes, Giả định độc lập, Bài toán thời tiết Play Golf, Làm mịn Laplace, Phân loại văn bản NLP với MultinomialNB, GaussianNB & 10 hình ảnh minh họa |
| [part08-supervised-machine-learning.md](part08-supervised-machine-learning.md) | `.md` | Bản sao tiêu chuẩn bài học Supervised Learning |
| [part08-linear-regression.md](part08-linear-regression.md) | `.md` | Bản sao tiêu chuẩn bài học Linear Regression |
| [part08-logistic-regression.md](part08-logistic-regression.md) | `.md` | Bản sao tiêu chuẩn bài học Logistic Regression |
| [part08-decision-tree.md](part08-decision-tree.md) | `.md` | Bản sao tiêu chuẩn bài học Decision Tree |
| [part08-random-forest-regression.md](part08-random-forest-regression.md) | `.md` | Bản sao tiêu chuẩn bài học Random Forest Regression |
| [part08-support-vector-machine.md](part08-support-vector-machine.md) | `.md` | Bản sao tiêu chuẩn bài học Support Vector Machine |
| [part08-knn.md](part08-knn.md) | `.md` | Bản sao tiêu chuẩn bài học K-Nearest Neighbors |
| [part08-naive-bayes.md](part08-naive-bayes.md) | `.md` | Bản sao tiêu chuẩn bài học Naive Bayes Classifiers |

---

## 🖼️ Thư mục hình ảnh minh họa (`images/`)

Tất cả 47 hình ảnh sơ đồ toán học và biểu đồ minh họa được chuẩn hóa định dạng `.png` và lưu trữ tại thư mục [`images/`](images/):

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

### Nhóm 4: Hồi quy Rừng ngẫu nhiên (Random Forest Regression - 4 ảnh)
- `random-forest-regression-concept.png`: Sơ đồ khái niệm kiến trúc tổng thể nhiều cây con và cơ chế trung bình hóa dự báo.
- `random-forest-architecture.png`: Kiến trúc chi tiết quy trình lấy mẫu Bootstrap Aggregating (Bagging) và Random Subspace.
- `random-forest-regression-plot.png`: Đồ thị thực nghiệm hồi quy phi tuyến trên dữ liệu mức lương theo cấp bậc (Position Salaries).
- `random-forest-prediction-curve.png`: Đường cong hàm dự báo bậc thang phân giải cao (High-Resolution Grid Prediction Curve).

### Nhóm 5: Máy Vector Hỗ trợ (Support Vector Machine - 9 ảnh)
- `svm-what-is-svm.png`: Sơ đồ tổng quan giải thuật SVM và mục tiêu phân tách lớp.
- `svm-support-vectors-hyperplane.png`: Mô hình hóa Hyperplane, Support Vectors và khoảng cách Margin.
- `svm-linear-vs-non-linear-svm.png`: So sánh đối chiếu giữa Linear SVM và Non-Linear SVM.
- `svm-multiple-hyperplanes.png`: Minh họa nhiều siêu phẳng phân tách tiềm năng và việc chọn siêu phẳng có lề cực đại.
- `svm-outlier-scenario.png`: Tình huống dữ liệu thực tế có điểm ngoại lai (Outlier) vi phạm biên.
- `svm-optimized-soft-margin.png`: Tối ưu hóa siêu phẳng với cơ chế lề mềm (Soft Margin).
- `svm-1d-nonlinear-data.png`: Tập dữ liệu 1D phi tuyến không thể phân tách bằng một điểm cắt.
- `svm-kernel-trick-transformation.png`: Ánh xạ dữ liệu lên không gian 2D để phân tách tuyến tính qua Kernel Trick.
- `svm-breast-cancer-decision-boundary.png`: Trực quan hóa ranh giới quyết định phân loại ung thư vú bằng Scikit-Learn.

### Nhóm 6: K Láng giềng Gần nhất (K-Nearest Neighbors - 4 ảnh)
- `knn-concept-decision.png`: Sơ đồ khái niệm ra quyết định phân loại dựa trên khoảng cách láng giềng gần nhất.
- `knn-initial-data.png`: Biểu diễn tập dữ liệu ban đầu trong không gian 2 chiều trước khi truy vấn.
- `knn-calculate-distance.png`: Quy trình tính toán khoảng cách từ điểm truy vấn tới toàn bộ tập dữ liệu huấn luyện.
- `knn-voting-labels.png`: Xác định $K$ láng giềng gần nhất và quy trình bỏ phiếu bầu chọn nhãn lớp.

### Nhóm 7: Phân loại Naive Bayes (Naive Bayes Classifiers - 10 ảnh)
- `nb-original-data.png`: Tập dữ liệu phân loại 2 lớp ban đầu trong không gian 2 chiều.
- `nb-estimation-dim1.png`: Ước lượng phân phối xác suất riêng biệt dọc theo chiều thứ nhất $P(x_1 \mid y)$.
- `nb-estimation-dim2.png`: Ước lượng phân phối xác suất riêng biệt dọc theo chiều thứ hai $P(x_2 \mid y)$.
- `nb-resulting-distribution.png`: Phân phối xác suất kết hợp trong không gian 2D dựa trên giả định độc lập.
- `nb-table-outlook.png`: Bảng phân phối tần suất và xác suất có điều kiện cho đặc trưng Outlook.
- `nb-table-temperature.png`: Bảng phân phối tần suất và xác suất có điều kiện cho đặc trưng Temperature.
- `nb-table-humidity.png`: Bảng phân phối tần suất và xác suất có điều kiện cho đặc trưng Humidity.
- `nb-table-wind.png`: Bảng phân phối tần suất và xác suất có điều kiện cho đặc trưng Wind.
- `nb-probability-summary.png`: Bảng tổng hợp các xác suất thành phần phục vụ suy luận bài toán Play Golf.
- `nb-gaussian-bell-curve.png`: Đường cong phân phối chuẩn Gaussian cho biến số liên tục trong GaussianNB.

---

## 🔗 Nguồn tham khảo chính

- [GeeksforGeeks – Supervised Machine Learning](https://www.geeksforgeeks.org/machine-learning/supervised-machine-learning/)
- [GeeksforGeeks – Linear Regression in Machine Learning](http://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)
- [GeeksforGeeks – Understanding Logistic Regression](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/)
- [GeeksforGeeks – Decision Tree in Machine Learning](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/)
- [GeeksforGeeks – Random Forest Regression in Python](https://www.geeksforgeeks.org/machine-learning/random-forest-regression-in-python/)
- [GeeksforGeeks – Support Vector Machine Algorithm](https://www.geeksforgeeks.org/machine-learning/support-vector-machine-algorithm/)
- [GeeksforGeeks – K-Nearest Neighbors Algorithm](https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/)
- [GeeksforGeeks – Naive Bayes Classifiers](https://www.geeksforgeeks.org/machine-learning/naive-bayes-classifiers/)
- [Scikit-Learn Official User Guide](https://scikit-learn.org/stable/supervised_learning.html)
