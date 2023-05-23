#https://leetcode.com/problems/product-of-array-except-self/
import collections
def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #calculate prefix list
        prefix = []
        for i in range(len(nums)):
            if i <= 0:
                 prefix.append(nums[i])
                 continue
            prefix.append(nums[i]*prefix[i-1])

        #calculate postfix list
        postfix = [0]*len(nums)
        for i in range(len(nums) -1, -1, -1):
            #print(i)
            if i == len(nums)-1:
                 postfix[i] = nums[i]
                 continue
            postfix[i] = nums[i]*postfix[i+1]

        #calculate the output
        output = []
        for i in range(len(nums)):
            if i == 0:
                 output.append(postfix[i+1])
            elif i == len(nums)-1:
                 output.append(prefix[i-1])
            else:
                 output.append(prefix[i-1]*postfix[i+1])

        print("prefix:", prefix)
        print("postfix:", postfix)
        return output

def productExceptSelf2(nums):
     """
     :type nums: List[int]
     :rtype: List[int]
     """
     output = [1] * len(nums)

     pref = 1
     for i in range(len(nums)):
          output[i] = pref
          pref *= nums[i]
     #print(output)

     postf = 1
     for i in range(len(nums) -1, -1, -1):
          output[i] *= postf
          postf *= nums[i]
     
     return output
     




def main():
    print("Test1: nums = [-1,1,0,-3,3]")
    res = productExceptSelf2([-1,1,0,-3,3])
    print("Result", res)

if __name__ == "__main__":
    main()