import os

# Complete the solve function below.
def solve(s):
    # Split the input string 's' into a list of words, using spaces as the delimiter
    words = s.split(' ')

    # Capitalize the first letter of each word in the list using list comprehension
    capitalized_words = [word.capitalize() for word in words]

    # Join the list of capitalized words back into a single string with spaces
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    # Open the output file to write the result
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Take input string from the user
    s = input()

    # Call the solve function to process the input string
    result = solve(s)

    # Write the result to the output file followed by a newline
    fptr.write(result + '\n')

    # Close the file after writing the result
    fptr.close()
