class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort the list from 1--> end of the list
        nums.sort()

        for i in range(1, len(nums)):
            curr = nums[i] # current value in the list
            prev = nums[ i - 1] # prev value in the list

            if curr == prev:
                return True
        return False  


        #Time Complexity
     #1 Sorting the array == O (n log n) time to sort an array
     #2 Iterating through the array and compare the prev nums takes O(n)
     # so the entire function is O(n log n)

        