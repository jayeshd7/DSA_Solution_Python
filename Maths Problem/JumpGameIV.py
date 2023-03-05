from collections import deque, defaultdict
from typing import List


class JumpGameIV:
    def minJumps(self, arr: List[int]) -> int:
        visitedNum, visitedIdx = set(), set()
        queue = deque([0])
        maps = defaultdict(list)
        for i, num in enumerate(arr):
            maps[num].append(i)
        level = 0
        endIdx = len(arr) - 1

        while queue:
            lenQ = len(queue)
            for _ in range(lenQ):
                curr = queue.popleft()
                if curr == endIdx:
                    return level
                if curr - 1 >= 0 and curr - 1 not in visitedIdx:
                    queue.append(curr - 1)
                if curr + 1 <= endIdx and curr + 1 not in visitedIdx:
                    queue.append(curr + 1)
                visitedIdx.add(curr)
                val = arr[curr]
                if val not in visitedNum:
                    visitedNum.add(val)
                    for element in maps[val]:
                        if element not in visitedIdx:
                            queue.append(element)

            level += 1


if __name__ == "__main__":
    jg = JumpGameIV
    print(jg.minJumps(jg, [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
