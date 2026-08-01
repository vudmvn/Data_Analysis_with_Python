#!/usr/bin/env python3
"""
Script tự động quét các bài giảng trong `lectures/`, đối chiếu với đề cương `syllabus-vn.md`,
tạo/cập nhật Cổng thông tin môn học đầy đủ tại `README.md`, và thực hiện commit + push lên GitHub.

Cách dùng:
    python scripts/publish_lecture.py --message "Cập nhật bài giảng Tuần 01"
"""

import os
import sys
import re
import argparse
import subprocess

# Danh sách 15 tuần học chuẩn theo đề cương syllabus-vn.md
SYLLABUS_WEEKS = [
    {"week": "01", "topic": "Giới thiệu học phần", "desc": "Giới thiệu đề cương; Anaconda, Python, IPython, JupyterLab và Jupyter Notebook."},
    {"week": "02", "topic": "Thư viện tính toán NumPy", "desc": "Làm quen với NumPy, ndarray, vectorization & tính toán đại số tuyến tính."},
    {"week": "03", "topic": "Thư viện thao tác dữ liệu Pandas", "desc": "Series, DataFrame, Indexing, Thống kê mô tả & thao tác dữ liệu với Pandas."},
    {"week": "04", "topic": "Khám phá & Trực quan hóa dữ liệu", "desc": "Trực quan hóa dữ liệu bằng Matplotlib, Seaborn & biểu đồ tương tác Bokeh."},
    {"week": "05", "topic": "Truy xuất & Lưu trữ dữ liệu", "desc": "Đọc/ghi tệp CSV, Excel, JSON, HTML, PDF & kết nối MySQL, MongoDB, SQLite."},
    {"week": "06", "topic": "Làm sạch & Tiền xử lý dữ liệu", "desc": "Xử lý dữ liệu thiếu, nhiễu, ngoại lệ, encoding, scaling & feature transformation."},
    {"week": "07", "topic": "Thi giữa kỳ", "desc": "Ôn tập & Đánh giá kiến thức từ tuần 1 đến tuần 6."},
    {"week": "08", "topic": "Phân khúc & Phân cụm dữ liệu (Phần 1)", "desc": "Bài toán phân khúc dữ liệu, tiêu chí phân cụm & thuật toán K-Means."},
    {"week": "09", "topic": "Phân khúc & Phân cụm dữ liệu (Phần 2)", "desc": "Đánh giá mô hình phân cụm, Hierarchical Clustering & bài toán ứng dụng."},
    {"week": "10", "topic": "Dự báo dữ liệu & Hồi quy tuyến tính (Phần 1)", "desc": "Mô hình hồi quy tuyến tính đơn & bội, kiểm định giả định hồi quy."},
    {"week": "11", "topic": "Dự báo dữ liệu & Hồi quy tuyến tính (Phần 2)", "desc": "Kỹ thuật biến đổi đặc trưng (Feature Engineering) & đánh giá mô hình (RMSE, R2)."},
    {"week": "12", "topic": "Hồi quy phi tuyến & Classification Pipeline", "desc": "Hồi quy Logistic, đường cong Decision Boundary & xây dựng Pipeline với scikit-learn."},
    {"week": "13", "topic": "Phân loại nhị phân (Binary Classification)", "desc": "SVM, Cây quyết định (Decision Tree), Rừng ngẫu nhiên (Random Forest) & Đánh giá (Confusion Matrix, ROC-AUC)."},
    {"week": "14", "topic": "Phân loại đa lớp (Multiclass Classification)", "desc": "Chiến lược One-vs-Rest, One-vs-One, đánh giá mô hình đa lớp & xử lý dữ liệu mất cân bằng."},
    {"week": "15", "topic": "Tổng kết & Ôn tập cuối kỳ", "desc": "Hệ thống hóa toàn bộ kiến thức môn học, giải đáp thắc mắc & chuẩn bị thi cuối kỳ."}
]

