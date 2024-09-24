
def decimal_to_binary(n):
    binary_number = ''
    while n > 0:
        binary_number = str(n % 2) + binary_number
        n = n // 2
    return binary_number


decimal_number = int(input("Enter a decimal number: "))


binary_number = decimal_to_binary(decimal_number)

print(f"The binary representation of {decimal_number} is {binary_number}")
