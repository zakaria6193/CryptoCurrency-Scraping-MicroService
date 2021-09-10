from flask import Flask
import requests
from bs4 import BeautifulSoup
import schedule
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getdata')
def getdata():
    url = 'https://www.investing.com'
    r = requests.get(url, headers={"User-Agent": "Opera/9.80"})
    soup = BeautifulSoup(r.content, "html.parser")
    body = soup.find('body')
    rows = body.find('table', {'class': 'genTbl js-all-crypto-preview-table wideTbl elpTbl elp20 topCryptoHP'}).find(
        'tbody').find_all('tr')
    dic = dict()
    dic['name'] = []
    dic['symbol'] = []
    dic['price'] = []
    dic['market'] = []
    dic['vol'] = []
    dic['chg'] = []
    for row in rows:
        dic['name'].append(row.find_all('td')[1].text)
        dic['symbol'].append(row.find_all('td')[2].text)
        dic['price'].append(row.find_all('td')[3].text)
        dic['market'].append(row.find_all('td')[4].text)
        dic['vol'].append(row.find_all('td')[5].text)
        dic['chg'].append(row.find_all('td')[6].text)
    print(dic['name'][0])
    print(dic['price'][0])
    print(dic['chg'][0])

    return dic


if __name__ == '__main__':
    app.run()
