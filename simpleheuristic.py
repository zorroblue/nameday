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
neutrals=0
total=0
for line in f.readlines():
    count=count+1
    if count<363:
        continue
    words=line.split()
    #the second word is our man/woman
    if len(words)>1:
        total=total+1
        a=words[1]
        if a.endswith('a') or a.endswith('i'):
            #classify as female
            if words[0]=="F":
                positives=positives+1
            elif "?" in words[0]:
                neutrals=neutrals+1
            else:
                negatives=negatives+1
        else:
            #classify as male
            if words[0]=="M":
                positives=positives+1
            elif "?" in words[0]:
                neutrals=neutrals+1
            else:
                negatives=negatives+1

print "No of samples "+str(total)
print "Positives "+ str(positives)
print "Negatives "+ str(negatives)
print "Neutrals "+str(neutrals)

print "Accuracy= "+str(float(positives)/total)
