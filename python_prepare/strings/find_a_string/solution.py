def count_substring(string, sub_string):
    """
    Count the number of occurrences of a substring within a string.

    This method searches the provided `string` for the specified `sub_string`
    and counts the number of times it appears by finding all the start indices 
    where the substring occurs.

    Parameters:
    string (str): The main string in which to search for the substring.
    sub_string (str): The substring to search for in the main string.

    Returns:
    int: The number of times `sub_string` is found within `string`.
    """
    start = 0
    occurences = []

    # Find and count all occurrences of sub_string in the main string
    while True:
        index = string.find(sub_string, start)
        if index == -1:
            break  # Exit loop if no more occurrences are found
        occurences.append(index)
        start = index + 1  # Move start point after the found occurrence

    # Return the count of occurrences found
    return len(occurences)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
