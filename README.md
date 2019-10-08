# memescraper

Scraping program to download memes from any subreddit.

# How to use #

`cd memescraper`

`mkdir memes` All the memes will be saved in this directory

`cd memes/`

`python ../scrap.py`

# The log file #

The log file is updated after every run of the script. The log file is used to resume the running of the script from a page if required. For example, if the script is run once on page 1-5 then on running it again you can start scraping from page 6. No need to run it again on page 1-5. This is helpful in cases where the script intentionally stopped in the middle or due to a network error.

If the log file is present a message will be prompted - 

```
log file detected! 
https://old.reddit.com/r/dankmemes/ was last saved at 08-10-2019 15:01:49
Would you like to continue from last url in the log? (y/n)
```
If yes, the script will prompt asking the number of pages to be downloaded and continue from the given url.
If no, the script will ask the name of the subreddit and then the number of pages to be downloaded.

# Video Tutorial #
[![asciicast](https://asciinema.org/a/273038.png)](https://asciinema.org/a/273038)
