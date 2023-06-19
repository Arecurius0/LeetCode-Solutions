def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    charlist = []
    for c in s.lower():
        asci = ord(c)
        if (asci >= ord("a") and asci <= ord("z")) or (asci >= ord("0") and asci <= ord("9")):
            charlist.append(c)
    
    for i in range(len(charlist)):
        if charlist[i] != charlist[(-1)*i-1]:
            return False
        
    return True


def main():
    var1 = "0P"
    var2 = [6,8]
    var3 = [3,2]
    print("Test1:")
    res = isPalindrome(var1)
    print("Result", res)

if __name__ == "__main__":
    main()