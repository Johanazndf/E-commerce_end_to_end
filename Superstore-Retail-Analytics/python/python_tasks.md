# Python / Pandas learning tasks

Use Python only after your Excel and SQL work is complete.

## Task 1: Initial inspection
Start with:
- df.head()
- df.shape
- df.columns
- df.info()
- df.describe()
- df.isnull().sum()
- df.duplicated().sum()

## Task 2: Data type validation
- Check that date columns are datetime-like.
- Confirm numeric columns are numeric.
- Check whether there are any non-standard values in text columns.

## Task 3: Missing value review
- Count missing values by column.
- Decide whether missing values are a true issue or simply formatting noise.

## Task 4: Duplicate analysis
- Count duplicate rows.
- Review whether repeated Order IDs are actually duplicates or valid multi-product orders.

## Task 5: Descriptive statistics
- Summarize Sales, Quantity, Discount, and Profit.
- Review min, max, average, and percentiles.

## Task 6: Monthly analysis
- Analyze monthly sales.
- Analyze monthly profit.
- Look for trends and outliers by month.

## Task 7: Category and sub-category analysis
- Summarize sales and profit by Category.
- Summarize by Sub-Category.
- Identify which product groups contribute more or less than expected.

## Task 8: Region and segment analysis
- Break down sales and profit by Region.
- Break down sales and profit by Segment.
- Compare performance across customer groups and territories.

## Task 9: Product and customer analysis
- Find top-selling products.
- Find the most profitable products.
- Review top customers by sales.

## Task 10: Discount vs Profit
- Explore the relationship between Discount and Profit.
- Do not make a conclusion before reviewing the actual numbers and chart.

## Task 11: Shipping analysis
- Calculate Shipping Days.
- Review whether shipping delays are common or unusual.
- Check whether order dates and ship dates are consistent.

## Task 12: Visualization
Use Matplotlib to create simple charts for:
- sales by category
- monthly sales trend
- profit by region
- discount vs profit
- top products

## Final requirement
Do not hand in a completed notebook prematurely. Build the analysis step by step, and only write business findings after the calculation is complete.
