class Fetch:

    def __init__(self, filename):
        self.inst_counter = 0
        self.file = open(filename, "r")
        self.output = []

    def next(self, counter):
        if len(self.output) == 0:
            inst = self.file.readline()
            if inst != '':
                self.output.append(inst)
                return inst
            else:
                return False
        else:
            return False
