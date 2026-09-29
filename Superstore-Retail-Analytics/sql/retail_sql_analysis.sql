-- 1) Overall KPI summary
SELECT
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    COUNT(DISTINCT Order_ID) AS total_orders,
    COUNT(DISTINCT Customer_ID) AS total_customers,
    SUM(Quantity) AS total_quantity,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS avg_order_value,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Discount), 4) AS avg_discount
FROM superstore;

-- 2) Sales and profit by category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS sales,
    ROUND(SUM(Profit), 2) AS profit
FROM superstore
GROUP BY Category
ORDER BY sales DESC;

-- 3) Sales and profit by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS sales,
    ROUND(SUM(Profit), 2) AS profit
FROM superstore
GROUP BY Region
ORDER BY sales DESC;

-- 4) Loss-making sub-categories
SELECT
    `Sub-Category`,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- 5) Top products by sales
SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS total_sales
FROM superstore
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;

-- 6) Top products by profit
SELECT
    `Product Name`,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY `Product Name`
ORDER BY total_profit DESC
LIMIT 10;

-- 7) Monthly sales trend
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS month,
    ROUND(SUM(Sales), 2) AS monthly_sales
FROM superstore
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY month;

-- 8) Customer value ranking
SELECT
    Customer_ID,
    ROUND(SUM(Sales), 2) AS total_sales
FROM superstore
GROUP BY Customer_ID
ORDER BY total_sales DESC
LIMIT 10;
