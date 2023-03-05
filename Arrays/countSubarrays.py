from typing import List


class countSubarrays:
    def solution(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        minIdx, maxIdx, start = -1, -1, 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i + 1
                minIdx = -1
                maxIdx = -1
            if nums[i] == minK:
                minIdx = i
            if nums[i] == maxK:
                maxIdx = i

            count += max(0, min(minIdx, maxIdx) - start + 1)

        return count


if __name__ == "__main__":
    cs = countSubarrays
    print(cs.solution(cs, nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
