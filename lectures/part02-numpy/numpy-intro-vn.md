# Giới thiệu NumPy

**Ngôn ngữ:** Tiếng Việt  
**Cập nhật theo slide:** `numpy_beamer_vietnamese_full_translation.pdf`  
**Chủ đề:** Mảng, vector hóa, broadcasting và tính toán số

---

## 1. Giới thiệu bài học

Bài học này giới thiệu **NumPy**, một thư viện Python cốt lõi cho **tính toán số**. NumPy được thiết kế để làm việc hiệu quả với mảng, ma trận và các tập dữ liệu số. Đối tượng trung tâm của NumPy là **mảng N chiều**, hay `ndarray`.

Trong phân tích dữ liệu và khoa học dữ liệu, NumPy thường được dùng để:

- lưu trữ dữ liệu số dưới dạng mảng;
- thực hiện phép toán trên toàn bộ mảng thay vì viết vòng lặp thủ công;
- xử lý ma trận, vector và các phép đại số tuyến tính;
- sinh số ngẫu nhiên cho mô phỏng và thực nghiệm;
- tính toán các thống kê mô tả;
- trao đổi dữ liệu với Pandas, SciPy, Matplotlib và Scikit-learn.

So với `list` thông thường trong Python, mảng NumPy thường lưu dữ liệu **đồng nhất về kiểu dữ liệu**, có cấu trúc bộ nhớ đều đặn hơn và hỗ trợ các phép toán vector hóa được tối ưu hóa.

---

## 2. Mục tiêu học tập

Sau bài học này, người học có thể:

- Giải thích vai trò của NumPy trong tính toán số.
- Phân biệt mảng NumPy với `list` Python.
- Cài đặt và import NumPy.
- Tạo mảng một chiều, hai chiều và nhiều chiều.
- Kiểm tra các thuộc tính như `shape`, `ndim`, `size`, `dtype`, `itemsize`, `nbytes`.
- Truy cập phần tử bằng indexing và slicing.
- Reshape, resize, stack và split mảng.
- Áp dụng phép toán vector hóa và broadcasting.
- Dùng các hàm tổng hợp như `sum()`, `mean()`, `min()`, `max()`.
- Dùng các universal functions như `np.sqrt()`, `np.exp()`, `np.log()`, `np.sin()`.
- Thực hiện các phép đại số tuyến tính cơ bản.
- Sinh số ngẫu nhiên và tính các thống kê mô tả.
- Hiểu cách NumPy tích hợp với Pandas và Scikit-learn.

---

## 3. Cấu trúc bài học

Bài học được tổ chức theo các nhóm tính năng, đúng với cấu trúc của slide:

1. NumPy là gì?
2. Vì sao nên học NumPy?
3. Cài đặt và import.
4. Tạo mảng.
5. Thuộc tính của mảng.
6. Indexing và slicing.
7. Reshape, resize, stack và split.
8. Broadcasting và số học.
9. Aggregation và universal functions.
10. Toán tử Boolean.
11. Đại số tuyến tính.
12. Số ngẫu nhiên và thống kê.
13. Vector hóa và hiệu năng.
14. Bộ nhớ, kiểu dữ liệu, sắp xếp, tìm kiếm.
15. Tích hợp với Pandas và Scikit-learn.
16. Lỗi thường gặp.
17. Câu hỏi ôn tập và bài tập thực hành.

---

## 4. Điều kiện tiên quyết

Người học nên có:

- Kiến thức Python cơ bản.
- Biết sử dụng biến, list, vòng lặp và hàm.
- Có môi trường chạy Python như Jupyter Notebook, JupyterLab, Google Colab hoặc VS Code.

---

# Phần 1. NumPy là gì?

## 1.1. Khái niệm

**NumPy**, viết tắt của **Numerical Python**, là thư viện Python dùng cho tính toán số nhanh và hiệu quả.

Đối tượng chính của NumPy là `ndarray`, tức là mảng N chiều. Một mảng NumPy có thể biểu diễn:

- vector một chiều;
- ma trận hai chiều;
- tensor ba chiều;
- các cấu trúc số có nhiều chiều hơn.

Ví dụ:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)
```

Kết quả:

```text
[10 20 30 40]
```

Ở đây, `np.array()` chuyển một list Python thành mảng NumPy.

## 1.2. NumPy cung cấp gì?

NumPy cung cấp:

- thao tác mảng nhanh;
- tính toán vector hóa;
- broadcasting;
- hàm đại số tuyến tính;
- hàm thống kê;
- sinh số ngẫu nhiên;
- tích hợp với Pandas, SciPy, Matplotlib, Scikit-learn.

## 1.3. Kiểm tra nhanh

**Câu 1.** Cấu trúc dữ liệu chính trong NumPy là gì?

A. `DataFrame`  
B. `tuple`  
C. `dictionary`  
D. `ndarray`  

**Câu 2. Đúng hay sai?** NumPy được thiết kế chủ yếu cho tính toán số.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 1.1. Nhận diện cấu trúc dữ liệu**

Cho đoạn mã:

```python
import numpy as np

x = np.array([2, 4, 6, 8])
```

Hãy:

1. Cho biết `x` là kiểu cấu trúc dữ liệu gì trong NumPy.
2. Dự đoán số chiều của `x`.
3. Giải thích vì sao `x` phù hợp cho tính toán số hơn một list Python thông thường.

**Bài 1.2. Liên hệ ứng dụng**

Nêu một ví dụ trong Data Science mà dữ liệu có thể được biểu diễn bằng:

- mảng một chiều;
- ma trận hai chiều;
- mảng ba chiều.


# Phần 2. Vì sao nên học NumPy?

## 2.1. Ý nghĩa trong phân tích dữ liệu

NumPy quan trọng vì nó là nền tảng cho rất nhiều công việc tính toán trong Python. Khi dữ liệu là số, việc dùng mảng NumPy thường giúp mã ngắn hơn, rõ hơn và nhanh hơn.

## 2.2. List Python và mảng NumPy

Một list Python có thể chứa nhiều kiểu dữ liệu khác nhau:

```python
values = [10, 2.5, "Python", True]
```

Một mảng NumPy thường chứa dữ liệu cùng kiểu:

```python
import numpy as np

