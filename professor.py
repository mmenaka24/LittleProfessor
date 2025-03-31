import random


def main():
    level = get_level()

    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y

        correct = False

        for i in range(3):
            try:
                guess = int(input((f"{x} + {y} = ")))
            except ValueError:
                pass

            if guess == ans:
                correct = True
                break
            else:
                print("EEE")

        if correct:
            score += 1
        else:
            print(f"{x} + {y} = {ans}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if not level in [1, 2, 3]:
        raise ValueError
    else:
        return random.randint(0, pow(10, level) - 1)


if __name__ == "__main__":
    main()
