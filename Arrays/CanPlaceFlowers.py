from typing import List


class CanPlaceFlowers:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        count = 0

        for i in range(0, m):
            if count < n:
                if flowerbed[i] == 0:
                    next = 0 if (i == (m - 1)) else flowerbed[i + 1]
                    prev = 0 if (i == 0) else flowerbed[i - 1]
                    if next == 0 and prev == 0:
                        flowerbed[i] = 1
                        count = count + 1

        return count == n


if __name__ == "__main__":
    cpf = CanPlaceFlowers
    print(cpf.canPlaceFlowers(cpf, flowerbed=[1, 0, 0, 0, 1], n=1))
