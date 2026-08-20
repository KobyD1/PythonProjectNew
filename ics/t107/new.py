def process_grades(grades_list):
    """
    Processes a list of grades to identify valid grades (between 0 and 100),
    prints any invalid grades, and calculates the average of the valid grades.

    Args:
        grades_list (list): A list of numerical grades.
    """
    valid_grades = []
    invalid_grades = []

    for grade in grades_list:
        if 0 <= grade <= 100:
            valid_grades.append(grade)
        else:
            invalid_grades.append(grade)

    # Print all invalid values
    if invalid_grades:
        print(f"Invalid grades found: {invalid_grades}")
    else:
        print("No invalid grades found.")

    # Calculate and print the average of valid grades
    if valid_grades:
        average = sum(valid_grades) / len(valid_grades)
        print(f"Average of valid grades: {average:.2f}")
    else:
        print("No valid grades found to calculate an average.")


# Example usage:
grades_example = [77, 34, 56, 89, 98, 120, -45]
print("--- Processing Example Grades ---")
process_grades(grades_example)

print("\n--- Processing Grades with All Valid Values ---")
grades_all_valid = [85, 92, 78, 100, 65]
process_grades(grades_all_valid)

print("\n--- Processing Grades with All Invalid Values ---")
grades_all_invalid = [-10, 101, 150]
process_grades(grades_all_invalid)

print("\n--- Processing an Empty List of Grades ---")
grades_empty = []
process_grades(grades_empty)

print("\n--- Processing Grades Including a Zero ---")
grades_with_zero = [75, 0, 90, 50, 100]
process_grades(grades_with_zero)
