def check_character(s: str, ch):
    c = 0
    for i in s:
        if i == ch:
            c += 1
    return c


if __name__ == "__main__":
    print(check_character('Order of the Phoenix', 'o'))

    # zakazano, ale lepsi je
    print("Order of the Phoenix".count("o"))