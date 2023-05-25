

# This is considered Big O(N^2)
def printUnorderedPairs(array: list[int]):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            print(f"{i}, {j}")


n = [1, 2, 3, 4, 5]
printUnorderedPairs(n)
