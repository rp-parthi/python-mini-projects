def get_pizza_size(prompt: str) -> str:
    valid_sizes = ('s', 'm', 'l')
    while True:
        value = input(prompt).strip().lower()
        if value in valid_sizes:
            return value
        print("Please enter S, M, or L.")


def get_yes_no(prompt: str) -> str:
    while True:
        value = input(prompt).strip().lower()
        if value in ('y', 'n'):
            return value
        print("Please enter Y or N.")

BASE_PRICE = {
    's': 15,
    'm': 20,
    'l': 25
}

PEPPERONI_PRICE = {
    's': 2,
    'm': 3,
    'l': 3
}

def calculate_total(size: str, pepperoni: str, extra_cheese: str) -> int:
    total = BASE_PRICE[size]

    if pepperoni == 'y':
        total += PEPPERONI_PRICE[size]

    if extra_cheese == 'y':
        total += 1

    return total


def main():
    print("Welcome to Python Pizza Deliveries!")

    size = get_pizza_size("What size pizza do you want? S, M or L: ")
    pepperoni = get_yes_no("Do you want pepperoni? Y or N: ")
    extra_cheese = get_yes_no("Do you want extra cheese? Y or N: ")

    total_price = calculate_total(size, pepperoni, extra_cheese)

    print(f"Your total bill is: ${total_price}")


if __name__ == "__main__":
    main()
