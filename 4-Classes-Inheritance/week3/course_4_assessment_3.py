
def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM


#The function mySum is supposed to return the sum of a list of numbers 
# (and 0 if that list is empty), but it has one or more errors in it. 
# Use this space to write test cases to determine what errors there are. 
# You will be using this information to answer the next set of multiple 
# choice questions.
import test
test.testEqual(mySum([1,2,3]),6)
test.testEqual(mySum([1]),1)
test.testEqual(mySum([]),0)


Which of the following cases fail for the mySum function?
->A. an empty list
B. a list with one item
->C. a list with more than one item

Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?
A. Yes
->B. No

