if __name__ == '__main__':
    # Read the number of students
    n = int(input())

    # Create a dictionary to store student names and their scores
    student_marks = {}

    # Loop to read student data
    for _ in range(n):
        # Input the name and the scores for each student
        name, *line = input().split()
        # Convert the scores from strings to floats and store them in the dictionary
        student_marks[name] = list(map(float, line))

    # Get the name of the student whose average score is queried
    query_name = input()

    # Retrieve the scores for the queried student and calculate the average
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Print the average score formatted to 2 decimal places
    print(f"{average_score:.2f}")
