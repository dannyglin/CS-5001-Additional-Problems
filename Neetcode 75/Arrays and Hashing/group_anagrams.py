
"""
Practice: Group Anagrams
===========================
Course:   Leetcode
Semester: Fall 2023
Student:  Danny Lin
""" 

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()
