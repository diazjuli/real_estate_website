# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myFile.txt', 'w')


#get info
print('Name: ', myFile.name)
print('Isclosed? : ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write("I love python")
myFile.write(" and javascript")
myFile.close()
print('Name: ', myFile.name)
print('Isclosed? : ', myFile.closed)
print('Opening mode: ', myFile.mode)

#append to file
myFile = open('myFile.txt', 'a')
myFile.write(" and now im appending java")

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)