# leetcode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myMap = {}
        for i in range(len(nums)):
            currNum = num[i]
            need = target - currNum
            if need in myMap.keys():
                return [myMap[need], i]
            else:
                myMap[currNum] = i

        return