from typing import List

from efolio.entity.Trade import Trade
from efolio.service.FilesystemService import FileSystemService
from efolio.entity.Holding import Holding


class GhostfolioImportService:
    def __init__(self, file_system: FileSystemService):
        self.file_system = file_system

    def parse_json(self, file_path: str) -> List[Holding]:
        data = self.file_system.parse_json(file_path)

        activities = {}

        for activity in data.get("activities", []):
            symbol = activity.get("symbol")
            date = activity.get("date")
            trade_type = activity.get("type")
            currency = activity.get("currency")
            unit_price = activity.get("unitPrice")
            quantity = activity.get("quantity")
            fee = activity.get("fee")

            if trade_type not in ["BUY", "SELL", "DIVIDEND"]:
                continue

            if activities.get(symbol) is None:
                activities[symbol] = []

            activities[symbol].append({
                "date": date,
                "trade_type": trade_type,
                "currency": currency,
                "unit_price": unit_price,
                "quantity": quantity,
                "fee": fee
            })

        holdings: List[Holding] = []

        for symbol in activities.keys():
            holding = Holding(symbol)
            holdings.append(holding)

            for trade in activities[symbol]:
                holding.add(Trade(
                    symbol=symbol,
                    date=trade.get("date"),
                    trade_type=trade.get("trade_type"),
                    currency=trade.get("currency"),
                    unit_price=trade.get("unit_price"),
                    quantity=trade.get("quantity"),
                    fee=trade.get("fee")
                ))

        for holding in holdings:
            holding.sort()

        return holdings
