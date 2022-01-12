row_list = []
tree_count = 0

previous_index_right = 0

index_right = 3

previous_index_down = 0

index_down = 1

 

f = open("inputDay3.txt")

for line in f.readlines():

    row_list.append(line)

f.close()

row_list = [line.replace('\n','') for line in row_list]

 

for line in row_list:

    try:

        if row_list[index_down][index_right] == '#':

            tree_count = tree_count + 1

            # print("Oh no a tree!")

        index_right = index_right + 3

        if index_right >= len(line):

            index_right = index_right - len(line)

        index_down = index_down + 1

    except IndexError:

        print("index_down was " + str(index_down) + " and index_right was " + str(index_right))

        break

print(tree_count)