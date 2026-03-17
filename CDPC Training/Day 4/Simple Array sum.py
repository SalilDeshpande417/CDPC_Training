def simpleArraySum(ar):
    total = 0
    for i in range(len(ar)):
        total = total + ar[i]
    return total

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().strip().split()))

    result = simpleArraySum(ar)

    print(result) 