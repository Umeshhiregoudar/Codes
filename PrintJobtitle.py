import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\uhiregou\\PycharmProjects\\FirstProject\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://jobs.hp.com/software-engineer-one/?job_type[]=Experienced&business_unit[]=china&sort=title&dir=ascending")
driver.maximize_window()
elements = driver.find_elements(By.CLASS_NAME,"jobTitle")
for i in elements:
    print(i.text)
while(True):
    try:
        driver.find_element(By.XPATH,"//a[@class='button inactive btn-next']").click()
    except:
        break
    time.sleep(10)
    elements = driver.find_elements(By.CLASS_NAME,"jobTitle")
    for i in elements:
        print(i.text)
driver.close()




