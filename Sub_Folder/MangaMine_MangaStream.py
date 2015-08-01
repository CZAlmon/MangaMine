#Ver. 0.0.1
#Authors: Dylan Wise & Zach Almon

import urllib.request
import re
import os
import platform
import sys
import string
import html

platformType = platform.system()


def main():

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


    while success == False:

        downloadManga = False

        print('The URL you are to input below should be the top level page of the')
        print('manga you wish to download')
        print('Ex: http://mangastream.com/manga/one_piece ')
        print()

        print('Please enter the url of the manga you wish to download (or q to quit): ')
        urlRequest = input('')
        print('\n')

        try:

            urllibHTML = urllib.request.urlopen(urlRequest).read()
            downloadManga = True
            
        except:
            print()
            print('Invalid URL or connection time-out.')

        if downloadManga == True:
            
            Manga_Title = re.findall(r'<title>(.*?) Manga', str(urllibHTML))

            if len(Manga_Title) == 0:
                print("Title not found. URL or HTML Error.")
                break

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
            directorySafeName = directorySafeName.replace("\"","'")
            directorySafeName = directorySafeName.replace("%", " Percent ")
            directorySafeName = directorySafeName.replace("<", "")   
            directorySafeName = directorySafeName.replace(">", "")

            Manga_Title_string = directorySafeName

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

                while True:
                    try:
                        urllibHTML = urllib.request.urlopen(chapter_link_string).read()
                        break

                    except:
                        print()
                        print('Request Failed. Trying again in 10 seconds.')
                        time.sleep(10)

                page_list_raw = re.findall(r'<ul class="dropdown-menu">(.*?)</ul>', str(urllibHTML), re.DOTALL)

                page_list_string = page_list_raw[-1]

                list_of_some_of_the_pages = re.findall(r'href="(.*?)">', str(page_list_string))

                final_page = list_of_some_of_the_pages[-1]

                number_of_pages_list = re.findall(r'http://readms.com/r/.*?/\d+/\d+/(\d+)', final_page)

                number_of_pages = int(number_of_pages_list[0])

                chapter_url_list = re.findall(r'(http://readms.com/r/.*?/\d+/\d+/)\d+', final_page)

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
                        while True:
                            try:
                                page_urllibHTML = urllib.request.urlopen(chapter_url + str(j+1)).read()
                                break

                            except:
                                print()
                                print('Request Failed. Trying again in 10 seconds.')
                                time.sleep(10)
                        

                    image_file_name_list = re.findall(r'<img id="manga-page" src="(.*?)"/></a>', str(page_urllibHTML))

                    image_file_name = image_file_name_list[0]

                    #CHECK EXTENSION. Mangastream Could use .png or .jpg or .jpeg
                    image_file_extension_list = re.findall(r'(\.\D[^\.]+)', image_file_name)
                    image_file_extension = image_file_extension_list[-1]

                    imageName = "Page " + str(j+1) + image_file_extension

                    fileExists = os.path.isfile(imageName)

                    #If file does not already exist, opens a file, writes image binary data to it and closes
                    if fileExists == False:

                        while True:
                            try:
                                rawImage = urllib.request.urlopen(image_file_name).read()
                                break

                            except:
                                print()
                                print('Request Failed. Trying again in 10 seconds.')
                                time.sleep(10)

                        fout = open(imageName, 'wb')       
                        fout.write(rawImage)                          
                        fout.close()

        while 1:
            print('\n')
            print('Do you wish to download another manga?[y/n]')
            continueChoice = input('')

            if continueChoice == 'y':
                break

            elif continueChoice == 'n':
                success = True
                break

            else:
                print('Invalid Option!')




main()
