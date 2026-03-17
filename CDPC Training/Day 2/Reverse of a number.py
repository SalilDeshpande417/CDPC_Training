no = int(input("Enter Number: "))
rev = 0; 
while no>0:
  rem = no%10 # it will give the last no in remainder
  rev = rev*10+rem #formula 
  no = no//10  #it will remove the last number
print("Reverse is", rev)
  