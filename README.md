# environment set up

## Run these command

```cli
python -m venv venv
```

```cli
venv\Scripts\activate
```

_If use bash_

```bash
source ./venv/Scripts/activate
```

## Install libraries

```cli
pip install -r requirements.txt
```

## Enter your accounts and emails into .env

| | |
|---|---|
|PORT=465|                            # For SSL|
|SMTP_SERVER="smtp.gmail.com"|        # SMTP server host|
|SERVER_GMAIL|                       # Your gmail address|
|APP_PASSWORD|                       # Your app password of your gmail account|
|SENDER_EMAIL|                       # Sender's email|
|RECEIVER_EMAIL|                     # Receiver's email|

## Run app

```cli
python main.py
```

## Stop app

Ctrl + c

## How to create app password?

<https://support.google.com/mail/answer/185833?hl=en>
