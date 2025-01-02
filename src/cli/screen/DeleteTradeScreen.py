from textual.app import ComposeResult
from textual.containers import Grid
from textual.events import Key
from textual.screen import ModalScreen
from textual.widgets import Button, Label

from efolio.entity.Holding import Holding
from efolio.entity.Trade import Trade


class DeleteTradeScreen(ModalScreen[bool]):
    """Screen with a dialog to delete."""

    CSS_PATH = "DeleteTradeScreen.tcss"

    def __init__(self, holding: Holding, trade: Trade, **kwargs):
        self.holding = holding
        self.trade = trade
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to delete trade?", id="question"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("Delete", variant="error", id="delete"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "delete":
            self.holding.trades.remove(self.trade)
            self.dismiss(True)
            return
        self.dismiss(False)

    def on_key(self, event: Key):
        if event.key == "escape":
            self.dismiss(False)