import random


def main():
    level = get_level()

    score = 0

    for q in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y

        for attempt in range(3):
            try:
                guess = int(input((f"{x} + {y} = ")))
                if guess == ans:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                
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
    
    return random.randint(0, pow(10, level) - 1)


if __name__ == "__main__":
    main()
