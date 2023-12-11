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
    word = input("")

    if word == "Hi":
        print("Hi, how are you?\nDone")
    else:
        print("Done")


if __name__ == "__main__":
    main()
