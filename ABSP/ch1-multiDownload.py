# XKCD download

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok = True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic,endComic):
        #download the page
        print('downloading page %s...' %(urlNumber))
        res = requests.get ('http://xkcd.com/%s' %(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # find the url of the comic image
        comicElem == soup.select('#comic img')
        if comicElem == []:
            print('could not find comic img')
        else:
            comicUrl = comicElem[0].get('src')
        #download the img
        print('downloading img %s' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        #save img to ./xkcd
        imageFile = open(os.path.join('skcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # create and start thread objects
downloadThread = []
for i in range(0, 1400, 100): # loop 14 times
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('done')
