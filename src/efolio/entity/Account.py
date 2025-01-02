from typing import List
from uuid import uuid4

from efolio.entity.Holding import Holding


class Account:
    def __init__(self, account_id: uuid4 , name: str):
        self.account_id = id
        self.name = name
        self.holdings: List[Holding] = []

    def add_holdings(self, holdings: List[Holding]):
        self.holdings = self.holdings + holdings

        self.holdings = sorted(self.holdings, reverse=True)

    def get_holding_by_symbol(self, symbol: str) -> Holding:
        for holding in self.holdings:
            if holding.symbol == symbol:
                return holding

        raise RuntimeError(f"Failed to find any holdings of {symbol}")

    def __eq__(self, other):
        other: Account
        return self.account_id == other.account_id