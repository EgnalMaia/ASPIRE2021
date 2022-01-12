'''Maia Egnal -- Day 5 of Advent of Code'''
'''For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.
In this example, the seat has ID 44 * 8 + 5 = 357.'''

rawSeats = []
rowTest = 127
columnTest = 8
highest = 0
highEnd = 0
middle = 0
lowEnd = 0
row = 0
column = 0
seatID = 0


f=open("inputDay5.txt")
for line in f.readlines():
    rawSeats.append(line)
f.close()

for item in rawSeats:
    rowTest = 127
    middle = rowTest/2
    highEnd = range(middle, 127)
    lowEnd = range(0, middle)
    if item[0] = F:
        rowTest = lowEnd
        #I realized I have an error in every one of these which is I need to reset the ranges later on
        #somehow I need to get the highest number of my lowEnd to set as the top of the range.
    if item[0] = B:
        rowTest = highEnd
   #I will repeat this for all seven of the letters, but first I need to figure out what is above to make it work
    row = rowTest
    columnTest = 8
    middle = columnTest/2
    highEnd = range(middle, 8)
    lowEnd = range(0, middle)
    if item[7] = R
        columnTest = highEnd
    if item[7] = L
        columnTest = lowEnd
    #this test will be repeated for all three letters
    column = columnTest
    seatID = row*8 + column
    if seatID => highest:
        highest = seatID
    else
        continue
print(highest)