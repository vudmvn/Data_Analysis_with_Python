# Giới thiệu về NumPy

**Cập nhật lần cuối:** 02 tháng 08 năm 2026

## Giới thiệu bài học

Bài học này giới thiệu **NumPy**, một thư viện cốt lõi của Python dành cho tính toán số. NumPy được thiết kế để làm việc hiệu quả với các mảng lớn, ma trận và tập dữ liệu số. Cấu trúc dữ liệu trung tâm của NumPy là `ndarray`, hỗ trợ các phép toán nhanh, broadcasting, đại số tuyến tính, sinh số ngẫu nhiên và tính toán thống kê.

So với danh sách Python thông thường, mảng NumPy lưu trữ dữ liệu đồng nhất theo cấu trúc bộ nhớ hiệu quả hơn và hỗ trợ các phép toán vector hóa được triển khai bằng mã mức thấp đã tối ưu. Vì vậy, NumPy đặc biệt hữu ích trong phân tích dữ liệu, tính toán khoa học, mô phỏng, xử lý ảnh và học máy.

## Kiến thức và kỹ năng sẽ đạt được

Sau khi hoàn thành bài học, người học có thể:

- Giải thích vai trò của NumPy trong tính toán số.
- Phân biệt mảng NumPy với danh sách Python thông thường.
- Cài đặt và nhập thư viện NumPy.
- Tạo mảng một chiều và mảng nhiều chiều.
- Kiểm tra các thuộc tính như hình dạng, kích thước, số chiều và kiểu dữ liệu.
- Truy cập phần tử bằng indexing và slicing.
- Thay đổi hình dạng, thay đổi kích thước, ghép và tách mảng.
- Thực hiện các phép toán số học theo hướng vector hóa.
- Sử dụng các hàm tổng hợp như `sum()`, `mean()`, `min()` và `max()`.
- Giải thích và áp dụng broadcasting.
- Sử dụng các hàm toán học và universal functions.
- Thực hiện các phép toán cơ bản với ma trận và vector.
- Sinh dữ liệu ngẫu nhiên từ các phân phối xác suất thông dụng.
- Tính các thống kê mô tả cơ bản.
- Hiểu cách NumPy tích hợp với Pandas, SciPy và Scikit-learn.

## Cấu trúc bài học

Bài học gồm các nội dung chính sau:

1. NumPy là gì?
2. Vì sao nên học NumPy?
3. Cài đặt và nhập thư viện.
4. Tạo mảng NumPy.
5. Các thuộc tính của mảng.
6. Indexing và slicing.
7. Thay đổi hình dạng và kích thước.
8. Ghép và tách mảng.
9. Broadcasting.
10. Các phép toán số học và phép tổng hợp.
11. Universal functions.
12. Đại số tuyến tính.
13. Sinh số ngẫu nhiên.
14. Các hàm thống kê.
15. Vector hóa và hiệu năng.
16. Tích hợp với các thư viện Python khác.
17. Câu hỏi ôn tập và bài tập thực hành.

## Yêu cầu chuẩn bị

Người học nên có:

- Kiến thức Python cơ bản.
- Hiểu biết về biến, danh sách, vòng lặp và hàm.
- Môi trường Jupyter Notebook, JupyterLab, Google Colab hoặc môi trường Python tương đương.

---

# NumPy là gì?

**NumPy**, viết tắt của **Numerical Python**, là thư viện Python được thiết kế để thực hiện các phép tính số nhanh và hiệu quả.

Đối tượng quan trọng nhất của NumPy là **mảng N chiều**, được gọi là `ndarray`. Một mảng NumPy có thể biểu diễn:

- Vector một chiều.
- Ma trận hai chiều.
- Tensor ba chiều.
- Các cấu trúc số nhiều chiều hơn.

NumPy cung cấp:

- Các phép toán nhanh trên mảng.
- Tính toán vector hóa.
- Broadcasting.
- Các hàm đại số tuyến tính.
- Các hàm thống kê.
- Công cụ sinh số ngẫu nhiên.
- Khả năng tích hợp với Pandas, SciPy, Matplotlib và Scikit-learn.

## Các đặc trưng chính

### `ndarray`

`ndarray` là cấu trúc dữ liệu trung tâm của NumPy. Nó lưu trữ các phần tử có cùng kiểu dữ liệu trong một mảng nhiều chiều được tổ chức hiệu quả.

### Phép toán vector hóa

Phép toán vector hóa cho phép áp dụng phép tính lên toàn bộ mảng mà không cần viết vòng lặp Python tường minh.

### Broadcasting

Broadcasting cho phép NumPy thực hiện phép toán giữa các mảng có hình dạng khác nhau nhưng tương thích.

### Đại số tuyến tính

NumPy hỗ trợ nhân ma trận, định thức, ma trận nghịch đảo, trị riêng, vector riêng và các tích vector.

### Hàm thống kê

NumPy có các hàm tính trung bình, trung vị, phương sai, độ lệch chuẩn, phân vị và nhiều thống kê mô tả khác.

### Khả năng tích hợp

Mảng NumPy được sử dụng rộng rãi trong:

- Pandas.
- SciPy.
- Matplotlib.
- Scikit-learn.
- Statsmodels.


### Câu hỏi nhanh

**Câu 1.** Cấu trúc dữ liệu trung tâm của NumPy là gì?

A. `DataFrame`  
B. `ndarray`  
C. `dictionary`  
D. `tuple`  

**Câu 2. Đúng hay sai?** NumPy được thiết kế chủ yếu cho tính toán số.

---

# Vì sao nên học NumPy?

NumPy quan trọng vì nó cung cấp nền tảng hiệu quả cho các bài toán tính toán số trong Python.

## Ưu điểm chính

- Thực hiện các phép toán vector hóa nhanh hơn đáng kể so với vòng lặp Python trong nhiều bài toán số.
- Lưu trữ dữ liệu số đồng nhất gọn hơn danh sách Python.
- Cung cấp các hàm tối ưu cho đại số tuyến tính và thao tác ma trận.
- Hỗ trợ sinh số ngẫu nhiên và phân tích thống kê.
- Biểu diễn các công thức phức tạp bằng cú pháp ngắn gọn.
- Là nền tảng số học cho nhiều thư viện khoa học dữ liệu.

## So sánh mảng NumPy và danh sách Python

Danh sách Python có thể chứa nhiều kiểu dữ liệu khác nhau:

```python
values = [10, 2.5, "Python", True]
```

