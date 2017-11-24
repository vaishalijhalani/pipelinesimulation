class Execute:

    def __init__(self, Input):
        self.input = Input
        self.output = []

    def next(self, counter):
    	if len(self.output) == 0 and len(self.input)!=0:
    		self.output.append(self.input.pop())
        
                        