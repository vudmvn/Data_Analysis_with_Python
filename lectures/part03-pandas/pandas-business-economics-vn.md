# LAB — Pandas cho Phân tích Kinh doanh, Kinh tế và Chuỗi cung ứng

**Định dạng:** Ví dụ mẫu có lời giải + bài tập lập trình cho sinh viên  
**Thư viện chính:** Pandas  
**Thư viện hỗ trợ:** NumPy  
**Bối cảnh:** Doanh số, định giá, khách hàng, lạm phát, tồn kho, mua hàng, nhà cung cấp, logistics, dự báo và hiệu quả chuỗi cung ứng

## Thiết kế bài học

Mỗi phần gồm:

1. **Ví dụ mẫu** — đoạn code minh họa ý tưởng Pandas chính.
2. **Bài tập** — bài tương ứng để sinh viên tự lập trình.
3. **Bối cảnh Kinh doanh / Kinh tế / Chuỗi cung ứng** — giải thích vì sao bài toán có ý nghĩa trong thực tế.
4. **Yêu cầu** — các đầu ra và tên biến bắt buộc.
5. **Gợi ý** — các phương thức và thao tác Pandas nên sử dụng.
6. **Diễn giải** — giải thích ngắn theo góc nhìn quản trị, kinh tế hoặc chuỗi cung ứng.

## Quy định

- Sử dụng **Pandas** làm thư viện chính.
- Có thể sử dụng NumPy khi hỗ trợ tự nhiên cho các thao tác Pandas.
- Không sử dụng vòng lặp `for` tường minh trừ khi đề bài yêu cầu.
- Không hard-code các đáp án số cuối cùng.
- Giữ nguyên các tên biến được yêu cầu.
- Sau khi lọc, group, merge hoặc reshape, kiểm tra kết quả bằng `shape`, `head()` hoặc cả hai.
- Khi xử lý giá trị thiếu, so sánh số lượng giá trị thiếu trước và sau xử lý.
- Khi merge các tập dữ liệu, so sánh số hàng trước và sau khi merge.

## Mục tiêu học tập

Sau khi hoàn thành bài lab này, sinh viên có thể:

1. Biểu diễn dữ liệu kinh doanh, kinh tế và chuỗi cung ứng bằng Pandas `Series` và `DataFrame`.
2. Kiểm tra dữ liệu dạng bảng bằng `head()`, `shape`, `columns`, `dtypes`, `info()` và `describe()`.
3. Chọn các quan sát bằng `loc`, `iloc`, chọn cột và lọc Boolean.
4. Tạo các biến kinh doanh mới bằng phép toán vector hóa trên cột.
5. Đọc và ghi dữ liệu CSV, Excel và JSON.
6. Phát hiện và xử lý giá trị thiếu và bản ghi trùng lặp.
7. Làm sạch dữ liệu chuỗi và chuyển đổi kiểu dữ liệu.
8. Sắp xếp, xếp hạng và chọn các đối tượng kinh doanh có hiệu quả cao.
9. Nhóm và tổng hợp dữ liệu bằng `groupby()` và `agg()`.
10. Xây dựng pivot table cho báo cáo quản trị.
11. Merge dữ liệu khách hàng, đơn hàng, nhà cung cấp, mua hàng và logistics.
12. Phân tích tồn kho và nguy cơ hết hàng.
13. Đánh giá hiệu quả nhà cung cấp và logistics.
14. Làm việc với dữ liệu kinh doanh chuỗi thời gian bằng datetime index, `resample()` và `rolling()`.
15. Tính tương quan và tạo trực quan hóa nhanh.
16. Diễn giải kết quả Pandas ngắn gọn theo góc nhìn quản trị, kinh tế và chuỗi cung ứng.

## Kiến thức và kỹ năng Pandas sử dụng trong bài lab

### DataFrame và Series

Sinh viên sẽ thực hành:

- `pd.Series()`
- `pd.DataFrame()`
- `shape`
- `columns`
- `index`
- `dtypes`
- `head()`
- `tail()`
- `info()`
- `describe()`

### Indexing và lọc dữ liệu

Sinh viên sẽ sử dụng:

- `df["column"]`
- `df[["col1", "col2"]]`
- `loc`
- `iloc`
- Boolean masks
- Multiple conditions using `&`, `|`, and `~`

### Biến đổi dữ liệu

Sinh viên sẽ thực hành:

- Tạo các cột tính toán
- Phép toán vector hóa
- `assign()`
- `map()`
- `apply()`
- `astype()`
- `pd.to_numeric()`
- Các phương thức xử lý chuỗi bằng `.str`

### Làm sạch dữ liệu

Sinh viên sẽ sử dụng:

- `isna()`
- `isna().sum()`
- `dropna()`
- `fillna()`
- `duplicated()`
- `drop_duplicates()`