Mảng NumPy thường lưu trữ các phần tử có cùng kiểu dữ liệu:

```python
import numpy as np

values = np.array([10, 20, 30, 40])
```

Nhờ cấu trúc đồng nhất, NumPy có thể thực hiện các phép toán số hiệu quả hơn.

### Ví dụ: Nhân toàn bộ phần tử

Sử dụng danh sách Python:

```python
values = [1, 2, 3, 4]

result = []

for value in values:
    result.append(value * 10)

print(result)
```

Kết quả:

```text
[10, 20, 30, 40]
```

Sử dụng NumPy:

```python
import numpy as np

values = np.array([1, 2, 3, 4])

result = values * 10

print(result)
```

Kết quả:

```text
[10 20 30 40]
```

### Câu hỏi nhanh

**Câu 1.** Vì sao mảng NumPy hiệu quả trong tính toán số?

A. Vì luôn chứa dữ liệu văn bản  
B. Vì sử dụng cấu trúc mảng đồng nhất và được tối ưu  
C. Vì không sử dụng bộ nhớ  
D. Vì tự động kết nối Internet  

**Câu 2.** Biểu thức nào nhân mọi phần tử của mảng `a` với 10?

A. `a * 10`  
B. `a.append(10)`  
C. `a.add("10")`  
D. `a.sort(10)`  

---

# Cài đặt và nhập NumPy

## Cài đặt

Có thể cài NumPy bằng lệnh:

```bash
pip install numpy
```

Trong nhiều môi trường khoa học dữ liệu, NumPy có thể đã được cài sẵn.

## Nhập thư viện

Quy ước phổ biến là:

```python
import numpy as np
```

Bí danh `np` được sử dụng rộng rãi trong mã nguồn và tài liệu NumPy.

## Kiểm tra phiên bản

```python
import numpy as np

print(np.__version__)
```

### Câu hỏi nhanh

**Câu 1.** Bí danh thông dụng của NumPy là gì?

A. `ny`  
B. `np`  
C. `num`  
D. `py`  

**Câu 2.** Lệnh nào dùng để cài NumPy?

A. `pip install numpy`  
B. `python import numpy`  
C. `install numpy.py`  
D. `pip numpy open`  

---

# Mảng NumPy

Mảng NumPy có thể được tạo từ danh sách, tuple, dãy số hoặc các hàm dựng sẵn.

## Tạo mảng từ danh sách

```python
import numpy as np

a = [9, 3, 3, 5]

arr = np.array(a)

print(arr)
```

Kết quả:

```text
[9 3 3 5]
```

## Tạo mảng một chiều

```python
arr = np.array([10, 20, 30, 40])

print(arr)
```

## Tạo mảng hai chiều

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
```

Kết quả:

```text
[[1 2 3]
 [4 5 6]]
```

## Tạo mảng ba chiều

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

### Câu hỏi nhanh

**Câu 1.** Hàm nào chuyển danh sách Python thành mảng NumPy?

A. `np.array()`  
B. `np.list()`  
C. `np.convert()`  
D. `np.ndarray_list()`  

**Câu 2.** Mảng hai chiều thường được dùng để biểu diễn:

A. Ma trận  
B. Chuỗi ký tự  
C. Đường dẫn tệp  
D. Điều kiện Boolean  

---

# Các hàm tạo mảng thông dụng

## Mảng toàn số 0

```python
zeros = np.zeros(5)

print(zeros)
```

Kết quả:

```text
[0. 0. 0. 0. 0.]
```

Tạo ma trận số 0:

```python
zeros_matrix = np.zeros((2, 3))

print(zeros_matrix)
```

## Mảng toàn số 1

```python
ones = np.ones((2, 3))

print(ones)
```

## Mảng chứa một giá trị cố định

```python
filled = np.full((2, 3), 7)

print(filled)
```

## Tạo dãy bằng `arange()`

```python
values = np.arange(0, 10, 2)

print(values)
```

Kết quả:

```text
[0 2 4 6 8]
```

## Tạo các giá trị cách đều bằng `linspace()`

```python
values = np.linspace(0, 1, 5)

print(values)
```

Kết quả:

```text
[0.   0.25 0.5  0.75 1.  ]
```

## Tạo ma trận đơn vị

```python
identity = np.eye(3)

print(identity)
```

Kết quả:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### Câu hỏi nhanh

**Câu 1.** Hàm nào tạo mảng toàn số 0?

A. `np.zeros()`  
B. `np.empty_text()`  
C. `np.null()`  
D. `np.zero_array_only()`  

**Câu 2.** Hàm nào tạo các giá trị cách đều giữa hai đầu mút?

A. `np.linspace()`  
B. `np.stack()`  
C. `np.split()`  
D. `np.mean()`  

---

# Thuộc tính của mảng

Xét mảng:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## Số chiều

```python
print(arr.ndim)
```

Kết quả:

```text
2
```

## Hình dạng

```python
print(arr.shape)
```

Kết quả:

```text
(2, 3)
```

Mảng có hai hàng và ba cột.

## Tổng số phần tử

```python
print(arr.size)
```

Kết quả:

```text
6
```

## Kiểu dữ liệu

```python
print(arr.dtype)
```

Kết quả cụ thể phụ thuộc vào nền tảng và các giá trị trong mảng.

## Số byte cho mỗi phần tử

```python
print(arr.itemsize)
```

### Bảng tóm tắt

| Thuộc tính | Ý nghĩa |
|---|---|
| `ndim` | Số chiều |
| `shape` | Kích thước theo từng chiều |
| `size` | Tổng số phần tử |
| `dtype` | Kiểu dữ liệu |
| `itemsize` | Số byte của mỗi phần tử |

### Câu hỏi nhanh

**Câu 1.** Thuộc tính nào trả về hình dạng của mảng?

A. `shape`  
B. `mean`  
C. `append`  
D. `index`  

**Câu 2.** Thuộc tính nào trả về tổng số phần tử?

A. `size`  
B. `dtype`  
C. `ndim`  
D. `itemsize`  

---

# Indexing trong mảng

Indexing được dùng để truy cập từng phần tử.

## Indexing mảng một chiều

```python
arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[2])
```

Kết quả:

```text
10
30
```

Chỉ số âm truy cập từ cuối mảng:

```python
print(arr[-1])
```

Kết quả:

```text
40
```

## Indexing mảng hai chiều

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix[0, 1])
print(matrix[1, 2])
```

