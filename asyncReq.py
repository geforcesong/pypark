import grequests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

urls = [
    'http://google.com/',
    'https://www.movoto.com/elkins-wv/181-oak-crest-dr-apt-kerens-hill-elkins-wv-26241-881_10112804/'
]

rs = (grequests.get(u, headers=headers) for u in urls)

print('aaa')
print('111')
results = grequests.map(rs)
print('bbb')
print(results)
print('ccc')