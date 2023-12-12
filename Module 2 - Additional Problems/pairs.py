"""
Practice: Pairs
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin

"""

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    numbers = [num1, num2, num3, num4]
    numbers.sort()

    if numbers[0] == numbers[1] and numbers[2] == numbers[3]:
        print(f"{num1} {num2} {num3} {num4} two pairs")
    else:
        print(f"{num1} {num2} {num3} {num4} not two pairs")

if __name__ == "__main__":
    main()
