def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ["/", "*", "+", "-"]:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    stack.append(op2 + op1)
                if token == '-':
                    stack.append(op2 - op1)
                if token == '*':
                    stack.append(op2 * op1)
                if token == '/':
                    #stack.append(int(op2 // op1))
                    stack.append((op2+(-op2%op1))//op1)
            else:
                n = int(token)
                stack.append(n)
            print(stack)
        return stack[-1]



def main():
    var = ["4","13","5","/","+"]
    print("Test1:")
    res = evalRPN(var)
    print("Result", res)

if __name__ == "__main__":
    main()