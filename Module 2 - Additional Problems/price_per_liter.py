"""
Practice: RPrice per liter
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin
""" 


def main():

    six_pack_price = float(input("Price per six-pack: "))
    two_liter_price = float(input("Price per two-liter: "))

    print("Six-pack price per liter:", six_pack_price/2.13)
    print("Two-liter price per liter:", two_liter_price/2)


if __name__ == "__main__":
    main()
