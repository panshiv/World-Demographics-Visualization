import requests
from bs4 import BeautifulSoup
import pandas as pd

url1 = 'https://www.worldometers.info/world-population/population-by-country/'
attr1={"id": "example2"}
filename1 = 'country.csv'

url2 = 'https://www.worldometers.info/world-population/population-by-region/'
attr2 ={"class":"table table-hover table-condensed"}
filename2='region.csv'

url3='https://www.worldometers.info/world-population/world-population-by-year/'
attr3={"class":"table table-hover table-condensed"}
filename3= 'pop_by_year.csv'

def get_data(url,attr,filename):
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    #print(soup)

    table_data = soup.find("table", attrs=attr)

    headings = []
    for th in table_data.thead.find_all("th") :
        # remove any newlines and extra spaces from left and right
        #headings.append(td.b.text.replace('\n', ' ').strip())
        headings.append(th.text.replace("\n","").strip())
    #print(headings)
    data = pd.DataFrame(columns = headings)
    #print(data)

    for j in table_data.tbody.find_all('tr'):
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(data)
        data.loc[length] = row
    #print(data)
    data.to_csv(filename)

get_data(url3,attr3,filename3)



'''
body = table_data.tbody.find_all('tr')
data = []
for r in range(1,len(body)):
    row = [] # empty lsit to hold one row data
    for tr in body[r].find_all("td"):
        row.append(tr.text.replace("\n","").strip())
        #append row data to row after removing newlines escape and triming unnecesary spaces
    data.append(row)
df = pd.DataFrame(data,columns=headings)
print(df)
data contains all the rows excluding header
row contains data for one row
'''