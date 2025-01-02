from typing import List

from efolio.entity.Trade import Trade


class Holding:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.trades: List[Trade] = []

    def add(self, trade: Trade):
        self.trades.append(trade)

    def sort(self):
        self.trades = sorted(self.trades, reverse=True)

    def get_number_of_trades(self) -> int:
        return len(self.trades)

    def get_position(self):
        position = 0
        for trade in sorted(self.trades):
            if trade.trade_type not in ["BUY", "SELL"]:
                continue

            quantity = trade.quantity

            if trade.trade_type == "SELL":
                position -= quantity
            else:
                position += quantity

        return position

    def __eq__(self, other):
        if isinstance(other, Holding):
            return self.get_position() == other.get_position()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Holding):
            return self.get_position() > other.get_position()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Holding):
            return self.get_position() < other.get_position()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Holding):
            return self.get_position() >= other.get_position()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Holding):
            return self.get_position() <= other.get_position()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Holding):
            return self.get_position() != other.get_position()
        return NotImplemented