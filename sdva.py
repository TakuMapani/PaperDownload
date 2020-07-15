import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import shutil
import os
from tkinter import *
from tkinter import ttk
import datetime
import threading
import pygeoip
import socket

def dive(link):

    print("hello")
    if re.search(re.compile('pdf'),link.get('href')):
        global max
        url = 'https://pastpapers.co' + link.get('href')
        print("This is a PDF" + url)
        web = urllib.request.Request(url, headers={
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
        website = urllib.request.urlopen(web)
        soup = BeautifulSoup(website)

        fileName = []

        for link1 in soup.findAll('a', href=re.compile('.pdf')):
            #fileName.append(link1.get('href'))
            print(link.get('href'))

        # fPDF = fileName[1]
        # print('\n' + fPDF + '\n')
        # dir = fPDF.split('/')[3:6]
        # # del dir[0:2]
        # # del dir[-1]
        # print(dir)
        # max = len(fileName)
        # downloading['maximum'] = max
        # print(str(max) + ' max is \n')
        # downloading['value'] = 1
        # directory = '/'.join(dir) + '/'
        # if not os.path.exists(directory):
        #     os.makedirs('/'.join(dir) + '/')
        #
        # # for item in itertools.product(dir):
        # #     os.makedirs(os.path.join(*item))
        #
        # for file in fileName:
        #     clock()
        #     global i
        #     i = i + 1
        #     downloading['value'] = i
        #     print(i)
        #     f = file.split("=")[-1]
        #     name = file.split("/")
        #     print('downloading ' + str(name[6]))
        #     url = 'https://pastpapers.co' + f
        #     pdfFile = urllib.request.Request(url, headers={
        #         'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
        #     with urllib.request.urlopen(pdfFile) as response, open(os.path.join(directory, name[6]),
        #                                                            'wb') as out_file:
        #         shutil.copyfileobj(response, out_file)
        #
        # # print(links)
        # website.close()
    elif re.search(re.compile('%'),link.get('href')):
        if link.get('href').find("=asc") >-1 or link.get('href').find("=desc") >-1 :
            pass
        else:
            url = 'https://pastpapers.co' + link.get('href')
            print(url)
            web = urllib.request.Request(url, headers={
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
            website = urllib.request.urlopen(web)
            soup = BeautifulSoup(website)

            for link in soup.findAll('a', href=re.compile('%')):
                print("hie")
                dive(link)

if __name__ == '__main__':
    global i

    #User input for the Subject URL to download
    mainurl = "https://pastpapers.co/cie/?dir=A-Level%2FBusiness-9609"


    MainWeb = urllib.request.Request(mainurl, headers={
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    MainWebsite = urllib.request.urlopen(MainWeb)
    soup = BeautifulSoup(MainWebsite)
    #Array to hold URLArrays
    #It will use a position index

    URLArray = []



    for link in soup.findAll('a', href=re.compile('%')):
   o
            dive(link)
        except socket.gaierror:
            print
            'ignoring failed address lookup'
        #URLArray.append(link.get('href'))
        print(link.get('href'))