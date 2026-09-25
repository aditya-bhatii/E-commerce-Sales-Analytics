------
-- ========================================================
-- ==========
-- ---											ECOMMERCE SALES ANALYTICS
---											SQL BUSINESS ANALYTICS
---											DATABASE : ecommerce_analytics
---											TABLE : ecommerce_sales
-- ========================================================
-- ==========



-- CREATE TABLE ecommerce_sales (
--     order_id VARCHAR(50),
--     order_date DATE,
--     customer_id VARCHAR(50),
--     product_category VARCHAR(100),
--     region VARCHAR(50),
--     quantity INTEGER,
--     unit_price DECIMAL(10,2),
--     discount DECIMAL(10,2),
--     payment_method VARCHAR(50),
--     delivery_days INTEGER,
--     customer_rating DECIMAL(3,2),
--     revenue DECIMAL(12,2)
-- );



-----
-- ========================================================
-- ==========
--01. DATA VALIDATION
---- Check Total Number of records!!
----
-- ========================================================
-- ==========

SELECT Count(*) AS total_records
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--02. TOTAL REVENUE
---- What is the Total Revenue Generated?
----
-- ========================================================
-- ==========

SELECT SUM(revenue) AS total_revenue
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--03. TOTAL ORDERS
---- How many Unique Orders were Places?
----
-- ========================================================
-- ==========

SELECT 
		COUNT(Distinct order_id) AS total_orders
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--04. TOTAL CUSTOMERS
---- How many Unique Customers made purchase?
----
-- ========================================================
-- ==========

SELECT 
		COUNT (Distinct customer_id) AS
		total_customers
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--05. TOTAL QUANTITY SOLD
---- How many Total Units were sold?
----
-- ========================================================
-- ==========

SELECT 
		SUM(quantity) AS 
		total_quantity_sold
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--06.AVERAGE ORDER VALUE
---- What is the Average Revenue Generated Per order?
----
-- ========================================================
-- ==========

SELECT
		ROUND(
				SUM(revenue)/ COUNT(Distinct order_id),2
		) AS average_order_value
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--07. REVENUE BY PRODUCT CATEGORY
---- Which Product Categories Generate the most Revenue?
----
-- ========================================================
-- ==========

SELECT 
		product_category,
		SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY product_category
ORDER BY total_revenue DESC;



-----
-- ========================================================
-- ==========
--08.ORDER BY PRODUCT CATEGORY
---- How many Orders were Placed in each Category
----
-- ========================================================
-- ==========

SELECT
		product_category,
		COUNT(Distinct order_id) AS total_orders
FROM ecommerce_sales
GROUP BY product_category
ORDER BY total_orders DESC;



-----
-- ========================================================
-- ==========
--09.REVENUE BY REGION
---- How many Revenue does each Region Generate?
----
-- ========================================================
-- ==========

SELECT 
		region,
		SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY region
ORDER BY total_revenue DESC;



-----
-- ========================================================
-- ==========
--10.ORDERS BY REGION
---- How many orders were placed in each region?
----
-- ========================================================
-- ==========

SELECT 
		region,
		COUNT(Distinct order_id) AS total_orders
FROM ecommerce_sales
GROUP BY region
ORDER BY total_orders DESC;



-----
-- ========================================================
-- ==========
--11.REVENUE BY PAYMENT METHOD
---- Which payment methods generate the most revenue ?
----
-- ========================================================
-- ==========

SELECT 
		payment_method,
		SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY payment_method
ORDER BY total_revenue DESC;



-----
-- ========================================================
-- ==========
--12.SALES BY MONTH
---- How does revenue change month by month?
----
-- ========================================================
-- ==========

SELECT
		Date_Trunc('month',order_date) AS sales_month,
		SUM(revenue) AS monthly_revenue
FROM ecommerce_sales
GROUP BY sales_month
ORDER BY sales_month;



-----
-- ========================================================
-- ==========
--13.TOP 10 CUSTOMERS
---- Which customers generate the highest revenue?
----
-- ========================================================
-- ==========

SELECT
		customer_id,
		SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;



-----
-- ========================================================
-- ==========
--14.AVERAGE CUSTOMER RATING BY CATEGORY
---- What is the average customer rating for each category?
----
-- ========================================================
-- ==========

SELECT 
		product_category,
		ROUND(AVG(customer_rating),2) AS average_rating
FROM ecommerce_sales
GROUP BY product_category
ORDER BY average_rating DESC;



-----
-- ========================================================
-- ==========
--15.AVERAGE DELIVERY TIME BY REGION
---- What is the average delivery time in each region?
----
-- ========================================================
-- ==========

SELECT 
		region,
		ROUND(AVG(delivery_days),2) AS average_delivery_days
FROM ecommerce_sales
GROUP BY region
ORDER BY average_delivery_days;



-----
-- ========================================================
-- ==========
--16.DISCOUNT ANALYSIS
---- What is the average discount offered?
----
-- ========================================================
-- ==========

SELECT
		ROUND(AVG(discount),2) AS average_discount
FROM ecommerce_sales;



-----
-- ========================================================
-- ==========
--17. CATEGORY + REGION ANALYSIS
---- How does each category perform across different region?
----
-- ========================================================
-- ==========

SELECT 
		product_category
		region,
		SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY product_category , region
ORDER BY total_revenue DESC;



-- ============================================================
-- 18. HIGH-VALUE ORDERS
-- Which orders generated more than ₹5,000 revenue?
-- ============================================================

SELECT
    order_id,
    customer_id,
    product_category,
    region,
    revenue
FROM ecommerce_sales
WHERE revenue > 5000
ORDER BY revenue DESC;



-- ============================================================
-- 19. CATEGORY RANKING BY REGION
-- Rank product categories based on revenue within each region
-- ============================================================

SELECT
    region,
    product_category,
    SUM(revenue) AS total_revenue,
    RANK() OVER (
        PARTITION BY region
        ORDER BY SUM(revenue) DESC
    ) AS category_rank
FROM ecommerce_sales
GROUP BY region, product_category
ORDER BY region, category_rank;



-- ============================================================
-- 20. MONTHLY REVENUE WITH RUNNING TOTAL
-- Track monthly revenue and cumulative revenue over time
-- ============================================================

WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date) AS sales_month,
        SUM(revenue) AS monthly_revenue
    FROM ecommerce_sales
    GROUP BY DATE_TRUNC('month', order_date)
)

SELECT
    sales_month,
    monthly_revenue,
    SUM(monthly_revenue) OVER (
        ORDER BY sales_month
    ) AS cumulative_revenue
FROM monthly_sales
ORDER BY sales_month;