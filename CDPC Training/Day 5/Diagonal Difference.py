def diagonalDifference(arr):
    n = len(arr)
    a = 0
    b = 0

    for i in range(n):
        a = a + arr[i][i]
        b = b + arr[i][n-1-i]

    return abs(a - b)


if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)