num = int(input("Enter a number: "))

sum = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10

print("Sum of digits =", sum) 