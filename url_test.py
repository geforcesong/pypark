import requests

with requests.get('https://api.douban.com/v2/book/2129650') as f:
    print('Status:', f.status_code, f.reason)