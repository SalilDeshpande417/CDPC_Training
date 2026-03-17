no = int(input("Enter Number: "))
rev = 0; 
temp = no
while no>0:
  rem = no%10 # it will give the last no in remainder
  rev = rev*10+rem #formula 
  no = no//10
if temp == rev:
    print("palindrome")
else: 
    print("not palindrome") 