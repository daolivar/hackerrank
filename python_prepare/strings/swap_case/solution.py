def swap_case(s):
    """
    Swap the case of each letter in the input string.
    
    This function iterates through each character of the input string `s`:
    - If the character is uppercase, it is converted to lowercase.
    - If the character is lowercase, it is converted to uppercase.
    - Non-alphabetic characters remain unchanged.
    
    Parameters:
    s (str): The input string in which case conversion needs to be performed.
    
    Returns:
    str: A new string where all letter cases have been swapped.
    
    Approach:
    A list is used to accumulate the modified characters because strings in Python are immutable, 
    meaning that modifying a string creates a new one every time, which is inefficient in loops. 
    Using a list to collect characters and then joining them into a final string improves performance,
    especially for large inputs, because appending to a list is more efficient than continuously modifying strings.
    """
    # Initialize an empty list to hold the swapped characters
    result = []

    # Iterate over each character in the string
    for char in s:
        if char.isupper():
            # If the character is uppercase, convert it to lowercase
            result.append(char.lower())
        else:
            # If the character is lowercase (or non-letter), convert it to uppercase
            result.append(char.upper())

    # Join the list into a new string and return it
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
