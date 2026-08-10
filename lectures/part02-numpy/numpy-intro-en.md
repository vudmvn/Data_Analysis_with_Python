# Introduction to NumPy
**Language:** English  
**Topic:** Arrays, vectorization, broadcasting, and numerical computing

---

## 1. Lesson Introduction
This lesson introduces **NumPy**, a core Python library for **numerical computing**. NumPy is designed for efficient work with arrays, matrices, and numerical datasets. Its central object is the **N-dimensional array**, or `ndarray`.

In data analysis and Data Science, NumPy is commonly used to:

- store numerical data as arrays;
- perform operations on whole arrays instead of writing explicit loops;
- work with matrices, vectors, and linear-algebra operations;
- generate random values for simulation and experiments;
- calculate descriptive statistics;
- exchange data with Pandas, SciPy, Matplotlib, and Scikit-learn.

Compared with ordinary Python lists, NumPy arrays usually store **homogeneous data**, use a more regular memory layout, and support optimized vectorized operations.

---

## 2. Learning Outcomes
After completing this lesson, learners will be able to:

- Explain the role of NumPy in numerical computing.
- Distinguish NumPy arrays from Python lists.
- Install and import NumPy.
- Create one-dimensional, two-dimensional, and multidimensional arrays.
- Inspect properties such as `shape`, `ndim`, `size`, `dtype`, `itemsize`, and `nbytes`.
- Access elements using indexing and slicing.
- Reshape, resize, stack, and split arrays.
- Apply vectorized operations and broadcasting.
- Use aggregation functions such as `sum()`, `mean()`, `min()`, and `max()`.
- Use universal functions such as `np.sqrt()`, `np.exp()`, `np.log()`, and `np.sin()`.
- Perform basic linear-algebra operations.
- Generate random values and calculate descriptive statistics.
- Explain how NumPy integrates with Pandas and Scikit-learn.

---

## 3. Lesson Structure
The lesson is organized into the following feature groups:

1. What NumPy is.
2. Why NumPy is useful.
3. Installation and importing.
4. Creating arrays.
5. Array properties.
6. Indexing and slicing.
7. Reshape, resize, stack, and split.
8. Broadcasting and arithmetic.
9. Aggregation and universal functions.
10. Boolean operations.
11. Linear algebra.
12. Random numbers and statistics.
13. Vectorization and performance.
14. Memory, data types, sorting, searching, and images.
15. Integration with Pandas and Scikit-learn.
16. Common errors.
17. Good practices.
18. Content summary.
19. Review questions.
20. Practical exercises.

---

## 4. Prerequisites
Learners should have:

- Basic Python knowledge.
- Familiarity with variables, lists, loops, and functions.
- Access to Jupyter Notebook, JupyterLab, Google Colab, VS Code, or a similar Python environment.

---

# Part 1. What Is NumPy?
## 1.1. Concept
**NumPy**, short for **Numerical Python**, is a Python library for fast and efficient numerical computing.

Its main object is the `ndarray`, an N-dimensional array. A NumPy array can represent:

- a one-dimensional vector;
- a two-dimensional matrix;
- a three-dimensional tensor;
- higher-dimensional numerical structures.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)
```

### Mini Exercise — `np.array()`

Create a NumPy array containing `[5, 10, 15, 20]`.

```python
# arr = np.array([...])
# print(arr)
```

**Hint:** pass a Python list to `np.array()`.

Output:

```text
[10 20 30 40]
```

Here, `np.array()` converts a Python list into a NumPy array.

## 1.2. What Does NumPy Provide?
NumPy provides:

- fast array operations;
- vectorized calculations;
- broadcasting;
- linear-algebra functions;
- statistical functions;
- random-number generation;
- integration with Pandas, SciPy, Matplotlib, and Scikit-learn.

## 1.3. Quick Check
**Question 1.** What is the main data structure in NumPy?

A. `dictionary`  
B. `tuple`  
C. `DataFrame`  
D. `ndarray`

**Question 2. True or false?** NumPy is designed mainly for numerical computing.

## Exercises
### Exercise 1.1. Identify the Data Structure
Consider:

```python
import numpy as np

x = np.array([2, 4, 6, 8])
```

Answer the following:

1. What type of NumPy data structure is `x`?
2. Predict the number of dimensions of `x`.
3. Explain why `x` is suitable for numerical computation compared with an ordinary Python list.

### Exercise 1.2. Connect to Data Science
Give one Data Science example in which data could be represented as:

- a one-dimensional array;
- a two-dimensional matrix;
- a three-dimensional array.

---

# Part 2. Why Learn NumPy?
## 2.1. Importance in Data Analysis
NumPy provides an efficient foundation for numerical work in Python. When data are numerical, using NumPy arrays often makes code shorter, clearer, and faster.

## 2.2. Python Lists and NumPy Arrays
A Python list can store values of different types:

```python
values = [10, 2.5, "Python", True]
```

A NumPy array usually stores values with one common data type:

```python
import numpy as np

values = np.array([10, 20, 30, 40])
print(values.dtype)
```

Because NumPy arrays have a regular structure, numerical operations can be implemented efficiently.

## 2.3. Example: Multiplying Values
### Using a Python List
```python
values = [1, 2, 3, 4]

result = []
for value in values:
    result.append(value * 10)

print(result)
```

### Mini Exercise — Vectorization

Rewrite the operation without a loop.

```python
x = np.array([1, 2, 3, 4])

# result = x * ... + ...
# print(result)
```

Output:

```text
[10, 20, 30, 40]
```

### Using NumPy
```python
import numpy as np

values = np.array([1, 2, 3, 4])
result = values * 10

print(result)
```

Output:

```text
[10 20 30 40]
```

NumPy allows `values * 10` to be applied to the entire array. This is a simple example of **vectorization**.

## 2.4. Quick Check
**Question 1.** Why are NumPy arrays efficient for numerical calculations?

A. They automatically connect to the Internet.  
B. They use a homogeneous and optimized array structure.  
C. They do not use memory.  
D. They always contain text.

**Question 2.** Which expression multiplies every element of a NumPy array `a` by 10?

A. `a.append(10)`  
B. `a.sort(10)`  
C. `a * 10`  
D. `a.add("10")`

## Exercises
### Exercise 2.1. Compare Lists and NumPy
Write two programs that multiply the values `[2, 4, 6, 8]` by 5.

- Method 1: use a Python list and a loop.
- Method 2: use NumPy.

Then compare the number of lines required by the two approaches.

### Exercise 2.2. Vectorization
Given:

```python
a = np.array([1, 3, 5, 7])
```

Without using a loop, create new arrays in which each element is:

1. increased by 10;
2. multiplied by 2;
3. squared.

---

# Part 3. Installing and Importing NumPy
## 3.1. Installation
Install NumPy using:

```bash
pip install numpy
```

NumPy is already installed in many environments such as Google Colab and Anaconda.

## 3.2. Importing NumPy
The standard convention is:

```python
import numpy as np
```

The alias `np` is widely used in Python code, documentation, and teaching materials.

## 3.3. Check the Version
```python
import numpy as np

