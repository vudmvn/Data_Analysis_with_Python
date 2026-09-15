# Đề kiểm tra Định kỳ 60 phút (Tuần 1 – 4) / Midterm Examination (Weeks 1 – 4)
## Học phần: Phân tích dữ liệu với Python (DSAI1005) / Data Analysis with Python

- **Đơn vị phụ trách / Department:** Khoa Khoa học dữ liệu & Trí tuệ nhân tạo – Đại học Kinh tế Quốc dân (NEU) / Faculty of Data Science & AI – National Economics University
- **Giảng viên / Instructor:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)
- **Phạm vi kiến thức / Scope:** Tuần 1 – 4 (EDA & Overview, NumPy, Pandas, Visualization Matplotlib & Seaborn)
- **Hình thức thi / Format:** Thi viết trên giấy / Paper-based exam (Trắc nghiệm + Tự luận ngắn gọn / Multiple Choice + Short-Answer Coding)
- **Thời gian làm bài / Duration:** 60 phút / 60 minutes
- **Độ dài đề thi / Page Length:** Đúng 6 trang in A4 chuẩn / Exactly 6 pages

---

## 📁 Danh mục tài liệu / Exam Package Directory

### 1. Bản Tiếng Việt (Vietnamese Version)
| Tệp tin | Định dạng | Mô tả |
| :--- | :---: | :--- |
| [de_thi_giay_lectures_1_4.tex](de_thi_giay_lectures_1_4.tex) | `.tex` | Mã nguồn LaTeX đề thi chính thức cho sinh viên (Mã đề 201, đúng 6 trang) |
| [de_thi_giay_lectures_1_4.pdf](de_thi_giay_lectures_1_4.pdf) | `.pdf` | Bản PDF đề thi chính thức (Bảng 20 ô điền đáp án trang 1, khung kẻ dòng tự luận trang 4-6) |
| [dap_an_chi_tiet_lectures_1_4.tex](dap_an_chi_tiet_lectures_1_4.tex) | `.tex` | Mã nguồn LaTeX Hướng dẫn chấm & Đáp án chi tiết cho Cán bộ chấm thi |
| [dap_an_chi_tiet_lectures_1_4.pdf](dap_an_chi_tiet_lectures_1_4.pdf) | `.pdf` | Bản PDF Hướng dẫn chấm, đáp án trắc nghiệm kèm giải thích & barem điểm chi tiết (3 trang) |

### 2. Bản Tiếng Anh (English Version)
| File | Format | Description |
| :--- | :---: | :--- |
| [exam_paper_lectures_1_4_en.tex](exam_paper_lectures_1_4_en.tex) | `.tex` | LaTeX source code for official student exam paper (Exam Code 201, exactly 6 pages) |
| [exam_paper_lectures_1_4_en.pdf](exam_paper_lectures_1_4_en.pdf) | `.pdf` | Compiled PDF for official student exam paper (20-box answer grid on p.1, ruled writing boxes on pp. 4-6) |
| [exam_solution_lectures_1_4_en.tex](exam_solution_lectures_1_4_en.tex) | `.tex` | LaTeX source code for Instructor Solutions & Grading Rubric |
| [exam_solution_lectures_1_4_en.pdf](exam_solution_lectures_1_4_en.pdf) | `.pdf` | Compiled PDF of Detailed Solutions, MCQ answer keys with explanations & grading rubrics (3 pages) |

---

## 🎯 Cấu trúc đề thi & Phân bổ điểm số / Exam Structure (10 Points)

### Part I: Multiple-Choice Questions (5.0 pts — 20 questions $\times$ 0.25 pt each)
- **Week 1 / Lecture 1 (4 questions):** Core EDA objectives, standard deviation scaling properties, Boxplot outlier fence formula ($Q_1/Q_3 \pm 1.5\text{IQR}$), Pearson correlation interpretation ($r = 0$).
- **Week 2 / Lecture 2 (5 questions):** Array generation `np.arange()`, 2D slicing with step inversion `m[::-1, 1]`, 3D broadcasting rules `(5, 1, 3) * (4, 1) -> (5, 4, 3)`, conditional masking `np.where()`, aggregation axis `axis=0` in `np.sum()`.
- **Week 3 / Lecture 3 (6 questions):** `pd.Series` architecture & indexing, inclusive label slicing with `.loc`, missing value imputation `df.fillna()`, boolean bitwise OR `|`, MultiIndex column extraction after `groupby().agg(['min', 'max'])`, `inner join` record matching behavior.
- **Week 4 / Lecture 4 (5 questions):** Subplot axis unpacking `plt.subplots(2, 3)`, kernel density estimation `sns.kdeplot()`, pairwise grid `sns.pairplot()`, overlapping layout fix `plt.tight_layout()`, bar plots with confidence intervals `sns.barplot()`.

### Part II: Short-Answer & Code Reading (5.0 pts — 4 questions)
- **Question 1 (1.0 pt) [NumPy]:** Weighted grade calculation via **Broadcasting**; calculate row-wise semester GPA (`axis=1`) and predict conditional filtering output.
- **Question 2 (1.5 pts) [Pandas]:** Write conditional filter expression `&` combined with `.fillna(0)`; chain `.groupby('branch').agg(...)` to compute total volume, average fee, and transaction count, followed by `sort_values(ascending=False)`.
- **Question 3 (1.0 pt) [Matplotlib]:** Complete code snippet to create a 2-subplot canvas `plt.subplots(1, 2, figsize=(12, 4))`, plot line chart `axes[0].plot` (circle markers) and bar chart `axes[1].bar`, and invoke `plt.tight_layout()`.
- **Question 4 (1.5 pts) [EDA & Visualization]:** Recommend **Boxplot** for skewed transaction anomaly detection, write single-line Seaborn call `sns.boxplot(..., hue='card_type')`, and provide **2 data-driven analytical insights/fraud prevention policies** for high-limit corporate cards.

---

## ⚙️ Compilation Instructions (XeLaTeX)

Both Vietnamese and English documents require `xelatex` due to fontspec and font handling:

```powershell
# English version
xelatex -synctex=1 -interaction=nonstopmode exam_paper_lectures_1_4_en.tex
xelatex -synctex=1 -interaction=nonstopmode exam_solution_lectures_1_4_en.tex

# Vietnamese version
xelatex -synctex=1 -interaction=nonstopmode de_thi_giay_lectures_1_4.tex
xelatex -synctex=1 -interaction=nonstopmode dap_an_chi_tiet_lectures_1_4.tex
```
