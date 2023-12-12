
"""
Practice: Count Negatives
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def count_negatives(numbers: list):
    counter = 0
    for i in numbers:
        if i < 0:
            counter += 1
    return counter
