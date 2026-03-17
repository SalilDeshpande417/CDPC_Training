# Accept 9 digit no and find sum of 1st and last digit in 3 steps
no = int(input("Enter a Number: "))
n1 = no%10; 
n2 = no//100000000
res = n1 + n2
print(res)
