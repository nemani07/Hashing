from Record import *
from Block import *
import math

class StaticlyHashedFile:

	def __init__(self,blockSize, recordSize, fileLoc):
	        self.file=fileLoc		 
		self.blockSize= blockSize
		self.fieldSize=fieldSize
		self.recordSize=recordSize
		self.numOfblocks=256
	#if there is any space in the block when colission occurs
	        numOfBlocksare=[]
		#self.blockPointerSize= 4
		self.bfr= math.floor((self.blockSize)/self.recordSize)
		 with open(self.file, 'wb') as f:
			f.write(b"This is a shorter less ridiculous file header")
			f.seek(self.blockSize*2)
			f.write(bytearray(self.blockSize))
		
	#hash function:
	 def hash_function(self, value):
    i = value % self.numOfblocks
    return i
	
	#hash insert:
	#insert method
	def insert(self, value,record):
	#pass value to the hash function
    slot = self.hash_function(value)
    orig = slot
	#original logic
    while True:
        if self.numOfBlocksare[slot] is None:
            self.numOfBlocksare[slot] = 1
            return slot
			else:
			 if (self.numOfBlocksare[slot] +1) > self.bfr:
	 			slot = (slot + 1) % self.numOfblocks
				if slot == orig:
					return -1
			else:
				self.numOfBlocksare[slot] = self.numOfBlocksare[slot] + 1
				return slot

			#which block it should get into
	
	
	
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
			
				 
				 
				
				
				
				
				
				