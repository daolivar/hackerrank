if __name__ == '__main__':
    N = int(input())  # Read the number of commands from user input
    operand_list = []  # Initialize an empty list to store the operands

    # Command mapping for better readability and maintainability
    command_map = {
        "insert": lambda params: operand_list.insert(params[0], params[1]),  # Insert at specified index
        "print": lambda params: print(operand_list),  # print the current state of the list
        "remove": lambda params: operand_list.remove(params[0]),  # Remove the specified value
        "append": lambda params: operand_list.append(params[0]),  # Append a value to the end
        "sort": lambda params: operand_list.sort(),  # Sort the list in ascending order
        "pop": lambda params: operand_list.pop(),  # Remove and return the last element
        "reverse": lambda params: operand_list.reverse()  # Reverse the list
    }

    # Loop through the number of commands
    for _ in range(N):
        cmd, *params = input().split()  # Read a command and its parameters
        # Check if the command exists in the command mapping
        if cmd in command_map:
            # Convert parameters to integers and execute the corresponding command
            command_map[cmd]([int(p) for p in params])  # Convert parameters to int only if needed