values = np.array([10, 20, 30, 40])
print(values.dtype)
```

Mảng NumPy có cấu trúc đều đặn hơn, nhờ đó các phép toán số có thể được thực hiện hiệu quả hơn.

## 2.3. Ví dụ: nhân các giá trị

### Cách dùng list Python

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

### Cách dùng NumPy

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

Điểm khác biệt là NumPy cho phép viết `values * 10` để áp dụng phép nhân cho toàn bộ mảng. Đây là ví dụ đơn giản của **vectorization**.

## 2.4. Kiểm tra nhanh

**Câu 1.** Vì sao mảng NumPy hiệu quả cho tính toán số?

A. Vì nó tự động kết nối Internet.  
B. Vì nó dùng cấu trúc mảng đồng nhất và được tối ưu.  
C. Vì nó không sử dụng bộ nhớ.  
D. Vì nó luôn chứa văn bản.  

**Câu 2.** Biểu thức nào nhân mọi phần tử của mảng NumPy `a` với 10?

A. `a.sort(10)`  
B. `a.add("10")`  
C. `a * 10`  
D. `a.append(10)`  

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 2.1. So sánh list và NumPy**

Viết hai đoạn mã thực hiện cùng nhiệm vụ: nhân các giá trị `[2, 4, 6, 8]` với 5.

- Cách 1: dùng list và vòng lặp.
- Cách 2: dùng NumPy.

Sau đó so sánh số dòng mã của hai cách.

**Bài 2.2. Vectorization**

Cho:

```python
a = np.array([1, 3, 5, 7])
```

Không dùng vòng lặp, hãy tạo mảng mới sao cho mỗi phần tử được:

1. cộng thêm 10;
2. nhân với 2;
3. bình phương.


# Phần 3. Cài đặt và import NumPy

## 3.1. Cài đặt

Cài đặt NumPy bằng lệnh:

```bash
pip install numpy
```

Trong Google Colab hoặc Anaconda, NumPy thường đã được cài sẵn.

## 3.2. Import NumPy

Quy ước chuẩn là:

```python
import numpy as np
```

Bí danh `np` được dùng rộng rãi trong tài liệu, bài giảng và mã nguồn Python.

## 3.3. Kiểm tra phiên bản

```python
import numpy as np

print(np.__version__)
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 3.1. Kiểm tra môi trường**

Chạy:

```python
import numpy as np

print(np.__version__)
```

Hãy ghi lại:

1. phiên bản NumPy đang sử dụng;
2. bí danh chuẩn của NumPy;
3. tên hàm hoặc thuộc tính vừa dùng để kiểm tra phiên bản.


# Phần 4. Nhóm tính năng: Tạo mảng

## 4.1. Các lệnh NumPy liên quan

| Lệnh | Ý nghĩa |
|---|---|
| `np.array(data)` | Chuyển list, tuple hoặc cấu trúc lồng nhau thành `ndarray`. |
| `np.zeros(shape)` | Tạo mảng toàn số 0. |
| `np.ones(shape)` | Tạo mảng toàn số 1. |
| `np.full(shape, value)` | Tạo mảng được lấp đầy bởi một giá trị. |
| `np.arange(start, stop, step)` | Tạo dãy cách đều; `stop` không được lấy. |
| `np.linspace(start, stop, n)` | Tạo đúng `n` giá trị cách đều giữa hai đầu mút. |
| `np.eye(n)` | Tạo ma trận đơn vị kích thước `n × n`. |

## 4.2. Tạo mảng từ list

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

## 4.3. Tạo mảng một chiều

```python
arr = np.array([10, 20, 30, 40])
print(arr)
```

## 4.4. Tạo mảng hai chiều

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

## 4.5. Tạo mảng ba chiều

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

Mảng ba chiều có thể được hiểu như nhiều ma trận được xếp chồng lên nhau.

## 4.6. Các hàm tạo mảng thường dùng

```python
np.zeros(5)
```

Kết quả:

```text
[0. 0. 0. 0. 0.]
```

```python
np.zeros((2, 3))
```

Kết quả:

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

Kết quả:

```text
[0 2 4 6 8]
```

```python
np.linspace(0, 1, 5)
```

Kết quả:

```text
[0.   0.25 0.5  0.75 1.  ]
```

```python
np.eye(3)
```

Kết quả:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

## 4.7. Kiểm tra nhanh

**Câu 1.** Hàm nào chuyển list Python thành mảng NumPy?

A. `np.ndarray_list()`  
B. `np.array()`  
C. `np.convert()`  
D. `np.list()`  

**Câu 2.** Hàm nào tạo các giá trị cách đều giữa hai đầu mút?

A. `np.stack()`  
B. `np.mean()`  
C. `np.split()`  
D. `np.linspace()`  

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 4.1. Tạo các mảng cơ bản**

Hãy dùng NumPy để tạo:

1. mảng `[5, 10, 15, 20]`;
2. ma trận toàn số 0 kích thước `3 × 4`;
3. ma trận toàn số 1 kích thước `2 × 5`;
4. ma trận `3 × 3` toàn giá trị 7;
5. dãy số chẵn từ 0 đến 18;
6. 6 giá trị cách đều từ 0 đến 1.

**Bài 4.2. Ma trận đơn vị**

Tạo ma trận đơn vị kích thước `4 × 4` và giải thích vị trí của các phần tử bằng 1.


# Phần 5. Nhóm tính năng: Thuộc tính của mảng

## 5.1. Các thuộc tính liên quan

| Thuộc tính | Ý nghĩa |
|---|---|
| `arr.ndim` | Số chiều của mảng. |
| `arr.shape` | Kích thước theo từng chiều. |
| `arr.size` | Tổng số phần tử. |
| `arr.dtype` | Kiểu dữ liệu của phần tử. |
| `arr.itemsize` | Số byte cho mỗi phần tử. |
| `arr.nbytes` | Tổng số byte của toàn bộ mảng. |

## 5.2. Ví dụ

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

Diễn giải:

