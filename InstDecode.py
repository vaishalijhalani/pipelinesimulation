class Decode:

   def __init__(self,fetched): #fetch instrctions form a file

   	  self.fetched = fetched
   	  inst = self.fetched.next()
   	  inst = inst[:-1]
   	  list = inst.split(" ")
   	  dict = {'opcode':list[0], 'operand1':list[1], 'operand2':list[2]}
   	  if len(list) == 4:
   	  	dict['operand3'] = list[3]
   	  print dict