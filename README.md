# To Do App API

This is the API codebase of the To Do App.

## Tech Stack

- Python (see `.python-version` for the current version in use)
- Django and Django REST Framework
- Pytest

## How to set up the development environment

Install Python (check the version in `.python-version`)

Go to the root directory of this project and create the virtual environment, open it and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
`.venv` could be substituted with any path, if you wish to create the virual env elsewhere

## How to run the development environment

If you use VSCode, open a new terminal, and virtual environment should open automatically.

Run this command to start the development server:

```bash
python manage.py runserver
```

To use a regular terminal, go to the root directory of this project, open the virtual environment and start the server:

```bash
source .venv/bin/activate
python manage.py runserver
```

## Tests

The project uses Pytest unit tests.

To run the tests, run the following command:

```bash
pytest
```

## Database

The project uses a SQLite3 database.

To open it, you need to install SQLite3: see [SQLite homepage](https://sqlite.org/)

Linux installation:

```bash
sudo apt install sqlite3
```

If you have SQLite3 installed, run the dbshell command in the virtual env:

```bash
python manage.py dbshell
```

Some commands to navigate the DB shell:

```bash
.tables # view the list of tables
.help # view the help file
```

### Changing the data model

If you make changes to the data models, you must run a database migration to update the database according to those changes:

```bash
python manage.py makemigrations # create the migration files based on the code changes
python manage.py migrate # migrate the database to the latest migrations
```

You can view the current state of the migrations by running this:

```bash
python manage.py showmigrations
```
