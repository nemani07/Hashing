from Record import *
from Block import *
import math

class LinearlyHashedFile:
	
	def __init__(self, blockSize, recordSize, fieldSize, fileLoc):
		self.m = 1
		self.n = 0
		self.file = fileLoc
		self.overflow = fileLoc + "_overflow"
		self.blockSize = blockSize
		# record size supplied by user should include the hash field size
		# 1 is added for the deletion marker
		self.recordSize = recordSize + 1
		self.fieldSize = fieldSize
		self.blockPointerSize = 4
		self.bfr = math.floor((blockSize-self.blockPointerSize)/self.recordSize)
		# truncates the file
		with open(self.file, 'wb') as f:
			f.write(b"This is a shorter less ridicculous file header")
			f.seek(self.blockSize*3 - self.blockPointerSize)
			f.write((0).to_bytes(fieldSize, byteorder='big'))
		# create overflow file
		open(self.overflow, 'wb').close()
	
	def h1(self, value):
		return value % self.m
	
	def h2(self, value):
		return value % (2*self.m)
	
	def insert(self, value, record):
		# pass value to first hash function
		bucket = self.h1(value)
		# check to see if the secondary hash function needs to be used
		if bucket < self.n:
			bucket = self.h2(value)
		# format the record to be inserted
		formattedRecord = Record.new(self.recordSize, self.fieldSize, value, record)
		# open the file as binary read and write
		with open(self.file, 'r+b', buffering=self.blockSize) as f:
			# navigate to the appropriate bucket
			# plus 2 is to account for the header
			f.seek(self.blockSize*(bucket+2))
			# check to see if data exists in this bucket
			theBlock = self.makeBlock(f.read(self.blockSize))
			space = theBlock.hasSpace()
			if space>=0:
				# spot was open, move pointer back
				f.seek(self.blockSize*(bucket+2) + self.recordSize*space)
				# slot data in there boiii
				f.write(formattedRecord.bytes)
				
			else:
				# there has been a collision. handle it.
				print("need a split yoooooo")
				
				# here is where we need to put the data into an overflow bucket
				with open(self.overflow, 'r+b') as overflow:
					print(theBlock.getPointer())
					# need to ignore the 0 pointer because that'll be null pointer
					# but we don't want to waste the first block in overflow
					# so we could subtract one? or maybe use first block for info
					pointer = theBlock.getPointer() - 1
					# only if the pointer points to something, meaning that this block already has an overflow bucket assigned to it
					if pointer >= 0:
						# navigate to the block in overflow file
						overflow.seek(self.blockSize*pointer)
						# read the block
						overflowBlock = self.makeBlock(overflow.read(self.blockSize))
						# find a spot to put the record
						overflowSpace = overflowBlock.hasSpace()
						# if there's a spot
						if overflowSpace>=0:
							# put it in there! gotta move the pointer back cause we read the block
							overflow.seek(self.blockSize*pointer + self.recordSize*overflowSpace)
							overflow.write(formattedRecord.bytes)
						else:
							print("we're having an overflow... in the overflow. OVERFLOWCEPTION")
						
					# else the bucket doesn't already have an overflow bucket assigned to it. so we must make one.
					else:
						# but where do we make it?
						# linear search through the overflow file? is that gross
						i = 0
						bucketFound = False
						while bucketFound == False:
							overflow.seek(i*self.blockSize)
							aBlock = makeBlock(overflow.read(self.blockSize))
							if aBlock.isEmpty():
								bucketFound = True
							else:
								i += 1
						overflow.seek(self.blockSize*i)
						overflow.write(formattedRecord.bytes)
					
				
				# navigate to the bucket to be split
				f.seek(self.blockSize*(self.n+2))
				# load bucket to memory
				bucketToBeSplit = makeBlock(f.read(self.blockSize))
				# clear out bucket
				f.seek(self.blockSize*(self.n+2))
				f.write(bytearray(self.blockSize))
				BTBSpointer = bucketToBeSplit.getPointer() - 1
				# see if it is pointing to anything
				if BTBSpointer >= 0:
					# this method will only handle one overflow bucket per bucket in the original file
					# eventually I should probably use some sort of list of overflow buckets.
					with open(self.overflow, 'r+b') as overflow:
						# navigate to bucket of interest
						overflow.seek(self.blockSize*BTBSpointer)
						# read bucket into memory
						ofBucketToBeSplit = makeBlock(overflow.read(self.blockSize))
						# clear the heck out of that bucket
						overflow.seek(self.blockSize*BTBSpointer)
						overflow.write(bytearray(self.blockSize))
				allRecords = bucketToBeSplit.getAllRecords().append(ofBucketToBeSplit.getAllRecords())
				# loop through all records
				oldBucketCount = 0
				newBucketCount = 0
				for record in allRecords:
					whichBucket = self.h2(record.getHashValue())
					f.seek(self.blockSize*(newBucket+2))
				
				
	def makeBlock(self, data):
		return Block(self.blockSize, self.blockPointerSize, self.recordSize, self.fieldSize, self.bfr, data)
	
	def rehashRecord(self):
		