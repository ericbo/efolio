from textual.app import ComposeResult
from textual.events import Key
from textual.screen import Screen
from textual.widgets import Header, Footer

from cli.table.TradeTable import TradeTable
from efolio.entity.Holding import Holding


class TradeScreen(Screen):
    """ Screen to display all trades for a given symbol """
    BINDINGS = [
        ("a", "add_trade", "Add"),
        ("e", "edit_trade", "Edit"),
        ("d", "delete_trade", "Delete")
    ]

    def __init__(self, holding: Holding):
        self.holding = holding
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield TradeTable(self.holding)

    def on_key(self, event: Key):
        if event.key == "escape":
            event.stop()
            self.app.pop_screen()

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

        self.holding.delete_trade(row_key.value)

        table.update_table()