### Sắp xếp và xếp hạng

Sinh viên sẽ thực hành:

- `sort_values()`
- `nlargest()`
- `nsmallest()`
- `rank()`

### Nhóm và tổng hợp dữ liệu

Sinh viên sẽ sử dụng:

- `groupby()`
- `sum()`
- `mean()`
- `count()`
- `min()`
- `max()`
- `agg()`
- `reset_index()`

### Merge và reshape dữ liệu

Sinh viên sẽ sử dụng:

- `pd.merge()`
- `pd.concat()`
- `pivot()`
- `pd.pivot_table()`
- `pd.melt()`

### Phân tích chuỗi thời gian

Sinh viên sẽ thực hành:

- `pd.to_datetime()`
- `set_index()`
- `sort_index()`
- `resample()`
- `rolling()`

### Phân tích Kinh doanh và Chuỗi cung ứng

Sinh viên sẽ đánh giá:

- Doanh thu và lợi nhuận
- Giá trị khách hàng
- Doanh số theo vùng
- Giá trị điều chỉnh theo lạm phát
- Mức độ bao phủ tồn kho
- Nguy cơ hết hàng
- Chất lượng nhà cung cấp và lead time
- Chi tiêu mua hàng
- Hiệu quả giao hàng
- Sai số dự báo
- KPI chuỗi cung ứng

---

# Phần 0 — Chuẩn bị môi trường

```python
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

print("Pandas version:", pd.__version__)
```

---

# Phần 1 — Phân tích doanh số và doanh thu

## Ví dụ mẫu 1.1 — Tạo và kiểm tra DataFrame doanh số

```python
example_sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Units": [100, 120, 110, 140],
    "Price": [10.0, 10.0, 11.0, 11.5]
})

example_sales["Revenue"] = (
    example_sales["Units"] *
    example_sales["Price"]
)

print(example_sales)
print("Shape:", example_sales.shape)
print(example_sales.dtypes)
```

## Bài tập 1.1 — Phân tích hiệu quả kinh doanh 12 tháng

### Bối cảnh kinh doanh

Một nhà quản lý bán lẻ muốn đánh giá hiệu quả kinh doanh theo tháng của một sản phẩm trong một năm. Nhà quản lý cần biết doanh thu, hiệu quả trung bình theo tháng và tháng có kết quả tốt nhất.

### Mô tả bài tập

Trong bài này, bạn sẽ tạo một Pandas DataFrame, tính doanh thu, kiểm tra tập dữ liệu và xác định tháng có doanh thu cao nhất.

Bài tập nhấn mạnh **tạo DataFrame**, **tạo cột tính toán**, **tổng hợp dữ liệu** và **chọn hàng**.

Sử dụng:

```python
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

units_sold = [
    420, 460, 440, 500, 540, 525,
    575, 610, 590, 650, 690, 720
]

unit_price = [
    12.0, 12.0, 12.5, 12.5, 13.0, 13.0,
    13.5, 13.5, 14.0, 14.0, 14.5, 14.5
]
```

### Yêu cầu

Tạo:

- `sales_df`
- column `Revenue`
- `annual_revenue`
- `average_monthly_revenue`
- `best_month_row`

In:

- `sales_df.head()`
- `sales_df.shape`
- `sales_df.dtypes`
- required results

### Gợi ý

- `pd.DataFrame({...})`
- `df["Revenue"] = ...`
- `df["Revenue"].sum()`
- `df["Revenue"].mean()`
- `df.loc[df["Revenue"].idxmax()]`

```python
# CODE SINH VIÊN — 1.1

# sales_df = pd.DataFrame({
#     "Month": ...,
#     "Units": ...,
#     "Price": ...
# })

# sales_df["Revenue"] = ...
# annual_revenue = ...
# average_monthly_revenue = ...
# best_month_row = ...

# In các kết quả được yêu cầu.
```

### Diễn giải

Viết 2–3 câu giải thích liệu hiệu quả kinh doanh có xu hướng cải thiện trong năm hay không và tháng nào đóng góp doanh thu cao nhất.

---

## Ví dụ mẫu 1.2 — Lọc các tháng có hiệu quả cao

```python
example_sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [1000, 1250, 1100, 1500]
})

high_months = example_sales[
    example_sales["Revenue"] >= 1200
]

print(high_months)
```

## Bài tập 1.2 — Xác định các tháng có doanh thu cao

### Bối cảnh kinh doanh

Nhà quản lý thường tập trung vào các tháng vượt ngưỡng hiệu quả để phân tích chương trình khuyến mại, tính mùa vụ hoặc điều kiện cầu.

### Yêu cầu

Using `sales_df`, create:

- `high_revenue_months` where Revenue is above the annual monthly average;
- `high_revenue_high_volume` where:
  - Revenue is above average;
  - Units are at least 600.

### Gợi ý

