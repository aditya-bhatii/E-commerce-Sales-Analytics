import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

df = pd.read_csv("ecommerce_sales_analytics_5000_cleaned.csv")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# 2. FEATURE ENGINEERING
# ==========================================

# Year
df["year"] = df["order_date"].dt.year

# Month
df["month"] = df["order_date"].dt.month

# Month Name
df["month_name"] = df["order_date"].dt.month_name()

# Gross sales before discount
df["gross_sales"] = df["quantity"] * df["unit_price"]

# Discount amount
df["discount_amount"] = df["gross_sales"] * df["discount"]


# ==========================================
# 3. KEY BUSINESS METRICS
# ==========================================

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_quantity = df["quantity"].sum()
total_customers = df["customer_id"].nunique()
average_order_value = total_revenue / total_orders
average_rating = df["customer_rating"].mean()
average_delivery = df["delivery_days"].mean()

print("\n========== KEY METRICS ==========")

print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))
print("Average Customer Rating:", round(average_rating, 2))
print("Average Delivery Days:", round(average_delivery, 2))


# ==========================================
# 4. CATEGORY ANALYSIS
# ==========================================

category_sales = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY CATEGORY ==========")
print(category_sales)


# ==========================================
# 5. REGION ANALYSIS
# ==========================================

region_sales = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY REGION ==========")
print(region_sales)


# ==========================================
# 6. PAYMENT METHOD ANALYSIS
# ==========================================

payment_sales = (
    df.groupby("payment_method")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY PAYMENT METHOD ==========")
print(payment_sales)





