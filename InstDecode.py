class Decode:

    def __init__(self, fetched, counter):  # fetch instrctions form a file
        self.input = fetched
        self.output = []
        self.counter = counter

    def next(self):
        inst = self.input.pop()
        print self.counter,'in decode'
        inst = inst[:-1]
        aList = inst.split(" ")
        aDict = {'opcode': aList[0], 'DestReg': aList[
            1], 'SourceReg': aList[2:]}
        if aDict['opcode'] == 'add':
            aDict['opcode'] = 1
        if aDict['opcode'] == 'or':
            aDict['opcode'] = 2
        if aDict['opcode'] == 'sub':
            aDict['opcode'] = 3
        if aDict['opcode'] == 'and':
            aDict['opcode'] = 4
        self.output.append(aDict)
        
        self.counter += 1
        # print self.output
