import requests
from datetime import datetime
import smtplib
import time

# API globals
ISS_API_URL = 'http://api.open-notify.org/iss-now.json'
SUN_RISE_SET_API_URL = 'http://api.sunrise-sunset.org/json'
SAMPLE_LAT = 41.3948
SAMPLE_LONG = 73.4540
ISS_LAT = 0
ISS_LONG = 0

# Email notification globals
SMTP_ADDRESS = '<SMTP address goes here>'
USERNAME = '<email login goes here>'
TO_ADDRESS = '<address where to send motivational quote goes here>'
PASSWORD = 'email password goes here' # Note, it's a bad idea to store passwords in the code.

def send_notification():
    '''
    Sends a motivational quote
    '''
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=TO_ADDRESS,
            msg=f'Subject:The ISS is should be visible!\n\ncurrent location is {ISS_LAT, ISS_LONG}')

def is_iss_overhead():
    '''
    Quereis the iss open-notify API to determine if the ISS is visible from the preset lat and long coordinates
    '''
    global ISS_LAT
    global ISS_LONG
    response = requests.get(url=ISS_API_URL)
    response.raise_for_status()
    data = response.json()
    ISS_LAT = float(data['iss_position']['latitude'])
    ISS_LONG = float(data['iss_position']['longitude'])

    if (abs(ISS_LAT - SAMPLE_LAT) <= 5) and (abs(ISS_LONG - SAMPLE_LONG) <= 5):
        return True
    else:
        return False

def is_nighttime():
    '''
    Queries the sun rise/set API and returns True if the sun has set or is setting for the day, and False if the sun has risen.
    '''
    parameters = {
    'lat': SAMPLE_LAT,
    'lng': SAMPLE_LONG,
    'formatted': 0
    }

    response = requests.get(url = SUN_RISE_SET_API_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]
    time_now = datetime.now()

    if (sunset.hour >= time_now.hour()) or (sunrise.hour >= time_now.hour()):
        return True
    else:
        return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        send_notification()