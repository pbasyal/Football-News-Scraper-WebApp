#Beatiful Soup - To parse the html
from bs4 import BeautifulSoup
#urllib.request - to make http request
import urllib.request
#To remove any language special characters
import unicodedata
# EMAIL library
import smtplib

#NOTES:
# - In this code instead of saving to data structures, I saved the info in a txt file for debugging purposes


#Function to convert special characters from a text to standard text
def remove_accents(input_str):
	nfkd_form = unicodedata.normalize('NFKD', input_str)
	only_ascii = nfkd_form.encode('ASCII', 'ignore')
	return only_ascii.decode()

def send_email(fromMail, toMail, fileName, user, pw):
	fromaddr = fromMail
	toaddrs  = toMail
	message = ""
	file = open(fileName, 'r')
	data = [line.strip() for line in file]
	i=1
	for line in data:
		message+=line+'\n'
		if(i%2==0):
			message+='\n'
		i+=1


	# Credentials (if needed)
	username = user
	password = pw

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, message)
	server.quit()


def main():
	r = urllib.request.urlopen('http://www.record.pt/futebol/futebol-nacional/liga-nos/sporting.html').read()
	soup = BeautifulSoup(r, 'lxml')

	# letters = soup.findAll('div', class_='thumb-info')
	letters = soup.findAll('div', ['h3', 'p'], class_='thumb-info')
	listOfWords=['sporting', 'bruno', 'carvalho', 'william', 'adrien', 'palhinha', 'alvalade', 'patrício',
				'bas', 'dost', 'leões', 'leonino', 'jesus', 'schelotto', 'jefferson', 'coates', 'douglas',
				'marvin', 'zeegelaar', 'semedo', 'esgaio', 'campbell', 'ruiz', 'castaignos', 'gelson', 'matheus']
	dicti = {}
	for elm in letters:
		dicti[remove_accents(elm.find('h3').getText())]=remove_accents(elm.find('p').getText())

	file = open('output.txt', 'w')
	for key, value in dicti.items():
		for word in key.strip().split():
			if word.lower() in listOfWords:
				file.write(key+'\n'+value+'\n')
	file.close()
	filterDuplicates('output.txt')
	#Note: Change from-email to your e-mail, and to-email to the receiver e-mail. 
	send_email('from-email@gmail.com', 'to-email@gmail.com', 'output.txt', 'from-email', 'from-password')

def filterDuplicates(filename):
	try:
		file = open(filename, 'r')
		data = [line.strip() for line in file]
		data2=[]
		for elm in data:
			if(elm not in data2):
				data2.append(elm)
	
		file.close()
		file = open('output.txt', 'w')
		for elm in data2:
			file.write(elm+'\n')
		file.close()
	except:
		print("Error opening file.")
		

if __name__ == '__main__':
	main()