# shuffle the dataset into equal number of males and females
from random import shuffle
import re

f= open("nam_dict.txt")

lines=f.readlines()
count=0
males=[]
females=[]

fw=open("dataset.txt","w")
ft=open("test.txt","w")

for line in lines:
    count=count+1
    if count<363:
        continue
    words=line.split()
    if len(words)>1:
        if words[0]!="M" and words[0]!="F":
            continue
        valid = re.match('^[\w-]+$', words[1]) is not None
        if valid==False:
            continue
        if words[0]=="M":
            males.append(words[1])
        elif words[0]=="F":
            females.append(words[1])
shuffle(males)
shuffle(females)
min_size=min(len(males),len(females))
dataset_size=int(min_size*0.7)
#print "ddataset=",dataset_size
for word in males[0:dataset_size]:
    fw.write("%s %s\n"%("M",word))
for word in females[0:dataset_size]:
    fw.write("%s %s\n"%("F",word))
for word in males[dataset_size+1:len(males)-1]:
    ft.write("%s %s\n"%("M",word))
for word in females[dataset_size+1:len(females)-1]:
    ft.write("%s %s\n"%("F",word))