def scan_lectures_dir(lectures_dir):
    """
    Quét thư mục lectures/ để tìm các thư mục tuần học và các file tài liệu bên trong.
    """
    lecture_map = {}
    if not os.path.exists(lectures_dir):
        return lecture_map

    for folder in os.listdir(lectures_dir):
        folder_path = os.path.join(lectures_dir, folder)
        if os.path.isdir(folder_path) and folder.startswith("week-"):
            parts = folder.split("-")
            if len(parts) >= 2:
                week_key = parts[1] # e.g. "01", "02"
                
                # Tìm các file trong thư mục tuần
                files = os.listdir(folder_path)
                
                notebook_link = f"[📘 Notebook](lectures/{folder}/lecture.ipynb)" if "lecture.ipynb" in files else "-"
                slides_link = f"[📊 Slides](lectures/{folder}/slides.md)" if "slides.md" in files else "-"
                lab_link = f"[💻 Lab](lectures/{folder}/lab_exercise.ipynb)" if "lab_exercise.ipynb" in files else "-"
                solution_link = f"[🔑 Đáp án](lectures/{folder}/lab_solution.ipynb)" if "lab_solution.ipynb" in files else "-"
                data_link = f"[📁 Data](lectures/{folder}/data/)" if "data" in files and os.path.isdir(os.path.join(folder_path, "data")) else "-"
                images_link = f"[🖼️ Images](lectures/{folder}/images/)" if "images" in files and os.path.isdir(os.path.join(folder_path, "images")) else "-"

                # Tìm các bài đọc bổ sung dạng .md (ngoại trừ README.md và slides.md)
                extra_mds = []
                for f in files:
                    if f.endswith(".md") and f not in ["README.md", "slides.md"]:
                        doc_title = f.replace(".md", "").replace("_", " ").title()
                        extra_mds.append(f"[{doc_title}](lectures/{folder}/{f})")

                extra_docs_str = "<br>".join(extra_mds) if extra_mds else ""

                lecture_map[week_key] = {
                    "folder": folder,
                    "notebook": notebook_link,
                    "slides": slides_link,
                    "lab": lab_link,
                    "solution": solution_link,
                    "data": data_link,
                    "images": images_link,
                    "extra_docs": extra_docs_str
                }
    return lecture_map

def generate_portal_readme():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lectures_dir = os.path.join(root_dir, "lectures")
    readme_path = os.path.join(root_dir, "README.md")

    lecture_map = scan_lectures_dir(lectures_dir)

    readme_content = """# 🐍 DSAI1005 – Phân tích dữ liệu với Python (Data Analysis with Python)

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
"""

    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic = item["topic"]
        
        if w in lecture_map:
            info = lecture_map[w]
            theory_parts = []
            if info["notebook"] != "-":
                theory_parts.append(info["notebook"])
            if info["extra_docs"]:
                theory_parts.append(info["extra_docs"])
            
            theory_str = "<br>".join(theory_parts) if theory_parts else "-"
            resources_parts = []
            if info["data"] != "-":
                resources_parts.append(info["data"])
            if info["images"] != "-":
                resources_parts.append(info["images"])
            res_str = " | ".join(resources_parts) if resources_parts else "-"

            readme_content += f"| **Tuần {w}** | **{topic}** | {theory_str} | {info['slides']} | {info['lab']} | {info['solution']} | {res_str} | ✅ *Đã sẵn sàng* |\n"
        else:
            readme_content += f"| **Tuần {w}** | {topic} | - | - | - | - | - | ⏳ *Đang biên soạn* |\n"

    readme_content += """
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
"""

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✅ Đã cập nhật Cổng thông tin bài giảng đầy đủ vào README.md!")

def run_git_publish(message):
    print("Đang đẩy dữ liệu lên GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🎉 Đã xuất bản cập nhật lên GitHub thành công!")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Lỗi khi xuất bản bằng git: {e}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Cập nhật Cổng thông tin syllabus và đẩy bài giảng lên GitHub.")
    parser.add_argument("--message", "-m", default="docs(readme): Cập nhật cổng thông tin môn học & ma trận bài giảng 15 tuần", help="Nội dung commit message")
    parser.add_argument("--no-push", action="store_true", help="Chỉ cập nhật README.md, không git commit & push")
    args = parser.parse_args()

    generate_portal_readme()

    if not args.no_push:
        run_git_publish(args.message)
