def is_leap(year):
    """
    Determines if a given year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # Initialize leap as False, assuming it's not a leap year
    leap = False

    # Check if the year is divisible by 4 but not divisible by 100,
    # or if it's divisible by 400 (special case for centuries)
    if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
        leap = True

    # Return the result (True if leap year, False otherwise)
    return leap
