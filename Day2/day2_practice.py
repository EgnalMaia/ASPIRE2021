s = '4-5 m: my name is maia' #creates string to test
l1 = s.split( ) #splits that string by spaces and converts it to a list
count = 0
sum = s.count(l1[1][0])-1 #count all the times that m appears in the string, store it as sum
beginRange = int(l1[0][0]) #must convert to int so it is not a character but instead a number
endRange = int(l1[0][2])
if sum <= endRange:
    if sum >= beginRange:
        count = count + 1
print(count)
#check if that number found is equal to the range of the above very first element, if for one value, for if you test a list


#print("number found =" + str(s.count(l1[1][0])-1))