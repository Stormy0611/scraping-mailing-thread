# environment set up
## Run these command:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Enter your accounts and emails into .env
PORT=465                            # For SSL
SMTP_SERVER="smtp.gmail.com"        # SMTP server host
SERVER_GMAIL=                       # Your gmail address
APP_PASSWORD=                       # Your app password of your gmail account
SENDER_EMAIL=                       # Sender's email
RECEIVER_EMAIL=                     # Receiver's email

## Run app
python main.py

## Stop app
Ctrl + c
