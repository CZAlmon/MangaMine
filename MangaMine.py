#Ver. 0.6.0
#Authors: Dylan Wise & Zach Almon

import urllib.request
import re
import os
import platform
import sys
import string
import html
import time

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

                    print('Warning!! Some of these manga have special characters.')
                    print('These manga will display like: ')
                    print('"0\\xc3\\x970 Memories" instead of 0 (Special Characters) 0 Memories')
                    print('These special (unicode) Characters can\'t be displayed here. Sorry.')
                    print('You will still be able to search for the manga you want, just don\'t')
                    print('overlook anything with something like: \\xc95\\x73 \n\n')
                    

                    time.sleep(10)

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

                                if int(search_input) > 0 and int(search_input) < len(search_list_letters):
                                    print('Your choice is: ' + search_list_letters[int(search_input)-1], end = '\n\n')
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


def Batoto():

    success = False
    Search_feature = False

    currentDirectory = os.getcwd()

    
    if platformType == 'Windows':
        Search_feature_directory = currentDirectory + '\\Manga_Names_And_Links\\'
    else:
        Search_feature_directory = currentDirectory + '/Manga_Names_And_Links/'

    Search_feature = os.path.isfile(Search_feature_directory + 'Manga_Database.txt')



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

    while success == False:

        downloadManga = False

        if Search_feature:

            while True:

                search_url = Search_Feature(1, Search_feature_directory)

                try:
                    urllibHTML = urllib.request.urlopen(search_url).read()
                    downloadManga = True
                    break
                except:
                    print()
                    print('Invalid URL!')
                    print('Please Try Again')

        else:
            print('The URL you are to input below should be the top level page of the')
            print('manga you wish to download')
            print('Ex: http://bato.to/comic/_/comics/seto-no-hanayome-r385 ')
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
                    print('Invalid URL!')


        type_one_manga = False
        type_two_manga = False

        
        if downloadManga == True:

            Manga_Title = re.findall(r'<title>+(.*?)- Scanlations', str(urllibHTML))

            if len(Manga_Title) == 0:
                print("Title not found. URL or HTML Error.")
                break
            
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

            #For any other language on Bato.to change lang_English to whatever matches the language you desire. 
            #Then this file *SHOULD* work with your language. It is Untested as anything else but english
            allENGLISHChaps = re.findall(r'lang_English+(.*?)\ title="+', str(urllibHTML))
            
            if len(allENGLISHChaps) == 0:
                print("Manga has no English Chapters or there was an error reading the HTML!")
            else:
                First_chapter_string = allENGLISHChaps[-1]
                First_chapter_address = re.findall(r'href=\"+(.*?)\"', First_chapter_string)
                First_chapter_address_string = First_chapter_address[0]
                
                try:
                    First_chapter_html = urllib.request.urlopen(First_chapter_address_string).read()
                except:
                    print()
                    print('Trouble Opening Webpage!')
                    downloadManga = False

                if downloadManga == True:
                    #Find which type of manga this manga is. Whether all pages of the chapter are on one page or multiple pages.
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
                    


                    # list_of_Chapter_Links             Has Links    -Has Duplicates at this point
                    # list_of_chapter_names_refined     Has Names    -Has Duplicates at this point
                    #
                    #   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    #   This Comment Block is what remains of a method to delete repeated chapters
                    #   Due to some Manga Chapter names and Chapter Quality it has (as of 7/2/15) become
                    #   very difficult to keep duplicate chapters out without some problems arising.
                    #   This Code shall be kept here so in the future if a more effective way to
                    #   delete duplicates while keeping original's/good quality chapters becomes apparent
                    #   we can reimplement this feature.
                    #
                    #list_of_Chapter_Links_Final = []
                    #list_of_Chapter_Numbers_Final = []
                    #for i in range(len(list_of_chapter_names_refined)):
                    #    if list_of_chapter_names_refined[i] in list_of_Chapter_Numbers_Final:
                    #        pass
                    #    else:
                    #        list_of_Chapter_Numbers_Final.append(list_of_chapter_names_refined[i])
                    #        list_of_Chapter_Links_Final.append(list_of_Chapter_Links[i])



                    list_of_Chapter_Links_Final = list_of_Chapter_Links
                    list_of_Chapter_Numbers_Final = list_of_chapter_names_refined
                    
                    list_of_Chapter_Links_Final.reverse()
                    list_of_Chapter_Numbers_Final.reverse()
                    
                    can_be_sorted = True

                    #Checks to see if the manga chapters can be sorted by number (basically are all the chapters floats)
                    #If not only full downloads are available for that manga due to some manga chapters being
                    #   wildly out of order AND not being an integers/floats, a feature to download only some chapters 
                    #   has proven very difficult.

                    for i in range(len(list_of_Chapter_Numbers_Final)):
                        try:
                            float(list_of_Chapter_Numbers_Final[i])
                        except ValueError:
                            print('Sorry, this manga can\'t be sorted.')
                            print('You can only do a full download.')
                            print('\n')
                            can_be_sorted = False
                            break


                    fullDownload = False
                    chapter_found = False
                    custom_start = False
                    custom_end = False
                    chapter_to_start_from = ''
                    place_to_start_from_index = 0
                    chapter_to_end_at = ''
                    place_to_end_at_index = 0

                    if can_be_sorted:

                        #Selection Sort. Efficiency isn't needed here, all manga on bato.to should be below 1500 chapters.
                        #What's needed is to keep 'list_of_Chapter_Numbers_Final' and 'list_of_Chapter_Links_Final' together/one-to-one. 
                        #Meaning the chapter at list_of_Chapter_Numbers_Final[i] has the link at list_of_Chapter_Links_Final[i]
                        for i in range(len(list_of_Chapter_Numbers_Final)):

                            current = i                            

                            for k in range(i+1, len(list_of_Chapter_Numbers_Final)):
                                if float(list_of_Chapter_Numbers_Final[k]) < float(list_of_Chapter_Numbers_Final[current]):
                                    current = k
            
                            list_of_Chapter_Numbers_Final[i], list_of_Chapter_Numbers_Final[current] = list_of_Chapter_Numbers_Final[current], list_of_Chapter_Numbers_Final[i]
                            list_of_Chapter_Links_Final[i], list_of_Chapter_Links_Final[current] = list_of_Chapter_Links_Final[current], list_of_Chapter_Links_Final[i]
                        

                        while 1:
                            print('Do you wish to download the entire manga? [y/n], [l] to list out the chapters, or [q] to quit.')
                            continueChoiceFullDownload = input('')
                            print('\n')

                            if continueChoiceFullDownload == 'l':
                                for k in range(len(list_of_Chapter_Numbers_Final)):
                                    print(repr(list_of_Chapter_Numbers_Final[k]).ljust(20), end='')
                                    if (k % 3) == 2:
                                        print('\n', end='')
                                print('', end='\n')
                                print('', end='\n')

                            elif continueChoiceFullDownload == 'y':
                                fullDownload = True
                                break

                            elif continueChoiceFullDownload == 'n':
                                while 1:
                                    print('Do you wish to start download from a certain chapter? [y/n], [l] to list out the chapters, or [q] to quit.')
                                    print('By Choosing no the entire manga will download')
                                    continueChoiceCustomChap = input('')
                                    print('\n')
              
                                    if continueChoiceCustomChap == 'l':
                                        for k in range(len(list_of_Chapter_Numbers_Final)):
                                            print(repr(list_of_Chapter_Numbers_Final[k]).ljust(20), end='')
                                            if (k % 3) == 2:
                                                print('\n', end='')
                                        print('', end='\n')
                                        print('', end='\n')

                                    elif continueChoiceCustomChap == 'y':
                                        print('Please enter the chapter you wish to start from')
                                        chapNum = input('')
                                        print('\n')
                                    
                                        for i in range(len(list_of_Chapter_Numbers_Final)):
                                            if chapNum == list_of_Chapter_Numbers_Final[i]:
                                                chapter_found = True
                                                custom_start = True
                                                chapter_to_start_from = list_of_Chapter_Numbers_Final[i]
                                                place_to_start_from_index = i
                                                break
                            
                                        if chapter_found == False:
                                            print('Invalid chapter number! Maybe the chapter is missing?')
                                            print()

                                        else:
                                            print('Chapter Found!')
                                            print('\n')
                                            #May use chapter_found again for the end point
                                            chapter_found = False
                                            break

                                    elif continueChoiceCustomChap == 'n':
                                        fullDownload = True
                                        break
                                
                                    elif continueChoiceCustomChap == 'q':
                                        return

                                    else:
                                        print('Invalid Option!')
                                        print()

                        
                                if fullDownload == False:
                                    while 1:
                                        print('Do you wish to end the download at a certain chapter?[y/n], [l] to list out the chapters, or [q] to quit.')
                                        print('By Choosing no the entire manga will download from the start location')
                                        continueChoiceCustomChap = input('')
                                        print('\n')

                                        if continueChoiceCustomChap == 'l':
                                            for k in range(len(list_of_Chapter_Numbers_Final)):
                                                print(repr(list_of_Chapter_Numbers_Final[k]).ljust(20), end='')
                                                if (k % 3) == 2:
                                                    print('\n', end='')
                                            print('', end='\n')
                                            print('', end='\n')
                                
                                        elif continueChoiceCustomChap == 'y':
                                            print('Please enter the chapter you wish to end at')
                                            chapNum = input('')
                                            print('\n')

                                            temp_bool = True

                                            for i in range(len(list_of_Chapter_Numbers_Final)):

                                                if chapNum == list_of_Chapter_Numbers_Final[i]:
                                                    #not working
                                                    if i < place_to_start_from_index:
                                                        print('Sorry, Number must be greater than or equal to the Start chapter, which is:', chapter_to_start_from)
                                                        print('Invalid Option!')
                                                        print()
                                                        temp_bool = False
                                                        break

                                                    else:
                                                        chapter_found = True
                                                        custom_end = True
                                                        temp_bool = True
                                                        chapter_to_end_at = list_of_Chapter_Numbers_Final[i]
                                                        place_to_end_at_index = i

                                                        #This loop is to make sure all duplicates are included 
                                                        #in the chapter list
                                                        for k in range(place_to_end_at_index, len(list_of_Chapter_Numbers_Final)):
                                                            if chapNum == list_of_Chapter_Numbers_Final[k]:
                                                                place_to_end_at_index = k
                                                            
                                                        break

                                            if temp_bool == True:
                                                if chapter_found == False:
                                                    print('Invalid chapter number! Maybe the chapter is missing?')
                                                    print()

                                                else:
                                                    print('Chapter Found!')
                                                    print('\n')
                                                    break                                    

                                        elif continueChoiceCustomChap == 'n':
                                            break
    
                                        elif continueChoiceCustomChap == 'q':
                                            return

                                        else:
                                            print('Invalid Option!')
                                            print()
                                #At the end of the Main elif choice == no
                                break
    
                            elif continueChoiceFullDownload == 'q':
                                return

                            else:
                                print('Invalid Option!')

                    else:
                        fullDownload = True

                        print('Do you want to quit the program before downloading')
                        print('the entire manga? [y/n]')

                        while True:

                            quit_or_not = input()

                            quit_or_not = quit_or_not.lower()

                            if quit_or_not == 'y':
                                return

                            elif quit_or_not == 'n':
                                break

                            else:
                                print('Invalid input! Do you want to quit? [y/n]')

                



                    #For Reference:
                    #If fullDownload = True  
                            #The user wants to download From chapter 1 to the end (Whatever is available)
                    #If custom_start = True Than fullDownload == False  
                            #The user wants to download from The start chapter which was Found and stored in chapter_to_start_from
                            #Does not Need custom_end to be True. If it isnt then it will download until the end of manga
                    #If custom_end = True Than custom_start == True AND fullDownload == False                          
                            #The user wants to download from The start chapter which was Found and stored in chapter_to_start_from
                            #The user also wants to download until an end chapter which was Found and stored in chapter_to_end_at

                    

                    #This if, elif, and elif are to set which chapters are to be downloaded.
                    if fullDownload == True:
                        pass       
                 
                    #If you only have a start location, pop off chapter numbers/links until you hit that chapter
                    elif custom_start == True and custom_end == False:
                        for i in range(place_to_start_from_index):
                            list_of_Chapter_Links_Final.pop(0)
                            list_of_Chapter_Numbers_Final.pop(0)

                    #Do same As before But will need to pop off end as well
                    #I found it easier to reverse then do down the list in decending order
                    #And pop off from begining until the end chapter is reached.
                    #Then reverse again.           
                    elif custom_start == True and custom_end == True:
                        for i in range(place_to_start_from_index):
                            list_of_Chapter_Links_Final.pop(0)
                            list_of_Chapter_Numbers_Final.pop(0)

                        for i in range(len(list_of_Chapter_Links_Final)-(int(place_to_end_at_index)-int(place_to_start_from_index))-1):
                            list_of_Chapter_Links_Final.pop(-1)
                            list_of_Chapter_Numbers_Final.pop(-1)

                    else:
                        print('Fatal error with the start selection')
                        return

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
                    if fullDownload == True or custom_start == True:
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

                            urllibHTML = urllib.request.urlopen(list_of_Chapter_Links_Final[i]).read()
                            
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
                                        rawImage = urllib.request.urlopen(image_file_name).read()
                                        fout = open(imageName, 'wb')       
                                        fout.write(rawImage)                          
                                        fout.close()
                            
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
                                    try:
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
                                            page_urllibHTML = urllib.request.urlopen(list_of_page_links_final[j]).read()

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
                                            rawImage = urllib.request.urlopen(image_file_name).read()
                                            fout = open(imageName, 'wb')       
                                            fout.write(rawImage)                          
                                            fout.close()

                                    except:
                                        print("Invalid URL Error, or Connection Timeout!")
                                        return
                            else:
                                print("Manga Type Error!")
                                return



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

    #Main While Loop
        #Download Manga If statement
            #English chapters > 0
                #Download manga Main statement where everything is performed in

    return


