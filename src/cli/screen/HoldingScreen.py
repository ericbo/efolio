from textual.app import ComposeResult
from textual.events import Key
from textual.screen import Screen
from textual.widgets import Header, Footer

from cli.table.HoldingTable import HoldingTable
from efolio.entity.Account import Account


class HoldingScreen(Screen):

    def __init__(self, account: Account):
        self.account = account
        super().__init__()
        self.app.title = account.name

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield HoldingTable(self.account)

    def on_key(self, event: Key):
        if event.key == "escape":
            self.app.exit()