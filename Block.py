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
			aRecord = self.makeRecord(self.data[recNum*self.recordSize:(recNum+1)*self.recordSize])
			if aRecord.isEmpty():
				print("New Rec num:" + str(recNum))
				return recNum
		return -1
	
	def makeRecord(self, data):
		return Record(self.recordSize, self.fieldSize, data)
		
	def getPointer(self):
		# this is having an issue beacause we haven't actually written data to that part of the block yet... so it's just going out into memory and grabbing some random shit. pointer at the front of block instead? doable, but not as sexy. when writing a new block set all to null? possible. may need to just set pointer to null. the rest will fill in.
		return int.from_bytes(self.data[(-1*self.pointerSize):], byteorder='big')
	
	def isEmpty(self):
		for recNum in range(0, self.bfr):
			aRecord = self.makeRecord(self.data[recNum*self.recordSize:(recNum+1)*self.recordSize])
			if not aRecord.isEmpty():
				return False
		return True
		
	def getAllRecords(self):
		records = []
		for recNum in range(0, self.bfr):
			aRecord = self.makeRecord(self.data[recNum*self.recordSize:(recNum+1)*self.recordSize])
			if not aRecord.isEmpty():
				records.append(aRecord)
		return records