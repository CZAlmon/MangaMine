#Ver. 0.1.0
#Authors: Dylan Wise & Zach Almon

#   This program is intended to be used with MangaMine
#   This program is to be run periodically to get Manga Names and thier links from the respective sites
#   This program will then build a textfile that should not be altered, that will be read in when
#   MangaMine is run to give users the option to search for a specific Manga by title
#   If the textfile is altered then the search feature will not run correctly and could crash the program


import urllib.request
import re
import os
import platform
import sys
import string
import html
import time

platformType = platform.system()

def main():
    #Start Bato section

    batoto_search = 'http://bato.to/search'
    counter = 1

    #page 2 = http://bato.to/search?&p=2
    #page 10 = http://bato.to/search?&p=10

    currentDirectory = os.getcwd()
    if platformType == 'Windows':
        MASTERdirectoryName = currentDirectory + "\\Manga_Names_And_Links"
    else:
        MASTERdirectoryName = currentDirectory + "/Manga_Names_And_Links"
    try: 
        os.makedirs(MASTERdirectoryName)
    except OSError:                    
        if not os.path.isdir(MASTERdirectoryName):
            raise

    os.chdir(MASTERdirectoryName)

    print("Downloading Bato.to Page: %d" % (counter), end="", flush=True)
    print("\r", end="", flush=True)
        
    while True:
        try:
            urllibHTML = urllib.request.urlopen(batoto_search).read()
            break

        except:
            print()
            print('Request Failed. Trying again in 30 seconds.')
            time.sleep(30)

    bato_list_of_names = []
    bato_list_of_links = []

    while 1:

        #raw_data is a list of the Manga Names and links
        raw_data = re.findall(r'void\(\d+\)".*?\(\d+\);.*?a href="(.*?)">.*?alt="Status"/>(.*?)</a></strong>', str(urllibHTML), re.DOTALL)

        if len(raw_data) == 0:
            #There is no more Manga names
            break

        for i in range(len(raw_data)):

            bato_list_of_links.append(raw_data[i][0])
            name_str = raw_data[i][1]
            name_str = name_str[1:]
            bato_list_of_names.append(name_str)
            
        counter += 1
        batoto_search = 'http://bato.to/search?&p='

        temp_str = batoto_search + str(counter)

        batoto_search = temp_str

        print("Downloading Bato.to Page: %d" % (counter), end="", flush=True)
        print("\r", end="", flush=True)

        while True:
            try:
                urllibHTML = urllib.request.urlopen(batoto_search).read()
                break

            except:
                print()
                print('Request Failed. Trying again in 30 seconds.')
                time.sleep(30)

        #Hard break Currently there are no manga at page 500
        if counter == 500:
            break

    #End Bato Section
    #Start MangaPanda Section

    mangapanda_listOfLinks = []
    mangapanda_listOfNames = []

    print('\n')
    print("Downloading MangaPanda Page: 1")
    print()
        
    while True:
        try:
            allManga = urllib.request.urlopen('http://www.mangapanda.com/alphabetical').read()
            break

        except:
            print('Request Failed. Trying again in 30 seconds.')
            time.sleep(30)

    #grabs all manga starting with a particular letter, number or symbol
    mangasInAlphaBeta = re.findall(r'ul class=+(.*?)</ul>', str(allManga))

    #using regular patters from the text grabbed above seperates statments into links and names
    for i in range(len(mangasInAlphaBeta)):

        #the first item in the list is manga that start with a space which need to be handled differently from the rest
        if i == 0:
            linksInAlphaNumeric = re.findall(r'href="(.*?)"', mangasInAlphaBeta[i])
            for k in range(len(linksInAlphaNumeric)):
                mangapanda_listOfLinks.append(linksInAlphaNumeric[k])

            namesInAlphaNumeric = re.findall(r'> (.*?)</a>', mangasInAlphaBeta[i])
            for k in range(len(namesInAlphaNumeric)):
                mangapanda_listOfNames.append(namesInAlphaNumeric[k])

        else:
            linksInAlphaNumeric = re.findall(r'href="(.*?)"', mangasInAlphaBeta[i])
            for k in range(len(linksInAlphaNumeric)):
                mangapanda_listOfLinks.append(linksInAlphaNumeric[k])

            namesInAlphaNumeric = re.findall(r'<li>(.*?)</li>', mangasInAlphaBeta[i])
            for k in range(len(namesInAlphaNumeric)):
                tempNameList = re.findall(r'>(.*?)</a>', namesInAlphaNumeric[k])
                mangapanda_listOfNames.append(tempNameList[0])
                         
    #End MangaPanda Section
    #Start MangaHere Section

    mangahere_url = 'http://www.mangahere.co/mangalist/'

    mangahere_list_of_names = []
    mangahere_list_of_links = []

    print("Downloading MangaHere Page: 1")
    print('\n')

    while True:
        try:
            allManga = urllib.request.urlopen(mangahere_url).read()
            break

        except:
            print('Request Failed. Trying again in 30 seconds.')
            time.sleep(30)
    
    raw_data = re.findall('" href="(http://www\.mangahere\.co/manga/.*?/)"><span></span>(.*?)</a></li>', str(allManga))

    for i in range(len(raw_data)):

        mangahere_list_of_links.append(raw_data[i][0])
        mangahere_list_of_names.append(raw_data[i][1])

    
    # Write everything to a file
    #List number here
    #bato_list_of_names = []
    #bato_list_of_links = []
    #\n\n\n\n\n\n\n\n
    #List number here
    #mangapanda_listOfLinks = []
    #mangapanda_listOfNames = []
    #\n\n\n\n\n\n\n\n
    #List number here
    #mangahere_list_of_names = []
    #mangahere_list_of_links = []

    print('Writing to File', end='')
    print('.', end='')
    print('.', end='')
    print('.')

    with open("Manga_Database.txt", "w") as f:

        f.write('WARNING! DO NOT ALTER THIS TEXT! ALTERING THIS TEXT CAN CAUSE\n')
        f.write('MANGAMINE TO CRASH OR BEHAVE UNEXPECTEDLY. ALTER AT YOUR OWN RISK!\n')
        f.write("Bato.to\n")
        f.write(str(len(bato_list_of_names)) + '\n')
        for i in range(len(bato_list_of_names)):

            temp_name = str(bato_list_of_names[i])

            #Python 3.4 Converts '&amp;' Type things to their string equivelant. 
            temp_name = html.unescape(temp_name)

            temp_link = str(bato_list_of_links[i])

            f.write(temp_name + '\t' + temp_link + '\n')

        f.write('\n')
        f.write('*********************************************************\n')
        f.write("MangaPanda\n")
        f.write(str(len(mangapanda_listOfNames)) + '\n')
        for i in range(len(mangapanda_listOfNames)):

            temp_name = str(mangapanda_listOfNames[i])

            #Python 3.4 Converts '&amp;' Type things to their string equivelant. 
            temp_name = html.unescape(temp_name)

            temp_link = str(mangapanda_listOfLinks[i])

            f.write(temp_name + '\t' + temp_link + '\n')

        f.write('\n')
        f.write('*********************************************************\n')
        f.write("MangaHere\n")
        f.write(str(len(mangahere_list_of_names)) + '\n')
        for i in range(len(mangahere_list_of_names)):
       
            temp_name = str(mangahere_list_of_names[i])

            #Python 3.4 Converts '&amp;' Type things to their string equivelant. 
            temp_name = html.unescape(temp_name)

            temp_link = str(mangahere_list_of_links[i])

            f.write(temp_name + '\t' + temp_link + '\n')

    print('Done!')

   
main()
