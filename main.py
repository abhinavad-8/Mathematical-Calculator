import math
from collections import Counter
from statistics import statistics_calculator
from gcd_and_lcm import gcd_lcm_calculator
from geometrical import geometry_calculator
from matrix import matrix_menu
from polynomial import polynomial

def main():
    while True:
        print("\n")
        print("." * 40)
        print("~" * 40)
        print("       MATHEMATICAL CALCULATOR")
        print("~" * 40)
        print("." * 40)
        print("\n")
        print("1. Statistics Calculator")
        print("2. Matrix Calculator")
        print("3. Polynomial Calculator")
        print("4. Geometry Calculator")
        print("5. GCD & LCM Calculator")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            statistics_calculator()
        elif choice == "2":
            matrix_menu()
        elif choice == "3":
            polynomial()
        elif choice == "4":
            geometry_calculator()
        elif choice == "5":
            gcd_lcm_calculator()
        elif choice == "6":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
