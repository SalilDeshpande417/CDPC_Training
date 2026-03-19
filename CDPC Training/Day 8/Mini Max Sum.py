def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum, max_sum)


if __name__ == "__main__":
    # Take input from user (space-separated integers)
    arr = list(map(int, input("Enter 5 numbers: ").split()))

    if len(arr) != 5:
        print("Please enter exactly 5 integers.")
    else:
        miniMaxSum(arr) 