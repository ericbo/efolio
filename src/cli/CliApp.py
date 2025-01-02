from textual.app import App, ComposeResult
from textual.events import Key
from textual.screen import Screen
from textual.widgets import Footer, Header, DataTable

from efolio.entity.Account import Account
from efolio.entity.Holding import Holding


class TradeScreen(Screen):
    """ Screen to display all trades for a given symbol """

    def __init__(self, app: App, holding: Holding):
        self.app
        self.holding = holding
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        table.add_columns("date", "Type", "Currency", "Unit Price", "Quantity", "Fee")
        for trade in self.holding.trades:
            table.add_row(trade.get_formatted_date(), trade.trade_type, trade.currency, trade.unit_price, trade.quantity, trade.fee)

    def on_key(self, event: Key):
        if event.key == "escape":
            self.app.pop_screen()


class CliApp(App):
    def __init__(self, account: Account):
        self.account = account
        super().__init__()

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield DataTable()

    def on_mount(self) -> None:
        self.table = self.query_one(DataTable)
        self.table.cursor_type = "row"
        self.table.zebra_stripes = True

        self.table.add_columns("Symbol", "Position")

        for holding in self.account.holdings:
            if holding.get_position() == 0:
                continue
            self.table.add_row(holding.symbol, holding.get_position(), key=holding.symbol)

    def on_key(self, event: Key):
        if event.key == "enter":
            if isinstance(self.screen.screen, TradeScreen):
                return
            # Get the key of the currently selected row
            selected_row = self.table.get_row_at(self.table.cursor_row)
            if selected_row is not None:
                # The key should be the first column, assuming it is the identifier
                row_key = selected_row[0]

                self.push_screen(TradeScreen(self, self.account.get_holding_by_symbol(row_key)))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
