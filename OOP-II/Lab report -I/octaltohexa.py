
def octal_to_hexadecimal(octal_num):
    
    decimal_num = int(octal_num, 8)
    
    hexadecimal_num = hex(decimal_num)
    return hexadecimal_num

octal_num = input("Enter an octal number: ")


hexadecimal_num = octal_to_hexadecimal(octal_num)
print(f"The hexadecimal representation of octal number {octal_num} is {hexadecimal_num}")
