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
				#print("New Rec num:" + str(recNum))
				return recNum
		return -1
	
	# only to be used inside this class
	# makes creating records easier and more clear
	def makeRecord(self, data):
		return Record(self.recordSize, self.fieldSize, data)
		
	# return pointer value
	def getPointer(self):
		return int.from_bytes(self.data[(-1*self.pointerSize):], byteorder='big')
	
	def isEmpty(self):
		for recNum in range(0, self.bfr):
			aRecord = self.makeRecord(self.data[recNum*self.recordSize:(recNum+1)*self.recordSize])
			if not aRecord.isEmpty():
				return False
		return True
	
	# returns an array of record objects
	def getAllRecords(self):
		records = []
		for recNum in range(0, self.bfr):
			aRecord = self.makeRecord(self.data[recNum*self.recordSize:(recNum+1)*self.recordSize])
			if not aRecord.isEmpty():
				records.append(aRecord)
		return records
	
	def getRecordWithValue(self, value):
		records = self.getAllRecords()
		for record in records:
			if record.getHashValue() == value:
				return record
	
	def getRecordWithValueLoc(self, value):
		records = self.getAllRecords()
		i = 0
		for record in records:
			if record.getHashValue() == value:
				return i
			else:
				i += 1
	
	def containsRecordWithValue(self, value):
		records = self.getAllRecords()
		for record in records:
			if record.getHashValue() == value:
				return True
		return False