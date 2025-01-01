from typing import List

from efolio.entity.Trade import Trade


class Holding:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.holding: List[Trade] = []

    def add(self, trade: Trade):
        self.holding.append(trade)

    def number_of_trades(self) -> int:
        return len(self.holding)

    def get_trades(self):
        return self.holding