- Boolean filtering
- `df["Revenue"] > average_monthly_revenue`
- Combine conditions with `&`

```python
# CODE SINH VIÊN — 1.2

# high_revenue_months = ...
# high_revenue_high_volume = ...

# In shape và kết quả.
```

### Diễn giải

Giải thích vì sao lọc đồng thời theo doanh thu và sản lượng có thể cung cấp tín hiệu quản trị khác với chỉ lọc theo doanh thu.

---

# Phần 2 — Phân tích khách hàng và thị trường

## Ví dụ mẫu 2.1 — Phân khúc khách hàng bằng điều kiện Boolean

```python
customers = pd.DataFrame({
    "Customer": ["C1", "C2", "C3", "C4"],
    "Orders": [3, 10, 6, 12],
    "AnnualSpend": [500, 2500, 1300, 4200]
})

vip = customers[
    (customers["Orders"] >= 8) &
    (customers["AnnualSpend"] >= 2000)
]

print(vip)
```

## Bài tập 2.1 — Xác định khách hàng giá trị cao

### Bối cảnh kinh doanh

Một doanh nghiệp muốn xác định các khách hàng giá trị cao để triển khai chương trình khách hàng thân thiết và ưu đãi cá nhân hóa.

Sử dụng:

```python
customer_df = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08"],
    "Orders": [2, 8, 5, 12, 3, 9, 6, 15],
    "AnnualSpend": [450, 2200, 1400, 3900, 700, 2600, 1800, 5200],
    "Returns": [0, 1, 0, 2, 1, 0, 3, 1]
})
```

### Yêu cầu

Tạo:

- `high_value_customers`
- `high_value_low_return`
- `top_3_customers`

Điều kiện cho `high_value_customers`:

- Orders >= 8
- AnnualSpend >= 2000

Điều kiện cho `high_value_low_return`:

- high-value conditions;
- Returns <= 1.

### Gợi ý

- Boolean filtering
- `.nlargest(3, "AnnualSpend")`

```python
# CODE SINH VIÊN — 2.1

# high_value_customers = ...
# high_value_low_return = ...
# top_3_customers = ...

# In kết quả.
```

### Diễn giải

Giải thích vì sao doanh nghiệp có thể ưu tiên một khách hàng có mức chi tiêu thấp hơn đôi chút nhưng ít trả hàng hơn.

---

## Ví dụ mẫu 2.2 — Xếp hạng khách hàng

```python
customers["SpendRank"] = (
    customers["AnnualSpend"]
    .rank(ascending=False)
)

print(customers)
```

## Bài tập 2.2 — Xếp hạng giá trị khách hàng

### Yêu cầu

Thêm:

- `SpendRank`
- `OrderRank`

Sắp xếp DataFrame theo:

1. AnnualSpend descending;
2. Orders descending.

Tạo:

- `customer_ranking`

### Gợi ý

- `.rank(ascending=False)`
- `.sort_values([...], ascending=[False, False])`

```python
# CODE SINH VIÊN — 2.2

# customer_df["SpendRank"] = ...
# customer_df["OrderRank"] = ...
# customer_ranking = ...

# In kết quả.
```

---

# Phần 3 — Phân tích kinh tế: Giá cả và lạm phát

## Ví dụ mẫu 3.1 — Điều chỉnh doanh số theo lạm phát

```python
economic_df = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "NominalSales": [100, 110, 121],
    "CPI": [100, 105, 110]
})

economic_df["RealSales"] = (
    economic_df["NominalSales"] *
    100 /
    economic_df["CPI"]
)

print(economic_df)
```

## Bài tập 3.1 — Tăng trưởng danh nghĩa và tăng trưởng thực

### Bối cảnh kinh tế

Tăng trưởng kinh doanh danh nghĩa có thể một phần do lạm phát. Vì vậy, nhà phân tích điều chỉnh các giá trị tài chính bằng chỉ số giá để đo lường tăng trưởng thực.

Sử dụng:

```python
economic_df = pd.DataFrame({
    "Year": [2022, 2023, 2024, 2025, 2026],
    "NominalSales": [100, 108, 117, 126, 140],
    "CPI": [100, 103, 107, 112, 118]
})
```

### Yêu cầu

Tạo các cột:

- `RealSales`
- `NominalGrowthPct`
- `RealGrowthPct`
- `GrowthGap`

Use `pct_change()` for growth rates.

Tạo:

- `largest_gap_year`

### Gợi ý

- `df["NominalSales"] * 100 / df["CPI"]`
- `.pct_change() * 100`
- `.abs()`
- `.idxmax()`
- `.loc[...]`

```python
# CODE SINH VIÊN — 3.1

# economic_df["RealSales"] = ...
# economic_df["NominalGrowthPct"] = ...
# economic_df["RealGrowthPct"] = ...
# economic_df["GrowthGap"] = ...
# largest_gap_year = ...

# In kết quả.
```

