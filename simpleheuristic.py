#APPROACH 1

#######################################################

# CLASSIFY NAMES ENDING WITH 'A' OR 'I' AS FEMALE

# No of samples 48528
# Positives 27509
# Negatives 11079
# Accuracy= 0.566868611935


#######################################################

#parse the text files and get the names ending with a vowel

f=open('nam_dict.txt')
count=0

positives=0
negatives=0
pos_males=0
neg_males=0 # The name was actually male, but is reported as female
pos_females=0
neg_females=0 # The name was actually female, but is reported as male

neutrals=0
total=0

males=0
females=0
for line in f.readlines():
    count=count+1
    if count<363:
        continue
    words=line.split()
    #the second word is our man/woman
    if len(words)>1:
        total=total+1
        a=words[1]
        if words[0]=="F":
        	females=females+1
        else if words[0]=="M":
        	males=males+1
        if a.endswith('a') or a.endswith('i'):
            #classify as female
            if words[0]=="F":
                positives=positives+1
                pos_females=pos_females+1
            elif "?" in words[0]:
                neutrals=neutrals+1
            else:
                negatives=negatives+1
                neg_males=neg_males+1
        else:
            #classify as male
            if words[0]=="M":
                positives=positives+1
                pos_males=pos_males+1
            elif "?" in words[0]:
                neutrals=neutrals+1
            else:
                negatives=negatives+1
                neg_females=neg_females+1

print "No of samples "+str(total)
print "Positives "+ str(positives)
print "Negatives "+ str(negatives)
print "Neutrals "+str(neutrals)

print "Positive males "+str(pos_males)
print "Males reported as females"+str(neg_males)
print "Positive females"+str(neg_females)
print "Females reported as males"+str(pos_females)

print "Accuracy= "+str(float(positives)/total)
