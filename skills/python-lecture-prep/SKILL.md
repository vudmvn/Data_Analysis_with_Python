---
name: python-lecture-prep
description: Quy trình và công cụ hỗ trợ chuẩn bị bài giảng, tài liệu thực hành, Jupyter Notebooks, dữ liệu mẫu, hình ảnh minh họa và tự động xuất bản (publish) lên GitHub cho môn Phân tích dữ liệu với Python (DSAI1005). Kích hoạt khi người dùng yêu cầu soạn bài giảng, tạo notebook, thiết kế bài tập/lab, quản lý hình ảnh hoặc đẩy bài giảng mới lên GitHub.
---

# Skill: Hỗ trợ Soạn Bài giảng, Quản lý Hình ảnh & Xuất bản GitHub - Phân tích dữ liệu với Python (DSAI1005)

Skill này được thiết kế riêng cho học phần **DSAI1005 – Phân tích dữ liệu với Python** (Giảng viên: TS. Vũ Đức Minh, ĐH Kinh tế Quốc dân).

---

## 🏛️ 1. Cấu trúc Tài liệu Bài giảng Chuẩn

Mỗi bài giảng theo từng tuần (hoặc chủ đề) trong repository sẽ tuân theo cấu trúc thư mục tiêu chuẩn sau:

```text
lectures/
└── week-XX-<ten-chu-de>/
    ├── README.md                  # Tóm tắt lý thuyết, mục tiêu bài học & chỉ dẫn (dùng link images/)
    ├── slides.md                  # Slide bài giảng dạng Markdown (tương thích Marp, dùng link images/)
    ├── lecture.ipynb              # Notebook giảng dạy chính (Lý thuyết + Minh họa Code)
    ├── lab_exercise.ipynb         # Bài tập thực hành cho sinh viên (Skeleton Code)
    ├── lab_solution.ipynb         # Lời giải chi tiết dành cho giảng viên
    ├── data/                      # Dữ liệu mẫu phục vụ bài giảng & thực hành
    │   └── dataset.csv
    └── images/                    # THƯ MỤC CHỨA HÌNH ẢNH MINH HỌA CỦA TUẦN HỌC
        ├── architecture.png
        └── chart_example.png
```

---

## 🖼️ 2. Quy chuẩn Quản lý Hình ảnh & Cập nhật Đường dẫn (Image Management Rules)

Khi tạo hoặc nhúng hình ảnh vào bài giảng, Agent **BẮT BUỘC** thực hiện theo các nguyên tắc sau:

### 1. Vị trí lưu trữ hình ảnh
- Tất cả các tệp hình ảnh (sơ đồ, minh họa, ảnh chụp biểu đồ, ảnh sinh tự động từ `generate_image`, v.v.) dành cho tuần học nào **phải được đặt vào thư mục `images/`** của tuần học đó (`lectures/week-XX-<slug>/images/`).
- Tuyệt đối **không** đặt ảnh ở thư mục gốc, thư mục tạm, hay lưu URL bên ngoài không ổn định.

### 2. Định dạng & Đặt tên tệp hình ảnh
- Đặt tên tệp ảnh bằng chữ cái thường, không dấu, nối bằng dấu gạch ngang `-` (VD: `data-cleaning-pipeline.png`, `seaborn-heatmap-example.png`).

### 3. Cập nhật đường dẫn tương đối (Relative Paths) trong tệp Markdown (`.md`) và Jupyter Notebook (`.ipynb`)
- Trong `README.md` và `slides.md`: Sử dụng đường dẫn tương đối trỏ tới `images/`:
  - **Cú pháp Markdown:** `![Mô tả hình ảnh](images/ten-anh.png)`
  - **Cú pháp HTML (khi cần căn chỉnh kích thước):** `<img src="images/ten-anh.png" alt="Mô tả hình ảnh" width="700" />`
- Trong `lecture.ipynb` (các cell Markdown):
  - `![Mô tả hình ảnh](images/ten-anh.png)`

---

## 🔄 3. Quy trình Soạn Bài giảng (5 Bước)

Khi người dùng yêu cầu soạn bài giảng cho một tuần/chủ đề bất kỳ, Agent áp dụng quy trình 5 bước:

### Bước 1: Xác định Yêu cầu & Chuẩn đầu ra (CLOs)
- Đối chiếu chủ đề tuần học với file `syllabus-vn.md`.
- Xác định mục tiêu bài học (Ví dụ: Hiểu NumPy array, thao tác vectorized operations, v.v.).
- Lựa chọn dataset phù hợp (Finance, E-commerce, Marketing hoặc tự sinh data giả lập chất lượng cao).

### Bước 2: Tạo Nội dung Lý thuyết, Slide & Hình ảnh Minh họa (`README.md`, `slides.md` & `images/`)
- Biên soạn nội dung ngắn gọn, súc tích bằng tiếng Việt.
- Đưa vào các ví dụ thực tế trong kinh doanh, tài chính và thương mại điện tử.
- Nếu tạo hoặc sinh ảnh minh họa, lưu ảnh vào `lectures/week-XX-<slug>/images/` và chèn đường dẫn `![Mô tả](images/filename.png)` vào `README.md` & `slides.md`.
- Thiết kế slide bằng định dạng Marp Markdown để dễ dàng convert sang PDF/PPTX.

### Bước 3: Biên soạn Jupyter Notebook (`lecture.ipynb`)
- Sử dụng Markdown cell giải thích trực quan (kèm công thức LaTeX và ảnh minh họa từ `images/`).
- Code Cell: Viết code Python mẫu sạch, có chú thích chi tiết, chuẩn PEP 8.
- Trực quan hóa dữ liệu (Matplotlib / Seaborn / Plotly) đẹp mắt. Khi xuất đồ thị ra file ảnh, lưu vào `images/`.

### Bước 4: Tạo Bài tập Thực hành & Lời giải (`lab_exercise.ipynb` & `lab_solution.ipynb`)
- **`lab_exercise.ipynb`**: Chứa yêu cầu bài tập, gợi ý (hints), cùng các ô code dạng `# TODO: Sinh viên viết code tại đây`.
- **`lab_solution.ipynb`**: Chứa lời giải hoàn chỉnh cùng kết quả output mẫu.

### Bước 5: Kiểm tra & Xuất bản lên GitHub (`Git & GitHub CLI`)
- Kiểm tra tính hợp lệ của code và các đường dẫn hình ảnh `images/`.
- Cập nhật mục lục tại file root `README.md`.
- Thực hiện xuất bản tự động qua `python scripts/publish_lecture.py -m "feat(lecture): Soạn bài giảng Tuần XX - <Tên chủ đề>"`.

---

## 🛠️ 4. Lệnh Thường Dùng (Commands & Workflow Integration)

### Tạo Bài giảng mới:
Người dùng có thể yêu cầu:
> *"Soạn bài giảng Tuần 4 về Trực quan hóa dữ liệu với Matplotlib và Seaborn kèm hình ảnh sơ đồ quy trình trong folder images"*

Agent sẽ tự động tạo bộ tệp bài giảng cho Tuần 4, lưu ảnh vào `images/`, cập nhật link `images/` trong các file `.md` và tự động push lên GitHub khi hoàn tất.
