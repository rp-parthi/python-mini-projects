from database import get_connection, initialise_database

def get_valid_amount():
    while True:
        value = input("Amount: ")
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Enter a valid number.")

def add_expense():
    book = input("Book name: ")
    category = input("Category: ")
    amount = get_valid_amount()

    if not book or not category:
        print("Book name and category are required.")

    with get_connection() as conn:
        conn.execute("INSERT INTO expenses (book_name, category, amount) VALUES (?, ?, ?)",
        (book, category, amount)
                     )
    print("Expense added.")

def view_all():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM expenses").fetchall()

    for row in rows:
        print(row)

def total_spent():
    with get_connection() as conn:
        total = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]

    print(f"Total spent: ${total if total else 0}")

def category_summary():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT category, SUM(amount) FROM expenses GROUP BY category"
        ).fetchall()

    for category, total in rows:
        print(f"{category}: ${total}")

def show_menu():
    print("\n1. Add expense")
    print("2. View all expenses")
    print("3. Total spent")
    print("4. Category summary")
    print("5. Exit")

def handle_choice(choice):
    actions = {
        "1": add_expense,
        "2": view_all,
        "3": total_spent,
        "4": category_summary
    }

    if choice == "5":
        return False
    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice.")
    return True


def main():
    initialise_database()

    running = True
    while running:
       show_menu()
       choice = input("Choose: ").strip()
       running = handle_choice(choice)

if __name__ == "__main__":
    main()
