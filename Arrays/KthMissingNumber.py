from typing import List


class KthMissingNumber:
    def solution(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] - mid < k:
                left = mid + 1
            else:
                right = mid
        return left + k


if __name__ == "__main__":
    kmn = KthMissingNumber
    print(kmn.solution(kmn, arr=[2, 3, 4, 7, 11], k=5))