### Diễn giải

Giải thích sự khác nhau giữa tăng trưởng danh nghĩa và tăng trưởng thực, và vì sao sự phân biệt này quan trọng đối với lập kế hoạch kinh doanh.

---

# Phần 4 — Làm sạch dữ liệu kinh doanh

## Ví dụ mẫu 4.1 — Giá trị thiếu

```python
example_df = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Price": [10.0, np.nan, 15.0]
})

print(example_df.isna().sum())

example_df["Price"] = (
    example_df["Price"]
    .fillna(example_df["Price"].median())
)

print(example_df)
```

## Bài tập 4.1 — Làm sạch một tập dữ liệu bán hàng chưa chuẩn

### Bối cảnh kinh doanh

Dữ liệu vận hành thường chứa giá bị thiếu, nhãn văn bản không nhất quán, định dạng số không đúng và các hàng trùng lặp.

Sử dụng:

```python
messy_sales = pd.DataFrame({
    "OrderID": ["O01", "O02", "O02", "O03", "O04", "O05"],
    "Product": [" Basic ", "PREMIUM", "PREMIUM", "standard", "Basic", " enterprise "],
    "Quantity": ["2", "3", "3", "4", "unknown", "5"],
    "Price": [10.0, 25.0, 25.0, np.nan, 10.0, 40.0]
})
```

### Yêu cầu

Tạo:

- `missing_before`
- cleaned `Product`
- numeric `Quantity`
- filled `Price`
- `clean_sales`
- `missing_after`

Các bước làm sạch bắt buộc:

1. remove exact duplicates;
2. strip spaces from Product;
3. convert Product to title case;
4. convert Quantity using `pd.to_numeric(errors="coerce")`;
5. fill missing Quantity using median;
6. fill missing Price using median.

### Gợi ý

- `.drop_duplicates()`
- `.str.strip()`
- `.str.title()`
- `pd.to_numeric(..., errors="coerce")`
- `.fillna(...)`

```python
# CODE SINH VIÊN — 4.1

# missing_before = ...

# clean_sales = messy_sales.copy()
# clean_sales = ...

# clean_sales["Product"] = ...
# clean_sales["Quantity"] = ...
# clean_sales["Quantity"] = ...
# clean_sales["Price"] = ...

# missing_after = ...

# In shape trước/sau và số lượng giá trị thiếu.
```

### Diễn giải

Giải thích dữ liệu chưa được làm sạch có thể làm sai lệch phân tích doanh thu, nhu cầu hoặc tồn kho như thế nào.

---

# Phần 5 — Nhóm dữ liệu và hiệu quả kinh doanh theo vùng

## Ví dụ mẫu 5.1 — Nhóm doanh số

```python
example = pd.DataFrame({
    "Region": ["North", "South", "North", "South"],
    "Sales": [100, 120, 150, 130]
})

region_summary = (
    example
    .groupby("Region")["Sales"]
    .agg(["count", "sum", "mean"])
)

print(region_summary)
```

## Bài tập 5.1 — Hiệu quả doanh số theo vùng

### Bối cảnh kinh doanh

Một doanh nghiệp hoạt động trên toàn quốc muốn so sánh hiệu quả doanh số giữa các vùng và sản phẩm.

Sử dụng:

```python
regional_sales = pd.DataFrame({
    "Region": [
        "North", "North", "South", "South",
        "Central", "Central", "North", "South"
    ],
    "Product": [
        "A", "B", "A", "B",
        "A", "B", "A", "B"
    ],
    "Revenue": [120, 180, 150, 210, 110, 160, 140, 190],
    "Units": [12, 15, 14, 18, 10, 13, 11, 16]
})
```

### Yêu cầu

Tạo:

- `region_summary`
- `product_summary`
- `region_product_summary`

Với `region_summary`, tính:

- count;
- sum Revenue;
- mean Revenue;
- sum Units.

### Gợi ý

- `.groupby("Region")`
- `.agg(...)`
- `.groupby(["Region", "Product"])`
- `.reset_index()`

```python
# CODE SINH VIÊN — 5.1

# region_summary = ...
# product_summary = ...
# region_product_summary = ...

# In tất cả kết quả.
```

### Diễn giải

Xác định vùng có vẻ hoạt động tốt nhất và giải thích liệu chỉ dùng doanh thu có đủ để đánh giá hiệu quả hay không.

---

## Ví dụ mẫu 5.2 — Pivot Table

```python
pivot = pd.pivot_table(
    regional_sales,
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print(pivot)
```

## Bài tập 5.2 — Bảng báo cáo quản trị

### Yêu cầu

Tạo:

- `revenue_pivot`
- `units_pivot`

Thêm:

- a `Total` column to `revenue_pivot`.

### Gợi ý

