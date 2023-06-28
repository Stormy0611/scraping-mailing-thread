import asyncio
from pyppeteer import launch
import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl
from dotenv import load_dotenv
import os

# Load variables from .env into the environment
load_dotenv()
isStart = 0

history = []

port = os.getenv('PORT')
smtp_server = os.getenv('SMTP_SERVER')
server_email = os.getenv('SERVER_GMAIL')
password = os.getenv('APP_PASSWORD')

sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')

def send_mail(subject, content):
    
    message = f"""\
Subject: {subject}

{content}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(server_email, password)
        server.sendmail(sender_email, receiver_email, message)

def scraper():
    try:

        # browser = launch(ignoreHTTPSErrors=True)
        # page = browser.newPage()
        # page.setDefaultNavigationTimeout(60000); # Increases the timeout limit to 60 seconds


        # page.goto('https://betdiary.io/tipster/bets/4915/hamexrodregan/')
        # page.waitForSelector('div[id^="kupong"]', timeout=5000)
        # html = page.content()
        response = requests.get("https://betdiary.io/tipster/bets/4915/hamexrodregan/")
        time.sleep(1)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.select_one('div[id^="kupong"]:first-child')

        id = element['id'].split('-')[-1]
        global history, isStart
        if 'open' in element['data-betfilter'] and id not in history:
            title = list(element.select_one('.card-header > div > .col-lg-6:first-child').children)[-1].text
            content = "Title: " + title + '\n'
            content += list(element.select_one('.card-header > div > .col-lg-6:last-child').children)[3].text.split(', ')[-1] + '\n'
            for ele in element.select('.card-block > div > div.o'):
                content += ele.text + '\n'
            print(content)
            if (not isStart):
                isStart = 1
            else:
                send_mail("A new post by hamexrodregan", content)
            history.append(id)
        else:
            print('not open or already exist')

    except Exception as err:
        print(err)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    while not loop.is_closed():
        scraper()
        time.sleep(1)

    