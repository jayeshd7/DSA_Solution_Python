

class Data:
    def __init__(self, data):
        self.data = data

    def summary(self):
        print("Data Summary")


class DataFrame(Data):
    def __init__(self, data):
        super.__init__(data)

    def summary(self):
        print("DataFrame Summary")
        print(self.data.describe())

df = DataFrame
df.summary(df)