# MangaMine

Download Manga from 4 different manga hosting websites







For the MangaDatabaseIntializer.py:

  This is a utility for MangaMine to download all the manga names and links from batoto, mangahere, and mangapanda (Mangastream is not supported here, sorry). Simply run this in the same directory as MangaMine.py and then when it is completed do not touch the folder and Database.txt file that it creates. MangaMine will detect the folder and .txt file.
  
  You do not have to download and use this utility. If the folder and file are not detected then MangaMine will simply prompt for a link to the top of the manga on whichever site you want to download from. It will give you an example each prompt.

  This utility is meant to be run weekly, biweekly or once a month to keep an updated list of all manga for each website available to use instead of haing to find and copy and paste links yourself.

DO NOT ALTER THE DATABASE TEXT FILE. DOING SO WILL BREAK MANGAMINE. ALTER ONLY AT YOUR OWN RISK.


For the MangaBotDownloader.py:

  This is a Bot that will automatically download all the chapters to manga you specify in the lists. It will run 5 times over a 10 hour period (Not including time spent downloading manga. The first time through may take a while since it will download every chapter, from there it will not redownload each chapter/page but update if any new chapters have been uploaded). Then it will sleep for 1 week. Then it will repeat the process to keep manga up to date.
  
For the Sub_Folder:

  This folder contains 3 python files that are the individual functions that download from a speicifc site. This is how we built this Main MangaMine program. We started with individual functions/programs that download from one site then merged them altogether with more options and commands. 
