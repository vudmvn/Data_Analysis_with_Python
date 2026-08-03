# Introduction to NumPy

**language:** "en" | **date_updated:** "August 3, 2026"

## Lesson Introduction

This lesson introduces **NumPy**, a core Python library for numerical computing. NumPy is designed for efficient work with large arrays, matrices, and numerical datasets. Its central data structure, the `ndarray`, supports fast mathematical operations, broadcasting, linear algebra, random-number generation, and statistical calculations.

Compared with ordinary Python lists, NumPy arrays store homogeneous data more compactly and support vectorized operations implemented in optimized low-level code. This makes NumPy especially useful in data analysis, scientific computing, simulation, image processing, and machine learning.

## Learning Outcomes

After completing this lesson, learners will be able to:

- Explain the purpose of NumPy in numerical computing.
- Distinguish NumPy arrays from ordinary Python lists.
- Install and import NumPy.
- Create one-dimensional and multidimensional arrays.
- Inspect array properties such as shape, size, dimension, and data type.
- Access elements using indexing and slicing.
- Reshape, resize, stack, and split arrays.
- Apply vectorized arithmetic operations.
- Use aggregation functions such as `sum()`, `mean()`, `min()`, and `max()`.
- Explain and apply broadcasting.
- Use common mathematical and universal functions.
- Perform basic matrix and vector operations.
- Generate random values from common probability distributions.
- Calculate basic descriptive statistics.
- Understand how NumPy integrates with Pandas, SciPy, and Scikit-learn.

## Lesson Structure

The lesson covers:

1. What NumPy is.
2. Why NumPy is useful.
3. Installation and importing.
4. Creating NumPy arrays.
5. Array properties.
6. Indexing and slicing.
7. Reshaping and resizing.
8. Stacking and splitting.
9. Broadcasting.
10. Mathematical and aggregation operations.
11. Universal functions.
12. Linear algebra.
13. Random-number generation.
14. Statistical functions.
15. Vectorized operations and performance.
16. Integration with other Python libraries.
17. Review questions and practical exercises.

## Prerequisites

Learners should have:

- Basic Python knowledge.
- Familiarity with variables, lists, loops, and functions.
- Access to Jupyter Notebook, JupyterLab, Google Colab, or another Python environment.

---

# What Is NumPy?

**NumPy**, short for **Numerical Python**, is a Python library designed for fast and efficient numerical computation.

Its main object is the **N-dimensional array**, called an `ndarray`. A NumPy array can represent:

- A one-dimensional vector.
- A two-dimensional matrix.
- A three-dimensional tensor.
- Higher-dimensional numerical structures.

NumPy provides:

- Fast array operations.
- Vectorized calculations.
- Broadcasting.
- Linear algebra functions.
- Statistical functions.
- Random-number generation.
- Integration with Pandas, SciPy, Matplotlib, and Scikit-learn.

## Main Features

### `ndarray`

The `ndarray` is NumPy's central data structure. It stores values of the same data type in an efficient multidimensional array.

### Vectorized Operations

Vectorized operations apply calculations to entire arrays without requiring explicit Python loops.

### Broadcasting

Broadcasting allows NumPy to perform operations on arrays with compatible but different shapes.

### Linear Algebra

NumPy supports matrix multiplication, determinants, inverses, eigenvalues, eigenvectors, and vector products.

### Statistical Functions

NumPy includes functions for calculating means, medians, variances, standard deviations, percentiles, and other descriptive measures.

### Integration

NumPy arrays are widely used by libraries such as:

- Pandas.
- SciPy.
- Matplotlib.
- Scikit-learn.
- Statsmodels.


### Quick Check

**Question 1.** What is the main data structure in NumPy?

A. `DataFrame`  
B. `ndarray`  
C. `dictionary`  
D. `tuple`  

**Question 2. True or false?** NumPy is designed mainly for numerical computing.

---

# Why Learn NumPy?

NumPy is important because it provides an efficient foundation for numerical work in Python.

## Main Advantages

- Executes vectorized operations much faster than ordinary Python loops in many numerical tasks.
- Stores homogeneous numerical data more compactly than standard Python lists.
- Provides optimized functions for matrix operations and linear algebra.
- Supports random-number generation and statistical analysis.
- Expresses complex mathematical operations using concise syntax.
- Serves as the numerical foundation for many data-science libraries.

## NumPy Arrays and Python Lists

A Python list can contain values of different types:

```python
values = [10, 2.5, "Python", True]
```

A NumPy array usually stores values of one common data type:

```python
import numpy as np

import numpy as np
```

Because NumPy arrays use a regular, homogeneous structure, numerical operations can be performed more efficiently.

### Example: Multiplying Values

Using a Python list:

```python
values = [1, 2, 3, 4]

values = [1, 2, 3, 4]

result = []
for value in values:

    result.append(value * 10)
```

Output:

```text
[10, 20, 30, 40]
```

Using NumPy:

```python
import numpy as np

import numpy as np

values = np.array([1, 2, 3, 4])

result = values * 10
```

Output:

```text
[10 20 30 40]
```

### Quick Check

**Question 1.** Why are NumPy arrays efficient for numerical calculations?

A. They always contain text  
B. They use a homogeneous and optimized array structure  
C. They do not use memory  
D. They automatically connect to the internet  

**Question 2.** Which expression multiplies every element of a NumPy array `a` by 10?

