# Giới thiệu Khám phá & Trực quan hóa dữ liệu với Matplotlib và Seaborn

**Cập nhật lần cuối:** 26 tháng 8 năm 2026  
**Ngôn ngữ:** Tiếng Việt  
**Học phần:** Phân tích dữ liệu với Python (DSAI1005)  
**Chủ đề:** Trực quan hóa dữ liệu tĩnh, thống kê, đa biến với Matplotlib & Seaborn phục vụ Data Science, Business và Economics

---

## 1. Giới thiệu bài học

Trong kỷ nguyên số, dữ liệu được sinh ra với tốc độ chóng mặt và khối lượng khổng lồ. Tuy nhiên, một bảng dữ liệu thô chứa hàng triệu con số hay hàng chục ngàn dòng bản ghi lại vượt quá khả năng xử lý nhận thức trực tiếp của não bộ con người. Trực quan hóa dữ liệu (**Data Visualization**) chính là cây cầu chuyển hóa những ma trận số liệu phức tạp thành các mẫu hình hình học (đường nét, hình khối, màu sắc, vị trí) mà thị giác con người có thể tiếp nhận và phân tích trong vài phần trăm giây.

Trực quan hóa không chỉ là bước "trang trí đồ họa" ở cuối dự án, mà đóng vai trò chủ đạo xuyên suốt 3 giai đoạn của quy trình Khoa học Dữ liệu:
1. **Khám phá dữ liệu (Exploratory Data Analysis - EDA):** Tìm kiếm cấu trúc dữ liệu, nhận diện quy luật tiềm ẩn, phát hiện giá trị dị biệt (*outliers*) và kiểm tra tính toàn vẹn của dữ liệu trước khi lập mô hình.
2. **Kiểm định giả thuyết (Hypothesis Confirmation):** Kiểm tra trực quan các giả định thống kê về phân phối chuẩn, tính tuyến tính và hiện tượng đa cộng tuyến.
3. **Kể chuyện và Truyền thông kết quả (Data Storytelling & Reporting):** Truyền tải thông điệp kinh doanh và khuyến nghị hành động đến các nhà quản trị một cách thuyết phục, dễ hiểu và trung thực.

Trong hệ sinh thái Python, **Matplotlib** và **Seaborn** tạo nên cặp công cụ bổ trợ hoàn hảo:

```text
   ┌─────────────────────────────────────────────────────────┐
   │             Pandas: Dữ liệu dạng bảng (DataFrame)       │
   └────────────────────────────┬────────────────────────────┘
                                │
                                ▼
   ┌─────────────────────────────────────────────────────────┐
   │        Seaborn: Trực quan hóa thống kê bậc cao          │
   │   (Tự động hóa tính toán thống kê, dải tin cậy 95%)     │
   └────────────────────────────┬────────────────────────────┘
                                │
                                ▼
   ┌─────────────────────────────────────────────────────────┐
   │         Matplotlib: Nền tảng đồ họa cốt lõi             │
   │  (Kiểm soát chi tiết từng pixel, trục tọa độ, nhãn dán) │
   └────────────────────────────┬────────────────────────────┘
                                │
                                ▼
   ┌─────────────────────────────────────────────────────────┐
   │    Đầu ra trực quan: Figure / Axes / PNG / PDF / SVG    │
   └─────────────────────────────────────────────────────────┘
```

---

## 2. Mục tiêu học tập

Sau khi nghiên cứu bài học và hoàn thành các bài thực hành, người học sẽ làm chủ được các năng lực sau:

1. **Hiểu sâu mô hình phân cấp đồ họa:** Nắm vững kiến trúc cốt lõi **Figure – Axes – Axis** và thành thạo trường phái lập trình hướng đối tượng (**Object-Oriented API**) trong Matplotlib.
2. **Lựa chọn chính xác 5 loại biểu đồ nền tảng:**
   - **Line chart:** Khám phá xu hướng theo thời gian và biến động chu kỳ.
   - **Bar chart:** So sánh quy mô và độ lớn giữa các nhóm danh mục rời rạc.
   - **Scatter plot:** Phân tích tương quan và mối liên hệ giữa hai biến định lượng liên tục.
   - **Histogram & Box plot:** Đánh giá hình dạng phân phối, độ lệch, trung vị và nhận diện giá trị ngoại lệ.
   - **Pie chart:** Thể hiện cơ cấu tỷ trọng thành phần một cách có chọn lọc.
3. **Thành thạo thư viện trực quan hóa thống kê Seaborn:**
   - Khai thác 6 họ biểu đồ chuyên sâu: Relational, Categorical, Distribution, Regression, Matrix và Multi-plot grids.
   - Hiểu rõ sự khác biệt giữa hai cấp độ hàm **Axes-level** và **Figure-level**.
4. **Tùy biến thẩm mỹ & Bố cục chuyên nghiệp:** Thiết lập bảng màu chuẩn (*palettes*), hệ thống phông chữ tiếng Việt, lưới hỗ trợ (*grid*), chú giải (*legend*) và chú thích dữ liệu (*annotations*).
5. **Thiết kế bảng điều khiển trực quan đa chiều (Dashboard):** Ghép nối nhiều đồ thị con trên cùng một giao diện hiển thị bằng `plt.subplots()`.
6. **Ứng dụng giải quyết bài toán thực tế:** Thực hành giải quyết các bài toán trong **Kinh doanh (Sales & Profitability)**, **Kinh tế học (Đường cong Phillips, Lạm phát, Thất nghiệp)** và **Khoa học dữ liệu (Customer Churn, Class Imbalance)**.
7. **Tuân thủ chuẩn mực đạo đức & thẩm mỹ:** Tối ưu hóa tỷ lệ dữ liệu/mực (*Data-Ink Ratio*), đảm bảo tính toàn vẹn của gốc tọa độ và thiết kế thân thiện với người khiếm thị màu (*Colorblind-friendly*).

---

## 3. Cấu trúc nội dung

Tài liệu được thiết kế theo lộ trình sư phạm từ nền tảng đến nâng cao:

- [Phần 1: Kiến trúc cốt lõi của Matplotlib (Figure & Axes)](#phần-1-kiến-trúc-cốt-lõi-của-matplotlib-figure--axes)
  - [1.1. Khái niệm Figure, Axes và Axis: Bản chất phân cấp đồ họa](#11-khái-niệm-figure-axes-và-axis-bản-chất-phân-cấp-đồ-họa)
  - [1.2. Hai trường phái lập trình: Tại sao nên chọn Object-Oriented API?](#12-hai-trường-phái-lập-trình-tại-sao-nên-chọn-object-oriented-api)
- [Phần 2: Năm loại biểu đồ nền tảng trong Matplotlib](#phần-2-năm-loại-biểu-đồ-nền-tảng-trong-matplotlib)
  - [2.1. Line Chart — Xu hướng và biến động theo chuỗi thời gian](#21-line-chart--xu-hướng-và-biến-động-theo-chuỗi-thời-gian)
  - [2.2. Bar Chart — So sánh đại lượng giữa các nhóm rời rạc](#22-bar-chart--so-sánh-đại-lượng-giữa-các-nhóm-rời-rạc)
  - [2.3. Scatter Plot — Mối liên hệ tương quan và quy luật phân tán](#23-scatter-plot--mối-liên-hệ-tương-quan-và-quy-luật-phân-tán)
  - [2.4. Histogram & Box Plot — Khám phá hình dạng phân phối và nhận diện ngoại lệ](#24-histogram--box-plot--khám-phá-hình-dạng-phân-phối-và-nhận-diện-ngoại-lệ)
  - [2.5. Pie Chart — Cơ cấu tỷ trọng và các khuyến cáo sử dụng thực tiễn](#25-pie-chart--cơ-cấu-tỷ-trọng-và-các-khuyến-cáo-sử-dụng-thực-tiễn)
- [Phần 3: Tùy biến chuyên sâu & Thiết kế Dashboard Subplots](#phần-3-tùy-biến-chuyên-sâu--thiết-kế-dashboard-subplots)
  - [3.1. Bố cục nhiều biểu đồ con: Xây dựng Dashboard quản trị](#31-bố-cục-nhiều-biểu-đồ-con-xây-dựng-dashboard-quản-trị)
  - [3.2. Định hướng thị giác với Chú thích điểm quan trọng (`ax.annotate`)](#32-định-hướng-thị-giác-với-chú-thích-điểm-quan-trọng-axannotate)
  - [3.3. So sánh đa chiều với Trục kép phụ (`ax.twinx`)](#33-so-sánh-đa-chiều-với-trục-kép-phụ-axtwinx)
  - [3.4. Xuất bản biểu đồ chuẩn in ấn và báo cáo học thuật (`fig.savefig`)](#34-xuất-bản-biểu-đồ-chuẩn-in-ấn-và-báo-cáo-học-thuật-figsavefig)
- [Phần 4: Trực quan hóa thống kê với Seaborn](#phần-4-trực-quan-hóa-thống-kê-với-seaborn)
  - [4.1. Triết lý thiết kế hướng DataFrame của Seaborn](#41-triết-lý-thiết-kế-hướng-dataframe-của-seaborn)
  - [4.2. Bản đồ kiến trúc: Phân biệt Axes-level API và Figure-level API](#42-bản-đồ-kiến-trúc-phân-biệt-axes-level-api-và-figure-level-api)
- [Phần 5: Các họ biểu đồ chuyên sâu trong Seaborn](#phần-5-các-họ-biểu-đồ-chuyên-sâu-trong-seaborn)
  - [5.1. Relational Plots: Khám phá quan hệ đa chiều giữa các biến liên tục](#51-relational-plots-khám-phá-quan-hệ-đa-chiều-giữa-các-biến-liên-tục)
  - [5.2. Categorical Plots: Phân tích và so sánh nhóm danh mục](#52-categorical-plots-phân-tích-và-so-sánh-nhóm-danh-mục)
  - [5.3. Distribution Plots: Khám phá mật độ xác suất và tích lũy](#53-distribution-plots-khám-phá-mật-độ-xác-suất-và-tích-lũy)
  - [5.4. Regression Plots: Mô hình hóa đường xu hướng và dải tin cậy](#54-regression-plots-mô-hình-hóa-đường-xu-hướng-và-dải-tin-cậy)
  - [5.5. Matrix Plots & Heatmap: Ma trận tương quan và cấu trúc dữ liệu thiếu](#55-matrix-plots--heatmap-ma-trận-tương-quan-và-cấu-trúc-dữ-liệu-thiếu)
  - [5.6. Multi-Plot Grids: Cái nhìn toàn cảnh từ trên cao với `pairplot` & `FacetGrid`](#56-multi-plot-grids-cái-nhìn-toàn-cảnh-từ-trên-cao-với-pairplot--facetgrid)
- [Phần 6: Ứng dụng thực tiễn trong Data Science, Business & Economics](#phần-6-ứng-dụng-thực-tiễn-trong-data-science-business--economics)
  - [6.1. Business Analytics: Doanh thu, Biên lợi nhuận & Tối ưu hóa định giá](#61-business-analytics-doanh-thu-biên-lợi-nhuận--tối-ưu-hóa-định-giá)
  - [6.2. Economics: Khám phá Đường cong Phillips và Chu kỳ kinh tế vĩ mô](#62-economics-khám-phá-đường-cong-phillips-và-chu-kỳ-kinh-tế-vĩ-mô)
  - [6.3. Data Science & EDA: Phân tích Churn, Dữ liệu thiếu và Mất cân bằng nhãn](#63-data-science--eda-phân-tích-churn-dữ-liệu-thiếu-và-mất-cân-bằng-nhãn)
- [Phần 7: Bảng tra cứu lệnh nhanh (Cheat Sheet) & Nguyên tắc thiết kế](#phần-7-bảng-tra-cứu-lệnh-nhanh-cheat-sheet--nguyên-tắc-thiết-kế)
  - [7.1. Bảng đối chiếu cú pháp Matplotlib vs. Seaborn](#71-bảng-đối-chiếu-cú-pháp-matplotlib-vs-seaborn)
  - [7.2. Tùy biến Theme, Palette và Hỗ trợ Tiếng Việt](#72-tùy-biến-theme-palette-và-hỗ-trợ-tiếng-việt)
  - [7.3. Bộ quy tắc vàng thiết kế biểu đồ chuẩn mực](#73-bộ-quy-tắc-vàng-thiết-kế-biểu-đồ-chuẩn-mực)
- [Phần 8: Tài liệu học tập & Liên kết tham khảo](#8-tài-liệu-học-tập--liên-kết-tham-khảo)

---

# Phần 1. Kiến trúc cốt lõi của Matplotlib (Figure & Axes)

> **Lời dẫn dắt:**  
> Đa số người mới bắt đầu học trực quan hóa dữ liệu trong Python thường cảm thấy lúng túng khi muốn căn chỉnh lề, gộp nhiều biểu đồ hay đổi màu đường nét. Nguyên nhân cốt lõi là do họ chưa nắm vững **mô hình phân cấp đối tượng (Object Hierarchy)** của Matplotlib. Hiểu rõ kiến trúc nền tảng này sẽ giúp bạn hoàn toàn làm chủ việc bố cục và tinh chỉnh đồ thị một cách tự tin, không phụ thuộc vào việc "thử và sai".

## 1.1. Khái niệm Figure, Axes và Axis: Bản chất phân cấp đồ họa

Hãy tưởng tượng Matplotlib hoạt động tương tự như một họa sĩ vẽ tranh trong phòng trưng bày nghệ thuật:
- **`Figure` (Khung tranh tổng thể):** Là toàn bộ trang giấy vẽ, khung tranh hoặc cửa sổ ứng dụng. Nó quản lý kích thước (`figsize`), độ phân giải (`dpi`), màu nền và chứa tất cả các thành phần con.
- **`Axes` (Vùng vẽ thực sự / Khung đồ thị con):** Là ô vẽ nằm bên trong khung tranh. Một `Figure` có thể chứa 1 `Axes` đơn lẻ hoặc một lưới gồm 4, 6 hay 12 `Axes` khác nhau. Mỗi `Axes` là nơi diễn ra các hành vi vẽ (đường, cột, điểm) và sở hữu hệ trục tọa độ riêng biệt.
- **`Axis` (Trục đo lường số học):** Là các trục số $X$, $Y$ (hoặc $Z$ trong 3D) thuộc về một `Axes`. `Axis` quản lý phạm vi giá trị (`limits`), vạch chia nhỏ (`ticks`), nhãn vạch chia (`tick labels`) và tỷ lệ thang đo (tuyến tính hay logarit).

```text
+-------------------------------------------------------------------+
| Figure (Khung tranh bao quát toàn bộ)                             |
|                                                                   |
|   Figure Super Title (fig.suptitle)                               |
|   +-----------------------------+   +--------------------------+  |
|   | Axes 1 (ax1)                |   | Axes 2 (ax2)             |  |
|   | Y-Axis                      |   | Y-Axis                   |  |
|   |  ^                          |   |  ^                       |  |
|   |  |   [Line/Bar/Scatter]     |   |  |   [Histogram/Box]     |  |
|   |  +------------------> X-Axis|   |  +----------------> X-Axis| |
|   +-----------------------------+   +--------------------------+  |
|                                                                   |
+-------------------------------------------------------------------+
```

> ⚠️ **Lưu ý nhận diện:** Trong tiếng Anh, `Axes` là số nhiều của `Axis`, nhưng trong thuật ngữ Matplotlib, **một đối tượng `Axes` là một khung biểu đồ con cụ thể**. Nhầm lẫn giữa `Figure` và `Axes` là nguyên nhân của 90% lỗi phát sinh khi người học điều chỉnh bố cục.

---

## 1.2. Hai trường phái lập trình: Tại sao nên chọn Object-Oriented API?

Trong lịch sử phát triển, Matplotlib được tạo ra nhằm cung cấp giao diện tương tự phần mềm MATLAB cho cộng đồng khoa học kỹ thuật. Do đó, thư viện hỗ trợ 2 phong cách lập trình song song:

### 1. Trường phái Hướng đối tượng (Object-Oriented API - Chuẩn mực bắt buộc trong Data Science)
Ở phong cách này, ta luôn khởi tạo tường minh cặp đối tượng `fig, ax = plt.subplots()`, sau đó gọi các phương thức trực tiếp trên biến `ax` (như `ax.plot()`, `ax.set_title()`, `ax.set_xlabel()`).

*Ưu điểm vượt trội:*
- **Tính tường minh:** Luôn biết chính xác lệnh vẽ đang tác động lên khung đồ thị con nào.
- **Dễ kiểm soát bố cục phức tạp:** Thuận tiện khi vẽ lưới Dashboard $2 \times 2$ hay $3 \times 3$.
- **Dễ đóng gói thành hàm:** Dễ dàng viết các hàm vẽ tái sử dụng trong các pipeline phân tích tự động.

```python
import matplotlib.pyplot as plt

# Khởi tạo tường minh Figure và Axes
fig, ax = plt.subplots(figsize=(8, 4), dpi=100)

# Thực thi vẽ trực tiếp trên Axes
ax.plot([1, 2, 3, 4], [10, 25, 18, 30], color="#1F5AA6", marker="o", linewidth=2, label="Doanh thu thực tế")

# Thiết lập các thuộc tính của Axes
ax.set_title("Xu hướng Doanh thu theo Quý (Năm tài chính 2026)", fontsize=12, fontweight="bold")
ax.set_xlabel("Quý trong năm")
ax.set_ylabel("Triệu VNĐ")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(frameon=True)

plt.tight_layout()
plt.show()
```

### 2. Trường phái Trạng thái hàm (Pyplot State-based API)
Mô phỏng cơ chế ngầm định của MATLAB thông qua các lệnh như `plt.plot()`, `plt.title()`. Matplotlib sẽ tự động theo dõi "biểu đồ hiện hành" ở hậu trường.

*Hạn chế:* Khi vẽ nhiều đồ thị con cùng lúc, người lập trình rất dễ gọi nhầm lệnh vào biểu đồ trước đó, làm mã nguồn trở nên khó đọc và khó bảo trì. Trong toàn bộ học phần DSAI1005, chúng ta **ưu tiên tuyệt đối trường phái Object-Oriented API**.

---

# Phần 2. Năm loại biểu đồ nền tảng trong Matplotlib

> **Lời dẫn dắt:**  
> Một trong những sai lầm phổ biến nhất trong phân tích dữ liệu là "vẽ biểu đồ vì thấy nó đẹp" thay vì dựa trên câu hỏi nghiên cứu. Mỗi loại biểu đồ được thiết kế với một mục đích hình học riêng biệt. Bảng ma trận dưới đây là kim chỉ nam giúp bạn ra quyết định lựa chọn biểu đồ chính xác:

| Loại biểu đồ | Phương thức Matplotlib | Kiểu biến số đầu vào | Câu hỏi phân tích trọng tâm |
|:---|:---|:---|:---|
| **Line Chart** | `ax.plot()` | Chuỗi thời gian / Số liên tục | *Biến số này đang tăng, giảm hay biến động chu kỳ theo thời gian như thế nào?* |
| **Bar Chart** | `ax.bar()`, `ax.barh()` | Phân loại (Categorical) vs Định lượng | *Độ lớn/doanh số giữa các nhóm danh mục chênh lệch nhau ra sao?* |
| **Scatter Plot** | `ax.scatter()` | 2 biến định lượng liên tục | *Hai biến số này có quan hệ đồng biến, nghịch biến hay phi tuyến tính với nhau không?* |
| **Histogram & Boxplot** | `ax.hist()`, `ax.boxplot()` | 1 hoặc nhiều biến định lượng | *Dữ liệu tập trung ở đâu, có đối xứng không, có xuất hiện điểm dị biệt (outlier) không?* |
| **Pie Chart** | `ax.pie()` | Danh mục rời rạc (tổng = 100%) | *Cơ cấu đóng góp của từng bộ phận chiếm bao nhiêu phần trăm trong tổng thể?* |

---

## 2.1. Line Chart — Xu hướng và biến động theo chuỗi thời gian

> **Bối cảnh ứng dụng:**  
> Line chart là công cụ số một khi trục hoành $X$ mang tính liên tục (đặc biệt là trục thời gian như ngày, tháng, quý, năm). Bằng cách nối các điểm dữ liệu bằng đoạn thẳng, Line chart kích hoạt khả năng nhận diện độ dốc và hướng đi của mắt người, làm nổi bật ngay lập tức các giai đoạn tăng trưởng, suy thoái hoặc tính mùa vụ.

Trong phân tích kinh doanh, việc vẽ đồng thời **Doanh thu** và **Chi phí** trên cùng một hệ trục giúp nhà quản trị dễ dàng quan sát điểm hòa vốn và vùng sinh lời:

```python
import matplotlib.pyplot as plt
import numpy as np

# Tạo chuỗi thời gian 12 tháng kinh doanh
months = np.arange(1, 13)
revenue = np.array([120, 135, 128, 145, 160, 155, 170, 190, 185, 210, 240, 280])
costs = np.array([90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150])

fig, ax = plt.subplots(figsize=(9, 4.5))

# Vẽ 2 đường xu hướng
ax.plot(months, revenue, marker="o", color="#1F5AA6", linewidth=2, label="Doanh thu")
ax.plot(months, costs, marker="s", color="#D1495B", linewidth=2, linestyle="--", label="Chi phí vận hành")

# Tô màu vùng lợi nhuận ròng giữa Doanh thu và Chi phí
ax.fill_between(months, revenue, costs, where=(revenue >= costs), color="#2A9D8F", alpha=0.15, label="Vùng lợi nhuận dương")

ax.set_title("Diễn biến Doanh thu và Chi phí qua 12 Tháng (Năm 2026)", fontsize=12, fontweight="bold")
ax.set_xlabel("Tháng trong năm")
ax.set_ylabel("Giá trị (Triệu VNĐ)")
ax.set_xticks(months)
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(frameon=True, loc="upper left")

plt.tight_layout()
plt.show()
```

---

## 2.2. Bar Chart — So sánh đại lượng giữa các nhóm rời rạc

> **Bối cảnh ứng dụng:**  
> Mắt người đặc biệt nhạy cảm với việc so sánh **chiều dài của các vật thể đặt song song trên cùng một đường cơ sở (baseline)** hơn là so sánh góc hoặc diện tích. Bar chart tận dụng tối đa cơ chế thị giác này để so sánh quy mô giữa các phòng ban, vùng thị trường hoặc danh mục sản phẩm.

> ⚠️ **Quy tắc đạo đức dữ liệu (Baseline Rule):**  
> Gốc trục đo lường của biểu đồ cột **bắt buộc phải bắt đầu từ số 0**. Nếu cắt xén gốc tọa độ (ví dụ bắt đầu từ 200 thay vì 0), sự khác biệt trực quan giữa các cột sẽ bị phóng đại quá mức, dẫn đến sai lệch nhận thức nghiêm trọng của người xem.

```python
regions = ["Miền Bắc", "Miền Trung", "Miền Nam", "Tây Nguyên"]
sales = [450, 280, 520, 160]
colors = ["#1F5AA6", "#E76F51", "#2A9D8F", "#F4A261"]

fig, ax = plt.subplots(figsize=(8, 4.2))
bars = ax.bar(regions, sales, color=colors, width=0.55, edgecolor="black", linewidth=0.6)

# Kỹ thuật Data Labeling: Ghi nhãn số liệu trực tiếp lên đầu cột
for bar in bars:
    height = bar.get_height()
    ax.annotate(f"{height:,.0f} tr",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points",
                ha="center", va="bottom", fontsize=9.5, fontweight="bold")

ax.set_title("Doanh số Bán hàng theo Vùng Thị trường (Quý 3/2026)", fontweight="bold")
ax.set_ylabel("Doanh số (Triệu VNĐ)")
ax.set_ylim(0, 620)
ax.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
```

---

## 2.3. Scatter Plot — Mối liên hệ tương quan và quy luật phân tán

> **Bối cảnh ứng dụng:**  
> Khi bạn muốn kiểm tra xem: *"Liệu tăng ngân sách quảng cáo có thực sự làm tăng doanh thu hay không?"* hoặc *"Tỷ lệ lạm phát tăng thì tỷ lệ thất nghiệp thay đổi như thế nào?"*, Scatter plot (biểu đồ phân tán) là công cụ khảo sát đầu tiên. Mỗi quan sát được biểu diễn bằng một điểm tọa độ $(x, y)$, giúp phát hiện quy luật đồng biến (tuyến tính thuận), nghịch biến (tuyến tính nghịch) hay phi tuyến (hình chữ U, đường cong bão hòa).

```python
np.random.seed(42)
ad_spend = np.random.uniform(15, 100, 45)
# Giả lập doanh thu phụ thuộc vào quảng cáo kèm nhiễu ngẫu nhiên
revenue = 60 + 2.8 * ad_spend + np.random.normal(0, 18, 45)

fig, ax = plt.subplots(figsize=(8, 4.5))

# Vẽ các điểm quan sát
ax.scatter(ad_spend, revenue, color="#2A9D8F", edgecolor="black", linewidth=0.7, alpha=0.85, s=65, label="Chiến dịch quảng cáo")

# Khớp và vẽ đường xu hướng tuyến tính (Linear Trendline)
slope, intercept = np.polyfit(ad_spend, revenue, 1)
x_line = np.linspace(ad_spend.min(), ad_spend.max(), 100)
ax.plot(x_line, slope * x_line + intercept, color="#D1495B", linestyle="--", linewidth=2,
        label=f"Đường xu hướng: y = {slope:.2f}x + {intercept:.1f}")

ax.set_title("Mối quan hệ giữa Ngân sách Quảng cáo & Doanh thu Thực tế", fontweight="bold")
ax.set_xlabel("Ngân sách quảng cáo (Triệu VNĐ)")
ax.set_ylabel("Doanh thu thực tế (Triệu VNĐ)")
ax.legend(frameon=True)
ax.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.show()
```

> 💡 **Ghi nhớ:** *Tương quan không đồng nghĩa với Nhân quả (Correlation is not Causation)*. Scatter plot giúp nhận diện mối liên hệ thống kê, nhưng việc khẳng định quan hệ nhân quả đòi hỏi phân tích kinh tế lượng và thiết kế thực nghiệm chuyên sâu.

---

## 2.4. Histogram & Box Plot — Khám phá hình dạng phân phối và nhận diện ngoại lệ

> **Bối cảnh ứng dụng:**  
> Các chỉ số trung bình (Mean) đơn thuần rất dễ đánh lừa nhà phân tích khi dữ liệu bị lệch (*skewed*) hoặc có sự xuất hiện của các giá trị ngoại lệ cực đoan (*outliers*). Bộ đôi **Histogram** và **Box Plot** là hai góc nhìn bổ trợ không thể thiếu:
> - **Histogram:** Cho thấy toàn cảnh mật độ tần suất, hình dáng phân phối (phân phối chuẩn hình chuông, lệch trái, lệch phải hay đa đỉnh).
> - **Box Plot (Biểu đồ hộp Tukey):** Cô đọng 5 con số tóm tắt thống kê ($Min, Q_1, Median, Q_3, Max$) và đánh dấu chính xác các điểm vượt ngưỡng $1.5 \times \text{IQR}$ là ngoại lệ tiềm năng.

```python
# Giả lập thời gian giao hàng (phân phối lệch phải Gamma)
delivery_time = np.random.gamma(shape=3.5, scale=8.0, size=600)

fig, (ax_hist, ax_box) = plt.subplots(1, 2, figsize=(11, 4.2))

# 1. Histogram kèm vạch Mean và Median
ax_hist.hist(delivery_time, bins=25, color="#1F5AA6", edgecolor="white", density=True, alpha=0.75)
ax_hist.axvline(np.mean(delivery_time), color="red", linestyle="--", linewidth=1.8, label=f"Mean: {np.mean(delivery_time):.1f}p")
ax_hist.axvline(np.median(delivery_time), color="orange", linestyle="-", linewidth=2, label=f"Median: {np.median(delivery_time):.1f}p")
ax_hist.set_title("1. Phân phối Thời gian giao hàng (Histogram)", fontweight="bold")
ax_hist.set_xlabel("Thời gian (Phút)")
ax_hist.set_ylabel("Mật độ xác suất")
ax_hist.legend()
ax_hist.grid(axis="y", linestyle=":", alpha=0.5)

# 2. Box Plot nhận diện giá trị ngoại lệ Outliers
ax_box.boxplot(delivery_time, vert=False, patch_artist=True,
               boxprops=dict(facecolor="#2A9D8F", color="black"),
               medianprops=dict(color="red", linewidth=2),
               flierprops=dict(marker="o", markerfacecolor="#E76F51", alpha=0.6))
ax_box.set_title("2. Cấu trúc Phân vị & Outliers (Box Plot)", fontweight="bold")
ax_box.set_xlabel("Thời gian (Phút)")
ax_box.grid(axis="x", linestyle=":", alpha=0.5)

plt.tight_layout()
plt.show()
```

---

## 2.5. Pie Chart — Cơ cấu tỷ trọng và các khuyến cáo sử dụng thực tiễn

> **Bối cảnh ứng dụng & Cảnh báo:**  
> Biểu đồ tròn (Pie chart) là một trong những biểu đồ hay bị lạm dụng nhất trong kinh doanh. Não bộ con người rất khó ước lượng và so sánh chính xác sự chênh lệch giữa các góc ở tâm hoặc diện tích hình quạt.

> 📌 **Quy tắc vàng khi dùng Pie Chart:**
> 1. **Chỉ dùng khi tổng các thành phần bằng 100%:** Tuyệt đối không dùng khi các nhóm có thể trùng lặp lựa chọn.
> 2. **Số lượng lát cắt $\le 5$:** Nếu có nhiều hơn 5 nhóm, hãy gom các nhóm nhỏ vào mục "Khác" hoặc chuyển hẳn sang dạng **Bar Chart**.
> 3. **Luôn hiển thị kèm tỷ lệ phần trăm (%):** Giúp người đọc nắm bắt con số chính xác mà không phải ước đoán bằng mắt.

```python
channels = ["E-commerce", "Cửa hàng bán lẻ", "Đại lý phân phối", "Bán sỉ B2B"]
shares = [42, 28, 18, 12]
colors = ["#1F5AA6", "#2A9D8F", "#F4A261", "#E76F51"]
explode = (0.06, 0, 0, 0)  # Tách nhẹ lát cắt lớn nhất để tạo điểm nhấn

fig, ax = plt.subplots(figsize=(6, 4.5))
ax.pie(shares, labels=channels, autopct="%1.1f%%", startangle=140,
       colors=colors, explode=explode, shadow=False,
       textprops={"fontsize": 9.5, "fontweight": "medium"})

ax.set_title("Cơ cấu Tỷ trọng Kênh Doanh thu (Năm 2026)", fontweight="bold")
plt.tight_layout()
plt.show()
```

---

# Phần 3. Tùy biến chuyên sâu & Thiết kế Dashboard Subplots

> **Lời dẫn dắt:**  
> Trong môi trường doanh nghiệp thực tế, các nhà quản lý không có thời gian mở 10 biểu đồ rời rạc để so sánh dữ liệu. Họ cần một **Bảng điều khiển trực quan tổng hợp (Executive Dashboard)** nằm gọn trên một trang báo cáo duy nhất. Phần này hướng dẫn bạn kỹ thuật tổ chức lưới đa đồ thị, chú thích định hướng thị giác và xuất bản biểu đồ chuẩn in ấn.

## 3.1. Bố cục nhiều biểu đồ con: Xây dựng Dashboard quản trị

Hàm `plt.subplots(nrows, ncols, figsize=(w, h))` trả về một mảng 2 chiều chứa các đối tượng `Axes`. Ta có thể truy cập từng ô bằng tọa độ chỉ mục `axes[row, col]`:

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 7.5))

# Ô (0, 0): Xu hướng Doanh thu
axes[0, 0].plot(months, revenue, color="#1F5AA6", marker="o", linewidth=2)
axes[0, 0].set_title("1. Xu hướng Doanh thu theo Tháng", fontweight="bold", fontsize=11)
axes[0, 0].set_xlabel("Tháng")
axes[0, 0].grid(True, linestyle=":", alpha=0.5)

# Ô (0, 1): Doanh số theo Vùng
axes[0, 1].bar(regions, sales, color=colors, edgecolor="black", linewidth=0.5)
axes[0, 1].set_title("2. Phân bổ Doanh số theo Vùng", fontweight="bold", fontsize=11)
axes[0, 1].grid(axis="y", linestyle=":", alpha=0.5)

# Ô (1, 0): Tương quan Quảng cáo vs Doanh thu
axes[1, 0].scatter(ad_spend, revenue, color="#2A9D8F", edgecolor="black", alpha=0.8)
axes[1, 0].set_title("3. Tương quan Quảng cáo - Doanh thu", fontweight="bold", fontsize=11)
axes[1, 0].set_xlabel("Ngân sách (Tr. VNĐ)")
axes[1, 0].grid(True, linestyle=":", alpha=0.5)

# Ô (1, 1): Phân phối Thời gian giao hàng
axes[1, 1].hist(delivery_time, bins=20, color="#E76F51", edgecolor="white", alpha=0.8)
axes[1, 1].set_title("4. Phân phối Thời gian Giao hàng", fontweight="bold", fontsize=11)
axes[1, 1].set_xlabel("Phút")
axes[1, 1].grid(axis="y", linestyle=":", alpha=0.5)

# Đặt tiêu đề lớn bao quát toàn bộ Dashboard
fig.suptitle("BÁO CÁO TỔNG QUAN HIỆU SUẤT HOẠT ĐỘNG KINH DOANH (DSAI1005)", fontsize=13, fontweight="bold", y=0.99)
plt.tight_layout()
plt.show()
```

---

## 3.2. Định hướng thị giác với Chú thích điểm quan trọng (`ax.annotate`)

> **Bối cảnh ứng dụng:**  
> Một biểu đồ tự giải thích (*Self-explanatory plot*) luôn có các điểm chú thích văn bản kèm mũi tên chỉ dẫn tới những mốc sự kiện quan trọng (đỉnh doanh thu mùa Tết, thời điểm sụt giảm do đứt gãy chuỗi cung ứng). Điều này giúp người xem nắm bắt ngay insight trọng tâm trong 3 giây đầu tiên.

```python
fig, ax = plt.subplots(figsize=(8.5, 4.2))
ax.plot(months, revenue, marker="o", color="#1F5AA6", linewidth=2.2)

# Thiết lập chú thích có mũi tên trỏ vào đỉnh tháng 12
ax.annotate("Mùa cao điểm Lễ hội & Tết\nĐạt đỉnh: 280 triệu VNĐ",
            xy=(12, 280), xytext=(7.5, 250),
            arrowprops=dict(facecolor="#D1495B", shrink=0.08, width=1.5, headwidth=8),
            fontsize=9.5, fontweight="bold", color="#D1495B",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF3CD", edgecolor="#D1495B", alpha=0.9))

ax.set_title("Biến động Doanh thu năm 2026 kèm Điểm nhấn Mùa vụ", fontweight="bold")
ax.set_xlabel("Tháng")
ax.set_ylabel("Triệu VNĐ")
ax.set_xticks(months)
ax.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.show()
```

---

## 3.3. So sánh đa chiều với Trục kép phụ (`ax.twinx`)

> **Bối cảnh ứng dụng:**  
> Khi cần biểu diễn đồng thời hai biến số có **thang đo và đơn vị hoàn toàn khác nhau** trên cùng một biểu đồ (ví dụ: *Doanh thu* tính bằng Tỷ VNĐ và *Biên lợi nhuận* tính bằng %), phương thức `ax.twinx()` cho phép tạo ra một trục tung thứ hai ở mép phải đồ thị.

```python
categories = ["Điện máy", "Gia dụng", "Thời trang", "Công nghệ", "Mỹ phẩm"]
revenue_cat = [520, 310, 290, 680, 220]      # Đơn vị: Tỷ VNĐ
profit_margin = [0.08, 0.22, 0.35, 0.12, 0.40] # Đơn vị: Tỷ lệ %

fig, ax1 = plt.subplots(figsize=(8.5, 4.5))

# Trục 1 (Bên trái): Cột Doanh thu
color1 = "#1F5AA6"
ax1.bar(categories, revenue_cat, color=color1, alpha=0.75, width=0.5, label="Doanh thu (Tỷ VNĐ)")
ax1.set_xlabel("Ngành hàng", fontweight="bold")
ax1.set_ylabel("Doanh thu (Tỷ VNĐ)", color=color1, fontweight="bold")
ax1.tick_params(axis="y", labelcolor=color1)
ax1.set_ylim(0, 800)

# Trục 2 (Bên phải): Đường Biên lợi nhuận
ax2 = ax1.twinx()
color2 = "#D1495B"
ax2.plot(categories, [p * 100 for p in profit_margin], color=color2, marker="s", linewidth=2.5, label="Biên lợi nhuận (%)")
ax2.set_ylabel("Biên Lợi nhuận (%)", color=color2, fontweight="bold")
ax2.tick_params(axis="y", labelcolor=color2)
ax2.set_ylim(0, 50)
ax2.grid(False) # Tắt grid trục 2 để tránh rối mắt

plt.title("Ma trận Doanh thu & Biên Lợi nhuận theo Ngành hàng (Dual Y-Axis)", fontweight="bold")
plt.tight_layout()
plt.show()
```

---

## 3.4. Xuất bản biểu đồ chuẩn in ấn và báo cáo học thuật (`fig.savefig`)

Để biểu đồ hiển thị sắc nét trong các ấn phẩm báo cáo khoa học, slide trình chiếu hoặc web:

```python
# 1. Lưu định dạng Raster (Ảnh bitmap độ phân giải cao 300 DPI)
fig.savefig("sales_report_2026.png", dpi=300, bbox_inches="tight")

# 2. Lưu định dạng Vector (Phóng to vô hạn không vỡ nét - dùng cho LaTeX / In ấn)
fig.savefig("sales_report_2026.pdf", bbox_inches="tight")
fig.savefig("sales_report_2026.svg", bbox_inches="tight")
```
- `dpi=300`: Đảm bảo mật độ điểm ảnh chuẩn in ấn chất lượng cao (*Dots Per Inch*).
- `bbox_inches='tight'`: Tự động cắt bỏ các khoảng trắng thừa ngoài rìa khung biểu đồ.

---

# Phần 4. Trực quan hóa thống kê với Seaborn

> **Lời dẫn dắt:**  
> Nếu Matplotlib là "chiếc cọ vẽ tự do" cho phép bạn can thiệp vào từng chi tiết nhỏ nhất, thì **Seaborn** là "bộ khuôn thống kê thông minh". Seaborn được xây dựng trực tiếp trên nền Matplotlib nhằm tối ưu hóa quy trình Phân tích Khám phá Dữ liệu (EDA) với các bộ dữ liệu dạng bảng (*Pandas DataFrame*).

## 4.1. Triết lý thiết kế hướng DataFrame của Seaborn

Trong Matplotlib, để vẽ biểu đồ phân nhóm (ví dụ: Doanh thu theo Tháng, tách biệt giữa Khách hàng Mới và Khách hàng Cũ), bạn phải tự viết vòng lặp lọc dữ liệu và cấu hình màu sắc thủ công. 

Ngược lại, Seaborn áp dụng nguyên lý **Ánh xạ Ngữ nghĩa (Semantic Mapping)**: Bạn chỉ cần chỉ định tên cột dữ liệu vào các tham số thị giác:
- `data=df`: DataFrame nguồn.
- `x='col_x'`, `y='col_y'`: Cột ánh xạ lên tọa độ.
- `hue='group_col'`: Tự động tách nhóm và gán bảng màu phân biệt.
- `style='group_col'`: Tự động đổi kiểu nét vẽ (liền, đứt nét) hoặc kiểu marker.
- `size='numeric_col'`: Tự động thay đổi kích thước điểm theo độ lớn biến số.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Thiết lập giao diện hiển thị chuẩn mực của Seaborn
sns.set_theme(style="whitegrid", font_scale=1.05)
```

---

## 4.2. Bản đồ kiến trúc: Phân biệt Axes-level API và Figure-level API

Hiểu rõ cấu trúc hai tầng API là điều cốt tử để làm chủ Seaborn mà không gặp lỗi bố cục:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Figure-level Functions                          │
│     (Tự quản lý toàn bộ Figure qua FacetGrid, tạo lưới đa chiều)       │
│                                                                        │
│       relplot()              displot()               catplot()         │
└───────────┬──────────────────────┬───────────────────────┬─────────────┘
            │                      │                       │
            ▼                      ▼                       ▼
┌──────────────────────┬───────────────────────┬─────────────────────────┐
│     Relational       │     Distributions     │       Categorical       │
│  (Axes-level Func)   │   (Axes-level Func)   │    (Axes-level Func)    │
│                      │                       │                         │
│ • scatterplot()      │ • histplot()          │ • barplot(), countplot()│
│ • lineplot()         │ • kdeplot(), ecdfplot │ • boxplot(), violinplot │
│                      │ • rugplot()           │ • stripplot, swarmplot  │
└──────────────────────┴───────────────────────┴─────────────────────────┘
```

1. **Hàm cấp độ Axes (Axes-level functions - `scatterplot`, `barplot`, `boxplot`, `histplot`, `heatmap`):**
   - Luôn nhận tham số `ax=...`.
   - Vẽ trực tiếp lên một ô `Axes` có sẵn, kết hợp hoàn hảo khi bạn dùng `fig, axes = plt.subplots()`.
2. **Hàm cấp độ Figure (Figure-level functions - `relplot`, `catplot`, `displot`, `pairplot`):**
   - Tự khởi tạo và kiểm soát toàn bộ `Figure` thông qua đối tượng `FacetGrid`.
   - Chuyên dùng để phân rã dữ liệu thành ma trận biểu đồ đa chiều bằng các tham số `col='col_name'` và `row='row_name'`.

---

# Phần 5. Các họ biểu đồ chuyên sâu trong Seaborn

> **Lời dẫn dắt:**  
> Seaborn tổ chức các công cụ trực quan hóa thành 6 họ biểu đồ thống kê chuyên biệt. Việc nắm vững từng họ biểu đồ giúp bạn nhanh chóng giải quyết mọi bài toán phân tích trong thực tế.

## 5.1. Relational Plots: Khám phá quan hệ đa chiều giữa các biến liên tục

> **Bối cảnh ứng dụng:**  
> Khảo sát mối tương quan đồng thời giữa 4 đến 5 biến số trong cùng một biểu đồ mà không làm rối mắt người xem:

```python
import seaborn as sns
tips = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(8.5, 4.8))
# Tích hợp đồng thời: Tổng hóa đơn (X), Tiền Tip (Y), Hút thuốc (Hue), Thời gian (Style), Quy mô bàn (Size)
sns.scatterplot(data=tips, x="total_bill", y="tip",
                hue="smoker", style="time", size="size",
                sizes=(40, 200), palette="Set1", alpha=0.85, ax=ax)

ax.set_title("Mối quan hệ Hóa đơn - Tiền Tip đa chiều", fontweight="bold")
ax.set_xlabel("Tổng hóa đơn ($)")
ax.set_ylabel("Tiền Tip ($)")
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left") # Đặt legend ra ngoài khung

plt.tight_layout()
plt.show()
```

---

## 5.2. Categorical Plots: Phân tích và so sánh nhóm danh mục

> **Bối cảnh ứng dụng:**  
> Khi biến $X$ là biến định tính (nhóm phân loại) và biến $Y$ là biến định lượng liên tục, Seaborn cung cấp 4 góc nhìn từ cơ bản đến nâng cao:
> 1. `countplot()`: Đếm tần suất xuất hiện của từng nhóm.
> 2. `barplot()`: So sánh **giá trị trung bình (mean)** kèm dải sai số khoảng tin cậy 95% (*95% bootstrap CI*).
> 3. `boxplot()`: Tóm tắt 5 số thống kê và xác định ngoại lệ.
> 4. `violinplot()`: Kết hợp Box plot với đường cong mật độ phân phối đối xứng (KDE).

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

# 1. Barplot ước lượng Tip trung bình kèm khoảng tin cậy 95%
sns.barplot(data=tips, x="day", y="tip", hue="sex", palette="muted", errorbar="ci", ax=axes[0])
axes[0].set_title("1. Tiền Tip Trung bình theo Ngày & Giới tính (95% CI)", fontweight="bold")
axes[0].set_xlabel("Ngày trong tuần")
axes[0].set_ylabel("Tip trung bình ($)")

# 2. Violinplot phân phối Total Bill theo ngày tách biệt theo nhóm hút thuốc
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker", split=True, palette="pastel", ax=axes[1])
axes[1].set_title("2. Phân phối Tổng hóa đơn (Split Violin Plot)", fontweight="bold")
axes[1].set_xlabel("Ngày trong tuần")
axes[1].set_ylabel("Tổng hóa đơn ($)")

plt.tight_layout()
plt.show()
```

---

## 5.3. Distribution Plots: Khám phá mật độ xác suất và tích lũy

> **Bối cảnh ứng dụng:**  
> Trong nhiều trường hợp, việc phân nhóm theo bin của Histogram truyền thống có thể che giấu những biến động cục bộ của dữ liệu. Phương thức `kdeplot()` (Kernel Density Estimation) làm mượt phân phối thành đường cong mật độ xác suất liên tục:

```python
fig, ax = plt.subplots(figsize=(8.5, 4.2))
sns.histplot(data=tips, x="total_bill", hue="time", kde=True, bins=25,
             palette="viridis", alpha=0.4, element="step", ax=ax)

ax.set_title("Phân phối Tổng hóa đơn: Bữa Trưa (Lunch) vs Bữa Tối (Dinner)", fontweight="bold")
ax.set_xlabel("Tổng hóa đơn ($)")
ax.set_ylabel("Tần suất quan sát")

plt.tight_layout()
plt.show()
```

---

## 5.4. Regression Plots: Mô hình hóa đường xu hướng và dải tin cậy

> **Bối cảnh ứng dụng:**  
> Trong kinh tế lượng và khoa học dữ liệu, việc kiểm tra sơ bộ mối liên hệ tuyến tính trước khi xây dựng mô hình hồi quy là bước bắt buộc. `sns.regplot()` tự động khớp mô hình hồi quy bình phương tối thiểu ($OLS$) và tính toán dải bóng mờ biểu thị khoảng tin cậy 95%:

```python
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.regplot(data=tips, x="total_bill", y="tip",
            scatter_kws={"alpha": 0.6, "color": "#1F5AA6"},
            line_kws={"color": "#D1495B", "linewidth": 2.2}, ax=ax)

ax.set_title("Đường Hồi quy Tuyến tính: Tiền Tip theo Tổng Hóa đơn ( kèm 95% CI)", fontweight="bold")
ax.set_xlabel("Tổng hóa đơn ($)")
ax.set_ylabel("Tiền Tip ($)")

plt.tight_layout()
plt.show()
```

---

## 5.5. Matrix Plots & Heatmap: Ma trận tương quan và cấu trúc dữ liệu thiếu

> **Bối cảnh ứng dụng:**  
> Khi bước vào một tập dữ liệu mới có 20–30 cột, làm thế nào để biết những biến nào có liên quan chặt chẽ với nhau? **Heatmap ma trận tương quan Pearson** là công cụ EDA nhanh nhất giúp phát hiện hiện tượng đa cộng tuyến (*Multicollinearity*) và xác định các đặc trưng tiềm năng cho mô hình Machine Learning:

```python
import numpy as np

# Lọc các biến định lượng và tính ma trận hệ số tương quan
numeric_df = tips.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()

fig, ax = plt.subplots(figsize=(7, 5.2))
# Dùng colormap phân kỳ coolwarm với điểm cân bằng ở 0
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1,
            linewidths=1, linecolor="white", cbar_kws={"shrink": 0.85}, ax=ax)

ax.set_title("Ma trận Hệ số Tương quan Tuyến tính Pearson", fontweight="bold")
plt.tight_layout()
plt.show()
```

---

## 5.6. Multi-Plot Grids: Cái nhìn toàn cảnh từ trên cao với `pairplot` & `FacetGrid`

> **Bối cảnh ứng dụng:**  
> Thay vì viết hàng chục dòng lệnh để khảo sát từng cặp biến, `sns.pairplot()` cung cấp "cái nhìn từ trên cao" (*Bird's-eye view*), tự động tạo ra một ma trận biểu đồ phân tán cho tất cả các cặp biến số liên tục, đồng thời vẽ phân phối đơn biến trên đường chéo chính:

```python
iris = sns.load_dataset("iris")

# Vẽ ma trận phân tán toàn diện phân loại theo loài hoa
g = sns.pairplot(iris, hue="species", palette="Set2", corner=True, diag_kind="kde")
g.fig.suptitle("Ma trận Khám phá Cặp biến Toàn diện (Pairplot Iris Dataset)", y=1.02, fontweight="bold")

plt.show()
```

---

# Phần 6. Ứng dụng thực tiễn trong Data Science, Business & Economics

> **Lời dẫn dắt:**  
> Trực quan hóa dữ liệu chỉ thực sự phát huy giá trị khi được đặt trong bối cảnh giải quyết các bài toán nghiệp vụ cụ thể. Dưới đây là 3 tình huống ứng dụng điển hình được trích xuất từ các dự án thực tế của học phần DSAI1005:

## 6.1. Business Analytics: Doanh thu, Biên lợi nhuận & Tối ưu hóa định giá

> **Bài toán:**  
> Bộ phận Quản trị Bán hàng cần đánh giá hiệu quả kinh doanh của các dòng sản phẩm và tìm ra mức giá tối ưu nhằm tối đa hóa doanh thu dựa trên đường cầu thực nghiệm ($Demand = a - b \cdot Price$):

```python
import pandas as pd

# Giả lập mô hình kinh tế: Quan hệ Giá bán, Lượng cầu và Doanh thu
prices = np.linspace(10, 100, 50)
demand = np.maximum(0, 1000 - 10 * prices + np.random.normal(0, 20, 50))
revenue_curve = prices * demand

# Điểm tối ưu lý thuyết
opt_idx = np.argmax(revenue_curve)
opt_price = prices[opt_idx]
max_rev = revenue_curve[opt_idx]

fig, ax1 = plt.subplots(figsize=(8.5, 4.5))

# Đường 1: Đường cầu (Demand Curve)
color1 = "#1F5AA6"
ax1.plot(prices, demand, color=color1, linewidth=2, label="Đường cầu (Sản lượng bán)")
ax1.set_xlabel("Mức giá bán ($/sản phẩm)", fontweight="bold")
ax1.set_ylabel("Sản lượng cầu (Đơn vị)", color=color1, fontweight="bold")
ax1.tick_params(axis="y", labelcolor=color1)

# Đường 2: Đường Doanh thu (Revenue Curve)
ax2 = ax1.twinx()
color2 = "#D1495B"
ax2.plot(prices, revenue_curve, color=color2, linewidth=2.5, linestyle="--", label="Tổng Doanh thu")
ax2.set_ylabel("Tổng Doanh thu ($)", color=color2, fontweight="bold")
ax2.tick_params(axis="y", labelcolor=color2)
ax2.grid(False)

# Đánh dấu mức giá tối ưu
ax2.scatter([opt_price], [max_rev], color="red", s=100, zorder=5)
ax2.annotate(f"Giá tối ưu: ${opt_price:.1f}\nDoanh thu đỉnh: ${max_rev:,.0f}",
             xy=(opt_price, max_rev), xytext=(opt_price + 10, max_rev - 4000),
             arrowprops=dict(facecolor="black", shrink=0.08, width=1, headwidth=6),
             fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF3CD"))

plt.title("Phân tích Định giá Tối ưu hóa Doanh thu (Pricing & Revenue Strategy)", fontweight="bold")
plt.tight_layout()
plt.show()
```

---

## 6.2. Economics: Khám phá Đường cong Phillips và Chu kỳ kinh tế vĩ mô

> **Bài toán:**  
> Trong kinh tế học vĩ mô, **Đường cong Phillips** mô tả mối quan hệ đánh đổi trong ngắn hạn giữa Tỷ lệ Lạm phát (*Inflation Rate*) và Tỷ lệ Thất nghiệp (*Unemployment Rate*). Ta sử dụng biểu đồ phân tán kết hợp ánh xạ thời gian theo dải màu (*Colormap*) để quan sát sự dịch chuyển cấu trúc kinh tế:

```python
macro = pd.DataFrame({
    "Year": np.arange(2015, 2026),
    "Unemployment": [5.3, 4.9, 4.4, 3.9, 3.7, 8.1, 5.4, 3.6, 3.6, 4.0, 4.2],
    "Inflation": [0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8.0, 4.1, 3.0, 2.6]
})

fig, ax = plt.subplots(figsize=(8.5, 4.5))
scatter = ax.scatter(macro["Unemployment"], macro["Inflation"], c=macro["Year"],
                     cmap="plasma", s=100, edgecolors="black", linewidth=0.8, alpha=0.9)

cbar = plt.colorbar(scatter)
cbar.set_label("Giai đoạn Năm", fontweight="bold")

# Nối các điểm theo trật tự thời gian để thấy quỹ đạo kinh tế
ax.plot(macro["Unemployment"], macro["Inflation"], color="gray", linestyle=":", alpha=0.5)

ax.set_title("Khám phá Đường cong Phillips Thực nghiệm (Giai đoạn 2015–2025)", fontweight="bold")
ax.set_xlabel("Tỷ lệ Thất nghiệp (%)", fontweight="bold")
ax.set_ylabel("Tỷ lệ Lạm phát (%)", fontweight="bold")
ax.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.show()
```

---

## 6.3. Data Science & EDA: Phân tích Churn, Dữ liệu thiếu và Mất cân bằng nhãn

> **Bài toán:**  
> Trong bài toán phân loại khách hàng rời bỏ dịch vụ viễn thông (*Customer Churn*), việc kiểm tra mức độ mất cân bằng nhãn (*Class Imbalance*) là bước sống còn trước khi lựa chọn hàm mất mát và thuật toán huấn luyện:

```python
churn_data = pd.Series([820, 180], index=["Khách hàng Ở lại (Non-Churn)", "Khách hàng Rời bỏ (Churn)"])

fig, ax = plt.subplots(figsize=(6.5, 3.8))
bars = churn_data.plot(kind="bar", color=["#2A9D8F", "#E76F51"], edgecolor="black", linewidth=0.6, ax=ax)

ax.set_title("Kiểm tra Mất cân bằng Nhãn mục tiêu (Customer Churn Imbalance)", fontweight="bold")
ax.set_ylabel("Số lượng khách hàng")
ax.set_xticklabels(churn_data.index, rotation=0, fontweight="medium")
ax.set_ylim(0, 950)
ax.grid(axis="y", linestyle=":", alpha=0.5)

# Ghi nhãn số lượng và tỷ trọng %
total = churn_data.sum()
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f"{height:,d}\n({height/total:.1%})",
                xy=(p.get_x() + p.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points",
                ha="center", va="bottom", fontsize=9.5, fontweight="bold")

plt.tight_layout()
plt.show()
```

---

# Phần 7. Bảng tra cứu lệnh nhanh (Cheat Sheet) & Nguyên tắc thiết kế

> **Lời dẫn dắt:**  
> Nhằm giúp bạn tra cứu nhanh cú pháp khi làm bài tập thực hành và dự án cuối khóa, phần này cung cấp bảng đối chiếu tổng hợp và bộ quy tắc vàng trong thiết kế trực quan hóa dữ liệu.

## 7.1. Bảng đối chiếu cú pháp Matplotlib vs. Seaborn

| Tác vụ trực quan hóa | Matplotlib (OO API) | Seaborn (Axes-level API) | Seaborn (Figure-level API) |
|:---|:---|:---|:---|
| **Vẽ đường (Line plot)** | `ax.plot(x, y)` | `sns.lineplot(data=df, x=..., y=..., ax=ax)` | `sns.relplot(kind="line", ...)` |
| **Vẽ cột (Bar plot)** | `ax.bar(x, height)` | `sns.barplot(data=df, x=..., y=..., ax=ax)` | `sns.catplot(kind="bar", ...)` |
| **Đếm tần suất** | `ax.bar(cats, counts)` | `sns.countplot(data=df, x=..., ax=ax)` | `sns.catplot(kind="count", ...)` |
| **Điểm phân tán** | `ax.scatter(x, y)` | `sns.scatterplot(data=df, x=..., y=..., ax=ax)` | `sns.relplot(kind="scatter", ...)` |
| **Phân phối Histogram**| `ax.hist(x, bins=...)` | `sns.histplot(data=df, x=..., kde=True, ax=ax)` | `sns.displot(kind="hist", ...)` |
| **Biểu đồ Hộp (Boxplot)**| `ax.boxplot(x)` | `sns.boxplot(data=df, x=..., y=..., ax=ax)` | `sns.catplot(kind="box", ...)` |
| **Hồi quy tuyến tính** | `np.polyfit` + `ax.plot` | `sns.regplot(data=df, x=..., y=..., ax=ax)` | `sns.lmplot(data=df, x=..., y=...)` |
| **Ma trận nhiệt (Heatmap)**| `ax.imshow(mat)` | `sns.heatmap(df.corr(), annot=True, ax=ax)` | `sns.clustermap(df.corr())` |
| **Ma trận cặp biến** | Vòng lặp `subplots` | - | `sns.pairplot(df, hue=...)` |

---

## 7.2. Tùy biến Theme, Palette và Hỗ trợ Tiếng Việt

```python
# 1. Cấu hình phông chữ hệ thống hiển thị tốt tiếng Việt có dấu
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI']
plt.rcParams['axes.unicode_minus'] = False # Tránh lỗi hiển thị dấu âm '-'

# 2. Quản lý Theme thẩm mỹ của Seaborn
sns.set_theme(style="whitegrid", palette="tab10", font_scale=1.0)
# Các kiểu style hỗ trợ: 'whitegrid', 'darkgrid', 'ticks', 'white'
# Các bộ palette tiêu biểu:
# - Định danh (Categorical): 'tab10', 'Set2', 'muted'
# - Thứ bậc (Sequential): 'Blues', 'viridis', 'plasma'
# - Phân kỳ (Diverging): 'coolwarm', 'vlag', 'RdBu'
```

---

## 7.3. Bộ quy tắc vàng thiết kế biểu đồ chuẩn mực

1. **Tối ưu hóa Tỷ lệ Dữ liệu / Mực in (Data-Ink Ratio - Edward Tufte):**  
   Loại bỏ triệt để các chi tiết trang trí thừa thãi (*chart junk*), đường viền bao khung quá đậm, hiệu ứng 3D giả lập hoặc đổ bóng làm sai lệch góc nhìn thị giác.
2. **Tôn trọng Tính toàn vẹn của Tọa độ (Axis Integrity):**  
   Biểu đồ cột (Bar chart) **luôn luôn phải bắt đầu từ gốc tọa độ 0**. Không cắt cụt trục tung nhằm phóng đại giả tạo mức độ tăng trưởng.
3. **Phối màu có chủ đích & Hỗ trợ người khiếm thị màu (Accessibility):**  
   - Dùng màu nổi bật (*Accent color*) cho thông điệp quan trọng nhất, các nhóm còn lại dùng màu trung tính (xám, xanh nhạt).
   - Tránh kết hợp cặp màu Đỏ - Xanh lá (*Red-Green*) trên cùng một chuỗi dữ liệu để đảm bảo người khiếm thị màu (*Colorblind*) vẫn đọc hiểu chính xác.
4. **Nguyên tắc Tự giải thích (Self-explanatory Standard):**  
   Một biểu đồ hoàn chỉnh phải đứng độc lập và truyền tải đầy đủ thông tin: Tiêu đề nêu bật kết luận, nhãn trục ghi rõ đơn vị tính, có chú giải nhận diện và trích dẫn nguồn dữ liệu rõ ràng.

---

## 8. Tài liệu học tập & Liên kết tham khảo

- 💻 **Notebook thực hành Matplotlib toàn diện (19 chủ đề):** [part04-matplotlib-practice-vn.ipynb](part04-matplotlib-practice-vn.ipynb)
- 💻 **Notebook thực hành Seaborn toàn diện (20 chủ đề):** [part04-seaborn-practice-vn.ipynb](part04-seaborn-practice-vn.ipynb)
- 📊 **Project thực hành tổng hợp 4 bài toán lớn:** [part04-matplotlib-exercies-vn.ipynb](part04-matplotlib-exercies-vn.ipynb)
- 📑 **Slide bài giảng Matplotlib (66 trang):** <a href="part04-matplotlib-vn.pdf" target="_blank">part04-matplotlib-vn.pdf</a>
- 📑 **Slide bài giảng Seaborn (31 trang):** <a href="part04-seaborn-vn.pdf" target="_blank">part04-seaborn-vn.pdf</a>
- 🌐 **Tài liệu tham khảo chính thức:** [Matplotlib Official Docs](https://matplotlib.org/) | [Seaborn Official Docs](https://seaborn.pydata.org/)