print(np.__version__)
```

### Mini Exercise — `np.__version__`

Complete the code to display the installed NumPy version.

```python
# version = ...
# print(version)
```

**Hint:** use `np.__version__`.

## Exercises
### Exercise 3.1. Check Your Environment
Run:

```python
import numpy as np

print(np.__version__)
```

Record:

1. the NumPy version being used;
2. the standard NumPy alias;
3. the attribute used to check the version.

---

# Part 4. Feature Group: Creating Arrays
## 4.1. Related NumPy Commands
| Command | Meaning |
|---|---|
| `np.array(data)` | Convert a list, tuple, or nested structure into an `ndarray`. |
| `np.zeros(shape)` | Create an array filled with zeros. |
| `np.ones(shape)` | Create an array filled with ones. |
| `np.full(shape, value)` | Create an array filled with a specified value. |
| `np.arange(start, stop, step)` | Create regularly spaced values; `stop` is excluded. |
| `np.linspace(start, stop, n)` | Create exactly `n` evenly spaced values between two endpoints. |
| `np.eye(n)` | Create an `n × n` identity matrix. |

## 4.2. Create an Array from a List
```python
import numpy as np

a = [9, 3, 3, 5]
arr = np.array(a)

print(arr)
```

Output:

```text
[9 3 3 5]
```

## 4.3. Create a One-Dimensional Array
```python
arr = np.array([10, 20, 30, 40])
print(arr)
```

## 4.4. Create a Two-Dimensional Array
```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

## 4.5. Create a Three-Dimensional Array
```python
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

print(tensor)
```

A three-dimensional array can be interpreted as multiple matrices stacked together.

## 4.6. Common Array-Creation Functions
```python
np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

```python
np.zeros((2, 3))
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

```python
np.ones((2, 3))
```

```python
np.full((2, 3), 7)
```

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

```python
np.linspace(0, 1, 5)
```

Output:

```text
[0.   0.25 0.5  0.75 1.  ]
```

```python
np.eye(3)
```

### Mini Exercise — Array-Creation Functions

Complete the following commands.

```python
# zeros = np.zeros((..., ...))
# ones = np.ones((..., ...))
# filled = np.full((..., ...), ...)
# even_numbers = np.arange(..., ..., ...)
# points = np.linspace(..., ..., ...)
# identity = np.eye(...)
```

Create:

1. a `2 × 4` zero matrix;
2. a `3 × 2` one matrix;
3. a `2 × 3` matrix filled with 5;
4. even numbers from 0 to 10;
5. five equally spaced values from 0 to 1;
6. a `4 × 4` identity matrix.

Output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

## 4.7. Quick Check
**Question 1.** Which function converts a Python list into a NumPy array?

A. `np.reshape()`  
B. `np.array()`  
C. `np.list()`  
D. `np.convert()`

**Question 2.** Which function creates evenly spaced values between two endpoints?

A. `np.stack()`  
B. `np.mean()`  
C. `np.split()`  
D. `np.linspace()`

## Exercises
### Exercise 4.1. Create Basic Arrays
Use NumPy to create:

1. the array `[5, 10, 15, 20]`;
2. a `3 × 4` matrix of zeros;
3. a `2 × 5` matrix of ones;
4. a `3 × 3` matrix filled with 7;
5. the even numbers from 0 to 18;
6. six evenly spaced values from 0 to 1.

### Exercise 4.2. Identity Matrix
Create a `4 × 4` identity matrix and explain where the values equal to 1 appear.

---

# Part 5. Feature Group: Array Properties
## 5.1. Related Attributes
| Attribute | Meaning |
|---|---|
| `arr.ndim` | Number of dimensions. |
| `arr.shape` | Size along each dimension. |
| `arr.size` | Total number of elements. |
| `arr.dtype` | Data type of the elements. |
| `arr.itemsize` | Number of bytes per element. |
| `arr.nbytes` | Total number of bytes used by the array elements. |

## 5.2. Example
```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)
```

### Mini Exercise — Array Properties

Complete the code.

```python
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)
# print(arr.nbytes)
```

Then explain the difference between `size`, `itemsize`, and `nbytes`.

Interpretation:

- `arr.ndim = 2`: the array has two dimensions.
- `arr.shape = (2, 3)`: the array has two rows and three columns.
- `arr.size = 6`: the array has six elements in total.
- `arr.dtype`: reports the element data type.
- `arr.itemsize`: reports bytes per element.
- `arr.nbytes`: reports total memory used by the elements.

## 5.3. Good Habit
Before reshaping, broadcasting, or passing data to a machine-learning model, inspect:

```python
print(arr.shape)
print(arr.dtype)
```

### Mini Exercise — `nbytes` and `dtype`

Create the same values with `int8` and `int64`, then compare memory use.

```python
# a = np.array([1, 2, 3, 4], dtype=np.int8)
# b = np.array([1, 2, 3, 4], dtype=np.int64)

# print(a.nbytes)
# print(b.nbytes)
```

Many NumPy errors are caused by unexpected shapes or data types.

## Exercises
### Exercise 5.1. Read Array Properties
Given:

```python
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
```

Before running the code, predict:

1. `A.ndim`;
2. `A.shape`;
3. `A.size`.

Then run the code and check your predictions.

### Exercise 5.2. Data Types and Memory
Create two arrays containing `[1, 2, 3, 4]`, one with `int64` and one with `int8`.

Compare:

```python
arr.dtype
arr.itemsize
arr.nbytes
```

---

# Part 6. Feature Group: Indexing and Slicing
## 6.1. Related Syntax
| Syntax | Meaning |
|---|---|
| `arr[i]` | Select the element at position `i`. |
| `arr[-1]` | Select the last element. |
| `arr[a\:b]` | Select elements from index `a` up to, but not including, `b`. |
| `arr[::step]` | Select elements using a specified step. |
| `matrix[i, j]` | Select the element at row `i`, column `j`. |
| `matrix[r1\:r2, c1\:c2]` | Select a two-dimensional slice. |
| `arr.copy()` | Create an independent copy. |

## 6.2. One-Dimensional Indexing
```python
arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[2])
print(arr[-1])
```

### Mini Exercise — 1D Indexing

Given:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Complete:

```python
# first = arr[...]
# third = arr[...]
# last = arr[...]

# print(first, third, last)
```

Output:

```text
10
30
40
```

## 6.3. Two-Dimensional Indexing
```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix[0, 1])
print(matrix[1, 2])
```

### Mini Exercise — 2D Indexing

Given a matrix, retrieve:

- row 0, column 2;
- row 1, column 0.

```python
# value1 = matrix[..., ...]
# value2 = matrix[..., ...]
```

Output:

```text
2
6
```

## 6.4. One-Dimensional Slicing
```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[::2])
```

### Mini Exercise — 1D Slicing

Complete the slices.

```python
# middle = arr[...:...]
# every_second = arr[::...]
# reversed_arr = arr[::...]
```

Output:

```text
[20 30 40]
[10 30 50]
```

## 6.5. Two-Dimensional Slicing
```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0:2, 1:3])
```

### Mini Exercise — 2D Slicing

Extract:

1. the first two rows;
2. the last two columns;
3. rows 1–2 and columns 1–2.

```python
# first_two_rows = matrix[...]
# last_two_cols = matrix[...]
# submatrix = matrix[...]
```

Output:

```text
[[2 3]
 [5 6]]
```

## 6.6. Views and Copies
Many NumPy slices return a **view**, which may share memory with the original array.

```python
arr = np.array([10, 20, 30, 40])

view = arr[1:3]
view[0] = 999

print(arr)
```

Output:

```text
[ 10 999  30  40]
```

Create an independent copy with:

```python
copy = arr[1:3].copy()
```

### Mini Exercise — View vs. Copy

Create both a view and a copy from the same slice.

```python
# view = arr[...]
# independent_copy = arr[...].copy()
```

Modify both and compare the original array.

## Exercises
### Exercise 6.1. Indexing
Given:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Extract:

1. the first element;
2. the third element;
3. the last element.

### Exercise 6.2. Slicing
Given:

```python
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
```

Extract:

1. the first two rows;
2. the last two columns;
3. the submatrix consisting of rows 2–3 and columns 2–4;
4. the last row.

### Exercise 6.3. View or Copy?
Create a slice, modify one element of the slice, and inspect the original array. Repeat the experiment using `.copy()` and compare the results.

---

# Part 7. Feature Group: Reshape, Resize, Stack, and Split
## 7.1. Related Commands
| Command | Meaning |
|---|---|
| `arr.reshape(r, c)` | Change the shape if the number of elements is compatible. |
| `arr.reshape(..., -1)` | Let NumPy infer one dimension automatically. |
| `arr.flatten()` | Flatten the array and return a copy. |
| `arr.ravel()` | Flatten the array and often return a view when possible. |
| `np.resize(arr, shape)` | Change the total size; values may be repeated. |
| `np.vstack((a, b))` | Stack arrays vertically. |
| `np.hstack((a, b))` | Stack arrays horizontally. |
| `np.stack((a, b), axis=k)` | Stack arrays along a new axis. |
| `np.split(arr, n)` | Split an array into `n` equal parts when possible. |
| `np.hsplit(matrix, n)` | Split a matrix along columns. |

## 7.2. Reshape
```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)

print(matrix)
```

Output:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

Use `-1` to let NumPy infer one dimension:

```python
matrix = arr.reshape(2, -1)
print(matrix.shape)
```

### Mini Exercise — `reshape()`

Given:

```python
arr = np.arange(12)
```

Complete:

```python
# A = arr.reshape(..., ...)
# B = arr.reshape(3, -1)

# print(A.shape)
# print(B.shape)
```

Create shapes `(4, 3)` and `(3, 4)`.

## 7.3. Flatten and Ravel
```python
flat = matrix.flatten()
flat_view = matrix.ravel()
```

### Mini Exercise — `flatten()` vs. `ravel()`

Complete:

```python
# flat1 = matrix.flatten()
# flat2 = matrix.ravel()

# print(flat1.shape)
# print(flat2.shape)
```

Then explain which one always returns a copy.

- `flatten()` returns a copy.
- `ravel()` often returns a view when possible.

## 7.4. Resize
```python
arr = np.array([1, 2, 3, 4])
resized = np.resize(arr, (2, 3))

print(resized)
```

### Mini Exercise — `np.resize()`

Resize `[1, 2, 3, 4]` to shape `(3, 2)`.

```python
# resized = np.resize(..., (..., ...))
# print(resized)
```

Observe what happens when more output positions are required than original values.

Output:

```text
[[1 2 3]
 [4 1 2]]
```

`np.resize()` may repeat values when the requested shape contains more positions than the original array.

## 7.5. Stacking
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(np.stack((a, b), axis=0))
```

### Mini Exercise — Stacking

Complete:

```python
# vertical = np.vstack((a, b))
# horizontal = np.hstack((a, b))
# stacked = np.stack((a, b), axis=...)

# print(vertical)
# print(horizontal)
# print(stacked.shape)
```

## 7.6. Splitting
```python
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(arr, 3)

print(parts)
```

### Mini Exercise — Splitting

Split the values 1 through 12 into:

1. three equal parts;
2. four equal parts.

```python
# arr = np.arange(..., ...)
# parts3 = np.split(arr, ...)
# parts4 = np.split(arr, ...)
```

Output:

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

## Exercises
### Exercise 7.1. Reshape
Create:

```python
arr = np.arange(1, 13)
```

Reshape it into:

1. a `3 × 4` matrix;
2. a `2 × 6` matrix;
3. a matrix with 4 rows and let NumPy infer the number of columns using `-1`.

### Exercise 7.2. Flatten and Ravel
From a `3 × 4` matrix, create:

```python
flat1 = matrix.flatten()
flat2 = matrix.ravel()
```

Print the `shape` of both results and explain the important difference between the two commands.

### Exercise 7.3. Stack and Split
Given:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Do the following:

1. stack vertically;
2. stack horizontally;
3. use `np.stack()` with `axis=0`;
4. create the values 1 through 8 and split them into four equal parts.

---

# Part 8. Feature Group: Broadcasting and Arithmetic
## 8.1. Related Expressions
| Expression | Meaning |
|---|---|
| `a + b`, `a - b` | Element-wise addition and subtraction. |
| `a * b` | Element-wise multiplication. |
| `a / b` | Element-wise division. |
| `a ** p` | Raise each element to power `p`. |
| `a % b` | Element-wise remainder. |
| `array + scalar` | Broadcast a scalar to all elements. |
| `matrix + row` | Broadcast a compatible one-dimensional row across matrix rows. |

## 8.2. Broadcasting with a Scalar
```python
arr = np.array([1, 2, 3, 4])
result = arr + 10

