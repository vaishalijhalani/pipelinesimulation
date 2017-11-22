class Memory:

    def __init__(self, counter):
        self.counter = counter

    def next(self):
    	print self.counter,'in mem'
        self.counter += 1
