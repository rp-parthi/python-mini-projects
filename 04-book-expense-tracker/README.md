# Expense Tracker (CLI)

A simple **Python command-line application** to track book-related expenses using **SQLite**.
This project focuses on writing clean, readable, production-style Python code while learning how Python interacts with SQL.

---

## 📌 Project Overview

This CLI app allows a user to:

* Add a new expense
* View all expenses
* View total amount spent
* View category-wise spending summary

The project demonstrates how to:

* Validate user input safely
* Separate database logic from application logic
* Use SQL queries from Python
* Structure a small backend-style project

---

## 🧠 Concepts Used

* Python functions
* Input validation (`try / except`)
* SQLite database
* SQL queries (`INSERT`, `SELECT`, `SUM`, `GROUP BY`)
* Context managers (`with`)
* Dictionary-based command dispatcher
* Clean `main()` entry point

---

## ▶️ How to Run

```bash
python main.py
```

3️⃣ Follow the on-screen menu

---

## 📋 Menu Options

```
1. Add expense
2. View all expenses
3. Total spent
4. Category summary
5. Exit
```

---

## 🔍 Example Features

### Add Expense

* Validates numeric input for amount
* Prevents negative or zero values
* Stores data in SQLite

### Category Summary

* Uses SQL `GROUP BY`
* Displays total spending per category

---

## 🧪 Input Validation

The app safely handles:

* Non-numeric input
* Negative numbers
* Empty values

This prevents crashes and ensures clean data storage.

---

## 🧱 Design Decisions

* `main()` acts as the **controller** managing program flow
* Database access is isolated in `database.py`
* SQL schema is stored separately in `schema.sql`
* Uses a dictionary-based action router instead of long `if/elif` chains

---

## 📈 What I Learned

* How Python communicates with a SQL database
* Why input validation is critical
* How to structure a CLI app like a backend service
* How to use context managers for safe resource handling
* Writing readable and maintainable Python code

---

## 🚀 Future Improvements

* Add date filtering
* Export expenses to CSV
* Add logging
* Convert to FastAPI REST API
* Replace SQLite with PostgreSQL
