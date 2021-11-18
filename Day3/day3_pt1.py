"How many trees will be hit when following a -3/1 slope?"
"Maia Egnal"
map = []
f = open("inputDay3.txt")
for item in f.readlines():
    map.append(item)
f.close

count = 0
new line = 0
new position = 0
for string in map:
    mapForTest = "-" * 100 #repeat all of the strings in map 100 times within the same line
for item in mapForTest:
   itemCheck = item[new line][new position] #go one string down, count three more positions over than the last time
   if itemCheck = "#": #if itemCheck is a tree, then add one to the tree count
       count == count + 1
    else
        continue #if it is not a tree, leave it alone
   new line == new line + 1 #reset new line
   new position == new position + 3 #reset new position for next time


