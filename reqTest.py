import grequests
import datetime
file = open('./AccessLog')
host = 'https://www.movoto.com/'
localhost = 'http://172.24.0.217:3015/'
line = file.readline()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
lineIndex = 0
try:
    while line:
        strArr = line.split(';')
        if lineIndex > 4036 and strArr[0] != '' and strArr[0].find('/') >= 0:
            # strArr[0] = 'healthcheck/'
            url = host + strArr[0]
            localUrl = localhost + strArr[0]
            print(lineIndex, 'Checking:', url)
            rs = (grequests.get(u, headers=headers) for u in [localUrl, url])
            results = grequests.map(rs)

            if results[0].status_code != 200 or results[1].status_code != 200:
                print('local:{0}/{1}ms, Prod:{2}/{3}ms, {4}\n'.format(results[0].status_code, int(results[0].elapsed.total_seconds()*1000),
                results[1].status_code, int(results[1].elapsed.total_seconds()*1000), url))
        line = file.readline()
        lineIndex = lineIndex + 1
except:
    print('finished!')