Kết quả:

```text
2
6
```

### Câu hỏi nhanh

**Câu 1.** `arr[0]` trả về gì?

A. Phần tử đầu tiên  
B. Phần tử cuối cùng  
C. Hình dạng của mảng  
D. Kích thước mảng  

**Câu 2.** Trong mảng hai chiều, `matrix[1, 2]` chỉ:

A. Hàng chỉ số 1 và cột chỉ số 2  
B. Chỉ hàng 1  
C. Chỉ cột 2  
D. Số chiều của mảng  

---

# Slicing trong mảng

Slicing dùng để trích một phần của mảng.

## Slicing mảng một chiều

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
```

Kết quả:

```text
[20 30 40]
```

## Slicing với bước nhảy

```python
print(arr[::2])
```

Kết quả:

```text
[10 30 50]
```

## Slicing mảng hai chiều

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0:2, 1:3])
```

Kết quả:

```text
[[2 3]
 [5 6]]
```

## Lưu ý: view và copy

Nhiều phép slicing trong NumPy trả về một **view** của mảng gốc thay vì tạo bản sao độc lập. Vì vậy, thay đổi view có thể làm thay đổi dữ liệu gốc.

```python
arr = np.array([10, 20, 30, 40])

view = arr[1:3]
view[0] = 999

print(arr)
```

Kết quả:

```text
[ 10 999  30  40]
```

Tạo bản sao độc lập bằng:

```python
copy = arr[1:3].copy()
```

### Câu hỏi nhanh

**Câu 1.** `arr[1:4]` chứa các phần tử nào?

A. Các phần tử tại chỉ số 1, 2 và 3  
B. Các phần tử từ chỉ số 1 đến 4, gồm cả 4  
C. Chỉ phần tử tại chỉ số 4  
D. Mọi phần tử cách một vị trí  

**Câu 2. Đúng hay sai?** Một lát cắt NumPy có thể dùng chung bộ nhớ với mảng gốc.

---

# Thay đổi hình dạng mảng

`reshape()` thay đổi hình dạng mà không thay đổi dữ liệu.

```python
arr = np.arange(12)

matrix = arr.reshape(3, 4)

print(matrix)
```

Kết quả:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

## Dùng `-1` để NumPy tự suy ra một chiều

```python
matrix = arr.reshape(2, -1)

print(matrix)
```

NumPy tự tính kích thước còn thiếu.

## Làm phẳng mảng

```python
flat = matrix.flatten()

print(flat)
```

## Dùng `ravel()`

```python
flat_view = matrix.ravel()

print(flat_view)
```

`flatten()` trả về bản sao, trong khi `ravel()` thường trả về view khi có thể.

### Câu hỏi nhanh

**Câu 1.** Phương thức nào thay đổi hình dạng của mảng?

A. `reshape()`  
B. `mean()`  
C. `split()`  
D. `sort_index()`  

**Câu 2.** `-1` trong `reshape()` có ý nghĩa gì?

A. NumPy tự suy ra chiều đó  
B. Xóa một chiều  
C. Đảo ngược mảng  
D. Chuyển các giá trị thành số âm  

---

# Thay đổi kích thước mảng

`resize()` có thể thay đổi hình dạng và số lượng phần tử.

```python
arr = np.array([1, 2, 3, 4])

resized = np.resize(arr, (2, 3))

print(resized)
```

Kết quả:

```text
[[1 2 3]
 [4 1 2]]
```

Khi mảng mới lớn hơn, các giá trị có thể được lặp lại.

> **Lưu ý:** `reshape()` yêu cầu tổng số phần tử tương thích. `resize()` có thể tạo ra kích thước tổng khác.

### Câu hỏi nhanh

**Câu 1.** Phép toán nào thông thường giữ nguyên tổng số phần tử?

A. `reshape()`  
B. `np.resize()` trong mọi trường hợp  
C. `np.delete()`  
D. `np.append()`  

---

# Ghép mảng

Ghép mảng kết hợp nhiều mảng thành một mảng lớn hơn.

## Ghép theo chiều dọc

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))

print(result)
```

Kết quả:

```text
[[1 2 3]
 [4 5 6]]
```

## Ghép theo chiều ngang

```python
result = np.hstack((a, b))

print(result)
```

Kết quả:

```text
[1 2 3 4 5 6]
```

## Ghép tổng quát

```python
result = np.stack((a, b), axis=0)

print(result)
```

### Câu hỏi nhanh

**Câu 1.** Hàm nào ghép các mảng theo chiều dọc?

A. `np.vstack()`  
B. `np.mean()`  
C. `np.split()`  
D. `np.random()`  

---

# Tách mảng

Tách mảng chia một mảng thành nhiều mảng nhỏ.

```python
arr = np.array([1, 2, 3, 4, 5, 6])

parts = np.split(arr, 3)

print(parts)
```

Kết quả:

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

## Tách theo chiều ngang và chiều dọc

```python
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

left, right = np.hsplit(matrix, 2)

print(left)
print(right)
```

### Câu hỏi nhanh

**Câu 1.** Hàm nào chia một mảng thành các phần bằng nhau?

A. `np.split()`  
B. `np.join()`  
C. `np.mean()`  
D. `np.dot()`  

---

# Broadcasting

Broadcasting cho phép NumPy thực hiện phép toán giữa các mảng có hình dạng khác nhau nhưng tương thích.

## Broadcasting với số vô hướng

```python
arr = np.array([1, 2, 3, 4])

result = arr + 10

print(result)
```

Kết quả:

```text
[11 12 13 14]
```

Số `10` được áp dụng cho từng phần tử.

## Broadcasting giữa các mảng

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([10, 20, 30])

result = matrix + row

print(result)
```

Kết quả:

```text
[[11 22 33]
 [14 25 36]]
```

## Quy tắc broadcasting cơ bản

So sánh các chiều từ phải sang trái. Hai chiều tương thích khi:

- Chúng bằng nhau; hoặc
- Một trong hai chiều bằng `1`.

Nếu hình dạng không tương thích, NumPy phát sinh lỗi.

### Ví dụ hình dạng không tương thích

```python
a = np.ones((2, 3))
b = np.ones((2, 2))

# a + b phát sinh lỗi broadcasting
```

### Câu hỏi nhanh

**Câu 1.** Broadcasting cho phép điều gì?

A. Thực hiện phép toán giữa các mảng có hình dạng tương thích  
B. Truyền dữ liệu tự động qua Internet  
C. Chuyển mảng thành tệp  
D. Xóa mọi chiều của mảng  

