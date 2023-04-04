import collections
from typing import List


def deleteAndEarn(nums: List[int])-> int:
    nums.sort()
    count = collections.Counter(nums)

    dp = [0 for i in range(max(nums)+1)]

    if 1 in count:
        dp[1] = count[1]

    for i in range(2, len(dp)):
        p = 0
        if i in count:
            p = count[i] * i
        dp[i] = max(dp[i-1], dp[i-2]+p)
    return dp[-1]





print(deleteAndEarn([3,4,2]))
