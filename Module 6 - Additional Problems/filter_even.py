
"""
Practice: Print multiples of 5
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def filter_evens(numbers: list):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
