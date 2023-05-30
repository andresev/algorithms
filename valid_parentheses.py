def validParetheses(s):
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            print(False)
            return False
        stack.pop()

        print(True)
        return not stack
