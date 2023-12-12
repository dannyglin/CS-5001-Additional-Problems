
"""
Practice: Print multiples of 5
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def multiples():
    number = int(input("Enter a positive integer: "))

    for i in range(5, number + 1, 5):
        print(i)
