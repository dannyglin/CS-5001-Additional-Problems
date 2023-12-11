
"""
Practice: Area of a triangle with 3 sides
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 
import math

def area_triangle(side1,side2,side3):
    """
    Outputs the area of a triangle with 3 sides
    """
    a = (side1 + side2 + side3) / 2
   
    return math.sqrt(a * (a - side1) * (a - side2) * (a - side3))

