from bs4 import BeautifulSoup
from lxml import html
import urllib3, requests, zipfile, os
from io import BytesIO
import pandas as pd

def main():
    # specify the link
    url = 'https://www.sec.gov/dera/data/financial-statement-data-sets.html'

    http = urllib3.PoolManager()

    response = http.request('GET', url)

    # query the website and return the html to the variable ‘page’

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.prettify())  # Soup variable containes the HTML of the target page

    name_box = soup.find("a", attrs={"class": "views-element-container"})

    page = requests.get('https://www.sec.gov/dera/data/financial-statement-data-sets.html')
    webpage = html.fromstring(page.content)

    a = webpage.xpath('//a/@href')
    target_data = filter(lambda x: 'zip' in x, a)

    pathList = []
    for i in target_data:
        url = 'https://www.sec.gov' + i
        pathList.append(os.path.basename(i))
        print(pathList)
        r = requests.get(url, stream=True)
        z = zipfile.ZipFile(BytesIO(r.content))
        z.extractall(pathList[-1])
        print(url)

    frames_num = []
    frames_sub = []

    for i in pathList:
        path = os.path.abspath(i + "/num.txt")
        print(path)
        dfTemp = pd.read_csv(path, sep='\t', encoding="ISO-8859-1")
        frames_num.append(dfTemp)

    print(frames_num)
    resultNum = pd.concat(frames_num)
    resultNum

    for i in pathList:
        path = os.path.abspath(i + "/sub.txt")
        print(path)
        dfTemp = pd.read_csv(path, sep='\t', encoding="ISO-8859-1")
        frames_sub.append(dfTemp)

    print(frames_sub)
    resultSub = pd.concat(frames_sub)

    resultSub1 = resultSub[['adsh', 'name', 'countryba', 'sic']]
    resultNum1 = resultNum[['adsh', 'tag', 'ddate', 'uom', 'value']]
    result = resultSub1.set_index('adsh').join(resultNum1.set_index('adsh'))

    result.to_csv('result_total.csv')

if __name__ == "__main__":
    main()