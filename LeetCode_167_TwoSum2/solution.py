def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                res.append(i+1)
                res.append(j+1)
        
    return res

def twoSum3(numbers, target):
    lIndex = 0
    rIndex = len(numbers) -1

    while(lIndex +1 != rIndex):
        sum = numbers[lIndex]+numbers[rIndex]
        if sum == target:
            return [lIndex+1, rIndex+1]
        elif sum > target:
            rIndex -=1
        elif sum < target:
            lIndex +=1
    if numbers[lIndex] + numbers[rIndex] == target:
        return [lIndex+1, rIndex+1]
    else:
        return [-1,-1]
            

def main():
    var1 = [2,7,11,15]
    var2 = 9
    var3 = [3,2]

    print("Test1:")
    res = twoSum3(var1,var2)
    print("Result", res)

if __name__ == "__main__":
    main()