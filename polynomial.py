def polynomial():
    print("\n--- Polynomial Calculator ---")
    degree = int(input("Enter degree of polynomial: "))
    coefficients = []
    print("\nEnter coefficients from highest power to constant.")
    for i in range(degree + 1):
        power = degree - i
        coefficient = float(input(f"Coefficient of x^{power}: "))
        coefficients.append(coefficient)
    x = float(input("\nEnter value of x: "))
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    print("\nPolynomial value:")
    print(f"P({x}) =", result)