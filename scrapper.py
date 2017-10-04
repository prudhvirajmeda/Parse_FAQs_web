#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import re

f1 = open('ques.txt','w')


quote_page = 'https://www.ugrad.vcu.edu/why/faqs/admissions.html'

page_1 = "https://www.ugrad.vcu.edu/why/faqs/admissions.html"
page_2 = "https://www.ugrad.vcu.edu/why/faqs/activities.html"
page_3 = "https://www.ugrad.vcu.edu/why/faqs/dining.html"
page_4 = "https://www.ugrad.vcu.edu/why/faqs/enrollment.html"
page_5 = "https://www.ugrad.vcu.edu/why/faqs/financing.html"
page_6 = "https://www.ugrad.vcu.edu/why/faqs/health.html"
page_7 = "https://www.ugrad.vcu.edu/why/faqs/housing.html"
page_8 = "https://www.ugrad.vcu.edu/why/faqs/libraries.html"
page_9 = "https://www.ugrad.vcu.edu/why/faqs/transfers.html"
page_10 = "https://www.ugrad.vcu.edu/why/faqs/transportation.html"

listPage = [page_1, page_2, page_3, page_4, page_5, page_6, page_7, page_8, page_9, page_10]

pageFile = [len(listPage)]

for i in listPage:
	page = urllib2.urlopen(i)

	soup = BeautifulSoup(page,'html.parser')

	questions = soup.find_all('h4')



	first_link = soup.h4

	tags = []

	for tag in soup.find_all(True):
	    tags.append(tag.name)



	tags_post_h4 = []


	for num,i in enumerate(tags):
		if i == 'h4':
			tags_post_h4.append(tags[num+1])
			


	def check_questions(questions):
		if 'table' in tags_post_h4:

			ind = tags_post_h4.index('table')
			questions.pop(ind)
			return questions
		
		else:
			pass


	if 'table' in tags_post_h4:

		questions = check_questions(questions)


	for i in questions:
		print i.text.strip()
		



	answers = first_link.find_all_next('p')

	

	string_ans = []

	for i in answers:
		string_ans.append(str(i))

	grab_ans = []

	def cleanhtml(raw_html):
	 cleanr = re.compile('<a.*?>')
	 cleantext = re.sub(cleanr, '', raw_html)
	 cleantext = re.sub('</a>', '', cleantext)
	 return cleantext

	for i in string_ans:	
		if i.startswith('<p>') :
			ans = re.search('<p>(.*)<',i).group(1)
			ans = cleanhtml(ans)
			grab_ans.append(ans)
			print ('\n'+ans)
			



