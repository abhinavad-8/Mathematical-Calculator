def gcd_lcm_calculator():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    def lcm(a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // gcd(a, b)
    print("\n--- GCD & LCM Calculator ---")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD:", gcd(a, b))
    print("LCM:", lcm(a, b))


