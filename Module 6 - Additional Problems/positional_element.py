
"""
Practice: Positional Element
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def positional_elements(data):
    count = 0
    for i, element in enumerate(data):
        if i == element:
            count += 1
    return count
