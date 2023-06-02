def dailyTemperatures_quadraticTime(t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(t)
        for i in range(len(t)):
            counter = 0
            for j in range(i+1, len(t)):
                counter +=1
                if t[i] < t[j]:
                    res[i] = counter
                    break
        return res

def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack =[]
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = (temperatures[i], i)
            while stack and temp[0] > stack[-1][0]:
                prevTemp = stack.pop()
                output[prevTemp[1]] = i - prevTemp[1]
            stack.append(temp)
        return output
            
                    



def main():
    var = [30,40,50,60]
    print("Test1:")
    res = dailyTemperatures(var)
    print("Result", res)

if __name__ == "__main__":
    main()