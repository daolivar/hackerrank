if __name__ == '__main__':
    # Take input string from the user
    s = input()

    # Check if any character in the string is alphanumeric (either a letter or a number)
    alnum = any(char.isalnum() for char in s)

    # Check if any character in the string is alphabetic (either uppercase or lowercase letter)
    alpha = any(char.isalpha() for char in s)

    # Check if any character in the string is a digit (numeric character)
    digits = any(char.isdigit() for char in s)

    # Check if any character in the string is a lowercase letter
    lower = any(char.islower() for char in s)

    # Check if any character in the string is an uppercase letter
    upper = any(char.isupper() for char in s)

    # Print the boolean results for each of the checks, each on a new line
    print(f"{alnum}\n{alpha}\n{digits}\n{lower}\n{upper}")
