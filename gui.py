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

global array_urlarrays
global array_pos
array_pos = 0
##The Layout configarations
root = Tk()
i = 0
max = 0

helpLabel = ttk.Label(root, text='Enter URL for Past Papers')
helpLabel.grid(row=0, column=0, columnspan=2)
startButton = ttk.Button(root, text='Start', command=lambda: download()).grid(row=1, column=0, columnspan=1, padx=2,
                                                                              pady=2)
stopButton = ttk.Button(root, text='Exit', command=lambda: exit()).grid(row=1, column=1, columnspan=1, padx=2, pady=2)
urlInput = ttk.Entry(root)
urlInput.grid(row=2, column=0, columnspan=4, padx=2, pady=2)
downloading = ttk.Progressbar(root, orient="horizontal",
                              length=200, mode="determinate")
downloading.grid(row=3, column=0, columnspan=4)


# errorLabel = ttk.Label(root, text = 'Please Enter a URL',).grid(row = 3, column = 0 , columnspan = 1)

def exit():
    root.destroy()


def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    root.update()
    root.after(10, clock)  # run itself again after 1000 ms


def download():
    clock()

    if urlInput.index("end") == 0:
        global helpLabel
        helpLabel['text'] = 'Please enter Correct URL'
        clock()
    else:

        download_thread = threading.Thread(target=backgroundDownload())
        download_thread.start()





def backgroundDownload():
    global i

    #User input for the Subject URL to download
    mainurl = urlInput.get()


    MainWeb = urllib.request.Request(mainurl, headers={
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    MainWebsite = urllib.request.urlopen(MainWeb)
    soup = BeautifulSoup(MainWebsite)
    #Array to hold URLArrays
    #It will use a position index

    URLArray = []



    # for link in soup.findAll('a', href=re.compile('%')):
    #     URLArray.append(link.get('href'))
    #     print(link.get('href'))

    # for PartUrl in URLArray:
    #     global max
    #     url = 'https://pastpapers.co' + PartUrl
    #     web = urllib.request.Request(url, headers={
    #         'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    #     website = urllib.request.urlopen(web)
    #     soup = BeautifulSoup(website)

    # web = urllib.request(mainurl, headers={
    #          'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

    # website = urllib.request.urlopen(web)
    fileName = []

    for link in soup.findAll('a', href=re.compile('.pdf')):
        fileName.append(link.get('href'))
        print(link.get('href'))
    #
    fPDF = fileName[1]
    print('\n' + fPDF + '\n')
    dir = fPDF.split('/')[11:13]
    # del dir[0:2]
    # del dir[-1]
    print(dir)
    max = len(fileName)
    downloading['maximum'] = max
    print(str(max) + ' max is \n')
    downloading['value'] = 1
    directory = '/'.join(dir)
    if not os.path.exists(directory):
        os.makedirs('/'.join(dir) + '/')



    for file in fileName:
        clock()
        global i
        i = i + 1
        downloading['value'] = i
        print(i)

        f = re.sub('[ ]',"%20",file)
        url = re.sub('/wp-content/uploads/../..',"",f)
        nameArray = url.split('%20')[1:10]
        name = nameArray[0]+"_"+nameArray[1]+nameArray[2]+nameArray[3]+nameArray[4]+nameArray[len(nameArray)-1]
        print(name)
        print(url)
        pdfFile = urllib.request.Request(url, headers={
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
        with urllib.request.urlopen(pdfFile) as response, open(os.path.join(directory, name),
                                                               'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    i = 0
    downloading['value'] = i

    print(fileName)
    MainWebsite.close()


root.mainloop()
