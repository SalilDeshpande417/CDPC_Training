# Peterson number check without loop

n = int(input("Enter a number: "))

# taking digits (for 3 digit number example)
a = n // 100
b = (n // 10) % 10
c = n % 10

# factorials written manually
fa = 1
if a == 1:
    fa = 1
elif a == 2:
    fa = 2
elif a == 3:
    fa = 6
elif a == 4:
    fa = 24
elif a == 5:
    fa = 120

fb = 1
if b == 1:
    fb = 1
elif b == 2:
    fb = 2
elif b == 3:
    fb = 6
elif b == 4:
    fb = 24
elif b == 5:
    fb = 120

fc = 1
if c == 1:
    fc = 1
elif c == 2:
    fc = 2
elif c == 3:
    fc = 6
elif c == 4:
    fc = 24
elif c == 5:
    fc = 120

sum = fa + fb + fc

if sum == n:
    print("Peterson Number")
else:
    print("Not Peterson Number") 


