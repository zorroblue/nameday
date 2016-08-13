***Get the gender of a person from his name!***

These were some of the approaches taken by others in this problem.

1.)While a thread on StackOverflow says it is not programmatically possible to find it with reasonable accuracy, many have tried using features like the last letter of the name. With the last letter of the name as a vowel, there is more probability for names ending with 'a' or 'i' to be a female. It had a poor accuracy of around 57% as expected :P
You can find it in simple_heuristic.py

2.) I used a bi-gram approach with Naive Bayes classifiers to classift the dataset. I am getting around 68-69% accuracy almost consistently with shuffling my dataset. You can run it by 

`. run.sh` 


