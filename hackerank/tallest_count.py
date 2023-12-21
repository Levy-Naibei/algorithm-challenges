"""
Given an list of candles with height in integer.
Return the number of tallest candles
"""
def birth_day_cake_candles(candles):
    tall_count = 0
    max_height=max(candles)
    for i in range(len(candles)-1):
        if candles[i] == max_height:
            tall_count += 1
    return tall_count

print(birth_day_cake_candles([4, 2, 5, 4]))
