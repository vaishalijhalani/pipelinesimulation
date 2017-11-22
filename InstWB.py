class Writeback:

    def __init__(self, counter):
        self.counter = counter

    def next(self):
    	print self.counter,'in wb'
        self.counter += 1
