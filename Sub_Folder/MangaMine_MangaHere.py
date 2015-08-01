#Ver. 0.1.5
#Authors: Dylan Wise & Zach Almon

import urllib.request
import re
import os
import platform
import sys
import string
import html

platformType = platform.system()


#site_number:
#   Bato.to = 1
#   Panda = 2
#   Here = 3

def Search_Feature(site_number, file_directory):

    set_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    search_list_names = []
    search_list_links = []

    lines_from_file = []

    with open((file_directory + "Manga_Database.txt"), "r") as f:

        for line_in_text in f:
            temp_string = line_in_text
            lines_from_file.append(temp_string)

    lines_from_file.pop(0)      #Pop the warning off of the TextFile
    lines_from_file.pop(0)      #Pop the warning off of the TextFile

    if site_number == 1:

        lines_from_file.pop(0)

        try:
            my_int_number = int(lines_from_file[0])
        except ValueError:
            print('File Corrupt!')
            exit()

        lines_from_file.pop(0)

        counter = 0

        specific_sites_lines = []

        for i in range(len(lines_from_file)):
            temp_string = lines_from_file[i]
            temp_string = temp_string[:-1]      #Get rid of '\n' The Newline character
            specific_sites_lines.append(temp_string)
            counter += 1
            if counter == my_int_number:
                break

    elif site_number == 2:

        lines_from_file.pop(0)

        try:
            my_int_number = int(lines_from_file[0])
        except ValueError:
            print('File Corrupt!')
            exit()

        lines_from_file.pop(0)

        counter = 0

        for i in range(len(lines_from_file)):

            lines_from_file.pop(0)
            counter += 1

            if counter == my_int_number:
                break

        lines_from_file.pop(0)  #Extra Newline Pop
        lines_from_file.pop(0)  #Stars Pop
        lines_from_file.pop(0)  #Panda Name Pop

        try:
            my_int_number = int(lines_from_file[0])
        except ValueError:
            print('File Corrupt!')
            exit()

        lines_from_file.pop(0)

        counter = 0

        specific_sites_lines = []

        for i in range(len(lines_from_file)):

            temp_string = lines_from_file[i]
            temp_string = temp_string[:-1]      #Get rid of '\n' The Newline character
            specific_sites_lines.append(temp_string)
            counter += 1

            if counter == my_int_number:
                break

            
    elif site_number == 3:
        lines_from_file.pop(0)

        try:
            my_int_number = int(lines_from_file[0])
        except ValueError:
            print('File Corrupt!')
            exit()

        lines_from_file.pop(0)

        counter = 0

        for i in range(len(lines_from_file)):

            lines_from_file.pop(0)
            counter += 1

            if counter == my_int_number:
                break

        lines_from_file.pop(0)  #Extra Newline Pop
        lines_from_file.pop(0)  #Stars Pop
        lines_from_file.pop(0)  #Panda Name Pop

        try:
            my_int_number = int(lines_from_file[0])
        except ValueError:
            print('File Corrupt!')
            exit()

        lines_from_file.pop(0)

        counter = 0

        for i in range(len(lines_from_file)):

            lines_from_file.pop(0)
            counter += 1

            if counter == my_int_number:
                break

        lines_from_file.pop(0)  #Extra Newline Pop
        lines_from_file.pop(0)  #Stars Pop
        lines_from_file.pop(0)  #Here Name Pop

        try:
            my_int_number = int(lines_from_file[0])
        except ValueError:
            print('File Corrupt!')
            exit()

        lines_from_file.pop(0)

        counter = 0

        specific_sites_lines = []

        for i in range(len(lines_from_file)):

            temp_string = lines_from_file[i]
            temp_string = temp_string[:-1]      #Get rid of '\n' The Newline character
            specific_sites_lines.append(temp_string)
            counter += 1

            if counter == my_int_number:
                break


    else:
        print('Invalid Site Number! Program Terminated')
        exit()

    lines_from_list = []

    for i in range(len(specific_sites_lines)):
        lines_from_list = specific_sites_lines[i].split("\t")
        search_list_names.append(lines_from_list[0])
        search_list_links.append(lines_from_list[1])




    #Actual Input Decision Making After Here:
    search_list_letters = []
    search_list_letter_links = []

    search_found_bool = False #Search is/isnt found
    search_quit_bool = False
    
    search_int = 0    #Search is/isnt found


    while True:
        print('You have 2 options to choose the manga you want to download.')
        print('Do you want to provide a direct [l]ink or [s]earch for a manga?')
        print('\tOr do you want to [q]uit the program?\n')
        urlRequest = input('')
        print()

        if urlRequest == 'q':
            exit()

        elif urlRequest == 'l':
            print('Please enter the url of the manga you wish to download (or q to quit): ')
            print('The Link needs to be the top page of the manga you wish to download like:')
            print('Ex. 1:\thttp://bato.to/comic/_/comics/seto-no-hanayome-r385')
            print('Ex. 2:\thttp://www.mangapanda.com/372/seto-no-hanayome.html')
            print('Ex. 3:\thttp://www.mangahere.co/manga/seto_no_hanayome/')
            urlRequest = input('')
            print('\n')

            if urlRequest == 'q':
                exit()

            else:
                return urlRequest
            

        elif urlRequest == 's':

            print('To Search for a Manga Title, Please input a Letter')
            print('A - Z to choose a manga starting with that letter')
            print('\'Misc\' for manga not starting with a letter')
            print('or \'Quit\' to quit the search\n')
            search_input = input('')
            print()

            #We need everything in the string to be lower case.
            search_input = search_input.lower()

            #Set of letters is a hard coded list
            if search_input in set_of_letters or search_input == 'misc':

                if search_input in set_of_letters:
                    #Get the list of mangas in the specific letter
                    for i in range(len(search_list_names)):
                        if search_list_names[i][0] == search_input.lower() or search_list_names[i][0] == search_input.upper():
                            search_list_letters.append(search_list_names[i])
                            search_list_letter_links.append(search_list_links[i])
                
                elif search_input == 'misc':
                    #Get the list of mangas that are misc
                    for i in range(len(search_list_names)):
                        if search_list_names[i][0] not in set_of_letters:
                            search_list_letters.append(search_list_names[i])
                            search_list_letter_links.append(search_list_links[i])

                else:
                    print('Fatal Error with search input!')
                    exit()



                print('Here is a list of the first 50 Manga Names.')
                print('Keep in mind you cannot go back')
                print('\tYour options are:')
                print('The number of the manga you want')
                print('\'n\' for the next 50 names')
                print('\'q\' to quit to the main menu\n')

                for i in range(len(search_list_letters)):

                    #Plus one here So there will be a minus one later!!!
                    print('Number ' + str(i+1) + ' ' + search_list_letters[i])
                            
                    if i % 50 == 49 or (i == (len(search_list_letters) - 1)):
                                
                        print('\nYour options are:')
                        print('The number of the manga you want')
                        print('\'n\' for the next 50 names')
                        print('\'q\' to quit to the main menu\n')

                        while True:
                            print('Choose:')             
                            search_input = input('')
                            print('\n')

                            if search_input.isdigit():

                                if int(search_input) > 0 or int(search_input) < len(search_list_letters):
                                    print('Your choice is: ' + search_list_letters[int(search_input)-1])
                                    downloadManga = True
                                    search_int = (int(search_input) - 1) #Subtract one for the option before
                                    search_found_bool = True
                                    break
                                
                                else:
                                    print('Your choice needs to be greater then 0 and less then ' + str(len(search_list_letters)))
                                

                            elif search_input == 'n':
                                print('\nThe next 50 manga:\n')
                                break

                            elif search_input == 'q':
                                search_quit_bool = True
                                break

                            elif search_input == 'l':
                                print('\nYour options are:')
                                print('The number of the manga you want')
                                print('\'n\' for the next 50 names')
                                print('\'q\' to quit to the main menu\n')

                            else:
                                print('Invalid choice!')
                                print()

                        if search_found_bool:
                            break

                    if search_quit_bool:
                        break
                    
                if search_found_bool:
                    #At this point the index has been found for the manga name and link
                    #   In the search list letters list!!!
                    break

                else:
                    #Reset Settings
                    search_list_letters = []
                    search_list_letter_links = []

                    search_found_bool = False
                    search_quit_bool = False
    
                    search_int = 0

                    print('For some reason your search didn\'t work.')
                    print('You will now have to try again, sorry!')


                #If found succesful break here

            elif search_input == 'quit':
                #Dont break just loop back to the main choices again
                pass

            else:
                print()
                print('Invalid option!')

                
        else:
            print('Invalid option!')


    link_to_return = search_list_letter_links[search_int]

    return link_to_return



