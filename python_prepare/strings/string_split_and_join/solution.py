def split_and_join(line):
    """
    Split the input string by spaces and join the words with hyphens.
    Leading and trailing whitespace is trimmed.

    Parameters:
    line (str): A string that may contain words separated by spaces.

    Returns:
    str: A string where spaces have been replaced by hyphens.
    """
    return "-".join(line.strip().split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
