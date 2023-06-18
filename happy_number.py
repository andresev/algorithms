def isHappy(n):
    visited = set()

    while sum != 1 and n not in visited:
        visited.add(n)
        n = sum(int(num)**2 for num in str(n))

    return n == 1
