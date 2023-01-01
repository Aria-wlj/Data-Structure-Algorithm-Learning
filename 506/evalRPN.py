from typing import List

class ArrayStack():
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self._data[-1]

    def push(self, e):
        return self._data.append(e)

    def pop(self):
        if self.isEmpty():
            return None
        return self._data.pop()

'''
evaluating a Reverse Polish notation using Stack
'''
def evalRPN(tokens: List[str]) -> int:
    # print("--------", tokens[0])
    stk = ArrayStack()
    for i in tokens:
        if i.isnumeric() or len(i) > 1:
            if i[0] == "-":
                result = 0 - int(i[1:])
            else:
                result = int(i)
            # print(result)
        else:
            num2 = stk.pop()
            print("~~~  pop({})".format(num2))
            num1 = stk.pop()
            print("~~~  pop({})".format(num1))
            # print(num1, "   ", num2)
            if i == "+":
                result = num1 + num2
            elif i == "-":
                result = num1 - num2
            elif i == "*":
                result = num1 * num2
        stk.push(result)
        print("~~~  push({})".format(result))
    return stk.pop()

if __name__ == '__main__':
    lst = ["5", "4", "-", "2", "1", "+", "+", "3", "*"]
    print(evalRPN(lst))
