# string-and-list
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not
#append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
file = open(fname)
lst = list()
for line in file:
    lm = line.split()    #creat one list first
    for word in lm:
        if word in lst:
            continue
        else:
            lst.append(word) #add the word which is not in the list lm to it.
lst.sort()
print(lst)
