# botkawalpilpres2019
merupakan script menjalankan bot https://twitter.com/BotKawalPemilu1 

## background
adanya kawalpemilu.org melihat telah mentabulasi data dari crowdsource C1 seteralah pemilu indonesia, sehingga tertarik untuk menyajikannya pada sebuah akun twitter yang merupakan bot update tweet setiap 30 menit.

### sedikit cerita
dari proses pembelajaran ini tujuannya agar belajar bagaimana metode scrapping menggunakan python itu sendir, setelah semua sistem go ada beberapa yang unik menurut saya, karena script ini mempublish ke sosial media, apalagi sedang dalam suasana politik, awalnya saya berpikir akun bot tersebut tidak perlu memiliki banyak akun yang di follow, namun melihat trendnya masih stagnan dan tidak banyak orang yang memperhatikan, kemudian saya mem-follow akun yang juga di ikuti oleh akun resmi kawalpemilu.org, di saat itu traction naik ketika mereka me retweet akun bot ini, grwoth dari follower akun tersebut meningkat dalam 4 hari sampai pada 2500 follower twitter, hal ini cukup menarik bagi saya.
kemudian dari sisi teknis, awalnya saya melihat bahwa jalur scraping dari total pada table kawal pemilu bisa menjadi solusi praktis(read: terlalu malas untuk mengolah hasil json endpoint mereka), lalu hal ini menjadi mengesalkan karena dalam proses update row/colum pada tabel hasil perhitungan pemilu, di lihat pada scrip **pilprescountv1.py** lalu karena ada komunikasi dengan tim dev mereka saya tau kapan table tersebut di update secara script, dan di jalankan di dalam raspi dengan cron per 30 menit, kemudian mencoba untuk menyimpan data yang di ambil per 30 menit tersebut pada **pilprescountv2.py**, dari scrolling twitter melihat retweet kawalpemilu saya melihat ada yang menganalisis data json mereka dengan python orangnya <link>[ini](https://github.com/dimitrijray/kawal-pemilu-capture) dan mempelajari script tersebut maka tidak perlu scrapping tabel lagi dan tidak berpengaruh ketika bentuk tabel berganti **pilprescountv3.py** (kecuali mereka merubah format jsonnya). 


## setup
1. ikuti setup untuk akun developer twitter di <link>[sini](https://developer.twitter.com/en/apply-for-access.html)
2. berjalan pada python memerlukan library :
	1. Tweepy
 	2. BeautifulSoup
 	3. selenium
3. raspberry pi (yang ini untuk gak ganggu kerjaan sih, biar bisa 24/7)
4. mie rebus sama kopi

