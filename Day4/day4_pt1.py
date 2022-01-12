'''Maia Egnal'''
'''How many passports are valid?'''
'''The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)'''

temp = []
lines = []
count = 0
fields = []
passports = []
aPassport = []


f = open("inputDay4.txt")

for line in f.readlines():

    lines.append(line)
f.close()

for item in lines:
    if item is not "\n":
        temp = item.split()
        for thing in temp:
            aPassport.append(thing)
    if item is "\n":
        passports.append(aPassport) #passports should be a list of passports each of which is a list of data
        aPassport = []


for passport in passports:
    #for item in passport:
    item = "".join(passport)
    if 'byr' in item:
        if 'iyr' in item:
            if 'eyr' in item:
                if 'hgt' in item:
                    if 'hcl' in item:
                        if 'ecl' in item:
                            if 'pid' in item:
                                count = count + 1
print(count)
