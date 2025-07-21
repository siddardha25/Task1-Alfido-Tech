import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------------------
# Settings
# ---------------------------------------------------

csv_path = r"C:\Users\HP\OneDrive\Desktop\task 1\ecommerce_customer_data_custom_ratios.csv"
output_path = r"C:\Users\HP\OneDrive\Desktop\task 1\monthly_revenue_trend_clean.png"

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv(csv_path, encoding='latin1')

# Find the date and revenue columns
date_column = next((col for col in df.columns if 'date' in col.lower()), None)
revenue_column = next((col for col in df.columns if 'revenue' in col.lower() 
                       or 'sales' in col.lower() 
                       or 'total purchase' in col.lower()), None)

if not date_column or not revenue_column:
    print("[ERROR] Missing required columns.")
    exit()

# ---------------------------------------------------
# Prepare Data
# ---------------------------------------------------

df[date_column] = pd.to_datetime(df[date_column])
df['Year'] = df[date_column].dt.year
df['Month'] = df[date_column].dt.month

monthly_revenue = df.groupby(['Year', 'Month'])[revenue_column].sum().reset_index()

# ---------------------------------------------------
# Plot Clean Trend
# ---------------------------------------------------

sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Get unique years
years = sorted(monthly_revenue['Year'].unique())
palette = sns.color_palette("tab10", n_colors=len(years))

for i, year in enumerate(years):
    year_data = monthly_revenue[monthly_revenue['Year'] == year]
    plt.plot(
        year_data['Month'],
        year_data[revenue_column],
        label=str(year),
        marker='o',
        color=palette[i]
    )
    
    # Label only the LAST point for each year
    last_month = year_data.iloc[-1]['Month']
    last_value = year_data.iloc[-1][revenue_column]
    plt.text(
        last_month + 0.1, 
        last_value, 
        f"₹{last_value/1e5:.1f}L", 
        fontsize=9, 
        color=palette[i]
    )

plt.title("Monthly Revenue Trends by Year", fontsize=16, weight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Revenue (₹)", fontsize=12)
plt.xticks(range(1,13))
plt.legend(title="Year", loc='upper left')
plt.tight_layout()

plt.savefig(output_path, dpi=300)
plt.show()

print(f"[OK] Clean trend plot saved at:\n{output_path}")
