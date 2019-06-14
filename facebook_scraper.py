import getpass
import calendar
import os
import platform
import sys
import time
import urllib.request
from bson.objectid import ObjectId

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print("connected")
mydb = myclient["facebook"]
posts = mydb["posts"]
comments = mydb["comments"]

post = { "_id" : None, "page_name" : None, "page_url" : None, "post" : None }
comment = { "_id" : None, "page_name" : None , "page_url" : None , "commenter_id" : None , "comment" : None }

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = None

#Enter your page name and url here
page_name = ""
url = ""

#Change the value of total_scrolls depending on how futher you want to go. It's value can be any non-negative integer.
total_scrolls = 10000
current_scrolls = 0
scroll_time = 5
old_height = 0
done_posts_click=0
done_comments_click=0


def check_height():
    new_height = driver.execute_script("return document.body.scrollHeight")
    return new_height != old_height

def scroll():
    global old_height
    current_scrolls = 0

    while (True):
        try:
            if current_scrolls == total_scrolls:
                return
            old_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, scroll_time, 0.05).until(lambda driver: check_height())
            current_scrolls += 1            
        except TimeoutException:
            break

    return	

def login(email,password):
	try:
		global driver
		options = Options()
		options.add_argument("--disable-notifications")
		options.add_argument("--disable-infobars")
		options.add_argument("--mute-audio")
		try:
			driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
		except:
			print("Latest driver required")
			exit()
		driver.get("https://en-gb.facebook.com")
		driver.maximize_window()
		driver.find_element_by_name('email').send_keys(email)
		driver.find_element_by_name('pass').send_keys(password)
		driver.find_element_by_id('loginbutton').click()
	except Exception as e:
		print("There's some error in log in.")
		print(sys.exc_info()[0])
		exit()

def scrape():
	driver.get(url)
	scroll()

	txt=driver.find_elements_by_xpath("//a[@class='see_more_link']")

	try:
		for x in txt:
			x.send_keys(Keys.ENTER)
	except:
		pass
	
	txt=driver.find_elements_by_xpath("//a[@class='_5v47 fss']")
	try:
		for x in txt:
			x.send_keys(Keys.ENTER)
	except:
		pass

	j=0
	while True:
		try:
			a=driver.find_element_by_xpath("//a[@class='_4sxc _42ft']")
			a.send_keys(Keys.ENTER)
			j+=1
		except:
			print(j)
			break
			# pass
		
			
	txt=driver.find_elements_by_xpath("//div[contains(@class,'_5pbx userContent')]")
	try:
		for x in txt:
			print ("post data - ", x.text)
			print ()

			post["_id"] = ObjectId() 
			post["page_name"] =  page_name
			post["page_url"] = url
			post["post"] = x.text
			InsertedResultObj = posts.insert_one(post)
	except:
		pass

	txt=driver.find_elements_by_xpath("//div[@class='_72vr']")
	try:
		for x in txt:
			a = x.find_elements_by_xpath (".//a[@class='_6qw4']")
			print ("who made the comment?  - ", a[0].get_attribute("href"))
			print ("what's in the comment? - ", x.text)
			print ()

			comment["_id"] = ObjectId()
			comment["page_name"] = page_name
			comment["page_url"] = url
			comment["commenter_id"] = a[0].get_attribute("href")
			comment["comment"] = x.text
			InsertedResultObj = comments.insert_one(comment)
	except:
		pass
	
def main():
	#Enter your facebook's email id and password here 
	email = ""
	password = ""
	login(email,password)
	scrape()
	driver.close()
	        
if __name__ == '__main__':
	main()
