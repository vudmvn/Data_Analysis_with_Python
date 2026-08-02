# What Is Statistical Analysis?

**Last updated:** August 2, 2026

## Lesson Introduction

This lesson introduces the foundations of **statistical analysis**, from collecting and organizing data to descriptive, inferential, exploratory, predictive, prescriptive, and causal methods. It emphasizes the use of data and evidence to support decisions, test hypotheses, evaluate uncertainty, and interpret results responsibly.

The lesson combines statistical concepts, basic formulas, Python examples, application scenarios, and review questions. It provides learners with an overview of the role of statistics in data analysis, scientific research, and management.

## Learning Outcomes

After completing this lesson, learners will be able to:

- Explain the concept and role of statistical analysis.
- Describe four major stages: data collection, data organization, data analysis, and interpretation and presentation.
- Distinguish between descriptive and inferential statistics.
- Distinguish between Exploratory Data Analysis (EDA) and Confirmatory Data Analysis (CDA).
- Recognize the roles of regression, hypothesis testing, confidence intervals, and ANOVA.
- Calculate and interpret the mean, variance, and standard deviation at a basic level.
- Distinguish predictive, prescriptive, and causal analysis.
- Explain the difference between correlation and causation.
- Recognize the basic uses of R, Python, SPSS, and Excel.
- Select suitable tools and methods for different analytical objectives.
- Present statistical results using reports, charts, dashboards, or presentations.
- State limitations, uncertainty, and practical implications of results.
- Apply statistical concepts in business, healthcare, education, social science, and environmental contexts.

## Lesson Structure

The lesson covers:

1. The concept and role of statistical analysis.
2. Data collection.
3. Data organization and cleaning.
4. Data analysis using EDA, CDA, regression, and hypothesis testing.
5. Interpretation and presentation.
6. Descriptive statistics.
7. Inferential statistics.
8. Exploratory Data Analysis.
9. Predictive modeling.
10. Prescriptive analysis.
11. Causal analysis.
12. Statistical analysis tools.
13. Importance and applications.
14. Review questions and case-based exercises.

## Prerequisites

Learners should have:

- Basic mathematical knowledge of means and proportions.
- An introductory understanding of data, variables, samples, and populations.
- Basic Python knowledge for the coding examples.
- Access to Jupyter Notebook, JupyterLab, or Google Colab.
- The `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`, `statsmodels`, and `scikit-learn` libraries.

Install the required libraries with:

```bash
pip install numpy pandas scipy matplotlib seaborn statsmodels scikit-learn
```

---

Statistical analysis is the process of examining data to understand it more clearly and extract useful insights. It helps identify patterns, relationships, and trends, thereby supporting decision-making and forecasting.

<p align="center">
  <img src="images/image-26.png" alt="Statistical analysis overview" />
</p>

### Quick Check

**Question 1.** What is the main objective of statistical analysis?

A. Only to store data  
B. To understand data and extract useful information  
C. Only to create charts  
D. To completely replace humans in decision-making  

**Question 2. True or false?** Statistical analysis can help identify patterns, relationships, and trends in data.

---

<p align="center">
  <img src="images/image-27.png" alt="Statistical analysis process" />
</p>

# Steps in Statistical Analysis

Statistical analysis is usually carried out through a structured process to ensure that results are accurate and meaningful. This process supports effective data collection, preparation, analysis, and communication.

---

## 1. Collect Data

Data collection is the first step in statistical analysis. The data must have sufficient reliability and quality for the results to be meaningful.

### Possible Data Sources

- Surveys.
- Observations.
- Experiments.
- Internal databases.
- Administrative data.
- APIs.
- Public datasets.
- Sensors.

### Data Requirements

- Relevant to the research objective.
- Collected from trustworthy sources.
- Sufficient in size.
- Collected using a clear method.
- Designed to minimize bias and missingness.

### Example

A company that wants to assess customer satisfaction may collect information through questionnaires, purchase histories, online feedback, and customer-service records.

### Quick Check

**Question 1.** Why should high-quality data be collected?

A. To increase the number of columns  
B. To ensure reliable analytical results  
C. To eliminate the need for cleaning  
D. To replace interpretation  

**Question 2.** Which can be used as a data source?

A. Surveys  
B. APIs  
C. Databases  
D. All of the above  

---

## 2. Organize the Data

After collection, data must be cleaned and organized before they can be analyzed correctly.

### Main Tasks

