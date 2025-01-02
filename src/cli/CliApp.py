from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Footer, Header

from cli.table.HoldingTable import HoldingTable
from efolio.entity.Account import Account


class CliApp(App):
    def __init__(self, account: Account):
        self.account = account
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield HoldingTable(self.account)

    def on_key(self, event: Key):
        if event.key == "escape":
            self.app.exit()
