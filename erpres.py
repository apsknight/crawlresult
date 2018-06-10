import mechanize
from bs4 import BeautifulSoup
import json

def attempt(rollno, dob):
	url = 'http://14.139.195.241/Result/login.php'
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
		name = soup.find('h1', attrs={'class': 'section-heading-page-center'}).text[6:].strip()
		tables = soup.find_all('table')
		# grade = [rollno, name]
		re = {}
		re["dob"] = dob
		re["sgpa"] = []
		re["cgpa"] = []
		re["name"] = name
		re["grades"] = {"1" : {}, "2" : {}, "3" : {}, "4" : {}, "5" : {}, "6" : {}, "7" : {}, "8" : {}}
		for table in tables:
			tr = table.find_all('tr')
			gpa = tr[-1].find_all('td')
			re["sgpa"].append(gpa[0].text.strip()[5:])
			re["cgpa"].append(gpa[1].text.strip()[5:])
			# print re
			sem = tr[0].find("td").text.strip()[-1]
			# print sem
			tr = tr[2:-1]
			for row in tr:
				# print(row)			
				td = row.find_all('td')
				# for gp in td:
				# 	print gp.text.strip()
				# print(td)
				subcode = td[0].text.strip()
				subname = td[1].text.strip()
				ltp = td[2].text.strip()
				credit = td[3].text.strip()
				re["grades"][sem][td[0].text.strip()] = td[4].text.strip()
				with open("course.json") as c:
					crs = json.load(c)
				if subcode not in crs:
					crs[subcode] = {"subnane": subname, "ltp": ltp, "credit": credit}

				with open("course.json", "w") as c:
					json.dump(crs, c)
		# print re
			# gp_tuple = []
			# for gp in td:
			# 	gp_tuple.append(gp.text.strip())
			# grade.append(gp_tuple[0][5:])
			# grade.append(gp_tuple[1][5:])

		with open("stres.json") as f:
			prev = json.load(f)
			
		prev[rollno] = re
		with open('stres.json', 'w') as f:
			json.dump(prev, f)
		return True



