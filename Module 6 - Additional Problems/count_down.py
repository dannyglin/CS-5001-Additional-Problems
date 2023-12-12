
"""
Practice: Print multiples of 5
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def count_down():
    for i in range(100, -1 , -5):
        if i != 0:
            print(i)
        else:
            print("Blastoff!")
