from LinearlyHashedFile import *

file = LinearlyHashedFile(512, 100, 10, 'C:/RF/test1')
file2 = LinearlyHashedFile(256, 50, 10, 'C:/RF/test2')


file.insert(53, "this is a string in file 1")
file2.insert(10, "this is a string in file 2")


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
