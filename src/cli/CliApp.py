from itertools import cycle

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DataTable


class CliApp(App):
    def __init__(self, rows: list):
        self.cursors = cycle(["row"])
        self.rows = rows
        super().__init__()

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = next(self.cursors)
        table.zebra_stripes = True
        table.add_columns(*self.rows[0])
        table.add_rows(self.rows[1:])

    def key_c(self):
        table = self.query_one(DataTable)
        table.cursor_type = next(self.cursors)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )