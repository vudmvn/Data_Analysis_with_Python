# Quy trình Soạn bài giảng, Quản lý Hình ảnh & Xuất bản lên GitHub (Phân tích dữ liệu với Python - DSAI1005)

Tài liệu này hướng dẫn chi tiết quy trình chuẩn bị bài giảng, tạo tài liệu thực hành (Jupyter Notebooks, Slides), sinh/quản lý dữ liệu và hình ảnh minh họa trong thư mục `images/`, đồng thời tự động xuất bản lên GitHub bằng công cụ **Antigravity Skill** và các bộ script hỗ trợ.

---

## 🏗️ 1. Cấu trúc Quản lý Bài giảng trong Repository

Mỗi tuần học sẽ nằm trong một thư mục riêng biệt tại đường dẫn `lectures/week-XX-<ten-chu-de>`:

```text
Data_Analysis_with_Python/
├── skills/                         # THƯ MỤC QUẢN LÝ TẤT CẢ CUSTOM SKILLS
│   ├── python-lecture-prep/        # Skill chuẩn bị bài giảng, lab & quản lý ảnh
│   │   └── SKILL.md
│   └── course-syllabus-updater/    # Skill cập nhật trang chủ syllabus & ma trận bài giảng
│       └── SKILL.md
├── lectures/
│   ├── part01-gioi-thieu-hoc-phan/
│   │   ├── README.md               # Tóm tắt lý thuyết & chỉ dẫn tuần 1 (Dùng link images/...)
│   │   ├── slides.md               # Slide bài giảng (định dạng Marp, dùng link images/...)
│   │   ├── lecture.ipynb           # Notebook bài giảng lý thuyết + minh họa
│   │   ├── lab_exercise.ipynb      # Notebook bài tập thực hành sinh viên
│   │   ├── lab_solution.ipynb      # Notebook đáp án cho giảng viên/trợ giảng
│   │   ├── data/                   # Bộ dữ liệu dùng trong tuần 1
│   │   └── images/                 # THƯ MỤC LƯU HÌNH ẢNH MINH HỌA CỦA TUẦN 1
│   │       ├── overview.png
│   │       └── diagram.png
│   └── week-02-numpy-pandas/
├── scripts/
│   ├── create_lecture.py           # Script khởi tạo khung bài giảng mới
│   └── publish_lecture.py          # Script tự động cập nhật README & push GitHub
├── syllabus-vn.md                  # Đề cương chi tiết học phần DSAI1005
└── README.md                       # Trang chủ repo + Mục lục bài giảng
```

---

## 🖼️ 2. Quy chuẩn Quản lý, Căn giữa & Bảo vệ Hình ảnh (Image Preservation & Centering Rules)

1. **Vị trí lưu trữ**: Tất cả ảnh minh họa, sơ đồ, infographic hoặc biểu đồ được tạo/export cho tuần học nào sẽ nằm trong thư mục `lectures/week-XX-<slug>/images/`.
2. **Quy tắc Không Ghi đè & Tự động Đổi tên (No-Overwrite & Auto-Rename Rule)**:
   - **Tuyệt đối không xóa hoặc ghi đè** lên các tệp ảnh đã tồn tại trong thư mục `images/`.
   - Nếu tên tệp ảnh mới định lưu bị trùng tên với tệp ảnh đã có sẵn, Antigravity Skill sẽ tự động thêm số thứ tự phân biệt (ví dụ `image-1.png`, `image-2.png` hoặc `chart-v2.png`) để đảm bảo không làm mất ảnh cũ.
3. **Quy tắc Bắt buộc Căn giữa (Image Centering Rule)**:
   - **TẤT CẢ HÌNH ẢNH** trong các tệp Markdown (`README.md`, `slides.md`, các bài đọc `.md`) và Notebook (`.ipynb`) **PHẢI ĐƯỢC CĂN GIỮA (CENTERED)** để hiển thị trực quan và đẹp mắt.
   - Cú pháp HTML Căn giữa Chuẩn:
     ```html
     <p align="center">
       <img src="images/ten-anh.png" alt="Mô tả hình ảnh" width="800" />
     </p>
     ```
4. **Tự động hóa**: Antigravity Skill sẽ tự động chuyển tệp ảnh vào `images/`, đổi tên chống trùng, căn giữa ảnh và cập nhật lại đường dẫn tương đối chính xác trong các tệp `.md` và `.ipynb`.

5. **Quy tắc Cập nhật Ngày chỉnh sửa (Auto Last-Updated Date Rule)**:
   - Mỗi tệp bài giảng Markdown (`.md`) bắt buộc phải có dòng thông tin ngày cập nhật ngay dưới tiêu đề bài học.
   - Khi tạo mới bài giảng hoặc bất kỳ khi nào chỉnh sửa, cập nhật nội dung của tệp bài giảng `.md`, Antigravity Skill sẽ tự động cập nhật dòng ngày này về ngày hiện tại (`**Cập nhật lần cuối:** <ngày> tháng <tháng> năm <năm>` cho Tiếng Việt hoặc `**Last updated:** <Month> <Day>, <Year>` cho Tiếng Anh).

6. **Quy chuẩn Slide TeX/PDF (.tex ➔ .pdf)**:
   - **Kiểm tra đường dẫn ảnh trong `.tex`:** Mọi hình ảnh chèn vào Slide LaTeX Beamer phải được đối chiếu tồn tại thực tế tại thư mục `images/`. Macro `\imageplaceholder` được thiết lập tự động render hình ảnh thật qua `\IfFileExists`.
   - **Biên dịch XeLaTeX & Xóa tệp tạm:** Biên dịch bằng `xelatex -interaction=nonstopmode <filename>.tex` (2 lượt). Ngay sau khi xuất xong tệp PDF, Antigravity Skill **bắt buộc dọn dẹp xóa các tệp tạm** (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc`, `.vrb`) để repo luôn sạch sẽ.

7. **Quy tắc Cập nhật Link Slide PDF vào `README.md` & `README-en.md` (Anti-404 Docsify Link)**:
   - Cập nhật liên kết slide PDF vào ô Slide thuộc bảng Ma trận bài giảng ở cả 2 tệp `README.md` và `README-en.md`.
   - **Bắt buộc dùng thẻ HTML `target="_blank"`:** Do trang web Docsify là ứng dụng Single Page (SPA), liên kết tệp PDF phải sử dụng dạng `<a href="lectures/.../partXX_lecture_X.pdf" target="_blank">PDF</a>` để trình duyệt mở trực tiếp tệp PDF trên tab mới, tránh lỗi 404 Not Found từ Docsify router.

---

## ⚡ 3. Quy trình Soạn Bài giảng Chi tiết

### Bước 1: Khởi tạo khung bài giảng tuần mới
Chạy script Python để sinh nhanh bộ file mẫu (bao gồm cả thư mục `images/` và `data/`):
```bash
python scripts/create_lecture.py --week <Số_tuần> --title "<Tên_chủ_đề>"
```
*Ví dụ:*
```bash
python scripts/create_lecture.py --week 2 --title "Thư viện tính toán NumPy và Pandas"
```

### Bước 2: Nhờ AI Assistant (Antigravity Agent) biên soạn nội dung
Khi Antigravity được kích hoạt, bạn chỉ cần ra lệnh cho AI bằng tiếng Việt:
> *"Soạn bài giảng Tuần 2 về NumPy và Pandas theo đề cương syllabus-vn.md. Tạo thêm sơ đồ minh họa quy trình làm sạch dữ liệu đặt vào folder images và nhúng đường dẫn tương đối vào file slides.md."*

Agent sẽ tự động đọc `syllabus-vn.md`, áp dụng `python-lecture-prep` skill để:
1. Điền lý thuyết chi tiết vào `lecture.ipynb` & `slides.md`.
2. Lưu các bức ảnh minh họa vào `images/` và chèn đường dẫn `images/<filename>` vào các file `.md`.
3. Tạo mã nguồn ví dụ (có chú thích Tiếng Việt, chuẩn PEP8).
4. Tạo dữ liệu giả lập chất lượng cao lưu vào thư mục `data/`.
5. Tạo bài tập thực hành `lab_exercise.ipynb` và đáp án `lab_solution.ipynb`.

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

## 🤖 4. Các câu lệnh mẫu tương tác với AI Assistant

- **Tạo bài giảng mới có hình ảnh:**
  > *"Soạn bài giảng Tuần 4 về Khám phá và Trực quan hóa dữ liệu với Matplotlib và Seaborn. Lưu các biểu đồ mẫu vào folder images và cập nhật đường dẫn trong slides.md."*

- **Tạo riêng bài tập Lab:**
  > *"Tạo 5 bài tập thực hành kèm đáp án cho Tuần 6 về Tiền xử lý dữ liệu và Xử lý Missing values."*

- **Cập nhật & Xuất bản:**
  > *"Cập nhật lại bài giảng Tuần 1 và push tất cả lên GitHub."*

---

## 🌐 5. Thông tin Repository & Giảng viên
- **Giảng viên:** TS. Vũ Đức Minh (minhvd@neu.edu.vn)
- **Học phần:** Phân tích dữ liệu với Python (DSAI1005) - ĐH Kinh tế Quốc dân
- **GitHub Repository:** [vudmvn/Data_Analysis_with_Python](https://github.com/vudmvn/Data_Analysis_with_Python)
