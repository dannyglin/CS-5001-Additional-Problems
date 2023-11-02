
"""
Neetcode 75: Contains Duplicates
===========================
Course:   Leetcode
Semester: Fall 2023
Student:  Danny Lin
""" 

def containsDuplicate(self, sums: List[int]) -> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False
