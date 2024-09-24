def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    return (x * y) // compute_gcd(x, y)

#
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The L.C.M. of {num1} and {num2} is {compute_lcm(num1, num2)}")
