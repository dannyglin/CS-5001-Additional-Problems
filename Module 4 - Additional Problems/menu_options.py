"""
Practice: Calculations
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
"""

def menu_options():
    """
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 1
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 3
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 5
    Invalid option
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 0
    Result: OxXx
    """
    result = ''
    
    while True:
        menu = input('0 -- Quit\n1 -- Add "O"\n2 -- Add "oo"\n3 -- Add "xXx"\nOption: ')
        if menu == "1":
            result += "O"
        elif menu == "2":
            result += "oo"
        elif menu == "3":
            result += "xXx"
        elif menu == "0":
            print(result)
            break
        else:
            print("Please select a number 0 through 4")
            

def main():
    menu_options()

if __name__ == "__main__":
    main()