A. `a * 10`  
B. `a.append(10)`  
C. `a.add("10")`  
D. `a.sort(10)`  

---

# Installing and Importing NumPy

## Installation

Install NumPy with:

```bash
pip install numpy
```

In many scientific Python environments, NumPy may already be installed.

## Importing NumPy

The standard import convention is:

```python
import numpy as np
```

The alias `np` is widely used in Python code and documentation.

## Check the Installed Version

```python
import numpy as np

import numpy as np
```

### Quick Check

**Question 1.** What is the conventional alias for NumPy?

A. `ny`  
B. `np`  
C. `num`  
D. `py`  

**Question 2.** Which command installs NumPy?

A. `pip install numpy`  
B. `python import numpy`  
C. `install numpy.py`  
D. `pip numpy open`  

---

# NumPy Arrays

NumPy arrays can be created from Python lists, tuples, ranges, or built-in NumPy functions.

## Create an Array from a List

```python
import numpy as np

import numpy as np

a = [9, 3, 3, 5]

arr = np.array(a)
```

Output:

```text
[9 3 3 5]
```

## Create a One-Dimensional Array

```python
arr = np.array([10, 20, 30, 40])

arr = np.array([10, 20, 30, 40])
```

## Create a Two-Dimensional Array

```python
matrix = np.array([
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]

])
```

Output:

```text
[[1 2 3]
[[1 2 3]
```

## Create a Three-Dimensional Array

```python
tensor = np.array([
tensor = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]

])
```

### Quick Check

**Question 1.** Which function converts a Python list into a NumPy array?

A. `np.array()`  
B. `np.list()`  
C. `np.convert()`  
D. `np.ndarray_list()`  

**Question 2.** A two-dimensional NumPy array is commonly used to represent:

A. A matrix  
B. A string  
C. A file path  
D. A Boolean condition  

---

# Common Array-Creation Functions

## Create an Array of Zeros

```python
zeros = np.zeros(5)

zeros = np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

Create a matrix of zeros:

```python
zeros_matrix = np.zeros((2, 3))

zeros_matrix = np.zeros((2, 3))
```

## Create an Array of Ones

```python
ones = np.ones((2, 3))

ones = np.ones((2, 3))
```

## Create an Array with a Constant Value

```python
filled = np.full((2, 3), 7)

filled = np.full((2, 3), 7)
```

## Create a Sequence with `arange()`

```python
values = np.arange(0, 10, 2)

values = np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

## Create Evenly Spaced Values with `linspace()`

```python
values = np.linspace(0, 1, 5)

values = np.linspace(0, 1, 5)
```

Output:

```text
[0.   0.25 0.5  0.75 1.  ]
```

## Create an Identity Matrix

```python
identity = np.eye(3)

identity = np.eye(3)
```

Output:

```text
[[1. 0. 0.]
[[1. 0. 0.]
 [0. 1. 0.]
```

### Quick Check

**Question 1.** Which function creates an array filled with zeros?

A. `np.zeros()`  
B. `np.empty_text()`  
C. `np.null()`  
D. `np.zero_array_only()`  

**Question 2.** Which function creates evenly spaced values between two endpoints?

A. `np.linspace()`  
B. `np.stack()`  
C. `np.split()`  
D. `np.mean()`  

---

# Array Properties

NumPy arrays provide several useful attributes.

```python
arr = np.array([
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
```

## Number of Dimensions

```python
print(arr.ndim)
```

Output:

```text
2
```

## Shape

```python
print(arr.shape)
```

Output:

```text
(2, 3)
```

The array has two rows and three columns.

## Total Number of Elements

```python
print(arr.size)
```

Output:

```text
6
```

## Data Type

```python
print(arr.dtype)
```

The exact output depends on the platform and the values stored in the array.

## Number of Bytes per Element

```python
print(arr.itemsize)
```

### Summary

| Attribute | Meaning |
|---|---|
| `ndim` | Number of dimensions |
| `shape` | Size along each dimension |
| `size` | Total number of elements |
| `dtype` | Data type |
| `itemsize` | Number of bytes used by each element |

### Quick Check

**Question 1.** Which attribute returns the dimensions of an array?

A. `shape`  
B. `mean`  
C. `append`  
D. `index`  

**Question 2.** Which attribute returns the total number of elements?

A. `size`  
B. `dtype`  
C. `ndim`  
D. `itemsize`  

---

# Array Indexing

Indexing is used to access individual elements.

## One-Dimensional Indexing

```python
arr = np.array([10, 20, 30, 40])

arr = np.array([10, 20, 30, 40])
print(arr[0])
```

Output:

```text
10
10
```

Negative indexing accesses elements from the end:

```python
print(arr[-1])
```

Output:

```text
40
```

## Two-Dimensional Indexing

```python
matrix = np.array([
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]

])
print(matrix[0, 1])
```

Output:

```text
2
2
```

### Quick Check

**Question 1.** What does `arr[0]` return?

A. The first element  
B. The last element  
C. The array shape  
D. The array size  

**Question 2.** In a two-dimensional array, `matrix[1, 2]` refers to:

A. Row index 1 and column index 2  
B. Row 1 only  
C. Column 2 only  
D. The array dimensions  

---

# Array Slicing

Slicing extracts part of an array.

## One-Dimensional Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

