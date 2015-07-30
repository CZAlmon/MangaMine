#Ver. 0.5.0
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

main()

time.sleep(15)
