import datetime
from erpres import attempt

def generate(roll, year, times):
	date = datetime.date(year,01,01)
	while(attempt(roll, str(date)) != True or times == 0):
		print 'attempting for', roll, 'with', str(date)
		date += datetime.timedelta(days=1)
		times = times - 1