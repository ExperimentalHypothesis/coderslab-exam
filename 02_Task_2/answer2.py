from random import randint as ri


def get_random(number=3):
    if not isinstance(number, int):
        raise Exception("Invalid Data!")

    s = set()
    while True:
        s.add(ri(1, 100))
        if len(s) == number:
            return sorted(list(s))



if __name__ == "__main__":
    print(get_random(10))


