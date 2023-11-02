
"""
Practice: Two Sum
===========================
Course:   Leetcode
Semester: Fall 2023
Student:  Danny Lin
""" 
def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[n] = index
    return
