import random


def main():
    level = get_level()
    operation = get_mode()

    score = 0

    for q in range(10):
        ans, q_str = generate_question(level, operation)

        for attempt in range(3):
            try:
                guess = int(input(q_str))
                if guess == ans:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                
        else:
            print(q_str + str(ans))

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level (1-3): "))
            if not level in [1, 2, 3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def get_mode():
    instruction_string = "\n".join(
        (
            "====Supports the following modes====",
            "+ for addition",
            "- for subtraction",
            "x for multiplication",
            "/ for division",
        )
    )
    print(instruction_string)

    while True:
        operation = input("Mode: ")
        if operation in ["+", "-", "x", "/"]:
            return operation


def generate_integer(level):
    if not level in [1, 2, 3]:
        raise ValueError

    return random.randint(0, pow(10, level) - 1)


def generate_question(level, operation):
    if not operation in ["+", "-", "x", "/"]:
        raise ValueError
    
    x = generate_integer(level)

    while True:
        y = generate_integer(level)
        if not (operation == "/" and y == 0):
            break

    match operation:
        case "+":
            ans = x + y
            q_str = f"{x} + {y} = "
        case "-":
            ans = x - y
            q_str = f"{x} - {y} = "
        case "x":
            ans = x * y
            q_str = f"{x} x {y} = "
        case "/":
            ans = x
            q_str = f"{x*y} / {y} = "

    return (ans, q_str)


if __name__ == "__main__":
    main()
