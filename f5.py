""" A water reservation system constructed in a city has several opening and closing gates. 
If any opening gates are not closed with a corresponding closing gate then the water will 
leak out of the system and there will be a threat to the life of people living in the city. 
Also, the closing gate cannot exist without the opening gate, so the system head checks the 
design of the system and he has to ensure that the people are safe in the city. 
Write an algorithm to find whether people are safe or not. """

def findTotalGates(gateStr):
    open_list = ["("]
    close_list = [")"]
    stack = []
    for i in gateStr:
        if i in gateStr:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return -1
    return int(len(gateStr)/2)


gateStr = "()(())(())"
res = findTotalGates(gateStr)
print(res)