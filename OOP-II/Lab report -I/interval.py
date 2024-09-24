def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

print(f"Prime numbers between {lower} and {upper} are:")


for num in range(lower, upper + 1):
    if is_prime(num):
        print(num)