- `pd.pivot_table()`
- `.sum(axis=1)`

```python
# CODE SINH VIÊN — 5.2

# revenue_pivot = ...
# units_pivot = ...
# revenue_pivot["Total"] = ...

# In kết quả.
```

---

# Phần 6 — Phân tích tồn kho và nguy cơ hết hàng

## Ví dụ mẫu 6.1 — Mức độ bao phủ tồn kho

```python
inventory = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Inventory": [100, 80, 150],
    "DailyDemand": [10, 20, 15]
})

inventory["DaysCover"] = (
    inventory["Inventory"] /
    inventory["DailyDemand"]
)

print(inventory)
```

## Bài tập 6.1 — Mức độ bao phủ tồn kho và nguy cơ hết hàng

### Bối cảnh chuỗi cung ứng

Nhà quản lý tồn kho cần biết lượng tồn kho hiện tại có thể đáp ứng nhu cầu dự kiến trong bao lâu. Số ngày bao phủ thấp cho thấy nguy cơ hết hàng cao hơn.

Sử dụng:

```python
inventory_df = pd.DataFrame({
    "SKU": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "Inventory": [500, 180, 420, 90, 650, 220],
    "DailyDemand": [40, 30, 35, 25, 50, 28],
    "LeadTimeDays": [8, 6, 10, 5, 12, 7]
})
```

### Yêu cầu

Tạo các cột:

- `DaysCover`
- `LeadTimeDemand`
- `ReorderRisk`

Định nghĩa `ReorderRisk` là:

```text
Inventory < LeadTimeDemand
```

Tạo:

- `at_risk_skus`
- `lowest_cover_skus`

trong đó `lowest_cover_skus` chứa ba SKU có `DaysCover` thấp nhất.

### Gợi ý

- vectorized division
- `Inventory < LeadTimeDemand`
- `.nsmallest(3, "DaysCover")`

```python
# CODE SINH VIÊN — 6.1

# inventory_df["DaysCover"] = ...
# inventory_df["LeadTimeDemand"] = ...
# inventory_df["ReorderRisk"] = ...

# at_risk_skus = ...
# lowest_cover_skus = ...

# In kết quả.
```

### Diễn giải

Giải thích vì sao chỉ so sánh tồn kho với nhu cầu hiện tại có thể gây hiểu nhầm khi lead time bổ sung hàng dài.

---

# Phần 7 — Hiệu quả nhà cung cấp

## Ví dụ mẫu 7.1 — Điểm đánh giá nhà cung cấp

```python
suppliers = pd.DataFrame({
    "Supplier": ["S1", "S2", "S3"],
    "Quality": [95, 90, 98],
    "LeadTime": [8, 6, 10]
})

suppliers["LeadTimeScore"] = (
    1 -
    (suppliers["LeadTime"] - suppliers["LeadTime"].min()) /
    (suppliers["LeadTime"].max() - suppliers["LeadTime"].min())
)

print(suppliers)
```

## Bài tập 7.1 — Đánh giá nhà cung cấp

### Bối cảnh chuỗi cung ứng

Quyết định mua hàng thường phụ thuộc vào nhiều chỉ tiêu có thể xung đột như chi phí, chất lượng, lead time và độ tin cậy giao hàng.

Sử dụng:

```python
supplier_df = pd.DataFrame({
    "Supplier": ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"],
    "UnitCost": [12.5, 11.8, 13.0, 12.2, 11.5],
    "QualityScore": [92, 88, 97, 94, 85],
    "LeadTimeDays": [8, 6, 10, 7, 5],
    "OnTimeRate": [0.94, 0.90, 0.98, 0.95, 0.87]
})
```

### Yêu cầu

Tạo các cột đã chuẩn hóa:

- `CostScore` — lower cost is better;
- `QualityNorm` — higher is better;
- `LeadTimeScore` — lower lead time is better;
- `OnTimeNorm` — higher is better.

Sử dụng trọng số:

```python
weights = {
    "CostScore": 0.30,
    "QualityNorm": 0.25,
    "LeadTimeScore": 0.20,
    "OnTimeNorm": 0.25
}
```

Tạo:

- `SupplierScore`
- `supplier_ranking`

### Gợi ý

Với KPI dạng lợi ích:

```python
(x - x.min()) / (x.max() - x.min())
```

Với KPI dạng chi phí:

```python
1 - normalized_value
```

Sort:

```python
.sort_values("SupplierScore", ascending=False)
```

```python
# CODE SINH VIÊN — 7.1

# supplier_df["CostScore"] = ...
# supplier_df["QualityNorm"] = ...
# supplier_df["LeadTimeScore"] = ...
# supplier_df["OnTimeNorm"] = ...

# supplier_df["SupplierScore"] = ...
# supplier_ranking = ...

# In bảng xếp hạng.
```

### Diễn giải

