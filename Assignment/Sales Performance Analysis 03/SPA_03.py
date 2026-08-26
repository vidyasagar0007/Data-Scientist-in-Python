import numpy as np
import pandas as pd

# Given Dataset
sales = np.array([
    [12000, 15000, 18000],
    [10000, 14000, 16000],
    [18000, 20000, 22000],
    [9000, 12000, 15000],
    [15000, 17000, 19000]
])

# Columns:
# January | February | March

# 1. Total sales of each salesperson
total_sales = np.sum(sales, axis=1)
print("1. Total sales of each salesperson:")
print(total_sales)

# 2. Average monthly sales for each salesperson
average_sales = np.mean(sales, axis=1)
print("\n2. Average monthly sales:")
print(average_sales)

# 3. Highest sales achieved in each month
highest_monthly_sales = np.max(sales, axis=0)
print("\n3. Highest sales in each month:")
print(highest_monthly_sales)

# 4. Lowest sales achieved in each month
lowest_monthly_sales = np.min(sales, axis=0)
print("\n4. Lowest sales in each month:")
print(lowest_monthly_sales)

# 5. Salesperson with the highest total sales
highest_salesperson_index = np.argmax(total_sales)
print("\n5. Salesperson with highest total sales:")
print("Salesperson", highest_salesperson_index + 1)
print("Total Sales:", total_sales[highest_salesperson_index])

# 6. Salespersons whose average sales are above ₹15,000
above_15000 = np.where(average_sales > 15000)[0]
print("\n6. Salespersons with average sales above ₹15,000:")
print(above_15000 + 1)

# 7. Total company sales for each month
company_monthly_sales = np.sum(sales, axis=0)
print("\n7. Total company sales for each month:")
print(company_monthly_sales)

# 8. Standard deviation of monthly sales
monthly_std = np.std(sales, axis=0)
print("\n8. Standard deviation of monthly sales:")
print(monthly_std)

# 9. Classify salespersons using np.where()
# Average >= 18000 -> Excellent
# Average >= 15000 -> Good
# Otherwise -> Needs Improvement

performance = np.where(
    average_sales >= 18000,
    "Excellent",
    np.where(
        average_sales >= 15000,
        "Good",
        "Needs Improvement"
    )
)

print("\n9. Salesperson Classification:")
print(performance)

# 10. Convert final results into Pandas DataFrame
df = pd.DataFrame(
    sales,
    columns=["January", "February", "March"]
)

df["Total Sales"] = total_sales
df["Average Sales"] = average_sales
df["Performance"] = performance

print("\n10. Final DataFrame:")
print(df)