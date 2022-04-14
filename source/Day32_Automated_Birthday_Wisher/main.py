import smtplib
import datetime as dt
import pandas as pd

# Global vars
SMTP_ADDRESS = '<SMTP address goes here>'
USERNAME = '<email login goes here>'
TO_ADDRESS = '<address where to send motivational quote goes here>'
PASSWORD = 'email password goes here' # Note, it's a bad idea to store passwords in the code.
now = dt.datetime.now()

def email_motivational_quote(send_to = TO_ADDRESS):
    '''
    Sends a motivational quote
    '''
    if now.strftime('%A') == 'Wednesday': # if now.weekday() == 2:

        quotes = pd.read_csv('quotes.txt',header=None)
        quote = quotes.sample().values
        with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=send_to,
                msg=f'Subject:Wednesday motivational quote from Python project\n\n{quote[0][0]}')

def email_birthday_message():
    '''
    Takes a CSV file of birthdays and sends an automated birthday message to each one on their respective birthdays
    '''
    birthdays = pd.read_csv('birthdays.csv',index_col=None)
    
    todays_birthdays = birthdays[(birthdays['month'] == now.month) & (birthdays['day'] == now.day)]

    for i in range(len(todays_birthdays)):
        name = todays_birthdays.loc[0]['name']
        TO_ADDRESS = todays_birthdays.loc[0].email
        with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=TO_ADDRESS,
                msg=f'Subject:Happy birthday, {name}!  \n\nWishing you the happiest birthday! \n\n -Python app.')


if __name__ == '__main__':
    email_motivational_quote(send_to=TO_ADDRESS)
    #email_birthday_message()