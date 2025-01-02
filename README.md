# eFolio
A simple terminal based application to track your portfolio performance. Presently the database for this application
comes from an existing [ghostfolio](https://github.com/ghostfolio/ghostfolio) portfolio export. Eventually this app will
be capable of creating a database that can be browsed/edited via a UI.

## Running the Application

### First Run

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

### Subsequent Runs

```bash
python src/CliApp.py ghostfolio.json
```