print(result)
```

Output:

```text
[11 12 13 14]
```

The scalar `10` is conceptually applied to every element.

## 8.3. Broadcasting Between Arrays
```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([10, 20, 30])
result = matrix + row

print(result)
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

## 8.4. Basic Broadcasting Rule
Starting from the rightmost dimensions, two dimensions are compatible if:

- they are equal; or
- one of them is `1`.

If shapes are incompatible, NumPy raises an error.

## 8.5. Basic Arithmetic Operations
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(b % a)
```

### Mini Exercise — Element-Wise Arithmetic

Complete:

```python
# add = a + b
# subtract = a - b
# multiply = a * b
# divide = a / b
# square = a ** ...
# remainder = b % a
```

Remember: `a * b` performs element-wise multiplication, not matrix multiplication.

## Exercises
### Exercise 8.1. Element-Wise Arithmetic
Given:

```python
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
```

Calculate:

1. `a + b`;
2. `a - b`;
3. `a * b`;
4. `a / b`;
5. `a ** 2`.

### Exercise 8.2. Broadcasting with a Scalar
Given:

```python
scores = np.array([7, 8, 6, 9])
```

Add 1 point to every score without using a loop.

### Exercise 8.3. Broadcasting with a Vector
Given:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([10, 20, 30])
```

Calculate `A + row`, then explain why broadcasting is valid.

---

# Part 9. Feature Group: Aggregation and Universal Functions
## 9.1. Related Commands
| Command | Meaning |
|---|---|
| `arr.sum()`, `arr.mean()` | Sum and arithmetic mean. |
| `arr.min()`, `arr.max()` | Minimum and maximum. |
| `np.median(arr)` | Median. |
| `np.var(arr)`, `np.std(arr)` | Variance and standard deviation. |
| `func(..., axis=0)` | Aggregate by column. |
| `func(..., axis=1)` | Aggregate by row. |
| `np.sqrt(arr)` | Square root element by element. |
| `np.exp(arr)`, `np.log(arr)` | Exponential and natural logarithm element by element. |
| `np.sin(arr)` | Sine element by element. |
| `np.abs(arr)`, `np.round(arr)` | Absolute value and rounding. |

## 9.2. Aggregation
```python
arr = np.array([9, 3, 3, 5])

print(arr.sum())
print(arr.mean())
print(arr.min())
print(arr.max())
print(np.median(arr))
print(np.var(arr))
print(np.std(arr))
```

### Mini Exercise — Aggregation Functions

Given:

```python
x = np.array([4, 8, 6, 10, 12])
```

Complete:

```python
# total = x.____()
# mean_value = x.____()
# minimum = x.____()
# maximum = x.____()
# median = np.____(x)
# variance = np.____(x)
# std_dev = np.____(x)
```

## 9.3. Aggregation Along an Axis
```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix.sum(axis=0))
print(matrix.sum(axis=1))
```

### Mini Exercise — `axis`

Complete:

```python
# column_sum = matrix.sum(axis=...)
# row_sum = matrix.sum(axis=...)
# column_mean = matrix.mean(axis=...)
```

State what `axis=0` and `axis=1` mean.

Output:

```text
[5 7 9]
[ 6 15]
```

- `axis=0`: aggregate down the rows, producing one result per column.
- `axis=1`: aggregate across columns, producing one result per row.

## 9.4. Universal Functions
```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
```

Output:

```text
[1. 2. 3. 4.]
```

Other examples:

```python
print(np.exp(np.array([0, 1, 2])))
print(np.log(np.array([1, np.e, np.e**2])))
print(np.sin(np.array([0, np.pi / 2, np.pi])))
print(np.abs(np.array([-3, -1, 2, 4])))
print(np.round(np.array([1.234, 5.678]), 2))
```

### Mini Exercise — Universal Functions

Given:

```python
x = np.array([1.0, 4.0, 9.0, 16.0])
```

Complete:

```python
# sqrt_x = np.sqrt(x)
# log_x = np.log(x)
# abs_x = np.abs(...)
# rounded = np.round(..., 2)
```

## Exercises
### Exercise 9.1. Quick Statistics
Given:

```python
x = np.array([4, 8, 6, 10, 12])
```

Calculate:

1. sum;
2. mean;
3. minimum;
4. maximum;
5. median;
6. standard deviation.

### Exercise 9.2. Axis
Given:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

Calculate:

1. the sum of each column;
2. the sum of each row;
3. the mean of each column.

### Exercise 9.3. Ufunc
Given:

```python
x = np.array([1, 4, 9, 16])
```

Apply `np.sqrt()` and explain the output.

---

# Part 10. Feature Group: Boolean Operations
## 10.1. Related Commands
| Expression | Meaning |
|---|---|
| `arr > value` | Create a Boolean array from a comparison. |
| `arr[arr > value]` | Filter elements satisfying a condition. |
| `(cond1) & (cond2)` | Element-wise AND. |
| `(cond1) \| (cond2)` | Element-wise OR. |
| `~mask` | Element-wise NOT. |
| `np.where(cond, a, b)` | Choose `a` when the condition is true and `b` otherwise. |

## 10.2. Comparison and Boolean Filtering
```python
arr = np.array([10, 20, 30, 40])

print(arr > 20)
```

Output:

```text
[False False  True  True]
```

```python
selected = arr[arr > 20]
print(selected)
```

### Mini Exercise — Combined Conditions

Select values from 20 through 35 inclusive.

```python
x = np.array([10, 20, 25, 30, 35, 40])

# selected = x[(x >= ...) & (x <= ...)]
# print(selected)
```

Output:

```text
[30 40]
```

## 10.3. Combine Conditions
```python
selected = arr[(arr >= 20) & (arr <= 30)]
print(selected)
```

Output:

```text
[20 30]
```

When combining multiple comparisons, place each condition inside parentheses.

## 10.4. Vectorized Conditional Logic with `np.where()`
```python
arr = np.array([10, 20, 30, 40])

labels = np.where(arr >= 30, "high", "low")
print(labels)
```

### Mini Exercise — `np.where()`

Create `"Pass"` / `"Fail"` labels.

