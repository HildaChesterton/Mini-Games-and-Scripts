import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_data(url, output_filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    for row in soup.select('table tr'):
        tds = row.find_all('td')
        if len(tds) == 3:
            date = tds[0].text.strip()
            name = tds[1].text.strip()
            value = tds[2].text.strip()
            data.append([date, name, value])

    df = pd.DataFrame(data, columns=['Date', 'Name', 'Value'])

    df['Value'] = df['Value'].str.replace(',', '').astype(float)

    df = df.groupby(['Name', 'Date']).sum().reset_index()

    df.to_csv(output_filename, index=False)

if __name__ == '__main__':
    url = input("Enter URL to scrape data from: ")
    output_filename = input("Enter output CSV filename: ")
    scrape_data(url, output_filename)
