"""
Inheritance
"""


class DataProcessor:
    def process_data(self) -> None:
        pass


class Plotter:
    def plot_data(self) -> None:
        pass


class DataPlotter(DataProcessor, Plotter):
    def plot_processed_data(self) -> None:
        self.process_data(self)
        self.plot_data(self)


dp = DataPlotter
print(dp.plot_processed_data(dp))