```python
scores = np.array([4, 7, 8, 5, 9, 3])

# labels = np.where(scores >= ..., ..., ...)
# print(labels)
```

Output:

```text
['low' 'low' 'high' 'high']
```

## Exercises
### Exercise 10.1. Filter with One Condition
Given:

```python
scores = np.array([4, 7, 8, 5, 9, 6])
```

Filter:

1. scores greater than or equal to 7;
2. scores below 6.

### Exercise 10.2. Combine Conditions
Filter scores from 6 through 8, including both endpoints.

### Exercise 10.3. Create Labels
Use `np.where()` to create:

- `"Pass"` when the score is `>= 5`;
- `"Fail"` when the score is `< 5`.

---

# Part 11. Feature Group: Linear Algebra
## 11.1. Related Commands
| Command | Meaning |
|---|---|
| `A @ B` | Matrix multiplication. |
| `np.dot(A, B)` | Dot product or matrix product depending on dimensions. |
| `A.T` | Transpose. |
| `np.linalg.det(A)` | Determinant. |
| `np.linalg.inv(A)` | Inverse of a nonsingular square matrix. |
| `np.linalg.solve(A, b)` | Solve `Ax=b`. |
| `np.linalg.eig(A)` | Eigenvalues and eigenvectors. |
| `np.inner(a, b)` | Inner product. |
| `np.outer(a, b)` | Outer product. |
| `np.vdot(a, b)` | Vector dot product with complex conjugation when needed. |

## 11.2. Matrix Multiplication
```python
A = np.array([
    [1, 2],
    [3, 4]
])

print(np.dot(A, A))
print(A @ A)
```

### Mini Exercise — Matrix Multiplication

Complete both operations.

```python
# elementwise = A * A
# matrix_product = A @ A

# print(elementwise)
# print(matrix_product)
```

Explain why the two outputs differ.

Output:

```text
[[ 7 10]
 [15 22]]
```

## 11.3. Element-Wise vs. Matrix Multiplication
```python
print(A * A)
print(A @ A)
```

- `A * A`: element-wise multiplication.
- `A @ A`: matrix multiplication.

## 11.4. Transpose, Determinant, and Inverse
```python
print(A.T)
print(np.linalg.det(A))
print(np.linalg.inv(A))
```

### Mini Exercise — Transpose, Determinant, Inverse

```python
# transpose = A.T
# determinant = np.linalg.det(A)
# inverse = np.linalg.inv(A)

# print(transpose)
# print(determinant)
# print(inverse)
```

An inverse exists only for a square, nonsingular matrix.

## 11.5. Solve a Linear System
```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])

x = np.linalg.solve(A, b)
print(x)
print(A @ x)
```

### Mini Exercise — `np.linalg.solve()`

Solve:

```python
A = np.array([
    [3, 1],
    [1, 2]
])

b = np.array([9, 8])

# x = np.linalg.solve(..., ...)
# check = A @ x
```

## 11.6. Eigenvalues and Eigenvectors
```python
eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)
print(eigenvectors)
```

### Mini Exercise — `np.linalg.eig()`

Complete:

```python
# eigenvalues, eigenvectors = np.linalg.eig(A)

# print(eigenvalues)
# print(eigenvectors)
```

## Exercises
### Exercise 11.1. Element-Wise and Matrix Multiplication
Given:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [2, 0],
    [1, 2]
])
```

Calculate and compare:

```python
A * B
A @ B
```

### Exercise 11.2. Determinant and Transpose
Calculate:

```python
A.T
np.linalg.det(A)
```

### Exercise 11.3. Solve a System
Given:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])
```

Solve `Ax=b` using `np.linalg.solve()` and verify the result using `A @ x`.

---

# Part 12. Feature Group: Random Numbers and Statistics
## 12.1. Related Commands
| Command | Meaning |
|---|---|
| `np.random.default_rng(seed)` | Create a modern random-number generator. |
| `rng.integers(low, high, size)` | Generate random integers; `high` is excluded. |
| `rng.uniform(...)` | Sample from a uniform distribution. |
| `rng.normal(loc, scale, size)` | Sample from a normal distribution. |
| `rng.binomial(...)` | Sample from a binomial distribution. |
| `rng.poisson(...)` | Sample from a Poisson distribution. |
| `np.percentile(data, q)` | Calculate percentile `q` on a 0–100 scale. |
| `np.quantile(data, q)` | Calculate quantile `q` on a 0–1 scale. |
| `np.isnan(data)` | Identify `NaN` values. |
| `np.nanmean(data)` | Calculate the mean while ignoring `NaN`. |

## 12.2. Create a Random-Number Generator
```python
rng = np.random.default_rng(42)
```

### Mini Exercise — `default_rng()`

Create a generator with seed `123`.

```python
# rng = np.random.default_rng(...)
```

The seed `42` supports reproducibility in a compatible environment.

## 12.3. Generate Random Values
```python
print(rng.integers(low=1, high=10, size=5))
print(rng.uniform(low=0, high=1, size=5))
print(rng.normal(loc=0, scale=1, size=5))
print(rng.binomial(n=10, p=0.5, size=5))
print(rng.poisson(lam=3, size=5))
```

### Mini Exercise — Random Distributions

Generate:

```python
# integers = rng.integers(low=1, high=11, size=5)
# uniform = rng.uniform(low=0, high=1, size=5)
# normal = rng.normal(loc=0, scale=1, size=5)
# binomial = rng.binomial(n=10, p=0.5, size=5)
# poisson = rng.poisson(lam=3, size=5)
```

## 12.4. Descriptive Statistics
```python
data = np.array([12, 15, 18, 20, 25])

print(np.mean(data))
print(np.median(data))
print(np.var(data))
print(np.std(data))
print(np.percentile(data, 25))
print(np.quantile(data, 0.75))
```

### Mini Exercise — Percentile and Quantile

```python
# p25 = np.percentile(data, ...)
# p50 = np.percentile(data, ...)
# q75 = np.quantile(data, ...)
```

By default, `np.var()` and `np.std()` use `ddof=0`, corresponding to division by `N`.

For the common sample convention, divide by `N-1` using:

```python
print(np.var(data, ddof=1))
print(np.std(data, ddof=1))
```

### Mini Exercise — `ddof`

Calculate both population and sample standard deviations.

```python
# population_std = np.std(data, ddof=...)
# sample_std = np.std(data, ddof=...)
```

## 12.5. Missing Values
```python
data = np.array([10.0, 20.0, np.nan, 40.0])

print(np.mean(data))
print(np.nanmean(data))
print(np.nanmedian(data))
print(np.isnan(data))
```

