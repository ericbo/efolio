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

    def get_holdings(self) -> List[Holding]:
        return self.holdings

    def get_rows(self):
        rows = [("Symbol", "Number of Trades")]

        for holding in self.holdings:
            rows.append((holding.symbol, holding.number_of_trades()))

        return rows

    def __eq__(self, other):
        other: Account
        return self.account_id == other.account_id