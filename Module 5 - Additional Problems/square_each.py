
"""
Practice: Square Each
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 

def square_each(number_list: list):

    for i in range(len(number_list)):
        number_list[i] = number_list[i] **2

    return number_list

square_each([1,2,3,4,5,6,7,8,9,10])
