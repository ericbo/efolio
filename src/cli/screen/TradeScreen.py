from textual.app import ComposeResult
from textual.events import Key
from textual.screen import Screen
from textual.widgets import Header, Footer

from cli.screen.DeleteTradeScreen import DeleteTradeScreen
from cli.table.TradeTable import TradeTable
from efolio.entity.Holding import Holding


class TradeScreen(Screen):
    BINDINGS = [
        ("a", "add_trade", "Add"),
        ("e", "edit_trade", "Edit"),
        ("d", "delete_trade", "Delete")
    ]

    def __init__(self, holding: Holding):
        self.holding = holding
        super().__init__()
        self.app.title = holding.symbol

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield TradeTable(self.holding)

    def on_key(self, event: Key):
        if event.key == "escape":
            event.stop()
            self.dismiss()

    def action_add_trade(self) -> None:
        pass

    def action_edit_trade(self) -> None:
        pass

    def action_delete_trade(self) -> None:
        table = self.query_one(TradeTable)

        if table.row_count <= 0:
            return

        cell_key = table.coordinate_to_cell_key(table.cursor_coordinate)
        row_key, _ = cell_key

        def update_table(updated: bool | None) -> None:
            if updated:
                table.update_table()

        self.app.push_screen(
            DeleteTradeScreen(self.holding, self.holding.find_trade(row_key.value)),
            update_table
        )