### Mini Exercise — Missing Values

Complete:

```python
# missing_mask = np.isnan(data)
# mean_ignore_nan = np.nanmean(data)
# clean_data = data[~np.isnan(data)]

# print(missing_mask)
# print(mean_ignore_nan)
# print(clean_data)
```

`np.mean(data)` returns `nan` when the array contains a missing value. Functions such as `np.nanmean()` ignore `NaN`.

## Exercises
### Exercise 12.1. Random Integers
Create:

```python
rng = np.random.default_rng(42)
```

Then generate 10 random integers from 1 to 100.

### Exercise 12.2. Normal Distribution
Generate 1,000 values from a normal distribution with:

- mean = 0;
- standard deviation = 1.

Calculate the sample mean and standard deviation.

### Exercise 12.3. Percentile and Quantile
Given:

```python
data = np.array([10, 20, 30, 40, 50])
```

Calculate:

1. the 25th percentile;
2. the 50th percentile;
3. the 0.75 quantile.

### Exercise 12.4. NaN
Given:

```python
data = np.array([10.0, np.nan, 20.0, 30.0])
```

Do the following:

1. identify the location of `NaN`;
2. calculate the mean while ignoring `NaN`;
3. remove the `NaN` value.

---

# Part 13. Feature Group: Vectorization and Performance
## 13.1. Core Idea
Vectorization means expressing an operation at the array level rather than iterating manually through elements with a Python loop.

## 13.2. Example
```python
a = np.arange(5)
result = a * 10

print(result)
```

Output:

```text
[ 0 10 20 30 40]
```

Without NumPy:

```python
a = list(range(5))

result = []
for value in a:
    result.append(value * 10)

print(result)
```

Vectorized code is often:

- shorter;
- easier to read;
- faster for large numerical arrays;
- better suited to data-analysis workflows.

## Exercises
### Exercise 13.1. Convert a Loop to Vectorization
Rewrite the following code using NumPy without an explicit loop:

```python
values = [1, 2, 3, 4, 5]
result = []

for x in values:
    result.append(x * 3 + 1)
```

### Exercise 13.2. Vectorized Condition
Given:

```python
sales = np.array([80, 120, 95, 150, 60])
```

Use `np.where()` to label each value as:

- `"High"` if sales are `>= 100`;
- `"Low"` otherwise.

---

# Part 14. Feature Group: Memory, Data Types, Sorting, Searching, and Images
## 14.1. Related Commands
| Command | Meaning |
|---|---|
| `arr.nbytes` | Total bytes used by the array elements. |
| `arr.astype(dtype)` | Convert values to another data type. |
| `np.sort(arr)` | Return sorted values. |
| `np.where(condition)` | Return indices satisfying a condition. |
| `np.unique(arr)` | Return unique values. |
| `np.unique(arr, return_counts=True)` | Return unique values and their frequencies. |
| `np.clip(arr, low, high)` | Restrict values to a specified interval. |

## 14.2. Check Memory Use
```python
arr = np.array([1, 2, 3, 4], dtype=np.int32)

print(arr.nbytes)
print(arr.dtype)
```

## 14.3. Convert Data Types
```python
arr = np.array([1.2, 2.8, 3.5])
integers = arr.astype(np.int32)

print(integers)
```

### Mini Exercise — `astype()`

Convert:

```python
x = np.array([1.9, 2.2, 3.8])

# integers = x.astype(...)
# print(integers)
```

Output:

```text
[1 2 3]
```

Converting floating-point values to integers removes the fractional part.

## 14.4. Sorting and Searching
```python
arr = np.array([9, 3, 7, 1])
sorted_arr = np.sort(arr)

print(sorted_arr)
```

### Mini Exercise — `np.sort()`

Sort:

```python
x = np.array([8, 3, 6, 1, 5])

# sorted_x = np.sort(...)
# print(sorted_x)
```

Output:

```text
[1 3 7 9]
```

```python
arr = np.array([10, 20, 30, 40])
indices = np.where(arr > 20)

print(indices)
```

### Mini Exercise — `np.where(condition)`

Return the indices of values greater than or equal to 30.

```python
x = np.array([10, 20, 30, 40, 50])

# indices = np.where(...)
# print(indices)
```

```python
arr = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique(arr, return_counts=True)

print(values)
print(counts)
```

### Mini Exercise — `np.unique()`

Return unique values and frequencies.

```python
x = np.array([2, 2, 3, 3, 3, 4, 5, 5])

# values, counts = np.unique(
#     ...,
#     return_counts=...
# )

# print(values)
# print(counts)
```

## 14.5. Working with Images
Digital images can be represented as NumPy arrays:

- a grayscale image can be represented by a two-dimensional array;
- a color image can be represented by a three-dimensional array containing height, width, and color channels.

Example:

```python
image = np.array([
    [0, 128, 255],
    [255, 128, 0],
    [50, 100, 150]
])

print(image.shape)
```

Increase brightness:

```python
brighter = np.clip(image + 30, 0, 255)
```

### Mini Exercise — `np.clip()`

Increase brightness by 50 and keep all values in `[0, 255]`.

```python
# brighter = np.clip(image + ..., ..., ...)
```

`np.clip()` keeps values in the valid interval, such as 0 through 255 for image intensities.

## Exercises
### Exercise 14.1. Data Types
Create:

```python
x = np.array([1.2, 2.8, 3.5])
```

Convert `x` to `int32` and inspect the result.

### Exercise 14.2. Sorting and Unique Values
Given:

```python
x = np.array([4, 2, 4, 1, 2, 2, 5])
```

Do the following:

1. sort the array;
2. return the unique values;
3. count the frequency of each value.

### Exercise 14.3. Digital Image
Given:

```python
image = np.array([
    [0, 100, 240],
    [50, 200, 255]
])
```

Increase brightness by 30 while ensuring all values remain within `[0, 255]`.

---

# Part 15. Integration with Pandas and Scikit-learn
## 15.1. Integration with Pandas
```python
import numpy as np
import pandas as pd

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

df = pd.DataFrame(arr, columns=["A", "B"])
array_from_df = df.to_numpy()

df["A_sqrt"] = np.sqrt(df["A"])
```

### Mini Exercise — NumPy ↔ Pandas

Complete:

```python
# df = pd.DataFrame(arr, columns=[..., ...])
# array_again = df.to_numpy()
# df["A_sqrt"] = np.sqrt(df["A"])
```

Interpretation:

