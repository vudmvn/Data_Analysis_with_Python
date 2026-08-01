---
name: python-lecture-prep
description: Quy trình và công cụ hỗ trợ chuẩn bị bài giảng, tài liệu thực hành, Jupyter Notebooks, dữ liệu mẫu, hình ảnh minh họa (căn giữa ảnh, tự động đổi tên ảnh trùng không ghi đè) và tự động xuất bản (publish) lên GitHub cho môn Phân tích dữ liệu với Python (DSAI1005). Kích hoạt khi người dùng yêu cầu soạn bài giảng, tạo notebook, thiết kế bài tập/lab, quản lý hình ảnh hoặc đẩy bài giảng mới lên GitHub.
---

# Skill: Hỗ trợ Soạn Bài giảng, Quản lý & Căn giữa Hình ảnh, Xuất bản GitHub - Phân tích dữ liệu với Python (DSAI1005)

Skill này được thiết kế riêng cho học phần **DSAI1005 – Phân tích dữ liệu với Python** (Giảng viên: TS. Vũ Đức Minh, ĐH Kinh tế Quốc dân).

---

## 🏛️ 1. Cấu trúc Tài liệu Bài giảng Chuẩn

Mỗi bài giảng theo từng tuần (hoặc chủ đề) trong repository sẽ tuân theo cấu trúc thư mục tiêu chuẩn sau:

```text
lectures/
└── week-XX-<ten-chu-de>/
    ├── README.md                  # Tóm tắt lý thuyết, mục tiêu bài học & chỉ dẫn (dùng link images/ + căn giữa ảnh)
    ├── slides.md                  # Slide bài giảng dạng Markdown (tương thích Marp, căn giữa ảnh)
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

## 🖼️ 2. Quy chuẩn Quản lý, Căn giữa & Bảo vệ Hình ảnh (Image Centering & Preservation Rules)

Khi tạo, nhúng hoặc hiển thị hình ảnh trong tệp Markdown (`.md`) và Jupyter Notebook (`.ipynb`), Agent **BẮT BUỘC** thực hiện theo 4 nguyên tắc sau:

### 1. Vị trí lưu trữ hình ảnh
- Tất cả các tệp hình ảnh (sơ đồ, minh họa, ảnh chụp biểu đồ, ảnh sinh tự động từ `generate_image`, v.v.) dành cho tuần học nào **phải được đặt vào thư mục `images/`** của tuần học đó (`lectures/week-XX-<slug>/images/`).
- Tuyệt đối **không** đặt ảnh ở thư mục gốc, thư mục tạm, hay lưu URL bên ngoài không ổn định.

### 2. Định dạng & Đặt tên tệp hình ảnh
- Đặt tên tệp ảnh bằng chữ cái thường, không dấu, nối bằng dấu gạch ngang `-` (VD: `data-cleaning-pipeline.png`, `seaborn-heatmap-example.png`).

### 3. Quy tắc Không Ghi đè & Tự động Đổi tên Ảnh Trùng (No-Overwrite & Auto-Rename Rule)
- **TUYỆT ĐỐI KHÔNG XÓA HOẶC GHI ĐÈ** lên các tệp hình ảnh đã tồn tại trong thư mục `images/`.
- Khi chèn hoặc sinh một hình ảnh mới, Agent phải kiểm tra xem tên tệp đã tồn tại trong thư mục `images/` hay chưa.
- **Tự động đổi tên ảnh trùng (Auto-rename on collision):** Nếu tên tệp dự định lưu đã tồn tại (ví dụ `data-flow.png`), Agent sẽ tự động bổ sung số thứ tự tăng dần thành `data-flow-1.png`, `data-flow-2.png`, ... hoặc gán nhãn mô tả phân biệt.
- Cập nhật đường dẫn tương đối trong tệp Markdown (`.md`) hoặc Notebook (`.ipynb`) trỏ chính xác tới tên tệp mới đã đổi tên.

### 4. Quy chuẩn Căn giữa Hình ảnh (Image Centering Mandatory Rule)
- **TẤT CẢ HÌNH ẢNH** xuất hiện trong các tệp Markdown (`README.md`, `slides.md`, các bài đọc `.md`) và cell Markdown của Jupyter Notebook (`.ipynb`) **PHẢI ĐƯỢC CĂN GIỮA (CENTERED)** để tạo giao diện bài giảng chuyên nghiệp và cân đối.
- **Cú pháp HTML Căn giữa Chuẩn (Recommended):**
  ```html
  <p align="center">
    <img src="images/ten-anh.png" alt="Mô tả hình ảnh" width="800" />
  </p>
  ```
- Cú pháp này tương thích 100% trên GitHub Markdown, Marp Presentation Slides, Jupyter Notebooks và các trình duyệt web.

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
- Lưu ảnh mới vào `lectures/week-XX-<slug>/images/` (kiểm tra đổi tên nếu trùng ảnh cũ) và **luôn căn giữa hình ảnh** bằng `<p align="center"><img src="images/..." /></p>`.
- Thiết kế slide bằng định dạng Marp Markdown để dễ dàng convert sang PDF/PPTX.

### Bước 3: Biên soạn Jupyter Notebook (`lecture.ipynb`)
- Sử dụng Markdown cell giải thích trực quan (kèm công thức LaTeX và ảnh căn giữa từ `images/`).
- Code Cell: Viết code Python mẫu sạch, có chú thích chi tiết, chuẩn PEP 8.
- Trực quan hóa dữ liệu (Matplotlib / Seaborn / Plotly) đẹp mắt. Khi xuất đồ thị ra file ảnh, lưu vào `images/` (kiểm tra không đè file cũ).

### Bước 4: Tạo Bài tập Thực hành & Lời giải (`lab_exercise.ipynb` & `lab_solution.ipynb`)
- **`lab_exercise.ipynb`**: Chứa yêu cầu bài tập, gợi ý (hints), cùng các ô code dạng `# TODO: Sinh viên viết code tại đây`.
- **`lab_solution.ipynb`**: Chứa lời giải hoàn chỉnh cùng kết quả output mẫu.

### Bước 5: Kiểm tra & Xuất bản lên GitHub (`Git & GitHub CLI`)
- Kiểm tra tính hợp lệ của code, căn giữa ảnh, tự động đổi tên bảo vệ ảnh và các đường dẫn hình ảnh `images/`.
- Cập nhật mục lục tại file root `README.md`.
- Thực hiện xuất bản tự động qua `python scripts/publish_lecture.py -m "feat(lecture): Soạn bài giảng Tuần XX - <Tên chủ đề>"`.

---

## 🛠️ 4. Lệnh Thường Dùng (Commands & Workflow Integration)

### Tạo Bài giảng mới:
Người dùng có thể yêu cầu:
> *"Soạn bài giảng Tuần 4 về Trực quan hóa dữ liệu với Matplotlib và Seaborn kèm hình ảnh mới không ghi đè ảnh cũ và căn giữa tất cả ảnh trong folder images"*

Agent sẽ tự động tạo bộ tệp bài giảng cho Tuần 4, lưu ảnh vào `images/` (tự đổi tên nếu trùng), căn giữa tất cả ảnh trong `.md` và tự động push lên GitHub khi hoàn tất.
