no = int(input("Enter Number: "))
sum = 0
temp = no
count = 0
while no>0:
    no = no//10 # it removes the last number
    count = count+1
temp=no
while no>0:
    rem = no%10
    sum = sum +rem**count
    no = no//10
if temp==sum:
    print("Armstrong")
else:
    print("not Armstrong") 

