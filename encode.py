import pybase100

# 这里填入你的shellcode
shellcode = b''
# 输出密文
print(pybase100.encode(shellcode).decode())