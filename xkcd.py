from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib import urlretrieve
import os, sys
import io, codecs, re

base_url = "http://www.xkcd.com/"
total = 1242

def down_them_all(directory='/temp/xkcd/' , start = 1):
    links = [base_url + str(i) for i in range(start, total + 1)]
    print "Starting download of all links..."
    for url in links:
        print "Fetching" + url
        if int(url.split('/')[-1]) != 404:
            down_content(url, directory + url.split('/')[-1] + '/')

def down_content(url, directory):
    if os.path.exists(directory):
        return
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    if soup.find("div", {"id" : "ctitle"}).string:
        title = (soup.find("div", {"id" : "ctitle"})).string.strip()
    else:
        title = (soup.find("div", {"id" : "ctitle"})).span.string.strip()
    title = re.sub('[.!/;]','', title)
    img_section = soup.find("div", {"id": "comic"})
    img_text = unicode(img_section.img['title'])
    img_url = img_section.img['src']
    img_name = title + '.jpeg'
    os.makedirs(directory)
    imgpath = os.path.join(directory, img_name)
    textfile = os.path.join(directory, title + '.txt')
    f = codecs.open(textfile, 'w', 'utf-8')
    f.write(img_text)
    print "Fetching image: "+ unicode(title)
    urlretrieve(img_url, imgpath)
    print "Done with downloading" + url + "Check at" + directory

if __name__ == '__main__':
#    directory = raw_input('Where to store?')
    print "Let the game begin!"
    down_them_all()
    
    
