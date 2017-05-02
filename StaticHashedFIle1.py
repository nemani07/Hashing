from Record import *
from Block import *
import math

class StaticlyHashedFile:

	def __init__(self,blockSize, recordSize, fileLoc):
	         self.m=1
			 	self.m = m
    self.slots = [None] * self.m
			 
		  self.file=fileLoc		 
		self.blockSize= blockSize
		self.fieldSize=fieldSize
		self.recordSize=recordSize
		self.blockPointerSize= 4
		self.bfr= math.floor((blockSize-self.blockPointerSize)/self.recordSize)
		 with open(self.file, 'wb') as f:
			f.write(b"This is a shorter less ridiculous file header")
			f.seek(self.blockSize*2)
			f.write(bytearray(self.blockSize))
		
	#hash function:
	 def hash_function(self, value):
    i = value % self.m
    return i
	
	#hash insert:
	#insert method
	def insert(self, value,record):
	#pass value to the hash function
    slot = self.hash_function(value)
    orig = slot
	#original logic
    while True:
        if self.slots[slot] is None:
            self.slots[slot] = value
            return slot
        if self.slots[slot] =  value:
            return -2
        slot = (slot + 1) % self.m
        if slot == orig:
            return -1
			#original logic ends
			
			#ray logic
			# open the file as binary read and write
		with open(self.file, 'r+b', buffering=self.blockSize) as f:
			# navigate to the appropriate bucket
			# plus 2 is to account for the header
			f.seek(self.blockSize*(slot+2))
			# check to see if data exists in this bucket
			theBlock = self.makeBlock(f.read(self.blockSize))
			space = theBlock.hasSpace()
			if space>=0:
			#INEEDTOASKABOUTTHIS
				# spot was open, move pointer back
				f.seek(self.blockSize*(slot+2) + self.recordSize*space)
				else:
				# there has been a collision. handle it by searching on to the next available value.
				#navigate to the next available block
				f.seek((self.blockSize*space)+i) %self.m
				#I"M NOT SURE WHAT TO PUT IN THE PLACE OF M
			
				
				
			
				# original logic
				def search(self, value)
                hsh = self.hash_function(value)
                if self.slots[hsh] is None:
				print("Nothing")
                return -1
                for i in range(self.m):
                 mod = (hsh + i) % self.m
				 if self.slots[mod] == value:
                 return mod
                 return -1
				#original logic ends
				
				#Joy's logic:
				
				def search(self, value):
	#pass value to hash function
		slot = self.hash_function(value)
	#open the file as binary read and write 
	with open(self.file, 'rb', buffering=self.blockSize) as f:
		# navigate to the appropriate bucket
		# plus 2 is to account for the header
		f.seek(self.blockSize*(slot+2))
		# load bucket into memory
		theBlock = self.makeBlock(f.read(self.blockSize))	
		# currently only built to handle key values
		if theBlock.containsRecordWithValue(value):	
			theRecord = theBlock.getRecordWithValue(value)	
			print(theRecord.bytes)
			else
			#if not found, check the next hash value 
			for i in range(self.m):
			f.seek((self.blockSize*space)+i) %self.m
			print("something ")
			
			#ends
			
			#update
			def update(self, value, data):
         # pass value to hash function
		bucket = self.h1(value)
		# format the record to overwrite with
		formattedRecord = Record.new(self.recordSize, self.fieldSize, value, data)	
		# open the file as binary read and write
		with open(self.file, 'r+b', buffering=self.blockSize) as f:
		# navigate to the appropriate bucket
		# plus 2 is to account for the header
		f.seek(self.blockSize*(bucket+2))
		# load bucket into memory
		theBlock = self.makeBlock(f.read(self.blockSize))
		# currently only built to handle key values	
		recLoc = theBlock.getRecordWithValueLoc(value)
		# navigate to the record to be updated
		f.seek(self.blockSize*(bucket+2) + self.recordSize*recLoc)
		# write over the old record with new formatted one
		f.write(formattedRecord.bytes)
			
				 
				 
				
				
				
				
				
				