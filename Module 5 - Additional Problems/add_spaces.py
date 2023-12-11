
"""
Practice: Add Space
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def add_spaces(input_string: str):
    result = ""

    for char in input_string:
        result += char + " "

    result = result.rstrip() #Remove the trailing space

    return result