**Câu 2.** Hai chiều tương thích khi bằng nhau hoặc:

A. Một trong hai bằng 1  
B. Cả hai đều âm  
C. Cả hai đều là văn bản  
D. Tổng của chúng bằng 0  

---

# Các phép toán số học cơ bản

NumPy hỗ trợ phép toán theo từng phần tử.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

## Cộng

```python
print(a + b)
```

Kết quả:

```text
[5 7 9]
```

## Trừ

```python
print(a - b)
```

Kết quả:

```text
[-3 -3 -3]
```

## Nhân theo từng phần tử

```python
print(a * b)
```

Kết quả:

```text
[ 4 10 18]
```

## Chia

```python
print(a / b)
```

## Lũy thừa

```python
print(a ** 2)
```

Kết quả:

```text
[1 4 9]
```

## Chia lấy dư

```python
print(b % a)
```

### Phân biệt quan trọng

Toán tử `*` thực hiện **nhân theo từng phần tử**, không phải nhân ma trận.

### Câu hỏi nhanh

**Câu 1.** `a * b` thực hiện gì với hai mảng cùng hình dạng?

A. Nhân theo từng phần tử  
B. Nghịch đảo ma trận  
C. Sắp xếp  
D. Ghép mảng  

---

# Các hàm tổng hợp

Các hàm tổng hợp tóm tắt giá trị trong mảng.

```python
arr = np.array([9, 3, 3, 5])
```

## Tổng

```python
print(arr.sum())
```

Kết quả:

```text
20
```

## Trung bình

```python
print(arr.mean())
```

Kết quả:

```text
5.0
```

## Giá trị nhỏ nhất và lớn nhất

```python
print(arr.min())
print(arr.max())
```

## Trung vị

```python
print(np.median(arr))
```

## Phương sai và độ lệch chuẩn

```python
print(np.var(arr))
print(np.std(arr))
```

## Tổng hợp theo trục

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix.sum(axis=0))
print(matrix.sum(axis=1))
```

Kết quả:

```text
[5 7 9]
[ 6 15]
```

- `axis=0`: tổng hợp theo chiều dọc, tạo một giá trị cho mỗi cột.
- `axis=1`: tổng hợp theo chiều ngang, tạo một giá trị cho mỗi hàng.

### Câu hỏi nhanh

**Câu 1.** Hàm nào tính trung bình số học?

A. `np.mean()`  
B. `np.stack()`  
C. `np.dot()`  
D. `np.reshape()`  

**Câu 2.** Trong mảng hai chiều, `axis=0` thường có ý nghĩa gì?

A. Tổng hợp theo các hàng để tạo kết quả theo cột  
B. Tổng hợp theo các cột để tạo kết quả theo hàng  
C. Tổng hợp tên tệp  
D. Tổng hợp kiểu dữ liệu  

---

# Universal Functions

**Universal function**, thường viết là **ufunc**, thực hiện phép toán theo từng phần tử trên mảng.

## Căn bậc hai

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
```

Kết quả:

```text
[1. 2. 3. 4.]
```

## Hàm mũ

```python
print(np.exp(np.array([0, 1, 2])))
```

## Logarit tự nhiên

```python
values = np.array([1, np.e, np.e**2])

print(np.log(values))
```

## Hàm lượng giác

```python
angles = np.array([0, np.pi / 2, np.pi])

print(np.sin(angles))
```

## Giá trị tuyệt đối

```python
values = np.array([-3, -1, 2, 4])

print(np.abs(values))
```

## Làm tròn

```python
values = np.array([1.234, 5.678])

print(np.round(values, 2))
```

### Câu hỏi nhanh

**Câu 1.** Hàm nào tính căn bậc hai theo từng phần tử?

A. `np.sqrt()`  
B. `np.split()`  
C. `np.stack()`  
D. `np.size()`  

---

# Phép so sánh và Boolean

NumPy hỗ trợ so sánh theo từng phần tử.

```python
arr = np.array([10, 20, 30, 40])

print(arr > 20)
```

Kết quả:

```text
[False False  True  True]
```

## Lọc bằng Boolean

```python
selected = arr[arr > 20]

print(selected)
```

Kết quả:

```text
[30 40]
```

## Kết hợp nhiều điều kiện

```python
selected = arr[(arr >= 20) & (arr <= 30)]

print(selected)
```

Kết quả:

```text
[20 30]
```

Sử dụng:

- `&` cho AND theo từng phần tử.
- `|` cho OR theo từng phần tử.
- `~` cho NOT theo từng phần tử.

### Câu hỏi nhanh

**Câu 1.** `arr[arr > 20]` trả về gì?

A. Các phần tử lớn hơn 20  
B. Kích thước mảng  
C. Kiểu dữ liệu của mảng  
D. Toàn bộ phần tử được chuyển thành Boolean  

---

# Đại số tuyến tính

NumPy cung cấp các hàm đại số tuyến tính thông qua `numpy.linalg` và các toán tử ma trận.

## Nhân ma trận

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

result = np.dot(A, A)

print(result)
```

Kết quả:

```text
[[ 7 10]
 [15 22]]
```

Có thể dùng toán tử `@`:

```python
result = A @ A

print(result)
```

## Nhân theo từng phần tử và nhân ma trận

```python
print(A * A)
print(A @ A)
```

- `A * A`: nhân theo từng phần tử.
- `A @ A`: nhân ma trận.

## Chuyển vị ma trận

```python
print(A.T)
```

## Định thức

```python
determinant = np.linalg.det(A)

print(determinant)
```

## Ma trận nghịch đảo

```python
inverse = np.linalg.inv(A)

print(inverse)
```

Ma trận nghịch đảo chỉ tồn tại với ma trận vuông không suy biến.

## Giải hệ phương trình tuyến tính

Với hệ \(Ax=b\):

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])

x = np.linalg.solve(A, b)

print(x)
```

## Trị riêng và vector riêng

```python
eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)
print(eigenvectors)
```

## Tích trong

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.inner(a, b))
```

## Tích ngoài

```python
print(np.outer(a, b))
```

## `dot()` và `vdot()`

```python
print(np.dot(a, b))
print(np.vdot(a, b))
```

Với mảng một chiều thực, hai kết quả thường giống nhau. `vdot()` còn xử lý liên hợp phức.

### Câu hỏi nhanh

**Câu 1.** Toán tử nào thực hiện nhân ma trận?

A. `@`  
B. `%`  
C. `//`  
D. `&`  

