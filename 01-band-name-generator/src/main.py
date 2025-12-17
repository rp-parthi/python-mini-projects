def get_user_input(prompt: str) -> str:
    """Prompt the user until a valid (non-empty) input is given."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a valid input!")


def main() -> None:
    print("Welcome to the Band Name Generator!")

    city_name = get_user_input("What's the name of the city you grew up in? ")
    pet_name = get_user_input("What's your pet's name? ")

    print(f"Your band name could be: {city_name} {pet_name}")


if __name__ == "__main__":
    main()
