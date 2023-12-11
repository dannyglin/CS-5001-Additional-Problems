
"""
Practice: Read Values
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def read_values():
    result = []
    while True:
        number = int(input("Enter a number: "))
        if number <= 0:
            break
        result.append(number)
    print(result)


read_values()

