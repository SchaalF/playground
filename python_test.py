import os

#function to count the number of lines in a file
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
os.system("clear")
print("Number of lines in the file: ",file_lengthy("test.txt"))



