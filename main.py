(1024).to_bytes(2, byteorder='big')
(1024).to_bytes(10, byteorder='big')
(-1024).to_bytes(10, byteorder='big', signed=True)
x = 1000
x.to_bytes((x.bit_length() // 8) + 1, byteorder='little')
