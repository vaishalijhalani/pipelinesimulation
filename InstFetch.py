class Fetch:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.output = []


    def next(self):
        self.output.append(self.file.readline())