- `arr.ndim = 2`: mảng có 2 chiều.
- `arr.shape = (2, 3)`: mảng có 2 hàng và 3 cột.
- `arr.size = 6`: tổng cộng có 6 phần tử.
- `arr.dtype`: cho biết kiểu dữ liệu.
- `arr.itemsize`: số byte cho mỗi phần tử.
- `arr.nbytes`: tổng bộ nhớ mà các phần tử chiếm.

## 5.3. Ghi nhớ

Trước khi reshape, broadcasting hoặc đưa dữ liệu vào mô hình học máy, nên kiểm tra:

```python
print(arr.shape)
print(arr.dtype)
```

Nhiều lỗi NumPy bắt nguồn từ shape hoặc kiểu dữ liệu không như mong đợi.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 5.1. Đọc thuộc tính mảng**

Cho:

```python
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
```

Không chạy mã trước, hãy dự đoán:

1. `A.ndim`;
2. `A.shape`;
3. `A.size`.

Sau đó chạy mã để kiểm tra.

**Bài 5.2. Kiểu dữ liệu và bộ nhớ**

Tạo hai mảng cùng nội dung `[1, 2, 3, 4]`, một mảng dùng `int64`, một mảng dùng `int8`.

So sánh:

```python
arr.dtype
arr.itemsize
arr.nbytes
```


# Phần 6. Nhóm tính năng: Indexing và slicing

## 6.1. Các cú pháp liên quan

| Cú pháp | Ý nghĩa |
|---|---|
| `arr[i]` | Lấy phần tử tại vị trí `i`. |
| `arr[-1]` | Lấy phần tử cuối cùng. |
| `arr[a:b]` | Lấy các phần tử từ chỉ số `a` đến trước `b`. |
| `arr[::step]` | Lấy phần tử theo bước nhảy. |
| `matrix[i, j]` | Lấy phần tử ở hàng `i`, cột `j`. |
| `matrix[r1:r2, c1:c2]` | Lấy lát cắt hai chiều. |
| `arr.copy()` | Tạo bản sao độc lập. |

## 6.2. Indexing một chiều

```python
arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[2])
print(arr[-1])
```

Kết quả:

```text
10
30
40
```

## 6.3. Indexing hai chiều

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

## 6.4. Slicing một chiều

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[::2])
```

Kết quả:

```text
[20 30 40]
[10 30 50]
```

## 6.5. Slicing hai chiều

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

## 6.6. View và copy

Nhiều lát cắt trong NumPy trả về **view**, tức là dữ liệu có thể vẫn chia sẻ bộ nhớ với mảng gốc.

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

Nếu cần bản sao độc lập, dùng:

```python
copy = arr[1:3].copy()
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 6.1. Indexing**

Cho:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Hãy lấy:

1. phần tử đầu tiên;
2. phần tử thứ ba;
3. phần tử cuối cùng.

**Bài 6.2. Slicing**

Cho:

```python
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
```

Hãy lấy:

1. hai hàng đầu tiên;
2. hai cột cuối cùng;
3. khối con gồm hàng 2–3 và cột 2–4;
4. hàng cuối cùng.

**Bài 6.3. View hay copy?**

Tạo một slice từ mảng, thay đổi một phần tử của slice và kiểm tra mảng gốc. Sau đó lặp lại với `.copy()` và so sánh kết quả.


# Phần 7. Nhóm tính năng: Reshape, resize, stack và split

## 7.1. Các lệnh liên quan

| Lệnh | Ý nghĩa |
|---|---|
| `arr.reshape(r, c)` | Đổi shape của mảng nếu số phần tử tương thích. |
| `arr.reshape(..., -1)` | Để NumPy tự suy ra một chiều. |
| `arr.flatten()` | Làm phẳng mảng và trả về bản sao. |
| `arr.ravel()` | Làm phẳng mảng và thường trả về view nếu có thể. |
| `np.resize(arr, shape)` | Thay đổi tổng kích thước; có thể lặp lại giá trị. |
| `np.vstack((a, b))` | Ghép theo chiều dọc. |
| `np.hstack((a, b))` | Ghép theo chiều ngang. |
| `np.stack((a, b), axis=k)` | Ghép theo một trục mới. |
| `np.split(arr, n)` | Chia mảng thành `n` phần bằng nhau nếu có thể. |
| `np.hsplit(matrix, n)` | Chia ma trận theo chiều cột. |

## 7.2. Reshape

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

Dùng `-1` để NumPy tự suy ra một chiều:

```python
matrix = arr.reshape(2, -1)
print(matrix.shape)
```

## 7.3. Flatten và ravel

```python
flat = matrix.flatten()
flat_view = matrix.ravel()
```

- `flatten()` trả về bản sao.
- `ravel()` thường trả về view nếu có thể.

## 7.4. Resize

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

`resize()` có thể lặp lại giá trị nếu shape mới cần nhiều phần tử hơn.

## 7.5. Stacking

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(np.stack((a, b), axis=0))
```

## 7.6. Splitting

```python
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(arr, 3)

print(parts)
```

Kết quả:

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 7.1. Reshape**

Tạo:

```python
arr = np.arange(1, 13)
```

Hãy reshape thành:

1. ma trận `3 × 4`;
2. ma trận `2 × 6`;
3. ma trận có 4 hàng và để NumPy tự suy ra số cột bằng `-1`.

**Bài 7.2. Flatten và ravel**

Từ ma trận `3 × 4`, tạo:

```python
flat1 = matrix.flatten()
flat2 = matrix.ravel()
```

In `shape` của hai kết quả và cho biết điểm khác nhau quan trọng giữa hai lệnh.

**Bài 7.3. Stack và split**

Cho:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Hãy:

1. ghép dọc;
2. ghép ngang;
3. dùng `np.stack()` với `axis=0`;
4. tạo mảng từ 1 đến 8 và chia thành 4 phần bằng nhau.


# Phần 8. Nhóm tính năng: Broadcasting và số học

## 8.1. Các biểu thức liên quan

| Biểu thức | Ý nghĩa |
|---|---|
| `a + b`, `a - b` | Cộng/trừ theo từng phần tử. |
| `a * b` | Nhân theo từng phần tử. |
| `a / b` | Chia theo từng phần tử. |
| `a ** p` | Nâng từng phần tử lên lũy thừa `p`. |
| `a % b` | Phần dư theo từng phần tử. |
| `array + scalar` | Broadcast số vô hướng đến mọi phần tử. |
| `matrix + row` | Broadcast hàng 1-D tương thích lên các hàng của ma trận. |

## 8.2. Broadcasting với số vô hướng

```python
arr = np.array([1, 2, 3, 4])
result = arr + 10

