from electricity_bill import ElectricityBillCalculator
from storage import BillStorage
from ui import (
    banner, print_bill, print_history, print_summary,
    get_positive_number, get_customer_name, get_units, pause, print_menu
)


def calculate_bill(calculator, storage):
    print("\n--- Calculate Electricity Bill ---")
    name = get_customer_name()
    units = get_units()
    customer_id = get_positive_number("Enter customer ID: ", integer=True)

    bill = calculator.calculate(
        customer_id=int(customer_id),
        customer_name=name,
        units=units
    )

    storage.save_bill(bill)
    print_bill(bill)
    pause()


def view_history(storage):
    print("\n--- Bill History ---")
    bills = storage.get_all()
    print_history(bills)
    pause()


def view_summary(storage):
    print("\n--- Billing Summary ---")
    bills = storage.get_all()
    print_summary(bills)
    pause()


def main():
    calculator = ElectricityBillCalculator()
    storage = BillStorage()

    while True:
        banner()
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculate_bill(calculator, storage)
        elif choice == "2":
            view_history(storage)
        elif choice == "3":
            view_summary(storage)
        elif choice == "4":
            print("\nThank you for using Electricity Bill Calculator.")
            break
        else:
            print("\nInvalid choice. Please select 1-4.")
            pause()


if __name__ == "__main__":
    main()
