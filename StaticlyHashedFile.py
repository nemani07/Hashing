from Record import *
from Block import *
import math

class StaticlyHashedFile:
	
	def __init__(self,blockSize, recordSize, fileLoc):
	          self.m=1
		  self.file=fileLoc
		  self.overflow =fileLoc + "_overflow"
		 
		self.blockSize= blockSize
		self.fieldSize=fieldSize
		self.recordSize=recordSize
		self.blockPointerSize= 4
		self.bfr= math.floor((blockSize-self.blockPointerSize)/self.recordSize)
		# truncates the file
		with open(self.file,'wb') as f:
		f.write(b"This is a test")
		f.seek(self.blockSize*3 - self.blockPointerSize)
	        f.write((0).to_bytes(fieldSize,byteorder='big'))
		#creates an overflow file
		open(self.overflow,'wb').close()
		
		#hash definition 
		def h(self,value)
		return value % self.m
		
	def insert(self, value, record):
	# pass value to hash function
	bucket= self.h(value)
	#open the file as binary read and write
	with open(self.file, 'r+b' , buffering=self.blockSize) as f:
	f.seek(self.blockSize*(bucket+2))
	#check if data exists in bucket
	theBlock=self.makeBlock(f.read(self.blockSize))
	space = theBlock.hasSpace()
	if space>=0
	f.seek(self.blockSize*(bucket+2)+ self.recordSize*space
        else:
       print("linking has to be done")	
       
	# put data into the bucket by linking
	with open(self.overflow, 'r+b') as overflow
	print(theBlock.getPointer())
        pointer=theBlock.getPointer())-1
	
	if pointer>=0:
	
	
			
	def makeBlock(self, data):
		return Block(self.blockSize, self.blockPointerSize, self.recordSize, self.fieldSize, self.bfr, data)
		