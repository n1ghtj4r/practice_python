def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[0:length-1]
    given_check_digit = isbn[length-1]

    # Check for invalid characters
    for char in main_digits:
        if not char.isdigit():
            print('Invalid character was found.')
            return

    if length == 10:
        if not (given_check_digit.isdigit() or given_check_digit == 'X'):
            print('Invalid character was found.')
            return
    else:  # length == 13
        if not given_check_digit.isdigit():
            print('Invalid character was found.')
            return

    main_digits_list = [int(digit) for digit in main_digits]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11

    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10

    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')

    if len(values) != 2:
        print('Enter comma-separated values.')
        return

    isbn = values[0].strip()
    length_str = values[1].strip()

    if not length_str.isdigit():
        print('Length must be a number.')
        return

    length = int(length_str)

    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    # Check for invalid characters early (except X is allowed only as last digit of ISBN-10)
    for i, char in enumerate(isbn):
        if char == 'X' and not (length == 10 and i == len(isbn) - 1):
            print('Invalid character was found.')
            return
        if not (char.isdigit() or char == 'X'):
            print('Invalid character was found.')
            return

    validate_isbn(isbn, length)


# Comment out the call to main so the tests can work properly
main()