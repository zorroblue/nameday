""" This is the one that tests on inputs"""
from __future__ import division

f=open("result.txt")

line_count=0
lines=f.readlines()
prob_male={}
prob_female={}
males=0
females=0
for line in lines:
    line_count=line_count+1
    words=line.split(" ")
    if line_count==1:
        males=int(words[0])
        females=int(words[1])
    if len(words)!=3:
        continue
    prob_male[words[0]]=float(words[1])
    prob_female[words[0]]=float(words[2])

f.close()
ft=open("test.txt")
lines=ft.readlines()

correct=0
incorrect=0
ambiguous=0

for line in lines:
    words=line.split()
    a=words[1]
    gender=words[0]
    a=a.lower()
    bigrams=[a[i:i+2] for i in range(len(a)-1)]

    chance_male=males/(males+females)
    chance_female=females/(males+females)

    for bigram in bigrams:
        key=bigram
        if key in prob_male and prob_female:
        #print bigram,prob_male[bigram],prob_female[bigram]
            chance_male=chance_male*prob_male[bigram]
            chance_female=chance_female*prob_female[bigram]

    predict="A"

    if chance_male==chance_female:
        predict="A"
    elif chance_male>chance_female:
        predict="M"
    else:
        predict="F"

    if predict=="A":
        ambiguous=ambiguous+1
        continue
    elif predict==gender:
        correct=correct+1
    else:
        incorrect=incorrect+1

print "Total samples: ",correct+incorrect+ambiguous
print "Ambiguous: ",ambiguous
print "Correct: ",correct
print "Incorrect: ",incorrect
print "Accuracy: ",correct/(correct+incorrect+ambiguous)

