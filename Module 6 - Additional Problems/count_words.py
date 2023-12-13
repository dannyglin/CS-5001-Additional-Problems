
"""
Practice: Count Words
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


sentence = input("Enter a sentence: ")

for index, word in enumerate(sentence.split()):
    print(f"{index}. {word}")
