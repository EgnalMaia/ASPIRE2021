'''How many passwords are valid according to their policies?'''
'''Maia Egnal'''
# example input: a file with many lines like this: '4-5 m: my name is maia'
# example output: 0 (there is no m in the fourth or fifth place
password = []
f = open("inputdata_day2.txt")
for item in f.readlines():
    password.append(item)
f.close()
count = 0
for item in password:
    l1 = item.split( )#I want it to split the string after every space, so I would have three seperate things 
    l2 = l1[0] #setting aside the testing range so it can be altered independently
    l2_splat = l2.split("-") #splitting it by hyphen to separate the numbers
    beginRange = int(l2_splat[0]) #begin range is the first number in l2_splat
    endRange = int(l2_splat[1])
    firstCheck = l1[2][beginRange] #firstCheck is the letter that is at the place mark beginRange
    if firstCheck == l1[1][0]: #if firstCheck is the letter we are checking for, it is valid
        count = count + 1
    else:
        continue #the password can still be valid, even if the first test is wrong
    secondCheck = l1[2][endRange]
    if secondCheck == l1[1][0]: #if secondCheck is the letter we are checking for, it is valid, if not invalid
        count = count + 1
print(count)
    
    




