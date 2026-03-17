def aVeryBigSum(ar):
    total = 0
    for i in range(len(ar)):
        total = total + ar[i]
    return total


if __name__ == '__main__':
    ar_count = int(input("Enter number of elements: "))
    ar = list(map(int, input("Enter numbers: ").split()))

    result = aVeryBigSum(ar)
    print("Sum =", result) 