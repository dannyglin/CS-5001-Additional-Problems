"""
Practice: Rectangle (Area, Parameter, and Diagonal)
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def main():
    
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    print("The area of the rectangle is", width * height)
    print("The perimeter of the rectangle is", 2 * (width + height))
    print("The diagonal of the rectangle is", (width**2 + height**2)**0.5)


if __name__ == "__main__":
    main()
