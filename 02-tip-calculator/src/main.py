def get_bill_amount(prompt: str) -> float:
    while True:
        value = input(prompt).strip()
        try:
            amount = float(value)
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_tip_percent(prompt: str) -> int:
    valid_tips = (10, 12, 15)

    while True:
        value = input(prompt).strip()
        if value.isdigit():
            tip = int(value)
            if tip in valid_tips:
                return tip
        print("Please enter a valid tip (10, 12 or 15).")


def get_people_count(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            count = int(value)
            if count > 0:
                return count
        print("Please enter a valid number greater than 0. ")

def main() -> None:
    print("Welcome to the Tip Calculator!")

    bill_amount = get_bill_amount("Wha was the total bill?")
    tip_percent = get_tip_percent("How much tip would you like to give? (10, 12 or 15) ")
    people_count = get_people_count("How many people to split the bill?")

    total_bill = bill_amount * (1 + tip_percent / 100)
    per_person = total_bill / people_count

    print(f"Each person should pay: {per_person:.2f}")


if __name__ == "__main__":
    main()
