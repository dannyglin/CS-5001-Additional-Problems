"""
Practice: String Equality
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin

Write a program that reads in a word from the keyboard and prints "Hi, how are you"
and "Done" if someone enters the word "Hi" (capitalization matters).
Otherwise it just prints "Done"
"""

def main():
    value = int(input("Enter value: "))

    if value > 100:
        print(f"Too big, clamping required\nValue is {value}")
    elif value < 1:
        print(f"Too small, clamping required\nValue is {value}")
    else:
        print(f"Value is {value}")


if __name__ == "__main__":
    main()
