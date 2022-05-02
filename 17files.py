import os
file = open("demofile.txt",'r')
print(file.read())
file.close()

file = open("demofile.txt",'r')
print(file.read(5))
file.close()

file = open("demofile.txt",'r')
print(file.readline())      #reads only first line
file.close()

file = open("demofile.txt",'r')
print(file.readlines())
file.close()


file = open("demofile.txt",'r')
for line in file:
    print(file.readlines())
file.close()

#writing in a file using append or write
# write overwrties over existing code

file2 = open("demofile2.txt",'w')
file2.write("hello world")
file2.write("writing into a new file")
file2.close();

#to create a new file use open method and a name of file that does not already exist
#os.remove() deletes a file that exist
#os.rmdir removes the whole folder