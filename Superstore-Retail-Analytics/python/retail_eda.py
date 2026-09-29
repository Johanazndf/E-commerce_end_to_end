import pandas as pd

path = r'E:\endtoend\Superstore-Retail-Analytics\data\Sample - Superstore.csv'
df = pd.read_csv(path, encoding='cp1252')

# Convert the date fields to actual datetime values
for col in ['Order Date', 'Ship Date']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Create derived columns

df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Profit Margin %'] = (df['Profit'] / df['Sales'] * 100).replace([float('inf'), float('-inf')], float('nan'))

print('Shape:', df.shape)
print('Missing values:\n', df.isna().sum())
print('Duplicate rows:', df.duplicated().sum())

# KPI summary
summary = {
    'Total Sales': df['Sales'].sum(),
    'Total Profit': df['Profit'].sum(),
    'Total Orders': df['Order ID'].nunique(),
    'Total Customers': df['Customer ID'].nunique(),
    'Total Quantity': df['Quantity'].sum(),
    'Average Order Value': df.groupby('Order ID')['Sales'].sum().mean(),
    'Profit Margin %': df['Profit'].sum() / df['Sales'].sum() * 100,
    'Average Discount': df['Discount'].mean(),
    'Average Shipping Days': df['Shipping Days'].mean(),
}

for k, v in summary.items():
    print(f'{k}: {v}')

print('\nCategory sales:')
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False).to_string())

print('\nCategory profit:')
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False).to_string())

print('\nLoss-making sub-categories:')
print(df.groupby('Sub-Category')['Profit'].sum().loc[lambda x: x < 0].sort_values().to_string())

print('\nTop 10 products by sales:')
print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).to_string())

print('\nTop 10 products by profit:')
print(df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10).to_string())

print('\nMonthly sales trend:')
monthly_sales = df.assign(Month=df['Order Date'].dt.to_period('M').astype(str)).groupby('Month')['Sales'].sum().sort_index()
print(monthly_sales.to_string())

print('\nMonthly profit trend:')
monthly_profit = df.assign(Month=df['Order Date'].dt.to_period('M').astype(str)).groupby('Month')['Profit'].sum().sort_index()
print(monthly_profit.to_string())
