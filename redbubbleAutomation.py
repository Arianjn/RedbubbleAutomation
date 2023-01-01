import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook, load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

def redbubble_upload():

    chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C://Users/Aryan/AppData/Local/Google/Chrome/User Data') #Path to your chrome profile
    options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.redbubble.com/portfolio/images/72286835-being-a-hero-doesnt-mean-you-are-invincible-it-just-means-youre-brave-enough-to-stand-up-and-do-whats-needed/duplicate")

    timeout = 500000
    try: # Security Checks and shit
        element_present = expected_conditions.presence_of_element_located((By.ID, "work_title_en"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

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

    driver.find_element(By.ID,"rightsDeclaration").click()



    driver.find_element(By.ID,"submit-work").click()

    time.sleep(20)
    # #CenterImage
    # driver.find_element(By.XPATH,"(//div[text()='Edit'])[4]").click()
    #
    # time.sleep(4)
    # element = driver.find_element(By.XPATH,"(//button[text()='Center horizontally'")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()


    driver.quit()

#Redbubble Upload-----------------------------------------------------------------------RedbubbleUpload


