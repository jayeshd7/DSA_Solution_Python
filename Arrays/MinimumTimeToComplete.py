from typing import List


class MinimumTimeToComplete:
    @staticmethod
    def feasible(mid, time):
        totalCount = 0
        for var in time:
            totalCount += mid // var
        return totalCount

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        maxBus = max(time)
        low = 1
        high = maxBus * totalTrips

        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            tripsDone = self.feasible(mid, time)

            if tripsDone >= totalTrips:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    mtc = MinimumTimeToComplete
    print(mtc.minimumTime(mtc, time=[1, 2, 3], totalTrips=5))
