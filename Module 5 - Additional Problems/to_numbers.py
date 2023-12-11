
"""
Practice: Convert to Numbers
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 

def to_numbers(str_values: list):
    float_values = []
    for str_value in str_values:
        float_value = float(str_value)
        list(float_values.append(float_value))
    print(float_values)



to_numbers(["3.14", "42", "5.0", "invalid", "123.45"])
