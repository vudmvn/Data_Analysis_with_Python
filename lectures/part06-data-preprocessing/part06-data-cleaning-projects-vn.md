# Projects thực hành Data Cleaning trong Economics, Business và Data Science

Các project dưới đây được thiết kế để sinh viên vận dụng toàn bộ quy trình **Data Cleaning** trong các bối cảnh thực tế.

Mỗi project đều yêu cầu:

```text
Raw Data
   ↓
Assess Data Quality
   ↓
Detect Problems
   ↓
Clean / Correct / Standardize
   ↓
Validate
   ↓
Analyze the Cleaned Data
   ↓
Document Cleaning Decisions
```

Sinh viên không chỉ cần viết code mà còn phải giải thích:

- dữ liệu có vấn đề gì;
- tại sao chọn cách xử lý đó;
- dữ liệu thay đổi như thế nào sau cleaning;
- quyết định cleaning có thể ảnh hưởng đến kết quả phân tích ra sao.

---

# Project 1 — Làm sạch dữ liệu bán lẻ và kiểm tra doanh thu

## 1. Bối cảnh

Một chuỗi cửa hàng bán lẻ muốn phân tích hiệu quả kinh doanh theo:

- khu vực;
- sản phẩm;
- phương thức thanh toán;
- thời gian;
- khách hàng.

Tuy nhiên, dữ liệu giao dịch được tổng hợp từ nhiều chi nhánh và có nhiều lỗi về chất lượng.

Mục tiêu của bạn là xây dựng một dataset sạch trước khi nhóm phân tích sử dụng dữ liệu để tính doanh thu và đánh giá hiệu quả kinh doanh.

---

## 2. Dataset

File:

```text
retail_sales_dirty.csv
```

Các cột có thể gồm:

```text
Order_ID
Customer_ID
Region
Store
Order_Date
Product
Category
Quantity
Unit_Price
Revenue
Payment_Method
Discount
```

---

## 3. Một số vấn đề được cài vào dữ liệu

Dataset có thể chứa:

```text
Duplicate Order_ID

Region:
"Hanoi"
"HANOI"
" Ha Noi "
"ha noi"

Payment_Method:
"Cash"
"cash"
"CASH"
"Credit card"
"credit-card"

Order_Date:
2026-01-01
01/02/2026
Mar 03 2026
invalid-date

Quantity:
-2
0
500

Unit_Price:
missing values
negative values

Revenue:
không bằng Quantity × Unit_Price × (1 - Discount)

Discount:
0.1
10
10%
NaN
```

---

## 4. Nhiệm vụ

### Task 1 — Khám phá chất lượng dữ liệu

Kiểm tra:

```python
df.shape
df.info()
df.describe()
df.isna().sum()
df.duplicated().sum()
```

Xác định:

- numerical variables;
- categorical variables;
- identifiers;
- date variables.

---

### Task 2 — Duplicate Records

Kiểm tra:

```text
duplicate rows
duplicate Order_ID
```

Trả lời:

> Hai bản ghi có cùng Customer, Product và Revenue nhưng khác Order_ID có nên bị xóa không?

---

### Task 3 — Chuẩn hóa categorical variables

Chuẩn hóa:

```text
Region
Payment_Method
Category
```

Yêu cầu:

- loại khoảng trắng;
- lowercase hoặc title case nhất quán;
- mapping các nhãn tương đương.

---

### Task 4 — Chuẩn hóa ngày tháng

Chuyển:

```text
Order_Date
```

sang `datetime`.

Kiểm tra các ngày không hợp lệ.

---

### Task 5 — Missing Values

Tính:

```text
missing count
missing percentage
```

Đề xuất phương pháp xử lý cho:

```text
Unit_Price
Discount
Region
Payment_Method
```

---

### Task 6 — Business Rules

Kiểm tra:

```text
Quantity > 0

Unit_Price > 0

0 ≤ Discount ≤ 1
```

Sau đó tính:

