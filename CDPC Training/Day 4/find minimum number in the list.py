arr = [4, 50, 35, 75, 100]

minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num

print(minimum)