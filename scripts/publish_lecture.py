#!/usr/bin/env python3
"""
Script tự động quét các bài giảng trong `lectures/`, đối chiếu với đề cương `syllabus-vn.md`,
tạo/cập nhật Cổng thông tin môn học Song ngữ (Tiếng Việt `README.md` và Tiếng Anh `README-en.md`),
và thực hiện commit + push lên GitHub.
"""

import os
import sys
import re
import argparse
import subprocess

# Danh sách 15 tuần học chuẩn Song ngữ (Bilingual Syllabus Mapping)
SYLLABUS_WEEKS = [
    {
        "week": "01",
        "topic_vn": "Giới thiệu học phần",
        "topic_en": "Course Introduction & Setup",
        "desc_vn": "Giới thiệu đề cương; Anaconda, Python, IPython, JupyterLab và Jupyter Notebook.",
        "desc_en": "Syllabus overview; Anaconda, Python, IPython, JupyterLab & Jupyter Notebook setup."
    },
    {
        "week": "02",
        "topic_vn": "Thư viện tính toán NumPy",
        "topic_en": "Numerical Computing with NumPy",
        "desc_vn": "Làm quen với NumPy, ndarray, vectorization & tính toán đại số tuyến tính.",
        "desc_en": "Introduction to NumPy, ndarrays, vectorized operations & linear algebra."
    },
    {
        "week": "03",
        "topic_vn": "Thư viện thao tác dữ liệu Pandas",
        "topic_en": "Data Manipulation with Pandas",
        "desc_vn": "Series, DataFrame, Indexing, Thống kê mô tả & thao tác dữ liệu với Pandas.",
        "desc_en": "Series, DataFrames, indexing, descriptive statistics & data manipulation with Pandas."
    },
    {
        "week": "04",
        "topic_vn": "Khám phá & Trực quan hóa dữ liệu",
        "topic_en": "Data Exploration & Visualization",
        "desc_vn": "Trực quan hóa dữ liệu bằng Matplotlib, Seaborn & biểu đồ tương tác Bokeh.",
        "desc_en": "Data visualization with Matplotlib, Seaborn & interactive charts with Bokeh."
    },
    {
        "week": "05",
        "topic_vn": "Truy xuất & Lưu trữ dữ liệu",
        "topic_en": "Data Access & Storage Systems",
        "desc_vn": "Đọc/ghi tệp CSV, Excel, JSON, HTML, PDF & kết nối MySQL, MongoDB, SQLite.",
        "desc_en": "Reading/writing CSV, Excel, JSON, HTML, PDF & connecting to MySQL, MongoDB, SQLite."
    },
    {
        "week": "06",
        "topic_vn": "Làm sạch & Tiền xử lý dữ liệu",
        "topic_en": "Data Cleaning & Preprocessing",
        "desc_vn": "Xử lý dữ liệu thiếu, nhiễu, ngoại lệ, encoding, scaling & feature transformation.",
        "desc_en": "Handling missing data, noise, outliers, encoding, scaling & feature transformation."
    },
    {
        "week": "07",
        "topic_vn": "Thi giữa kỳ",
        "topic_en": "Midterm Examination",
        "desc_vn": "Ôn tập & Đánh giá kiến thức từ tuần 1 đến tuần 6.",
        "desc_en": "Review and assessment of topics from Week 1 to Week 6."
    },
    {
        "week": "08",
        "topic_vn": "Phân khúc & Phân cụm dữ liệu (Phần 1)",
        "topic_en": "Data Segmentation & Clustering (Part 1)",
        "desc_vn": "Bài toán phân khúc dữ liệu, tiêu chí phân cụm & thuật toán K-Means.",
        "desc_en": "Customer/Data segmentation concepts, distance metrics & K-Means clustering."
    },
    {
        "week": "09",
        "topic_vn": "Phân khúc & Phân cụm dữ liệu (Phần 2)",
        "topic_en": "Data Segmentation & Clustering (Part 2)",
        "desc_vn": "Đánh giá mô hình phân cụm, Hierarchical Clustering & bài toán ứng dụng.",
        "desc_en": "Cluster evaluation metrics, Hierarchical Clustering & practical business cases."
    },
    {
        "week": "10",
        "topic_vn": "Dự báo dữ liệu & Hồi quy tuyến tính (Phần 1)",
        "topic_en": "Data Forecasting & Linear Regression (Part 1)",
        "desc_vn": "Mô hình hồi quy tuyến tính đơn & bội, kiểm định giả định hồi quy.",
        "desc_en": "Simple & Multiple Linear Regression models and regression assumptions verification."
    },
    {
        "week": "11",
        "topic_vn": "Dự báo dữ liệu & Hồi quy tuyến tính (Phần 2)",
        "topic_en": "Data Forecasting & Linear Regression (Part 2)",
        "desc_vn": "Kỹ thuật biến đổi đặc trưng (Feature Engineering) & đánh giá mô hình (RMSE, R2).",
        "desc_en": "Feature Engineering techniques & regression performance evaluation (RMSE, R2)."
    },
    {
        "week": "12",
        "topic_vn": "Hồi quy phi tuyến & Classification Pipeline",
        "topic_en": "Non-linear Regression & Classification Pipeline",
        "desc_vn": "Hồi quy Logistic, đường cong Decision Boundary & xây dựng Pipeline với scikit-learn.",
        "desc_en": "Logistic Regression, Decision Boundaries & building ML Pipelines with scikit-learn."
    },
    {
        "week": "13",
        "topic_vn": "Phân loại nhị phân (Binary Classification)",
        "topic_en": "Binary Classification Algorithms",
        "desc_vn": "SVM, Cây quyết định (Decision Tree), Rừng ngẫu nhiên (Random Forest) & Đánh giá (Confusion Matrix, ROC-AUC).",
        "desc_en": "SVM, Decision Trees, Random Forest & evaluation metrics (Confusion Matrix, ROC-AUC)."
    },
    {
        "week": "14",
        "topic_vn": "Phân loại đa lớp (Multiclass Classification)",
        "topic_en": "Multiclass Classification & Imbalanced Data",
        "desc_vn": "Chiến lược One-vs-Rest, One-vs-One, đánh giá mô hình đa lớp & xử lý dữ liệu mất cân bằng.",
        "desc_en": "One-vs-Rest & One-vs-One strategies, multiclass metrics & imbalanced dataset handling."
    },
    {
        "week": "15",
        "topic_vn": "Tổng kết & Ôn tập cuối kỳ",
        "topic_en": "Course Summary & Final Review",
        "desc_vn": "Hệ thống hóa toàn bộ kiến thức môn học, giải đáp thắc mắc & chuẩn bị thi cuối kỳ.",
        "desc_en": "Systematizing full course knowledge, Q&A session & final exam preparation."
    }
]

