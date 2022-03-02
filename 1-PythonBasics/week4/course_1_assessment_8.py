#Could aliasing cause potential confusion in this problem?
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

->A. yes
B. no

#Could aliasing cause potential confusion in this problem?
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

A. yes
->B. no

#Which of these is a correct reference diagram following the execution 
# of the following code?
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

A. I.
B. II.
->C. Neither is the correct reference diagram.



#Which of these is a correct reference diagram following the execution 
# of the following code?
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']

A. I.
B. II.
C. III.
->D. IV.

#Which of these is a correct reference diagram following the execution 
# of the following code?

sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)

->A. I.
B. II.
C. III.
D. IV.