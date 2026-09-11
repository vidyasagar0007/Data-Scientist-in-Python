import numpy as np
import pandas as pd

# ============================================================
# PROJECT 5: PRODUCT SALES ANALYSIS
# ============================================================

# Given Dataset
sales = np.array([
    [100, 120, 150],
    [80, 100, 130],
    [150, 160, 180],
    [70, 90, 110],
    [120, 140, 160]
])

# Product names and months
products = [
    "Product 1",
    "Product 2",
    "Product 3",
    "Product 4",
    "Product 5"
]

months = ["January", "February", "March"]


# ============================================================
# 1. TOTAL SALES FOR EVERY PRODUCT
# ============================================================

total_sales = np.sum(sales, axis=1)

print("\n1. Total Sales of Every Product:")

for i in range(len(products)):
    print(f"{products[i]}: {total_sales[i]}")


# ============================================================
# 2. AVERAGE MONTHLY SALES FOR EVERY PRODUCT
# ============================================================

average_sales = np.mean(sales, axis=1)

print("\n2. Average Monthly Sales of Every Product:")

for i in range(len(products)):
    print(f"{products[i]}: {average_sales[i]:.2f}")


# ============================================================
# 3. BEST-SELLING PRODUCT
# ============================================================

best_product_index = np.argmax(total_sales)

print("\n3. Best-Selling Product:")

print(
    f"{products[best_product_index]} "
    f"with total sales = {total_sales[best_product_index]}"
)


# ============================================================
# 4. WORST-SELLING PRODUCT
# ============================================================

worst_product_index = np.argmin(total_sales)

print("\n4. Worst-Selling Product:")

print(
    f"{products[worst_product_index]} "
    f"with total sales = {total_sales[worst_product_index]}"
)


# ============================================================
# 5. HIGHEST SALES IN EACH MONTH
# ============================================================

highest_monthly_sales = np.max(sales, axis=0)

print("\n5. Highest Sales in Each Month:")

for i in range(len(months)):
    print(f"{months[i]}: {highest_monthly_sales[i]}")


# ============================================================
# 6. LOWEST SALES IN EACH MONTH
# ============================================================

lowest_monthly_sales = np.min(sales, axis=0)

print("\n6. Lowest Sales in Each Month:")

for i in range(len(months)):
    print(f"{months[i]}: {lowest_monthly_sales[i]}")


# ============================================================
# 7. PRODUCTS WHOSE AVERAGE SALES ARE GREATER THAN 120
# ============================================================

print("\n7. Products Having Average Sales Greater Than 120:")

for i in range(len(products)):
    if average_sales[i] > 120:
        print(
            f"{products[i]}: "
            f"{average_sales[i]:.2f}"
        )


# ============================================================
# 8. TOTAL SALES FOR EACH MONTH
# ============================================================

monthly_total_sales = np.sum(sales, axis=0)

print("\n8. Total Sales for Each Month:")

for i in range(len(months)):
    print(f"{months[i]}: {monthly_total_sales[i]}")


# ============================================================
# 9. STANDARD DEVIATION OF MONTHLY SALES
# ============================================================

standard_deviation = np.std(sales)

print("\n9. Standard Deviation of Monthly Sales:")

print(f"{standard_deviation:.2f}")


# ============================================================
# 10. HIGH / LOW PRODUCT CLASSIFICATION USING np.where()
# ============================================================

classification = np.where(
    average_sales >= 120,
    "High",
    "Low"
)

print("\n10. Product Classification:")

for i in range(len(products)):
    print(
        f"{products[i]}: "
        f"{classification[i]}"
    )


# ============================================================
# 11. CREATE PANDAS DATAFRAME
#     Product, Total Sales and Average Sales
# ============================================================

df = pd.DataFrame({
    "Product": products,
    "Total Sales": total_sales,
    "Average Sales": average_sales
})

print("\n11. Product Sales DataFrame:")

print(df)


# ============================================================
# 12. SORT DATAFRAME ACCORDING TO TOTAL SALES
# ============================================================

sorted_df = df.sort_values(
    by="Total Sales",
    ascending=False
)

print("\n12. DataFrame Sorted According to Total Sales:")

print(sorted_df)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("              PRODUCT SALES ANALYSIS")
print("=" * 60)

print(f"Best-Selling Product  : {products[best_product_index]}")
print(f"Worst-Selling Product : {products[worst_product_index]}")
print(f"Total Overall Sales   : {np.sum(sales)}")
print(f"Standard Deviation    : {standard_deviation:.2f}")

print("\nMonthly Total Sales:")

for i in range(len(months)):
    print(f"{months[i]}: {monthly_total_sales[i]}")

print("=" * 60)
