#Ver. 0.3.0
#Authors: Dylan Wise & Zach Almon

import urllib.request
import re
import os
import platform
import sys

platformType = platform.system()

def main():
    success = False
    currentDirectory = os.getcwd()
    downloadMangaListOnce = False
    searchAgain = False

    print('Currently MangaMine only supports MangaPanda.')
    print()
    print('The URL you are to input below should be the top level page of the')
    print('manga you wish to download')
    print('Ex: http://www.mangapanda.com/372/seto-no-hanayome.html ')

    while success == False:
        downloadManga = True
        mangaFound = False

        while 1:
            if searchAgain == False:
                print()
                print('Do you wish to search for a manga or provide a link like the one above?')
                print('[s]earch, [l]ink and [q]uit')
                searchRequest = input('')
                print()

            if searchRequest == 's' or searchAgain == True:
                mangaFound = False
                tryLink = False
                searchAgain = False

                #to ensure we aren't repeatedly loading the same page of HTML this bool will trigger once per time the script is run
                if downloadMangaListOnce == False:
                    listOfLinks = []
                    listOfNames = []
                    downloadMangaListOnce = True

                    allManga = urllib.request.urlopen('http://www.mangapanda.com/alphabetical').read()

                    #grabs all manga starting with a particular letter, number or symbol
                    mangasInAlphaBeta = re.findall(r'ul class=+(.*?)</ul>', str(allManga))

                    #using regular patters from the text grabbed above seperates statments into links and names
                    for i in range(len(mangasInAlphaBeta)):

                        #the first item is the list is manga that start with a space which need to be handled differently from the rest
                        if i == 0:
                            linksInAlphaNumeric = re.findall(r'href="(.*?)"', mangasInAlphaBeta[i])
                            for k in range(len(linksInAlphaNumeric)):
                                listOfLinks.append(linksInAlphaNumeric[k])

                            namesInAlphaNumeric = re.findall(r'> (.*?)</a>', mangasInAlphaBeta[i])
                            for k in range(len(namesInAlphaNumeric)):
                                listOfNames.append(namesInAlphaNumeric[k])

                        else:
                            linksInAlphaNumeric = re.findall(r'href="(.*?)"', mangasInAlphaBeta[i])
                            for k in range(len(linksInAlphaNumeric)):
                                listOfLinks.append(linksInAlphaNumeric[k])

                            namesInAlphaNumeric = re.findall(r'<li>(.*?)</li>', mangasInAlphaBeta[i])
                            for k in range(len(namesInAlphaNumeric)):
                                tempNameList = re.findall(r'>(.*?)</a>', namesInAlphaNumeric[k])
                                listOfNames.append(tempNameList[0])
                          

                #checks list created above for the particular manga stated below
                print('What is the name of the Manga you wish to download? (Case sensitive!)')
                potentialMangaName = input('')
                print()

                for i in range(len(listOfNames)):
                    if potentialMangaName == listOfNames[i]:
                        mangaFound = True
                        searchedMangaLink = listOfLinks[i]
                        break

                if mangaFound == True:
                    print('Success! That manga exists on MangaPanda.')
                    print()
                    break

                else:
                    print('Error! That manga does not exist on MangaPanda!')
                    while 1:
                        print()
                        print('Do you wish to [s]earch again or provide a [l]ink? (or [q]uit)')
                        failSearchQuery = input('')
                        print()

                        if failSearchQuery == 's':
                            searchAgain = True
                            break

                        elif failSearchQuery == 'l':
                            tryLink = True
                            break

                        elif failSearchQuery == 'q':
                            return

                        else:
                            print('Invalid Input!')

            elif searchRequest == 'l':
                break

            elif searchRequest == 'q':
                return

            else:
                print('Invalid input!')

            if tryLink == True:
                break

        if mangaFound == False:
            print()
            print('Please enter the url of the manga you wish to download or [q]uit: ')
            urlRequest = input('')
            print()

            if urlRequest == 'q':
                return
            
        else:
            urlRequest = 'http://www.mangapanda.com' + searchedMangaLink 

        #take the URL the user gave and cut off last five characters (.html)
        try:
            urllibHTML = urllib.request.urlopen(urlRequest).read()
            urlRequest = urlRequest[:-5]

        except:
            print()
            print('Invalid URL!')
            downloadManga = False

            #links to chapters on mangapanda are identified by the class 'chico_manga'
        if downloadManga == True:
            allChaps = re.findall(r'<div class="chico_manga"></div>\\n<a href="+(.*?)\">+', str(urllibHTML))

            numOfChapLinks = len(allChaps)
            
            #However the 6 most recent chapters are also under the 'chico_manga' class
            #so it is necessary to pop those chapters off and if there are not a total
            #of 6 chapters in the manga we have special cases
            if numOfChapLinks < 12:

                if numOfChapLinks == 10:
                    for i in range(5):
                        allChaps.pop(0)
                    
                elif numOfChapLinks == 8:
                    for i in range(4):
                        allChaps.pop(0)

                elif numOfChapLinks == 6:
                    for i in range(3):
                        allChaps.pop(0)

                elif numOfChapLinks == 4:
                    for i in range(2):
                        allChaps.pop(0)

                elif numOfChapLinks == 2:
                    allChaps.pop(0)

                else:
                    print('There was an error parsing the HTML!')

            else:
                for i in range(6):
                    allChaps.pop(0)

            #Rather conveniently, there is a class called 'aname' which contains the name of the manga
            grabName = re.findall(r'<h2 class="aname">+(.*?)\</h2>+', str(urllibHTML))

            #some mangas contained characters in aname which cannot be used in windows directories
            #these statements attempt to make said strings directory friendly
            directorySafeName = grabName[0]
            directorySafeName = directorySafeName.replace("/", " over ")
            directorySafeName = directorySafeName.replace(":", "")
            directorySafeName = directorySafeName.replace("?", "")
            directorySafeName = directorySafeName.replace("+", "")
            directorySafeName = directorySafeName.replace("\"","'")
            directorySafeName = directorySafeName.replace("%", " Percent")
            directorySafeName = directorySafeName.replace("<", "")   
            directorySafeName = directorySafeName.replace(">", "")

            #since Windows and UNIX platforms use different directory syntax we need to know the platform
            #and adjust accordingly
            if platformType == 'Windows':
                directoryName = currentDirectory + "\\MangaPanda\\" + str(directorySafeName)

            else:
                directoryName = currentDirectory + "/MangaPanda/" + str(directorySafeName)

            try: 
                os.makedirs(directoryName)    

            except OSError:                    
                if not os.path.isdir(directoryName):
                    raise

            os.chdir(directoryName)

            #loops chapter URLs to determine chapter number for both types of URLs
            chapterNames = []
            for i in range(len(allChaps)):
                chapterNum = re.findall('((?:\d)+)', allChaps[i])
                chapterNames.append(chapterNum[-1])
            
            fullDownload = False
            while 1:
                customStart = False
                customEnd = False
                chapterFound = False
                restartMenu = False
                singleChapter = False
                startLocation = 0
                endLocation = 0

                #asks the user if they want to download all the manga or start from a certain chapter
                print('Do you wish to download the entire manga?[y/n]')
                continueChoiceFullDownload = input('')
                print()

                if continueChoiceFullDownload == 'y':
                    fullDownload = True
                    break

                elif continueChoiceFullDownload == 'n':
                    while 1:
                        print('Do you wish to start downloading from a certain chapter?[y/n]')
                        continueChoiceCustomChap = input('')
                        print()

                        if continueChoiceCustomChap == 'y':
                            print('Please enter the chapter you wish to start from.')
                            startChap = input('')
                            print()

                            for i in range(len(chapterNames)):
                                if startChap == chapterNames[i]:
                                    chapterFound = True
                                    customStart = True
                                    startLocation = i
                                    break

                            #this else is connected with the if in the for loop. If the for loop goes through all of its iterations
                            #and the if statement is never tripped then this else is tripped
                            else:
                                print("Invalid chapter number! Maybe the chapter is missing?")
                                print()
                                break

                            if chapterFound == True:
                                chapterFound = False
                                break

                        elif continueChoiceCustomChap == 'n':
                            restartMenu = True
                            break

                        elif continueChoiceCustomChap == 'q':
                            return

                        else:
                            print('Invalid Option!')
                            print()

                elif continueChoiceFullDownload == 'q':
                    return

                else:
                    print('Invalid Option!')
                    print()

                if restartMenu == True:
                    break

                if customStart == True:
                    break

            #Inquires the user where they wish to end. If they do not specify the program will run to the last chapter

            if fullDownload == False and restartMenu == False:
                while 1:
                    print('Do you wish to end the download at a certain chapter?[y/n]')
                    print('Making the end location the same as the start location will download')
                    print('only that chapter')
                    print('Choosing [n]o will download the entire manga starting from the location')
                    print('you chose above')
                    continueChoiceCustomChap = input('')
                    print()

                    if continueChoiceCustomChap == 'y':
                        print('Please enter the chapter you wish to end at.')
                        endChap = input('')
                        print()

                        if int(endChap) < int(startChap):
                            print('Invalid chapter number! Your end chapter cannot be before the start!')
                            print()

                        else:
                            for i in range(len(chapterNames)):
                                if endChap == chapterNames[i]:
                                    chapterFound = True
                                    customEnd = True
                                    endLocation = i
                                    break

                            else:
                                print('Invalid chapter number! Maybe the chapter is missing?')
                                print()

                        if chapterFound == True:
                            break

                    elif continueChoiceCustomChap == 'n':
                        break

                    elif continueChoiceCustomChap == 'q':
                        return

                    else:
                        print('Invalid Option!')
                        print()

            #once we have what chapters the user wants to download here the program modifies the chapter
            #lists that will be passed to the main for-loop to download the chapters off MangaPanda
            if customStart == True and customEnd == False:
                for i in range(startLocation):
                    allChaps.pop(0)
                    chapterNames.pop(0)

            elif customStart == True and customEnd == True:
                for i in range(startLocation):
                    allChaps.pop(0)
                    chapterNames.pop(0)

                for i in range(len(allChaps)-(int(endLocation)-int(startLocation))-1):
                    allChaps.pop(-1)
                    chapterNames.pop(-1)

            
            if fullDownload == True or customStart == True:

                for i in range(len(allChaps)):

                    if platformType == 'Windows':
                        chapDirectoryName = directoryName + "\\Chapter " + str(chapterNames[i])

                    else:
                        chapDirectoryName = directoryName + "/Chapter " + str(chapterNames[i])

                    try: 
                        os.makedirs(chapDirectoryName)    

                    except OSError:                    
                        if not os.path.isdir(chapDirectoryName):
                            raise

                    os.chdir(chapDirectoryName)

                    #There are some special cases associated with the first loop through the chapter
                    isFirstLoopPage = True

                    chapURL = "http://www.mangapanda.com" + allChaps[i]
                    print("Downloading Chapter", str(chapterNames[i]))

                    imageLocation = 0

                    while 1:
                        try:
                            imageLocation += 1

                            #Looks at page URLs for any and all sequences of numbers
                            nextChapDetermine = re.findall('((?:\d)+)', chapURL)

                            urllibHTML = urllib.request.urlopen(chapURL).read()

                            if isFirstLoopPage == True:
                                determineAmountOfPages = re.findall('<option value="+(.*?)\</option>', str(urllibHTML))

                            if len(determineAmountOfPages) == imageLocation - 1:
                                break

                            #Checks the number of files in directory in comparison to the number of images in the chapter
                            #If the number is the same the assumption is made that all images have been downloaded
                            if isFirstLoopPage == True:
                                isFirstLoopPage = False
                                numOfFileInCWD = len([name for name in os.listdir('.') if os.path.isfile(name)])
                                if numOfFileInCWD == len(determineAmountOfPages):
                                    break
                        
                            #grabs both the next page URL and the URL for the image on the current page
                            URLandIMG = re.findall(r'<div id="imgholder">+(.*?)\" name=+', str(urllibHTML))
                            nextPageURL = re.findall(r'<a href="+(.*?)\">', URLandIMG[0])
                            imageURL = re.findall(r'src="+(.*?)\"', URLandIMG[0])
                            extensionForIMG = re.findall('\.\D[^\.]+', imageURL[0])
                        
                            imageName = "Page " + str(imageLocation) + extensionForIMG[-1]
                            fileExists = os.path.isfile(imageName)

                            #Old code that would put each page thats currently downloading on a new line
                            #print("Downloading Page", imageLocation) 

                            #New code that will overwrite each "Downloading Page #" with the next page 
                            #and will eventually be overwrote by the "Downloading Chapter #"
                            print("Downloading Page %d" % imageLocation, end="", flush=True)
                            print("\r", end="", flush=True)

                            #If file does not already exist, opens a file, writes image binary data to it and closes
                            if fileExists == False:
                                rawImage = urllib.request.urlopen(imageURL[0]).read()
                                fout = open(imageName, 'wb')       
                                fout.write(rawImage)                          
                                fout.close()
                        
                            chapURL = "http://www.mangapanda.com" + nextPageURL[0]

                        #Probably need to do more with this error
                        except:
                            print('                           ')
                            print("Invalid URL Error!")
                            return
            
                while 1:
                    print('Do you wish to download another manga?[y/n]')
                    continueChoice = input('')
                    print()

                    if continueChoice == 'y':
                        break

                    elif continueChoice == 'n':
                        success = True
                        break

                    elif continueChoice == 'q':
                        return

                    else:
                        print('Invalid Option!')

main()
