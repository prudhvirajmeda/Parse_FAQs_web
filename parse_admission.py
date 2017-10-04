
import urllib2
from bs4 import BeautifulSoup
import re
quote_page = 'https://www.ugrad.vcu.edu/why/faqs/admissions.html'
page = urllib2.urlopen(quote_page)

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
		# print ind
		questions.pop(ind)
		return questions
		
	else:
		pass


if 'table' in tags_post_h4:

	questions = check_questions(questions)



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
		# print ('\n'+ans)
		

ques_ans_dic = {}

for num,i in enumerate(questions):
	i=str(i)
	j = i.replace('?','')
	j = re.search(r'(?<=\>)(?!\<)(.*)(?=\<)(?<!\>)',j).group(1)
	ques_ans_dic[str(j)]= grab_ans[num]

print ques_ans_dic

