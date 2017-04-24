#Beatiful Soup - To parse the html
from bs4 import BeautifulSoup
#urllib.request - to make http request
import urllib.request
#To remove any language special characters
import unicodedata
# EMAIL library
import smtplib

#Function to convert special characters from a text to standard text
def remove_uknown_characters(input_str):
	nfkd_form = unicodedata.normalize('NFKD', input_str)
	only_ascii = nfkd_form.encode('ASCII', 'ignore')
	return only_ascii.decode()

def filter_duplicates(news_list):
	return_list = []
	for item in news_list:
		if(item not in return_list):
			return_list.append(item)
	return return_list

def get_news(soup):
	# letters = soup.findAll('div', class_='thumb-info')
	letters = soup.findAll('div', ['a','h3', 'p'], class_='thumb-info')
	listOfWords=['sporting', 'bruno', 'carvalho', 'william', 'adrien', 'palhinha', 'alvalade', 'patrício',
				'bas', 'dost', 'leões', 'leonino', 'jesus', 'schelotto', 'jefferson', 'coates', 'douglas',
				'marvin', 'zeegelaar', 'semedo', 'esgaio', 'campbell', 'ruiz', 'castaignos', 'gelson', 'matheus']
	news_ = []
	for elm in letters:
		link = 'http://www.record.pt'+elm.find('a')['href']
		news_item = [link, remove_uknown_characters(elm.find('h3').getText()), remove_uknown_characters(elm.find('p').getText())]
		news_.append(news_item)


	news_ = filter_duplicates(news_)

	to_return = []
	id_counter=1
	for elm in news_:
		tmp = {}
		tmp['link']=elm[0]
		tmp['title'] = elm[1]
		tmp['content'] = elm[2]
		tmp['id'] = id_counter
		id_counter+=1
		to_return.append(tmp)
		
	return to_return

def get_news_full_text(link):
	r = urllib.request.urlopen(link).read()
	soup = BeautifulSoup(r, 'lxml')

	return_ = {}

	#News header
	news_header_ = {}
	news_header = soup.findAll('div', ['h1','p'], class_='article-header clearfix')
	count=0
	for elm in news_header:
		if(count==0):
			try:
				title_ = elm.find('h1').getText()
				title_mini_ = elm.find('p').getText()
				news_header_['title'] = title_
				news_header_['title_mini'] = title_mini_
			except:
				pass
		else:
			break
		count+=1
	return_['header'] = news_header_
	
	#News photo
	news_photo_ = {}
	news_photo = soup.findAll('div', ['img'], class_= 'article-photo clearfix')
	for elm in news_photo:
		try:
			news_photo_['photo_url'] = elm.find('img')['src']
			news_photo_['photo_alt'] = elm.find('img')['alt']
		except:
			pass
	return_['photo'] = news_photo_

	#News content
	news_content_ = {}
	news_content = soup.findAll('div', class_='col-xs-12 article-main')
	count=0
	for elm in news_content:
		if(count==0):
			try:
				news_content_['content'] = elm.find('p').getText()
			except:
				pass
		else:
			break
		count+=1
	return_['content'] = news_content_

	# print(return_)
	return return_


def run():
	r = urllib.request.urlopen('http://www.record.pt/futebol/futebol-nacional/liga-nos/sporting.html').read()
	soup = BeautifulSoup(r, 'lxml')

	news_ = get_news(soup)

	# print(news_)
	# get_news_full_text('http://www.record.pt/futebol/futebol-nacional/liga-nos/sporting/detalhe/ruben-e-gelson-reavaliados-amanha.html')
	return news_

if __name__ == '__main__':
	run()