import mechanize
from bs4 import BeautifulSoup
import csv

def attempt(rollno, dob):
	url = 'http://14.139.195.241/result/login.php'
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	response = browser.open(url)
	browser.select_form('frm')
	browser['regno'] = rollno
	browser['dob'] = dob
	response = browser.submit()
	# assert browser.title().strip() == 'IIT BHUBANEWSAR', 'Login was not succesful!'
	if browser.title().strip() != 'IIT BHUBANEWSAR':
		return False
	else :
		soup = BeautifulSoup(response.read(), 'html.parser')
		name = soup.find('h1', attrs={'class': 'section-heading-page-center'}).text[6:]
		tables = soup.find_all('table')
		grade = [rollno, name]

		for table in tables:
			tr = table.find_all('tr')[-1]
			td = tr.find_all('td')
			gp_tuple = []
			for gp in td:
				gp_tuple.append(gp.text.strip())
			grade.append(gp_tuple[0][5:])
			grade.append(gp_tuple[1][5:])

		with open('output.csv', 'a') as file:
			writer = csv.writer(file)
			writer.writerow(grade)
		print 'Succesfully crawled for', name
		return True



