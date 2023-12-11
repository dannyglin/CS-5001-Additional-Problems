
"""
Practice: Grade
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 

def grade(value:int):
    """
    Using the following grading scale, write a function called grade
    that receives a score and returns the letter grade for that score.
    """
    if value >= 93 and value <= 100:
        return "A"
    elif value >= 90 and value < 93:
        return "A-"
    if value >= 86 and value < 90:
        return "B+"
    if value >= 82 and value < 86:
        return "B"
    if value >= 77 and value < 82:
        return "B-"
    if value >= 73 and value < 77:
        return "C+"
    if value >= 69 and value < 73:
        return "C"
    if value >= 65 and value < 69:
        return "C-"
    if value >= 0 and value < 65:
        return "F"

    
    

