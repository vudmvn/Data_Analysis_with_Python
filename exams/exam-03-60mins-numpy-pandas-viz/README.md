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
  - **Q1 (0.5 pt):** Array creation with `np.arange(2, 11, 2)` evaluating half-open sequence boundaries.
  - **Q2 (0.5 pt):** Basic array attributes: verifying 2D matrix shape `(2, 3)` and dimensions `ndim = 2`.
  - **Q3 (0.5 pt):** Standard 2D matrix indexing `m[row, col]` accessing element `m[1, 2]`.
  - **Q4 (0.5 pt):** Direction of axis reduction: column-wise mean computation via `np.mean(arr, axis=0)`.
- **Pandas (20% / 2.0 pts):**
  - **Q5 (0.5 pt):** Core data structure definitions: 1D labeled `Series` vs 2D tabular `DataFrame`.
  - **Q6 (0.5 pt):** Positional integer row access using `df.iloc[0]`.
  - **Q7 (0.5 pt):** Missing value counting across columns via `df.isna().sum()`.
  - **Q8 (0.5 pt):** Standard boolean filtering syntax: bitwise `&` operator and parentheses `df[(cond1) & (cond2)]`.
- **Data Visualization (20% / 2.0 pts):**
  - **Q9 (0.5 pt):** Chart selection for chronological trends: Line chart for continuous time-series metrics.
  - **Q10 (0.5 pt):** Distribution & 5-number summary tool: Box plot (`sns.boxplot`) with whisker outlier flagging.
  - **Q11 (0.5 pt):** Seaborn semantic channel: `hue='Gender'` mapping categorical groups to distinct colors.
  - **Q12 (0.5 pt):** Matplotlib layout management: `plt.tight_layout()` preventing title and label clipping.

---

### Section II: Applied Coding & Short-Answer (4.0 pts / 40% --- Medium Difficulty)
*Integrated multi-step problems on an intuitive retail sales dataset (`df`)*
- **Question 1: Retail Sales Analysis with NumPy & Pandas (2.0 pts) [Medium]:**
  - Scenario: Retail orders DataFrame `df` with `OrderID`, `Category`, `Price`, `Quantity`, `Discount`.
  - Tasks a–e (5 tasks $\times$ 0.4 pt each):
    - *a) Net Revenue formula:* Vectorized column arithmetic: `df['Price'] * df['Quantity'] * (1 - df['Discount'])`.
    - *b) Conditional classification:* `np.where((df['Revenue'] >= 1000) | (df['Quantity'] >= 5), 'High', 'Standard')`.
    - *c) Filtering:* Filtering Tech orders with quantity at least 2: `df[(df['Category'] == 'Tech') & (df['Quantity'] >= 2)]`.
    - *d) Groupby Aggregation:* Computing total and mean revenue: `df.groupby('Category')['Revenue'].agg(['sum', 'mean'])`.
    - *e) Sorting:* Ordering summary table by total revenue descending: `summary.sort_values(by='sum', ascending=False)`.
  - Answer area: Ruled answer box (`\answerbox{7.2cm}`) with `\dotfill` guides on Page 4.
- **Question 2: Sales Performance Visualization with Matplotlib & Seaborn (1.5 pts) [Medium]:**
  - Scenario: 2-panel figure visualizing sales performance and distribution across categories.
  - Tasks a–b:
    - *a) Canvas initialization (0.5 pt):* Matplotlib OO canvas: `fig, axes = plt.subplots(1, 2, figsize=(12, 4))`.
    - *b) Seaborn plotting (1.0 pt):*
      - Subplot 1 (0.5 pt): `sns.barplot(data=df, x='Category', y='Revenue', ax=axes[0])`.
      - Subplot 2 (0.5 pt): `sns.boxplot(data=df, x='Category', y='Revenue', ax=axes[1])`.
  - Answer area: Ruled answer box (`\answerbox{13.0cm}`) with `\dotfill` guides on Page 5.
- **Question 3: Layout Optimization & Chart Interpretation (0.5 pts) [Medium]:**
  - Tasks a–b:
    - *a) Layout optimization (0.25 pt):* `plt.tight_layout()` to prevent overlapping subplots and labels.
    - *b) Outlier interpretation (0.25 pt):* Explaining how boxplot whiskers ($1.5 \times IQR$) delineate normal range from statistical outliers plotted as individual dots.
  - Answer area: Ruled answer box (`\answerbox{10.0cm}`) with `\dotfill` guides on Page 6.

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
- **Page 4:** Section II header, Question 1 (Retail Sales Analysis: scenario, DataFrame table, tasks a to e, and ruled answer box).
- **Page 5:** Question 2 (Sales Performance Visualization: scenario, tasks a & b, and ruled answer box).
- **Page 6:** Question 3 (Layout Optimization & Outlier Interpretation: scenario, tasks a & b, ruled answer box, and `--- END OF EXAM ---`).

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
