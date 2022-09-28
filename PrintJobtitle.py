import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\uhiregou\\PycharmProjects\\FirstProject\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://jobs.hp.com/software-engineer-one/?job_type[]=Experienced&business_unit[]=china&sort=title&dir=ascending")
driver.maximize_window()
element = driver.find_element(By.XPATH,"//div[contains(text(),'Showing Jobs')]")
length=int(((element.text)[23:]))
temp=0
for i in range(length):
     elements = driver.find_elements(By.CLASS_NAME, "jobTitle")
     temp = temp + len(elements)
     for i in elements:
         print(i.text)
     if(length==temp):
         break
     driver.find_element(By.XPATH, "//a[@class='button inactive btn-next']").click()
     time.sleep(10)
driver.close()
