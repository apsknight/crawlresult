import datetime
from erpres import attempt

def generate(roll, year):
	date = datetime.date(year, 1, 1)
	times = 366
	while(times != 0):
		if (attempt(roll, str(date))):
			print("Done for", roll)
			return True
		if times % 30 == 0:
			print('attempting for', roll, 'with', str(date))
		date += datetime.timedelta(days=1)
		times = times - 1
	return False