Giải thích vì sao nhà cung cấp có đơn giá thấp nhất chưa chắc đạt điểm tổng thể cao nhất.

---

# Phần 8 — Phân tích chi tiêu mua hàng

## Ví dụ mẫu 8.1 — Merge đơn mua hàng với dữ liệu nhà cung cấp

```python
supplier_master = pd.DataFrame({
    "SupplierID": ["S1", "S2"],
    "SupplierName": ["Alpha", "Beta"]
})

purchase_orders = pd.DataFrame({
    "PO": ["P1", "P2", "P3"],
    "SupplierID": ["S1", "S2", "S1"],
    "Amount": [1000, 1500, 1200]
})

merged = pd.merge(
    purchase_orders,
    supplier_master,
    on="SupplierID",
    how="left"
)

print(merged)
```

## Bài tập 8.1 — Phân tích chi tiêu mua hàng theo nhà cung cấp

### Bối cảnh chuỗi cung ứng

Nhà quản lý mua hàng thường lưu dữ liệu master của nhà cung cấp và giao dịch đơn mua hàng ở các bảng riêng biệt. Các bảng này cần được merge trước khi phân tích chi tiêu.

Sử dụng:

```python
supplier_master = pd.DataFrame({
    "SupplierID": ["S01", "S02", "S03", "S04"],
    "SupplierName": ["Alpha", "Beta", "Gamma", "Delta"],
    "Country": ["VN", "TH", "CN", "VN"]
})

purchase_orders = pd.DataFrame({
    "PO": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"],
    "SupplierID": ["S01", "S02", "S01", "S03", "S02", "S05", "S04"],
    "Amount": [12000, 15000, 9000, 22000, 8000, 7000, 14000]
})
```

### Yêu cầu

Tạo:

- `po_supplier`
- `unmatched_orders`
- `supplier_spend`
- `country_spend`

Sử dụng left merge bắt đầu từ bảng purchase orders.

### Gợi ý

- `pd.merge(..., how="left")`
- unmatched supplier:
  - `SupplierName.isna()`
- `.groupby(...)["Amount"].sum()`

```python
# CODE SINH VIÊN — 8.1

# po_supplier = ...
# unmatched_orders = ...
# supplier_spend = ...
# country_spend = ...

# In shape và kết quả.
```

### Diễn giải

Giải thích vì sao Supplier ID không khớp là một vấn đề chất lượng dữ liệu trong báo cáo mua hàng.

---

# Phần 9 — Hiệu quả logistics và giao hàng

## Ví dụ mẫu 9.1 — Độ trễ giao hàng

```python
delivery = pd.DataFrame({
    "Order": ["O1", "O2", "O3"],
    "PromisedDays": [3, 4, 2],
    "ActualDays": [3, 6, 2]
})

delivery["DelayDays"] = (
    delivery["ActualDays"] -
    delivery["PromisedDays"]
)

delivery["OnTime"] = (
    delivery["DelayDays"] <= 0
)

print(delivery)
```

## Bài tập 9.1 — Phân tích mức độ dịch vụ logistics

### Bối cảnh chuỗi cung ứng

Độ tin cậy giao hàng ảnh hưởng trực tiếp đến sự hài lòng của khách hàng và hiệu quả chuỗi cung ứng. Nhà quản lý cần cả mức dịch vụ tổng thể và so sánh theo hãng vận chuyển.

Sử dụng:

```python
delivery_df = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06", "O07", "O08"],
    "Carrier": ["A", "A", "B", "B", "C", "C", "A", "B"],
    "PromisedDays": [3, 4, 3, 5, 2, 4, 3, 4],
    "ActualDays": [3, 6, 4, 5, 2, 7, 2, 5],
    "ShippingCost": [20, 30, 25, 35, 18, 32, 22, 28]
})
```

### Yêu cầu

Tạo các cột:

- `DelayDays`
- `OnTime`

Tạo:

- `overall_on_time_rate`
- `carrier_summary`

Với mỗi hãng vận chuyển, tính:

- số lượt giao hàng;
- DelayDays trung bình;
- tỷ lệ giao đúng hạn;
- ShippingCost trung bình.

### Gợi ý

- Có thể lấy trung bình cột Boolean vì `True = 1`, `False = 0`.
- `.groupby("Carrier").agg(...)`
- Named aggregation syntax may be useful.

```python
# CODE SINH VIÊN — 9.1

# delivery_df["DelayDays"] = ...
# delivery_df["OnTime"] = ...

# overall_on_time_rate = ...

# carrier_summary = ...

# In kết quả.
```

### Diễn giải

Thảo luận về sự đánh đổi giữa hiệu quả giao hàng và chi phí vận chuyển.

---

# Phần 10 — Chuỗi thời gian doanh số và dự báo

## Ví dụ mẫu 10.1 — Resampling theo tháng

