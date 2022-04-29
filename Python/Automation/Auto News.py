import requests # http requests
from bs4 import BeautifulSoup #web scraping
import smtplib # email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime # System data and time manipulation

now = datetime.datetime.now()


content = '' #Email content placeholder

#Extracting website info

def extract_news(url):
    print('Extracting News Stories...')
    cnt = '' # content
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content # local source not related to content outside of function on line 8
    soup = BeautifulSoup(content, 'html.parser')
    
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''} )):
        cnt += ((str(i+1)+' :: '+tag.text+"\n"+'<br>') if tag.text!='More' else'')
        # print(tag.prettify) #find all('span',attrs={'class':'sitestr'}})
        return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('')
