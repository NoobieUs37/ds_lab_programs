file1 = open(r"test/original.txt", "r")
file2 = open(r"test/duplicate.txt", "r")
duplicateStr = file1.read()
originalStr = file2.read()
file1.close()
file2.close()
file1 = open(r"test/original.txt", "w")
file2 = open(r"test/duplicate.txt", "w")
file1.write(originalStr)
file2.write(duplicateStr)
file1.close()
file2.close()
print("Operation completed")