print(result)
```

Kết quả:

```text
[11 12 13 14]
```

Số `10` được áp dụng cho mọi phần tử của mảng.

## 8.3. Broadcasting giữa các mảng

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

## 8.4. Quy tắc broadcasting cơ bản

Xét từ chiều ngoài cùng bên phải, hai chiều tương thích nếu:

- chúng bằng nhau; hoặc
- một trong hai bằng `1`.

Nếu shape không tương thích, NumPy sẽ báo lỗi.

## 8.5. Phép toán số học cơ bản

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

Lưu ý: `a * b` là nhân theo từng phần tử, không phải nhân ma trận.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 8.1. Số học theo phần tử**

Cho:

```python
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
```

Tính:

1. `a + b`;
2. `a - b`;
3. `a * b`;
4. `a / b`;
5. `a ** 2`.

**Bài 8.2. Broadcasting với scalar**

Cho:

```python
scores = np.array([7, 8, 6, 9])
```

Cộng 1 điểm cho mọi phần tử mà không dùng vòng lặp.

**Bài 8.3. Broadcasting với vector**

Cho ma trận:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

và:

```python
row = np.array([10, 20, 30])
```

Hãy tính `A + row`, rồi giải thích vì sao broadcasting hợp lệ.


# Phần 9. Nhóm tính năng: Aggregation và universal functions

## 9.1. Các lệnh liên quan

| Lệnh | Ý nghĩa |
|---|---|
| `arr.sum()`, `arr.mean()` | Tổng và trung bình. |
| `arr.min()`, `arr.max()` | Nhỏ nhất và lớn nhất. |
| `np.median(arr)` | Trung vị. |
| `np.var(arr)`, `np.std(arr)` | Phương sai và độ lệch chuẩn. |
| `func(..., axis=0)` | Tổng hợp theo cột. |
| `func(..., axis=1)` | Tổng hợp theo hàng. |
| `np.sqrt(arr)` | Căn bậc hai theo từng phần tử. |
| `np.exp(arr)`, `np.log(arr)` | Hàm mũ và log tự nhiên theo từng phần tử. |
| `np.sin(arr)` | Hàm sin theo từng phần tử. |
| `np.abs(arr)`, `np.round(arr)` | Giá trị tuyệt đối và làm tròn. |

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

## 9.3. Aggregation theo trục

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

- `axis=0`: tổng hợp theo chiều hàng, cho kết quả theo từng cột.
- `axis=1`: tổng hợp theo chiều cột, cho kết quả theo từng hàng.

## 9.4. Universal functions

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
```

Kết quả:

```text
[1. 2. 3. 4.]
```

```python
print(np.exp(np.array([0, 1, 2])))
print(np.log(np.array([1, np.e, np.e**2])))
print(np.sin(np.array([0, np.pi / 2, np.pi])))
print(np.abs(np.array([-3, -1, 2, 4])))
print(np.round(np.array([1.234, 5.678]), 2))
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 9.1. Thống kê nhanh**

Cho:

```python
x = np.array([4, 8, 6, 10, 12])
```

Tính:

1. tổng;
2. trung bình;
3. nhỏ nhất;
4. lớn nhất;
5. trung vị;
6. độ lệch chuẩn.

**Bài 9.2. Axis**

Cho:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

Tính:

1. tổng theo từng cột;
2. tổng theo từng hàng;
3. trung bình theo từng cột.

**Bài 9.3. Ufunc**

Cho:

```python
x = np.array([1, 4, 9, 16])
```

Hãy áp dụng `np.sqrt()` và giải thích đầu ra.


# Phần 10. Nhóm tính năng: Boolean operations

## 10.1. Các lệnh liên quan

| Biểu thức | Ý nghĩa |
|---|---|
| `arr > value` | Tạo mảng Boolean từ phép so sánh. |
| `arr[arr > value]` | Lọc phần tử thỏa điều kiện. |
| `(cond1) & (cond2)` | AND theo từng phần tử. |
| `(cond1) | (cond2)` | OR theo từng phần tử. |
| `~mask` | NOT theo từng phần tử. |
| `np.where(cond, a, b)` | Chọn `a` nếu điều kiện đúng, ngược lại chọn `b`. |

## 10.2. So sánh và lọc Boolean

```python
arr = np.array([10, 20, 30, 40])

print(arr > 20)
```

Kết quả:

```text
[False False  True  True]
```

```python
selected = arr[arr > 20]
print(selected)
```

Kết quả:

```text
[30 40]
```

## 10.3. Kết hợp nhiều điều kiện

```python
selected = arr[(arr >= 20) & (arr <= 30)]
print(selected)
```

Kết quả:

```text
[20 30]
```

Khi kết hợp nhiều điều kiện, cần đặt từng điều kiện trong dấu ngoặc.

## 10.4. Vector hóa điều kiện bằng `np.where()`

```python
arr = np.array([10, 20, 30, 40])

labels = np.where(arr >= 30, "high", "low")
print(labels)
```

Kết quả:

```text
['low' 'low' 'high' 'high']
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 10.1. Lọc theo một điều kiện**

Cho:

```python
scores = np.array([4, 7, 8, 5, 9, 6])
```

Hãy lọc:

1. các điểm lớn hơn hoặc bằng 7;
2. các điểm nhỏ hơn 6.

**Bài 10.2. Kết hợp điều kiện**

Lọc các điểm nằm trong khoảng từ 6 đến 8, kể cả hai đầu mút.

**Bài 10.3. Gán nhãn**

Dùng `np.where()` để tạo nhãn:

- `"Pass"` nếu điểm `>= 5`;
- `"Fail"` nếu điểm `< 5`.


# Phần 11. Nhóm tính năng: Đại số tuyến tính

## 11.1. Các lệnh liên quan