- `pd.DataFrame(arr, columns=...)`: create a DataFrame from a NumPy array.
- `df.to_numpy()`: convert a DataFrame to a NumPy array.
- `np.sqrt(df["A"])`: apply a NumPy function to a Pandas column.

## 15.2. Integration with Scikit-learn
```python
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(np.array([[5]]))
print(prediction)
```

### Mini Exercise — NumPy with Scikit-learn

Inspect:

```python
# print(X.shape)
# print(y.shape)
```

Then explain why `X` is 2D while `y` is 1D.

In machine learning:

- `X` is commonly a feature matrix;
- `y` is a target vector;
- NumPy arrays are a common array-like format for model input.

## Exercises
### Exercise 15.1. NumPy to Pandas
Create:

```python
arr = np.array([
    [1, 10],
    [2, 20],
    [3, 30]
])
```

Convert it to a DataFrame with columns `"ID"` and `"Value"`.

### Exercise 15.2. Pandas to NumPy
Convert the DataFrame back to a NumPy array using `to_numpy()` and inspect its `shape`.

### Exercise 15.3. Feature Matrix
Given:

```python
X = np.array([
    [20, 1],
    [25, 2],
    [30, 3]
])
```

Explain:

1. what `X.shape` means;
2. what the rows represent;
3. what the columns represent in a machine-learning context.

---

# Part 16. Common NumPy Errors
## 16.1. Shape Mismatch
```python
a = np.ones((2, 3))
b = np.ones((2, 2))

# a + b raises a broadcasting error
```

The two shapes are not broadcasting-compatible.

## 16.2. Invalid Reshape
```python
arr = np.arange(10)

# arr.reshape(3, 4) raises an error
```

Ten elements cannot be reshaped into a `3 × 4` array because that shape requires 12 elements.

## 16.3. Division by Zero
```python
arr = np.array([1.0, 0.0])

print(1 / arr)
```

This may produce `inf` and a runtime warning.

## 16.4. Integer Overflow
```python
arr = np.array([127], dtype=np.int8)

print(arr + 1)
```

`int8` cannot represent values larger than 127, so overflow may occur.

## 16.5. Unexpected Changes Through Views
```python
arr = np.array([10, 20, 30, 40])

view = arr[1:3]
view[0] = 999

print(arr)
```

Use `.copy()` when an independent array is required:

```python
copy = arr[1:3].copy()
```

## Exercises
### Exercise 16.1. Predict Reshape Errors
Given:

```python
x = np.arange(10)
```

Which of the following commands are valid?

```python
x.reshape(2, 5)
x.reshape(5, 2)
x.reshape(3, 4)
x.reshape(1, 10)
```

Explain your answer using the total number of elements.

### Exercise 16.2. Predict Broadcasting
Consider the following shape pairs:

1. `(3, 4)` and `(4,)`;
2. `(3, 4)` and `(1, 4)`;
3. `(3, 4)` and `(3, 1)`;
4. `(3, 4)` and `(2, 4)`.

Predict which pairs are broadcasting-compatible.

### Exercise 16.3. View
Write a short example showing that modifying a slice can modify the original array, then fix the issue using `.copy()`.

---

# Part 17. Good Practices
- Import NumPy using `import numpy as np`.
- Prefer vectorized operations over Python loops when practical.
- Check `shape`, `ndim`, and `dtype` before complex operations.
- Use broadcasting only when the intended shape behavior is clear.
- Distinguish `A * B` from `A @ B`.
- Use `.copy()` when an independent array is required.
- Choose data types carefully to balance range, precision, and memory.
- Use a fixed seed when reproducibility is important.
- Handle `NaN`, `inf`, division by zero, and overflow explicitly.

## Exercises
### Exercise 17.1. Inspect the Code
Consider:

```python
A = np.arange(12).reshape(3, 4)
b = np.array([10, 20, 30])
result = A + b
```

Do the following:

1. inspect `A.shape` and `b.shape`;
2. predict whether the code runs successfully;
3. if it fails, modify `b` so broadcasting becomes valid.

### Exercise 17.2. Choose the Better NumPy Style
Compare:

```python
result = []
for x in arr:
    result.append(np.sqrt(x))
```

and:

```python
result = np.sqrt(arr)
```

Which style is more appropriate for NumPy, and why?

---

# Part 18. Content Summary
| Topic | Main idea |
|---|---|
| NumPy | Core Python library for numerical computing. |
| `ndarray` | Homogeneous N-dimensional array. |
| Vectorization | Array operations without explicit Python loops. |
| Broadcasting | Operations on differently shaped but compatible arrays. |
| Indexing and slicing | Access and extract array elements. |
| Reshaping | Change array dimensions. |
| Aggregation | Calculate sums, means, minima, maxima, variance, and standard deviation. |
| Universal functions | Fast element-wise mathematical functions. |
| Linear algebra | Matrix multiplication, inverse, determinant, eigenvalues, and linear-system solving. |
| Random generation | Generate values from probability distributions. |
| Statistics | Mean, median, variance, standard deviation, percentiles, and quantiles. |
| Integration | Exchange data with Pandas, SciPy, Matplotlib, and Scikit-learn. |

---

# Part 19. Review Questions
## 19.1. Multiple-Choice Questions
**Question 1.** What is NumPy primarily used for?

A. Sending emails  
B. Numerical computing  
C. Word processing  
D. Web-page design

**Question 2.** What is the central NumPy data structure?

A. `set`  
B. `ndarray`  
C. `class`  
D. `DataFrame`

**Question 3.** Which function creates an array from a Python list?

A. `np.array()`  
B. `np.frame()`  
C. `np.convert_list()`  
D. `np.list()`

**Question 4.** Which attribute returns an array's shape?

A. `shape`  
B. `mean`  
C. `type()`  
D. `size()`

**Question 5.** Which expression performs matrix multiplication?

A. `A @ B`  
B. `A % B`  
C. `A | B`  
D. `A // B`

**Question 6.** Which function calculates a mean while ignoring `NaN` values?

A. `np.dropna()`  
B. `np.mean_without_missing()`  
C. `np.nanmean()`  
D. `np.ignore_mean()`

**Question 7.** Which function creates an identity matrix?

A. `np.reshape()`  
B. `np.ones_like_text()`  
C. `np.identity_text()`  
D. `np.eye()`

**Question 8.** Which statement about broadcasting is correct?

A. It removes all duplicate values.  
B. It always changes the original array.  
C. It supports operations between compatible shapes.  
D. It converts every array to one dimension.

**Question 9.** In a two-dimensional aggregation, what does `axis=0` usually mean?

