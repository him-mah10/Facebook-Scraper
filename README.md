<h1 align="center"> Facebook-Scraper</h1>

#### Author - Himanshu Maheshwari

#### What it does?
This script is used to scrape the text of posts on a public facebook page and comments(all of them and all of their replies) on those posts and save them in mongodb database. It also stores the link to the profile of the person who made the comment. It uses selenium. This script __does not use facebook's graph api__.

#### Requirments
* python 3.x
* Latest chrome wedriver, should be placed in the same folder as the script
* mongodb and selenium to be installed

__Note: This script run on linux machine, with slight modification it could be run on windows machine also.__

#### How to use?
1) Open the `facebook_scraper.py` file in any text editor
	1) Assign the name of the page to `page_name` variable (line 31).
	2) Assign the URL to `url` variable (line 32).
	3) Assign how many time do you want to scroll to `total_scrolls` variable (line 35). The value should be a non-negative integer. More the value more will be scroll.
	4) Assign your facebook's email id to `email` variable (line 150). 
	5) Assign your password to `password` variable (line 151).
	6) Now save the changes.

2) Next put the latest chrome webdriver in the same folder as the script. I am attaching a webdriver which was latest durint the writing of this script.

3) Open terminal and `cd` into the directory containing the script. Than run the script by writing `python3 facebook_scraper.py` and wait for the script to complete it's work. 

4) _**suggestion**_ - It is suggested to use VPN for scraping the data as facebook might block your ip if you scrawl the data. Though this script works fine even without VPN.

#### Output
The output of this script is all the text of posts on a public facebook page and comments(all of them and all of their replies) on those posts stored in facebook mongodb database. With slight changes you could store them in a text or csv file.

#### Warning
Scraping data from facebook without permission from facebook or without using it's graph api is __illegal__. Kindly refer to https://www.facebook.com/robots.txt for more details.

#### Cheers!!!
