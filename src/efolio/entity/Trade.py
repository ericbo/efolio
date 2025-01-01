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
