from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bill:
    customer_id: int
    customer_name: str
    units: float
    energy_charge: float
    fixed_charge: float
    surcharge: float
    tax: float
    total: float
    generated_at: str


class ElectricityBillCalculator:
    """
    Core electricity billing engine.

    Slabs:
        0-100 units      -> ₹3.00/unit
        101-200 units    -> ₹5.00/unit
        201-500 units    -> ₹7.00/unit
        Above 500 units  -> ₹10.00/unit

    Fixed charge: ₹50
    Surcharge: 5% of energy charge when units > 500
    Tax: 5% of (energy charge + fixed charge + surcharge)
    """

    SLABS = [
        (100, 3.00),
        (200, 5.00),
        (500, 7.00),
        (float("inf"), 10.00),
    ]

    FIXED_CHARGE = 50.00
    SURCHARGE_RATE = 0.05
    TAX_RATE = 0.05

    def calculate_energy_charge(self, units):
        remaining = units
        previous_limit = 0
        charge = 0.0

        for upper_limit, rate in self.SLABS:
            if remaining <= 0:
                break

            slab_units = min(remaining, upper_limit - previous_limit)
            charge += slab_units * rate
            remaining -= slab_units

            if upper_limit != float("inf"):
                previous_limit = upper_limit

        return round(charge, 2)

    def calculate(self, customer_id, customer_name, units):
        if units < 0:
            raise ValueError("Units cannot be negative.")

        energy_charge = self.calculate_energy_charge(units)

        fixed_charge = self.FIXED_CHARGE

        surcharge = 0.0
        if units > 500:
            surcharge = energy_charge * self.SURCHARGE_RATE

        taxable_amount = energy_charge + fixed_charge + surcharge
        tax = taxable_amount * self.TAX_RATE
        total = taxable_amount + tax

        return Bill(
            customer_id=customer_id,
            customer_name=customer_name,
            units=units,
            energy_charge=round(energy_charge, 2),
            fixed_charge=round(fixed_charge, 2),
            surcharge=round(surcharge, 2),
            tax=round(tax, 2),
            total=round(total, 2),
            generated_at=datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        )
