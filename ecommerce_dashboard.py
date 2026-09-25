import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =========================
# LOAD CLEANED DATA
# =========================

file = "ecommerce_sales_analytics_5000_cleaned.csv"

df = pd.read_csv(file)

# Date conversion
df["order_date"] = pd.to_datetime(df["order_date"])

# =========================
# CALCULATIONS
# =========================

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_quantity = df["quantity"].sum()

# Monthly revenue
monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
    .reset_index()
)

monthly_revenue["order_date"] = monthly_revenue["order_date"].astype(str)

# Region
region_sales = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Category
category_sales = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Payment method
payment_sales = (
    df.groupby("payment_method")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Top customers
top_customers = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Average rating
rating = (
    df.groupby("product_category")["customer_rating"]
    .mean()
    .sort_values(ascending=False)
)

# Average delivery days
delivery = (
    df.groupby("region")["delivery_days"]
    .mean()
    .sort_values()
)

# =========================
# DASHBOARD
# =========================

fig = make_subplots(
    rows=5,
    cols=2,
    specs=[
        [{"type": "indicator"}, {"type": "indicator"}],
        [{"type": "indicator"}, {"type": "indicator"}],
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "domain"}],
        [{"type": "xy"}, {"type": "xy"}],
    ],
    subplot_titles=(
        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Total Quantity",
        "Monthly Revenue",
        "Revenue by Region",
        "Revenue by Category",
        "Revenue by Payment Method",
        "Top 10 Customers",
        "Average Delivery Days by Region"
    ),
    vertical_spacing=0.08,
    horizontal_spacing=0.08
)

# =========================
# KPI 1
# =========================

fig.add_trace(
    go.Indicator(
        mode="number",
        value=total_revenue,
        number={"prefix": "₹", "valueformat": ",.0f"}
    ),
    row=1, col=1
)

# =========================
# KPI 2
# =========================

fig.add_trace(
    go.Indicator(
        mode="number",
        value=total_orders,
        number={"valueformat": ",.0f"}
    ),
    row=1, col=2
)

# =========================
# KPI 3
# =========================

fig.add_trace(
    go.Indicator(
        mode="number",
        value=total_customers,
        number={"valueformat": ",.0f"}
    ),
    row=2, col=1
)

# =========================
# KPI 4
# =========================

fig.add_trace(
    go.Indicator(
        mode="number",
        value=total_quantity,
        number={"valueformat": ",.0f"}
    ),
    row=2, col=2
)

# =========================
# MONTHLY REVENUE
# =========================

fig.add_trace(
    go.Scatter(
        x=monthly_revenue["order_date"],
        y=monthly_revenue["revenue"],
        mode="lines+markers",
        name="Revenue"
    ),
    row=3, col=1
)

# =========================
# REGION SALES
# =========================

fig.add_trace(
    go.Bar(
        x=region_sales.index,
        y=region_sales.values,
        name="Region Revenue"
    ),
    row=3, col=2
)

# =========================
# CATEGORY SALES
# =========================

fig.add_trace(
    go.Bar(
        x=category_sales.index,
        y=category_sales.values,
        name="Category Revenue"
    ),
    row=4, col=1
)

# =========================
# PAYMENT METHOD
# =========================

fig.add_trace(
    go.Pie(
        labels=payment_sales.index,
        values=payment_sales.values,
        hole=0.4,
        name="Payment"
    ),
    row=4, col=2
)

# =========================
# TOP CUSTOMERS
# =========================

fig.add_trace(
    go.Bar(
        x=top_customers.index.astype(str),
        y=top_customers.values,
        name="Customer Revenue"
    ),
    row=5, col=1
)

# =========================
# DELIVERY DAYS
# =========================

fig.add_trace(
    go.Bar(
        x=delivery.index,
        y=delivery.values,
        name="Delivery Days"
    ),
    row=5, col=2
)

# =========================
# DASHBOARD DESIGN
# =========================

fig.update_layout(
    title="E-Commerce Sales Analytics Dashboard",
    height=1800,
    width=1400,
    showlegend=False,
    template="plotly_white"
)

fig.update_yaxes(title_text="Revenue", row=3, col=1)
fig.update_yaxes(title_text="Revenue", row=3, col=2)
fig.update_yaxes(title_text="Revenue", row=4, col=1)
fig.update_yaxes(title_text="Revenue", row=5, col=1)
fig.update_yaxes(title_text="Days", row=5, col=2)

# =========================
# SHOW DASHBOARD
# =========================

fig.show()

print("\n====================================")
print("STEP 7 COMPLETED")
print("E-COMMERCE DASHBOARD CREATED")
print("====================================")