def main():

    success = False

    Search_feature = False

    currentDirectory = os.getcwd()

    
    if platformType == 'Windows':
        Search_feature_directory = currentDirectory + '\\Manga_Names_And_Links\\'
    else:
        Search_feature_directory = currentDirectory + '/Manga_Names_And_Links/'

    Search_feature = os.path.isfile(Search_feature_directory + 'Manga_Database.txt')


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

    while 1:

        if Search_feature:

            while True:

                search_url = Search_Feature(3, Search_feature_directory)

                try:
                    urllibHTML = urllib.request.urlopen(search_url).read()
                    downloadManga = True
                    break
                except:
                    print()
                    print('Invalid URL or connection Timeout')
                    print('Please Try Again')

        else:
            print('The URL you are to input below should be the top level page of the')
            print('manga you wish to download')
            print('Ex: http://www.mangahere.co/manga/seto_no_hanayome/ ')
            print()

            while True:
                print('Please enter the url of the manga you wish to download (or q to quit): ')
                urlRequest = input('')
                print('\n')

                if urlRequest == 'q':
                    return

                try:
                    urllibHTML = urllib.request.urlopen(urlRequest).read()
                    downloadManga = True
                    break

                except:
                    print()
                    print('Invalid URL or connection Timeout')




        if downloadManga == True:
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

            #   Add in options here

            search_found_bool = False
            search_quit_bool = False

            fullDownload = False
            custom_start = False
            custom_end = False
            place_to_start_from_index = 0
            place_to_end_at_index = 0


            while True:

                search_found_bool = False
                search_quit_bool = False

                fullDownload = False
                custom_start = False
                custom_end = False
                place_to_start_from_index = 0
                place_to_end_at_index = 0

                print('Do you wish to download the entire manga? [y/n] or [q] to quit.')
                continueChoiceFullDownload = input('')
                print('\n')

                if continueChoiceFullDownload == 'n':

                    print('Here is a list of the first 50 Chapters.')
                    print('Keep in mind you cannot go back')
                    print('\tYour options are:')
                    print('The number of the chapter you want to start a')
                    print('\'n\' for the next 50 chapters')
                    print('\'q\' to quit to the main menu\n')
                                                
                    for i in range(len(allChaps)):

                        #This code block is to extract the Vol and Chapter numbers
                        #From the URL. It is a pain but needed.
                        #This code block is also used later on.

                        skipBool1 = False
                        skipBool2 = False
                        volChapDirectoryString = ""

                        findVolume = re.findall(r'v\d{2}.\d+' , allChaps[i])
                        findChap = re.findall(r'c\d{3}.\d+' , allChaps[i])
                
                        if len(findVolume) == 0:
                            findVolume = re.findall(r'v\d{2}', allChaps[i])

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
                            findChap = re.findall(r'c\d{3}', allChaps[i])

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
                            return



                        #Plus one here So there will be a minus one later!!!
                        print('Number ' + str(i+1) + ' ' + volChapDirectoryString)
                        
                            
                        if i % 50 == 49 or (i == (len(allChaps) - 1)):
                                
                            print('\nYour options are:')
                            print('The number of the manga you want')
                            print('\'n\' for the next 50 names')
                            print('\'q\' to quit to the main menu\n')

                            while True:
                                print('Choose:')             
                                search_input = input('')
                                print('\n')

                                if search_input.isdigit():

                                    if int(search_input) > 0 and int(search_input) <= len(allChaps):
                                        custom_start = True
                                        place_to_start_from_index = (int(search_input) - 1) #Subtract one for the option before
                                        search_found_bool = True
                                        break
                                
                                    else:
                                        length_of_list = len(allChaps)
                                        print('Your choice needs to be greater then 0 and less then ' + str(int(length_of_list)+1))
                                
                                elif search_input == 'n':
                                    print('\nThe next 50 manga:\n')
                                    break

                                elif search_input == 'q':
                                    search_quit_bool = True
                                    break

                                elif search_input == 'l':
                                    print('\nYour options are:')
                                    print('The number of the manga you want')
                                    print('\'n\' for the next 50 names')
                                    print('\'q\' to quit to the main menu\n')

                                else:
                                    print('Invalid choice!')
                                    print()

                            if search_found_bool:
                                break

                        if search_quit_bool:
                            break

                    
                    #If there was something found and the user wants to end at a chapter
                    #If the user quit than this will just loop back to the begining of the menu

                    if search_found_bool:

                        search_found_bool = False
                        search_quit_bool = False

                        while 1:
                            print('Do you wish to end the download at a certain chapter?[y/n] or [q] to quit.')
                            print('By Choosing no the entire manga will download from the start location')
                            continueChoiceCustomChap = input('')
                            print('\n')

                            if continueChoiceCustomChap == 'y':

                                while True:

                                    print('Here is a list of the first 50 Chapters.')
                                    print('Keep in mind you cannot go back')
                                    print('You must select a number equal to or greater than ' + str(place_to_start_from_index))
                                    print('\tYour options are:')
                                    print('The number of the chapter you want to start a')
                                    print('\'n\' for the next 50 chapters')
                                    print('\'q\' to quit and download until the end of the manga\n')
                                                
                                    for i in range(len(allChaps)):

                                        #This code block is to extract the Vol and Chapter numbers
                                        #From the URL. It is a pain but needed.
                                        #This code block is also used later on.

                                        skipBool1 = False
                                        skipBool2 = False
                                        volChapDirectoryString = ""

                                        findVolume = re.findall(r'v\d{2}.\d+' , allChaps[i])
                                        findChap = re.findall(r'c\d{3}.\d+' , allChaps[i])
                
                                        if len(findVolume) == 0:
                                            findVolume = re.findall(r'v\d{2}', allChaps[i])

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
                                            findChap = re.findall(r'c\d{3}', allChaps[i])

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
                                            return



                                        #Plus one here So there will be a minus one later!!!
                                        print('Number ' + str(i+1) + ' ' + volChapDirectoryString)
                            
                                        if i % 50 == 49 or (i == (len(allChaps) - 1)):
                                
                                            print('\nYour options are:')
                                            print('The number of the manga you want')
                                            print('\'n\' for the next 50 names')
                                            print('\'q\' to quit and download until the end of the manga\n')

                                            while True:
                                                print('Choose:')             
                                                search_input = input('')
                                                print('\n')

                                                if search_input.isdigit():

                                                    if int(search_input) >= (place_to_start_from_index + 1) and int(search_input) <= len(allChaps):
                                                        custom_end = True
                                                        place_to_end_at_index = (int(search_input) - 1) #Subtract one for the option before
                                                        search_found_bool = True
                                                        break
                                
                                                    else:
                                                        length_of_list = len(allChaps)
                                                        print('Your choice needs to be greater then ' +  str(place_to_start_from_index + 1) + ' and less then ' + str(int(length_of_list)+1))
                                

                                                elif search_input == 'n':
                                                    print('\nThe next 50 manga:\n')
                                                    break

                                                elif search_input == 'q':
                                                    search_quit_bool = True
                                                    break

                                                elif search_input == 'l':
                                                    print('\nYour options are:')
                                                    print('The number of the manga you want')
                                                    print('\'n\' for the next 50 names')
                                                    print('\'q\' to quit and download until the end of the manga\n')

                                                else:
                                                    print('Invalid choice!')
                                                    print()

                                            if search_found_bool:
                                                break

                                        if search_quit_bool:
                                            break
                                    
                                    if custom_start or custom_end:
                                        break

                                if custom_start or custom_end:
                                    break

                            elif continueChoiceCustomChap == 'n':
                                break

                            elif continueChoiceCustomChap == 'q':
                                return

                            else:
                                print('Invalid Option!')

                        #At this point There is a gurenteed start
                        #There may be an end chapter but if the user quit than custom_end will be false
                        #and the manga will download from the start until absolute end of manga
                        break

                    else:
                        print('No chapter Detected. Please try again.\n\n')


                #After if statement      

                elif continueChoiceFullDownload == 'y':
                    fullDownload = True
                    break

                elif continueChoiceFullDownload == 'q':
                    return

                else:
                    print('Invalid Option!')


            #
            #

            if fullDownload == True:
                pass       
                            
            #If you only have a start location, pop off chapter numbers/links until you hit that chapter
            elif custom_start == True and custom_end == False:
                for i in range(place_to_start_from_index):
                    allChaps.pop(0)

            #Do same As before But will need to pop off end as well
            #I found it easier to reverse then do down the list in decending order
            #And pop off from begining until the end chapter is reached.
            #Then reverse again.           
            elif custom_start == True and custom_end == True:
                for i in range(place_to_start_from_index):
                    allChaps.pop(0)

                for i in range(len(allChaps)-(int(place_to_end_at_index)-int(place_to_start_from_index))-1):
                    allChaps.pop(-1)

            else:
                print('Fatal error with the start selection')
                return


            #

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
                    return

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
                
                urllibIMG = str(urllib.request.urlopen(i).read())
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

                        urllibIMG = str(urllib.request.urlopen(urllibReq).read())

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
                            rawImage = urllib.request.urlopen(imageURL[0]).read()
                            fout = open(imageName, 'wb')       
                            fout.write(rawImage)                          
                            fout.close()
        
        while True:

            print('Do you want to download another manga from MangaHere?')
            print('[y/n]')

            Continue_or_not = input('')

            if Continue_or_not == 'y':
                break

            elif Continue_or_not == 'n':
                return

            else:
                print('Invalid choice!')
                print()
   
main()
