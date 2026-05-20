# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a Flask-based REST API for a messaging/chat system with JWT authentication. Single service, no external dependencies beyond SQLite (embedded).

### Key gotcha: Flask-JWT-Extended version

`requirements.txt` pins `PyJWT~=2.3.0` but leaves `Flask-JWT-Extended` unpinned. The latest `Flask-JWT-Extended` (4.7+) is **incompatible** with `PyJWT 2.3.0` (`ModuleNotFoundError: No module named 'jwt.types'`). The update script forces `Flask-JWT-Extended==4.3.1` after the main install to resolve this.

### Running the app

```bash
python3 app.py
```

Starts Flask dev server on `http://0.0.0.0:5000` with debug mode. SQLite database (`application/db.sqlite3`) and seed data are auto-created on first run.

### Running tests

```bash
python3 -m pytest test/ -v
```

All tests use Flask's test client — no running server needed.

### Seed users (auto-created)

| Name      | Password |
|-----------|----------|
| Иван      | 111      |
| Алексей   | 222      |
| Владимир  | 333      |
| Павел     | 444      |

### API endpoints

- `POST /` — Login (JSON: `{"name": "...", "password": "..."}`) → returns `{"token": "..."}`
- `POST /message` — Send message (requires Bearer token, JSON: `{"name": "...", "message": "..."}`)
- `POST /history` — Get history (requires Bearer token, JSON: `{"name": "...", "history": N}`)

### No lint tool configured

This project has no linter or formatter configured. There are deprecation warnings from Werkzeug/pytest on Python 3.12+ but these do not affect functionality.
