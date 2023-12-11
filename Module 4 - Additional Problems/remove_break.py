"""
Practice: Calculations
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
"""
def main():
    a = 0
    b = 1
    print("0\n1")
    c = a + b
    
    while c <= 1000:
        print(c)
        a, b = b, c
        c = a + b


if __name__ == "__main__":
    main()
