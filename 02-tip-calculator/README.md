## 💰 Tip Calculator (Day 02)

A simple Python command-line application that calculates how much each person should pay when splitting a bill, including tip.

This project focuses on **clean code structure**, **input validation**, and **thinking in a production-ready way**, rather than just making the program work.

---

## 🛠 Concepts Used

- Functions and modular design
- Input validation loops
- Type conversion (`str` → `int` / `float`)
- Error handling using `try / except`
- `main()` entry point
- f-strings for formatted output

---

## ▶️ How to Run

```bash
python src/main.py
```

## How It Works

- User enters:
- Total bill amount
- Tip percentage (10, 12, or 15)
- Number of people to split the bill
- Program validates all inputs
- Tip is calculated and added to the bill
- Final amount is split evenly
- Amount per person is displayed (2 decimal places)

## What I Learned

- Why user input must always be validated
- Difference between logical checks (if) and error handling (try / except)
- How to separate responsibilities using helper functions
- Why calculations should be done before printing
- Proper formatting of monetary values using .2f

## Future Improvements

- Allow custom tip percentages
- Handle currency symbols
- Add unit tests
- Convert to a GUI or web app
