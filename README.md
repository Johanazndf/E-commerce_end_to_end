# End-to-End Retail Analytics Project

A practical retail analytics project built using the Sample Superstore dataset to demonstrate end-to-end data analysis from raw data validation to business insight generation and dashboard storytelling.

## Project Overview

This project follows a real-world Data Analyst workflow:

- Excel for data quality checks and cleaning
- SQL for business analysis
- Python / Pandas for exploratory data analysis
- Power BI for dashboard storytelling and executive communication

The goal is not just to build a dashboard, but to show the full analytical process from raw data to actionable business insights.

## Business Problem

The business needed a clear view of:
- sales performance,
- profitability by category and region,
- customer and product contribution,
- loss-making product groups,
- and overall business health across segments.

The challenge was to validate the data, answer business questions with evidence, and then translate the findings into an insight-driven dashboard.

## Tools Used

- Excel
- SQL
- Python
- Pandas
- Power BI

## Dataset

The project uses the Superstore retail dataset, which includes information about:
- orders,
- customers,
- products,
- sales,
- profit,
- shipping,
- categories, regions, and segments.

## Workflow

### 1. Excel
- checked rows and columns
- reviewed missing values
- checked duplicates
- validated date fields
- reviewed suspicious numeric values
- created calculated fields such as Shipping Days and Profit Margin %

### 2. SQL
- analyzed sales, profit, customers, and orders
- reviewed category, region, and segment performance
- identified top products
- found loss-making sub-categories
- evaluated monthly trends

### 3. Python / Pandas
- validated dataset quality
- summarized KPIs
- explored monthly trend patterns
- compared category and sub-category performance
- confirmed the main business signals

### 4. Power BI
- final storytelling layer
- KPI cards and executive summary view
- category and product performance views
- slicers for filtering by region, category, and segment

## Verified Results

The analysis was validated using the dataset and confirmed the following:

- 9,994 rows
- no missing values
- no duplicate rows
- Total Sales: $2,297,200.86
- Total Profit: $286,397.02
- Profit Margin: 12.47%
- Total Orders: 5,009
- Total Customers: 793

## Key Findings

- Technology was the strongest category by both sales and profit.
- Furniture underperformed relative to the other categories.
- The main loss-making sub-categories were:
  - Tables
  - Bookcases
  - Supplies
- Consumer segment generated the highest sales.
- West region was the strongest sales and profit region.
- The business is healthy overall, but profitability is concentrated in a few stronger categories and products.

## Project Structure

- data/
  - raw Superstore dataset
- excel/
  - Excel validation and cleaning notes
- sql/
  - SQL analysis queries
- python/
  - Pandas exploratory analysis scripts
- powerbi/
  - dashboard plan and story structure
- insights.md
- interview_questions.md
- project_summary.md

## Power BI Status

The analysis phase is complete and validated. The final Power BI dashboard is the final presentation layer to communicate the findings visually to stakeholders.

## Why This Project Matters

This project demonstrates practical analytical thinking, not just chart creation. It shows the ability to:
- validate raw data,
- perform business analysis,
- use SQL and Python to answer real questions,
- and communicate results clearly in a dashboard.