```python
dates = pd.date_range(
    "2026-01-01",
    periods=10,
    freq="D"
)

daily = pd.DataFrame({
    "Date": dates,
    "Sales": np.arange(100, 110)
})

daily = daily.set_index("Date")

weekly = daily["Sales"].resample("W").sum()

print(weekly)
```

## Bài tập 10.1 — Tổng hợp doanh số từ ngày sang tuần

### Bối cảnh kinh doanh

Doanh số hằng ngày có thể biến động mạnh. Tổng hợp theo tuần giúp nhà quản lý có góc nhìn ở mức cao hơn cho lập kế hoạch và báo cáo.

Sử dụng:

```python
dates = pd.date_range(
    start="2026-01-01",
    periods=60,
    freq="D"
)

daily_sales = pd.DataFrame({
    "Date": dates,
    "Sales": 100 + np.arange(60) * 1.5
})
```

### Yêu cầu

1. set `Date` as the index;
2. create `weekly_sales`;
3. create `monthly_sales`;
4. create a 7-day moving average column `MA7`.

### Gợi ý

- `.set_index("Date")`
- `.resample("W").sum()`
- `.resample("ME").sum()`
- `.rolling(window=7).mean()`

```python
# CODE SINH VIÊN — 10.1

# daily_sales = ...
# weekly_sales = ...
# monthly_sales = ...
# daily_sales["MA7"] = ...

# In kết quả.
```

---

## Ví dụ mẫu 10.2 — Sai số dự báo trong DataFrame

```python
forecast_df = pd.DataFrame({
    "Actual": [100, 120, 110],
    "Forecast": [98, 125, 108]
})

forecast_df["Error"] = (
    forecast_df["Actual"] -
    forecast_df["Forecast"]
)

forecast_df["AbsoluteError"] = (
    forecast_df["Error"].abs()
)

print(forecast_df)
```

## Bài tập 10.2 — So sánh độ chính xác dự báo

### Bối cảnh Kinh doanh / Chuỗi cung ứng

Độ chính xác dự báo ảnh hưởng đến lập kế hoạch tồn kho, sản xuất, mua hàng và logistics.

Sử dụng:

```python
forecast_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
    "Actual": [120, 135, 128, 150, 160, 172, 168, 180],
    "ForecastA": [118, 132, 134, 147, 158, 169, 171, 176],
    "ForecastB": [125, 138, 127, 155, 166, 175, 165, 185]
})
```

### Yêu cầu

Create columns for both methods:

- `ErrorA`
- `ErrorB`
- `AbsErrorA`
- `AbsErrorB`
- `APE_A`
- `APE_B`

Tạo:

- `mae_a`
- `mae_b`
- `mape_a`
- `mape_b`

### Gợi ý

- `.abs()`
- `.mean()`
- percentage error:
  ```python
  abs(error / actual) * 100
  ```

```python
# CODE SINH VIÊN — 10.2

# forecast_df["ErrorA"] = ...
# forecast_df["ErrorB"] = ...
# forecast_df["AbsErrorA"] = ...
# forecast_df["AbsErrorB"] = ...
# forecast_df["APE_A"] = ...
# forecast_df["APE_B"] = ...

# mae_a = ...
# mae_b = ...
# mape_a = ...
# mape_b = ...

# In tất cả các kết quả được yêu cầu.
```

### Diễn giải

Nêu phương pháp dự báo nào tốt hơn theo MAE và MAPE, đồng thời giải thích vì sao độ chính xác dự báo quan trọng đối với lập kế hoạch tồn kho.

---

# Phần 11 — Dashboard KPI chuỗi cung ứng

## Ví dụ mẫu 11.1 — Tóm tắt KPI

```python
kpi_df = pd.DataFrame({
    "Warehouse": ["W1", "W2", "W3"],
    "FillRate": [0.95, 0.90, 0.97],
    "InventoryTurns": [8, 6, 9]
})

print(
    kpi_df.describe()
)
```

## Bài tập 11.1 — Hiệu quả kho hàng

### Bối cảnh chuỗi cung ứng

Một nhà quản lý chuỗi cung ứng đánh giá các kho hàng bằng nhiều KPI phản ánh mức dịch vụ, hiệu quả tồn kho và chi phí.

Sử dụng:

```python
warehouse_df = pd.DataFrame({
    "Warehouse": ["North DC", "South DC", "Central DC", "East DC"],
    "FillRate": [0.96, 0.91, 0.94, 0.89],
    "InventoryTurns": [8.5, 6.2, 7.8, 5.9],
    "OrderCycleDays": [2.8, 3.6, 3.0, 4.1],
    "CostPerOrder": [4.8, 4.2, 5.1, 3.9]
})
```

### Yêu cầu

1. inspect with `describe()`;
2. create normalized KPI columns;
3. reverse cost-type KPIs:
   - OrderCycleDays;
   - CostPerOrder;