arr = np.array([10, 20, 30, 40, 50])
```

Output:

```text
[20 30 40]
```

## Slicing with a Step

```python
print(arr[::2])
```

Output:

```text
[10 30 50]
```

## Two-Dimensional Slicing

```python
matrix = np.array([
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

])
```

Output:

```text
[[2 3]
[[2 3]
```

## Important Note: Views and Copies

Many NumPy slices return a **view** of the original array rather than an independent copy. Modifying the slice may therefore modify the original data.

```python
arr = np.array([10, 20, 30, 40])

arr = np.array([10, 20, 30, 40])
view = arr[1:3]

view[0] = 999
```

Output:

```text
[ 10 999  30  40]
```

Create an independent copy with:

```python
copy = arr[1:3].copy()
```

### Quick Check

**Question 1.** What does `arr[1:4]` include?

A. Elements at indices 1, 2, and 3  
B. Elements at indices 1 through 4, including 4  
C. Only the element at index 4  
D. Every second element  

**Question 2. True or false?** A NumPy slice may share memory with the original array.

---

# Reshaping Arrays

Reshaping changes the dimensions of an array without changing its data.

```python
arr = np.arange(12)

arr = np.arange(12)

matrix = arr.reshape(3, 4)
```

Output:

```text
[[ 0  1  2  3]
[[ 0  1  2  3]
 [ 4  5  6  7]
```

## Use `-1` to Infer a Dimension

```python
matrix = arr.reshape(2, -1)

matrix = arr.reshape(2, -1)
```

NumPy automatically calculates the missing dimension.

## Flatten an Array

```python
flat = matrix.flatten()

flat = matrix.flatten()
```

## Use `ravel()`

```python
flat_view = matrix.ravel()

flat_view = matrix.ravel()
```

`flatten()` returns a copy, while `ravel()` often returns a view when possible.

### Quick Check

**Question 1.** Which method changes an array from one shape to another?

A. `reshape()`  
B. `mean()`  
C. `split()`  
D. `sort_index()`  

**Question 2.** What does `-1` mean in `reshape()`?

A. NumPy should infer that dimension  
B. Delete one dimension  
C. Reverse the array  
D. Convert values to negative numbers  

---

# Resizing Arrays

`resize()` changes the shape of an array and may change the number of elements.

```python
arr = np.array([1, 2, 3, 4])

arr = np.array([1, 2, 3, 4])

resized = np.resize(arr, (2, 3))
```

Output:

```text
[[1 2 3]
[[1 2 3]
```

When the new array is larger, values may be repeated.

> **Note:** `reshape()` requires the total number of elements to remain compatible. `resize()` can create a different total size.

### Quick Check

**Question 1.** Which operation normally preserves the total number of elements?

A. `reshape()`  
B. `np.resize()` in every case  
C. `np.delete()`  
D. `np.append()`  

---

# Stacking Arrays

Stacking combines arrays.

## Vertical Stacking

```python
a = np.array([1, 2, 3])
a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

result = np.vstack((a, b))
```

Output:

```text
[[1 2 3]
[[1 2 3]
```

## Horizontal Stacking

```python
result = np.hstack((a, b))

result = np.hstack((a, b))
```

Output:

```text
[1 2 3 4 5 6]
```

## General Stacking

```python
result = np.stack((a, b), axis=0)

result = np.stack((a, b), axis=0)
```

### Quick Check

**Question 1.** Which function stacks arrays vertically?

A. `np.vstack()`  
B. `np.mean()`  
C. `np.split()`  
D. `np.random()`  

---

# Splitting Arrays

Splitting divides an array into smaller arrays.

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr = np.array([1, 2, 3, 4, 5, 6])

parts = np.split(arr, 3)
```

Output:

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

## Horizontal and Vertical Splitting

```python
matrix = np.array([
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]

])

left, right = np.hsplit(matrix, 2)
print(left)
```

### Quick Check

**Question 1.** Which function divides an array into equal parts?

A. `np.split()`  
B. `np.join()`  
C. `np.mean()`  
D. `np.dot()`  

---

# Broadcasting

Broadcasting allows NumPy to perform operations between arrays of compatible shapes.

## Scalar Broadcasting

```python
arr = np.array([1, 2, 3, 4])

arr = np.array([1, 2, 3, 4])

result = arr + 10
```

Output:

```text
[11 12 13 14]
```

The scalar `10` is conceptually applied to every element.

## Broadcasting Between Arrays

```python
matrix = np.array([
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]

])

row = np.array([10, 20, 30])

result = matrix + row
```

Output:

```text
[[11 22 33]
[[11 22 33]
```

## Basic Broadcasting Rule

Starting from the rightmost dimensions, two dimensions are compatible when:

- They are equal; or
- One of them is `1`.

If the shapes are incompatible, NumPy raises an error.

### Example of Incompatible Shapes

```python
a = np.ones((2, 3))
a = np.ones((2, 3))

# a + b raises a broadcasting error
```

### Quick Check

**Question 1.** What does broadcasting allow?

A. Operations on arrays with compatible different shapes  
B. Automatic internet transmission  
C. Conversion of arrays into files  
D. Removal of all dimensions  

**Question 2.** Two dimensions are broadcasting-compatible when they are equal or:

A. One of them is 1  
B. Both are negative  
C. Both are text  
D. Their sum is zero  

---

# Basic Arithmetic Operations

NumPy supports element-wise arithmetic.

```python
a = np.array([1, 2, 3])
a = np.array([1, 2, 3])
```

## Addition

```python
print(a + b)
```

Output:

```text
[5 7 9]
```

## Subtraction

```python
print(a - b)
```

Output:

```text
[-3 -3 -3]
```

## Multiplication

```python
print(a * b)
```

Output:

```text
[ 4 10 18]
```

## Division

```python
print(a / b)
```

## Exponentiation

```python
print(a ** 2)
```

Output:

```text
[1 4 9]
```

## Modulo

```python
print(b % a)
```

### Important Distinction

The `*` operator performs **element-wise multiplication**, not matrix multiplication.

### Quick Check

**Question 1.** What does `a * b` do for two arrays of the same shape?

A. Element-wise multiplication  
B. Matrix inversion  
C. Sorting  
D. Stacking  

---

# Aggregation Functions

Aggregation functions summarize an array.

```python
arr = np.array([9, 3, 3, 5])
```

## Sum

```python
print(arr.sum())
```

Output:

```text
20
```

## Mean

```python
print(arr.mean())
```

Output:

```text
5.0
```

## Minimum and Maximum

```python
print(arr.min())
print(arr.min())
```

## Median

```python
print(np.median(arr))
```

## Variance and Standard Deviation

```python
print(np.var(arr))
print(np.var(arr))
```

## Aggregation Along an Axis

```python
matrix = np.array([
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]

])
print(matrix.sum(axis=0))
```

Output:

```text
[5 7 9]
[5 7 9]
```

- `axis=0` aggregates down the rows, producing one value per column.
- `axis=1` aggregates across the columns, producing one value per row.

### Quick Check

**Question 1.** Which function calculates the arithmetic mean?

A. `np.mean()`  
B. `np.stack()`  
C. `np.dot()`  
D. `np.reshape()`  

**Question 2.** In a two-dimensional array, what does `axis=0` generally aggregate over?

A. Rows, producing column-wise results  
B. Columns, producing row-wise results  
C. File names  
D. Data types  

---

# Universal Functions

A **universal function**, or **ufunc**, performs element-wise operations on arrays.

## Square Root

```python
arr = np.array([1, 4, 9, 16])

arr = np.array([1, 4, 9, 16])
```

Output:

```text
[1. 2. 3. 4.]
```

## Exponential

```python
print(np.exp(np.array([0, 1, 2])))
```

## Natural Logarithm

```python
values = np.array([1, np.e, np.e**2])

values = np.array([1, np.e, np.e**2])
```

## Trigonometric Functions

```python
angles = np.array([0, np.pi / 2, np.pi])

angles = np.array([0, np.pi / 2, np.pi])
```

## Absolute Value

```python
values = np.array([-3, -1, 2, 4])

values = np.array([-3, -1, 2, 4])
```

## Rounding

```python
values = np.array([1.234, 5.678])

values = np.array([1.234, 5.678])
```

### Quick Check

**Question 1.** Which function calculates square roots element by element?

A. `np.sqrt()`  
B. `np.split()`  
C. `np.stack()`  
D. `np.size()`  

---

# Comparison and Boolean Operations

NumPy supports element-wise comparisons.

```python
arr = np.array([10, 20, 30, 40])

arr = np.array([10, 20, 30, 40])
```

Output:

```text
[False False  True  True]
```

## Boolean Filtering

```python
selected = arr[arr > 20]

selected = arr[arr > 20]
```

Output:

```text
[30 40]
```

## Combine Conditions

```python
selected = arr[(arr >= 20) & (arr <= 30)]

selected = arr[(arr >= 20) & (arr <= 30)]
```

Output:

```text
[20 30]
```

Use:

- `&` for element-wise AND.
- `|` for element-wise OR.
- `~` for element-wise NOT.

### Quick Check

**Question 1.** What does `arr[arr > 20]` return?

A. Elements greater than 20  
B. The array size  
C. The array data type  
D. All elements converted to Boolean values  

---

# Linear Algebra

NumPy provides linear-algebra functions through `numpy.linalg` and matrix multiplication operators.

## Matrix Multiplication

```python
import numpy as np

import numpy as np
A = np.array([
    [1, 2],
    [3, 4]

])

result = np.dot(A, A)
```

Output:

```text
[[ 7 10]
[[ 7 10]
```

The `@` operator can also be used:

```python
result = A @ A

result = A @ A
```

## Element-Wise vs. Matrix Multiplication

```python
print(A * A)
print(A * A)
```

- `A * A` performs element-wise multiplication.
- `A @ A` performs matrix multiplication.

## Matrix Transpose

```python
print(A.T)
```

## Determinant

```python
determinant = np.linalg.det(A)

determinant = np.linalg.det(A)
```

## Matrix Inverse

```python
inverse = np.linalg.inv(A)

inverse = np.linalg.inv(A)
```

An inverse exists only for a square, nonsingular matrix.

## Solve a Linear System

For the system \(Ax=b\):

```python
A = np.array([
A = np.array([
    [2, 1],
    [1, 3]

])

b = np.array([8, 13])

x = np.linalg.solve(A, b)
```

## Eigenvalues and Eigenvectors

```python
eigenvalues, eigenvectors = np.linalg.eig(A)

eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
```

## Inner Product

```python
a = np.array([1, 2, 3])
a = np.array([1, 2, 3])

b = np.array([4, 5, 6])
```

## Outer Product

```python
print(np.outer(a, b))
```

## Dot and Vector Dot Products

```python
print(np.dot(a, b))
print(np.dot(a, b))
```

For real one-dimensional arrays, these results are often the same. `vdot()` also handles complex conjugation.

### Quick Check

**Question 1.** Which operator performs matrix multiplication?

A. `@`  
B. `%`  
C. `//`  
D. `&`  

**Question 2.** Which function calculates a matrix inverse?

A. `np.linalg.inv()`  
B. `np.mean()`  
C. `np.resize()`  
D. `np.random()`  

---

# Random-Number Generation

NumPy provides tools for generating random values used in simulation, statistical experiments, and machine-learning workflows.

For new code, NumPy commonly uses a random-number generator object:

```python
import numpy as np

import numpy as np
```

> **Note:** NumPy's random-number generators are intended for numerical and statistical work. They should not be treated as cryptographically secure generators.

## Random Integers

```python
rng = np.random.default_rng(42)

rng = np.random.default_rng(42)
values = rng.integers(
    low=1,
    high=10,
    size=5

)
```

## Uniform Distribution

```python
values = rng.uniform(
values = rng.uniform(
    low=0,
    high=1,
    size=5

)
```

## Normal Distribution

```python
values = rng.normal(
values = rng.normal(
    loc=0,
    scale=1,
    size=5

)
```

## Binomial Distribution

```python
values = rng.binomial(
values = rng.binomial(
    n=10,
    p=0.5,
    size=5

)
```

## Poisson Distribution

```python
values = rng.poisson(
values = rng.poisson(
    lam=3,
    size=5

)
```

## Exponential Distribution

```python
values = rng.exponential(
values = rng.exponential(
    scale=2,
    size=5

)
```

## Chi-Square Distribution

```python
values = rng.chisquare(
values = rng.chisquare(
    df=4,
    size=5

)
```

## Reproducibility with a Seed

```python
rng = np.random.default_rng(42)
```

Using the same seed helps reproduce the same pseudorandom sequence.

### Example

```python
import numpy as np

import numpy as np

rng = np.random.default_rng(42)

a = rng.normal(0, 1, 5)
print("Data:", a)
```

The exact values depend on the generator and NumPy version, but a fixed seed makes a run reproducible within a compatible environment.

### Quick Check

**Question 1.** Which method creates a modern NumPy random-number generator?

A. `np.random.default_rng()`  
B. `np.random.file()`  
C. `np.create_random_array()`  
D. `np.random.text()`  

**Question 2.** Why is a seed useful?

A. It helps reproduce a pseudorandom sequence  
B. It makes values truly unpredictable  
C. It removes every random value  
D. It converts data into strings  

---

# Statistical Functions

NumPy supports common descriptive statistics.

```python
data = np.array([12, 15, 18, 20, 25])
```

## Mean

```python
print(np.mean(data))
```

## Median

```python
print(np.median(data))
```

## Variance

```python
print(np.var(data))
```

## Standard Deviation

```python
print(np.std(data))
```

## Percentiles

```python
print(np.percentile(data, 25))
print(np.percentile(data, 25))
print(np.percentile(data, 50))
```

## Quantiles

```python
print(np.quantile(data, 0.25))
print(np.quantile(data, 0.25))
print(np.quantile(data, 0.50))
```

## Range

```python
data_range = np.max(data) - np.min(data)

data_range = np.max(data) - np.min(data)
```

### Population and Sample Conventions

By default, `np.var()` and `np.std()` use `ddof=0`, corresponding to division by \(N\).

For a sample estimate using division by \(N-1\):

```python
sample_variance = np.var(data, ddof=1)
sample_variance = np.var(data, ddof=1)

sample_std = np.std(data, ddof=1)
print(sample_variance)
```

### Quick Check

**Question 1.** Which parameter can be used to obtain the usual sample standard deviation?

A. `ddof=1`  
B. `axis=-100`  
C. `dtype="sample"`  
D. `copy=False`  

---

# Missing and Invalid Numerical Values

NumPy commonly represents missing numerical values with `np.nan`.

```python
data = np.array([10.0, 20.0, np.nan, 40.0])

data = np.array([10.0, 20.0, np.nan, 40.0])
```

## Standard Mean

```python
print(np.mean(data))
```

This returns `nan` because the array contains a missing value.

## Ignore `NaN` Values

```python
print(np.nanmean(data))
print(np.nanmean(data))
print(np.nanmedian(data))
```

## Detect Missing Values

```python
print(np.isnan(data))
```

## Remove Missing Values

```python
clean_data = data[~np.isnan(data)]

clean_data = data[~np.isnan(data)]
```

> **Note:** NumPy provides basic support for missing numerical values. More complete missing-data workflows are commonly handled with Pandas.

### Quick Check

**Question 1.** Which function calculates the mean while ignoring `NaN` values?

A. `np.nanmean()`  
B. `np.mean_text()`  
C. `np.ignore()`  
D. `np.dropna()`  

---

# Vectorized Operations

Vectorization applies an operation to an entire array at once.

```python
import numpy as np

import numpy as np

a = np.arange(5)

result = a * 10
```

Output:

```text
[ 0 10 20 30 40]
```

Without NumPy, a loop might be required:

```python
a = list(range(5))

a = list(range(5))

result = []
for value in a:

    result.append(value * 10)
```

Vectorized code is often:

- Shorter.
- Easier to read.
- Faster for large numerical arrays.
- Better suited to scientific and data-analysis workflows.

## Vectorized Conditional Logic

```python
arr = np.array([10, 20, 30, 40])

arr = np.array([10, 20, 30, 40])
labels = np.where(
    arr >= 30,
    "high",
    "low"

)
```

Output:

```text
['low' 'low' 'high' 'high']
```

### Quick Check

**Question 1.** What is a major advantage of vectorization?

A. It applies array operations without explicit Python loops  
B. It converts every array into text  
C. It eliminates the need for memory  
D. It prevents all errors  

---

# Memory Considerations

NumPy arrays are efficient because they usually store homogeneous values in a regular memory layout.

## Check Memory Usage

```python
arr = np.array([1, 2, 3, 4], dtype=np.int32)

arr = np.array([1, 2, 3, 4], dtype=np.int32)
```

`nbytes` returns the total number of bytes used by the array elements.

## Select a Suitable Data Type

```python
small_values = np.array(
small_values = np.array(
    [1, 2, 3, 4],
    dtype=np.int8

)
print(small_values.dtype)
```

Choosing a smaller data type may reduce memory usage, but the selected type must be able to represent the required value range and precision.

## Convert Data Types

```python
arr = np.array([1.2, 2.8, 3.5])

arr = np.array([1.2, 2.8, 3.5])

integers = arr.astype(np.int32)
```

Output:

```text
[1 2 3]
```

Conversion from floating-point values to integers removes the fractional part.

### Quick Check

**Question 1.** Which attribute returns the number of bytes used by array elements?

A. `nbytes`  
B. `ndim`  
C. `mean`  
D. `shape`  

---

# Sorting and Searching

## Sort an Array

```python
arr = np.array([9, 3, 7, 1])

arr = np.array([9, 3, 7, 1])

sorted_arr = np.sort(arr)
```

Output:

```text
[1 3 7 9]
```

## Find Indices Matching a Condition

```python
arr = np.array([10, 20, 30, 40])

arr = np.array([10, 20, 30, 40])

indices = np.where(arr > 20)
```

## Find Unique Values

```python
arr = np.array([1, 2, 2, 3, 3, 3])

arr = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique(
    arr,
    return_counts=True

)
print(values)
```

### Quick Check

**Question 1.** Which function returns unique array values?

A. `np.unique()`  
B. `np.reshape()`  
C. `np.random()`  
D. `np.outer()`  

---

# Sparse Matrices

A sparse matrix contains many zero values.

NumPy can represent a sparse matrix as an ordinary dense array:

```python
matrix = np.array([
matrix = np.array([
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 0]
```

However, large sparse matrices are usually handled more efficiently using specialized sparse structures from SciPy.

```python
from scipy.sparse import csr_matrix

from scipy.sparse import csr_matrix

sparse_matrix = csr_matrix(matrix)
```

NumPy remains important because SciPy sparse matrices interact closely with NumPy arrays.

### Quick Check

**Question 1.** Which library commonly provides specialized sparse-matrix structures?

A. SciPy  
B. pathlib  
C. tkinter  
D. Flask  

---

# Working with Images

Digital images can be represented as NumPy arrays.

- A grayscale image may be represented by a two-dimensional array.
- A color image may be represented by a three-dimensional array containing height, width, and color channels.

## Simple Example

```python
image = np.array([
image = np.array([
    [0, 128, 255],
    [255, 128, 0],
    [50, 100, 150]

])
```

Output:

```text
(3, 3)
```

## Adjust Brightness

```python
brighter = np.clip(
brighter = np.clip(
    image + 30,
    0,
    255

)
```

`np.clip()` keeps values within the valid range.

### Quick Check

**Question 1.** A grayscale image is commonly represented as:

A. A two-dimensional numerical array  
B. A dictionary only  
C. A text file only  
D. A Boolean value  

---

# Integration with Pandas

A Pandas `Series` or `DataFrame` is built on array-oriented concepts and can exchange data with NumPy.

## Convert a NumPy Array to a DataFrame

```python
import numpy as np
import numpy as np

import pandas as pd
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]

])
df = pd.DataFrame(
    arr,
    columns=["A", "B"]

)
```

## Convert a DataFrame to a NumPy Array

```python
array_from_df = df.to_numpy()

array_from_df = df.to_numpy()
```

## Apply a NumPy Function to a Pandas Column

```python
df["A_sqrt"] = np.sqrt(df["A"])

df["A_sqrt"] = np.sqrt(df["A"])
```

### Quick Check

**Question 1.** Which Pandas method converts a DataFrame to a NumPy array?

A. `to_numpy()`  
B. `to_list_only()`  
C. `as_matrix_text()`  
D. `convert_numpy_file()`  

---

# Integration with Scikit-learn

Many Scikit-learn models accept NumPy arrays as input.

```python
import numpy as np
import numpy as np

from sklearn.linear_model import LinearRegression
X = np.array([
    [1],
    [2],
    [3],
    [4]

])

y = np.array([2, 4, 6, 8])
model = LinearRegression()

model.fit(X, y)
prediction = model.predict(
    np.array([[5]])

)
```

NumPy supports:

- Feature matrices.
- Target vectors.
- Model predictions.
- Numerical preprocessing.
- Evaluation calculations.

### Quick Check

**Question 1.** In machine learning, a two-dimensional NumPy array commonly represents:

A. A feature matrix  
B. A filename  
C. A chart title  
D. A package installer  

---

# Common NumPy Errors

## Shape Mismatch

```python
a = np.ones((2, 3))
a = np.ones((2, 3))

# a + b raises an error
```

The shapes are not broadcasting-compatible.

## Invalid Reshape

```python
arr = np.arange(10)

# arr.reshape(3, 4) raises an error
```

Ten elements cannot be reshaped into a `3 × 4` array.

## Division by Zero

```python
arr = np.array([1.0, 0.0])

arr = np.array([1.0, 0.0])
```

This may produce `inf` and a runtime warning.

## Integer Overflow

Small integer data types have limited ranges:

```python
arr = np.array([127], dtype=np.int8)

arr = np.array([127], dtype=np.int8)
```

The result may overflow because `int8` cannot represent values above 127.

## Unexpected Changes Through Views

A slice may share data with the original array. Use `.copy()` when an independent array is required.

### Quick Check

**Question 1.** Why does `np.arange(10).reshape(3, 4)` fail?

A. The total number of elements is incompatible  
B. NumPy cannot create matrices  
C. `reshape()` works only with strings  
D. The values must be negative  

---

# Good Practices

- Import NumPy using `import numpy as np`.
- Use vectorized operations instead of Python loops when practical.
- Check `shape`, `ndim`, and `dtype` before complex operations.
- Use broadcasting only when the intended shape behavior is clear.
- Distinguish element-wise multiplication from matrix multiplication.
- Use `.copy()` when an independent array is required.
- Choose data types carefully to balance range, precision, and memory.
- Use a fixed random seed when reproducibility is important.
- Treat `NaN`, infinity, and overflow explicitly.
- Use Pandas for richer labeled-table and missing-data workflows.
- Use SciPy for specialized scientific routines and sparse matrices.

---

# Content Summary

| Topic | Main idea |
|---|---|
| **NumPy** | Core Python library for numerical computing |
| **`ndarray`** | N-dimensional homogeneous array |
| **Vectorization** | Array operations without explicit Python loops |
| **Broadcasting** | Operations on compatible different shapes |
| **Indexing and slicing** | Access and extract array elements |
| **Reshaping** | Change array dimensions |
| **Aggregation** | Calculate sums, means, minima, and maxima |
| **Universal functions** | Fast element-wise mathematical functions |
| **Linear algebra** | Matrix multiplication, inverse, determinant, and eigenvalues |
| **Random generation** | Generate values from probability distributions |
| **Statistics** | Mean, median, variance, standard deviation, and percentiles |
| **Integration** | Works closely with Pandas, SciPy, and Scikit-learn |

---

# End-of-Lesson Review

## Part A. Multiple-Choice Questions

**Question 1.** What is NumPy primarily used for?

A. Numerical computing  
B. Web-page design  
C. Sending emails  
D. Word processing  

**Question 2.** What is the central NumPy data structure?

A. `ndarray`  
B. `DataFrame`  
C. `set`  
D. `class`  

**Question 3.** Which function creates an array from a Python list?

A. `np.array()`  
B. `np.list()`  
C. `np.frame()`  
D. `np.convert_list()`  

**Question 4.** Which attribute returns an array's shape?

A. `shape`  
B. `size()`  
C. `mean`  
D. `type()`  

**Question 5.** Which expression performs matrix multiplication?

A. `A @ B`  
B. `A % B`  
C. `A // B`  
D. `A | B`  

**Question 6.** Which function calculates a mean while ignoring `NaN` values?

A. `np.nanmean()`  
B. `np.mean_without_missing()`  
C. `np.dropna()`  
D. `np.ignore_mean()`  

**Question 7.** Which function is used for an identity matrix?

A. `np.eye()`  
B. `np.identity_text()`  
C. `np.ones_like_text()`  
D. `np.reshape()`  

**Question 8.** Which statement about broadcasting is correct?

A. It supports operations between compatible shapes  
B. It converts every array to one dimension  
C. It removes all duplicate values  
D. It always changes the original array  

**Question 9.** What does `axis=0` usually mean in a two-dimensional aggregation?

A. Aggregate down rows and return column-wise values  
B. Aggregate across columns and return row-wise values  
C. Convert the matrix into a scalar only  
D. Reverse all values  

**Question 10.** Which object is recommended for modern NumPy random-number generation?

A. `np.random.default_rng()`  
B. `np.random.file_reader()`  
C. `np.random.secure_password()`  
D. `np.array.randomize_text()`  

## Part B. True/False Questions

**Question 1.** NumPy arrays usually contain elements of one common data type.

**Question 2.** Vectorized NumPy operations always require an explicit Python loop.

**Question 3.** `A * B` and `A @ B` always perform the same operation.

**Question 4.** NumPy slices may share memory with the original array.

**Question 5.** Broadcasting requires array dimensions to be compatible.

**Question 6.** `np.std(data, ddof=1)` can be used for the usual sample-standard-deviation convention.

**Question 7.** NumPy random-number generation should be assumed to be cryptographically secure.

**Question 8.** NumPy arrays can be used as inputs to Scikit-learn models.

## Part C. Short-Answer Questions

**Question 1.** Explain two differences between a Python list and a NumPy array.

**Question 2.** Explain vectorization and state one advantage.

**Question 3.** Explain the difference between element-wise and matrix multiplication.

**Question 4.** State the basic broadcasting compatibility rule.

**Question 5.** Explain the difference between a view and a copy.

**Question 6.** Name four statistical functions available in NumPy.

## Part D. Practical Exercises

### Exercise 1. Array Creation

1. Create an array containing the values from 1 to 20.
2. Reshape it into a `4 × 5` matrix.
3. Print its shape, number of dimensions, size, and data type.

### Exercise 2. Indexing and Slicing

Using a `4 × 5` matrix:

1. Extract the first row.
2. Extract the last column.
3. Extract the central `2 × 3` section.
4. Select all even values using Boolean filtering.

### Exercise 3. Statistics

Create an array of ten numerical values and calculate:

1. Mean.
2. Median.
3. Variance.
4. Sample standard deviation.
5. Minimum and maximum.
6. The 25th, 50th, and 75th percentiles.

### Exercise 4. Broadcasting

1. Create a `3 × 4` matrix.
2. Create a one-dimensional array with four values.
3. Add the one-dimensional array to each row of the matrix.
4. Explain why broadcasting is valid.

### Exercise 5. Linear Algebra

Given:

```python
A = np.array([
A = np.array([
    [2, 1],
    [1, 3]

])
```

1. Calculate the determinant of `A`.
2. Calculate the inverse of `A`.
3. Solve \(Ax=b\).
4. Verify the solution by calculating `A @ x`.

### Exercise 6. Random Data

1. Create a random-number generator with seed `42`.
2. Generate 1,000 values from a standard normal distribution.
3. Calculate the mean and standard deviation.
4. Compare the sample results with the theoretical values.

### Exercise 7. Missing Values

Given:

```python
data = np.array([
data = np.array([
    10.0,
    np.nan,
    20.0,
    30.0,
    np.nan,
    40.0
```

1. Count the missing values.
2. Calculate the mean while ignoring missing values.
3. Remove all missing values.
4. Replace missing values with the median of the observed values.

---

# Answers and Suggested Responses

<details>
<summary><strong>Click to show answers</strong></summary>

## Quick Check Answers

### What Is NumPy?

1. B. `ndarray`.  
2. True.

### Why Learn NumPy?

1. B. They use a homogeneous and optimized array structure.  
2. A. `a * 10`.

### Installation and Importing

1. B. `np`.  
2. A. `pip install numpy`.

### NumPy Arrays

1. A. `np.array()`.  
2. A. A matrix.

### Array-Creation Functions

1. A. `np.zeros()`.  
2. A. `np.linspace()`.

### Array Properties

1. A. `shape`.  
2. A. `size`.

### Indexing

1. A. The first element.  
2. A. Row index 1 and column index 2.

### Slicing

1. A. Elements at indices 1, 2, and 3.  
2. True.

### Reshaping

1. A. `reshape()`.  
2. A. NumPy should infer that dimension.

### Resizing

1. A. `reshape()`.

### Stacking

1. A. `np.vstack()`.

### Splitting

1. A. `np.split()`.

### Broadcasting

1. A. Operations on arrays with compatible different shapes.  
2. A. One of them is 1.

### Arithmetic

1. A. Element-wise multiplication.

### Aggregation

1. A. `np.mean()`.  
2. A. Rows, producing column-wise results.

### Universal Functions

1. A. `np.sqrt()`.

### Boolean Operations

1. A. Elements greater than 20.

### Linear Algebra

1. A. `@`.  
2. A. `np.linalg.inv()`.

### Random Numbers

1. A. `np.random.default_rng()`.  
2. A. It helps reproduce a pseudorandom sequence.

### Statistical Functions

1. A. `ddof=1`.

### Missing Values

1. A. `np.nanmean()`.

### Vectorization

1. A. It applies array operations without explicit Python loops.

### Memory

1. A. `nbytes`.

### Sorting and Searching

1. A. `np.unique()`.

### Sparse Matrices

1. A. SciPy.

### Images

1. A. A two-dimensional numerical array.

### Pandas Integration

1. A. `to_numpy()`.

### Scikit-learn Integration

1. A. A feature matrix.

### Common Errors

1. A. The total number of elements is incompatible.

## Part A. Multiple-Choice Answers

1. A  
2. A  
3. A  
4. A  
5. A  
6. A  
7. A  
8. A  
9. A  
10. A  

## Part B. True/False Answers

1. True.  
2. False.  
3. False.  
4. True.  
5. True.  
6. True.  
7. False.  
8. True.  

## Part C. Suggested Responses

### Question 1

A NumPy array usually stores homogeneous values in a regular multidimensional structure, while a Python list can store mixed object types. NumPy arrays also support vectorized numerical operations.

### Question 2

Vectorization applies an operation to an entire array without writing an explicit Python loop. It often improves readability and execution speed for large numerical tasks.

### Question 3

Element-wise multiplication multiplies corresponding elements, as in `A * B`. Matrix multiplication combines rows and columns according to linear-algebra rules, as in `A @ B`.

### Question 4

Starting from the rightmost dimension, dimensions are compatible when they are equal or when one of them is 1.

### Question 5

A view may share memory with the original array, so modifying it may change the original data. A copy has independent memory.

### Question 6

Examples include `np.mean()`, `np.median()`, `np.var()`, `np.std()`, `np.percentile()`, and `np.quantile()`.

## Part D

The practical exercises are open coding tasks. A complete submission should include source code, output, and a short explanation of the result.

</details>
