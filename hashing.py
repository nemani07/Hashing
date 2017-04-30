from LinearlyHashedFile import *

file = LinearlyHashedFile(256, 100, 10, 'C:/RF/test1')


for i in range(50, 90):
	print("n: " + str(file.n) + "   m: " + str(file.m))
	file.insert(i, str(i) + "th record")


for i in range(60, 70):
	file.search(i)
	
file.search(88)


# lst = [12,34,200,255]

# strfile = 'C:/RF/test.txt'
# buffer = bytes(lst)

# print(buffer)

# with open(strfile,'bw') as f:
    # f.write(buffer)

# print('File written, reading it back')

# with open(strfile,'br') as f:
    # buffer = f.read(16)
    # print("Length of buffer is %d" % len(buffer))

    # for i in buffer:
        # print(int(i))
