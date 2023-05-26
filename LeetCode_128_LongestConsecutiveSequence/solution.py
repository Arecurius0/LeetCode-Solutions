def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Idea: iterate over array and check if number n can prepended or postpended onto an existing list if not, create a new list.
        numsSet = set(nums)
        longest = 0
        for n in numsSet:
            added = False
            #print("n: ",n," sequences: ",sequences)
            if n-1 not in numsSet:
                length = 0
                while (n+length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest


def main():
    print("Test1: nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]")
    res = longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])
    print("Result", res)

if __name__ == "__main__":
    main()