| Lệnh | Ý nghĩa |
|---|---|
| `A @ B` | Nhân ma trận. |
| `np.dot(A, B)` | Tích vô hướng hoặc tích ma trận tùy số chiều. |
| `A.T` | Chuyển vị. |
| `np.linalg.det(A)` | Định thức. |
| `np.linalg.inv(A)` | Nghịch đảo ma trận vuông không suy biến. |
| `np.linalg.solve(A, b)` | Giải hệ `Ax=b`. |
| `np.linalg.eig(A)` | Trị riêng và vector riêng. |
| `np.inner(a, b)` | Tích trong. |
| `np.outer(a, b)` | Tích ngoài. |
| `np.vdot(a, b)` | Tích vô hướng vector; xử lý liên hợp phức khi cần. |

## 11.2. Nhân ma trận

```python
A = np.array([
    [1, 2],
    [3, 4]
])

print(np.dot(A, A))
print(A @ A)
```

Kết quả:

```text
[[ 7 10]
 [15 22]]
```

## 11.3. Nhân theo phần tử và nhân ma trận

```python
print(A * A)
print(A @ A)
```

- `A * A`: nhân theo từng phần tử.
- `A @ A`: nhân ma trận.

## 11.4. Chuyển vị, định thức, nghịch đảo

```python
print(A.T)
print(np.linalg.det(A))
print(np.linalg.inv(A))
```

Nghịch đảo chỉ tồn tại với ma trận vuông không suy biến.

## 11.5. Giải hệ tuyến tính

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

## 11.6. Trị riêng và vector riêng

```python
eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)
print(eigenvectors)
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 11.1. Nhân theo phần tử và nhân ma trận**

Cho:

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

Tính và so sánh:

```python
A * B
A @ B
```

**Bài 11.2. Định thức và chuyển vị**

Tính:

```python
A.T
np.linalg.det(A)
```

**Bài 11.3. Giải hệ**

Cho:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])
```

Giải `Ax=b` bằng `np.linalg.solve()` và kiểm tra lại bằng `A @ x`.


# Phần 12. Nhóm tính năng: Số ngẫu nhiên và thống kê

## 12.1. Các lệnh liên quan

| Lệnh | Ý nghĩa |
|---|---|
| `np.random.default_rng(seed)` | Tạo bộ sinh số ngẫu nhiên hiện đại. |
| `rng.integers(low, high, size)` | Sinh số nguyên; `high` không được lấy. |
| `rng.uniform(...)` | Lấy mẫu từ phân phối đều. |
| `rng.normal(loc, scale, size)` | Lấy mẫu từ phân phối chuẩn. |
| `rng.binomial(...)` | Lấy mẫu từ phân phối nhị thức. |
| `rng.poisson(...)` | Lấy mẫu từ phân phối Poisson. |
| `np.percentile(data, q)` | Tính percentile trên thang 0–100. |
| `np.quantile(data, q)` | Tính quantile trên thang 0–1. |
| `np.isnan(data)` | Xác định giá trị `NaN`. |
| `np.nanmean(data)` | Tính trung bình khi bỏ qua `NaN`. |

## 12.2. Tạo bộ sinh số ngẫu nhiên

```python
rng = np.random.default_rng(42)
```

Seed `42` giúp tái lập kết quả trong môi trường tương thích.

## 12.3. Sinh số ngẫu nhiên

```python
print(rng.integers(low=1, high=10, size=5))
print(rng.uniform(low=0, high=1, size=5))
print(rng.normal(loc=0, scale=1, size=5))
print(rng.binomial(n=10, p=0.5, size=5))
print(rng.poisson(lam=3, size=5))
```

## 12.4. Thống kê mô tả

```python
data = np.array([12, 15, 18, 20, 25])

print(np.mean(data))
print(np.median(data))
print(np.var(data))
print(np.std(data))
print(np.percentile(data, 25))
print(np.quantile(data, 0.75))
```

Mặc định, `np.var()` và `np.std()` dùng `ddof=0`, tương ứng với chia cho `N`.

Nếu muốn dùng quy ước mẫu, chia cho `N-1`, sử dụng:

```python
print(np.var(data, ddof=1))
print(np.std(data, ddof=1))
```

## 12.5. Giá trị thiếu

```python
data = np.array([10.0, 20.0, np.nan, 40.0])

print(np.mean(data))
print(np.nanmean(data))
print(np.nanmedian(data))
print(np.isnan(data))
```

`np.mean(data)` trả về `nan` nếu mảng có giá trị thiếu. Các hàm như `np.nanmean()` bỏ qua `NaN`.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 12.1. Random integers**

Tạo:

```python
rng = np.random.default_rng(42)
```

Sau đó sinh 10 số nguyên trong khoảng từ 1 đến 100.

**Bài 12.2. Normal distribution**

Sinh 1,000 giá trị từ phân phối chuẩn với:

- mean = 0;
- standard deviation = 1.

Tính mean và standard deviation của mẫu.

**Bài 12.3. Percentile và quantile**

Cho:

```python
data = np.array([10, 20, 30, 40, 50])
```

Tính:

1. percentile 25;
2. percentile 50;
3. quantile 0.75.

**Bài 12.4. NaN**

Cho:

```python
data = np.array([10.0, np.nan, 20.0, 30.0])
```

Hãy:

1. xác định vị trí `NaN`;
2. tính mean khi bỏ qua `NaN`;
3. loại bỏ `NaN`.


# Phần 13. Nhóm tính năng: Vector hóa và hiệu năng

## 13.1. Ý tưởng

Vectorization nghĩa là viết phép toán ở mức toàn mảng thay vì lặp qua từng phần tử bằng vòng lặp Python.

## 13.2. Ví dụ

```python
a = np.arange(5)
result = a * 10

print(result)
```

Kết quả:

```text
[ 0 10 20 30 40]
```

Nếu không dùng NumPy:

```python
a = list(range(5))

result = []
for value in a:
    result.append(value * 10)

print(result)
```

Vectorized code thường:

- ngắn hơn;
- dễ đọc hơn;
- chạy nhanh hơn với dữ liệu số lớn;
- phù hợp hơn với quy trình phân tích dữ liệu.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 13.1. Chuyển vòng lặp thành vectorization**

Viết lại đoạn mã sau bằng NumPy mà không dùng vòng lặp:

```python
values = [1, 2, 3, 4, 5]
result = []

for x in values:
    result.append(x * 3 + 1)
```

**Bài 13.2. Vectorized condition**

Cho:

```python
sales = np.array([80, 120, 95, 150, 60])
```

Dùng `np.where()` để gán:

- `"High"` nếu doanh số `>= 100`;
- `"Low"` nếu doanh số `< 100`.


# Phần 14. Nhóm tính năng: Bộ nhớ, kiểu dữ liệu, sắp xếp, tìm kiếm và ảnh

## 14.1. Các lệnh liên quan

| Lệnh | Ý nghĩa |
|---|---|
| `arr.nbytes` | Tổng số byte của mảng. |
| `arr.astype(dtype)` | Chuyển kiểu dữ liệu. |
| `np.sort(arr)` | Trả về mảng đã sắp xếp. |
| `np.where(condition)` | Trả về chỉ số thỏa điều kiện. |
| `np.unique(arr)` | Trả về giá trị duy nhất. |
| `np.unique(arr, return_counts=True)` | Trả về giá trị duy nhất và tần suất. |
| `np.clip(arr, low, high)` | Giới hạn giá trị trong khoảng cho trước. |

## 14.2. Kiểm tra bộ nhớ

```python
arr = np.array([1, 2, 3, 4], dtype=np.int32)

print(arr.nbytes)
print(arr.dtype)
```

## 14.3. Chuyển kiểu dữ liệu

```python
arr = np.array([1.2, 2.8, 3.5])
integers = arr.astype(np.int32)

print(integers)
```

Kết quả:

```text
[1 2 3]
```

Khi chuyển từ số thực sang số nguyên, phần thập phân bị loại bỏ.

## 14.4. Sắp xếp và tìm kiếm

```python
arr = np.array([9, 3, 7, 1])
sorted_arr = np.sort(arr)

print(sorted_arr)
```

Kết quả:

```text
[1 3 7 9]
```

```python
arr = np.array([10, 20, 30, 40])
indices = np.where(arr > 20)

print(indices)
```

```python
arr = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique(arr, return_counts=True)

print(values)
print(counts)
```

## 14.5. Làm việc với ảnh

Ảnh số có thể được biểu diễn bằng mảng NumPy:

- ảnh xám: mảng hai chiều;
- ảnh màu: mảng ba chiều gồm chiều cao, chiều rộng và kênh màu.

Ví dụ:

```python
image = np.array([
    [0, 128, 255],
    [255, 128, 0],
    [50, 100, 150]
])

print(image.shape)
```

Tăng độ sáng:

```python
brighter = np.clip(image + 30, 0, 255)
```

`np.clip()` giữ giá trị trong khoảng hợp lệ, ví dụ từ 0 đến 255 với ảnh.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 14.1. Kiểu dữ liệu**

Tạo:

```python
x = np.array([1.2, 2.8, 3.5])
```

Chuyển `x` sang `int32` và quan sát kết quả.

**Bài 14.2. Sắp xếp và unique**

Cho:

```python
x = np.array([4, 2, 4, 1, 2, 2, 5])
```

Hãy:

1. sắp xếp mảng;
2. lấy các giá trị duy nhất;
3. đếm tần suất xuất hiện của từng giá trị.

**Bài 14.3. Ảnh số**

Cho:

```python
image = np.array([
    [0, 100, 240],
    [50, 200, 255]
])
```

Tăng độ sáng thêm 30 nhưng đảm bảo mọi giá trị vẫn nằm trong `[0, 255]`.


# Phần 15. Tích hợp với Pandas và Scikit-learn

## 15.1. Tích hợp với Pandas

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

Diễn giải:

- `pd.DataFrame(arr, columns=...)`: tạo DataFrame từ mảng NumPy.
- `df.to_numpy()`: chuyển DataFrame thành mảng NumPy.
- `np.sqrt(df["A"])`: áp dụng hàm NumPy cho cột Pandas.

## 15.2. Tích hợp với Scikit-learn

```python
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(np.array([[5]]))
print(prediction)
```

Trong học máy:

- `X` thường là ma trận đặc trưng;
- `y` là vector mục tiêu;
- dữ liệu đầu vào thường có dạng array-like, trong đó mảng NumPy là định dạng phổ biến.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 15.1. NumPy → Pandas**

Tạo mảng:

```python
arr = np.array([
    [1, 10],
    [2, 20],
    [3, 30]
])
```

Chuyển thành DataFrame với hai cột `"ID"` và `"Value"`.

**Bài 15.2. Pandas → NumPy**

Từ DataFrame vừa tạo, chuyển lại thành mảng NumPy bằng `to_numpy()` và kiểm tra `shape`.

**Bài 15.3. Feature matrix**

Cho:

```python
X = np.array([
    [20, 1],
    [25, 2],
    [30, 3]
])
```

Giải thích:

1. `X.shape` có ý nghĩa gì;
2. số hàng biểu diễn gì;
3. số cột biểu diễn gì trong ngữ cảnh machine learning.


# Phần 16. Các lỗi NumPy thường gặp

## 16.1. Shape không khớp

```python
a = np.ones((2, 3))
b = np.ones((2, 2))

# a + b gây lỗi broadcasting
```

Hai shape này không tương thích để broadcasting.

## 16.2. Reshape không hợp lệ

```python
arr = np.arange(10)

# arr.reshape(3, 4) gây lỗi
```

Lý do: 10 phần tử không thể reshape thành mảng `3 × 4`, vì shape đó cần 12 phần tử.

## 16.3. Chia cho 0

```python
arr = np.array([1.0, 0.0])

print(1 / arr)
```

Có thể sinh ra `inf` và cảnh báo runtime.

## 16.4. Tràn số nguyên

```python
arr = np.array([127], dtype=np.int8)

print(arr + 1)
```

Kiểu `int8` không biểu diễn được giá trị lớn hơn 127, nên có thể xảy ra tràn số.

## 16.5. Thay đổi ngoài ý muốn do view

```python
arr = np.array([10, 20, 30, 40])

view = arr[1:3]
view[0] = 999

print(arr)
```

Nếu cần mảng độc lập, dùng:

```python
copy = arr[1:3].copy()
```

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 16.1. Dự đoán lỗi reshape**

Cho:

```python
x = np.arange(10)
```

Trong các lệnh sau, lệnh nào hợp lệ?

```python
x.reshape(2, 5)
x.reshape(5, 2)
x.reshape(3, 4)
x.reshape(1, 10)
```

Giải thích bằng tổng số phần tử.

**Bài 16.2. Dự đoán broadcasting**

Cho các cặp shape:

1. `(3, 4)` và `(4,)`;
2. `(3, 4)` và `(1, 4)`;
3. `(3, 4)` và `(3, 1)`;
4. `(3, 4)` và `(2, 4)`.

Hãy dự đoán cặp nào broadcasting được.

**Bài 16.3. View**

Viết một ví dụ ngắn cho thấy thay đổi slice làm thay đổi mảng gốc, sau đó sửa bằng `.copy()`.


# Phần 17. Thực hành tốt

- Import NumPy bằng `import numpy as np`.
- Dùng vectorized operations thay vì vòng lặp Python khi phù hợp.
- Kiểm tra `shape`, `ndim`, `dtype` trước các phép toán phức tạp.
- Chỉ dùng broadcasting khi hiểu rõ shape sẽ hoạt động như thế nào.
- Phân biệt `A * B` và `A @ B`.
- Dùng `.copy()` khi cần bản sao độc lập.
- Chọn kiểu dữ liệu phù hợp để cân bằng miền giá trị, độ chính xác và bộ nhớ.
- Dùng seed cố định khi cần tái lập kết quả.
- Xử lý rõ ràng `NaN`, `inf`, chia cho 0 và tràn số.

---

## Bài tập nhỏ sau phần lý thuyết

**Bài 17.1. Kiểm tra mã**

Xem đoạn mã:

```python
A = np.arange(12).reshape(3, 4)
b = np.array([10, 20, 30])
result = A + b
```

Hãy:

1. kiểm tra `A.shape` và `b.shape`;
2. dự đoán mã có chạy được không;
3. nếu lỗi, sửa `b` để phép cộng broadcasting hợp lệ.

**Bài 17.2. Chọn cách viết tốt hơn**

So sánh:

```python
result = []
for x in arr:
    result.append(np.sqrt(x))
```

và:

```python
result = np.sqrt(arr)
```

Cho biết cách nào phù hợp hơn với NumPy và vì sao.


# Phần 18. Tóm tắt nội dung

| Chủ đề | Ý chính |
|---|---|
| NumPy | Thư viện cốt lõi của Python cho tính toán số. |
| `ndarray` | Mảng N chiều đồng nhất. |
| Vectorization | Phép toán trên toàn mảng không cần vòng lặp Python tường minh. |
| Broadcasting | Phép toán giữa các mảng có shape khác nhau nhưng tương thích. |
| Indexing và slicing | Truy cập và trích xuất phần tử. |
| Reshaping | Thay đổi hình dạng mảng. |
| Aggregation | Tính tổng, trung bình, min, max, phương sai, độ lệch chuẩn. |
| Ufunc | Hàm toán học nhanh theo từng phần tử. |
| Linear algebra | Nhân ma trận, nghịch đảo, định thức, trị riêng, giải hệ. |
| Random generation | Sinh giá trị từ phân phối xác suất. |
| Statistics | Trung bình, trung vị, phương sai, độ lệch chuẩn, percentile. |
| Integration | Kết nối với Pandas, SciPy, Matplotlib và Scikit-learn. |

---

# Phần 19. Câu hỏi ôn tập

## 19.1. Trắc nghiệm

**Câu 1.** NumPy chủ yếu dùng để làm gì?

A. Gửi email  
B. Tính toán số  
C. Thiết kế trang web  
D. Soạn thảo văn bản  

**Câu 2.** Cấu trúc dữ liệu trung tâm của NumPy là gì?

A. `set`  
B. `ndarray`  
C. `DataFrame`  
D. `class`  

**Câu 3.** Hàm nào tạo mảng từ list Python?

A. `np.array()`  
B. `np.list()`  
C. `np.convert_list()`  
D. `np.frame()`  

**Câu 4.** Thuộc tính nào trả về shape của mảng?

A. `shape`  
B. `type()`  
C. `mean`  
D. `size()`  

**Câu 5.** Biểu thức nào thực hiện nhân ma trận?

A. `A @ B`  
B. `A % B`  
C. `A | B`  
D. `A // B`  

**Câu 6.** Hàm nào tính trung bình khi bỏ qua `NaN`?

A. `np.ignore_mean()`  
B. `np.dropna()`  
C. `np.nanmean()`  
D. `np.mean_without_missing()`  

**Câu 7.** Hàm nào tạo ma trận đơn vị?

A. `np.reshape()`  
B. `np.ones_like_text()`  
C. `np.identity_text()`  
D. `np.eye()`  

**Câu 8.** Phát biểu nào đúng về broadcasting?

A. Nó luôn thay đổi mảng gốc.  
B. Nó xóa mọi giá trị trùng lặp.  
C. Nó hỗ trợ phép toán giữa các shape tương thích.  
D. Nó chuyển mọi mảng thành một chiều.  

**Câu 9.** Trong tổng hợp mảng hai chiều, `axis=0` thường có nghĩa là gì?

A. Chuyển ma trận thành một số duy nhất.  
B. Đảo ngược mọi giá trị.  
C. Tổng hợp theo chiều hàng và trả về kết quả theo từng cột.  
D. Tổng hợp theo chiều cột và trả về kết quả theo từng hàng.  

**Câu 10.** Đối tượng nào được khuyến nghị cho sinh số ngẫu nhiên hiện đại trong NumPy?

A. `np.random.file_reader()`  
B. `np.random.secure_password()`  
C. `np.array.randomize_text()`  
D. `np.random.default_rng()`  

## 19.2. Đúng/Sai