$$
Expected\ Revenue
=
Quantity \times Unit\_Price \times (1-Discount)
$$

So sánh với:

```text
Revenue
```

---

### Task 7 — Outliers

Dùng:

```text
Boxplot
IQR
```

để kiểm tra outliers của:

```text
Quantity
Unit_Price
Revenue
```

Không tự động xóa outliers.

Phân loại mỗi trường hợp thành:

```text
Likely error
Valid but unusual
Needs investigation
```

---

### Task 8 — Validation

Kiểm tra cuối cùng:

```text
Duplicate Order_ID
Missing values
Invalid dates
Invalid quantity
Revenue mismatch
Unexpected categories
```

---

## 5. Câu hỏi phân tích sau Cleaning

Sau khi làm sạch dữ liệu:

1. Khu vực nào có doanh thu cao nhất?
2. Sản phẩm nào bán nhiều nhất?
3. Average Order Value là bao nhiêu?
4. Phương thức thanh toán nào phổ biến nhất?
5. Kết quả trên có thay đổi đáng kể so với dữ liệu chưa cleaning không?

---

## 6. Deliverables

Sinh viên nộp:

```text
retail_sales_clean.ipynb
retail_sales_clean.csv
cleaning_report.md
```

Trong báo cáo phải có bảng:

| Vấn đề | Số bản ghi | Cách xử lý | Lý do |
|---|---:|---|---|
| Duplicate Order_ID | ... | ... | ... |
| Missing Unit_Price | ... | ... | ... |
| Invalid Discount | ... | ... | ... |
| Revenue mismatch | ... | ... | ... |

---

# Project 2 — Làm sạch dữ liệu khảo sát thu nhập và chi tiêu hộ gia đình

## 1. Bối cảnh

Một nhóm nghiên cứu kinh tế muốn nghiên cứu mối quan hệ giữa:

```text
Income
Consumption
Household Size
Employment
Region
```

Dữ liệu đến từ một cuộc khảo sát hộ gia đình.

Các surveys thường chứa:

- missing values;
- non-response;
- sai đơn vị;
- outliers;
- inconsistent labels.

---

## 2. Dataset

File:

```text
household_economic_survey_dirty.csv
```

Các cột:

```text
Household_ID
Region
Urban_Rural
Household_Size
Monthly_Income
Monthly_Consumption
Food_Expenditure
Housing_Expenditure
Employment_Status
Education_Level
Survey_Date
```

---

## 3. Vấn đề dữ liệu

Ví dụ:

```text
Monthly_Income:
-1
999999999
"Unknown"
NaN

Monthly_Consumption:
đơn vị nghìn VND ở một số dòng
đơn vị VND ở các dòng khác

Household_Size:
0
-2
25

Region:
North
north
NORTH
Northern

Employment_Status:
Employed
employed
EMP
Unemployed
Un-employed

Education_Level:
High School
Bachelor
Master
PhD
unknown
```

---

## 4. Nhiệm vụ

### Task 1 — Chuẩn hóa missing codes

Chuyển:

```text
-1
999
"Unknown"
"N/A"
"NULL"
```

thành:

```python
np.nan
```

nếu chúng thực sự đại diện cho missing data.

---

### Task 2 — Phân tích Missing Values

Tính missing percentage cho từng biến.

Phân loại sơ bộ:

```text
Có thể là MCAR?
Có thể là MAR?
Có khả năng MNAR?
```

Ví dụ:

> Monthly_Income bị thiếu nhiều ở nhóm self-employed có thể không hoàn toàn ngẫu nhiên.

---

### Task 3 — Chuẩn hóa đơn vị

Đưa toàn bộ:

```text
Income
Consumption
Food_Expenditure
Housing_Expenditure
```

về cùng đơn vị:

```text
VND/month
```

---

### Task 4 — Kiểm tra phạm vi

Business/domain rules:

```text
Household_Size >= 1

Monthly_Income >= 0

Monthly_Consumption >= 0

Food_Expenditure >= 0

Housing_Expenditure >= 0
```

Kiểm tra:

$$
Food + Housing
\le
Total\ Consumption
$$

---

### Task 5 — Outlier Analysis

Kiểm tra:

```text
Monthly_Income
Monthly_Consumption
```

bằng:

```text
Boxplot
IQR
Log transformation
```

Trả lời:

> Hộ có thu nhập rất cao có nên bị loại khỏi dataset không?

---

### Task 6 — Imputation

Đề xuất và thực hiện một số phương án:

```text
Median Income
Median Income by Region
Median Income by Employment_Status
Mode for categorical variables
```

So sánh các lựa chọn.

---

### Task 7 — Validation

Xây dựng hàm:

```python
def validate_household_data(df):
    ...
```

trả về các chỉ số:

```text
missing_income
invalid_household_size
negative_consumption
expense_rule_violation
duplicate_household_id
```

---

## 5. Câu hỏi phân tích sau Cleaning

1. Thu nhập trung vị theo Region là bao nhiêu?
2. Urban và Rural có khác nhau về consumption không?
3. Tỷ lệ:

$$
Consumption / Income
$$

khác nhau thế nào giữa các nhóm?
4. Nhóm Education nào có income cao nhất?
5. Imputation có ảnh hưởng tới mean income không?

---

## 6. Deliverables

```text
household_cleaning.ipynb
household_clean.csv
data_quality_report.md
```

Báo cáo phải so sánh:

```text
Before Cleaning
vs
After Cleaning
```

cho:

```text
Mean Income
Median Income
Std Income
Missing Rate
Number of Observations
```

---

# Project 3 — Làm sạch dữ liệu CRM cho Customer Churn Analysis

## 1. Bối cảnh

Một công ty dịch vụ muốn xây dựng mô hình dự đoán:

```text
Customer Churn
```

Nhưng dữ liệu CRM được tích hợp từ:

```text
Sales System
Billing System
Customer Support
Marketing Platform
```

nên tồn tại nhiều lỗi.

Mục tiêu là xây dựng dataset sạch và sẵn sàng cho bước Machine Learning.

---

## 2. Dataset

File:

```text
customer_churn_dirty.csv
```

Các cột:

```text
Customer_ID
Age
Gender
Region
Join_Date
Monthly_Fee
Total_Spending
Contract_Type
Payment_Method
Support_Tickets
Last_Login
Churn
```

---

## 3. Các vấn đề dữ liệu

```text
Customer_ID duplicate

Age:
-5
0
145

Gender:
M
Male
male
F
Female
female

Region:
inconsistent labels

Join_Date:
mixed formats

Monthly_Fee:
missing

Total_Spending:
string ở một số records

Contract_Type:
Monthly
Month-to-month
monthly

Churn:
Yes
YES
1
No
0
N
```

---

## 4. Nhiệm vụ

### Task 1 — Kiểm tra schema

Kiểm tra:

```text
dtype
unique values
missing values
duplicates
```

---

### Task 2 — Chuẩn hóa target

Chuẩn hóa:

```text
Churn
```

về:

```text
0 = No
1 = Yes
```

Kiểm tra xem có label nào không thể mapping.

---

### Task 3 — Chuẩn hóa categorical variables

Làm sạch:

```text
Gender
Region
Contract_Type
Payment_Method
```

---

### Task 4 — Numeric conversion

Chuyển:

```text
Monthly_Fee
Total_Spending
Support_Tickets
```

sang kiểu numeric.

Dùng:

```python
pd.to_numeric(
    ...,
    errors="coerce"
)
```

---

### Task 5 — Date Cleaning

Chuẩn hóa:

```text
Join_Date
Last_Login
```

Tạo:

```text
Customer_Tenure
Days_Since_Last_Login
```

---

### Task 6 — Business Rules

Kiểm tra:

```text
18 ≤ Age ≤ 100

Monthly_Fee >= 0

Total_Spending >= 0

Support_Tickets >= 0

Join_Date <= Last_Login
```

---

### Task 7 — Missing Values

Đề xuất xử lý:

```text
Age
Monthly_Fee
Total_Spending
Region
```

Lưu ý:

> Nếu đây là dataset dùng cho Machine Learning, imputation statistics sau này chỉ nên được `fit` trên training set.

---

### Task 8 — Outliers

Kiểm tra:

```text
Total_Spending
Monthly_Fee
Support_Tickets
```

Outlier có thể là:

```text
high-value customer
problematic customer
data error
```

---

### Task 9 — Leakage Check

Kiểm tra có feature nào chứa thông tin xảy ra **sau khi khách hàng churn** hay không.

Ví dụ:

```text
Closure_Date
Cancellation_Reason
```

nếu xuất hiện thì có thể gây target leakage.

---

## 5. Câu hỏi sau Cleaning

1. Churn rate là bao nhiêu?
2. Contract Type nào có churn cao nhất?
3. Khách hàng churn có support tickets nhiều hơn không?
4. Total Spending của churn vs non-churn khác nhau thế nào?
5. Dataset đã sẵn sàng để train model chưa?

---

## 6. Deliverables

```text
churn_cleaning.ipynb
customer_churn_clean.csv
feature_quality_report.md
```

Trong báo cáo phải có một mục:

```text
Potential Data Leakage
```

---

# Project 4 — Làm sạch dữ liệu logistics và giao hàng

## 1. Bối cảnh

Một công ty logistics muốn đánh giá:

- delivery performance;
- chi phí vận chuyển;
- delay;
- carrier performance.

Dữ liệu giao hàng được thu từ nhiều kho và nhà vận chuyển nên không nhất quán.

---

## 2. Dataset

File:

```text
logistics_delivery_dirty.csv
```

Các cột:

```text
Shipment_ID
Warehouse
Carrier
Origin
Destination
Ship_Date
Expected_Delivery_Date
Actual_Delivery_Date
Distance
Distance_Unit
Weight
Weight_Unit
Shipping_Cost
Status
```

---

## 3. Vấn đề dữ liệu

```text
Shipment_ID duplicate

Carrier:
DHL
dhl
DHL Express
FedEx
FED EX

Dates:
mixed formats
Actual_Delivery_Date < Ship_Date

Distance:
km
miles

Weight:
kg
g
lb

Shipping_Cost:
negative
missing
extreme values

Status:
Delivered
delivered
Late
Delayed
Cancelled
Canceled
```

---

## 4. Nhiệm vụ

### Task 1 — Duplicate Shipments

Kiểm tra:

```text
duplicate Shipment_ID
```

Xác định record nào là bản cập nhật trạng thái và record nào là duplicate thật.

---

### Task 2 — Standardize Carrier và Status

Chuẩn hóa labels.

Ví dụ:

```text
"DHL Express" → "DHL"
"FED EX" → "FedEx"

"Late" → "Delayed"
"Canceled" → "Cancelled"
```

---

### Task 3 — Chuẩn hóa ngày tháng

Convert:

```text
Ship_Date
Expected_Delivery_Date
Actual_Delivery_Date
```

sang datetime.

Kiểm tra:

```text
Ship_Date <= Expected_Delivery_Date

Ship_Date <= Actual_Delivery_Date
```

---

### Task 4 — Chuẩn hóa đơn vị

Chuyển:

```text
Distance → km
Weight → kg
```

Ví dụ:

$$
1 mile \approx 1.60934 km
$$

$$
1 lb \approx 0.453592 kg
$$

---

### Task 5 — Missing Values

Đề xuất xử lý:

```text
Shipping_Cost
Actual_Delivery_Date
Carrier
```

Lưu ý:

> Actual_Delivery_Date có thể missing hợp lệ nếu shipment chưa giao.

---

### Task 6 — Feature Validation

Tạo:

$$
Delivery\ Delay
=
Actual\ Delivery\ Date
-
Expected\ Delivery\ Date
$$

Kiểm tra:

```text
negative delay
very large delay
```

---

### Task 7 — Outliers

Kiểm tra:

```text
Distance
Weight
Shipping_Cost
Delivery_Delay
```

bằng:

```text
boxplot
IQR
```

---

### Task 8 — Business Rules

Ví dụ:

```text
Distance > 0
Weight > 0
Shipping_Cost >= 0
```

Với shipment:

```text
Status = Delivered
```

thì:

```text
Actual_Delivery_Date
```

không nên missing.

---

### Task 9 — Validation

Viết hàm:

```python
def validate_logistics_data(df):
    ...
```

trả về:

```text
duplicate_shipments
invalid_dates
missing_delivered_dates
negative_costs
invalid_weight
invalid_distance
```

---

## 5. Câu hỏi phân tích sau Cleaning

1. Carrier nào có average delay thấp nhất?
2. Carrier nào có shipping cost/km thấp nhất?
3. Tuyến Origin–Destination nào bị delay nhiều nhất?
4. Tỷ lệ Delivered / Delayed / Cancelled là bao nhiêu?
5. Outliers trong Shipping_Cost có hợp lý sau khi xét Distance và Weight không?

---

## 6. Deliverables

```text
logistics_cleaning.ipynb
logistics_clean.csv
logistics_quality_report.md
```

---

# So sánh bốn Project

| Project | Bối cảnh | Trọng tâm Data Cleaning |
|---|---|---|
| 1. Retail Sales | Business Analytics | Duplicate, category, date, business rules, revenue |
| 2. Household Survey | Economics | Missing data, survey codes, units, income outliers |
| 3. Customer Churn | Data Science / CRM | Schema, target cleaning, leakage, ML readiness |
| 4. Logistics | Supply Chain | Units, dates, domain rules, delivery anomalies |

---

# Yêu cầu chung cho tất cả Projects

Mỗi project nên có ba giai đoạn.

## Giai đoạn 1 — Data Quality Assessment

Sinh viên phải lập bảng:

| Variable | Type | Missing | Unique | Suspected Problems |
|---|---|---:|---:|---|

---

## Giai đoạn 2 — Cleaning Log

Mỗi quyết định cleaning phải được ghi lại.

| Step | Variable | Problem | Action | Reason |
|---|---|---|---|---|

Ví dụ:

```text
1 | Region | inconsistent labels | lowercase + mapping | same semantic group
2 | Income | -1 codes | replace with NaN | data dictionary
3 | Revenue | mismatch | flag only | needs business review
```

---

## Giai đoạn 3 — Validation

Sinh viên cần báo cáo:

```text
Before Cleaning
After Cleaning
```

với ít nhất:

```text
Number of Rows
Number of Columns
Duplicate Count
Missing Count
Invalid Values
Potential Outliers
Business Rule Violations
```

---

# Rubric gợi ý

| Thành phần | Tỷ trọng |
|---|---:|
| Data quality assessment | 15% |
| Duplicate & structural cleaning | 15% |
| Missing-value treatment | 15% |
| Outlier analysis | 15% |
| Domain/business-rule validation | 15% |
| Code quality & reproducibility | 10% |
| Interpretation of cleaning decisions | 10% |
| Final report | 5% |

---

# Nguyên tắc quan trọng

Trong cả bốn project:

> **Không đánh giá sinh viên chỉ dựa trên việc dataset cuối cùng không còn missing values hay outliers.**

Một quyết định tốt có thể là:

```text
Keep the value
```

nếu người học chứng minh được rằng nó:

- hợp lệ;
- có ý nghĩa;
- và không nên bị loại bỏ.

Mục tiêu của project là:

```text
Understand the data
→ detect quality problems
→ make justified cleaning decisions
→ validate the result
```

chứ không phải:

```text
delete everything unusual
```