def MangaPanda():

    success = False
    currentDirectory = os.getcwd()
    downloadMangaListOnce = False
    searchAgain = False


    if platformType == 'Windows':
        Search_feature_directory = currentDirectory + '\\Manga_Names_And_Links\\'
    else:
        Search_feature_directory = currentDirectory + '/Manga_Names_And_Links/'

    Search_feature = os.path.isfile(Search_feature_directory + 'Manga_Database.txt')


    while success == False:
        downloadManga = True

        if Search_feature:
            search_url = Search_Feature(2, Search_feature_directory)

            link_or_not = re.findall(r'(mangapanda.com)', search_url)

            if len(link_or_not) == 0:
                urlRequest = 'http://www.mangapanda.com' + search_url
            else:
                urlRequest = search_url

        else:
            print('The URL you are to input below should be the top level page of the')
            print('manga you wish to download')
            print('Ex: http://www.mangapanda.com/372/seto-no-hanayome.html ')

            print('Please enter the url of the manga you wish to download (or q to quit): ')
            urlRequest = input('')
            print('\n')

        #take the URL the user gave and cut off last five characters (.html)
        try:

            does_it_have_dot_html = re.findall(r'(\.html)', urlRequest)

            if len(does_it_have_dot_html) == 0:
                pass
            else:
                urlRequest = urlRequest[:-5]

            urllibHTML = urllib.request.urlopen(urlRequest).read()
            
        except:
            print()
            print('Invalid URL or connection timeout.')
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

    return


