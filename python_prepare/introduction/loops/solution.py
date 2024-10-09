# This block ensures that the following code runs only when this script is executed directly
if __name__ == '__main__':
    # Read an integer input from the user and assign it to variable 'n'
    n = int(input())

    # Loop through the range from 0 to n-1 (inclusive)
    for i in range(n):
        # Print the square of the current value of 'i'
        print(i**2)
