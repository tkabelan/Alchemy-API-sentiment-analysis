from bs4 import BeautifulSoup
import sys
import re 

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

#div = soup.find('div')
#print div

#div_class = soup.div['id']
#print div_class

#div_text = soup.div.text
#print div_text


#print(soup.get_text())

#correct attempt
count = 0;
imp = soup('div', {'class' : 'a-section'})
for i in imp:	
	if i.string:
		count = count + 1
		print i
	
print count

#attempt 2

imp2 = [div for div in soup('div')
		if 'a-section' in div.get('class', [0])]
# for ii in imp2:
	# count = count + 1
	# if count == 70:
		# print ii



		
#for link in soup.find(class="a-section")

#for link in soup.find_all('div'):
    #print(link.get('href'))
	#count = count + 1
	#soup.find_all(id="link2")
	#print(link.get('class'))
	#text = (link.get('class'))
	
	#print text
	#print (link.get_text('class'))
	

	
#<div class="a-section">
	
#www.amazon.co.uk/Web-Scraping-Python-Collecting-Modern/dp/1491910291/ref=sr_1_9?ie=UTF8&qid=1448799085&sr=8-9&keywords=data+mining+python
	
# python for beginers
#href
	
# amazon
#<div class="a-section">

