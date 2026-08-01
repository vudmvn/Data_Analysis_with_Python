---
name: python-lecture-prep
description: Quy trình và công cụ hỗ trợ chuẩn bị bài giảng, tài liệu thực hành, Jupyter Notebooks, dữ liệu mẫu và tự động xuất bản (publish) lên GitHub cho môn Phân tích dữ liệu với Python (DSAI1005). Kích hoạt khi người dùng yêu cầu soạn bài giảng, tạo notebook, thiết kế bài tập/lab, hoặc đẩy bài giảng mới lên GitHub.
---

# Skill: Hỗ trợ Soạn Bài giảng & Xuất bản GitHub - Phân tích dữ liệu với Python (DSAI1005)

Skill này được thiết kế riêng cho học phần **DSAI1005 – Phân tích dữ liệu với Python** (Giảng viên: TS. Vũ Đức Minh, ĐH Kinh tế Quốc dân).

---

## 🏛️ 1. Cấu trúc Tài liệu Bài giảng Chuẩn

Mỗi bài giảng theo từng tuần (hoặc chủ đề) trong repository sẽ tuân theo cấu trúc thư mục tiêu chuẩn sau:

```text
lectures/
└── week-XX-<ten-chu-de>/
    ├── README.md                  # Tóm tắt lý thuyết, mục tiêu bài học & chỉ dẫn
    ├── slides.md                  # Slide bài giảng dạng Markdown (tương thích Marp)
    ├── lecture.ipynb              # Notebook giảng dạy chính (Lý thuyết + Minh họa Code)
    ├── lab_exercise.ipynb         # Bài tập thực hành cho sinh viên (Skeleton Code)
    ├── lab_solution.ipynb         # Lời giải chi tiết dành cho giảng viên
    └── data/                      # Dữ liệu mẫu phục vụ bài giảng & thực hành
        └── dataset.csv
```

---

## 🔄 2. Quy trình Soạn Bài giảng (5 Bước)

Khi người dùng yêu cầu soạn bài giảng cho một tuần/chủ đề bất kỳ, Agent áp dụng quy trình 5 bước:

### Bước 1: Xác định Yêu cầu & Chuẩn đầu ra (CLOs)
- Đối chiếu chủ đề tuần học với file `syllabus-vn.md`.
- Xác định mục tiêu bài học (Ví dụ: Hiểu NumPy array, thao tác vectorized operations, v.v.).
- Lựa chọn dataset phù hợp (Finance, E-commerce, Marketing hoặc tự sinh data giả lập chất lượng cao).

### Bước 2: Tạo Nội dung Lý thuyết & Slide (`README.md` & `slides.md`)
- Biên soạn nội dung ngắn gọn, súc tích bằng tiếng Việt.
- Đưa vào các ví dụ thực tế trong kinh doanh, tài chính và thương mại điện tử.
- Thiết kế slide bằng định dạng Marp Markdown để dễ dàng convert sang PDF/PPTX.

### Bước 3: Biên soạn Jupyter Notebook (`lecture.ipynb`)
- Sử dụng Markdown cell giải thích trực quan (kèm công thức LaTeX nếu có).
- Code Cell: Viết code Python mẫu sạch, có chú thích chi tiết, chuẩn PEP 8.
- Trực quan hóa dữ liệu (Matplotlib / Seaborn / Plotly) đẹp mắt, có tiêu đề, nhãn trục và legend đầy đủ.

### Bước 4: Tạo Bài tập Thực hành & Lời giải (`lab_exercise.ipynb` & `lab_solution.ipynb`)
- **`lab_exercise.ipynb`**: Chứa yêu cầu bài tập, gợi ý (hints), cùng các ô code dạng `# TODO: Sinh viên viết code tại đây`.
- **`lab_solution.ipynb`**: Chứa lời giải hoàn chỉnh cùng kết quả output mẫu.

### Bước 5: Kiểm tra & Xuất bản lên GitHub (`Git & GitHub CLI`)
- Kiểm tra tính hợp lệ của code.
- Cập nhật mục lục tại file root `README.md`.
- Thực hiện chuỗi lệnh git:
  1. `git add .`
  2. `git commit -m "feat(lecture): Soạn bài giảng Tuần XX - <Tên chủ đề>"`
  3. `git push origin main`

---

## 🛠️ 3. Lệnh Thường Dùng (Commands & Workflow Integration)

### Tạo Bài giảng mới:
Người dùng có thể yêu cầu:
> *"Soạn bài giảng Tuần 4 về Trực quan hóa dữ liệu với Matplotlib và Seaborn"*

Agent sẽ tự động áp dụng Skill này để tạo đầy đủ bộ tệp bài giảng cho Tuần 4 và tự động push lên GitHub khi hoàn tất.