- Use spreadsheets, databases, or programming tools.
- Handle missing values.
- Correct errors or inconsistent values.
- Remove duplicate records.
- Standardize formats.
- Check data types.
- Arrange the data in a suitable structure.

### Possible Tools

- Microsoft Excel.
- Google Sheets.
- SQL.
- Python with Pandas.
- R with `dplyr` and `tidyr`.
- Database software.

### Python Example

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
```

### Handle Missing Data

```python
df["age"] = df["age"].fillna(
    df["age"].median()
)
```

### Remove Duplicates

```python
df = df.drop_duplicates()
```

### Quick Check

**Question 1.** Which activity belongs to data organization?

A. Handling missing values  
B. Correcting inconsistent data  
C. Removing duplicates  
D. All of the above  

**Question 2.** Which tool is suitable for handling tabular data in Python?

A. Pandas  
B. Matplotlib  
C. Seaborn  
D. TensorFlow  

**Question 3. True or false?** Collected data are always immediately ready for analysis.

---

## 3. Analyze the Data

At this stage, statistical techniques are applied to explore the data and extract useful insights.

### Common Methods

#### Exploratory Data Analysis

**Exploratory Data Analysis (EDA)** is used to understand the data and identify patterns, trends, and unusual observations.

Common techniques include:

- Descriptive statistics.
- Histograms.
- Box plots.
- Scatter plots.
- Correlation matrices.
- Outlier detection.

#### Confirmatory Data Analysis

**Confirmatory Data Analysis (CDA)** is used to test hypotheses or confirm conclusions formulated in advance.

#### Regression Analysis

Regression analysis studies the relationship between a dependent variable and one or more independent variables.

Examples:

- Predicting sales from advertising expenditure.
- Estimating house prices from area and location.
- Studying the effect of study time on examination scores.

#### Hypothesis Testing

Hypothesis testing evaluates whether an observed result is statistically significant or may have occurred by chance.

### Quick Check

**Question 1.** What is EDA mainly used for?

A. Exploring data and identifying patterns  
B. Only presenting reports  
C. Only storing data  
D. Only creating optimization models  

**Question 2.** CDA is commonly used to:

A. Test hypotheses  
B. Delete data  
C. Create spreadsheets  
D. Collect data  

**Question 3.** Regression analysis is used to:

A. Study relationships among variables  
B. Process text only  
C. Create pie charts only  
D. Remove every outlier  

**Question 4. True or false?** Hypothesis testing helps determine whether a result is statistically significant.

---

## 4. Interpret and Present Results

After analysis, results must be explained and presented clearly so that others can understand and use them.

### Presentation Formats

- Reports.
- Charts.
- Graphs.
- Dashboards.
- Presentations.
- Statistical tables.
- Executive summaries.

### Presentation Principles

- State the analytical objective clearly.
- Explain the method used.
- Present the main findings.
- Discuss practical meaning.
- State limitations.
- Recommend next actions.
- Avoid overinterpreting statistical results.

### Example

If an analysis shows that sales declined sharply in one region, a report should not provide only the percentage decline. It should explain:

- Which region was affected.
- How large the decline was.
- How long the trend lasted.
- Which factors may be related.
- Which actions the company should consider.

### Quick Check

**Question 1.** Which format can be used to present results?

A. Reports  
B. Charts  
C. Dashboards  
D. All of the above  

**Question 2.** Why should analytical limitations be stated?

A. So readers understand the scope and reliability of the results  
B. To make the report longer  
C. To avoid presenting results  
D. To replace the data  

---

# Types of Statistical Analysis

There are six major types of statistical analysis:

1. Descriptive statistics.
2. Inferential statistics.
3. Exploratory Data Analysis.
4. Predictive modeling.
5. Prescriptive analysis.
6. Causal analysis.

<p align="center">
  <img src="images/image-28.png" alt="Types of statistical analysis" />
</p>

---

## 1. Descriptive Statistics

Descriptive statistics summarize and organize data so that readers can quickly understand the main characteristics.

### Common Techniques

- Measures of central tendency.
- Variance.
- Standard deviation.
- Histograms.
- Bar charts.
- Box plots.

### Central Tendency

Common measures include:

- **Mean:** The sum of values divided by the number of observations.
- **Median:** The middle value after sorting.
- **Mode:** The most frequently occurring value.

### Mean Formula

$$
\bar{x}
=
\frac{1}{n}
\sum_{i=1}^{n}x_i
$$

### Sample Variance

$$
s^2
=
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}{
n-1
}
$$

### Sample Standard Deviation

$$
s
=
\sqrt{
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}{
n-1
}
}
$$

### Python Example

```python
print(df.describe())
print(df["income"].mean())
print(df["income"].median())
print(df["income"].std())
```

### Quick Check

**Question 1.** Descriptive statistics are used to:

A. Summarize data  
B. Prove causation  
C. Build deep-learning models only  
D. Forecast the future only  

**Question 2.** Which measure describes data dispersion?

A. Standard deviation  
B. Mode  
C. Median  
D. Variable name  

**Question 3.** Which chart is commonly used to detect outliers?

A. Box plot  
B. Pie chart  
C. Line chart  
D. Map  

---

## 2. Inferential Statistics

Inferential statistics use sample data to draw conclusions or make predictions about a larger population.

### Common Techniques

- Hypothesis testing.
- Confidence intervals.
- Regression analysis.
- Analysis of variance.
- Parameter estimation.

### Sample and Population

- **Population:** The complete group of interest.
- **Sample:** A subset selected from the population.

### Example

A university has 20,000 students. Instead of surveying all students, a researcher may select a sample of 1,000 students to estimate overall satisfaction.

### Confidence Interval

A confidence interval provides a range of plausible values for a population parameter.

### Quick Check

**Question 1.** Inferential statistics use sample data to:

A. Draw conclusions about a population  
B. Describe the sample only  
C. Create charts only  
D. Remove data  

**Question 2.** Which technique belongs to inferential statistics?

A. Hypothesis testing  
B. Confidence intervals  
C. ANOVA  
D. All of the above  

**Question 3. True or false?** A sample is the complete group of interest.

---

## 3. Exploratory Data Analysis

EDA focuses on understanding data before model building.

### Objectives

- Understand data structure.
- Detect patterns.
- Examine relationships.
- Detect missing data.
- Identify outliers.
- Check initial assumptions.

### Common Techniques

- Scatter plots.
- Correlation analysis.
- Distribution analysis.
- Outlier detection.

### Python Example

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(
    df["income"],
    kde=True
)

plt.title("Income Distribution")
plt.show()
```