A. Reverse all values.  
B. Convert the matrix into one scalar only.  
C. Aggregate down rows and return column-wise values.  
D. Aggregate across columns and return row-wise values.

**Question 10.** Which object is recommended for modern NumPy random-number generation?

A. `np.array.randomize_text()`  
B. `np.random.file_reader()`  
C. `np.random.secure_password()`  
D. `np.random.default_rng()`

## 19.2. True/False Questions
**Question 1.** NumPy arrays usually contain elements of one common data type.  
**Question 2.** Vectorized NumPy operations always require an explicit Python loop.  
**Question 3.** `A * B` and `A @ B` always perform the same operation.  
**Question 4.** NumPy slices may share memory with the original array.  
**Question 5.** Broadcasting requires array dimensions to be compatible.  
**Question 6.** `np.std(data, ddof=1)` can be used for the usual sample-standard-deviation convention.  
**Question 7.** NumPy random-number generation should be assumed to be cryptographically secure.  
**Question 8.** NumPy arrays can be used as inputs to Scikit-learn models.

## 19.3. Short-Answer Questions
**Question 1.** State two differences between a Python list and a NumPy array.  
**Question 2.** Explain vectorization and state one advantage.  
**Question 3.** Explain the difference between element-wise and matrix multiplication.  
**Question 4.** State the basic broadcasting compatibility rule.  
**Question 5.** Explain the difference between a view and a copy.  
**Question 6.** Name four statistical functions available in NumPy.

---

# Part 20. Practical Exercises
## Exercise 1. Array Creation
1. Create an array containing values from 1 to 20.
2. Reshape it into a `4 × 5` matrix.
3. Print its `shape`, `ndim`, `size`, and `dtype`.

## Exercise 2. Indexing and Slicing
Using the `4 × 5` matrix from Exercise 1:

1. Extract the first row.
2. Extract the last column.
3. Extract the central `2 × 3` section.
4. Select all even values using Boolean filtering.

## Exercise 3. Statistics
Create an array of ten numerical values and calculate:

1. mean;
2. median;
3. variance;
4. sample standard deviation;
5. minimum and maximum;
6. the 25th, 50th, and 75th percentiles.

## Exercise 4. Broadcasting
1. Create a `3 × 4` matrix.
2. Create a one-dimensional array with four values.
3. Add the one-dimensional array to each row of the matrix.
4. Explain why broadcasting is valid.

## Exercise 5. Linear Algebra
Given:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])
```

1. Calculate the determinant of `A`.
2. Calculate the inverse of `A`.
3. Solve `Ax=b`.
4. Verify the solution using `A @ x`.

## Exercise 6. Random Data
1. Create a random-number generator with seed `42`.
2. Generate 1,000 values from a standard normal distribution.
3. Calculate the mean and standard deviation.
4. Compare the sample results with the theoretical values.

## Exercise 7. Missing Values
Given:

```python
data = np.array([
    10.0,
    np.nan,
    20.0,
    30.0,
    np.nan,
    40.0
])
```

1. Count the missing values.
2. Calculate the mean while ignoring missing values.
3. Remove all missing values.
4. Replace missing values with the median of the observed values.

---

# Answers and Suggested Responses
## Quick Check Answers
1. D — What is the main data structure in NumPy?  
2. B — Why are NumPy arrays efficient for numerical calculations?  
3. C — Which expression multiplies every element of a NumPy array `a` by 10?  
4. B — Which function converts a Python list into a NumPy array?  
5. D — Which function creates evenly spaced values between two endpoints?

## Multiple-Choice Answers
1. B  
2. B  
3. A  
4. A  
5. A  
6. C  
7. D  
8. C  
9. C  
10. D

## True/False Answers
1. True  
2. False  
3. False  
4. True  
5. True  
6. True  
7. False  
8. True

## Suggested Short Answers
**Question 1.** A Python list can store mixed data types, while a NumPy array usually stores homogeneous data and is optimized for numerical computation.

**Question 2.** Vectorization applies an operation to an entire array without writing an explicit Python loop. It often makes code shorter, clearer, and faster.

**Question 3.** `A * B` multiplies corresponding elements. `A @ B` performs matrix multiplication according to linear-algebra rules.

**Question 4.** Starting from the rightmost dimension, two dimensions are compatible if they are equal or if one of them is 1.

**Question 5.** A view may share memory with the original array, while a copy has independent memory.

**Question 6.** Examples include `np.mean()`, `np.median()`, `np.var()`, `np.std()`, `np.percentile()`, and `np.quantile()`.

## Suggested Solutions to Practical Exercises
### Exercise 1
```python
arr = np.arange(1, 21)
matrix = arr.reshape(4, 5)

print(matrix)
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix.dtype)
```

### Exercise 2
```python
print(matrix[0, :])
print(matrix[:, -1])
print(matrix[1:3, 1:4])
print(matrix[matrix % 2 == 0])
```

### Exercise 3
```python
data = np.array([12, 15, 18, 20, 25, 28, 30, 35, 40, 50])

print(np.mean(data))
print(np.median(data))
print(np.var(data))
print(np.std(data, ddof=1))
print(np.min(data))
print(np.max(data))
print(np.percentile(data, [25, 50, 75]))
```

### Exercise 4
```python
matrix = np.arange(12).reshape(3, 4)
row = np.array([10, 20, 30, 40])

result = matrix + row
print(result)
```

Broadcasting is valid because `matrix.shape` is `(3, 4)` and `row\.shape` is `(4,)`. NumPy treats the one-dimensional array as a compatible row and broadcasts it across the three rows of the matrix.

### Exercise 5
```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
x = np.linalg.solve(A, b)

print(det_A)
print(inv_A)
print(x)
print(A @ x)
```

### Exercise 6
```python
rng = np.random.default_rng(42)

values = rng.normal(loc=0, scale=1, size=1000)

print(np.mean(values))
print(np.std(values, ddof=1))
```

The sample mean should be close to 0 and the sample standard deviation should be close to 1, although they will not necessarily be exactly 0 and 1.

### Exercise 7
```python
data = np.array([
    10.0,
    np.nan,
    20.0,
    30.0,
    np.nan,
    40.0
])

missing_count = np.isnan(data).sum()
mean_ignore_nan = np.nanmean(data)
clean_data = data[~np.isnan(data)]
median_value = np.nanmedian(data)

filled_data = np.where(np.isnan(data), median_value, data)

print(missing_count)
print(mean_ignore_nan)
print(clean_data)
print(filled_data)
```