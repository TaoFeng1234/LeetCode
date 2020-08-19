#If the Array is sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sort the array
        nums.sort()
        i = 0
        j = len(nums)-1
        while i<j :
            if nums[i] + nums[j] == target:
                return i,j
            else:
                if nums[i]+nums[j] < target:
                    i +=1
                else: 
                    j-=1
        return i,j

# If the array is unsorted. Solution provided by leetcode user/HankLiu5

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n],i]
