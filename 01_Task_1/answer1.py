def check_character(s: str, ch):
    c = 0
    for i in s:
        if i == ch:
            c += 1
    return c


if __name__ == "__main__":
    assert check_character('Order of the Phoenix', 'o') == 2