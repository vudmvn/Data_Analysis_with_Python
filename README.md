# 🐍 DSAI1005 – Phân tích dữ liệu với Python (Data Analysis with Python)

> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)  
> **Đơn vị phụ trách:** Khoa Khoa học dữ liệu và Trí tuệ nhân tạo – Trường Đại học Kinh tế Quốc dân (NEU)  
> **Chương trình đào tạo:** Data Science in Finance and E-commerce (EP15)  
> **Số tín chỉ:** 3 Tín chỉ (30h lý thuyết, 15h thực hành, 90h tự học)  

---

## 📌 1. Giới thiệu Học phần & Mục tiêu

Học phần **Phân tích dữ liệu với Python (DSAI1005)** cung cấp kiến thức nhập môn có hệ thống về Khoa học dữ liệu và Phân tích dữ liệu kinh doanh. Sinh viên được trang bị kỹ năng sử dụng thành thạo hệ sinh thái Python bao gồm **NumPy, Pandas, Matplotlib, Seaborn, Bokeh, SciPy, SQLite, PyMongo và Scikit-learn**.

### 🎯 Mục tiêu & Chuẩn đầu ra (CLOs):
1. **Công cụ & Môi trường:** Thành thạo Anaconda, Python, JupyterLab và quản lý môi trường ảo.
2. **Đại số tuyến tính & Thống kê:** Tính toán ma trận, vector và phân tích thống kê với NumPy & SciPy.
3. **Thao tác Dữ liệu:** Đọc, làm sạch, biến đổi, chuẩn hóa và xử lý missing values/outliers bằng Pandas.
4. **Trực quan hóa:** Xây dựng biểu đồ mô tả & biểu đồ tương tác với Matplotlib, Seaborn, Bokeh.
5. **Cơ sở dữ liệu:** Truy xuất và lưu trữ dữ liệu từ CSV, Excel, JSON, SQL (MySQL/SQLite) & NoSQL (MongoDB).
6. **Mô hình hóa:** Áp dụng thuật toán Phân cụm (K-Means), Hồi quy (Linear/Logistic) & Phân loại (SVM, Decision Tree, Random Forest).

---

## 📚 2. Ma trận Bài giảng, Tài liệu & Bài tập Thực hành (Course Portal Matrix)

Bảng dưới đây tổng hợp chi tiết tài liệu học tập, bài giảng Notebook, slide, bài tập thực hành, tệp dữ liệu và đáp án cho **15 tuần học**:

| Tuần | Chủ đề chính | Bài giảng & Bài đọc (.md / .ipynb) | Slide | Bài tập Lab | Đáp án | Tài nguyên (Data / Images) | Trạng thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **Tuần 01** | **Giới thiệu học phần** | [📘 Notebook](lectures/week-01-gioi-thieu-hoc-phan/lecture.ipynb)<br>[Phan Tich Du Lieu La Gi](lectures/week-01-gioi-thieu-hoc-phan/phan_tich_du_lieu_la_gi.md) | [📊 Slides](lectures/week-01-gioi-thieu-hoc-phan/slides.md) | [💻 Lab](lectures/week-01-gioi-thieu-hoc-phan/lab_exercise.ipynb) | [🔑 Đáp án](lectures/week-01-gioi-thieu-hoc-phan/lab_solution.ipynb) | [📁 Data](lectures/week-01-gioi-thieu-hoc-phan/data/) | [🖼️ Images](lectures/week-01-gioi-thieu-hoc-phan/images/) | ✅ *Đã sẵn sàng* |
| **Tuần 02** | Thư viện tính toán NumPy | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 03** | Thư viện thao tác dữ liệu Pandas | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 04** | Khám phá & Trực quan hóa dữ liệu | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 05** | Truy xuất & Lưu trữ dữ liệu | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 06** | Làm sạch & Tiền xử lý dữ liệu | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 07** | Thi giữa kỳ | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 08** | Phân khúc & Phân cụm dữ liệu (Phần 1) | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 09** | Phân khúc & Phân cụm dữ liệu (Phần 2) | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 10** | Dự báo dữ liệu & Hồi quy tuyến tính (Phần 1) | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 11** | Dự báo dữ liệu & Hồi quy tuyến tính (Phần 2) | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 12** | Hồi quy phi tuyến & Classification Pipeline | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 13** | Phân loại nhị phân (Binary Classification) | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 14** | Phân loại đa lớp (Multiclass Classification) | - | - | - | - | - | ⏳ *Đang biên soạn* |
| **Tuần 15** | Tổng kết & Ôn tập cuối kỳ | - | - | - | - | - | ⏳ *Đang biên soạn* |

---

## 🛠️ 3. Hướng dẫn Môi trường & Cài đặt (Setup Guide)

### 1. Cài đặt Python & Anaconda
Khuyến nghị cài đặt bản [Anaconda Distribution](https://www.anaconda.com/download) (Python 3.10+).

### 2. Cài đặt các thư viện phụ thuộc
Mở **Anaconda Prompt** hoặc **Terminal** và chạy lệnh:
```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn bokeh jupyterlab pymongo
```

### 3. Mở JupyterLab làm việc
```bash
jupyter lab
```

---

## 📖 4. Tài liệu & Quy trình Soạn bài giảng

- 📋 **Đề cương chi tiết học phần:** Xem tệp [syllabus-vn.md](syllabus-vn.md)
- ⚙️ **Quy trình soạn bài giảng & Quản lý ảnh:** Xem tệp [QUY_TRINH_SOAN_BAI_GIANG.md](QUY_TRINH_SOAN_BAI_GIANG.md)

---

> © 2026 TS. Vũ Đức Minh - Khoa Khoa học dữ liệu & Trí tuệ nhân tạo (NEU). Bản quyền tài liệu thuộc về tác giả.
