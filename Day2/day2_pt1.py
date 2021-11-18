'''How many passwords are valid according to their policies?'''
'''Maia Egnal'''
# example input: a file with many lines like this: '4-5 m: my name is maia'
# example output: 0 (because there are only 3 m chars in the string
password = []
f = open("inputdata_day2.txt")
for item in f.readlines():
    password.append(item)
f.close()
count = 0
for item in password:
    l1 = item.split( )#I want it to split the string after every space, so I would have three seperate things 
    l2 = l1[0]
    sum = item.count(l1[1][0])-1
    l2_splat = l2.split("-")
    beginRange = int(l2_splat[0])
    endRange = int(l2_splat[1])
    if sum <= endRange:
        if sum >= beginRange:
            count = count + 1
print(count)



