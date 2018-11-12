#!/usr/bin/env python3
f=open("d:/Python/NE/file1.txt")
output = f.read()
print("Type f.read() : ", type(output))
print("Isi File : ")
print(output)
output = f.read()
print("Isi File : ")
print(output)
#second f.read() will be blank as it has reach the end of file
f.seek(0)
output = f.read()
print("Isi File : ")
print(output)
f.close()
print("-"*80)
#f.readline() baca per baris
f=open("d:/Python/NE/file1.txt")
output = f.readline()
print("Type f.readline() : ", type(output))
print("Isi Line 1 : ")
print(output)
output = f.readline()
print("Isi Line 2 : ")
print(output)
output = f.readline()
print("Isi Line 2 : ")
print(output)
f.close()
print("-"*80)
#f.readlines() baca semua dan simpan ke list dan pertahankan \n 
f=open("d:/Python/NE/file1.txt")
output = f.readlines()
print("Type f.readlines() : ", type(output))
print("Isi File  : ")
print(output)
f.close()
print("-"*80)
#output=f.read() dan output.splitlines() format \n tidak dipertahankan
f=open("d:/Python/NE/file1.txt")
output = f.read()
output = output.splitlines()
print("Type Splitlines : ", type(output))
print("Isi File  : ")
print(output)
f.close()
print("-"*80)
#handle will automatically close
with open("d:/Python/NE/file1.txt") as f:
    output = f.read()
    print("Isi File : ")
    print(output)

with open("d:/Python/NE/file2.txt",mode="w") as f:
    f.write("Write Line1\n")
#if use normal file open, need to use f.flush()

#append mode
with open("d:/Python/NE/file2.txt",mode="a") as f:
    f.write("Write Line2 - Appended")




