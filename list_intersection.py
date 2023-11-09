
def find_intesection(inputList):
    return list(set.intersection(*map(set, inputList)))
    # intersection = []
    # for nestedList in inputList:
    #   .......

    #     intersection.append(nestedList[i])
    # return set(intersection)

print(find_intesection([
  [0, 1, 2, 3, 6],
  [0, 2, 1, 3, 6],
  [2, 3, 0, 4, 6],
  [0, 3, 4, 5, 8, 6, 1]
]))
