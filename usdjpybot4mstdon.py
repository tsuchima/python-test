import urllib.request
import time,datetime
from bs4 import BeautifulSoup
from mastodon import Mastodon

url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=USDJPY=X'

mastodon = Mastodon(
    client_id="app_key.txt",
    access_token="user_key.txt",
    api_base_url = "https://friends.nico/")


while True :
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
        bsObj = BeautifulSoup(body, "html.parser")
        table = bsObj.findAll("table",{"class":"stocksTable"})[0]
        rows = table.findAll("tr")
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())

        dt = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        toot = '{0} 1USD={1}YEN #botテスト'.format(dt,csvRow[1])
        print(toot)
        mastodon.toot(toot)

    time.sleep(60)


