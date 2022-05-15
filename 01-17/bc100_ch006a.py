inFile = open("wordlist.txt", "r")
wordlist =[] 
line = inFile.read()
wordlist = line.split()
print (" ", len(wordlist), "words loaded.")
print(wordlist[3])


