## 🍕 Python Pizza Deliveries (Mini Project)

A beginner-friendly Python command-line application that calculates the total cost of a pizza order based on size and optional add-ons.

This project focuses on **clean input handling**, **separation of concerns**, and **writing readable, maintainable Python code** instead of relying only on large `if/else` blocks.

---

## 🛠 Concepts Used

- Functions and modular programming
- Input validation loops
- Dictionaries for pricing rules
- Clean `main()` function design
- Separation of business logic and user interaction
- f-strings for output formatting

---

## ▶️ How to Run

```bash
python src/main.py
```

## Features
- Choose pizza size: Small (S), Medium (M), Large (L)
- Optional pepperoni (price varies by size)
- Optional extra cheese (flat price)
- Validates all user inputs
- Displays final bill amount

## What I Learned
- Why calculations should not live inside `main()`
- How using dictionaries avoids complex `if/else` logic
- Common input validation mistakes (e.g., `if value == 'y' or 'n'`)
- How to design functions that do one thing well
- Writing code that is easy to extend and test

## Possible Improvements
- Allow ordering multiple pizzas
- Support custom toppings
- Add unit tests
- Convert to a GUI or web-based app
