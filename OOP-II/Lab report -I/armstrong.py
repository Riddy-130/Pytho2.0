def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum


lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

print(f"Armstrong numbers between {lower} and {upper} are:")


for num in range(lower, upper + 1):
    if is_armstrong(num):
        print(num)
