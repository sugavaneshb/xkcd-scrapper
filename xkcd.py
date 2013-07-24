from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib import urlretrieve
import os, sys


base_url = "http://www.xkcd.com/"
total = 1242

def down_them_all(directory='/temp/xkcd/' , start = 1):
    links = [base_url + str(i) for i in range(start, total + 1)]
    print "Starting download of all links..."
    for url in links:
        print "Fetching" + url
        down_content(url, directory + url.split('/')[-1] + '/')

def down_content(url, directory):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    title = (soup.find("div", {"id" : "ctitle"})).string.strip()
    img_section = soup.find("div", {"id": "comic"})
    img_text = img_section.img['title']
    img_url = img_section.img['src']
    img_name = title + '.jpeg'
    if os.path.exists(directory):
        return
    os.makedirs(directory)
    imgpath = os.path.join(directory, img_name)
    textfile = os.path.join(directory, title + '.txt')
    print "Fetching image: "+title
    urlretrieve(img_url, imgpath)
    f = open(textfile, 'w')
    f.write(img_text)
    print "Done with downloading" + url + "Check at" + directory

if __name__ == '__main__':
#    directory = raw_input('Where to store?')
    print "Let the game begin!"
    down_them_all()
    
    
