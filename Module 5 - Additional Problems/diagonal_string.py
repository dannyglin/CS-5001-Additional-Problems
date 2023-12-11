
"""
Practice: Diagonal String
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 

def diagonal_string(word: str):

    space = 0
    for i in range(len(word)):
        print(' ' * space + word[i])
        space += 1
