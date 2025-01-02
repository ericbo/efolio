from datetime import datetime


class Trade:
    def __init__(self, symbol: str, date: str, trade_type: str, currency: str, unit_price: str, quantity: float,
                 fee: float):
        self.symbol = symbol
        self.date = date
        self.trade_type = trade_type
        self.currency = currency
        self.unit_price = unit_price
        self.quantity = quantity
        self.fee = fee

    def get_date(self) -> datetime:
        return datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%fZ")

    def get_formatted_date(self):
        date = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%fZ")
        return date.strftime("%Y-%m-%d")

    def __eq__(self, other):
        if isinstance(other, Trade):
            return self.get_date() == other.get_date()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Trade):
            return self.get_date() > other.get_date()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Trade):
            return self.get_date() < other.get_date()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Trade):
            return self.get_date() >= other.get_date()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Trade):
            return self.get_date() <= other.get_date()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Trade):
            return self.get_date() != other.get_date()
        return NotImplemented

