import json
from dataclasses import asdict
from pathlib import Path


class BillStorage:
    """Simple JSON-based persistence using only the Python standard library."""

    def __init__(self, filename="bills.json"):
        self.file = Path(filename)
        self._initialize()

    def _initialize(self):
        if not self.file.exists():
            self.file.write_text("[]", encoding="utf-8")

    def get_all(self):
        try:
            data = json.loads(self.file.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def save_bill(self, bill):
        bills = self.get_all()
        bills.append(asdict(bill))
        self.file.write_text(
            json.dumps(bills, indent=4),
            encoding="utf-8"
        )
