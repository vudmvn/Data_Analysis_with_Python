# Midterm Examination: NumPy, Pandas & Visualization (60 Minutes)
## Course: Data Analysis with Python (DSAI1005)

- **Department:** Faculty of Data Science & AI – National Economics University (NEU)
- **Laboratory:** DATCOM Lab
- **Course Code:** DSAI1005
- **Exam Code:** `301-EN`
- **Format:** Paper-based examination following the standardized **DATCOM Lab Exam Format** (as demonstrated in `Exam_ODD_English_120min.pdf`)
- **Duration:** 60 minutes
- **Total Score:** 10.0 Points (100%)
- **Target Page Count:** Exactly 6 pages (`Page 1/6` through `Page 6/6`)

---

## 🎯 Exam Structure & Grade Distribution

The examination strictly follows the specified syllabus breakdown:
- **Part I: Multiple Choice Questions (60% / 6.0 pts)**
  - **NumPy (20% / 2.0 pts):** 4 questions $\times$ 0.5 pt each (Q1–Q4)
  - **Pandas (20% / 2.0 pts):** 4 questions $\times$ 0.5 pt each (Q5–Q8)
  - **Data Visualization (20% / 2.0 pts):** 4 questions $\times$ 0.5 pt each (Q9–Q12)
  - *Format:* 2-column layout across Pages 2 and 3, with check-boxes (`Answer: □ A  □ B  □ C  □ D`) under each question for direct marking.
- **Part II: Integrated Data Problems (40% / 4.0 pts)**
  - **Question 13: Quantitative E-Commerce Performance Pipeline (20% / 2.0 pts) [NumPy & Pandas]**
    - Subparts a, b, c, d, e (5 subparts $\times$ 0.40 pt each)
  - **Question 14: Sales Dashboard & Anomaly Visualization (20% / 2.0 pts) [Pandas & Viz]**
    - Subpart a (0.40 pt): OO subplot canvas initialization
    - Subpart b (0.60 pt): Grouped Seaborn boxplot call with stratification
    - Subpart c (0.40 pt): Datetime weekly resampling & 4-week rolling moving average
    - Subpart d (0.20 pt): Automatic subplot margin spacing (`plt.tight_layout()`)
    - Subparts e & f (2 $\times$ 0.20 pt = 0.40 pt): Quantitative analytical interpretation (outlier fence detection & forecasting advantage)
  - *Format:* Dedicated answer boxes labeled *"Write your answer in this box."* for each subpart.

---

## 📁 Exam Package Directory

| File | Format | Description | Pages |
| :--- | :---: | :--- | :---: |
| [exam_paper_60mins_en.tex](exam_paper_60mins_en.tex) | `.tex` | XeLaTeX source code for official student exam paper | 6 |
| [exam_paper_60mins_en.pdf](exam_paper_60mins_en.pdf) | `.pdf` | Compiled student exam paper formatted to DATCOM Lab standard | **6** |
| [exam_solution_60mins_en.tex](exam_solution_60mins_en.tex) | `.tex` | XeLaTeX source code for Instructor Solutions & Grading Guide | 4 |
| [exam_solution_60mins_en.pdf](exam_solution_60mins_en.pdf) | `.pdf` | Compiled master answer key, in-depth technical rationales & grading rubrics | 4 |
| [Exam_ODD_English_120min.pdf](Exam_ODD_English_120min.pdf) | `.pdf` | Reference benchmark exam format from DATCOM Lab | 10 |
| [README.md](README.md) | `.md` | Documentation of exam structure, syllabus alignment, and compilation guides | — |

---

## 📄 Page-by-Page Layout (Student Exam Paper)

- **Page 1:**
  - Administrative header: National Economics University, Faculty of DS & AI.
  - Midterm Examination title, Course code, Exam Version `301-EN`.
  - Student identity fields: Full name, Student ID, Class, Room, Signature, Exam date.
  - Duration (60 mins), Total points (10.0 pts), Instructions (Rules 1 to 5).
  - Official Grading Score Table (Part I: 6.0, Part II: 4.0, Total: 10.0).
  - Invigilator guidance note.
- **Page 2:**
  - Running Header: `Data Analysis with Python | Exam Version: 301-EN | Student ID: ________`
  - Part I --- Multiple Choice (Two-column layout):
    - Q1: `np.linspace` & arithmetic vectorization.
    - Q2: Step slicing `[::-1, 1]` memory view mutation.
    - Q3: 3D Broadcasting rules `(4, 1, 6) * (3, 1)`.
    - Q4: Bitwise conditional filtering `np.where` and column reduction `axis=0`.
    - Q5: Disjoint Series arithmetic `.add(fill_value=0)`.
    - Q6: `.loc` inclusive label boundary vs `.iloc` half-open positional boundary.
  - Check-boxes `Answer: □ A  □ B  □ C  □ D` under each question.
  - Running Footer: `DATCOM Lab --- National Economics University | Page 2/6 | Write directly on this exam paper`.
- **Page 3:**
  - Part I --- Multiple Choice (continued, Two-column layout):
    - Q7: Multi-level aggregation `groupby(['Region', 'Category'])['Sales'].agg(['sum', 'count'])`.
    - Q8: Left merge / outer join record retention and `NaN` filling semantics.
    - Q9: Matplotlib OO 2D subplot array indexing `axes[row, col]` and `.set_title()`.
    - Q10: Boxplot for skewed distributions & $1.5 \times IQR$ outliers.
    - Q11: Seaborn `hue` and `style` semantic mappings.
    - Q12: `annot=True` heatmap overlays and `plt.tight_layout()` padding.
  - Check-boxes `Answer: □ A  □ B  □ C  □ D` under each question.
  - Running Footer: `Page 3/6`.
- **Page 4:**
  - Part II --- Integrated Data Problems:
    - Question 13: Quantitative E-Commerce Performance Pipeline ($5 \times 4$ array `tx_data`).
    - Subparts a) to e) with dedicated answer boxes labeled *"Write your answer in this box."*.
  - Running Footer: `Page 4/6`.
- **Page 5:**
  - Question 14: Sales Dashboard & Anomaly Visualization (`df_sales` schema).
    - Subpart a) [0.40]: $1 \times 2$ subplot grid initialization with `figsize=(14, 5)`.
    - Subpart b) [0.60]: Stratified grouped `sns.boxplot()` call.
    - Subplot title/label formatting listing.
  - Running Footer: `Page 5/6`.
- **Page 6:**
  - Question 14 --- Continued:
    - Subpart c) [0.40]: Weekly resampling & 4-week rolling moving average.
    - Subpart d) [0.20]: Automatic canvas padding adjustment (`plt.tight_layout()`).
    - Subparts e) & f) [0.40]: Analytical interpretation questions (Outlier fence identification & moving average smoothing for forecasting).
  - Official banner: `--- END OF EXAMINATION PAPER ---`.
  - Running Footer: `Page 6/6`.

---

## 🛠️ Compilation Instructions

The LaTeX documents utilize `fontspec` and standard system fonts (`Times New Roman`, `Arial`, `Consolas`), and must be compiled using **XeLaTeX**:

```powershell
# In exams/exam-03-60mins-numpy-pandas-viz/

# 1. Compile student exam paper
xelatex -synctex=1 -interaction=nonstopmode exam_paper_60mins_en.tex

# 2. Compile solutions and grading guide
xelatex -synctex=1 -interaction=nonstopmode exam_solution_60mins_en.tex
```
