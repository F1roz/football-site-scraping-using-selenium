from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

matches = driver.find_elements(By.TAG_NAME, 'tr')

date =[]
home_team=[]
score= []
away_team= []

for match in matches:
    date.append(match.find_element(By.XPATH, '//tr/td[1]').text)
    home = match.find_element(By.XPATH, '//tr/td[2]').text
    home_team.append(home)
    #print(home)
    score.append(match.find_element(By.XPATH, '//tr/td[3]').text)
    away_team.append(match.find_element(By.XPATH, '//tr/td[4]').text)
driver.quit()
df= pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index = False)
print(df)

time.sleep(180)
#driver.quit()