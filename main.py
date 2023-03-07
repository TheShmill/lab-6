# Will Albright
def main():
    # silly default, but whatever
    password = 0
    while True:
        option = get_option()
        # Encode
        if option == 1:
            num = int(input("Please enter your password to decode: "))
            password = combine_digits(map(shift_digit, get_digits(num)))
            print(f"Your password has been encoded and stored!")
        # Decode
        elif option == 2:
            # TODO
            pass
        # Quit
        else:
            return
        print()


def get_digits(num):
    result = []
    while num != 0:
        result.append(num % 10)
        num //= 10
    return reversed(result)


def shift_digit(d):
    return (d + 3) % 10


def combine_digits(digits):
    num = 0
    for digit in digits:
        num *= 10
        num += digit
    return num


def get_option():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    return int(input("Please enter an option: "))


if __name__ == "__main__":
    main()
