import requests
import datetime
file = open('./AccessLog')
host = 'https://www.movoto.com/'
localhost = 'http://172.24.0.217:3015/'
line = file.readline()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
lineIndex = 0
while line:
    strArr = line.split(';')
    if lineIndex>900 and strArr[0]!='' and strArr[0].find('/') >=0:
        url = host + strArr[0]
        localUrl = localhost + strArr[0]
        print(lineIndex, 'Checking:', url)
        
        startTime = datetime.datetime.now()
        localr = requests.get(url = localUrl, headers=headers)
        r = requests.get(url = url, headers=headers)
        endTime = datetime.datetime.now()
        if r.status_code != 200:
            print(localr.status_code, r.status_code, url , 'Totol Time:', (endTime-startTime).seconds, '\n')
    line = file.readline()
    lineIndex = lineIndex + 1
