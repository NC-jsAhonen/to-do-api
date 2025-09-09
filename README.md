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

### Setting up the database

First, you need to install SQLite3.

Installation in Linux (Debian family):

```bash
sudo apt install sqlite3
```

For other operating systems, see [SQLite homepage](https://sqlite.org/).

When you have SQLite3 installed, run the dbshell command in the virtual env:

```bash
python manage.py dbshell
```

When running this for the first time, the script creates the database file: `todo_api/db.sqlite3`

Then, you need to run the migrations to bring it up to date with the latest changes:

```bash
python manage.py migrate
```

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

Open the database shell:

```bash
python manage.py dbshell
```

Some commands to navigate the DB shell:

```bash
.tables # view the list of tables
.help # view the help file
```

### Handling the database migrations

#### Updating the data model

If you make changes to the data models, you must run a database migration to update the database according to those changes.

First, create the migration files:

```bash
python manage.py makemigrations
```

Then run all the migrations:

```bash
python manage.py migrate
```

#### Navigating the migrations

You can view the current state of the migrations by running this:

```bash
python manage.py showmigrations
```

You can also move around forward and backward in migrations by adding the app name and the migration number after the command name.

For example:

```bash
python manage.py migrate todo 0001
```
