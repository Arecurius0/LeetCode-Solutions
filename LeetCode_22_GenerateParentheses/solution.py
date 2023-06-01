def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        stack = []

        def recursiveHelper(open_counter, closed_counter):
            if open_counter == closed_counter == n:
                result.append("".join(stack))
                return result
    
            if open_counter < n:
                stack.append("(")
                recursiveHelper(open_counter+1, closed_counter)
                stack.pop()

            if closed_counter < open_counter:
                stack.append(")")
                recursiveHelper(open_counter, closed_counter+1)
                stack.pop()
        recursiveHelper(0,0)
        return result


def main():
    var = 4
    print("Test1:")
    res = generateParenthesis(var)
    print("Result", res)

if __name__ == "__main__":
    main()