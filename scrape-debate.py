import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
import numpy as np

#Term for the cases being looked at if looking at SCOTUS cases
url_19 = 'https://www.oyez.org/cases/2019' 
url_18 = 'https://www.oyez.org/cases/2018'
url_17 = 'https://www.oyez.org/cases/2017'
url_16 = 'https://www.oyez.org/cases/2016'
url_15 = 'https://www.oyez.org/cases/2015'
url_14 = 'https://www.oyez.org/cases/2014'

#Debate links
presidential_debate = 'https://www.debates.org/voter-education/debate-transcripts/'

#list of debate texts
debate_text = []

#Render Page Approach for Supreme Court Cases

opinions_xpath = '/html/body/div/div/div[3]/main/div/div/div/div/div/div[2]'

debate2020_xpath = '/html/body/div/div[6]/div[2]/blockquote[1]'

cases_list = []
list_of_cases = []

s = HTMLSession()
r = s.get(url_19)
 
r.html.render(sleep = 1)

cases = r.html.xpath('/html/body/div/div/div[3]/main/article/div/ng-include/ul', first = True)
cases_list = cases.absolute_links 
cases_list = list(cases_list)

for case in cases_list:
    if(len(case) > 0):
        test_case = str(case)
        new_string = test_case.replace('/cases', '', 1)
        list_of_cases.append(new_string)

#Presidential Debate Scraping

g = s.get(presidential_debate)

g.html.render(sleep = 1)

debate = g.html.xpath(debate2020_xpath, first = True)
debate_list = debate.absolute_links
debate_list = list(debate_list)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(debate_list[1])
text = driver.find_element(By.ID, "content-sm").text
text = text.split()
df = pd.DataFrame(text)
df.to_csv("debate_text.csv")

driver.quit()
















