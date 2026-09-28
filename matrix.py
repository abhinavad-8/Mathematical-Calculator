def matrix_menu():
    def input_matrix(name):
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
        matrix = []
        print(f"Enter {name} row by row:")
        for i in range(rows):
            while True:
                row = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(row) == cols:
                    matrix.append(row)
                    break
                else:
                    print(f"Please enter exactly {cols} numbers.")
        return matrix
    def print_matrix(matrix):
        for row in matrix:
            print(" ".join(f"{value:g}" for value in row))
    def matrix_addition(A, B):
        return [
            [A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))
        ]
    def matrix_subtraction(A, B):
        return [
            [A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))
        ]
    def matrix_multiplication(A, B):
        rows_A = len(A)
        cols_A = len(A[0])
        cols_B = len(B[0])
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    def transpose(A):
        return [list(row) for row in zip(*A)]
    def determinant(A):
        n = len(A)
        if n == 1:
            return A[0][0]
        if n == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]
        result = 0
        for col in range(n):
            minor = [
                [A[i][j] for j in range(n) if j != col]
                for i in range(1, n)
            ]
            result += ((-1) ** col) * A[0][col] * determinant(minor)

        return result
    print("\n--- Matrix Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    choice = input("Choose an operation: ")
    if choice in ["1", "2"]:
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            print("Matrices must have the same dimensions.")
            return
        if choice == "1":
            result = matrix_addition(A, B)
        else:
            result = matrix_subtraction(A, B)
        print("\nResult:")
        print_matrix(result)
    elif choice == "3":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if len(A[0]) != len(B):
            print("Number of columns in A must equal number of rows in B.")
            return
        result = matrix_multiplication(A, B)
        print("\nResult:")
        print_matrix(result)
    elif choice == "4":
        A = input_matrix("Matrix")
        print("\nTranspose:")
        print_matrix(transpose(A))
    elif choice == "5":
        A = input_matrix("Matrix")
        if len(A) != len(A[0]):
            print("Determinant is only defined for square matrices.")
            return
        print("\nDeterminant:", determinant(A))
    else:
        print("Invalid choice.")