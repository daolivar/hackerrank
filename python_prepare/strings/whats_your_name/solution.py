def print_full_name(first, last):
    """
    Print a greeting message using the provided first and last name.

    Parameters:
    first (str): The first name of the person.
    last (str): The last name of the person.

    The function prints a message in the format:
    "Hello {first} {last}! You just delved into python."
    """
    # Use formatted string to print the full name and a greeting message
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    # Read first name from input
    first_name = input()
    # Read last name from input
    last_name = input()
    # Call the function to print the full greeting message
    print_full_name(first_name, last_name)
