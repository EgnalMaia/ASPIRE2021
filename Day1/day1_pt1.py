'''Maia Egnal'''
''' Find the two entries that sum to 2020; what do you get if you multiply them together?'''

# Place all your variables at the top of your code

numbers = [] #emptylist
numbers2 = []
numbers3 = []
sum = 0


# open the file in the same folder this program is in that is called ‘input.txt’
f = open("inputdata_day1.txt") #F becomes a "file handle" which can be manipulated

for item in f.readlines(): #f."function"- means to do that function to the file that is defined above
    numbers.append(int(item)) # create a list called ‘numbers’ and "copy and paste" every item in the file into this empty list.
#int is saying make the item into an intefer so it is a full number not a string of characters
numbers2 = numbers.copy() # duplicate the list so I have two identical ones
numbers3 = numbers.copy()

f.close() # close the file that you just read, you don’t need it anymore

# the next two lines are 'loops'. Each time the first loop executes, it 
# goes through the entire second loop before it increments again. So entry 1
# in 'numbers' will get compared to EVERY value in 'numbers2' before entry 2 
# in 'numbers' gets compared to EVERY entry in 'numbers2' and so on.
# 
#  The variables called 'value' and 'value2' only exist until the loops end, 
# and are updated every time the loop executes. You can call them anything you want. 

for value in numbers: # for each value that is in the list called ‘numbers’
    for value2 in numbers2:
        for value3 in numbers3:# for every value2 in the second list, add it to that one value in the first list and see what you get
            sum = value + value2 + value3
            if sum == 2020:
            # ADD YOUR CODE HERE
            #Multiply value and value 2 to get final input value, then print that
                finalValue = value*value2*value3
                print(finalValue)
            else:
                continue