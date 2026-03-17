def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in range(n):
        if arr[i] > 0:
            positive+=1
        elif arr[i] < 0:
            negative+=1
        else:
            zero+=1
    positive_ratio = positive/n
    negative_ratio = negative/n
    zero_ratio = zero/n 
    
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)
    
if __name__== '__main__':
    n = int(input().strip())
    arr = list(map(int,input().rstrip().split()))
    plusMinus(arr)  