from StaticlyHashedFile import *
file=StaticlyHashedFile(256,100,'C:/LN/test1')

file.formatValue("a string")

file.insert("test", "test val")
file.search("test")












# lst = [12,34,200,255,203]

# strfile = 'C://RF/test.txt'
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
