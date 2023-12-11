"""
Practice: Multiples
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
Write a program that reads a measurement in meters and the converts
it to inches, feet, and miles.
"""

def multiples():
    integer = int(input("Enter a non-zero integer: "))
    
    while True:
        multiple = int(input("Enter a multiple: "))
        if multiple % integer == 0:
            print(f"Valid multiple entered: {multiple}")
            break
        else:
            print(f"Try again: {multiple}")
            
def main():
    multiples()

if __name__ == "__main__":
    main()
