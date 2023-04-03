"""

Polymorphism concept
"""
import json


class DataReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def read_data(self):
        pass


class CsvReader(DataReader):
    def read_csv(self):
        with open(self.fileName, "r") as f:
            data = [line.strip().split(",") for line in f]
        return data


class JsonReader(DataReader):
    def read_json(self):
        with open(self.fileName, "r") as f:
            data = json.load(f)
        return data


def process_data(reader):
    data = reader.read_data()

    print(f"data processed from {reader.fileName}")


csvReader = CsvReader("data.csv")
jsonReader = JsonReader("data.json")

process_data(csvReader)
process_data(jsonReader)
