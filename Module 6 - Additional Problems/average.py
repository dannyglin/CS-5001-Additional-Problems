
"""
Practice: Print multiples of 5
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def calculate_average(numbers: list):
    total_sum = 0
    for i in numbers:
        total_sum += i
    return total_sum/len(numbers)
