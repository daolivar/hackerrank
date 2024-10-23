import textwrap

# Function to wrap a string based on a specified width
def wrap(string, max_width):
    # Use textwrap.fill() to wrap the input string to the specified width
    wrapped_text = textwrap.fill(string, width=max_width)
    return wrapped_text

if __name__ == '__main__':
    # Take the input string and the maximum width for wrapping
    string, max_width = input(), int(input())

    # Call the wrap function to wrap the string and return the wrapped text
    result = wrap(string, max_width)

    # Print the wrapped text
    print(result)
