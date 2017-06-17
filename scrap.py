import urllib
import re
import subprocess
import time

urls="https://www.reddit.com/r/dankmemes/"

i=0
while i<10:
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
	else:
		urls = link1[0]
		i+=1