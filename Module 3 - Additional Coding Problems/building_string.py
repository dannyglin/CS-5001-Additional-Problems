
"""
Practice: Building a string
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 

def building_string(msg: str, int_1: int, int_2: int, int_3: int) -> str:
    """
    Write a function called build_string that takes a string value,
    and three integer values and returns a single string containing 3 lines.
    One each line, the string value is repeated the specified number of times.
    """
    return msg * int_1 + '\n' + msg * int_2 + '\n' + msg * int_3 + '\n'
