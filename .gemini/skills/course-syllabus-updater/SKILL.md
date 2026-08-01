---
name: course-syllabus-updater
description: Skill chuyên tự động tổng hợp, cập nhật và đồng bộ file README.md / syllabus giới thiệu môn học Phân tích dữ liệu với Python (DSAI1005). Tự động tạo bảng ma trận liên kết động tới tất cả các bài giảng (.ipynb, .md), slide (.md), bài tập lab, đáp án, tệp dữ liệu (data/) và hình ảnh (images/) cho cả 15 tuần học. Kích hoạt khi người dùng yêu cầu cập nhật trang chủ, cập nhật syllabus, đồng bộ bảng bài giảng hoặc cập nhật link tài liệu học phần.
---

# Skill: Cập nhật File Markdown Giới thiệu Môn học & Syllabus (Course Portal Updater)

Skill này hỗ trợ tự động duy trì và cập nhật tệp **`README.md`** (Trang chủ Cổng thông tin học phần) cho môn **Phân tích dữ liệu với Python (DSAI1005)** - Giảng viên: TS. Vũ Đức Minh (ĐH Kinh tế Quốc dân).

---

## 🎯 1. Nhiệm vụ chính của Skill

1. **Tổng hợp Thông tin Môn học & Syllabus**: Trích xuất dữ liệu từ `syllabus-vn.md` để trình bày thông tin chung, chuẩn đầu ra (CLOs), quy định đánh giá và lộ trình 15 tuần.
2. **Xây dựng Bảng Ma trận Ma trận Liên kết Động (Dynamic Course Matrix)**: Quét tự động thư mục `lectures/` và xây dựng bảng liên kết trực tiếp tới:
   - Bài giảng Jupyter Notebook (`lecture.ipynb`)
   - Bài đọc / Ghi chép lý thuyết bổ sung (`.md` như `phan_tich_du_lieu_la_gi.md`)
   - Slide bài giảng (`slides.md`)
   - Bài tập Lab dành cho sinh viên (`lab_exercise.ipynb`)
   - Đáp án chi tiết cho giảng viên (`lab_solution.ipynb`)
   - Thư mục Dữ liệu (`data/`) & Hình ảnh minh họa (`images/`)
3. **Cập nhật Trạng thái Tiến độ (Progress Tracker)**:
   - Các tuần đã có bài giảng: Hiển thị đầy đủ link tải/xem tài liệu.
   - Các tuần chưa soạn: Hiển thị trạng thái ⏳ *Đang biên soạn*.

---

## 📑 2. Cấu trúc Tiêu chuẩn của File Trang chủ (`README.md`)

File `README.md` môn học luôn được duy trì với đầy đủ 6 phần chính:

```markdown
# 🐍 DSAI1005 – Phân tích dữ liệu với Python (Data Analysis with Python)

> **Giảng viên:** TS. Vũ Đức Minh (`minhvd@neu.edu.vn`)  
> **Đơn vị:** Khoa Khoa học dữ liệu và Trí tuệ nhân tạo, Trường Đại học Kinh tế Quốc dân (NEU)  
> **Chương trình:** Data Science in Finance and E-commerce (EP15)  

---

## 📌 1. Giới thiệu Học phần & Mục tiêu
(Trích xuất từ syllabus-vn.md)

## 🗺️ 2. Lộ trình Đào tạo 15 Tuần (Syllabus Roadmap)
(Bảng tóm tắt lộ trình 15 tuần)

## 📚 3. Ma trận Bài giảng, Tài liệu & Bài tập Thực hành (Course Hub)
(Bảng liên kết động tự động được cập nhật từ thư mục `lectures/`)

## 🛠️ 4. Hướng dẫn Môi trường & Cài đặt (Setup Guide)
(Hướng dẫn cài đặt Anaconda, JupyterLab, Pandas, NumPy, Seaborn...)

## 📊 5. Trực quan hóa & Hình ảnh Minh họa Môn học
(Link dẫn tới thư mục images/ và sơ đồ môn học)

## 📝 6. Hướng dẫn Đóng góp & Quy trình Soạn bài giảng
(Link dẫn tới QUY_TRINH_SOAN_BAI_GIANG.md)
```

---

## ⚡ 3. Quy trình Cập nhật & Tự động hóa

Khi người dùng ra lệnh:
> *"Cập nhật file README/Syllabus môn học"*  
> hoặc  
> *"Đồng bộ lại danh sách bài giảng và link thực hành trên trang chủ"*

Agent sẽ thực hiện:
1. Đọc nội dung cập nhật từ `syllabus-vn.md`.
2. Chạy script `python scripts/publish_lecture.py --no-push` để quét toàn bộ thư mục trong `lectures/` và cập nhật lại bảng ma trận bài giảng trên `README.md`.
3. Kiểm tra tính hợp lệ của tất cả các liên kết tương đối (relative links).
4. Đẩy bản cập nhật mới nhất lên GitHub bằng lệnh:
   ```bash
   python scripts/publish_lecture.py -m "docs(readme): Đồng bộ syllabus và bảng ma trận bài giảng 15 tuần"
   ```

---

## 🛠️ 4. Lệnh Thường Dùng (Usage Prompts)

- **Cập nhật lại toàn bộ README.md:**
  > *"Cập nhật lại file README môn học chứa syllabus đầy đủ 15 tuần và tất cả các link bài giảng, bài thực hành đã soạn."*

- **Thêm bài đọc bổ sung vào bảng mục lục:**
  > *"Thêm bài đọc phan_tich_du_lieu_la_gi.md của Tuần 1 vào bảng ma trận bài giảng trên README.md và push lên GitHub."*
