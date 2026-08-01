# Quy trình Soạn bài giảng & Xuất bản lên GitHub (Phân tích dữ liệu với Python - DSAI1005)

Tài liệu này hướng dẫn chi tiết quy trình chuẩn bị bài giảng, tạo tài liệu thực hành (Jupyter Notebooks, Slides), sinh dữ liệu mẫu và tự động xuất bản lên GitHub bằng công cụ **Antigravity Skill** và các bộ script hỗ trợ.

---

## 🏗️ 1. Cấu trúc Quản lý Bài giảng trong Repository

Mỗi tuần học sẽ nằm trong một thư mục riêng biệt tại đường dẫn `lectures/week-XX-<ten-chu-de>`:

```text
Data_Analysis_with_Python/
├── .gemini/
│   └── skills/
│       └── python-lecture-prep/    # Antigravity Custom Skill
│           └── SKILL.md
├── lectures/
│   ├── week-01-gioi-thieu-hoc-phan/
│   │   ├── README.md               # Tóm tắt lý thuyết & chỉ dẫn tuần 1
│   │   ├── slides.md               # Slide bài giảng (định dạng Marp)
│   │   ├── lecture.ipynb           # Notebook bài giảng lý thuyết + minh họa
│   │   ├── lab_exercise.ipynb      # Notebook bài tập thực hành sinh viên
│   │   ├── lab_solution.ipynb      # Notebook đáp án cho giảng viên/trợ giảng
│   │   └── data/                   # Bộ dữ liệu dùng trong tuần 1
│   └── week-02-numpy-pandas/
├── scripts/
│   ├── create_lecture.py           # Script khởi tạo khung bài giảng mới
│   └── publish_lecture.py          # Script tự động cập nhật README & push GitHub
├── syllabus-vn.md                  # Đề cương chi tiết học phần DSAI1005
└── README.md                       # Trang chủ repo + Mục lục bài giảng
```

---

## ⚡ 2. Quy trình Soạn Bài giảng Chi tiết

### Bước 1: Khởi tạo khung bài giảng tuần mới
Chạy script Python để sinh nhanh bộ file mẫu:
```bash
python scripts/create_lecture.py --week <Số_tuần> --title "<Tên_chủ_đề>"
```
*Ví dụ:*
```bash
python scripts/create_lecture.py --week 2 --title "Thư viện tính toán NumPy và Pandas"
```

### Bước 2: Nhờ AI Assistant (Antigravity Agent) biên soạn nội dung
Khi Antigravity được kích hoạt, bạn chỉ cần ra lệnh cho AI bằng tiếng Việt:
> *"Soạn bài giảng Tuần 2 về NumPy và Pandas theo đề cương syllabus-vn.md. Bổ sung các ví dụ về phân tích dữ liệu bán hàng và tạo bài tập lab có gợi ý."*

Agent sẽ tự động đọc `syllabus-vn.md`, áp dụng `python-lecture-prep` skill để:
1. Điền lý thuyết chi tiết vào `lecture.ipynb` & `slides.md`.
2. Tạo mã nguồn ví dụ (có chú thích Tiếng Việt, chuẩn PEP8).
3. Tạo dữ liệu giả lập chất lượng cao lưu vào thư mục `data/`.
4. Tạo bài tập thực hành `lab_exercise.ipynb` và đáp án `lab_solution.ipynb`.

### Bước 3: Xuất bản tự động lên GitHub
Sau khi biên soạn xong, bạn chỉ cần chạy:
```bash
python scripts/publish_lecture.py -m "feat(lecture): Hoàn thành bài giảng Tuần 02"
```
Script sẽ tự động:
1. Đọc tất cả thư mục trong `lectures/`.
2. Cập nhật bảng **Mục lục bài giảng** chuyên nghiệp tại [README.md](file:///E:/MinhVD/Github/Data_Analysis_with_Python/README.md).
3. Thực hiện `git add .`, `git commit` và `git push` trực tiếp lên GitHub repository.

---

## 🤖 3. Các câu lệnh mẫu tương tác với AI Assistant

- **Tạo bài giảng mới từ đầu:**
  > *"Soạn bài giảng Tuần 4 về Khám phá và Trực quan hóa dữ liệu với Matplotlib và Seaborn."*

- **Tạo riêng bài tập Lab:**
  > *"Tạo 5 bài tập thực hành kèm đáp án cho Tuần 6 về Tiền xử lý dữ liệu và Xử lý Missing values."*

- **Cập nhật & Xuất bản:**
  > *"Cập nhật lại bài giảng Tuần 1 và push tất cả lên GitHub."*

---

## 🌐 4. Thông tin Repository & Giảng viên
- **Giảng viên:** TS. Vũ Đức Minh (minhvd@neu.edu.vn)
- **Học phần:** Phân tích dữ liệu với Python (DSAI1005) - ĐH Kinh tế Quốc dân
- **GitHub Repository:** [vudmvn/Data_Analysis_with_Python](https://github.com/vudmvn/Data_Analysis_with_Python)
