class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            sq=num**2
            result.append(sq)
        
        return sorted(result)

        

        