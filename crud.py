#CRUD Operations 

#READ file content 
file = open ("words.csv","r")
words=[]
for word in file:
    words.append(word.strip("\n"))
file.close()
print(words)

#Create new list of words and save file 
userInput - input ("Enter words seperated by comma: ").replace(" ","")
userList = userInput.split(",")
file = open ("words.csv","w")

for word in userList:
    file.write(word+'\n')
file.close()

#Update with new word 
userInput = open("words.csv","r")
words = []
for word in file:
    words.append(word.strip("\n"))
file.close()

i = 0 
while i <= len(words)-1:
    if words[i] == userList [0]:
        words[i] = userList[1]
    i += 1 
    
# Write to file
file = open ("words.csv","w")
for word in words:
    file.write(word+'\n')
file.close()

# Delete word
userInput - input ("Enter word to delete: ").replace(" ","")

# Read file content to list 
file = open ("words.csv","r")
words=[]
for word in file:
    words.append(word.strip("\n"))
file.close()

#Write to file 
file = open ("words.csv","w")
for word in words:
    if word != userInput:
        file.write(word+'\n')
file.close()