import urllib
import re
import subprocess
import time
import sys
import os.path
import pandas as pd
from bs4 import BeautifulSoup

#now, we can scrape any memes!
subreddit = raw_input("Please enter the name of subreddit to scrape: ");
if not isinstance(subreddit, str):
	sys.exit('Please enter a valid string')

#the url of the website to be scraped!
urls="https://old.reddit.com/r/" + subreddit + "/"

#a log functionality to return scraping as soon as restarted
#delete the url_log.csv file to restart the process!
if(os.path.isfile('../url_log.csv')):
	log = pd.read_csv('../url_log.csv');
	try:
		urls = log.iloc[-1].values[1];
	except:
		urls = log.columns[1];
	list_log = [];
else:
	list_log = [urls];

# input the number of pages to scrape memes from!
i=0
num = input("How many pages would you like to download(25 memes per page)?")
if num<1:
	sys.exit("Number of pages should be > 0")
else :
	try:
		while i<num:
			these_regex="data-url=\"(.+?)\""
			pattern=re.compile(these_regex)
			htmlfile=urllib.urlopen(urls)
			htmltext=htmlfile.read()
			content = htmltext;
			#using soup to find names!
			soup = BeautifulSoup(content,'lxml')
			names = soup.find_all(["p","a"],{'class':'title','data-event-action':'title'});
			titles=re.findall(pattern,htmltext)
			for i,s in enumerate(titles):
				try:
					com = "wget --no-check-certificate " + s + " -O \"" + names[i].get_text() + "\".jpg";
					subprocess.call(com,shell=True)
				except:
					com = "wget --no-check-certificate " + s;
					subprocess.call(com,shell=True)
			regex1 = "next-button.+?\"(.+?)\""
			pattern1 = re.compile(regex1)
			link1=re.findall(pattern1,htmltext)
			if(len(link1)==0):
				print "Something went wrong for i = %d. trying again..."%i
				time.sleep(3)
			else:
				urls = link1[0]
				list_log.append(urls);
				i+=1
		log = pd.Series(list_log);
		log.to_csv('../url_log.csv',mode = 'a');
	except Exception as e:
		print e;
		print "saving log";
		log = pd.Series(list_log);
		log.to_csv('../url_log.csv',mode = 'a');