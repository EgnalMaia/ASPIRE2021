rawQuestions = []
questionsForTesting = []
aQuestions = []
testLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
count = 0


#Prepping the data -- putting into a list and then organizing it so all of the answers are on one line
f = open("datainput_day6.txt")
for line in f.readlines():
    rawQuestions.append(line)
f.close()
#I took this from day4 -- it should combine everything that is not split by two enters into one string
for item in rawQuestions:
    if item is not "\n":
        temp = item.split()
        for thing in temp:
            aQuestions.append(thing)
    if item is "\n":
        questionsForTesting.append(aQuestions)
        aQuestions = [] 

for question in questionsForTesting:
    sortedQuestion = sorted(question)
    for i in range(question.length): #I think this is C programming notation so I need to convert
        currentLetter = sortedQuestion[i]
        previousLetter = sortedQuestion[i-1] #previous letter is given the sortedQuestion index before the one being tested
        if(previousLetter != sortedQuestion[i]): #if previousLetter doesnt equal that sortedQuestion index, count++
            count = count + 1
print(count)

