no = int(input("Enter Number: ")) 
count = 0
while no>0:
    no = no//10 # it removes the last number
    count = count+1
print(count) 