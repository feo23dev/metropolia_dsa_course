def check_balance(input):
    input = "a(b)c[d]e{f}g"
    times = 0
    stack = []

    hashTable = {")": "(", "]": "[", "}": "{"}

    for index, char in enumerate(input):
        if char == "(" or char == "[" or char == "{":
            stack.append(char)

        if char in hashTable:

            if stack and stack[-1] == hashTable[char]:
                stack.pop()
                times += 1

            else:
                return f"Match error at position {index}"

    if len(stack) == 0:
        return f"Ok - {times}"
    else:
        return f"Match error at position {len(input)-1}"


print(check_balance(input))
