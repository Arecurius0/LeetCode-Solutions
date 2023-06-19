from collections import defaultdict

def topKFrequent2(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Time Complexity: O(n)+O(n)+O(n log n)+O(k) = 
        #sort nums, grab highest integer of array. Create new array Counter where each index is the integer and count up
        counter = dict.fromkeys(nums, 0) # O(n)

        for n in nums:  # O(n)
            counter[n] += 1

        sort_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True) # O(n log n)
        result = []
        for i in sort_counter[0:k]: # O(k)
             result.append(i[0])
        return result

def main():
    print("Test1: nums = [1,1,1,2,2,3], k = 2")
    res = topKFrequent2([1,1,1,2,2,3], 2)
    print("Result", res)
    print("Test2: nums = [1], k = 1")
    res = topKFrequent2([1], 1)
    print("Result", res)

if __name__ == "__main__":
    main()
