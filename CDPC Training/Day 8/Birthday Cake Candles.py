def birthdayCakeCandles(candles):
    max1 = max(candles)
    ans = candles.count(max1)
    return ans


# 🔽 Main program 
candles_count = int(input("Enter number of candles: "))
candles = list(map(int, input("Enter candle heights: ").split()))

result = birthdayCakeCandles(candles)

print(result) 