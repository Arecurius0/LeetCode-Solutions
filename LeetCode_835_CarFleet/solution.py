def carFleet(target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed),reverse=True)
        stack = []
        for car in cars:
            #turns needed= (target - position)/speed
            stack.append(float(target -car[0])/car[1])
            if len(stack) >= 2:
                followingCar = stack.pop()
                leadingCar = stack.pop()
                if leadingCar >= followingCar:
                    stack.append(leadingCar)
                else:
                    stack.append(leadingCar)
                    stack.append(followingCar)
                    
            
        print(cars)
        print(stack)
        return len(stack)    

            
                    



def main():
    var1 = 10
    var2 = [6,8]
    var3 = [3,2]
    print("Test1:")
    res = carFleet(var1,var2,var3)
    print("Result", res)

if __name__ == "__main__":
    main()