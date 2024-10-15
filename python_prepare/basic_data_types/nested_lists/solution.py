if __name__ == '__main__':
    # Initialize an empty list to store student names and scores
    student_scores = []

    # Read the number of students
    for _ in range(int(input())):
        name = input()  # Get the student's name
        score = float(input())  # Get the student's score as a float
        new_list = [name, score]  # Create a new list containing the name and score
        student_scores.append(new_list)  # Append the new list to the student_scores list

    # Extract unique scores from student_scores, sort them, and convert to a list
    scores = sorted(list(set([inner_list[1] for inner_list in student_scores])))

    # Identify the second lowest score from the sorted scores list
    second_lowest = scores[1]

    # Create a sorted list of names of students who have the second lowest score
    names = sorted([inner_list[0] for inner_list in student_scores if inner_list[1] == second_lowest])

    # Print the names of students with the second lowest score
    for name in names:
        print(name)
