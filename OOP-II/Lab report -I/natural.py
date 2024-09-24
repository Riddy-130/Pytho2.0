def sum_of_natural_numbers_formula(n):
    return n * (n + 1) // 2


num = int(input("Enter a positive number: "))
if num < 0:
    print("Please enter a positive number")
else:
    print(f"The sum of natural numbers up to {num} is {sum_of_natural_numbers_formula(num)}")
