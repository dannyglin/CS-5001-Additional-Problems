"""
Practice: Both Sides
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
Write a program that prompts with: Enter Value:" and reads in the integer value
from the keyboard and prints the appropriate messages depending upon the value of
that input.
"""

def main():
    value = int(float(input("Enter Value: ")))

    if value % 2 == 0:
        if value < 0:
            print("even negative number")
        else:
            print("even positive number")
    else:  
        if value < 0:
            print("odd negative number")
        else:
            print("odd positive number")


if __name__ == "__main__":
    main()
