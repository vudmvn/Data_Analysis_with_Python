# Midterm Examination: NumPy, Pandas & Visualization (60 Minutes)
## Course: Data Analysis with Python (DSAI1005)

- **Department:** Faculty of Data Science & AI – National Economics University (NEU)
- **Course Code:** DSAI1005
- **Exam Code:** `301-EN`
- **Duration:** 60 minutes
- **Format:** Paper-based written examination (Multiple-Choice + Fill-in-the-Blanks Code Integration)
- **Total Score:** 10.0 Points (100%)
- **Target Page Count:** Exactly 6 pages (`Page 1 of 6` through `Page 6 of 6`)

---

## 🎯 Exam Structure & Grade Distribution

The examination strictly follows the required curriculum breakdown:
- **Part I: Multiple-Choice Questions (Quiz) — 60% (6.0 pts)**
  - **Section A: NumPy (20% / 2.0 pts)** — 4 questions $\times$ 0.5 pt each (Q1–Q4)
  - **Section B: Pandas (20% / 2.0 pts)** — 4 questions $\times$ 0.5 pt each (Q5–Q8)
  - **Section C: Data Visualization (20% / 2.0 pts)** — 4 questions $\times$ 0.5 pt each (Q9–Q12)
- **Part II: Applied Coding (Fill-in-the-Blanks) — 40% (4.0 pts)**
  - **Problem 1: Quantitative E-Commerce Performance Pipeline (20% / 2.0 pts)** — Integrated NumPy & Pandas (5 blanks $\times$ 0.4 pt each)
  - **Problem 2: Multi-Channel Sales Dashboard & Risk Analytics (20% / 2.0 pts)** — Integrated Pandas & Matplotlib/Seaborn (Part A: 1.0 pt, Part B: 0.6 pt, Part C: 0.4 pt)

---

## 📁 Exam Package Directory

| File | Format | Description | Pages |
| :--- | :---: | :--- | :---: |
| [exam_paper_60mins_en.tex](exam_paper_60mins_en.tex) | `.tex` | XeLaTeX source code for official student exam paper | 6 |
| [exam_paper_60mins_en.pdf](exam_paper_60mins_en.pdf) | `.pdf` | Compiled student exam paper with top answer sheet grid & compact answer tables | **6** |
| [exam_solution_60mins_en.tex](exam_solution_60mins_en.tex) | `.tex` | XeLaTeX source code for Instructor Solutions & Grading Guide | 4 |
| [exam_solution_60mins_en.pdf](exam_solution_60mins_en.pdf) | `.pdf` | Compiled master answer key, in-depth technical rationales & grading rubrics | 4 |
| [README.md](README.md) | `.md` | Documentation of exam structure, syllabus alignment, and compilation guides | — |

---

## 📄 Detailed Page-by-Page Layout (Student Exam Paper)

- **Page 1:**
  - Administrative header & course metadata.
  - Examiner score entry rubric table.
  - Student identity fields (Full Name, Student ID, Class, Room, Seat).
  - 12-cell Multiple-Choice Answer Sheet table for rapid grading.
  - Part I, Section A (NumPy): Q1 (`np.linspace` & arithmetic vectorization), Q2 (Step slicing `[::-1, 1]` memory view mutation), Q3 (3D broadcasting rules `(4, 1, 6) * (3, 1)`).
- **Page 2:**
  - Part I, Section A (NumPy): Q4 (Bitwise conditional filtering `np.where` and column reduction `axis=0`).
  - Part I, Section B (Pandas): Q5 (Disjoint Series arithmetic `.add(fill_value=0)`), Q6 (Inclusive `.loc` vs half-open `.iloc`), Q7 (Multi-level `.groupby().agg()`), Q8 (Left merge semantics and `NaN` preservation).
- **Page 3:**
  - Part I, Section C (Visualization): Q9 (Matplotlib OO 2D subplot indexing `axes[0, 1]` and `.set_title()`), Q10 (Boxplot for skewed distributions & $1.5 \times IQR$ outliers), Q11 (Seaborn `hue` and `style` semantic mappings), Q12 (`annot=True` heatmap overlays and `plt.tight_layout()` padding).
- **Page 4:**
  - Part II, Problem 1 (NumPy & Pandas Pipeline): Complete business transaction scenario, 2D ndarray extraction, vectorized Net Revenue formula, conditional order tier tagging (`np.where`), left join merge, multi-level aggregation, descending sorting.
  - Compact 5-row student answer sheet table (`[BLANK 1]` to `[BLANK 5]`).
- **Page 5:**
  - Part II, Problem 2 Part A (Canvas & Categorical Distribution): Multi-panel executive dashboard scenario, `plt.subplots(1, 2)` grid initialization (`[BLANK 6]`), and grouped `sns.boxplot()` call stratified by fraud status (`[BLANK 7]`).
  - Compact student answer sheet table for Part A.
- **Page 6:**
  - Part II, Problem 2 Part B (Time-Series & Spacing): Datetime conversion, weekly resampling, 4-week moving average `.rolling(4).mean()` (`[BLANK 8]`), and `plt.tight_layout()` padding call (`[BLANK 9]`).
  - Student answer sheet table for Part B.
  - Part II, Problem 2 Part C (Analytical Insights): 2 executive decision-making questions (Outlier identification via $IQR$ whiskers and forecasting advantages of moving averages) with ruled response box.
  - Official footer: `--- END OF EXAMINATION PAPER ---`.

---

## 🛠️ Compilation Instructions

The LaTeX documents utilize `fontspec` and standard system fonts (`Times New Roman`, `Arial`, `Consolas`), and must be compiled using **XeLaTeX**:

```powershell
# In exams/exam-03-60mins-numpy-pandas-viz/

# 1. Compile student exam paper (run twice to resolve cross-references)
xelatex -synctex=1 -interaction=nonstopmode exam_paper_60mins_en.tex
xelatex -synctex=1 -interaction=nonstopmode exam_paper_60mins_en.tex

# 2. Compile solutions and grading guide (run twice)
xelatex -synctex=1 -interaction=nonstopmode exam_solution_60mins_en.tex
xelatex -synctex=1 -interaction=nonstopmode exam_solution_60mins_en.tex
```
