from re import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
import time
#doneby-yashshahcba19162101034
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")
time.sleep(1)
username =driver.find_element_by_xpath("//input[@name='username']")
user=input("enter the email to check:")
username.send_keys(user)
time.sleep(2)
passwd =driver.find_element_by_xpath("//input[@name='password']")
passwd.send_keys("tstauto12")
time.sleep(3)
login=driver.find_element_by_xpath("//div[contains(text(),'Log In')]")
login.click()
try: 
  driver.find_element_by_xpath("/html//p[@id='slfErrorAlert']")
  print("account  found")
except Exception as e:
  print("account not found")
time.sleep(2)
