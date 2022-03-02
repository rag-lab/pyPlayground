#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num.
filename="travel_plans.txt"
fileref = open(filename, "r")
str1 = fileref.read()
print(str1)
num = len(str1)

#We have provided a file called emotion_words.txt that contains lines of words 
# that describe emotions. Find the total number of words in the file and assign 
# this value to the variable num_words.
filename="emotion_words.txt"
fileref = open(filename, "r")
num_words=0
for line in fileref.readlines():
    num_words+=len(line.split())

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
filename="school_prompt.txt"
num_lines=0
with open(filename, "r") as fileref:
    for line in fileref:
        num_lines+=1

#Assign the first 30 characters of school_prompt.txt as a string to the variable 
# beginning_chars.
filename="school_prompt.txt"
with open(filename, "r") as fileref:
    str1 = fileref.read()
    beginning_chars=str1[:30]

#Challenge: Using the file school_prompt.txt, ~
# assign the third word of every line to a list called three.
filename="school_prompt.txt"
three=[]
listline=[]
with open(filename, "r") as fileref:
    for line in fileref:
        listline = line.split()
        three.append(listline[2])

#Challenge: Create a list called emotions that contains 
# the first word of every line in emotion_words.txt.
filename="emotion_words.txt"
three=[]
emotions =[]
with open(filename, "r") as fileref:
    for line in fileref:
        listline = line.split()
        emotions.append(listline[0])

#Assign the first 33 characters from the textfile, travel_plans.txt 
# to the variable first_chars
filename="travel_plans.txt"
with open(filename, "r") as fileref:
    str1 = fileref.read()
    first_chars=str1[:33]

#Challenge: Using the file school_prompt.txt, 
# if the character ‘p’ is in a word, then add the word to a list called p_words.
filename="school_prompt.txt"
p_words=[]
listline=[]
with open(filename, "r") as fileref:
    for line in fileref:
        listline = line.split()
        for word in listline:  
            if("p" in word):
                p_words.append(word)

