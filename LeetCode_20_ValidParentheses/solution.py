#https://leetcode.com/problems/valid-parentheses/
from collections import defaultdict


def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        #()[]{}
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                parenthesis = stack.pop()
                if ((parenthesis == '(' and c != ')') or
                    (parenthesis == '[' and c != ']') or
                    (parenthesis == '{' and c != '}')):
                    return False
        if stack.count() != 0:
            return False
        return True


        
    

        
     




def main():
    var = "(]"
    print("Test1: ")
    res = isValid(var)
    print("Result", res)

if __name__ == "__main__":
    main()