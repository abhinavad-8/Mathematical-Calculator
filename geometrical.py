import math
def geometry_calculator():
    print("\n--- Geometry Calculator ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Sphere")
    print("6. Cylinder")
    choice = input("Choose a shape: ")
    if choice == "1":
        radius = float(input("Enter radius: "))
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print("Area:", area)
        print("Circumference:", circumference)
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        perimeter = 2 * (length + width)
        print("Area:", area)
        print("Perimeter:", perimeter)
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area:", area)
    elif choice == "4":
        side = float(input("Enter side: "))
        area = side ** 2
        perimeter = 4 * side
        print("Area:", area)
        print("Perimeter:", perimeter)
    elif choice == "5":
        radius = float(input("Enter radius: "))
        surface_area = 4 * math.pi * radius ** 2
        volume = (4 / 3) * math.pi * radius ** 3
        print("Surface Area:", surface_area)
        print("Volume:", volume)
    elif choice == "6":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        surface_area = 2 * math.pi * radius * (radius + height)
        volume = math.pi * radius ** 2 * height
        print("Surface Area:", surface_area)
        print("Volume:", volume)
    else:
        print("Invalid choice.")


