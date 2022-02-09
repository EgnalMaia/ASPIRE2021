questionsForTesting = "azedybkmuwgotquqztdwasygmb"
testLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
count = 0



sortedQuestion = sorted(questionsForTesting)
print(sortedQuestion)#alphabetizes
#for (i = 0, i < 26, i++): #I think this is C programming notation so I need to convert
for i in range(26):
    previousLetter = sortedQuestion[i-1] #previous letter is given the sortedQuestion index before the one being tested
    if previousLetter != sortedQuestion[i]: #if previousLetter doesnt equal that sortedQuestion index, count++
        count = count + 1
print(count)