import requests
r= requests.get('http://www.tsl.news')

#using BeautifulSoup framework
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

#fields= soup.findAll('article', attrs={'class':'article-preview'})


#for link in fields:
for link in soup.findAll('a'):
    #stores all the lines with starting a in link
    
    for content in link.contents:
       #link.contents has all the contents of the field starting with a
        try:
            #strips the leftside  and rightside space from the words
            print(content.strip())
        except:
            print(' ')
            
  #ToDo lists:
#write the contents into File



