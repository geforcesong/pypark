import struct
filePath = './tmpfiles/data.bin'

F = open(filePath, 'wb')
# bytes = struct.pack('>i4sh', 7, b'spam', 8)

values = (1, b'good', b'hello', 1.22)
newb = struct.pack('i4s5sf', *values) # i4s5sf must match with values.
# Struct 字节对照表 https://blog.csdn.net/zhongbeida_xue/article/details/79026333 


# print(bytes)
print(newb)

# F.write(bytes)
F.write(newb)
F.close()

F = open(filePath, 'rb')
data = F.read()
values = struct.unpack('i4s5sf', data)
print(values)

