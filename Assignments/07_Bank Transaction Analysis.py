import numpy as np
import pandas as pd

# ============================================================
# PROJECT 7: BANK TRANSACTION ANALYSIS
# ============================================================

# Given Dataset
transactions = np.array([
    [5000, 2000, 3000],
    [8000, 1500, 4000],
    [3000, 1000, 2500],
    [10000, 3000, 5000],
    [7000, 2500, 3500]
])

# Customer names
customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5"
]

# Column names
columns = ["Deposit", "Withdrawal", "Investment"]


# ============================================================
# 1. TOTAL DEPOSIT AMOUNT
# ============================================================

total_deposit = np.sum(transactions[:, 0])

print("\n1. Total Deposit Amount:")
print(f"₹{total_deposit:,.2f}")


# ============================================================
# 2. TOTAL WITHDRAWAL AMOUNT
# ============================================================

total_withdrawal = np.sum(transactions[:, 1])

print("\n2. Total Withdrawal Amount:")
print(f"₹{total_withdrawal:,.2f}")


# ============================================================
# 3. TOTAL INVESTMENT AMOUNT
# ============================================================

total_investment = np.sum(transactions[:, 2])

print("\n3. Total Investment Amount:")
print(f"₹{total_investment:,.2f}")


# ============================================================
# 4. NET BALANCE = DEPOSIT - WITHDRAWAL
# ============================================================

net_balance = transactions[:, 0] - transactions[:, 1]

print("\n4. Net Balance of Each Customer:")

for i in range(len(customers)):
    print(
        f"{customers[i]}: "
        f"₹{net_balance[i]:,.2f}"
    )


# ============================================================
# 5. CUSTOMER WITH HIGHEST DEPOSIT
# ============================================================

highest_deposit_index = np.argmax(transactions[:, 0])

print("\n5. Customer With Highest Deposit:")

print(
    f"{customers[highest_deposit_index]}: "
    f"₹{transactions[highest_deposit_index, 0]:,.2f}"
)


# ============================================================
# 6. CUSTOMER WITH HIGHEST WITHDRAWAL
# ============================================================

highest_withdrawal_index = np.argmax(transactions[:, 1])

print("\n6. Customer With Highest Withdrawal:")

print(
    f"{customers[highest_withdrawal_index]}: "
    f"₹{transactions[highest_withdrawal_index, 1]:,.2f}"
)


# ============================================================
# 7. CUSTOMERS WHOSE NET BALANCE IS GREATER THAN ₹4,000
# ============================================================

print("\n7. Customers With Net Balance Greater Than ₹4,000:")

for i in range(len(customers)):
    if net_balance[i] > 4000:
        print(
            f"{customers[i]}: "
            f"₹{net_balance[i]:,.2f}"
        )


# ============================================================
# 8. AVERAGE DEPOSIT
# ============================================================

average_deposit = np.mean(transactions[:, 0])

print("\n8. Average Deposit:")

print(f"₹{average_deposit:,.2f}")


# ============================================================
# 9. STANDARD DEVIATION OF DEPOSITS
# ============================================================

deposit_std = np.std(transactions[:, 0])

print("\n9. Standard Deviation of Deposits:")

print(f"₹{deposit_std:,.2f}")


# ============================================================
# 10. CLASSIFY CUSTOMERS AS HIGH, MEDIUM OR LOW
#
# High   -> Net Balance >= ₹7,000
# Medium -> Net Balance >= ₹4,000 and < ₹7,000
# Low    -> Net Balance < ₹4,000
# ============================================================

classification = np.where(
    net_balance >= 7000,
    "High",
    np.where(
        net_balance >= 4000,
        "Medium",
        "Low"
    )
)

print("\n10. Customer Classification:")

for i in range(len(customers)):
    print(
        f"{customers[i]}: "
        f"₹{net_balance[i]:,.2f} - "
        f"{classification[i]}"
    )


# ============================================================
# 11. CONVERT FINAL DATA INTO PANDAS DATAFRAME
# ============================================================

df = pd.DataFrame(
    transactions,
    columns=columns
)

# Add Customer column
df.insert(0, "Customer", customers)

# Add Net Balance column
df["Net Balance"] = net_balance

# Add Classification column
df["Classification"] = classification


print("\n11. Final Bank Transaction DataFrame:")

print(df)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 65)
print("               BANK TRANSACTION ANALYSIS")
print("=" * 65)

print(f"Total Deposit       : ₹{total_deposit:,.2f}")
print(f"Total Withdrawal    : ₹{total_withdrawal:,.2f}")
print(f"Total Investment    : ₹{total_investment:,.2f}")
print(f"Average Deposit     : ₹{average_deposit:,.2f}")
print(f"Deposit Std. Dev.   : ₹{deposit_std:,.2f}")

print(
    f"Highest Deposit     : "
    f"{customers[highest_deposit_index]}"
)

print(
    f"Highest Withdrawal  : "
    f"{customers[highest_withdrawal_index]}"
)

print("=" * 65)
