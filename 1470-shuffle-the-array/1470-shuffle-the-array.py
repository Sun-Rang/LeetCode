class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x1 = nums[0:n]
        y1 = nums[n:]
        new_nums = []
        for i in range(n):
            new_nums.append(x1[i])
            new_nums.append(y1[i]) 
        return new_nums