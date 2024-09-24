def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The H.C.F. of {num1} and {num2} is {compute_hcf(num1, num2)}")
