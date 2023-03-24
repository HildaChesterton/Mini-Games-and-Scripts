import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('data.csv')

# Clean data
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
df['Value'] = df['Value'].str.replace(',', '').astype(float)

# Analyze data
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
monthly_sales = df.groupby(['Year', 'Month'])['Value'].sum()
yearly_sales = df.groupby(['Year'])['Value'].sum()

# Visualize data
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(monthly_sales.index, monthly_sales.values)
ax.set_xticks(range(1, 13))
ax.set_xticklabels([str(i) for i in range(1, 13)])
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Monthly Sales')
plt.show()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(yearly_sales.index, yearly_sales.values, '-o')
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_title('Yearly Sales')
plt.show()