**Câu 1.** Mảng NumPy thường chứa các phần tử cùng kiểu dữ liệu.  
**Câu 2.** Vectorized operations luôn cần vòng lặp Python tường minh.  
**Câu 3.** `A * B` và `A @ B` luôn thực hiện cùng một phép toán.  
**Câu 4.** Slice của NumPy có thể chia sẻ bộ nhớ với mảng gốc.  
**Câu 5.** Broadcasting yêu cầu các chiều của mảng phải tương thích.  
**Câu 6.** `np.std(data, ddof=1)` có thể dùng cho quy ước độ lệch chuẩn mẫu.  
**Câu 7.** Bộ sinh số ngẫu nhiên của NumPy nên được xem là an toàn mật mã.  
**Câu 8.** Mảng NumPy có thể được dùng làm đầu vào cho mô hình Scikit-learn.

## 19.3. Câu hỏi ngắn

**Câu 1.** Nêu hai điểm khác nhau giữa list Python và mảng NumPy.  
**Câu 2.** Giải thích vectorization và nêu một lợi ích.  
**Câu 3.** Phân biệt nhân theo từng phần tử và nhân ma trận.  
**Câu 4.** Nêu quy tắc tương thích broadcasting cơ bản.  
**Câu 5.** Phân biệt view và copy.  
**Câu 6.** Kể tên bốn hàm thống kê trong NumPy.

---

# Phần 20. Bài tập thực hành

## Bài tập 1. Tạo mảng

1. Tạo mảng chứa các giá trị từ 1 đến 20.
2. Reshape thành ma trận `4 × 5`.
3. In ra `shape`, `ndim`, `size`, `dtype`.

## Bài tập 2. Indexing và slicing

Với ma trận `4 × 5` ở Bài tập 1:

1. Lấy hàng đầu tiên.
2. Lấy cột cuối cùng.
3. Lấy phần trung tâm kích thước `2 × 3`.
4. Lọc tất cả giá trị chẵn bằng Boolean filtering.

## Bài tập 3. Thống kê

Tạo một mảng gồm 10 giá trị số và tính:

1. Mean.
2. Median.
3. Variance.
4. Sample standard deviation.
5. Minimum và maximum.
6. Percentile 25, 50 và 75.

## Bài tập 4. Broadcasting

1. Tạo một ma trận `3 × 4`.
2. Tạo một mảng một chiều gồm 4 giá trị.
3. Cộng mảng một chiều đó vào từng hàng của ma trận.
4. Giải thích vì sao broadcasting hợp lệ.

## Bài tập 5. Đại số tuyến tính

Cho:

```python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([8, 13])
```

1. Tính định thức của `A`.
2. Tính nghịch đảo của `A`.
3. Giải hệ `Ax=b`.
4. Kiểm tra nghiệm bằng `A @ x`.

## Bài tập 6. Dữ liệu ngẫu nhiên

1. Tạo bộ sinh số ngẫu nhiên với seed `42`.
2. Sinh 1,000 giá trị từ phân phối chuẩn chuẩn hóa.
3. Tính mean và standard deviation.
4. So sánh kết quả mẫu với giá trị lý thuyết.

## Bài tập 7. Giá trị thiếu

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
2. Tính trung bình khi bỏ qua giá trị thiếu.
3. Loại bỏ tất cả giá trị thiếu.
4. Thay giá trị thiếu bằng trung vị của các giá trị quan sát được.

---

# Đáp án và gợi ý


## Đáp án các câu kiểm tra nhanh

1. D — Cấu trúc dữ liệu chính trong NumPy là gì?  
2. B — Vì sao mảng NumPy hiệu quả cho tính toán số?  
3. C — Biểu thức nào nhân mọi phần tử của mảng NumPy `a` với 10?  
4. B — Hàm nào chuyển list Python thành mảng NumPy?  
5. D — Hàm nào tạo các giá trị cách đều giữa hai đầu mút?  

## Đáp án trắc nghiệm

1. B  
2. B  
3. A  
4. A  
5. A  
6. C  
7. D  
8. C  
9. C  
10. D  ## Đáp án Đúng/Sai

1. Đúng  
2. Sai  
3. Sai  
4. Đúng  
5. Đúng  
6. Đúng  
7. Sai  
8. Đúng

## Gợi ý câu hỏi ngắn

**Câu 1.** List Python có thể chứa nhiều kiểu dữ liệu khác nhau; mảng NumPy thường chứa dữ liệu đồng nhất và tối ưu cho tính toán số.

**Câu 2.** Vectorization là cách áp dụng phép toán cho toàn bộ mảng mà không viết vòng lặp Python tường minh. Lợi ích là mã ngắn hơn, dễ đọc hơn và thường nhanh hơn.

**Câu 3.** `A * B` nhân từng phần tử tương ứng. `A @ B` là nhân ma trận theo quy tắc đại số tuyến tính.

**Câu 4.** Xét từ chiều ngoài cùng bên phải, hai chiều tương thích nếu chúng bằng nhau hoặc một trong hai bằng 1.

**Câu 5.** View có thể chia sẻ bộ nhớ với mảng gốc; copy là bản sao độc lập.

**Câu 6.** Ví dụ: `np.mean()`, `np.median()`, `np.var()`, `np.std()`, `np.percentile()`, `np.quantile()`.

## Gợi ý lời giải bài tập thực hành

### Bài tập 1

```python
arr = np.arange(1, 21)
matrix = arr.reshape(4, 5)

print(matrix)
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix.dtype)
```

### Bài tập 2

```python
print(matrix[0, :])
print(matrix[:, -1])
print(matrix[1:3, 1:4])
print(matrix[matrix % 2 == 0])
```

### Bài tập 3

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

### Bài tập 4

```python
matrix = np.arange(12).reshape(3, 4)
row = np.array([10, 20, 30, 40])

result = matrix + row
print(result)
```

Broadcasting hợp lệ vì shape của `matrix` là `(3, 4)` và shape của `row` là `(4,)`. NumPy xem `row` như một hàng có 4 phần tử và broadcast nó qua 3 hàng của ma trận.

### Bài tập 5

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

### Bài tập 6

```python
rng = np.random.default_rng(42)

values = rng.normal(loc=0, scale=1, size=1000)

print(np.mean(values))
print(np.std(values, ddof=1))
```

Mean mẫu nên gần 0 và standard deviation mẫu nên gần 1, nhưng không nhất thiết đúng bằng 0 và 1.

### Bài tập 7

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
