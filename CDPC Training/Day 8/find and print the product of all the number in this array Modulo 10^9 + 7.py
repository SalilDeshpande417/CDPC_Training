N = int(input())
A = list(map(int,input().split()))
ten = 1000000007
sum = 1
for i in A:
    sum = (sum*i)%ten
print(sum) 