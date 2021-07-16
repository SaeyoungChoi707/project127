from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/sudhe/OneDrive/Pictures/CODING!!/Python/Projects/c127,128,129 projects")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ["name","distance","mass","radius"]
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for th_tag in soup.find_all("th",attrs={"class","exoplanet"}):
            tr_tags = th_tag.find_all("tr")
            templist = []
            for index,tr_tag in enumerate(tr_tags):
                if index == 0:
                    templist.append(tr_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(tr_tag.contents[0])
                    except:
                        templist.append("")
            planet_data.append(templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open ("scrapper2.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()