# Write a program to read text file.
file1 = open("C:/Users/pashi/OneDrive/Documents/new 1.txt","r")
data = file1.read()
print(data)
print()

file2 = open("C:/Users/pashi/OneDrive/Documents/new 1.txt","w")
str1 = 'Python'
file2.write(str1)
print()

file3 = open("C:/Users/pashi/OneDrive/Documents/new 1.txt","r+")
print(file3.readline(11))
print()

