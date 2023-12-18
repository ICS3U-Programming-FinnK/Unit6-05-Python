#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: December 19th, 2023
# This program uses loops to create a list to calculate the average grades inputted from the user
def calc_average(marks):
    # Checking if the list of marks is empty
    if len(marks) == 0:
        raise ValueError("List of marks is empty.")

    # Calculating the sum of all marks
    total = sum(marks)

    # Calculating the average by dividing the sum by the number of marks
    average = total / len(marks)

    return average


def main():
    # Creating an empty list to store the marks
    marks = []

    # Loop to repeatedly ask the user for marks
    while True:
        try:
            # Asking the user to enter a mark
            mark = int(input("Enter a mark between 0 and 100 (-1 to stop): "))

            # Checking if the user wants to stop entering marks
            if mark == -1:
                break

            # Checking if the mark is within the valid range
            if mark < 0 or mark > 100:
                raise ValueError("Invalid mark. Please enter a mark between 0 and 100.")

            # Adding the mark to the list
            marks.append(mark)

        except ValueError:
            print("Error: Invalid input, you entered a string, not a mark.")

    try:
        # Calculating the average of the marks
        average = calc_average(marks)

        # Displaying the average
        print("Average of marks:", average)

    except ValueError as e:
        print("Error:", e)


# Calling the main function
if __name__ == "__main__":
    main()
