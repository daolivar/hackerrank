def mutate_string(string, position, character):
    """
    Mutates the input string by changing the character at a specified position.

    Parameters:
    string (str): The original string.
    position (int): The index at which the character is to be changed.
    character (str): The new character to place at the specified position.

    Returns:
    str: The modified string with the character replaced at the given position.
    """
    # Convert the string into a list of characters since strings are immutable
    characters = list(string)

    # Modify the character at the specified position
    characters[position] = character

    # Join the list back into a string and return the result
    return "".join(characters)

if __name__ == '__main__':
    # Take input for the string
    s = input()

    # Take input for the position and the new character, split them into separate variables
    i, c = input().split()

    # Call the mutate_string function with the provided inputs, converting 'i' to an integer
    s_new = mutate_string(s, int(i), c)

    # Print the mutated string
    print(s_new)