**Câu 2.** Hàm nào tính ma trận nghịch đảo?

A. `np.linalg.inv()`  
B. `np.mean()`  
C. `np.resize()`  
D. `np.random()`  

---

# Sinh số ngẫu nhiên

NumPy cung cấp công cụ sinh dữ liệu ngẫu nhiên phục vụ mô phỏng, thí nghiệm thống kê và học máy.

Trong mã nguồn mới, nên sử dụng đối tượng bộ sinh số ngẫu nhiên:

```python
import numpy as np

rng = np.random.default_rng()
```

> **Lưu ý:** Bộ sinh số ngẫu nhiên của NumPy phù hợp cho tính toán và mô phỏng, không nên xem là bộ sinh số an toàn cho mật mã.

## Sinh số nguyên ngẫu nhiên

```python
rng = np.random.default_rng(42)

values = rng.integers(
    low=1,
    high=10,
    size=5
)

print(values)
```

## Phân phối đều

```python
values = rng.uniform(
    low=0,
    high=1,
    size=5
)

print(values)
```

## Phân phối chuẩn

```python
values = rng.normal(
    loc=0,
    scale=1,
    size=5
)

print(values)
```

## Phân phối nhị thức

```python
values = rng.binomial(
    n=10,
    p=0.5,
    size=5
)

print(values)
```

## Phân phối Poisson

```python
values = rng.poisson(
    lam=3,
    size=5
)

print(values)
```

## Phân phối mũ

```python
values = rng.exponential(
    scale=2,
    size=5
)

print(values)
```

## Phân phối Chi-square

```python
values = rng.chisquare(
    df=4,
    size=5
)

print(values)
```

## Tái lập kết quả bằng seed

```python
rng = np.random.default_rng(42)
```

Dùng cùng một seed giúp tái tạo cùng chuỗi giả ngẫu nhiên trong môi trường tương thích.

### Ví dụ

```python
import numpy as np

rng = np.random.default_rng(42)

a = rng.normal(0, 1, 5)

print("Data:", a)
print("Mean:", np.mean(a))
```

Giá trị cụ thể phụ thuộc bộ sinh và phiên bản NumPy, nhưng seed cố định hỗ trợ khả năng tái lập.

### Câu hỏi nhanh

**Câu 1.** Phương thức nào tạo bộ sinh số ngẫu nhiên theo cách hiện đại?

A. `np.random.default_rng()`  
B. `np.random.file()`  
C. `np.create_random_array()`  
D. `np.random.text()`  

**Câu 2.** Seed có ích vì sao?

A. Giúp tái tạo một chuỗi giả ngẫu nhiên  
B. Làm giá trị trở nên hoàn toàn không thể đoán  
C. Xóa toàn bộ số ngẫu nhiên  
D. Chuyển dữ liệu thành chuỗi  

---

# Các hàm thống kê

NumPy hỗ trợ nhiều thống kê mô tả.

```python
data = np.array([12, 15, 18, 20, 25])
```

## Trung bình

```python
print(np.mean(data))
```

## Trung vị

```python
print(np.median(data))
```

## Phương sai

```python
print(np.var(data))
```

## Độ lệch chuẩn

```python
print(np.std(data))
```

## Phân vị phần trăm

```python
print(np.percentile(data, 25))
print(np.percentile(data, 50))
print(np.percentile(data, 75))
```

## Quantile

```python
print(np.quantile(data, 0.25))
print(np.quantile(data, 0.50))
print(np.quantile(data, 0.75))
```

## Khoảng biến thiên

```python
data_range = np.max(data) - np.min(data)

print(data_range)
```

### Quy ước tổng thể và mẫu

Theo mặc định, `np.var()` và `np.std()` dùng `ddof=0`, tương ứng chia cho \(N\).

Để dùng quy ước mẫu chia cho \(N-1\):

```python
sample_variance = np.var(data, ddof=1)
sample_std = np.std(data, ddof=1)

print(sample_variance)
print(sample_std)
```

### Câu hỏi nhanh

**Câu 1.** Tham số nào dùng cho độ lệch chuẩn mẫu thông dụng?

A. `ddof=1`  
B. `axis=-100`  
C. `dtype="sample"`  
D. `copy=False`  

---

# Dữ liệu thiếu và giá trị không hợp lệ

NumPy thường biểu diễn dữ liệu số bị thiếu bằng `np.nan`.

```python
data = np.array([10.0, 20.0, np.nan, 40.0])

print(data)
```

## Tính trung bình thông thường

```python
print(np.mean(data))
```

Kết quả là `nan` vì mảng có giá trị thiếu.

## Bỏ qua `NaN`

```python
print(np.nanmean(data))
print(np.nanmedian(data))
print(np.nanstd(data))
```

## Phát hiện giá trị thiếu

```python
print(np.isnan(data))
```

## Loại bỏ giá trị thiếu

```python
clean_data = data[~np.isnan(data)]

print(clean_data)
```

> **Lưu ý:** NumPy chỉ cung cấp hỗ trợ cơ bản cho dữ liệu thiếu. Các quy trình xử lý dữ liệu thiếu đầy đủ thường được thực hiện bằng Pandas.

### Câu hỏi nhanh

**Câu 1.** Hàm nào tính trung bình và bỏ qua `NaN`?

A. `np.nanmean()`  
B. `np.mean_text()`  
C. `np.ignore()`  
D. `np.dropna()`  

---

# Phép toán vector hóa

Vector hóa áp dụng một phép toán lên toàn bộ mảng cùng lúc.

```python
import numpy as np

a = np.arange(5)

result = a * 10

print(result)
```

Kết quả:

```text
[ 0 10 20 30 40]
```

Nếu không dùng NumPy, có thể phải viết vòng lặp:

```python
a = list(range(5))

result = []

for value in a:
    result.append(value * 10)

print(result)
```

Mã vector hóa thường:

- Ngắn gọn hơn.
- Dễ đọc hơn.
- Nhanh hơn với mảng số lớn.
- Phù hợp với phân tích dữ liệu và tính toán khoa học.

## Điều kiện vector hóa

```python
arr = np.array([10, 20, 30, 40])

labels = np.where(
    arr >= 30,
    "high",
    "low"
)

print(labels)
```

Kết quả:

```text
['low' 'low' 'high' 'high']
```

### Câu hỏi nhanh

