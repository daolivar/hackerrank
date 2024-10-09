if __name__ == '__main__':
    # Take input from the user, strip any extra whitespace, and convert it to an integer
    n = int(input().strip())

    # Determine the output based on the value of n
    if n % 2 != 0:  # Odd n value
        print("Weird")
    elif n <= 5:  # Even n value, less than or equal to 5
        print("Not Weird")
    elif n <= 20:  # Even n value, between 6 and 20 (inclusive)
        print("Weird")
    else:  # n is greater than 20
        print("Not Weird")
