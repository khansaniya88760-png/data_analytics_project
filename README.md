# Online Shopping Data Analysis

A beginner-friendly Python data analysis project on an online shopping orders dataset. It covers data cleaning, exploratory analysis, and visualisation using **pandas**, **NumPy**, **matplotlib** and **seaborn**.

**Author:** Saniya
**Repository:** https://github.com/khansaniya88760-png/data_analytics_project

---

## Objective

To understand customer buying behaviour on an online shopping platform by answering questions such as:

- Which product categories earn the most revenue?
- Which cities place the most orders?
- How do customers prefer to pay?
- How does revenue change over time?
- Which factors are related to customer ratings and order value?

---

## Dataset

**File:** `shopping_data.csv` (255 rows, 12 columns, orders from Nov 2024 to Nov 2026)

| Column | Description |
|---|---|
| `Order_ID` | Unique order identifier |
| `Order_Date` | Date the order was placed |
| `City` | Customer city |
| `Product_Category` | Electronics, Fashion, Home_Kitchen, Beauty, Books |
| `Payment_Mode` | UPI, Debit_Card, Cash_on_Delivery, Credit_Card |
| `Customer_Type` | New, Returning, Prime |
| `Items_Count` | Number of items in the order |
| `Order_Value_INR` | Order amount in Indian rupees |
| `Discount_Percent` | Discount applied (%) |
| `Delivery_Days` | Days taken to deliver |
| `Browsing_Time_Min` | Time spent browsing before ordering (minutes) |
| `Customer_Rating` | Rating given by the customer (1 to 5) |

---

## Data Cleaning

The raw data had several quality problems, which were fixed before analysis:

| Issue | Fix |
|---|---|
| 5 duplicate rows | Removed with `drop_duplicates()` (250 orders remain) |
| Inconsistent city names (`delhi`, `LUCKNOW`, ` Kolkata `) | Stripped spaces and standardised case (12 variants become 5 cities) |
| Invalid discounts (135% and -20%) | Treated as missing values |
| Missing values in `Customer_Type`, `Order_Value_INR`, `Delivery_Days`, `Browsing_Time_Min` | Left as missing and excluded from the charts that use them |
| Very large orders (up to about ₹30,000) | Kept, as they look like genuine high-value purchases |

---

## Key Findings

- **Total revenue** is about ₹8.97 lakh across 250 orders. The average order is about ₹3,660, while the median is ₹1,687, so a few large orders pull the average up.
- **Electronics** earns about ₹5.7 lakh, which is more than all other categories combined. Fashion (about ₹1.7 lakh) is second.
- **Delhi** has the most orders (65), followed by Bengaluru (55), Mumbai (53), Kolkata (47) and Lucknow (30).
- **UPI** is the most popular payment mode (about 46%), followed by Debit Card (22%), Cash on Delivery (20%) and Credit Card (12%).
- **Returning customers** make up about half of all orders with a known customer type.
- **Delivery days and ratings** show a moderate negative correlation (about -0.42): slower delivery tends to go with lower ratings.
- **Discount and ratings** show a moderate positive correlation (about 0.47).
- **Items count** is the factor most related to order value (about 0.37).

> Correlation does not prove cause. These are patterns in a small dataset, not firm conclusions.

---

## Visualisations

The charts are saved in the `charts/` folder.

| Chart | What it shows |
|---|---|
| `1_revenue_by_category.png` | Total revenue per product category |
| `2_orders_by_city.png` | Number of orders per city |
| `3_payment_mode_share.png` | Share of each payment mode |
| `4_customer_type.png` | Orders by customer type |
| `5_monthly_revenue_trend.png` | Revenue over time |
| `6_order_value_distribution.png` | Distribution of order values |
| `7_rating_by_category.png` | Ratings by product category |
| `8_discount_vs_order_value.png` | Discount vs order value |
| `9_delivery_days_vs_rating.png` | Average rating by delivery days |
| `10_correlation_heatmap.png` | Correlation between numeric columns |

---

## Tools and Libraries

- Python 3
- pandas
- NumPy
- matplotlib
- seaborn

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/khansaniya88760-png/data_analytics_project.git
   cd data_analytics_project
   ```
2. Install the libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the script to clean the data and generate all charts:
   ```bash
   python charts.py
   ```

Make sure `shopping_data.csv` is in the same folder, and update the file path inside `charts.py` if needed.

---

## Project Structure

```
data_analytics_project/
├── shopping_data.csv     # raw dataset
├── charts.py             # cleaning + chart generation code
├── charts/               # generated chart images
└── README.md
```

---

## Future Improvements

- Add a Jupyter notebook that walks through each step
- Fill missing values instead of excluding them
- Add statistical tests for the relationships found
- Build a simple dashboard
