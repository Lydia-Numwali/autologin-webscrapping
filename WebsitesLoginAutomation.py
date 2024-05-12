from selenium import webdriver
import yaml

conf = yaml.safe_load(open('loginDetails.yml'))
myFbEmail = conf['tcg_user']['email']
myFbPassword = conf['tcg_user']['password']

driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()

login("http://www.tcgplayer.com/", "input-2b78eed9-97ee-40bc-aafa-0e0e19d53649", myFbEmail, "input-d7e4505c-148e-4d7d-ad62-024c98a8faaa", myFbPassword, "signIn")