def is_valid_content_file(file_path, min_bytes=500):
    if not os.path.exists(file_path):
        return False
    return os.path.getsize(file_path) >= min_bytes

def scan_lectures_dir(lectures_dir):
    lecture_map = {}
    if not os.path.exists(lectures_dir):
        return lecture_map

    for folder in os.listdir(lectures_dir):
        folder_path = os.path.join(lectures_dir, folder)
        if os.path.isdir(folder_path):
            week_key = None
            if folder.startswith("part"):
                num_match = re.search(r'part(\d+)', folder)
                if num_match:
                    week_key = f"{int(num_match.group(1)):02d}"
            elif folder.startswith("week-"):
                num_match = re.search(r'week-(\d+)', folder)
                if num_match:
                    week_key = f"{int(num_match.group(1)):02d}"

            if not week_key:
                continue

            files = os.listdir(folder_path)

            # Check lecture notebooks / PDFs
            lecture_file = os.path.join(folder_path, "lecture.ipynb")
            notebook_link = f"[📘 Notebook](lectures/{folder}/lecture.ipynb)" if is_valid_content_file(lecture_file, 1000) else "-"

            # Check slides
            slide_links = []
            for f in sorted(files):
                if f.endswith(".pdf"):
                    slide_links.append(f'<a href="lectures/{folder}/{f}" target="_blank">PDF ({f.replace(".pdf", "")})</a>')
            slides_link = "<br>".join(slide_links) if slide_links else "-"

            # Check lab exercises
            lab_links = []
            for f in sorted(files):
                if f.endswith(".ipynb") and "practice" in f or "exercise" in f:
                    lab_links.append(f'<a href="lectures/{folder}/{f}" target="_blank">Lab ({f.replace(".ipynb", "")})</a>')
            lab_link = "<br>".join(lab_links) if lab_links else "-"

            solution_file = os.path.join(folder_path, "lab_solution.ipynb")
            solution_link = f"[🔑 Đáp án / Solution](lectures/{folder}/lab_solution.ipynb)" if is_valid_content_file(solution_file, 1000) else "-"

            extra_mds_vn = []
            extra_mds_en = []

            for f in sorted(files):
                if f.endswith(".md") and f not in ["README.md", "slides.md"]:
                    file_full_path = os.path.join(folder_path, f)
                    doc_title = f.replace(".md", "").replace("_", " ").replace("-", " ").title()
                    try:
                        with open(file_full_path, "r", encoding="utf-8") as mdf:
                            for line in mdf:
                                line_str = line.strip()
                                if line_str.startswith("# "):
                                    doc_title = line_str.replace("# ", "").strip()
                                    break
                    except Exception:
                        pass

                    link_str = f"• [{doc_title}](lectures/{folder}/{f})"
                    if f.endswith("-en.md"):
                        extra_mds_en.append(link_str)
                    elif f.endswith("-vn.md") or not f.endswith("-en.md"):
                        extra_mds_vn.append(link_str)

            extra_docs_vn_str = "<br>".join(extra_mds_vn) if extra_mds_vn else ""
            extra_docs_en_str = "<br>".join(extra_mds_en) if extra_mds_en else ""

            lecture_map[week_key] = {
                "folder": folder,
                "notebook": notebook_link,
                "slides": slides_link,
                "lab": lab_link,
                "solution": solution_link,
                "extra_docs_vn": extra_docs_vn_str,
                "extra_docs_en": extra_docs_en_str
            }
    return lecture_map

