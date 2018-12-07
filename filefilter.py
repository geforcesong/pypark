import re
file = open('/Users/george/Downloads/service_perf.log')
line = file.readline()
while line:
    matchObj = re.search( r'(\d+) ms.', line)
    if matchObj == None:
        continue
    ms = int(matchObj.group(1))
    if ms >1500:
        print(ms)
    line = file.readline();