def banner():
    print("\n" + "=" * 68)
    print("        ELECTRICITY BILL CALCULATOR")
    print("              CORE PYTHON PROJECT")
    print("=" * 68)


def print_menu():
    print("\n1. Calculate New Bill")
    print("2. View Bill History")
    print("3. View Billing Summary")
    print("4. Exit")
    print("-" * 68)


def get_customer_name():
    while True:
        name = input("Enter customer name: ").strip()
        if name and all(ch.isalpha() or ch.isspace() for ch in name):
            return name
        print("Invalid name. Use alphabetic characters and spaces only.")


def get_positive_number(prompt, integer=False):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError

            if integer:
                return int(value)
            return value
        except ValueError:
            print("Please enter a valid positive number.")


def get_units():
    while True:
        try:
            units = float(input("Enter electricity units consumed: "))
            if units < 0:
                raise ValueError
            return units
        except ValueError:
            print("Please enter a valid non-negative number.")


def money(value):
    return f"₹{value:,.2f}"


def print_bill(bill):
    print("\n" + "=" * 58)
    print("                    ELECTRICITY BILL")
    print("=" * 58)
    print(f"Customer ID       : {bill.customer_id}")
    print(f"Customer Name     : {bill.customer_name}")
    print(f"Units Consumed    : {bill.units:,.2f}")
    print(f"Generated At      : {bill.generated_at}")
    print("-" * 58)
    print(f"Energy Charge     : {money(bill.energy_charge)}")
    print(f"Fixed Charge      : {money(bill.fixed_charge)}")
    print(f"Surcharge         : {money(bill.surcharge)}")
    print(f"Tax               : {money(bill.tax)}")
    print("-" * 58)
    print(f"TOTAL BILL        : {money(bill.total)}")
    print("=" * 58)


def print_history(bills):
    if not bills:
        print("No bills found.")
        return

    print(f"{'ID':<8}{'Customer':<22}{'Units':>10}{'Total':>16}")
    print("-" * 58)

    for bill in bills:
        print(
            f"{bill['customer_id']:<8}"
            f"{bill['customer_name'][:20]:<22}"
            f"{bill['units']:>10.2f}"
            f"{money(bill['total']):>16}"
        )


def print_summary(bills):
    if not bills:
        print("No billing data available.")
        return

    total_revenue = sum(bill["total"] for bill in bills)
    total_units = sum(bill["units"] for bill in bills)
    average_bill = total_revenue / len(bills)

    highest = max(bills, key=lambda bill: bill["total"])

    print(f"Total Bills       : {len(bills)}")
    print(f"Total Units       : {total_units:,.2f}")
    print(f"Total Revenue     : {money(total_revenue)}")
    print(f"Average Bill      : {money(average_bill)}")
    print(
        f"Highest Bill      : {money(highest['total'])} "
        f"({highest['customer_name']})"
    )


def pause():
    input("\nPress Enter to continue...")
