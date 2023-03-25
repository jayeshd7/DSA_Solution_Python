from typing import List


class DataSet:
    def __init__(self, data: List[int]):
        self.data = data

    def mean(self) -> float:
        return sum(self.data) / len(self.data)


data = [1, 2, 3]
dataset = DataSet(data)

print(f"Mean: {dataset.mean()}")
