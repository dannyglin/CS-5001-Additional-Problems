"""
Practice: Read Words
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
Write a program that reads a measurement in meters and the converts
it to inches, feet, and miles.
"""

def read_and_print_words():
    word_string = ""

    while True:
        word = input("Enter a word: ")
        if word.lower() == "stop":
            break
        word_string += word + " "

    word_string = word_string.strip()
    print(word_string)

def main():
    read_and_print_words()

if __name__ == "__main__":
    main()
