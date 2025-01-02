from textual.app import App

from cli.screen.HoldingScreen import HoldingScreen
from efolio.entity.Account import Account


class CliApp(App):
    def __init__(self, account: Account):
        self.account = account
        super().__init__()

    def on_mount(self) -> None:
        self.push_screen(HoldingScreen(self.account))