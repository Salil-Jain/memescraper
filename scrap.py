import urllib
import re
import subprocess
import time
import sys

urls="https://old.reddit.com/r/dankmemes/"

i=0
num = input("How many pages would you like to download(25 memes per page)?")
if num<1:
	sys.exit("Number of pages should be > 0")
else :
	while i<num:
		these_regex="data-url=\"(.+?)\""
		pattern=re.compile(these_regex)
		htmlfile=urllib.urlopen(urls)
		htmltext=htmlfile.read()
		titles=re.findall(pattern,htmltext)
		for s in titles:
			com = "wget " + s
			subprocess.call(com,shell=True)
		regex1 = "next-button.+?\"(.+?)\""
		pattern1 = re.compile(regex1)
		link1=re.findall(pattern1,htmltext)
		if(len(link1)==0):
			print "Something went wrong for i = %d. trying again..."%i
			time.sleep(2)
		else:
			urls = link1[3]
			i+=1