from generator import generate
import json

year = int(raw_input('Enter first two digit of Roll No. : '))
# assert (year >= 14 and year <= 17), 'Entered Year is not correct'

branch = str(raw_input('Enter branch abbreviation : ')).upper()
branches = ['CE', 'CS', 'ME', 'MM', 'EE', 'EC']
assert branch in branches, 'Entered branch abbreviation not correct'

degree = int(raw_input('Enter 1 for single degree and 2 for dual degree : '))
assert degree in [1, 2], 'Entered degree not correct'

lastroll = int(raw_input('Enter last possible Roll No. : '))
# assert lastroll <= 46 and lastroll >= 9, 'lastroll should be less than 46'
firstroll = int(raw_input('Enter first Roll No. : '))

depc = []
for i in range(firstroll, lastroll):
	if i in depc:
		continue
	if (i < 10) :
		roll = str(year) + str(branch) + '0' + str(degree) + '00' + str(i)
	else :
		roll = str(year) + str(branch) + '0' + str(degree) + '0' + str(i)

	with open("stres.json") as f:
		prev = json.load(f)
		if roll in prev:
			continue
	scheme = 0
	choice = [[2000 - 18, 2000 - 17, 2000 - 19, 2000 - 16, 2000 - 20], [2000 - 18, 2000 - 19, 2000 - 17, 2000 - 16, 2000 - 20], [2000 - 17, 2000 - 18, 2000 - 19, 2000 - 16, 2000 - 20], [2000 - 19, 2000 - 18, 2000 - 17, 2000 - 16, 2000 - 20]]
	if generate(roll, year + choice[scheme][0]) == False:
		if generate(roll, year + choice[scheme][1]) == False:
			if generate(roll, year + choice[scheme][2]) == False:
				# if generate(roll, year + choice[scheme][3]) == False:
				# 	if generate(roll, year + choice[scheme][4]) == False:
				print ("I fail for", roll)

	