class Writeback:

    def __init__(self, Input):
        self.input = Input

    def next(self, counter):
        if len(self.input) != 0:
            inst = self.input.pop()
            inst['cycle'] = counter + 1
            return inst
        else:
            return None
