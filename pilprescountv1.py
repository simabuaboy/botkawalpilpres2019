from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import tweepy
import time
import datetime

consumer_key ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxx"



options = Options()
options.headless = True

driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
link = 'https://kawalpemilu.org/#pilpres:0'
driver.get(link)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()

tables = soup.findAll('table',{'class':'aggregate'})

output = []
currentDT = datetime.datetime.now()


for table in tables:
    for row in table.find('tr', {'class':'total'}):
        output.append(row.getText())

pas01 = int(output[2].replace('.', ''))
pas02 = int(output[3].replace('.', ''))
SuaraSah = int(output[4].replace('.', ''))
TidakSah = int(output[5].replace('.', ''))
TPSterima = int(output[7].replace('.', ''))
TotalTPS = int(output[6].replace('.', ''))

persPas01 = '{0:.2f}'.format((pas01/SuaraSah)*100.0)
persPas02 = '{0:.2f}'.format((pas02/SuaraSah)*100.0)
persTotTPS = '{0:.2f}'.format((TPSterima/TotalTPS)*100.0)


hasil = f'Data Kawal Pemilu 2019\n{"{:,}".format(TPSterima)} ' \
        f'TPS dari {"{:,}".format(TotalTPS)} TPS Total ({persTotTPS}%)\n\n' \
        f'Jokowi-Amin | Prabowo-Sandi\n' \
        f'{persPas01}%           {persPas02}%\n\n' \
        f'Jokowi-Amin: { "{:,}".format(pas01)}\n' \
        f'Prabowo-Sandi: { "{:,}".format(pas02)}\n' \
        f'Suara Sah: {"{:,}".format(SuaraSah)}\n' \
        f'Tidak Sah: {"{:,}".format(TidakSah)}\n' \
        f'@KawalPemilu2019 #PantauFotoUpload\n' \
        f'diakses pada : {currentDT.strftime("%Y-%m-%d %H:%M:%S")}'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(status = hasil)
