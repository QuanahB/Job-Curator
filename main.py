# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
import random
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests



driver = webdriver.Chrome(executable_path='/Users/quanahbennett/PycharmProjects/RecursivePractice/chromedriver')
url= "https://www.indeed.com/jobs?q=developer&l=Westbury%2C%20NY&vjk=0b0cbe29e5f86422"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
officials = soup.findAll("a",{"class":"tapItem"})
#links = [a['href'] for a in soup.find_all('a', href=True)]
#results = soup.findAll("href")
#f= open("guru99.txt","w+")

#for entry in officials:
    #f.write(str(entry.text))
    #print(str(entry))
    #print(' ')

#for official in officials:
    #jobTitle = soup.find('h2',{'class': 'jobTitle'}).text
    #companyName = soup.find('div',{'class': 'comapny_location'})
    #location = soup.find('div',{'class': 'companyLocation'}).text
    #salary = soup.find('div',{'class': 'salary-snippet'})
    #actualSalary = salary.find('span').text
    #summary = soup.find('div',{'class': 'job-snippet'}).text

    #print('Title: ' + str(jobTitle) + '\nCompany Name: ' + str(companyName) + '\nLocation: ' + str(location)
          #+ '\nSalary: ' + str(actualSalary) + "\nSummary: " + str(summary))
    #print(str(official))
    #print(' ')

for i in range(len(officials)):
    jobTitle = soup.findAll('h2',{'class': 'jobTitle'})[i].text

    companyName = soup.findAll('div',{'class': 'comapny_location'})[i].text if len(soup.findAll('div',{'class': 'comapny_location'})) > i else "NULL"
    location = soup.findAll('div',{'class': 'companyLocation'})[i].text if len(soup.findAll('div',{'class': 'companyLocation'})) > i else "NULL"
    salary = soup.findAll('div',{'class': 'salary-snippet'})[i].text if len(soup.findAll('div',{'class': 'salary-snippet'})) > i else "NULL"
    actualSalary = salary.find('span')
    summary = soup.findAll('div',{'class': 'job-snippet'})[i].text if len(soup.findAll('div',{'class': 'job-snippet'})) > i else "NULL"

    print('Title: ' + str(jobTitle) + '\nCompany Name: ' + str(companyName) + '\nLocation: ' + str(location)
        + '\nSalary: ' + str(actualSalary) + "\nSummary: " + str(summary))
    print(' ')


driver.close()

print(' ')
print('-----------------------')
print(' ')

#driver2 = webdriver.Chrome(executable_path='/Users/quanahbennett/PycharmProjects/RecursivePractice/chromedriver')
#url2= "https://www.ziprecruiter.com/candidate/search?search=developer&location=Westbury%2C+NY"
#driver2.maximize_window()
#driver2.get(url2)

#time.sleep(5)
#content2 = driver2.page_source.encode('utf-8').strip()
#soup2 = BeautifulSoup(content2,"html.parser")
#results = soup2.findAll("div",{"class":"job_content"})

#for result in results:
    #title = soup2.find('span',{'class': 'just_job_title'}).text
    #print(str(title))

#driver2.quit()


