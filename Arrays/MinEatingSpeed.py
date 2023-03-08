from typing import List


def canFinish(piles, h, mid):
    time = 0
    for pile in piles:
        time += (pile+mid-1) // mid
    return time <= h


class MinEatingSpeed:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if canFinish(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    mes = MinEatingSpeed
    print(mes.minEatingSpeed(mes, piles=[3, 6, 7, 11], h=8))
