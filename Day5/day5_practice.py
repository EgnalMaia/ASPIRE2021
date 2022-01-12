
rowNumber = 0
columnNumber = 0
rawSeats = []
highest = 0

f = open("inputdata_day5.txt")
for line in f.readlines():
    rawSeats.append(line)
f.close()
    

def findRowRange(high, low, loopTest):
    radius = (((high - low)-1)/2)
    highEnd = high - radius
    lowEnd = low + radius
    if loopTest is "F":
        newHigh = lowEnd
        newLow = low
    if loopTest is "B":
        newLow = highEnd
        newHigh = high
    return newHigh, newLow;

def findColumnRange(high, low, loopTest):
    radius = (((high - low)-1)/2)
    highEnd = high - radius
    lowEnd = low + radius
    if loopTest is "L":
        newHigh = lowEnd
        newLow = low
    if loopTest is "R":
        newLow = highEnd
        newHigh = high
    return newHigh, newLow;

for line in rawSeats:
    test = line
    highRow,lowRow = 127, 0
    for item in test:
        highRow,lowRow = findRowRange(highRow, lowRow, item)
        if highRow == lowRow:
            break
    rowNumber = highRow

    highColumn,lowColumn = 7, 0
    for item in test:
        if not (item == "R" or item == "L"):
            continue
        highColumn,lowColumn = findColumnRange(highColumn, lowColumn, item)
        if highColumn == lowColumn:
            break
    columnNumber = highColumn

    seatID = (rowNumber*8)+columnNumber
    if seatID >= highest:
        highest = seatID

print(highest)
