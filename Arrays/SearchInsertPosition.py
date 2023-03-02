from typing import List


class SearchInsertPosition:
    def solution(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0
        while start <= end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start


if __name__ == "__main__":
    si = SearchInsertPosition
    print(si.solution(si, [1, 3, 5, 6], 6))