def generate_portal_readmes():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lectures_dir = os.path.join(root_dir, "lectures")
    readme_vn_path = os.path.join(root_dir, "README.md")
    readme_en_path = os.path.join(root_dir, "README-en.md")

    lecture_map = scan_lectures_dir(lectures_dir)

    # -------------------------------------------------------------
    # 1. TẠO FILE README.md (PHIÊN BẢN TIẾNG VIỆT CÓ DẤU CHUẨN)
    # -------------------------------------------------------------
    vn_content = """# 🐍 DSAI1005 – Phân tích dữ liệu với Python (Data Analysis with Python)

🌐 **Ngôn ngữ / Language:** 🇻🇳 **Tiếng Việt** | [🇬🇧 English Version (README-en.md)](README-en.md)

> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)  
> **Đơn vị phụ trách:** Khoa Khoa học dữ liệu và Trí tuệ nhân tạo – Trường Đại học Kinh tế Quốc dân (NEU)  
> **Số tín chỉ:** 3 Tín chỉ (45h lý thuyết, 22.5h thực hành, 90h tự học)  
> **Đề cương chi tiết học phần:** Xem tệp [syllabus-vn.md](syllabus-vn.md)

---

## 📌 1. Giới thiệu Học phần & Mục tiêu

Học phần **Phân tích dữ liệu với Python (DSAI1005)** cung cấp kiến thức nhập môn có hệ thống về Khoa học dữ liệu và Phân tích dữ liệu kinh doanh. Sinh viên được trang bị kỹ năng sử dụng thành thạo hệ sinh thái Python bao gồm **NumPy, Pandas, Matplotlib, Seaborn, Bokeh, SciPy, SQLite, PyMongo và Scikit-learn**.

### 🎯 Mục tiêu & Chuẩn đầu ra (CLOs):
1. **Công cụ & Môi trường:** Thành thạo Anaconda, Python, JupyterLab và quản lý môi trường ảo.
2. **Đại số tuyến tính & Thống kê:** Tính toán ma trận, vector và phân tích thống kê với NumPy & SciPy.
3. **Thao tác Dữ liệu:** Đọc, làm sạch, biến đổi, chuẩn hóa và xử lý giá trị thiếu / ngoại lệ bằng Pandas.
4. **Trực quan hóa:** Xây dựng biểu đồ mô tả & biểu đồ tương tác với Matplotlib, Seaborn, Bokeh.
5. **Cơ sở dữ liệu:** Truy xuất và lưu trữ dữ liệu từ CSV, Excel, JSON, SQL (MySQL/SQLite) & NoSQL (MongoDB).
6. **Mô hình hóa:** Áp dụng thuật toán Phân cụm (K-Means), Hồi quy (Linear/Logistic) & Phân loại (SVM, Decision Tree, Random Forest).

---

## 📚 2. Ma trận Bài giảng, Tài liệu & Bài tập Thực hành (Course Matrix)

Bảng dưới đây tổng hợp chi tiết tài liệu học tập, bài giảng Notebook, slide, bài tập thực hành, tệp dữ liệu và đáp án cho **15 tuần học**:

| Tuần | Chủ đề chính (Tiếng Việt) | Bài giảng & Bài đọc (.md / .ipynb) | Slide | Bài tập Lab | Đáp án | Trạng thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|
"""

    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic_vn = item["topic_vn"]
        
        if w in lecture_map:
            info = lecture_map[w]
            theory_parts = []
            if info["notebook"] != "-":
                theory_parts.append(info["notebook"])
            if info["extra_docs_vn"]:
                theory_parts.append(info["extra_docs_vn"])
            
            theory_str = "<br>".join(theory_parts) if theory_parts else "-"

            vn_content += f"| **Tuần {w}** | **{topic_vn}** | {theory_str} | {info['slides']} | {info['lab']} | {info['solution']} | ✅ *Đã sẵn sàng* |\n"
        else:
            vn_content += f"| **Tuần {w}** | {topic_vn} | - | - | - | - | ⏳ *Đang biên soạn* |\n"

    vn_content += """
---

## 📖 3. Sách tham khảo (References & Textbooks)

| Bìa sách | Tài liệu | Tác giả | Nhà xuất bản | ISBN | Liên kết |
|:---:|:---|:---|:---|:---:|:---:|
| <img src="assets/images/python-data-analysis-3rd-cover.jpg" alt="Python Data Analysis 3rd Edition" width="90" /> | **Python Data Analysis**, 3rd Edition | Avinash Navlani, Armando Fandango, Ivan Idris | Packt Publishing, 2021 | 9781800564480 | [Thông tin sách](https://www.packtpub.com/product/python-data-analysis-third-edition/9781800564480) |
| <img src="assets/images/data-science-marketing-analytics-cover.jpg" alt="Data Science for Marketing Analytics" width="90" /> | **Data Science for Marketing Analytics**, 2nd Edition | Mirza Rahim Baig, Gururajan Govindan, Vishwesh Ravi Shrimali | Packt Publishing, 2021 | 9781800560475 | [Thông tin sách](https://www.packtpub.com/product/data-science-for-marketing-analytics-second-edition/9781800560475) |
| <img src="assets/images/data-analysis-business-economics-cover.jpg" alt="Data Analysis for Business, Economics and Policy" width="90" /> | **Data Analysis for Business, Economics and Policy** | Gábor Békés, Gábor Kézdi | Cambridge University Press, 2021 | 9781108716208 | [Thông tin sách](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/B80C65A15ACD4FF5FA0B0FD7A73F1C46) |
| <img src="assets/images/python-for-data-science-dummies-cover.jpg" alt="Python for Data Science For Dummies" width="90" /> | **Python for Data Science For Dummies**, 2nd Edition | John Paul Mueller, Luca Massaron | John Wiley & Sons, 2019 | 9781119547624 | [Thông tin sách](https://www.wiley.com/en-us/Python+for+Data+Science+For+Dummies%2C+2nd+Edition-p-9781119547624) |
| <img src="assets/images/python-data-analysis-1st-cover.jpg" alt="Python Data Analysis 1st Edition" width="90" /> | **Python Data Analysis**, 1st Edition | Ivan Idris | Packt Publishing, 2014 | 9781783552030 | [Thông tin sách](https://www.packtpub.com/product/python-data-analysis/9781783552030) |

---

> © 2026 TS. Vũ Đức Minh - Khoa Khoa học dữ liệu & Trí tuệ nhân tạo (NEU). Bản quyền tài liệu thuộc về tác giả.
"""

    with open(readme_vn_path, "w", encoding="utf-8") as f:
        f.write(vn_content)
    print("✅ Đã cập nhật file README.md (Tiếng Việt có dấu chuẩn)!")

    # -------------------------------------------------------------
    # 2. TẠO FILE README-en.md (BILINGUAL / ENGLISH VERSION)
    # -------------------------------------------------------------
    en_content = """# 🐍 DSAI1005 – Data Analysis with Python

🌐 **Language:** [🇻🇳 Vietnamese Version (README.md)](README.md) | 🇬🇧 **English**

> **Lecturer:** Dr. Minh Duc Vu (`minhvd@neu.edu.vn`)  
> **Department:** School of Data Science and Artificial Intelligence – National Economics University (NEU)  
> **Credits:** 3 Credits (45h Lectures, 22.5h Labs, 90h Self-study)  
> **Detailed Syllabus:** View [syllabus-en.md](syllabus-en.md)

---

## 📌 1. Course Description & Objectives

The course **Data Analysis with Python (DSAI1005)** provides a systematic introduction to Data Science and Business Data Analytics. Students will master the core Python data ecosystem, including **NumPy, Pandas, Matplotlib, Seaborn, Bokeh, SciPy, SQLite, PyMongo, and Scikit-learn**.

### 🎯 Course Learning Outcomes (CLOs):
1. **Tools & Environment:** Master Anaconda, Python, JupyterLab, and virtual environment management.
2. **Linear Algebra & Statistics:** Perform matrix operations, vector computations, and statistical analysis with NumPy & SciPy.
3. **Data Manipulation:** Read, clean, transform, normalize, and handle missing values/outliers using Pandas.
4. **Data Visualization:** Create descriptive and interactive charts using Matplotlib, Seaborn, and Bokeh.
5. **Data Access & Storage:** Fetch and store data from CSV, Excel, JSON, relational SQL (MySQL/SQLite), and NoSQL (MongoDB).
6. **Machine Learning Modeling:** Apply Clustering (K-Means), Regression (Linear/Logistic), and Classification (SVM, Decision Tree, Random Forest).

---

## 📚 2. Course Portal & Learning Matrix (15-Week Syllabus)

The table below summarizes lecture notebooks, reading materials, slides, lab assignments, sample datasets, and solutions for all **15 weeks**:

| Week | Main Topic (English) | Lecture & Reading Materials (.md / .ipynb) | Slides | Lab Exercise | Solutions | Status |
|:---:|:---|:---|:---:|:---:|:---:|:---:|
"""

    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic_en = item["topic_en"]
        
        if w in lecture_map:
            info = lecture_map[w]
            theory_parts = []
            if info["notebook"] != "-":
                theory_parts.append(info["notebook"])
            if info["extra_docs_en"]:
                theory_parts.append(info["extra_docs_en"])
            
            theory_str = "<br>".join(theory_parts) if theory_parts else "-"

            en_content += f"| **Week {w}** | **{topic_en}** | {theory_str} | {info['slides']} | {info['lab']} | {info['solution']} | ✅ *Ready* |\n"
        else:
            en_content += f"| **Week {w}** | {topic_en} | - | - | - | - | ⏳ *In Progress* |\n"

    en_content += """
---

## 📖 3. References & Textbooks

| Book Cover | Reference | Author | Publisher | ISBN | Link |
|:---:|:---|:---|:---|:---:|:---:|
| <img src="assets/images/python-data-analysis-3rd-cover.jpg" alt="Python Data Analysis 3rd Edition" width="90" /> | **Python Data Analysis**, 3rd Edition | Avinash Navlani, Armando Fandango, Ivan Idris | Packt Publishing, 2021 | 9781800564480 | [Book Info](https://www.packtpub.com/product/python-data-analysis-third-edition/9781800564480) |
| <img src="assets/images/data-science-marketing-analytics-cover.jpg" alt="Data Science for Marketing Analytics" width="90" /> | **Data Science for Marketing Analytics**, 2nd Edition | Mirza Rahim Baig, Gururajan Govindan, Vishwesh Ravi Shrimali | Packt Publishing, 2021 | 9781800560475 | [Book Info](https://www.packtpub.com/product/data-science-for-marketing-analytics-second-edition/9781800560475) |
| <img src="assets/images/data-analysis-business-economics-cover.jpg" alt="Data Analysis for Business, Economics and Policy" width="90" /> | **Data Analysis for Business, Economics and Policy** | Gábor Békés, Gábor Kézdi | Cambridge University Press, 2021 | 97811108716208 | [Book Info](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/B80C65A15ACD4FF5FA0B0FD7A73F1C46) |
| <img src="assets/images/python-for-data-science-dummies-cover.jpg" alt="Python for Data Science For Dummies" width="90" /> | **Python for Data Science For Dummies**, 2nd Edition | John Paul Mueller, Luca Massaron | John Wiley & Sons, 2019 | 9781119547624 | [Book Info](https://www.wiley.com/en-us/Python+for+Data+Science+For+Dummies%2C+2nd+Edition-p-9781119547624) |
| <img src="assets/images/python-data-analysis-1st-cover.jpg" alt="Python Data Analysis 1st Edition" width="90" /> | **Python Data Analysis**, 1st Edition | Ivan Idris | Packt Publishing, 2014 | 9781783552030 | [Book Info](https://www.packtpub.com/product/python-data-analysis/9781783552030) |

---

> © 2026 Dr. Minh Duc Vu - School of Data Science & Artificial Intelligence (NEU). All rights reserved.
"""

    with open(readme_en_path, "w", encoding="utf-8") as f:
        f.write(en_content)
    print("✅ Đã cập nhật file README-en.md (Phiên bản Tiếng Anh / English Version)!")

def run_git_publish(message):
    print("Đang đẩy dữ liệu lên GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🎉 Đã xuất bản cập nhật Song ngữ lên GitHub thành công!")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Lỗi khi xuất bản bằng git: {e}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Cập nhật Cổng thông tin môn học Song ngữ và đẩy bài giảng lên GitHub.")
    parser.add_argument("--message", "-m", default="docs(readme): Cập nhật Cổng thông tin môn học Song ngữ", help="Nội dung commit message")
    parser.add_argument("--no-push", action="store_true", help="Chỉ cập nhật README files, không git commit & push")
    args = parser.parse_args()

    generate_portal_readmes()

    if not args.no_push:
        run_git_publish(args.message)
