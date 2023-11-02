
"""
Practice: Valid Anagrams
===========================
Course:   Leetcode
Semester: Fall 2023
Student:  Danny Lin
""" 

def isAnagram(self, s: str, t: str) -> bool:
    sorted_s = sort(s)
    sorted_t = sort(t)

    return sorted_s == sorted_t
