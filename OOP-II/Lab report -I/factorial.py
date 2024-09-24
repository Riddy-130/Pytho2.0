def factorial_iterative(n):
    factorial = 1
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial


num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial_iterative(num)}")
