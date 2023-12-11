"""
Practice: Length
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
Write a program that reads a measurement in meters and the converts
it to inches, feet, and miles.
"""

def main():

    meters = float(input("Enter length: "))

    print("The length in inches is ", meters * 39.3701)
    print("The length in feet is ", meters * 3.28084)
    print("The length in miles is", meters * 0.000621371)


if __name__ == "__main__":
    main()
