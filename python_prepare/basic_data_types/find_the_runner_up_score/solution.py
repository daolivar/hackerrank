if __name__ == '__main__':
    # Read the integer input n (not used in this implementation)
    n = int(input())
    
    # Read the list of scores from the input, mapping them to integers
    arr = map(int, input().split())

    # Initialize win_score and runner_up to negative infinity
    # This helps track the largest and second largest numbers in the array
    win_score = float('-inf')
    runner_up = float('-inf')

    # Iterate through each score in the list
    for score in arr:
        # If current score is greater than the win_score, update runner_up and win_score
        if score > win_score:
            runner_up = win_score  # Previous win_score becomes the new runner_up
            win_score = score      # Current score is the new win_score
        # If the current score is between the win_score and the runner_up
        # and it is not equal to the win_score, update runner_up
        elif score > runner_up and score != win_score:
            runner_up = score  # Update runner_up with the current score

    # Output the runner-up score
    print(runner_up)
