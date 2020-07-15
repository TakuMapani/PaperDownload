import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import shutil
import os

import itertools

def main():

    url = 'https://pastpapers.co/cie/?dir=IGCSE%2FBiology-0610%2F2010%2F2010%20Jun'
    web = urllib.request.Request(url,headers={'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    website =  urllib.request.urlopen(web)
    soup = BeautifulSoup(website)

    fileName =[]

    for link in soup.findAll('a', href=re.compile('.pdf')):
        fileName.append(link.get('href'))
       # print(link.get('href'))

    fPDF = fileName[1]
    print(fPDF)
    dir =fPDF.split('/')[3:6]
    # del dir[0:2]
    # del dir[-1]
    print (dir)
    directory = '/'.join(dir) + '/'
    if not os.path.exists(directory):
        os.makedirs('/'.join(dir) + '/')

    # for item in itertools.product(dir):
    #     os.makedirs(os.path.join(*item))


    for file in fileName :
        f = file.split("=")[-1]
        name = file.split("/")
        url = 'https://pastpapers.co' + f
        pdfFile = urllib.request.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
        with urllib.request.urlopen(pdfFile) as response, open(os.path.join(directory,name[6]),'wb') as out_file:
            shutil.copyfileobj(response,out_file)





    #print(links)
    website.close()


if __name__ == '__main__':
    main()


#*************************************************************
#print(fileName)
    # html = website.read().decode("utf-8")
    # links = re.findall('"((pdf)s?://.*?)"', html)
    #
    # out_str = ",".join(links)

    # with open("pdf.txt", "w") as outp:
    #     outp.write(out_str)
    #
    # for link in links :
    #     fileName = link.split("=")[-1]
    #     #print(fileName)