"""
Practice: Calculations
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
"""
def main():
    hi = int(input("Enter larger: "))
    lo = hi
    while lo >= hi:
        lo = int(input("Enter smaller: "))
  
    while lo <= hi:
        print(hi)
        hi -= 1

if __name__ == "__main__":
    main()
