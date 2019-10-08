import urllib
import re
import subprocess
import time
import sys
import os.path
import os
import pandas as pd

#a log functionality to restart scraping state as it was interrupted
restart = "n" #normal value for restart is no!
if(os.path.isfile('../url_log.csv')):
	#retreive the file
	log = pd.read_csv('../url_log.csv')
	urls = log.iloc[-1].values[0]
	times = log.iloc[-1].values[1]
	#option to restart!
	print "log file detected! " 
	print urls + " was last saved at " + times
	restart = raw_input("Would you like to continue from last url in the log? (y/n)")
	if not isinstance(restart, str):
		sys.exit('Please enter a valid string')
	if (restart.lower() == "n"):
		os.remove("../url_log.csv")
		log = log[0:0] #empty log
	elif(restart.lower() != "y"):
		sys.exit("Please enter valid string")
else:
	log = pd.DataFrame(columns = ['urls','times'])
	print("No log file detected!")

#now, we can scrape any memes!
if (restart.lower() == "n"):
	subreddit = raw_input("Please enter the name of subreddit to scrape: ")
	if not isinstance(subreddit, str):
		sys.exit('Please enter a valid string')

	#the url of the website to be scraped!
	urls = "https://old.reddit.com/r/" + subreddit + "/"
	times = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
	log = log.append(other = pd.Series([urls,times],index=log.columns),ignore_index = True)


# input the number of pages to scrape memes from!
i = 0
num = input("How many pages would you like to download(25 memes per page)?")
if num < 1:
	sys.exit("Number of pages should be > 0")
else :
	try:
		while i < num:
			htmlfile = urllib.urlopen(urls)
			htmltext = htmlfile.read()
			content = htmltext

			# regex to find urls
			these_regex = "data-url=\"(.+?)\""
			pattern = re.compile(these_regex)
			all_urls = re.findall(pattern,htmltext)
			
			# regex to find names
			names_regex = "data-event-action=\"title\".+?>(.+?)<"
			names_pattern = re.compile(names_regex)
			names = re.findall(names_pattern, htmltext)

			for j,s in enumerate(all_urls):
				try:
					com = "wget --no-check-certificate " + s + " -O \"" + names[j] + "\".jpg"
					subprocess.call(com,shell=True)
				except:
					com = "wget --no-check-certificate " + s
					subprocess.call(com,shell=True)
			regex1 = "next-button.+?\"(.+?)\""
			pattern1 = re.compile(regex1)
			link1 = re.findall(pattern1,htmltext)
			if(len(link1) == 0):
				print "Something went wrong for i = %d. trying again..."%i
				time.sleep(3)
			else:
				urls = link1[0]
				times = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
				log = log.append(other = pd.Series([urls,times],index=log.columns),ignore_index = True)
				i += 1
		log.to_csv('../url_log.csv',mode = 'w',index=False)
	except KeyboardInterrupt as e:
		print e
		print "saving log"
		log.to_csv('../url_log.csv',mode = 'w',index=False)