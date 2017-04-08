from Record import *

class Block: 
	
	def __init__(self, size, pointerSize, recordSize, fieldSize, bfr, data):
		self.size = size
		self.pointerSize = pointerSize
		# size of entire record (including hashing field)
		self.recordSize = recordSize
		self.fieldSize = fieldSize
		self.bfr = bfr
		self.data = data
	
	def hasSpace(self):
		for recNum in range(0, self.bfr):
			aRecord = self.makeRecord(self.data[recNum*self.recordSize:recNum+1*self.recordSize])
			if aRecord.isEmpty():
				return recNum
		return -1
	
	def makeRecord(self, data):
		return Record(self.recordSize, self.fieldSize, data)