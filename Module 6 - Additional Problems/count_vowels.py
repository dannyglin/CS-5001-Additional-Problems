
"""
Practice: Print multiples of 5
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def count_vowels(string: str):
    vowels = "aeiou"
    vowel_count = 0
    for char in string.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count
