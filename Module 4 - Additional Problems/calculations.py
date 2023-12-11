"""
Practice: Calculations
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
"""

def calculations():
    while True:
        num_values = int(input("Enter the number of values to read: "))
        
        if num_values <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            break

    input_count = 0
    total = 0

    while input_count < num_values:
        value = int(input("Enter an integer value: "))
        input_count += 1
        total += value

    average = value/num_values
    
    print(f"The sum is {total}")
    print(f"The sum is {average}")
     

def main():
    calculations()

if __name__ == "__main__":
    main()
