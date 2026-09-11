# Electricity Bill Calculator

A professional **Core Python** console project that calculates electricity bills using slab-based pricing.

## Features

- Slab-wise electricity calculation
- Functions and modular design
- Conditions and loops
- Input validation
- Fixed charge
- High-consumption surcharge
- Tax calculation
- JSON bill history
- Billing summary
- Clean CLI interface
- No third-party packages required

## Slab Rates

| Units | Rate |
|---|---:|
| 0-100 | ₹3/unit |
| 101-200 | ₹5/unit |
| 201-500 | ₹7/unit |
| Above 500 | ₹10/unit |

Additional rules:

- Fixed charge: ₹50
- Consumption above 500 units: 5% surcharge on energy charge
- Tax: 5% on energy charge + fixed charge + surcharge

## Concepts Demonstrated

1. Variables and data types
2. Input/output
3. Type conversion
4. Arithmetic operators
5. Conditional statements
6. `for` and `while` loops
7. Functions
8. Classes and objects
9. Dataclasses
10. Exception handling
11. Lists and dictionaries
12. JSON file handling
13. Modular programming
14. Basic data aggregation

## Project Structure

```text
electricity_bill_calculator/
│
├── main.py
├── electricity_bill.py
├── storage.py
├── ui.py
├── bills.json
└── README.md
```

## How to Run

Open a terminal in the project directory:

```bash
python main.py
```

The program automatically creates `bills.json` when needed.

## Example

For 350 units:

- First 100 × ₹3 = ₹300
- Next 100 × ₹5 = ₹500
- Next 150 × ₹7 = ₹1,050
- Energy charge = ₹1,850
- Fixed charge = ₹50
- Tax = 5% of ₹1,900 = ₹95
- Total = ₹1,995

## Project Objective

This project is designed as a portfolio-ready Core Python project for students learning programming fundamentals while practicing real-world billing logic.
