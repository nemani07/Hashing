from Record import Record
from Block import Block
import math

class ExtendibleHashedFile:
    
    def __init__(self, blockSize, recordSize, fieldSize, fileLoc):
        #self.m = 1
        #self.n = 0
        self.globalDepth = 0
        self.directory = [0]
        self.file = fileLoc
        self.blockSize = blockSize
        # record size supplied by user should include the hash field size
        # 1 is added for the deletion marker
        self.recordSize = recordSize + 1
        self.fieldSize = fieldSize
        self.blockPointerSize = 4
        self.bfr = math.floor((blockSize-self.blockPointerSize)/self.recordSize)
        # truncates the file
        with open(self.file, 'wb') as f:
            f.write(b"""This is a file header
            here is some information
            this is only two blocks in size at maximum""")
        # create overflow file
        open(self.file + '_overflow', 'wb').close()
    
    #def h1(self, value):
    #    return value % self.m
 
    def h1(self, value):
        asInt = int(value)
        bitCount = asInt.bit_length()
        highBits = asInt >> (bitCount - self.globalDepth) 
        return self.directory[highBits]            
        
    def insert(self, value, record):
        # pass value to hash function
        bucket = self.h1(value)
        # encode the record to be inserted
        formattedRecord = Record.new(self.recordSize, self.fieldSize, value, record)
        print(formattedRecord)
        # open the file as binary read and write
        with open(self.file, 'r+b', buffering=self.blockSize) as f:
            # navigate to the appropriate bucket
            # plus 2 is to account for the header
            f.seek(self.blockSize*(bucket+2))
            # check to see if data exists in this bucket
            theBlock = self.makeBlock(f.read(self.blockSize))
            space = theBlock.hasSpace();
            if space>=0:
                # spot was open, move pointer back
                f.seek(self.blockSize*(bucket+2) + self.recordSize*space)
                # slot data in there boiii
                f.write(formattedRecord.bytes)
                
            else:
                # there has been a collision. handle it.
                print("need a split yoooooo")
                
                # here is where we need to put the data into an overflow bucket
                # idk how to do that though.
                # so just ignore it for now.....
                
                # navigate to the bucket to be split
                f.seek(self.blockSize*(self.n+2))
                
                
    def makeBlock(self, data):
        return Block(self.blockSize, self.blockPointerSize, self.recordSize, self.fieldSize, self.bfr, data)