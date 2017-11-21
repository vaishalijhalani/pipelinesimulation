class Decode:

   def fetchedinst(self,inst): #fetch instrctions form a file
      opcode, operands = inst.split(" ")

      if opcode == "lw" or opcode == "sw":
      	operand1, operand2 = operands.split(" ")

      else:
      	operand1, operand2, operand3 = operands.split(" ")

      
