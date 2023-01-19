# leetcode
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myMap = {}
        for i in range(len(nums)):
            currNum = nums[i]
            need = target - currNum
            if need in myMap.keys():
                return [myMap[need], i]
            else:
                myMap[currNum] = i

        return