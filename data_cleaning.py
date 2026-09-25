import pandas as pd

# ==========================================
# 1. LOAD RAW DATA
# ==========================================

df = pd.read_csv("ecommerce_sales_analytics_5000.csv")

print("Original Shape:", df.shape)


# ==========================================
# 2. CONVERT DATE
# ==========================================

df["order_date"] = pd.to_datetime(df["order_date"])


# ==========================================
# 3. CHECK DUPLICATES
# ==========================================

print("Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()


# ==========================================
# 4. CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 5. DATA VALIDATION
# ==========================================

print("\nQuantity Range:", df["quantity"].min(), "-", df["quantity"].max())
print("Discount Range:", df["discount"].min(), "-", df["discount"].max())
print("Rating Range:", df["customer_rating"].min(), "-", df["customer_rating"].max())
print("Delivery Days Range:", df["delivery_days"].min(), "-", df["delivery_days"].max())


# ==========================================
# 6. CHECK REVENUE CALCULATION
# ==========================================

df["calculated_revenue"] = (
    df["quantity"]
    * df["unit_price"]
    * (1 - df["discount"])
)

df["revenue_difference"] = (
    df["revenue"] - df["calculated_revenue"]
)

print("\nMaximum Revenue Difference:",
      df["revenue_difference"].abs().max())


# ==========================================
# 7. REMOVE TEMPORARY VALIDATION COLUMNS
# ==========================================

df = df.drop(columns=[
    "calculated_revenue",
    "revenue_difference"
])


# ==========================================
# 8. SAVE CLEANED DATA
# ==========================================

df.to_csv(
    "ecommerce_sales_analytics_5000_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")
print("Final Shape:", df.shape)