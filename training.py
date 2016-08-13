from __future__ import  division
import re


f=open('dataset.txt')
count=0

males=0
females=0
total=0
male={}
female={}
total_occurrences={}
prob_male={}
prob_female={}
count_bigram={}

#train the dataset

for line in f.readlines():
    words=line.split()
    #train
    #the second word is our man/woman
    if len(words)==2:
        if words[0]!="M" and words[0]!="F":
        	continue
        valid = re.match('^[\w-]+$', words[1]) is not None
        if valid==False:
        	continue
        if words[0]=="M":
        	males=males+1
        if words[0]=="F":
        	females=females+1
       	total=total+1 
        a=words[1]
        a=a.lower()
        bigrams=[a[i:i+2] for i in range(len(a)-1)]
        for bigram in bigrams:
        	if len(bigram)!=2:
        		continue
        	if bigram not in count_bigram:
        		count_bigram[bigram]=1
        	else:
        		count_bigram[bigram]=count_bigram[bigram]+1
        	if words[0]=="M":

        		if bigram not in male:
       				male[bigram]=1
       			else:
       				male[bigram]=male[bigram]+1
       		else:
       			if bigram not in female:
       				female[bigram]=1
       			else:
       				female[bigram]=female[bigram]+1

       	for key,value in count_bigram.iteritems():
       		total_occurrences=count_bigram[key]
       		if total_occurrences==0:
       			prob_male[key]=0.5
       			prob_female[key]=0.5

       		if key in male:	
       			prob_male[key]=male[key]/total_occurrences
       		else:
       			prob_male[key]=0;
       		if key in female:
       			prob_female[key]=female[key]/total_occurrences
       		else:
       			prob_female[key]=0
       		#print key,prob_male
       		
#print to text file

f=open("result.txt","w")
f.write("%d %d\n"%(males,females))
for key in count_bigram:
	if key in prob_male and key in prob_female: #TODO NEED TO TAKE CARE OF CASES WHERE KEYS OCCUR ONLY IN ONE TYPE!!
		f.write("%s %f %f\n" %(key,prob_male[key],prob_female[key]))





