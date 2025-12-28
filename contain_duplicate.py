nums = [1,2,3,4,5,6,6]

class Solution:
    def solu1(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
    
    def solu2(self, nums: list[int]) -> bool:
        count = 0
        for i in nums:
            count = nums.count(i)
            if count > 1:
                return True
        
        return False
    
solve = Solution()
    
print(solve.solu1(nums))

print(solve.solu2(nums))