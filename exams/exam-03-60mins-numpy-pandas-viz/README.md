# Midterm Examination: NumPy, Pandas & Visualization (60 Minutes)
## Course: Data Analysis with Python (DSAI1005)

- **Department:** Faculty of Data Science & AI – National Economics University (NEU)
- **Course Code:** DSAI1005
- **Exam Code:** `301-EN`
- **Duration:** 60 minutes
- **Format:** Paper-based written examination formatted identically to [`exams/exam-02-lectures-1-4/exam_paper_lectures_1_4_en.tex`](../exam-02-lectures-1-4/exam_paper_lectures_1_4_en.tex)
- **Difficulty Balance:**
  - **60% Easy & Basic Foundational Questions** (Section I: Multiple-Choice)
  - **40% Medium-Level Integrated Problems** (Section II: Applied Coding)
- **Total Score:** 10.0 Points (100%)
- **Target Page Count:** Exactly 6 pages (`Page 1/6` through `Page 6/6`)

---

## 🎯 Exam Structure & Grade Distribution

The examination strictly follows the specified syllabus and difficulty breakdown:

### Section I: Multiple-Choice Questions (6.0 pts / 60% --- Easy & Basic)
*12 questions $\times$ 0.5 pt each = 6.0 pts (evaluated directly on the top answer sheet grid on Page 1)*
- **NumPy (20% / 2.0 pts):**
  - **Q1 (0.5 pt):** Array creation with `np.linspace(0, 10, 5)` and element-wise arithmetic vectorization with `np.arange`.
  - **Q2 (0.5 pt):** Basic step slicing `m[::-1, 1]` memory view mutation vs independent copy behavior.
  - **Q3 (0.5 pt):** Multi-dimensional broadcasting rules across shapes `(4, 1, 6)` and `(3, 1)`.
  - **Q4 (0.5 pt):** Compound bitwise conditional filtering with `np.where` and column-wise reduction along `axis=0`.
- **Pandas (20% / 2.0 pts):**
  - **Q5 (0.5 pt):** Series arithmetic `.add(fill_value=0)` across non-identical string index sets.
  - **Q6 (0.5 pt):** Indexing boundary semantics: inclusive label slicing with `.loc` vs half-open positional `.iloc`.
  - **Q7 (0.5 pt):** Chained multi-level aggregation `.groupby(['Region', 'Category'])['Sales'].agg(['sum', 'count'])`.
  - **Q8 (0.5 pt):** SQL left join semantics: preserving left table row count ($N=500$) with `NaN` insertion for unmatched right keys.
- **Data Visualization (20% / 2.0 pts):**
  - **Q9 (0.5 pt):** Matplotlib Object-Oriented 2D subplot array indexing `axes[row, col]` and `.set_title()`.
  - **Q10 (0.5 pt):** Boxplot outlier detection via Tukey whisker fences ($Q_1/Q_3 \pm 1.5 \times IQR$) for skewed financial distributions.
  - **Q11 (0.5 pt):** Seaborn semantic channels: `hue` for distinct colors, `style` for marker glyphs.
  - **Q12 (0.5 pt):** Heatmap correlation coefficient overlays (`annot=True`) and subplot margin padding (`plt.tight_layout()`).

---

### Section II: Applied Coding & Short-Answer (4.0 pts / 40% --- Medium Difficulty)
*Integrated multi-step pipelines requiring synthesized understanding of data operations and visualization*
- **Question 1: Vectorized Computations & Tabular Aggregation (2.0 pts) [NumPy & Pandas]:**
  - Scenario: Batch processing of e-commerce transactions across a $5 \times 4$ numerical array `tx_data`.
  - Tasks a–e (5 tasks $\times$ 0.4 pt each):
    - *a) Net Revenue formula:* Vectorized 2D slice arithmetic with column weights and discounts.
    - *b) Vectorized classification:* `np.where` with compound boolean conditions (`|`).
    - *c) Left Merge:* Joining order records with customer master profile DataFrame.
    - *d) Multi-level Aggregation:* Chained `.groupby(['city', 'tier'])['net_rev'].agg(['sum', 'count'])`.
    - *e) Sorting:* Sorting MultiIndex summary table by total revenue descending.
  - Answer area: Ruled answer box (`\answerbox{6.5cm}`) with `\dotfill` guides on Page 4.
- **Question 2: Multi-Panel Visual Analytics & Outlier Detection (1.5 pts) [Pandas & Seaborn]:**
  - Scenario: Multi-channel sales performance and fraud anomaly monitoring dashboard.
  - Tasks a–b:
    - *a) Canvas initialization (0.5 pt):* Matplotlib OO `plt.subplots(1, 2, figsize=(14, 5))` grid unpacking.
    - *b) Stratified Boxplot (1.0 pt):* Complete `sns.boxplot()` call with `x='payment'`, `y='amount'`, `hue='is_fraud'`, and `palette='Set2'` targeted to `axes[0]`.
  - Answer area: Ruled answer box (`\answerbox{12.8cm}`) with `\dotfill` guides on Page 5.
- **Question 3: Time-Series Revenue Trajectory & Executive Decision-Making (0.5 pts) [Pandas & Viz Insights]:**
  - Scenario: Revenue trend smoothing and forecasting.
  - Tasks a–b:
    - *a) Trend calculation (0.3 pt):* Weekly resampling, 4-week rolling moving average (`weekly_sales.rolling(4).mean()`), and `plt.tight_layout()`.
    - *b) Analytical Takeaways (0.2 pt):* Formulating two concise data-driven policies on boxplot whisker outliers and rolling moving average smoothing for forecasting.
  - Answer area: Ruled answer box (`\answerbox{9.2cm}`) with `\dotfill` guides on Page 6.

---

## 📁 Exam Package Directory

| File | Format | Description | Pages |
| :--- | :---: | :--- | :---: |
| [exam_paper_60mins_en.tex](exam_paper_60mins_en.tex) | `.tex` | XeLaTeX source code for official student exam paper (exam-02 format) | 6 |
| [exam_paper_60mins_en.pdf](exam_paper_60mins_en.pdf) | `.pdf` | Compiled student exam paper with 12-cell MCQ top grid and ruled answer boxes | **6** |
| [exam_solution_60mins_en.tex](exam_solution_60mins_en.tex) | `.tex` | XeLaTeX source code for Instructor Solutions & Grading Guide | 4 |
| [exam_solution_60mins_en.pdf](exam_solution_60mins_en.pdf) | `.pdf` | Compiled master answer key, in-depth technical rationales & grading rubrics | 4 |
| [README.md](README.md) | `.md` | Documentation of exam structure, difficulty distribution, and compilation guides | — |

---

## 📄 Detailed Page-by-Page Layout (Student Exam Paper)

- **Page 1:** Administrative header, course metadata, examiner grading table, student info line, **12-cell Multiple-Choice Answer Sheet**, Section I header, Questions 1 to 3 (NumPy).
- **Page 2:** Question 4 (NumPy), Questions 5 to 8 (Pandas).
- **Page 3:** Questions 9 to 12 (Data Visualization).
- **Page 4:** Section II header, Question 1 (NumPy & Pandas Pipeline: scenario, array listing, tasks a to e, and ruled answer box).
- **Page 5:** Question 2 (Multi-Panel Visual Analytics: scenario, schema listing, tasks a & b, axes formatting listing, and ruled answer box).
- **Page 6:** Question 3 (Time-Series Trajectory & Executive Takeaways: scenario, timeseries listing, tasks a & b, ruled answer box, and `--- END OF EXAM ---`).

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
