import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
# http request
# web scraping
# send the mail
# email body
# system date and time manipulation

now = datetime.datetime.now()

# email content placeholder
content = ''
password = os.getenv('PASSWORD_CODE')


def extract_news(url):
    print('Extracting news...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'\n'+'<br>'+'-'*50+'\n<br>')
    response = requests.get(url)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text + '\n' + '<br>')
                if tag.text != 'More' else '')
        # print('here', i, tag)
        # print(tag.prettify) #find all ('span', attrs={'class': 'sitestr'})
    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>'+'-'*6+'<br>')
content += ('<br><br>End of Message')
content += ('<br><br>Carlos was here,')

# print('blank\n blank\n')
# print(cnt)
print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'cvenegas9@gmail.com'
TO = 'carlosvenegas55@hotmail.com'  # must be a list
PASS = password

print('BOOM')
msg = MIMEMultipart()

msg['Subject'] = 'Top Stories HN [Automated Email]' + ' ' + \
    str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
print('Initiating Server...')
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent!')
server.quit()


# print('here', msg)
