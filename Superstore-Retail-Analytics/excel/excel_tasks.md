# Excel tasks

Work on this phase manually. Do not use Python to generate the final Excel outputs.

## Task 1: Initial inspection
- Open the raw dataset.
- Check the number of rows and columns.
- Review the column names and confirm they match the expected retail dataset structure.
- Check the row count and note whether it is realistic for this data source.

## Task 2: Data types and schema
- Confirm the data types for each column.
- Check whether dates are stored in a valid date format.
- Check whether sales, quantity, discount, and profit are numeric.
- Look for inconsistent text values in segment, region, category, sub-category, product, customer, and city fields.

## Task 3: Missing values
- Review missing values by column.
- Focus on the key fields listed in the project brief.
- Record which fields have nulls and whether the issue is real or a formatting problem.

## Task 4: Duplicate review
- Identify duplicate rows using the full row record.
- Do not assume duplicate Order IDs are duplicates.
- Explain why one order can contain multiple products.

## Task 5: Suspicious values
Check the following:
- Quantity <= 0
- Sales <= 0
- Discount < 0
- Discount > 1
- Ship Date < Order Date

Do not delete rows automatically. First decide whether the row is a true error or a legitimate business condition.

## Task 6: Text cleanup
Use Excel functions such as:
- TRIM
- CLEAN
- PROPER
- UPPER
- LOWER
- SUBSTITUTE

Standardize where needed.

## Task 7: Calculated columns
Create these exactly when needed:
- Shipping Days = Ship Date - Order Date
- Profit Margin % = Profit / Sales * 100

## Task 8: KPI calculations
Create the following KPIs:
- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Total Quantity
- Average Order Value
- Profit Margin %
- Average Discount
- Average Shipping Days

## Task 9: PivotTables and analysis
Create PivotTables for:
- Sales by Category
- Profit by Category
- Sales by Sub-Category
- Profit by Sub-Category
- Sales by Region
- Profit by Region
- Sales by Segment
- Profit by Segment
- Monthly Sales
- Monthly Profit
- Top 10 Products by Sales
- Top 10 Products by Profit
- Bottom 10 Products by Profit
- Customer-level sales
- Discount vs Profit
- Shipping performance

## Task 10: Final Excel review
Before moving on, answer these questions:
- What is clean and ready for analysis?
- What fields needed cleaning?
- Which risks remained after validation?
- Which numbers need to be explained in your interview?

When you are ready, ask for a hint or for the full solution for a specific Excel task.
