import requests
import json
import datetime
import tweepy

consumer_key ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxx"

request = requests.get('https://kawal-c1.appspot.com/api/c/0')
rawJSON = json.loads(request.text)
provinceRows = rawJSON['data']
kpuTPS = rawJSON['children']
currentDT = datetime.datetime.now()

TotTPSkpu = 0
suaraSah = list()
jokowiVoters = list()
prabowoVoters = list()
tidakSah = list()
tpsTerima = list()

for provinceRow in provinceRows.values():
    provinceVoteData = provinceRow['sum']
    suaraSah.append(int(provinceVoteData['sah']))
    jokowiVoters.append(int(provinceVoteData['pas1']))
    prabowoVoters.append(int(provinceVoteData['pas2']))
    tidakSah.append(int(provinceVoteData['tSah']))
    tpsTerima.append(int(provinceVoteData['cakupan']))

for n in range(len(kpuTPS)):
    Kpus = kpuTPS[n]
    TotTPSkpu += (Kpus[2])

persPas01 = '{0:.2f}'.format((sum(jokowiVoters)/sum(suaraSah))*100.00)
persPas02 = '{0:.2f}'.format((sum(prabowoVoters)/sum(suaraSah))*100.00)
persTotTPS = '{0:.2f}'.format((sum(tpsTerima)/TotTPSkpu)*100.0)

hasil = f'Data Kawal Pemilu 2019\n{"{:,}".format(sum(tpsTerima))} ' \
        f'TPS dari {"{:,}".format(TotTPSkpu)} TPS Total ({persTotTPS}%)\n\n' \
        f'Jokowi-Amin | Prabowo-Sandi\n' \
        f'{persPas01}%           {persPas02}%\n\n' \
        f'Jokowi-Amin: {"{:,}".format(sum(jokowiVoters))}\n' \
        f'Prabowo-Sandi: {"{:,}".format(sum(prabowoVoters))}\n' \
        f'Suara Sah: {"{:,}".format(sum(suaraSah))}\n' \
        f'Tidak Sah: {"{:,}".format(sum(tidakSah))}\n' \
        f'@KawalPemilu2019 #PantauFotoUpload\n' \
        f'diakses pada : {currentDT.strftime("%Y-%m-%d %H:%M:%S")}'

print(hasil)

csv1 =  f'{sum(jokowiVoters)},{sum(prabowoVoters)},{sum(suaraSah)},' \
        f'{sum(tidakSah)},{persPas01},{persPas02},' \
        f'{sum(tpsTerima)},{TotTPSkpu},{persTotTPS},' \
        f'{currentDT.strftime("%Y-%m-%d")},{currentDT.strftime("%H:%M:%S")}\n'

with open('/path/to/your/file.txt', 'a') as myfile:
     myfile.write(csv1)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(status = hasil)

