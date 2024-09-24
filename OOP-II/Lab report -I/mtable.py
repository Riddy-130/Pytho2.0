
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

#
num = int(input("Enter the number for the multiplication table: "))
multiplication_table(num)
