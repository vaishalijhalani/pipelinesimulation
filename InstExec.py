class Execute:

    def __init__(self, decoded, counter):
        self.input = decoded
        self.output = []
        self.counter = counter

    def next(self):
        length = len(self.input)
        if length > 1:
            if 1 <= self.input[length - 1]['opcode'] <= 4:
                if 1 <= self.input[length - 2]['opcode'] <= 4:
                    if self.input[length - 2]['DestReg'] in self.input[length - 1]['SourceReg']:
                    	print self.counter,'in exec'
                        self.counter += 3