def MangaHere():

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

    return


def MangaStream():

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

        print('To download from MangaStream you must input a URL.')
        print('The URL you are to input below should be the top level page of the')
        print('manga you wish to download')
        print('Ex: http://mangastream.com/manga/one_piece ')
        print()

        print('Please enter the url of the manga you wish to download (or q to quit): ')
        urlRequest = input('')
        print('\n')

        if urlRequest == 'q':
            return

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

                number_of_pages_list = re.findall(r'http://readms.com/r/.*?/\S+/\S+/(\d+)', final_page)

                number_of_pages = int(number_of_pages_list[0])

                chapter_url_list = re.findall(r'(http://readms.com/r/.*?/\S+/\S+/)\d+', final_page)

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

    return


def Main():

    print('\t\tWelcome to MangaMine!')     
    
    site_input = 'y'

    MAIN_currentDirectory = os.getcwd()
    
    while True:

        if site_input == 'y':
            
            print('Which manga site do you want to download from?')
            print('Choose a number:', end='\n\n')
            print('1. MangaStream')
            print('2. MangaPanda')
            print('3. MangaHere')
            print('4. Batoto', end='\n\n')

            while True:

                site_input = input()

                print()
           
                if site_input == '1':
                    MangaStream()
                    break

                elif site_input == '2':
                    MangaPanda()
                    break

                elif site_input == '3':
                    MangaHere()
                    break

                elif site_input == '4':
                    Batoto()
                    break

                else:
                    print('Invalid Input.')
                    print('Choose a number:', end='\n\n')
                    print('1. MangaStream')
                    print('2. MangaPanda')
                    print('3. MangaHere')
                    print('4. Batoto', end='\n\n')

        elif site_input == 'n':
            print('Goodbye.')
            break

        else:
            print('Invalid input.')


        os.chdir(MAIN_currentDirectory)
        
        print('Do you want to download from another manga site? [y/n]')
        
        site_input = input()

        print()

        site_input = site_input.lower()

        #End of While Loop

    #End of main





Main()

time.sleep(15)
