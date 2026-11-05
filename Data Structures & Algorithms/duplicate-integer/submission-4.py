class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        answer = len(numsSet) < len(nums)
        return answer

        