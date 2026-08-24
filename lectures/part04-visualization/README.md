# Tuần 04: Khám phá & Trực quan hóa dữ liệu với Matplotlib (Data Visualization with Matplotlib)

## 🎯 Mục tiêu bài học (Learning Objectives)
- Nắm vững mô hình kiến trúc cốt lõi **Figure – Axes** và thành thạo trường phái lập trình hướng đối tượng (Object-Oriented API) trong Matplotlib.
- Thành thạo 5 loại biểu đồ nền tảng trong phân tích dữ liệu: **Line chart** (xu hướng), **Bar chart** (so sánh nhóm), **Scatter plot** (mối liên hệ), **Histogram & Box plot** (phân phối dữ liệu), và **Pie chart** (cơ cấu/tỷ trọng).
- Tùy biến toàn diện giao diện trực quan hóa: tiêu đề, nhãn trục, ticks, chú giải (legend), dải màu (colormap/colorbar), lưới (grid), chú thích mũi tên (annotations) và thiết lập định dạng số (`rcParams`, style sheets).
- Thiết kế và bố trí nhiều biểu đồ trên cùng một giao diện hiển thị thông qua `plt.subplots`, chia sẻ trục (`sharex`, `sharey`) và xây dựng Dashboard trực quan hóa đa chiều.
- Xây dựng các đồ thị nâng cao: Heatmap ma trận tương quan / cấu trúc dữ liệu thiếu, biểu đồ đường mức (Contour), bề mặt 3D (Surface Plot) và hoạt họa dữ liệu (Animation/Widgets).
- Tích hợp Matplotlib với **Pandas** và **Seaborn** trong quy trình phân tích dữ liệu khám phá (EDA) và xuất bản đồ thị chất lượng cao phục vụ báo cáo.

---

## 📁 Cấu trúc tài liệu (Directory Structure)

### 📘 Bài giảng & Slide (Lectures & Slides)
- **Tiếng Việt:**
  - `part04-matplotlib-vn.tex`: Mã nguồn LaTeX Beamer của slide bài giảng (*Từ biểu đồ cơ bản đến quy trình phân tích dữ liệu có thể tái lập*).
  - `part04-matplotlib-vn.pdf`: Slide bài giảng định dạng PDF chất lượng cao.
  - `figures_annarbor/`: Thư mục chứa tài nguyên đồ thị và biểu đồ minh họa nhúng trong slide.

### 💻 Bài tập thực hành (Lab Notebooks & Projects)
- **Tiếng Việt:**
  - `part04-matplotlib-practice-vn.ipynb`: Hướng dẫn thực hành toàn diện 19 chủ đề từ cơ bản đến nâng cao (Mô hình Figure-Axes, 5 biểu đồ cơ bản, tùy biến nâng cao, Dashboard subplots, Heatmap, Contour, 3D, tích hợp Pandas/Seaborn, cheat sheet và bài tập kiểm tra).
  - `part04-matplotlib-exercies-vn.ipynb`: Project thực hành phân tích trực quan hóa tổng hợp gồm 4 Mini-Projects thực tế:
    1. **Mini-Project 1 (Business):** Phân tích xu hướng doanh thu, hiệu quả khu vực và lợi nhuận bán hàng.
    2. **Mini-Project 2 (Economics):** Khám phá đường cong Phillips, lạm phát, thất nghiệp và suy thoái kinh tế.
    3. **Mini-Project 3 (Data Science):** Trực quan hóa hành vi Churn của khách hàng, mất cân bằng lớp và phân tích đa biến.
    4. **Mini-Project 4 (Business + Economics):** Phân tích đường cầu (Demand Curve), tối ưu hóa doanh thu và định giá sản phẩm (Pricing Strategy).

---

## 🚀 Hướng dẫn học tập (Study Guide)
1. **Theo dõi Slide bài giảng:** Đọc slide `part04-matplotlib-vn.pdf` để nắm vững lý thuyết và các nguyên tắc thiết kế trực quan hóa chuẩn mực.
2. **Thực hành từng bước:** Chạy từng cell trong notebook `part04-matplotlib-practice-vn.ipynb`, tự hoàn thành các bài tập nhỏ sau mỗi phần để làm chủ cú pháp Matplotlib.
3. **Thực hiện Project:** Giải quyết trọn vẹn 4 Mini-Projects trong notebook `part04-matplotlib-exercies-vn.ipynb` nhằm rèn luyện tư duy phân tích dữ liệu bằng hình ảnh trong bài toán kinh doanh, kinh tế và khoa học dữ liệu.
