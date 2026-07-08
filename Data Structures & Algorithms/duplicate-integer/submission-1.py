class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## O(nlogn) time 
        ## O(1) space

        # in place sorting 
        nums.sort() 

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False