**Câu 1.** Ưu điểm quan trọng của vector hóa là gì?

A. Thực hiện phép toán trên mảng mà không cần vòng lặp Python tường minh  
B. Chuyển mọi mảng thành văn bản  
C. Loại bỏ nhu cầu sử dụng bộ nhớ  
D. Ngăn chặn mọi lỗi  

---

# Quản lý bộ nhớ

Mảng NumPy hiệu quả vì thường lưu trữ các giá trị đồng nhất theo bố cục bộ nhớ đều đặn.

## Kiểm tra lượng bộ nhớ

```python
arr = np.array([1, 2, 3, 4], dtype=np.int32)

print(arr.nbytes)
```

`nbytes` trả về tổng số byte dùng để lưu các phần tử.

## Chọn kiểu dữ liệu phù hợp

```python
small_values = np.array(
    [1, 2, 3, 4],
    dtype=np.int8
)

print(small_values.dtype)
print(small_values.nbytes)
```

Kiểu dữ liệu nhỏ có thể tiết kiệm bộ nhớ, nhưng phải đủ phạm vi và độ chính xác.

## Chuyển đổi kiểu dữ liệu

```python
arr = np.array([1.2, 2.8, 3.5])

integers = arr.astype(np.int32)

print(integers)
```

Kết quả:

```text
[1 2 3]
```

Chuyển từ số thực sang số nguyên làm mất phần thập phân.

### Câu hỏi nhanh

**Câu 1.** Thuộc tính nào trả về số byte dùng để lưu các phần tử?

A. `nbytes`  
B. `ndim`  
C. `mean`  
D. `shape`  

---

# Sắp xếp và tìm kiếm

## Sắp xếp mảng

```python
arr = np.array([9, 3, 7, 1])

sorted_arr = np.sort(arr)

print(sorted_arr)
```

Kết quả:

```text
[1 3 7 9]
```

## Tìm chỉ số thỏa điều kiện

```python
arr = np.array([10, 20, 30, 40])

indices = np.where(arr > 20)

print(indices)
```

## Tìm giá trị duy nhất

```python
arr = np.array([1, 2, 2, 3, 3, 3])

values, counts = np.unique(
    arr,
    return_counts=True
)

print(values)
print(counts)
```

### Câu hỏi nhanh

**Câu 1.** Hàm nào trả về các giá trị duy nhất?

A. `np.unique()`  
B. `np.reshape()`  
C. `np.random()`  
D. `np.outer()`  

---

# Ma trận thưa

Ma trận thưa là ma trận có phần lớn phần tử bằng 0.

NumPy có thể biểu diễn ma trận thưa dưới dạng mảng đặc:

```python
matrix = np.array([
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 0]
])
```

Tuy nhiên, ma trận thưa lớn thường được lưu hiệu quả hơn bằng các cấu trúc chuyên dụng của SciPy.

```python
from scipy.sparse import csr_matrix

sparse_matrix = csr_matrix(matrix)

print(sparse_matrix)
```

NumPy vẫn đóng vai trò quan trọng vì các ma trận thưa của SciPy tương tác trực tiếp với mảng NumPy.

### Câu hỏi nhanh

**Câu 1.** Thư viện nào thường cung cấp cấu trúc ma trận thưa chuyên dụng?

A. SciPy  
B. pathlib  
C. tkinter  
D. Flask  

---

# Làm việc với ảnh

Ảnh số có thể được biểu diễn bằng mảng NumPy.

- Ảnh xám có thể là mảng hai chiều.
- Ảnh màu có thể là mảng ba chiều gồm chiều cao, chiều rộng và kênh màu.

## Ví dụ đơn giản

```python
image = np.array([
    [0, 128, 255],
    [255, 128, 0],
    [50, 100, 150]
])

print(image.shape)
```

Kết quả:

```text
(3, 3)
```

## Tăng độ sáng

```python
brighter = np.clip(
    image + 30,
    0,
    255
)

print(brighter)
```

`np.clip()` giữ các giá trị trong khoảng hợp lệ.

### Câu hỏi nhanh

**Câu 1.** Ảnh xám thường được biểu diễn dưới dạng:

A. Mảng số hai chiều  
B. Chỉ một dictionary  
C. Chỉ một tệp văn bản  
D. Một giá trị Boolean  

---

# Tích hợp với Pandas

Một `Series` hoặc `DataFrame` của Pandas có thể trao đổi dữ liệu với NumPy.

## Chuyển mảng NumPy thành DataFrame

```python
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

print(df)
```

## Chuyển DataFrame thành mảng NumPy

```python
array_from_df = df.to_numpy()

print(array_from_df)
```

## Áp dụng hàm NumPy lên cột Pandas

```python
df["A_sqrt"] = np.sqrt(df["A"])

print(df)
```

### Câu hỏi nhanh

**Câu 1.** Phương thức nào của Pandas chuyển DataFrame thành mảng NumPy?

A. `to_numpy()`  
B. `to_list_only()`  
C. `as_matrix_text()`  
D. `convert_numpy_file()`  

---

# Tích hợp với Scikit-learn

Nhiều mô hình Scikit-learn nhận mảng NumPy làm đầu vào.

```python
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

print(prediction)
```

NumPy hỗ trợ:

- Ma trận đặc trưng.
- Vector mục tiêu.
- Kết quả dự báo.
- Tiền xử lý số.
- Tính toán chỉ số đánh giá.

### Câu hỏi nhanh

**Câu 1.** Trong học máy, mảng NumPy hai chiều thường biểu diễn:

A. Ma trận đặc trưng  
B. Tên tệp  
C. Tiêu đề biểu đồ  
D. Trình cài đặt gói  

---

# Các lỗi NumPy thường gặp

## Không khớp hình dạng

```python
a = np.ones((2, 3))
b = np.ones((2, 2))

# a + b phát sinh lỗi
```

Hai hình dạng không tương thích với broadcasting.

## `reshape()` không hợp lệ

```python
arr = np.arange(10)

# arr.reshape(3, 4) phát sinh lỗi
```

Mười phần tử không thể chuyển thành mảng `3 × 4`.

## Chia cho 0

```python
arr = np.array([1.0, 0.0])

print(1 / arr)
```

Kết quả có thể chứa `inf` và cảnh báo runtime.

## Tràn số nguyên

Kiểu số nguyên nhỏ có phạm vi giới hạn:

```python
arr = np.array([127], dtype=np.int8)

print(arr + 1)
```

