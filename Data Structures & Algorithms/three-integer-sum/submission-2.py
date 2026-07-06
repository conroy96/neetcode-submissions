class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        result = []

        for i in range(len(new_nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if (new_nums[i] + new_nums[j] + new_nums[k] == 0):
                    trip = [new_nums[i], new_nums[j], new_nums[k]]
                    if trip not in result:

                        result.append(trip)
                    j += 1
                    k -= 1
                elif new_nums[i] + new_nums[j] + new_nums[k] > 0:
                    k -= 1
                elif new_nums[i] + new_nums[j] + new_nums[k] < 0:
                    j += 1
        return result
