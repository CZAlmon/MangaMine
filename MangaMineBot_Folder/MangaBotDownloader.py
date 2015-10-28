#Ver. 0.0.7
#Author: Zach Almon

import urllib.request
import re
import os
import platform
import sys
import string
import html
import time

platformType = platform.system()


def Batoto(link_to_manga_site):

    success = False

    currentDirectory = os.getcwd()
    if platformType == 'Windows':
        MASTERdirectoryName = currentDirectory + "\\Batoto"
    else:
        MASTERdirectoryName = currentDirectory + "/Batoto"

    try: 
        os.makedirs(MASTERdirectoryName)
    except OSError:                    
        if not os.path.isdir(MASTERdirectoryName):
            raise

    #MASTERdirectoryName is the Variable that will keep the program downloading
    #Different Manga to the same Batoto Folder
    os.chdir(MASTERdirectoryName)

    type_one_manga = False
    type_two_manga = False
    

    try:
        urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
    except:
        print('Request 1 Failed. Trying again in 30 seconds.')
        time.sleep(30)

        try:
            urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
        except:
            print('Request 2 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
            except:
                print('Request 3 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
                except:
                    print('Request 4 Failed. Moving onto the Next manga.')
                    print('This was the First Main Request that Failed.')
                    return
    
        

    Manga_Title = re.findall(r'<title>+(.*?)- Scanlations', str(urllibHTML))

    if len(Manga_Title) == 0:
        print("Title not found. URL or HTML Error.")
        return
            
    Manga_Title_string = Manga_Title[0]
    Manga_Title_string = Manga_Title_string[:-1]

    Manga_Title_string = re.sub(r'\\x\w{2}', r' ', Manga_Title_string)
            
    #Python 3.4 Converts '&amp;' Type things to their string equivelant. 
    Manga_Title_string = html.unescape(Manga_Title_string)

    #Get rid of Non-Functioning characters for Filenames
    directorySafeName = Manga_Title_string
    directorySafeName = directorySafeName.replace("/", " over ")
    directorySafeName = directorySafeName.replace(":", "")
    directorySafeName = directorySafeName.replace("?", "")
    directorySafeName = directorySafeName.replace("+", " plus ")
    directorySafeName = directorySafeName.replace("\"","'")
    directorySafeName = directorySafeName.replace("%", " Percent ")
    directorySafeName = directorySafeName.replace("<", "")   
    directorySafeName = directorySafeName.replace(">", "")

    Manga_Title_string = directorySafeName

    
    print("Downloading", Manga_Title_string)


    #For any other language on Bato.to change lang_English to whatever matches the language you desire. 
    #Then this file *SHOULD* work with your language. It is Untested as anything else but english
    allENGLISHChaps = re.findall(r'lang_English+(.*?)\ title="+', str(urllibHTML))
            
    if len(allENGLISHChaps) == 0:
        print("Manga has no English Chapters or there was an error reading the HTML!")
        return
    else:
        First_chapter_string = allENGLISHChaps[-1]
        First_chapter_address = re.findall(r'href=\"+(.*?)\"', First_chapter_string)
        First_chapter_address_string = First_chapter_address[0]
                
        try:
            First_chapter_html = urllib.request.urlopen(First_chapter_address_string).read()
        except:
            print('Request 1 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                First_chapter_html = urllib.request.urlopen(First_chapter_address_string).read()
            except:
                print('Request 2 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    First_chapter_html = urllib.request.urlopen(First_chapter_address_string).read()
                except:
                    print('Request 3 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        First_chapter_html = urllib.request.urlopen(First_chapter_address_string).read()
                    except:
                        print('Request 4 Failed. Moving onto the Next manga.')
                        print('This was the Second Main Request that Failed.')
                        return
        
        


        type_one_padding_right = re.search("<div style=\"text-align:center;\">", str(First_chapter_html))
        type_two_comic_page = re.search("comic_page", str(First_chapter_html))


        #Type one is All images on One Page
        if type_one_padding_right != None:
            type_one_manga = True
        #Type two is All images on seperate pages
        elif type_two_comic_page != None:
            type_two_manga = True
        else:
            print("There was an error with the Manga Type!")
            return

                    
        #This will get the chapter links from the Select options on the chapters first page
        #There are 2 select options (one at top and one at bottom
        #They are same so its arbutrary which you pick. I Will be selecting [0]
        get_Chapters = re.findall(r'250px;">+(.*?)</select>', str(First_chapter_html))

        chapter_master_string = get_Chapters[0]

        list_of_Chapter_Links = []

        #Get all chapter links. Last thing in list is an unneeded "selected" string. Pop that off.
        list_of_Chapter_Links = re.findall(r'\"+(.*?)\"', chapter_master_string)

        #In this list there may be a "selected". It may or may not be at the end. The loop solves it.
        #I am 95% sure there will only ever be 1 "selected" per list.
        #list_of_Chapter_Links.pop(-1)
        for i in range(len(list_of_Chapter_Links)):
            if list_of_Chapter_Links[i] == "selected":
                list_of_Chapter_Links.pop(i)
                break

        #Get Numbers of the chapters. Will be "Matched" up to the list_of_Chapter_Links.
        list_of_Chapter_Numbers_raw = re.findall(r'Ch\.+(.*?)<', chapter_master_string)
        list_of_chapter_names_refined = []

        #Some chapters may be like "230: Title of Chapter" Some may be "145"
        for i in range(len(list_of_Chapter_Numbers_raw)):
            temp_list = re.findall('^(.*?):', list_of_Chapter_Numbers_raw[i])

            if len(temp_list) == 0:
                list_of_chapter_names_refined.append(list_of_Chapter_Numbers_raw[i])
            elif len(temp_list) == 1:
                list_of_chapter_names_refined.append(temp_list[0])
            else:
                print("Manga Chapter Name Error!")
                return
                    


        list_of_Chapter_Links_Final = list_of_Chapter_Links
        list_of_Chapter_Numbers_Final = list_of_chapter_names_refined
                    
        list_of_Chapter_Links_Final.reverse()
        list_of_Chapter_Numbers_Final.reverse()
        
        fullDownload = True

        #Because there are duplicates I must check and add a v2 or v3 if it is in there more times

        temp_name = []
        temp_name_str = ''

        for i in range(len(list_of_Chapter_Numbers_Final)):
            if list_of_Chapter_Numbers_Final[i] in temp_name:

                #At this point there are duplicates. The chapters may not be in order.
                #This is the only method I can come up with to deal with duplicates
                #   that may be out of order.

                temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v2'
                if temp_name_str in temp_name:
                    temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v3'
                    if temp_name_str in temp_name:
                        temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v4'
                        if temp_name_str in temp_name:
                            temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v5'
                            if temp_name_str in temp_name:
                                temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v6'
                                if temp_name_str in temp_name:
                                    temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v7'
                                    if temp_name_str in temp_name:
                                        temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v8'
                                        if temp_name_str in temp_name:
                                            temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v9'
                                            if temp_name_str in temp_name:
                                                temp_name_str = list_of_Chapter_Numbers_Final[i] + ' v10'
                                                #If there are more then 10 dulicates I can't help you

                temp_name.append(temp_name_str)

                            
            else:
                temp_name.append(list_of_Chapter_Numbers_Final[i])
         
                                   
        list_of_Chapter_Numbers_Final = temp_name                           


        currentDirectory = MASTERdirectoryName

        if platformType == 'Windows':
            manga_directory_name = currentDirectory + "\\" + Manga_Title_string
        else:
            manga_directory_name = currentDirectory + "/" + Manga_Title_string

        try: 
            os.makedirs(manga_directory_name)    
        except OSError:                    
            if not os.path.isdir(manga_directory_name):
                raise

        os.chdir(manga_directory_name)
                    
    #Main Loop for Downloading Images.         
        for i in range(len(list_of_Chapter_Numbers_Final)):
                        
            first_page_of_each_chapter = True
            chapter_number = list_of_Chapter_Numbers_Final[i]
            chapter_link = list_of_Chapter_Links_Final[i]

                            
            if platformType == 'Windows':
                chapDirectoryName = manga_directory_name + "\\Chapter " + chapter_number
            else:
                chapDirectoryName = manga_directory_name + "/Chapter " + chapter_number

            try: 
                os.makedirs(chapDirectoryName)    
            except OSError:                    
                if not os.path.isdir(chapDirectoryName):
                    raise

            os.chdir(chapDirectoryName)

            print("Downloading Chapter", chapter_number)


            try:
                urllibHTML = urllib.request.urlopen(list_of_Chapter_Links_Final[i]).read()
            except:
                print('Request 1 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(list_of_Chapter_Links_Final[i]).read()
                except:
                    print('Request 2 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        urllibHTML = urllib.request.urlopen(list_of_Chapter_Links_Final[i]).read()
                    except:
                        print('Request 3 Failed. Trying again in 30 seconds.')
                        time.sleep(30)

                        try:
                            urllibHTML = urllib.request.urlopen(list_of_Chapter_Links_Final[i]).read()
                        except:
                            print('Request 4 Failed. Moving onto the Next manga.')
                            print('This was the Chapter Request that Failed.')
                            return
            
                            
            if type_one_manga == True:
                get_images = re.findall(r'text-align:center;">+(.*?)</div><div', str(urllibHTML))
                get_images_master_string = get_images[0]
                image_file_name_list = re.findall(r"<img src=\\'(.*?)\\'", str(get_images_master_string))

                Amount_of_pages = len(image_file_name_list)

                for j in range(len(image_file_name_list)):

                    if first_page_of_each_chapter == True:
                        first_page_of_each_chapter = False
                        numOfFileInCWD = len([name for name in os.listdir('.') if os.path.isfile(name)])
                        if numOfFileInCWD == Amount_of_pages:
                            break

                    image_file_name = image_file_name_list[j]
                    image_file_extension_list = re.findall(r'(\.\D[^\.]+)', image_file_name)
                    image_file_extension = image_file_extension_list[-1]

                    imageName = "Page " + str(j+1) + image_file_extension

                    print("Downloading Page %d" % (j+1), end="", flush=True)
                    print("\r", end="", flush=True)

                    fileExists = os.path.isfile(imageName)
                    #If file does not already exist, opens a file, writes image binary data to it and closes
                    if fileExists == False:

                        image_worked = True

                        try:
                            rawImage = urllib.request.urlopen(image_file_name).read()
                        except:
                            print('Request 1 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                rawImage = urllib.request.urlopen(image_file_name).read()
                            except:
                                print('Request 2 Failed. Trying again in 30 seconds.')
                                time.sleep(30)

                                try:
                                    rawImage = urllib.request.urlopen(image_file_name).read()
                                except:
                                    print('Request 3 Failed. Trying again in 30 seconds.')
                                    time.sleep(30)

                                    try:
                                        rawImage = urllib.request.urlopen(image_file_name).read()
                                    except:
                                        print('Request 4 Failed. Moving onto the Next image.')
                                        image_worked = False
                        
                        if image_worked:
                            fout = open(imageName, 'wb')       
                            fout.write(rawImage)                          
                            fout.close()

                    #   I will leave this here in case you feel the need to slow down your requests to the website/server
                    # just incase something bad could happen. All you need to do is delete the # 3 lines below  
                    # and the program will sleep for 2 seconds after each page is downloaded. You can add more time if you wish
                    #
                    #time.sleep(2)
                            
            elif type_two_manga == True:
                #Get the pages between "<id..." and "</se..."
                get_Pages = re.findall(r'id="page_select" onchange="window.location=this.value;">+(.*?)</select></li>', str(urllibHTML))
                #There will be Two found
                Pages_master_string = get_Pages[0]

                #Get all page links. Second thing in list is an unneeded "selected" string. Loop to get rid
                list_of_page_Links = re.findall(r'\"+(.*?)\"', Pages_master_string)

                list_of_page_links_final = []
                #Loop to rid of the "Selected" part of list
                for j in range(len(list_of_page_Links)):
                    if list_of_page_Links[j] != "selected":
                        list_of_page_links_final.append(list_of_page_Links[j])
    
                Amount_of_pages = len(list_of_page_links_final)
                                
                for j in range(len(list_of_page_links_final)):
                
                    print("Downloading Page %d" % (j+1), end="", flush=True)
                    print("\r", end="", flush=True)

                    #Check for First page. Checks to see if anything is already downloaded
                    if first_page_of_each_chapter == True:
                        first_page_of_each_chapter = False
                        numOfFileInCWD = len([name for name in os.listdir('.') if os.path.isfile(name)])
                        if numOfFileInCWD == Amount_of_pages:
                            break
                        #At this point There will be something you need to download.
                        #Since we already have the HTML for the first page of EACH Chapter
                        #We dont need to waste time to read that again, set it here.
                        page_urllibHTML = urllibHTML
                    else:

                        try:
                            page_urllibHTML = urllib.request.urlopen(list_of_page_links_final[j]).read()
                        except:
                            print('Request 1 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                page_urllibHTML = urllib.request.urlopen(list_of_page_links_final[j]).read()
                            except:
                                print('Request 2 Failed. Trying again in 30 seconds.')
                                time.sleep(30)

                                try:
                                    page_urllibHTML = urllib.request.urlopen(list_of_page_links_final[j]).read()
                                except:
                                    print('Request 3 Failed. Trying again in 30 seconds.')
                                    time.sleep(30)

                                    try:
                                        page_urllibHTML = urllib.request.urlopen(list_of_page_links_final[j]).read()
                                    except:
                                        print('Request 4 Failed. Moving onto the Next manga.')
                                        print('This was the Page Request that Failed.')
                                        return
                        

                    #Get Image URL
                    image_file_name_list = re.findall(r'comic_page" style="max-width: 100%;" src="(.*?)"', str(page_urllibHTML))
                    image_file_name = image_file_name_list[0]
                    #CHECK EXTENSION. Bato.to Could use .png or .jpg or .jpeg
                    image_file_extension_list = re.findall(r'(\.\D[^\.]+)', image_file_name)
                    image_file_extension = image_file_extension_list[-1]

                    imageName = "Page " + str(j+1) + image_file_extension
                    fileExists = os.path.isfile(imageName)

                    #If file does not already exist, opens a file, writes image binary data to it and closes
                    if fileExists == False:

                        image_worked = True

                        try:
                            rawImage = urllib.request.urlopen(image_file_name).read()
                        except:
                            print('Request 1 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                rawImage = urllib.request.urlopen(image_file_name).read()
                            except:
                                print('Request 2 Failed. Trying again in 30 seconds.')
                                time.sleep(30)

                                try:
                                    rawImage = urllib.request.urlopen(image_file_name).read()
                                except:
                                    print('Request 3 Failed. Trying again in 30 seconds.')
                                    time.sleep(30)

                                    try:
                                        rawImage = urllib.request.urlopen(image_file_name).read()
                                    except:
                                        print('Request 4 Failed. Moving onto the Next image.')
                                        image_worked = False

                        if image_worked:
                            fout = open(imageName, 'wb')       
                            fout.write(rawImage)                          
                            fout.close()
                    
                    #   I will leave this here in case you feel the need to slow down your requests to the website/server
                    # just incase something bad could happen. All you need to do is delete the # 3 lines below  
                    # and the program will sleep for 2 seconds after each page is downloaded. You can add more time if you wish
                    #
                    #time.sleep(2)

            else:
                print("Manga Type Error!")
                return

    return


def MangaPanda(link_to_manga_site):

    success = False
    currentDirectory = os.getcwd()
    downloadMangaListOnce = False
    


    does_it_have_dot_html = re.findall(r'(\.html)', link_to_manga_site)

    if len(does_it_have_dot_html) == 0:
        pass
    else:
        link_to_manga_site = link_to_manga_site[:-5]

    try:
        urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
    except:
        print('Request 1 Failed. Trying again in 30 seconds.')
        time.sleep(30)

        try:
            urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
        except:
            print('Request 2 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
            except:
                print('Request 3 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
                except:
                    print('Request 4 Failed. Moving onto the Next manga.')
                    print('This was the First Main Request that Failed.')
                    return

            
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

    if len(grabName) == 0:
        print("Title not found. URL or HTML Error.")
        return


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

    print("Downloading", directorySafeName)


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
            
            imageLocation += 1

            #Looks at page URLs for any and all sequences of numbers
            nextChapDetermine = re.findall('((?:\d)+)', chapURL)


            try:
                urllibHTML = urllib.request.urlopen(chapURL).read()
            except:
                print('Request 1 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(chapURL).read()
                except:
                    print('Request 2 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        urllibHTML = urllib.request.urlopen(chapURL).read()
                    except:
                        print('Request 3 Failed. Trying again in 30 seconds.')
                        time.sleep(30)

                        try:
                            urllibHTML = urllib.request.urlopen(chapURL).read()
                        except:
                            print('Request 4 Failed. Moving onto the Next manga.')
                            print('This was the Chapter Request that Failed.')
                            return

           

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
                        

            #Waiting till next request. MangaPanda doesn't like alot of requests in a short time period.
            time.sleep(1)


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

                image_worked = True

                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

                url = imageURL[0]

                headers={'User-Agent':user_agent,} 

                request = urllib.request.Request(url,None,headers)
                

                try:
                    rawImage = urllib.request.urlopen(request).read()
                except:
                    print('Request 1 Failed. Trying again in 10 seconds.')
                    time.sleep(10)

                    try:
                        rawImage = urllib.request.urlopen(request).read()
                    except:
                        print('Request 2 Failed. Trying again in 10 seconds.')
                        time.sleep(10)

                        try:
                            rawImage = urllib.request.urlopen(request).read()
                        except:
                            print('Request 3 Failed. Trying again in 10 seconds.')
                            time.sleep(10)

                            try:
                                rawImage = urllib.request.urlopen(request).read()
                            except:
                                print('Request 4 Failed. Moving onto the Next image.')
                                image_worked = False

                if image_worked:
                    fout = open(imageName, 'wb')       
                    fout.write(rawImage)                          
                    fout.close()
                        
            chapURL = "http://www.mangapanda.com" + nextPageURL[0]

            #   I will leave this here in case you feel the need to slow down your requests to the website/server
            # just incase something bad could happen. All you need to do is delete the # 3 lines below  
            # and the program will sleep for 2 seconds after each page is downloaded. You can add more time if you wish
            #
            #time.sleep(2)

        #Time between chapters as well
        #time.sleep(1)

           
            
    return


def MangaHere(link_to_manga_site):

    success = False

    Search_feature = False

    currentDirectory = os.getcwd()

    
    if platformType == 'Windows':
        directoryName = currentDirectory + "\\MangaHere"
    else:
        directoryName = currentDirectory + "/MangaHere"

    try: 
        os.makedirs(directoryName)
    except OSError:                    
        if not os.path.isdir(directoryName):
            raise

    os.chdir(directoryName)

    #downloadMangaListOnce = False
    downloadManga = False

    
    try:
        urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
    except:
        print('Request 1 Failed. Trying again in 30 seconds.')
        time.sleep(30)

        try:
            urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
        except:
            print('Request 2 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
            except:
                print('Request 3 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
                except:
                    print('Request 4 Failed. Moving onto the Next manga.')
                    print('This was the First Main Request that Failed.')
                    return

     
    allChaps = re.findall(r'     <a class="color_0077" href="(.*?)"', str(urllibHTML))
    allChaps.reverse()

    numOfChapLinks = len(allChaps)

    mangaName = re.findall(r' <h1 class="title"><span class="title_icon"></span>(.*?)</h1>', str(urllibHTML))

    try:
        directorySafeName = mangaName[0]

    except:
        print('Invalid URL!')
        return

    #Python 3.4 Converts '&amp;' Type things to their string equivalent. 
    directorySafeName = html.unescape(directorySafeName)

    #Get rid of Non-Functioning characters for Filenames
    directorySafeName = directorySafeName.replace("/", " over ")
    directorySafeName = directorySafeName.replace(":", "")
    directorySafeName = directorySafeName.replace("?", "")
    directorySafeName = directorySafeName.replace("+", " plus ")
    directorySafeName = directorySafeName.replace("\"","'")
    directorySafeName = directorySafeName.replace("%", " Percent ")
    directorySafeName = directorySafeName.replace("<", "")   
    directorySafeName = directorySafeName.replace(">", "")

    directorySafeName = re.sub(r'\\x\w{2}', r' ', directorySafeName)
    directorySafeName = re.sub(r"\\'", r"'", directorySafeName)

    directorySafeName = directorySafeName.title()


    print("Downloading", directorySafeName)

    
    if platformType == 'Windows':
        directoryName = directoryName + "\\" + directorySafeName
    else:
        directoryName = directoryName + "/" + directorySafeName

    try: 
        os.makedirs(directoryName)
    except OSError:                    
        if not os.path.isdir(directoryName):
            raise

    os.chdir(directoryName)

    for i in allChaps:

        skipBool1 = False
        skipBool2 = False
        firstLoop = True
        currentPage = 0
        volChapDirectoryString = ""

        findVolume = re.findall(r'v\d{2}.\d+' , i)
        findChap = re.findall(r'c\d{3}.\d+' , i)
                
        if len(findVolume) == 0:
            findVolume = re.findall(r'v\d{2}', i)

            try:
                volTempString = re.findall(r'\d{2}', findVolume[0])

            except:
                skipBool1 = True
                    
            if skipBool1 == False:
                volTempString = str(int(volTempString[0]))
                volChapDirectoryString = volChapDirectoryString + 'Vol. ' + volTempString + ' '

        else:
            volTempString = re.findall(r'\d{2}.\d+', findVolume[-1])
            volTempString = str(float(volTempString[0]))
            volChapDirectoryString = volChapDirectoryString + 'Vol. ' + volTempString + ' '

        if len(findChap) == 0:
            findChap = re.findall(r'c\d{3}', i)

            try:
                chapTempString = re.findall(r'\d{3}', findChap[0])

            except:
                skipBool2 = True

            if skipBool2 == False:
                chapTempString = str(int(chapTempString[0]))
                volChapDirectoryString = volChapDirectoryString + 'Chap. ' + chapTempString

        else:
            chapTempString = re.findall(r'\d{3}.\d+', findChap[-1])
            chapTempString = str(float(chapTempString[0]))
            volChapDirectoryString = volChapDirectoryString + 'Chap. ' + chapTempString

        if volChapDirectoryString == "":
            print('An error has occured getting chapter or volume number!')
            return 1

        print('Downloading', volChapDirectoryString)

        if platformType == 'Windows':
            volChapDirectoryName = directoryName + "\\" + volChapDirectoryString
        else:
            volChapDirectoryName = directoryName + "/" + volChapDirectoryString

        try: 
            os.makedirs(volChapDirectoryName)
        except OSError:                    
            if not os.path.isdir(volChapDirectoryName):
                raise

        os.chdir(volChapDirectoryName)
                
        try:
            urllibIMG = str(urllib.request.urlopen(i).read())
        except:
            print('Request 1 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                urllibIMG = str(urllib.request.urlopen(i).read())
            except:
                print('Request 2 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibIMG = str(urllib.request.urlopen(i).read())
                except:
                    print('Request 3 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        urllibIMG = str(urllib.request.urlopen(i).read())
                    except:
                        print('Request 4 Failed. Moving onto the Next manga.')
                        print('This was the Chapter Request that Failed.')
                        return

        


        trimHTML = re.findall('<select id="top_chapter_list"(.*?)read_img', urllibIMG)

        try:
            allPageURLs = re.findall('<option value="(.*?)" ', trimHTML[-1])

        except:
            print('Something went wrong when trying to find the page URL\'s!')
            print('This manga cannot be downloaded at this time.')
            return
                
        for k in allPageURLs:
            currentPage += 1
            skipPage = False

            if firstLoop == False:
                #urllibReq = urllib.request.Request(k, None, {}, None, True,'POST')
                urllibReq = urllib.request.Request(k)
                urllibReq.method = 'POST'


                try:
                    urllibIMG = str(urllib.request.urlopen(urllibReq).read())
                except:
                    print('Request 1 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        urllibIMG = str(urllib.request.urlopen(urllibReq).read())
                    except:
                        print('Request 2 Failed. Trying again in 30 seconds.')
                        time.sleep(30)

                        try:
                            urllibIMG = str(urllib.request.urlopen(urllibReq).read())
                        except:
                            print('Request 3 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                urllibIMG = str(urllib.request.urlopen(urllibReq).read())
                            except:
                                print('Request 4 Failed. Moving onto the Next manga.')
                                print('This was the Page Request that Failed.')
                                return


                

            if firstLoop == True:
                firstLoop = False
                numOfFileInCWD = len([name for name in os.listdir('.') if os.path.isfile(name)])
                if numOfFileInCWD == len(allPageURLs):
                    break

            print("Downloading Page %d" % currentPage, end="", flush=True)
            print("\r", end="", flush=True)

            #textFile = open("HTMLFile " + str(currentPage) + ".HTML", "w")
            #textFile.write(urllibIMG)
            #textFile.close()

            imageURL = re.findall('<img src="(.*?)" onerror="', urllibIMG)

            try:
                extensionForIMG = re.findall('\.[a-z]{3}', imageURL[0])

            except:
                print('Page ' + str(currentPage) + ' could not be downloaded!')
                skipPage = True

            if skipPage == False:    
                imageName = "Page " + str(currentPage) + extensionForIMG[-1]
                fileExists = os.path.isfile(imageName)

                if fileExists == False:

                    image_worked = True

                    try:
                        rawImage = urllib.request.urlopen(imageURL[0]).read()
                    except:
                        print('Request 1 Failed. Trying again in 30 seconds.')
                        time.sleep(30)

                        try:
                            rawImage = urllib.request.urlopen(imageURL[0]).read()
                        except:
                            print('Request 2 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                rawImage = urllib.request.urlopen(imageURL[0]).read()
                            except:
                                print('Request 3 Failed. Trying again in 30 seconds.')
                                time.sleep(30)

                                try:
                                    rawImage = urllib.request.urlopen(imageURL[0]).read()
                                except:
                                    print('Request 4 Failed. Moving onto the Next image.')
                                    image_worked = False

                    
                    if image_worked:                   
                        fout = open(imageName, 'wb')       
                        fout.write(rawImage)                          
                        fout.close()

            #   I will leave this here in case you feel the need to slow down your requests to the website/server
            # just incase something bad could happen. All you need to do is delete the # 3 lines below  
            # and the program will sleep for 2 seconds after each page is downloaded. You can add more time if you wish
            #
            #time.sleep(2)

    return


def MangaStream(link_to_manga_site):

    success = False

    currentDirectory = os.getcwd()

    if platformType == 'Windows':
        MASTERdirectoryName = currentDirectory + "\\MangaStream"
    else:
        MASTERdirectoryName = currentDirectory + "/Mangastream"

    try: 
        os.makedirs(MASTERdirectoryName)
    except OSError:                    
        if not os.path.isdir(MASTERdirectoryName):
            raise

    #MASTERdirectoryName is the Variable that will keep the program downloading
    #Different Manga to the same Mangastream Folder
    os.chdir(MASTERdirectoryName)

    try:
        urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
    except:
        print('Request 1 Failed. Trying again in 30 seconds.')
        time.sleep(30)

        try:
            urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
        except:
            print('Request 2 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
            except:
                print('Request 3 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(link_to_manga_site).read()
                except:
                    print('Request 4 Failed. Moving onto the Next manga.')
                    print('This was the First Main Request that Failed.')
                    return
       

    Manga_Title = re.findall(r'<title>(.*?) Manga', str(urllibHTML))

    if len(Manga_Title) == 0:
        print("Title not found. URL or HTML Error.")
        return

    Manga_Title_string = Manga_Title[0]

    Manga_Title_string = re.sub(r'\\x\w{2}', r' ', Manga_Title_string)
            
    #Python 3.4 Converts '&amp;' Type things to their string equivelant. 
    Manga_Title_string = html.unescape(Manga_Title_string)

    #Get rid of Non-Functioning characters for Filenames
    directorySafeName = Manga_Title_string
    directorySafeName = directorySafeName.replace("/", " over ")
    directorySafeName = directorySafeName.replace(":", "")
    directorySafeName = directorySafeName.replace("?", "")
    directorySafeName = directorySafeName.replace("+", " plus ")
    directorySafeName = directorySafeName.replace("\"", "'")
    directorySafeName = directorySafeName.replace("\'", "'")
    directorySafeName = directorySafeName.replace("\\'", "'")
    directorySafeName = directorySafeName.replace("\\", "")
    directorySafeName = directorySafeName.replace("%", " Percent ")
    directorySafeName = directorySafeName.replace("<", "")   
    directorySafeName = directorySafeName.replace(">", "")

    Manga_Title_string = directorySafeName

    print("Downloading", Manga_Title_string)



    all_chaps_list = re.findall('<th style="width: 70%">Chapter<\/th>\\\\n<th style="width: 30%">Released<\/th>\\\\n<\/tr>\\\\n<tr>\\\\n(.*?)<\/table>', str(urllibHTML), re.DOTALL)

    all_chaps_str = all_chaps_list[0]

    chapter_list_tuples = re.findall(r'href="(.*?)">(.*?)</a>', str(all_chaps_str))

    chapter_names = []
    chapter_links = []
            
    for i in range(len(chapter_list_tuples)):
        chapter_links.append(chapter_list_tuples[i][0])
        chapter_names.append(chapter_list_tuples[i][1])

            
    #Start Manga Downloading

    currentDirectory = MASTERdirectoryName

    if platformType == 'Windows':
        manga_directory_name = currentDirectory + "\\" + Manga_Title_string
    else:
        manga_directory_name = currentDirectory + "/" + Manga_Title_string

    try: 
        os.makedirs(manga_directory_name)    
    except OSError:                    
        if not os.path.isdir(manga_directory_name):
            raise

    os.chdir(manga_directory_name)

    for i in range(len(chapter_names)):

        first_chapter_bool = True

        chapter_link_string = chapter_links[i]
        chapter_name_string = chapter_names[i]
        chapDirectoryName = ''


        chapter_name_string = re.sub(r'\\x\w{2}', r' ', chapter_name_string)
            
        #Python 3.4 Converts '&amp;' Type things to their string equivelant. 
        #chapter_name_string = html.unescape(chapter_name_string)

        #Get rid of Non-Functioning characters for Filenames
        directorySafeName = chapter_name_string
        directorySafeName = directorySafeName.replace("/", " over ")
        directorySafeName = directorySafeName.replace(":", "")
        directorySafeName = directorySafeName.replace("?", "")
        directorySafeName = directorySafeName.replace("+", " plus ")
        directorySafeName = directorySafeName.replace("\"", "'")
        directorySafeName = directorySafeName.replace("\'", "'")
        directorySafeName = directorySafeName.replace("\\'", "'")
        directorySafeName = directorySafeName.replace("\\", "")
        directorySafeName = directorySafeName.replace("%", " Percent ")
        directorySafeName = directorySafeName.replace("<", "")   
        directorySafeName = directorySafeName.replace(">", "")

        chapter_name_string = directorySafeName



        if platformType == 'Windows':
            chapDirectoryName = manga_directory_name + "\\Chapter " + chapter_name_string
        else:
            chapDirectoryName = manga_directory_name + "/Chapter " + chapter_name_string

        try: 
            os.makedirs(chapDirectoryName)    
        except OSError:                    
            if not os.path.isdir(chapDirectoryName):
                raise

        os.chdir(chapDirectoryName)

        print("Downloading Chapter", chapter_name_string)

        try:
            urllibHTML = urllib.request.urlopen(chapter_link_string).read()
        except:
            print('Request 1 Failed. Trying again in 30 seconds.')
            time.sleep(30)

            try:
                urllibHTML = urllib.request.urlopen(chapter_link_string).read()
            except:
                print('Request 2 Failed. Trying again in 30 seconds.')
                time.sleep(30)

                try:
                    urllibHTML = urllib.request.urlopen(chapter_link_string).read()
                except:
                    print('Request 3 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        urllibHTML = urllib.request.urlopen(chapter_link_string).read()
                    except:
                        print('Request 4 Failed. Moving onto the Next manga.')
                        print('This was the Chapter Request that Failed.')
                        return

        page_list_raw = re.findall(r'<ul class="dropdown-menu">(.*?)</ul>', str(urllibHTML), re.DOTALL)

        page_list_string = page_list_raw[-1]

        list_of_some_of_the_pages = re.findall(r'href="(.*?)">', str(page_list_string))

        final_page = list_of_some_of_the_pages[-1]

        number_of_pages_list = re.findall(r'http://readms.com/r/.*?/.*?/\d+/(\d+)', final_page)

        number_of_pages = int(number_of_pages_list[0])

        chapter_url_list = re.findall(r'(http://readms.com/r/.*?/.*?/\d+/)\d+', final_page)

        chapter_url = chapter_url_list[0]

        for j in range(number_of_pages):

            if j == 0:
                numOfFileInCWD = len([name for name in os.listdir('.') if os.path.isfile(name)])
                if numOfFileInCWD == number_of_pages:
                    break

            print("Downloading Page %d" % (j+1), end="", flush=True)
            print("\r", end="", flush=True)

            if first_chapter_bool:

                first_chapter_bool = False
                page_urllibHTML = urllibHTML

            else:
                try:
                    page_urllibHTML = urllib.request.urlopen(chapter_url + str(j+1)).read()
                except:
                    print('Request 1 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        page_urllibHTML = urllib.request.urlopen(chapter_url + str(j+1)).read()
                    except:
                        print('Request 2 Failed. Trying again in 30 seconds.')
                        time.sleep(30)

                        try:
                            page_urllibHTML = urllib.request.urlopen(chapter_url + str(j+1)).read()
                        except:
                            print('Request 3 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                page_urllibHTML = urllib.request.urlopen(chapter_url + str(j+1)).read()
                            except:
                                print('Request 4 Failed. Moving onto the Next manga.')
                                print('This was the Page Request that Failed.')
                                return
                
                       
            image_file_name_list = re.findall(r'<img id="manga-page" src="(.*?)"/></a>', str(page_urllibHTML))

            image_file_name = image_file_name_list[0]

            #CHECK EXTENSION. Mangastream Could use .png or .jpg or .jpeg
            image_file_extension_list = re.findall(r'(\.\D[^\.]+)', image_file_name)
            image_file_extension = image_file_extension_list[-1]

            imageName = "Page " + str(j+1) + image_file_extension

            fileExists = os.path.isfile(imageName)

            #If file does not already exist, opens a file, writes image binary data to it and closes
            if fileExists == False:

                image_worked = True

                try:
                    rawImage = urllib.request.urlopen(image_file_name).read()
                except:
                    print('Request 1 Failed. Trying again in 30 seconds.')
                    time.sleep(30)

                    try:
                        rawImage = urllib.request.urlopen(image_file_name).read()
                    except:
                        print('Request 2 Failed. Trying again in 30 seconds.')
                        time.sleep(30)

                        try:
                            rawImage = urllib.request.urlopen(image_file_name).read()
                        except:
                            print('Request 3 Failed. Trying again in 30 seconds.')
                            time.sleep(30)

                            try:
                                rawImage = urllib.request.urlopen(image_file_name).read()
                            except:
                                print('Request 4 Failed. Moving onto the Next image.')
                                image_worked = False

                if image_worked:
                    fout = open(imageName, 'wb')       
                    fout.write(rawImage)                          
                    fout.close()
            

            #
            #   Here may be a problem. After the program gets done with downloading a single page you may
            # want to artifically slow the program down so you don't anger the website/server hosts with
            # too many requests. A small test i did with good internet was 100 downloaded pages (around 4 chapters)
            # in a minute. Which would have been over 200 urllib requests to mangastream's website in under a minute.
            #   I will leave this here in case you feel the need to slow down your requests to the website/server
            # just incase something bad could happen. All you need to do is delete the # 3 lines below  
            # and the program will sleep for 2 seconds after each page is downloaded. You can add more time if you wish
            #
            #time.sleep(2)

    return


#FULL DOWNLOAD. NO OPTIONS. THIS IS A BOT TO RUN 24/7 TO CHECK FOR UPDATES



def main():

    #Time Run 5 Times over a ten hour period, once every 2 hours.
    #   Then wait a week. and Repeat. 2 Hours = 7200 ::: 1 week = 604800

    

    currentDirectory = os.getcwd()

    if platformType == 'Windows':
        Main_Directory = currentDirectory + "\\Manga_Bot_Folder"
    else:
        Main_Directory = currentDirectory + "/Manga_Bot_Folder"

    try: 
        os.makedirs(Main_Directory)
    except OSError:                    
        if not os.path.isdir(Main_Directory):
            raise

    os.chdir(Main_Directory)

    Main_Directory = os.getcwd()



    counter = 0

    #To add more items to any list
    #   '', '', '', '', '', '', '', ''
    #
    # Lists must Look like this:
    #
    # batoto_manga = ['http://bato.to/comic/_/comics/one-piece-r39']
    #
    # with comma's between each link. Links can all be on one line or to make it neater, each link on its own line (See test list)
    # 
    # Links must be to the manga's top page of each website. Examples:
    # Bato: http://bato.to/comic/_/comics/one-piece-r39
    # MangaPanda: http://www.mangapanda.com/one-piece
    # MangaStream: http://mangastream.com/manga/one_piece
    # MangaHere: http://www.mangahere.co/manga/one_piece/


    #This is a List to test things/manga/url or anything else
    #tests_list = ['', 
    #              '']

    batoto_manga = []

    mangahere_manga = []

    mangapanda_manga = []

    mangastream_manga = []


    while True:
        
        #This is a loop to test things/manga/url or anything else
        #print("Downloading Manga From TEST:\n")
        #for i in range(len(tests_list)):
        #    os.chdir(Main_Directory)
        #   #Change this call to whatever mangasite you are testing
        #    MangaHere(tests_list[i])
        #    #Batoto()
        #    #MangaPanda()
        #    #MangaStream()
        #    print('\n')

        ### PLEASE READ ###
        #Batoto has implemented anti-bot crawling measures. I would recommend you find the desired manga on 
        #   MangaHere or MangaPanda. I will leave this here, but I would recommend leaving the list blank/empty.
        print("Downloading Manga From Batoto:\n")
        for i in range(len(batoto_manga)):
            os.chdir(Main_Directory)
            Batoto(batoto_manga[i])
            print('\n')


        print("Downloading Manga From MangaHere:\n")
        for i in range(len(mangahere_manga)):
            os.chdir(Main_Directory)
            MangaHere(mangahere_manga[i])
            print('\n')


        print("Downloading Manga From MangaPanda:\n")
        for i in range(len(mangapanda_manga)):
            os.chdir(Main_Directory)
            MangaPanda(mangapanda_manga[i])
            print('\n')


        print("Downloading Manga From MangaStream:\n")
        for i in range(len(mangastream_manga)):
            os.chdir(Main_Directory)
            MangaStream(mangastream_manga[i])
            print('\n')



        counter += 1

        if counter < 5:
            print('\n\nSleeping for 2 Hours.\n')
            time.sleep(7200)

        else:
            counter = 0
            print('\n\nSleeping for 1 Week.\n')
            time.sleep(604800)





main()

#To See any error/error code wait before the program exits completely

time.sleep(15)
