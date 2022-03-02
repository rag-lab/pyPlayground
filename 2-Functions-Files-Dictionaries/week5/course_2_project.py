#We have provided some synthetic (fake, semi-randomly generated) twitter data 
# in a csv file named project_twitter_data.csv which has the text of a tweet, 
# the number of retweets of that tweet, and the number of replies to that tweet. 
# We have also words that express positive sentiment and negative sentiment, 
# in the files positive_words.txt and negative_words.txt. 
# Your task is to build a sentiment classifier, which will detect how 
# positive or negative each tweet is. You will create a csv file, 
# which contains columns for the Number of Retweets, Number of Replies, 
# Positive Score (which is how many happy words are in the tweet), 
# Negative Score (which is how many angry words are in the tweet), 
# and the Net Score for each tweet. At the end, you upload the csv file 
# to Excel or Google Sheets, and produce a graph of the Net Score 
# vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, 
# a string which represents a word, and removes characters considered punctuation 
# from everywhere in the word. (Hint: remember the .replace() method for strings.)
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str1):
    for char in punctuation_chars:
        str1 = str1.replace(char,"")
    return str1


#Next, copy in your strip_punctuation function and define a function called get_pos
#  which takes one parameter, a string which represents one or more sentences, 
# and calculates how many words in the string are considered positive words. 
# Use the list, positive_words to determine what words will count as positive. 
# The function should return a positive integer - how many occurrences there are 
# of positive words in the text. Note that all of the words in positive_words are 
# lower cased, so you’ll need to convert all the words in the input string to lower
# case as well.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


#Next, copy in your strip_punctuation function and define a function called 
# get_neg which takes one parameter, a string which represents one or more 
# sentences, and calculates how many words in the string are considered 
# negative words. Use the list, negative_words to determine what words will 
# count as negative. The function should return a positive integer - how many 
# occurrences there are of negative words in the text. Note that all of the 
# words in negative_words are lower cased, so you’ll need to convert all the 
# words in the input string to lower case as well.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str1):
    for char in punctuation_chars:
        str1 = str1.replace(char,"")
    return str1

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    total=0
    sentence = strip_punctuation(sentence)
    sentence2 = sentence.lower().split()
    for word in negative_words:
        #print(word)
        if(word in sentence2):
            total+=1
    return total


#Finally, copy in your previous functions and write code that opens the 
# file project_twitter_data.csv which has the fake generated twitter data 
# (the text of a tweet, the number of retweets of that tweet, and the number 
# of replies to that tweet). Your task is to build a sentiment classifier, 
# which will detect how positive or negative each tweet is. Copy the code from 
# the code windows above, and put that in the top of this code window. 
# Now, you will write code to create a csv file called resulting_data.csv, 
# which contains the Number of Retweets, Number of Replies, 
# Positive Score (which is how many happy words are in the tweet), 
# Negative Score (which is how many angry words are in the tweet), 
# and the Net Score (how positive or negative the text is overall) for each tweet. 
# The file should have those headers in that order. Remember that there is another
# component to this project. You will upload the csv file to Excel or Google Sheets
# and produce a graph of the Net Score vs Number of Retweets. Check Coursera for 
# that portion of the assignment, if you’re accessing this textbook from Coursera.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str1):
    for char in punctuation_chars:
        str1 = str1.replace(char,"")
    return str1

def get_neg(sentence):
    total=0
    sentence = strip_punctuation(sentence)
    sentence2 = sentence.lower().split()
    for word in negative_words:
        if(word in sentence2):
            total+=1
    return total

def get_pos(sentence):
    total=0
    sentence = strip_punctuation(sentence)
    sentence2 = sentence.lower().split()
    for word in positive_words:
        if(word in sentence2):
            total+=1
    return total

templist=[]

lines=0
with open("project_twitter_data.csv") as file:
    for lin in file:
        if(lines>0): # get from line1, without the header
            tweet,retweet,reply=lin.split(",")
            reply = int(reply.replace("\n", ""))
            retweet = int(retweet)
            tot_positive=get_pos(tweet)
            tot_negative=get_neg(tweet)
            templist.append([int(retweet), int(reply), tot_positive, tot_negative, (tot_positive-tot_negative)])
        lines+=1

template = "\n{},{},{},{},{}"

with open("resulting_data.csv", "w") as f:
    f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    for item in templist:
        #print(item)
        f.write(template.format(item[0],item[1],item[2],item[3],item[4]))
    f.write("\n")
f.close()

