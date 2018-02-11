from generator import generate

year = int(raw_input('Enter first two digit of Roll No. : '))
assert (year >= 14 and year <= 17), 'Entered Year is not correct'

branch = str(raw_input('Enter branch abbreviation : ')).upper()
branches = ['CE', 'CS', 'ME', 'MM', 'EE', 'EC']
assert branch in branches, 'Entered branch abbreviation not correct'

degree = int(raw_input('Enter 1 for single degree and 2 for dual degree : '))
assert degree in [1, 2], 'Entered degree not correct'

lastroll = int(raw_input('Enter last possible Roll No. : '))
assert lastroll <= 46 and lastroll >= 9, 'lastroll should be less than 46'

for i in range(1, lastroll):
	if (i < 10) :
		roll = str(year) + str(branch) + '0' + str(degree) + '00' + str(i)
	else :
		roll = str(year) + str(branch) + '0' + str(degree) + '0' + str(i)
	generate(roll, year + 2000 - 19, 735)