# Library Management System

A simple console-based Library Management System built in Python. It uses `pickle` for local data persistence (no external database required) and provides a menu-driven interface for managing library members and books.

## Features

- **Member Registration & Login** — Create a username/password to access the system.
- **Add Book** — Add one or more books with a code, title, author, and price.
- **Add Member** — Register students with admission number, name, roll number, class, section, and email.
- **View Books** — List all books currently in the library.
- **View Members** — List all registered student members.
- **Issue Book** — Issue a book to a student and set a 7-day due date.
- **Return Book** — Return a borrowed book and calculate a late fee if overdue.
- **Delete Member** — Remove a student record.
- **Delete Book** — Remove a book record.

## Requirements

- Python 3.x
- No external libraries required (uses only the standard library: `pickle`, `datetime`)

## How to Run

```bash
python library_management_system.py
```

On launch, you'll see a main menu:

```
L. To Login
R. To Register
E. To Exit
```

Register a new account first, then log in to access the library operations menu (add/view/issue/return/delete).

## Data Storage

The program stores data locally in `.dat` files (created automatically in the working directory) using Python's `pickle` module:

| File | Contents |
|---|---|
| `register_member.dat` | Login credentials (username/password) |
| `Book_details.dat` | Book records |
| `Members_details.dat` | Student member records |
| `issue_book.dat` | Currently issued books |

> **Note:** These `.dat` files are generated at runtime and are specific to each local setup. It's recommended to add them to `.gitignore` rather than committing them to the repository.

## Known Limitations

This is a learning/demo project and has a few rough edges worth knowing about before relying on it:
- Data files use `pickle`, which is not a safe format for untrusted input and isn't suitable for production use.
- Error handling is minimal (e.g., invalid input types can crash the program).

Contributions to fix these are welcome!
