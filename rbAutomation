import time

from selenium import webdriver


import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C://Users/Aryan/AppData/Local/Google/Chrome/User Data') #Path to your chrome profile
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=options)


driver.get("https://www.redbubble.com/portfolio/images/72286835-being-a-hero-doesnt-mean-you-are-invincible-it-just-means-youre-brave-enough-to-stand-up-and-do-whats-needed/duplicate")

#Input Title
driver.find_element(By.ID, "work_title_en").clear()
driver.find_element(By.ID, "work_title_en").send_keys("Titles")

#Input Tags
driver.find_element(By.ID, "work_tag_field_en").clear()
driver.find_element(By.ID, "work_tag_field_en").send_keys("Tags")

#Input Description
driver.find_element(By.ID, "work_description_en").clear()
driver.find_element(By.ID, "work_description_en").send_keys("Description")

#InsertImage
driver.find_element(By.ID, "select-image-base").send_keys(r"C:\Users\Aryan\Downloads\IMG_9345.jpg")

time.sleep(10)

driver.quit()