Kết quả có thể bị tràn vì `int8` không biểu diễn được giá trị lớn hơn 127.

## Thay đổi ngoài ý muốn do view

Một lát cắt có thể dùng chung bộ nhớ với mảng gốc. Hãy dùng `.copy()` khi cần mảng độc lập.

### Câu hỏi nhanh

**Câu 1.** Vì sao `np.arange(10).reshape(3, 4)` phát sinh lỗi?

A. Tổng số phần tử không tương thích  
B. NumPy không thể tạo ma trận  
C. `reshape()` chỉ dùng cho chuỗi  
D. Các giá trị phải là số âm  

---

# Thực hành tốt khi sử dụng NumPy

- Nhập NumPy bằng `import numpy as np`.
- Ưu tiên phép toán vector hóa thay cho vòng lặp Python khi phù hợp.
- Kiểm tra `shape`, `ndim` và `dtype` trước các phép toán phức tạp.
- Chỉ dùng broadcasting khi hiểu rõ hành vi về hình dạng.
- Phân biệt nhân theo từng phần tử và nhân ma trận.
- Dùng `.copy()` khi cần mảng độc lập.
- Chọn kiểu dữ liệu phù hợp với phạm vi, độ chính xác và bộ nhớ.
- Dùng seed cố định khi cần tái lập kết quả.
- Xử lý rõ ràng `NaN`, vô cùng và tràn số.
- Dùng Pandas cho dữ liệu bảng có nhãn và quy trình xử lý thiếu phức tạp.
- Dùng SciPy cho thuật toán khoa học chuyên sâu và ma trận thưa.

---

# Tóm tắt nội dung

| Nội dung | Ý chính |
|---|---|
| **NumPy** | Thư viện cốt lõi cho tính toán số |
| **`ndarray`** | Mảng đồng nhất N chiều |
| **Vector hóa** | Tính toán trên mảng không cần vòng lặp Python tường minh |
| **Broadcasting** | Phép toán giữa các hình dạng tương thích |
| **Indexing và slicing** | Truy cập và trích phần tử |
| **Reshaping** | Thay đổi hình dạng mảng |
| **Aggregation** | Tổng, trung bình, nhỏ nhất, lớn nhất |
| **Universal functions** | Hàm toán học theo từng phần tử |
| **Đại số tuyến tính** | Nhân ma trận, nghịch đảo, định thức và trị riêng |
| **Sinh số ngẫu nhiên** | Sinh dữ liệu từ các phân phối xác suất |
| **Thống kê** | Trung bình, trung vị, phương sai, độ lệch chuẩn và phân vị |
| **Tích hợp** | Làm việc với Pandas, SciPy và Scikit-learn |

---

# Câu hỏi ôn tập cuối bài

## Phần A. Câu hỏi trắc nghiệm

**Câu 1.** NumPy chủ yếu được sử dụng cho:

A. Tính toán số  
B. Thiết kế trang web  
C. Gửi email  
D. Soạn thảo văn bản  

**Câu 2.** Cấu trúc dữ liệu trung tâm của NumPy là:

A. `ndarray`  
B. `DataFrame`  
C. `set`  
D. `class`  

**Câu 3.** Hàm nào tạo mảng từ danh sách Python?

A. `np.array()`  
B. `np.list()`  
C. `np.frame()`  
D. `np.convert_list()`  

**Câu 4.** Thuộc tính nào trả về hình dạng của mảng?

A. `shape`  
B. `size()`  
C. `mean`  
D. `type()`  

**Câu 5.** Biểu thức nào thực hiện nhân ma trận?

A. `A @ B`  
B. `A % B`  
C. `A // B`  
D. `A | B`  

**Câu 6.** Hàm nào tính trung bình và bỏ qua `NaN`?

A. `np.nanmean()`  
B. `np.mean_without_missing()`  
C. `np.dropna()`  
D. `np.ignore_mean()`  

**Câu 7.** Hàm nào tạo ma trận đơn vị?

A. `np.eye()`  
B. `np.identity_text()`  
C. `np.ones_like_text()`  
D. `np.reshape()`  

**Câu 8.** Phát biểu nào đúng về broadcasting?

A. Hỗ trợ phép toán giữa các hình dạng tương thích  
B. Chuyển mọi mảng thành một chiều  
C. Xóa mọi giá trị trùng lặp  
D. Luôn thay đổi mảng gốc  

**Câu 9.** Trong phép tổng hợp mảng hai chiều, `axis=0` thường có nghĩa là:

A. Tổng hợp theo hàng và trả kết quả theo cột  
B. Tổng hợp theo cột và trả kết quả theo hàng  
C. Chuyển ma trận thành một số duy nhất  
D. Đảo ngược mọi giá trị  

**Câu 10.** Đối tượng nào được khuyến nghị để sinh số ngẫu nhiên trong NumPy hiện đại?

A. `np.random.default_rng()`  
B. `np.random.file_reader()`  
C. `np.random.secure_password()`  
D. `np.array.randomize_text()`  

## Phần B. Câu hỏi đúng/sai

**Câu 1.** Mảng NumPy thường chứa các phần tử có cùng kiểu dữ liệu.

**Câu 2.** Phép toán vector hóa luôn cần vòng lặp Python tường minh.

**Câu 3.** `A * B` và `A @ B` luôn thực hiện cùng một phép toán.

**Câu 4.** Lát cắt NumPy có thể dùng chung bộ nhớ với mảng gốc.

**Câu 5.** Broadcasting yêu cầu các chiều của mảng phải tương thích.

**Câu 6.** `np.std(data, ddof=1)` có thể dùng cho quy ước độ lệch chuẩn mẫu thông dụng.

**Câu 7.** Bộ sinh số ngẫu nhiên NumPy có thể được xem là an toàn cho mật mã.

**Câu 8.** Mảng NumPy có thể làm đầu vào cho mô hình Scikit-learn.

## Phần C. Câu hỏi tự luận

**Câu 1.** Trình bày hai điểm khác nhau giữa danh sách Python và mảng NumPy.

**Câu 2.** Giải thích vector hóa và nêu một ưu điểm.

**Câu 3.** Phân biệt nhân theo từng phần tử và nhân ma trận.

**Câu 4.** Trình bày quy tắc tương thích broadcasting cơ bản.

**Câu 5.** Phân biệt view và copy.

**Câu 6.** Nêu bốn hàm thống kê trong NumPy.

## Phần D. Bài tập thực hành

