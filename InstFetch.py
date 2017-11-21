class Fetch:

   def __init__(self,filename): #fetch instrctions form a file
      self.file = open(filename,"r")
      #self.object1 = object1

   def next(self):
      return self.file.readline() 

