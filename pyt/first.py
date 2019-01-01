import hmac
import base64
import requests 
import json
import calendar;
import time;
import datetime
import dateutil.parser
import csv
from pathlib import Path

CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'
base_url = 'https://www.okex.com'
key1='13c73ed2-f033-4699-bf9a-827d959a46efd'
key2='E3AD2EE1783BB5654CD130777A18672F5'
instrument_id='ETH-BTC'

utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
ts=datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()


 
response = requests.get(base_url + "/api/general/v3/time")

# json
print(response.json())
ts=response.json()['iso'];
print (ts)
# signature
def signature(timestamp, method, request_path,  secret_key):
    message = str(timestamp) + str.upper(method) + request_path 
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d).decode()

def signatureBody(timestamp, method, request_path, body, secret_key):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


# set request header
def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[CONTENT_TYPE] = APPLICATION_JSON
    header[OK_ACCESS_KEY] = api_key
    header[OK_ACCESS_SIGN] = sign
    header[OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[OK_ACCESS_PASSPHRASE] = passphrase
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


# request example
# set the request url

request_path = '/api/account/v3/currencies'
# set request header
header = get_header(key1, signature(ts, 'GET', request_path, key2), ts, 'sefidom')

# do request
response = requests.get(base_url + request_path, headers=header)
# json




request_path = '/api/spot/v3/instruments/ticker'
# set request header
header = get_header(key1, signature(ts, 'GET', request_path, key2), ts, 'sefidom')

# do request
response = requests.get(base_url + request_path, headers=header)
# json

tokenpair=response.json()
while True:
    print("new loop")
    for instrument in tokenpair:
      try:
        time.sleep(0.15)
        instrument_id=instrument['instrument_id']
        request_path = '/api/spot/v3/instruments/'+instrument_id+'/candles?granularity=60'
        # set request header
        header = get_header(key1, signature(ts, 'GET', request_path, key2), ts, 'sefidom')
        
        # do request
        response = requests.get(base_url + request_path, headers=header, timeout=15)
        # json
    

        fileCsv='eggs'+instrument_id+'.csv'
        my_file = Path(fileCsv)
        maxTime=0
        if my_file.is_file():
            with open(fileCsv, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                for row in spamreader:
                    
                    if(float(row[0])>maxTime):
                        maxTime=float(row[0])

        
        print(fileCsv+':maxtime:'+str(maxTime))
        with open(fileCsv, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for x in response.json():
                if (maxTime<dateutil.parser.parse(x['time']).timestamp()):
                    print(fileCsv+' add '+str(dateutil.parser.parse(x['time']).timestamp()))
                    spamwriter.writerow([dateutil.parser.parse(x['time']).timestamp(), x['open'], x['close'],x['low'],x['high'],x['volume']])
      except:
        print("error connection")	