### Bài 1. Tạo mảng

1. Tạo mảng chứa các giá trị từ 1 đến 20.
2. Chuyển mảng thành ma trận `4 × 5`.
3. In hình dạng, số chiều, số phần tử và kiểu dữ liệu.

### Bài 2. Indexing và slicing

Với một ma trận `4 × 5`:

1. Trích hàng đầu tiên.
2. Trích cột cuối cùng.
3. Trích vùng trung tâm `2 × 3`.
4. Chọn toàn bộ giá trị chẵn bằng lọc Boolean.

### Bài 3. Thống kê

Tạo mảng gồm mười giá trị số và tính:

1. Trung bình.
2. Trung vị.
3. Phương sai.
4. Độ lệch chuẩn mẫu.
5. Giá trị nhỏ nhất và lớn nhất.
6. Phân vị 25%, 50% và 75%.

### Bài 4. Broadcasting

1. Tạo ma trận `3 × 4`.
2. Tạo mảng một chiều gồm bốn giá trị.
3. Cộng mảng một chiều vào từng hàng của ma trận.
4. Giải thích vì sao broadcasting hợp lệ.

### Bài 5. Đại số tuyến tính

Cho:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])
```

1. Tính định thức của `A`.
2. Tính ma trận nghịch đảo của `A`.
3. Giải hệ \(Ax=b\).
4. Kiểm tra nghiệm bằng `A @ x`.

### Bài 6. Dữ liệu ngẫu nhiên

1. Tạo bộ sinh ngẫu nhiên với seed `42`.
2. Sinh 1.000 giá trị từ phân phối chuẩn tắc.
3. Tính trung bình và độ lệch chuẩn.
4. So sánh kết quả mẫu với giá trị lý thuyết.

### Bài 7. Dữ liệu thiếu

Cho:

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

1. Đếm số giá trị thiếu.
2. Tính trung bình và bỏ qua giá trị thiếu.
3. Loại bỏ mọi giá trị thiếu.
4. Thay giá trị thiếu bằng trung vị của các giá trị quan sát được.

---

# Đáp án và gợi ý trả lời

<details>
<summary><strong>Nhấn để hiển thị đáp án</strong></summary>

## Đáp án câu hỏi nhanh

### NumPy là gì?

1. B. `ndarray`.  
2. Đúng.

### Vì sao nên học NumPy?

1. B. Vì sử dụng cấu trúc mảng đồng nhất và được tối ưu.  
2. A. `a * 10`.

### Cài đặt và nhập thư viện

1. B. `np`.  
2. A. `pip install numpy`.

### Mảng NumPy

1. A. `np.array()`.  
2. A. Ma trận.

### Các hàm tạo mảng

1. A. `np.zeros()`.  
2. A. `np.linspace()`.

### Thuộc tính mảng

1. A. `shape`.  
2. A. `size`.

### Indexing

1. A. Phần tử đầu tiên.  
2. A. Hàng chỉ số 1 và cột chỉ số 2.

### Slicing

1. A. Các phần tử tại chỉ số 1, 2 và 3.  
2. Đúng.

### Reshaping

1. A. `reshape()`.  
2. A. NumPy tự suy ra chiều đó.

### Resizing

1. A. `reshape()`.

### Ghép mảng

1. A. `np.vstack()`.

### Tách mảng

1. A. `np.split()`.

### Broadcasting

1. A. Phép toán giữa các mảng có hình dạng tương thích.  
2. A. Một trong hai chiều bằng 1.

### Số học

1. A. Nhân theo từng phần tử.

### Tổng hợp

1. A. `np.mean()`.  
2. A. Tổng hợp theo hàng để tạo kết quả theo cột.

### Universal functions

1. A. `np.sqrt()`.

### Phép toán Boolean

1. A. Các phần tử lớn hơn 20.

### Đại số tuyến tính

1. A. `@`.  
2. A. `np.linalg.inv()`.

### Số ngẫu nhiên

1. A. `np.random.default_rng()`.  
2. A. Giúp tái tạo chuỗi giả ngẫu nhiên.

### Thống kê

1. A. `ddof=1`.

### Dữ liệu thiếu

1. A. `np.nanmean()`.

### Vector hóa

1. A. Thực hiện phép toán trên mảng mà không cần vòng lặp Python tường minh.

### Bộ nhớ

1. A. `nbytes`.

### Sắp xếp và tìm kiếm

1. A. `np.unique()`.

### Ma trận thưa

1. A. SciPy.

### Ảnh

1. A. Mảng số hai chiều.

### Tích hợp Pandas

1. A. `to_numpy()`.

### Tích hợp Scikit-learn

1. A. Ma trận đặc trưng.

### Lỗi thường gặp

1. A. Tổng số phần tử không tương thích.

## Đáp án phần A

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

## Đáp án phần B

1. Đúng.  
2. Sai.  
3. Sai.  
4. Đúng.  
5. Đúng.  
6. Đúng.  
7. Sai.  
8. Đúng.  

## Gợi ý phần C

### Câu 1

Mảng NumPy thường lưu trữ dữ liệu đồng nhất trong cấu trúc nhiều chiều đều đặn, trong khi danh sách Python có thể chứa nhiều kiểu đối tượng khác nhau. Mảng NumPy cũng hỗ trợ các phép toán số vector hóa.

### Câu 2

Vector hóa là áp dụng phép toán lên toàn bộ mảng mà không viết vòng lặp Python tường minh. Cách này thường giúp mã ngắn hơn và nhanh hơn với dữ liệu số lớn.

### Câu 3

Nhân theo từng phần tử nhân các phần tử tương ứng, ví dụ `A * B`. Nhân ma trận tuân theo quy tắc hàng–cột của đại số tuyến tính, ví dụ `A @ B`.

### Câu 4

Khi so sánh từ chiều ngoài cùng bên phải, hai chiều tương thích nếu chúng bằng nhau hoặc một trong hai bằng 1.

### Câu 5

View có thể dùng chung bộ nhớ với mảng gốc, nên thay đổi view có thể làm đổi dữ liệu gốc. Copy có bộ nhớ độc lập.

### Câu 6

Một số hàm thống kê gồm `np.mean()`, `np.median()`, `np.var()`, `np.std()`, `np.percentile()` và `np.quantile()`.

## Phần D

Đây là các bài tập lập trình mở. Bài làm nên trình bày mã nguồn, kết quả và giải thích ngắn gọn cho từng yêu cầu.

</details>
