T = int(input().strip())

for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    K = K % N

    result = arr[-K:] + arr[:-K]

    print(*result)