4. use weights:
   - FillRate: 0.35
   - InventoryTurns: 0.25
   - OrderCycleDays: 0.20
   - CostPerOrder: 0.20
5. create `PerformanceScore`;
6. create `warehouse_ranking`.

### Gợi ý

KPI dạng lợi ích:

```python
(x - x.min()) / (x.max() - x.min())
```

KPI dạng chi phí:

```python
1 - normalized_value
```

### Code của sinh viên

```python
# CODE SINH VIÊN — 11.1

# warehouse_df["FillRateNorm"] = ...
# warehouse_df["TurnsNorm"] = ...
# warehouse_df["CycleScore"] = ...
# warehouse_df["CostScore"] = ...

# warehouse_df["PerformanceScore"] = ...

# warehouse_ranking = ...

# In bảng xếp hạng.
```

### Diễn giải

Giải thích vì sao một kho có chi phí thấp nhất vẫn có thể xếp hạng tổng thể thấp.

---

# Phần 12 — Phân tích chuỗi cung ứng tích hợp

## Bài tập 12.1 — Phân tích đơn hàng end-to-end

### Bối cảnh chuỗi cung ứng

Một nhà quản lý muốn kết nối dữ liệu đơn hàng khách hàng, thông tin sản phẩm và hiệu quả giao hàng để phân tích doanh thu, biên lợi nhuận và chất lượng dịch vụ trong một tập dữ liệu tích hợp.

Sử dụng:

```python
orders = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06"],
    "CustomerID": ["C01", "C02", "C01", "C03", "C04", "C02"],
    "ProductID": ["P1", "P2", "P2", "P3", "P1", "P3"],
    "Quantity": [2, 1, 3, 2, 4, 1]
})

products = pd.DataFrame({
    "ProductID": ["P1", "P2", "P3"],
    "Price": [20.0, 35.0, 50.0],
    "UnitCost": [12.0, 21.0, 32.0]
})

delivery = pd.DataFrame({
    "OrderID": ["O01", "O02", "O03", "O04", "O05", "O06"],
    "Carrier": ["A", "B", "A", "C", "B", "C"],
    "PromisedDays": [3, 4, 3, 5, 4, 3],
    "ActualDays": [3, 5, 2, 7, 4, 4]
})
```

### Yêu cầu

Tạo DataFrame tích hợp `order_analysis` bằng cách:

1. merging orders with products;
2. merging the result with delivery;
3. creating:
   - `Revenue`;
   - `TotalCost`;
   - `Contribution`;
   - `DelayDays`;
   - `OnTime`.
4. calculate:
   - total Revenue;
   - total Contribution;
   - overall on-time rate.
5. create:
   - `product_summary`;
   - `carrier_summary`;
   - `customer_summary`.
6. xác định:
   - sản phẩm có doanh thu cao nhất;
   - khách hàng có contribution cao nhất;
   - hãng vận chuyển có tỷ lệ giao đúng hạn tốt nhất.

### Gợi ý

- `pd.merge()`
- Revenue:
  ```python
  Quantity * Price
  ```
- Contribution:
  ```python
  Revenue - TotalCost
  ```
- `groupby()` + `agg()`
- `idxmax()`

```python
# CODE SINH VIÊN — 12.1

# order_analysis = pd.merge(...)
# order_analysis = pd.merge(...)

# order_analysis["Revenue"] = ...
# order_analysis["TotalCost"] = ...
# order_analysis["Contribution"] = ...
# order_analysis["DelayDays"] = ...
# order_analysis["OnTime"] = ...

# total_revenue = ...
# total_contribution = ...
# overall_on_time_rate = ...

# product_summary = ...
# carrier_summary = ...
# customer_summary = ...

# In tất cả các kết quả được yêu cầu.
```

### Diễn giải

Viết 4–6 câu giải thích các phát hiện kinh doanh và chuỗi cung ứng quan trọng nhất từ phân tích tích hợp.

---

# Câu hỏi phản tư cuối bài

1. Phần nào minh họa rõ nhất việc tạo và kiểm tra DataFrame?
2. Phần nào minh họa rõ nhất lọc Boolean?
3. Phần nào minh họa rõ nhất `groupby()` và tổng hợp dữ liệu?
4. Phần nào minh họa rõ nhất việc merge nhiều tập dữ liệu?
5. Phần nào liên quan nhất đến Kinh doanh hoặc Kinh tế?
6. Phần nào liên quan nhất đến Quản trị Chuỗi cung ứng?
7. Bạn dự kiến thao tác Pandas nào sẽ được sử dụng thường xuyên nhất trong phân tích dữ liệu thực tế?
8. Một rủi ro của việc ra quyết định quản trị từ DataFrame mà chưa kiểm tra chất lượng dữ liệu là gì?
