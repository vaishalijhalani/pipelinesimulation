class Fetch:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.output = []
        self.counter = 0

    def next(self):
        self.output.append(self.file.readline())

        self.counter += 1
        print self.counter,'in fetch'
        # print self.output
