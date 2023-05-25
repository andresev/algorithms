

# This is considered Big O(N^2)
# Ex: (N-1) + (N-2) + (N-3)
def printUnorderedPairs(array: list[int]):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(f"{i}, {j}")


n = [1, 2, 3, 4, 5, 6, 7, 8]
printUnorderedPairs(n)
