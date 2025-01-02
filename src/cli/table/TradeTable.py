from textual.widgets import DataTable

from efolio.entity.Holding import Holding


class TradeTable(DataTable):
    def __init__(self, holding: Holding, **kwargs):
        super().__init__(**kwargs)
        self.holding = holding
        self.update_table()

    def update_table(self) -> None:
        self.clear(columns=True)
        self.cursor_type = "row"
        self.zebra_stripes = True
        self.add_columns("date", "Type", "Currency", "Unit Price", "Quantity", "Fee")

        for trade in self.holding.trades:
            self.add_row(trade.get_formatted_date(), trade.trade_type, trade.currency, trade.unit_price,
                         trade.quantity, trade.fee, key=trade.id)

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        event.stop()