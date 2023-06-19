import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import keyboard

history = []

import smtplib, ssl

def send_mail(user, content):

    sender_address = "devstar0611@gmail.com"
    receiver_address = "wemilly.jiang@gmail.com"

    message = """\
        Subject: Hello from Python!

        This message was sent from my Python application!"""

    port = 465  # This is the default SSL port
    password = input("password")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_address, password)
        server.sendmail(sender_address, receiver_address, message)



async def scraper():
    
    try:
        while True:
            browser = await launch(ignoreHTTPSErrors=True)
            page = await browser.newPage()

            await page.goto('https://betdiary.io/tipster/bets/4915/hamexrodregan/')
            await page.waitForSelector('div[id^="kupong"]', timeout=5000)
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            element = soup.select('div[id^="kupong"]', limit=1)[0]
            id = element['id'].split('-')[-1]
            global history
            if 'open' in element['data-betfilter'] and id not in history:
                print(element.select('.card-header > div > .col-lg-6:first-child').text)
                # send_mail("hamexrodregan", id)
                history.append(id)
                print(element['id'].split('-')[-1])
            else:
                print('not open or already exist')

            await browser.close()
            
            
            
            await asyncio.sleep(1)

            # # Create a new workbook and select the active worksheet
            # workbook = openpyxl.Workbook()
            # worksheet = workbook.active
            # # sheet = workbook['Sheet1']

            # # Add some data to the worksheet
            # worksheet['A1'] = 'Name'
            # worksheet['B1'] = 'Street Address'
            # worksheet['C1'] = 'City'
            # worksheet['D1'] = 'State'
            # worksheet['E1'] = 'ZIP Code'
            # worksheet['F1'] = 'Phone Number'
            # worksheet['G1'] = 'Email'
            # worksheet['H1'] = 'Website'
            # worksheet['I1'] = 'Average Rating'
            # worksheet['J1'] = 'Number of Reviews'

            # for res in result_names:
            #     worksheet.append(res)
            # # worksheet.append(['Jane', 30, 'London'])
            # # worksheet.append(['Bob', 40, 'Paris'])

            # # Save the workbook
            # workbook.save('sheet.xlsx')
    except asyncio.CancelledError:
        print("Coroutine was cancelled")
    except Exception as err:
        print(err)

async def main():
    # Start the coroutine in a separate thread
    task = asyncio.create_task(scraper())
    
    # Run other code concurrently here
    while not keyboard.is_pressed('esc'):
        await asyncio.sleep(0.1)

    task.cancel()

if __name__ == "__main__":
    try: 
        asyncio.run(main())
        print('exit')
    except:
        print('exit with error')
