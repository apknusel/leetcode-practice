### Optimized Solution ###

# This solution uses Python's "in" feature to run in O(N) time by checking to see if the second
# number is in the list before searching for it. This is more optimized because when using "in"
# the code runs in less then O(N) time allowing for the max time to be O(N) caused by the other loop.

### Solution ###

# Time Complexity: O(N)

class Solution:
    def twoSum(self, nums, target):
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []