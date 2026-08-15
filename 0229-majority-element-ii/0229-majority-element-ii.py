class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count1 = 0
        count2 = 0
        candidate1 = 0
        candidate2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1-=1
                count2-=1

        result = []

        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate1 != candidate2 and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result