### Quick Check

**Question 1.** When is EDA commonly performed?

A. Before model building  
B. Only after model deployment  
C. After deleting the data  
D. It is unrelated to modeling  

**Question 2.** Which technique belongs to EDA?

A. Scatter plots  
B. Correlation analysis  
C. Outlier detection  
D. All of the above  

---

## 4. Predictive Modeling

Predictive models use historical data to forecast future outcomes or trends.

### Common Methods

- Linear regression.
- Decision trees.
- Neural networks.
- Support Vector Machines.
- Random Forest.
- Time-series models.

### Applications

- Sales forecasting.
- Demand forecasting.
- Credit-risk prediction.
- Churn prediction.
- Price forecasting.

### Python Example

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

y_pred = model.predict(
    X_test
)
```

### Quick Check

**Question 1.** Predictive models use:

A. Historical data  
B. Text data only  
C. Missing data only  
D. No data  

**Question 2.** Which method can be used for prediction?

A. Linear regression  
B. Decision trees  
C. Neural networks  
D. All of the above  

---

## 5. Prescriptive Analysis

Prescriptive analysis recommends the best actions based on data. It goes beyond prediction by proposing solutions that can help achieve desired outcomes.

### Common Methods

- Optimization techniques.
- Simulation models.
- Decision theory.
- Scenario analysis.
- Multi-objective optimization.

### Applications

- Selecting an optimal price.
- Designing a production schedule.
- Optimizing delivery routes.
- Allocating an advertising budget.
- Selecting an investment portfolio.

### Quick Check

**Question 1.** Which question does prescriptive analysis answer?

A. What happened?  
B. Why did it happen?  
C. What may happen?  
D. What should we do?  

**Question 2.** Which techniques are commonly used in prescriptive analysis?

A. Optimization  
B. Simulation  
C. Decision theory  
D. All of the above  

---

## 6. Causal Analysis

Causal analysis evaluates whether one variable causes a change in another.

### Common Methods

- Randomized experiments.
- Regression models.
- Propensity-score matching.
- A/B testing.
- Instrumental variables.
- Difference-in-differences.

### Example

A company wants to determine whether a promotion truly increases sales or merely coincides with a period of naturally rising demand.

### Correlation and Causation

Correlation indicates that two variables are associated. It is not sufficient to establish causation.

For example:

- Ice-cream sales and the number of fires may both rise during summer.
- This does not mean that selling ice cream causes fires.
- High temperature may affect both variables.

### Quick Check

**Question 1.** The objective of causal analysis is to:

A. Identify cause-and-effect relationships  
B. Summarize data only  
C. Calculate means only  
D. Create dashboards only  

**Question 2.** Which method may be used in causal analysis?

A. Randomized experiments  
B. Propensity-score matching  
C. Regression models  
D. All of the above  

**Question 3. True or false?** A strong correlation always proves causation.

---

# Statistical Analysis Tools

## R

R is a programming language widely used for statistical computing and data visualization.

### Strengths

- Many statistical packages.
- Strong visualization support.
- Suitable for academic research.
- Large community.

## Python

Python provides many libraries for data analysis and modeling.

### Common Libraries

- **NumPy:** Numerical computing.
- **Pandas:** Data processing.
- **SciPy:** Statistical methods.
- **Scikit-learn:** Machine learning.
- **Matplotlib:** Visualization.
- **Seaborn:** Statistical visualization.
- **Statsmodels:** Statistical modeling.

## SPSS

SPSS is widely used in social-science research.

### Strengths

- User-friendly interface.
- Supports many statistical tests.
- Suitable for users with limited programming experience.

## Microsoft Excel

Excel is suitable for basic statistical calculations and simple visualizations.

### Strengths

- Easy to use.
- Suitable for small datasets.
- Supports PivotTables.
- Provides basic statistical functions.

### Comparison

| Tool | Main purpose | Key feature |
|---|---|---|
| **R** | Statistics and visualization | Many specialized statistical packages |
| **Python** | Data analysis and modeling | Flexible and well integrated with machine learning |
| **SPSS** | Social-science research | User-friendly graphical interface |
| **Excel** | Basic analysis | Widely available and accessible |

### Quick Check

**Question 1.** Which tool is a programming language widely used for statistics?

A. R  
B. SPSS  
C. Excel  
D. PowerPoint  

**Question 2.** Which Python libraries are commonly used for statistical methods?

A. SciPy  
B. Pandas  
C. Statsmodels  
D. Both A and C  

**Question 3.** Which tool is widely used in social-science research?

A. SPSS  
B. Matplotlib  
C. NumPy  
D. Git  

---

# The Importance of Statistical Analysis

Statistical analysis plays an important role in many decision-making activities.

## Data-Driven Decision-Making

Statistical analysis replaces guesswork with decisions based on data and evidence.

## Evaluating and Reducing Uncertainty

Probability models help evaluate uncertainty and risk.

## Testing Ideas

Statistical analysis supports hypothesis testing and the confirmation of findings.

## Evaluating Performance

Statistical analysis helps measure:

- KPIs.
- Productivity.
- Business growth.
- Product quality.
- Campaign effectiveness.
- Satisfaction levels.

### Quick Check

**Question 1.** Statistical analysis helps replace:

A. Guesswork with data-driven decisions  
B. Data with intuition  
C. Reports with speech  
D. Processes with randomness  

**Question 2.** Probability models support:

A. Evaluating uncertainty  
B. Eliminating all risk  
C. Removing data  
D. Creating charts only  

---

# Applications of Statistical Analysis

## Business and Markets

Statistical analysis supports:

- Market research.
- Quality control.
- Customer analysis.
- Financial decision-making.
- Business-performance measurement.

## Healthcare and Public Health

Statistical analysis is used in:

- Medical research.
- Public-health analysis.
- Drug-safety evaluation.
- Disease surveillance.
- Treatment-effectiveness assessment.

## Education

Statistical analysis can help:

- Evaluate learning outcomes.
- Improve teaching methods.
- Develop educational policy.
- Identify students who need support.

## Social Sciences

Statistical analysis supports:

- Human-behavior research.
- Social-trend analysis.
- Population studies.
- Public-policy evaluation.

## Environment

Statistical analysis is used to:

- Analyze climate.
- Monitor pollution.
- Evaluate resources.
- Support conservation.
- Forecast environmental risk.

### Quick Check

**Question 1.** Statistical analysis can be applied in:

A. Healthcare  
B. Education  
C. The environment  
D. All of the above  

**Question 2.** In education, statistical analysis can help:

A. Evaluate learning outcomes  
B. Improve teaching methods  
C. Support policy development  
D. All of the above  

**Question 3. Case.** A hospital wants to evaluate the effectiveness of a new treatment. How can statistical analysis support this task?

---

# Content Summary

| Topic | Main objective |
|---|---|
| **Data collection** | Obtain quality data from appropriate sources |
| **Data organization** | Clean and structure the data |
| **Data analysis** | Apply statistical techniques |
| **Interpretation and presentation** | Communicate results clearly |
| **Descriptive statistics** | Summarize data characteristics |
| **Inferential statistics** | Generalize from a sample to a population |
| **EDA** | Explore patterns and data problems |
| **Predictive modeling** | Forecast future outcomes |
| **Prescriptive analysis** | Recommend actions |
| **Causal analysis** | Identify cause-and-effect relationships |

---

# End-of-Lesson Review

## Part A. Multiple-Choice Questions

**Question 1.** Statistical analysis is the process of:

A. Only storing data  
B. Examining data to extract useful information  
C. Only designing charts  
D. Only building deep-learning models  

**Question 2.** The first step in statistical analysis is:

A. Data collection  
B. Presenting results  
C. Building a model  
D. Hypothesis testing  

**Question 3.** Which activity belongs to data organization?

A. Handling missing values  
B. Correcting errors  
C. Standardizing formats  
D. All of the above  

**Question 4.** Which method is used to explore patterns in data?

A. EDA  
B. CDA  
C. Optimization  
D. Simulation  

**Question 5.** Inferential statistics use:

A. Sample data to draw conclusions about a population  
B. Population data only  
C. Charts only  
D. Text data only  

**Question 6.** Which type of analysis forecasts future outcomes?

A. Predictive modeling  
B. Descriptive statistics  
C. EDA  
D. Missing-data analysis  

**Question 7.** Which type of analysis recommends the best action?

A. Prescriptive analysis  
B. Descriptive statistics  
C. EDA  
D. Data validation  

**Question 8.** Which type of analysis studies cause and effect?

A. Causal analysis  
B. Descriptive analysis  
C. Missing-data analysis  
D. Visual analysis  

**Question 9.** Which tool is widely used in social science?

A. SPSS  
B. Git  
C. HTML  
D. CSS  

**Question 10.** Which statement is correct?

A. Correlation always proves causation  
B. Statistical analysis supports evidence-based decision-making  
C. Data do not need cleaning  
D. A sample is always equal to the population  

## Part B. True/False Questions

**Question 1.** Statistical analysis is used only in business.

**Question 2.** Data should be organized before analysis.

**Question 3.** EDA helps identify patterns and unusual values.

**Question 4.** Descriptive statistics are used to generalize from a sample to a population.

**Question 5.** Inferential statistics may use hypothesis testing.

**Question 6.** Prescriptive analysis only forecasts the future and does not recommend action.

**Question 7.** Causal analysis is different from correlation analysis.

**Question 8.** Presenting results is part of statistical analysis.

## Part C. Short-Answer Questions

**Question 1.** Present the four main steps in statistical analysis.

**Question 2.** Distinguish between descriptive and inferential statistics.

**Question 3.** Distinguish between EDA and CDA.

**Question 4.** Distinguish between predictive modeling and prescriptive analysis.

**Question 5.** Why does correlation not prove causation?

**Question 6.** Name four statistical-analysis tools and state their main uses.

## Part D. Case-Based Exercises

### Exercise 1. Customer Satisfaction Analysis

A company collects ratings from 500 customers.

1. Define the analytical objective.
2. State the data-cleaning steps.
3. Propose three descriptive statistics.
4. Propose two suitable charts.
5. Explain how the results should be presented to managers.

### Exercise 2. Evaluating a Teaching Method

A school wants to know whether a new teaching method improves test scores.

1. Identify the population and sample.
2. Propose a research hypothesis.
3. Select an appropriate type of analysis.
4. State possible confounding factors.
5. Explain why causal conclusions require caution.

### Exercise 3. Sales Forecasting

A company has three years of sales data.

1. State the data-preparation steps.
2. Propose a predictive model.
3. Explain how training and test data should be divided.
4. Suggest evaluation metrics.
5. Explain how the results can support business decisions.

---

# References and Useful Links

The references below cover the tools, libraries, and methods discussed in the lesson, including descriptive statistics, inferential statistics, regression, hypothesis testing, machine learning, and visualization.

1. [What is Statistical Analysis? — GeeksforGeeks](https://www.geeksforgeeks.org/data-analysis/what-is-statistical-analysis/)  
   Introductory reference on the concept, process, types, and applications of statistical analysis.

2. [NumPy Documentation](https://numpy.org/doc/stable/)  
   Official NumPy documentation for numerical computing in Python.

3. [Pandas Documentation](https://pandas.pydata.org/docs/)  
   Official Pandas documentation for data organization, cleaning, and processing.

4. [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)  
   Official documentation for statistical methods in SciPy.

5. [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
   Official documentation for predictive models and machine learning.

6. [Statsmodels Documentation](https://www.statsmodels.org/stable/index.html)  
   Official documentation for statistical modeling, regression, and hypothesis testing.

7. [R Project for Statistical Computing](https://www.r-project.org/)  
   Official website of the R programming language.

8. [IBM SPSS Statistics](https://www.ibm.com/products/spss-statistics)  
   Information about SPSS for statistical analysis.

9. [Microsoft Excel](https://www.microsoft.com/microsoft-365/excel)  
   Spreadsheet software for basic statistical calculations and visualizations.

> **Note:** Prefer official documentation because syntax, parameters, and features may change between versions.

---

# Answers and Suggested Responses

<details>
<summary><strong>Click to show answers</strong></summary>

## Quick Check — Introduction

### Question 1

B. To understand data and extract useful information.

### Question 2

True.

## Quick Check — Data Collection

### Question 1

B. To ensure reliable analytical results.

### Question 2

D. All of the above.

## Quick Check — Data Organization

### Question 1

D. All of the above.

### Question 2

A. Pandas.

### Question 3

False. Data usually require cleaning and organization before analysis.

## Quick Check — Data Analysis

### Question 1

A. Exploring data and identifying patterns.

### Question 2

A. Testing hypotheses.

### Question 3

A. Studying relationships among variables.

### Question 4

True.

## Quick Check — Interpretation and Presentation

### Question 1

D. All of the above.

### Question 2

A. So readers understand the scope and reliability of the results.

## Quick Check — Descriptive Statistics

### Question 1

A. Summarizing data.

### Question 2

A. Standard deviation.

### Question 3

A. Box plot.

## Quick Check — Inferential Statistics

### Question 1

A. Drawing conclusions about a population.

### Question 2

D. All of the above.

### Question 3

False. A sample is a subset of a population.

## Quick Check — EDA

### Question 1

A. Before model building.

### Question 2

D. All of the above.

## Quick Check — Predictive Modeling

### Question 1

A. Historical data.

### Question 2

D. All of the above.

## Quick Check — Prescriptive Analysis

### Question 1

D. What should we do?

### Question 2

D. All of the above.

## Quick Check — Causal Analysis

### Question 1

A. Identifying cause-and-effect relationships.

### Question 2

D. All of the above.

### Question 3

False. Correlation is not sufficient to establish causation.

## Quick Check — Tools

### Question 1

A. R.

### Question 2

D. Both A and C.

### Question 3

A. SPSS.

## Quick Check — Importance

### Question 1

A. Guesswork with data-driven decisions.

### Question 2

A. Evaluating uncertainty.

## Quick Check — Applications

### Question 1

D. All of the above.

### Question 2

D. All of the above.

### Question 3

Statistical analysis can compare outcomes between treatment and control groups, test hypotheses, estimate confidence intervals, and assess confounding factors.

## Part A. Multiple-Choice Answers

1. B  
2. A  
3. D  
4. A  
5. A  
6. A  
7. A  
8. A  
9. A  
10. B  

## Part B. True/False Answers

1. False.  
2. True.  
3. True.  
4. False.  
5. True.  
6. False.  
7. True.  
8. True.  

## Part C. Suggested Responses

### Question 1

The four main steps are data collection, data organization, data analysis, and interpretation and presentation.

### Question 2

Descriptive statistics summarize the characteristics of observed data. Inferential statistics use sample data to draw conclusions about a population.

### Question 3

EDA focuses on exploring data and generating initial insights. CDA focuses on testing hypotheses or confirming predefined conclusions.

### Question 4

Predictive modeling estimates what may happen. Prescriptive analysis recommends what action should be taken.

### Question 5

A third variable, reverse causality, or a coincidental association may exist. Correlation measures association only.

### Question 6

R is used for statistical computing; Python is used for analysis and modeling; SPSS is suitable for social-science research; Excel is suitable for basic analysis.

## Part D

These are open exercises. A complete submission should clearly state the objective, data, method, results, and interpretation. Conclusions should remain consistent with the evidence and should not exceed what the statistical analysis supports.

</details>
