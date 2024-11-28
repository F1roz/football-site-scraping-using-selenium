from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
path = "/Users/firozfahim/Downloads/chromedriver-mac-arm64/chromedriver"

# Set up Chrome options
chrome_options = Options()

# Set up Chrome driver service
service = Service(executable_path=path)

# Initialize the Chrome driver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, 'country'))
#dropdown.select_by_visible_text('Spain')
country_options= [option.text for option in dropdown.options]
time.sleep(10)



date =[]
home_team=[]
score= []
away_team= []
country_list =[]

for country in country_options:
    dropdown.select_by_visible_text(country)
    time.sleep(15)

matches = driver.find_elements(By.TAG_NAME, 'tr')

for match in matches:
    date.append(match.find_element(By.XPATH, '//tr/td[1]').text)
    home = match.find_element(By.XPATH, '//tr/td[2]').text
    home_team.append(home)
    #print(home)
    score.append(match.find_element(By.XPATH, '//tr/td[3]').text)
    away_team.append(match.find_element(By.XPATH, '//tr/td[4]').text)
    country_list.append(country)

driver.quit()
df= pd.DataFrame({'date': date, 'country':country_list, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index = False)
print(df)

time.sleep(180)
#driver.quit()
