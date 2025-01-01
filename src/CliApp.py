import os
import sys
from uuid import uuid4

from cli.CliApp import CliApp
from efolio.entity.Account import Account
from efolio.service.FilesystemService import FileSystemService
from efolio.service.GhostfolioImportService import GhostfolioImportService

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a file path as a parameter.")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: The file at '{file_path}' does not exist.")
        sys.exit(1)

    file_system = FileSystemService()
    parser = GhostfolioImportService(file_system)
    account = Account(uuid4(), "All Accounts")
    holdings = parser.parse_json(file_path)
    account.add_holdings(holdings)
    app = CliApp(account.get_rows())
    app.run()
