for i in range(1, 10000):
    no = i
    temp = no
    sum = 0
    count = 0

    
    while temp > 0:
        temp = temp // 10
        count = count + 1

    temp = no

    
    while temp > 0:
        rem = temp % 10
        sum = sum + rem ** count
        temp = temp // 10

    
    if no == sum:
        print(no, "Armstrong")