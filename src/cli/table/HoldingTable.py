from textual.widgets import DataTable

from cli.screen.TradeScreen import TradeScreen
from efolio.entity.Account import Account


class HoldingTable(DataTable):
    def __init__(self, account: Account, **kwargs):
        super().__init__(**kwargs)
        self.account = account
        self.update_table()

    def update_table(self) -> None:
        self.clear()
        self.cursor_type = "row"
        self.zebra_stripes = True
        self.add_columns("Symbol", "Position")

        for holding in self.account.holdings:
            if holding.get_active_position() == 0:
                continue
            self.add_row(holding.symbol, holding.get_active_position(), key=holding.symbol)

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        self.app.push_screen(TradeScreen(self.account.get_holding_by_symbol(event.row_key.value)))
