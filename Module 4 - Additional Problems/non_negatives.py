"""
Practice: Read Words
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
Write a program that reads a measurement in meters and the converts
it to inches, feet, and miles.
"""

def non_negative():
    integer = int(input("Enter an integer: "))

    if integer >= 0:
        print(integer)
        return non_negative()
    else:
        pass

def main():
    non_negative()

if __name__ == "__main__":
    main()
