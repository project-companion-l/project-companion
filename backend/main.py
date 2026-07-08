from companion.companion import Companion


def main() -> None:
    companion = Companion()

    companion.start()

    while True:
        user_input = input("You > ")

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        response = companion.chat(user_input)

        print(f"LC > {response}")


if __name__ == "__main__":
    main()