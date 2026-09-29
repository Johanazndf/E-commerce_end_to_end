# SQL practice tasks

Use these questions to practice the analysis yourself. Do not treat them as complete answers.

## Part 1: Core business questions
1. Calculate overall Sales, Profit, Quantity, Orders, and Customers.
2. Calculate Average Order Value.
3. Analyze Sales and Profit by Category.
4. Analyze Sales and Profit by Sub-Category.
5. Analyze Sales and Profit by Region.
6. Analyze Sales and Profit by Segment.
7. Identify loss-making Sub-Categories.
8. Find the top products by Sales.
9. Find the top products by Profit.
10. Find customers with sales above the average using a subquery.
11. Find products with sales above the average using a subquery.

## Part 2: CASE WHEN and segmentation
12. Create profitability categories such as High Profit, Moderate Profit, Low Profit, and Loss.
13. Create Discount Categories and analyze Sales, Profit, and Profit Margin by discount bucket.

## Part 3: CTE practice
14. Calculate monthly sales using a CTE.
15. Create a customer-level summary using a CTE.
16. Use a CTE to classify customers into value groups.

## Part 4: Window functions
17. Rank products within each Category using RANK and PARTITION BY.
18. Find the top 3 products within each Category using CTE + RANK.
19. Calculate monthly running Sales using SUM() OVER().
20. Calculate month-over-month Sales change using LAG().

## Optional advanced practice
21. Rank customers by total sales.
22. Rank regions by total sales.
23. Compare sales and profit by shipping mode.
24. Use a LEFT JOIN to compare sales by customer and region if you add a customer dimension table.

## How to use this file
- Try each question before asking for the solution.
- If stuck, ask for a hint.
- If you want the full query, ask for it after your attempt.
- For each solution, explain:
  - business purpose
  - query logic
  - execution order
  - why the CTE or window function is needed
  - how to explain it in an interview
