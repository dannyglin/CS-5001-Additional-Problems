"""
Practice: Read Words
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
Write a program that reads a measurement in meters and the converts
it to inches, feet, and miles.
"""

def count_up():
    integer = int(input("Enter an integer that is greater than 1: "))
    count = 1
        
    while count <= integer:
        print(count)
        count += 1

def main():
    count_up()

if __name__ == "__main__":
    main()
