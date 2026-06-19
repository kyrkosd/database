# Simple Database API (SQLite + SQLAlchemy + FastAPI)

A clean, working backend database setup. SQLite stores everything in one file,
SQLAlchemy lets you work with Python objects instead of raw SQL, and FastAPI
exposes it all as a REST API with auto-generated docs.

## Project structure

```
db_project/
├── app/
│   ├── __init__.py     # makes "app" a package
│   ├── database.py     # engine + session setup (the core wiring)
│   ├── models.py       # your tables, as Python classes
│   ├── crud.py         # reusable create/read/update/delete functions
│   └── main.py         # the FastAPI web API
├── seed.py             # standalone script to test the DB without the server
├── requirements.txt
└── .gitignore
```

## Setup in VS Code

1. Open the `db_project` folder in VS Code (File → Open Folder).
2. Open a terminal (Terminal → New Terminal) and create a virtual environment:

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Recommended) Press `Ctrl+Shift+P` → "Python: Select Interpreter" → pick the
   one inside `.venv` so VS Code uses it.

## Try it without the server first

```bash
python seed.py
```
This creates the tables, adds a sample user + post, and prints them back.
You'll see an `app.db` file appear — that's your entire database.

## Run the API

```bash
uvicorn app.main:app --reload
```
Then open **http://127.0.0.1:8000/docs** in your browser. You get an interactive
interface to create users, add posts, and list them — no separate tool needed.

## How the pieces fit together

A request flows like this:

```
HTTP request  →  main.py (route)  →  crud.py (DB logic)  →  models.py (tables)
                                                        ↘  database.py (session)
```

Routes stay thin (validate + delegate), so all the real database logic lives in
`crud.py` where it's easy to test and reuse.

## Making it your own

- **Change what you store:** edit the classes in `models.py`. Each class is a
  table, each attribute a column. Delete the `User`/`Post` example and write
  your own.
- **Add operations:** add functions to `crud.py`, then a route in `main.py`.

## Two things to know before production

1. **Migrations.** This project calls `create_all()` to build tables on startup,
   which is fine for development but won't update existing tables when you change
   a model. For real projects, use **Alembic** (`pip install alembic`) to manage
   schema changes safely.
2. **Switching to PostgreSQL.** Change the `DATABASE_URL` in `database.py` to a
   `postgresql://...` string and remove the SQLite-only `connect_args`. Because
   you used the ORM, the rest of your code stays the same.