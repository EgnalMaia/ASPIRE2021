counter = 0
dictBagContents = {}
f = open("day7_input.txt");
for line in f.readlines(): # read the file one line at a time
    tempContents = line.split("contain") # Make every line into a separate string, splitting on the word contains
    rawBagContent = tempContents[1].split(",") # Split the second element in that list by commas
    dictBagContents[tempContents[0]]= rawBagContent # Make it into a dictionary where the key is the first element in the line and the values are the list from splitting commas
    tempContents = []
    rawBagContent = []




# Search for if shiny gold bag is in the values
# For each type of bag, replace the bag with its contents
# For every bag that was in its contents, replace those with its contents, etc.
# Recurse until you hit an empty bag or until you find a shiny gold bag
# Add to a counter if it contains a shiny gold bag