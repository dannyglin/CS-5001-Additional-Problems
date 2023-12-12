"""
Practice: String Equality
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Danny Lin

Write a program that reads in a word from the keyboard and prints "Hi, how are you"
and "Done" if someone enters the word "Hi" (capitalization matters).
Otherwise it just prints "Done"
"""

def main():
    print("p\tq\tr\tA\tB")
    for p in [False, True]:
        for q in [False, True]:
            for r in [False, True]:
                A = (p and q) or (not r)
                B = not (p and (q or not r))

                print(f"{p}\t{q}\t{r}\t{A}\t{B}")

if __name__ == "__main__":
    main()
