def find_century(year):
    century = (year + 99) // 100
    return century

print(find_century(1700))