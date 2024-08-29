from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import yaml

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.youtube.com")
actions = ActionChains(driver)
driver.maximize_window()

search_bar = driver.find_element(By.NAME, 'search_query')
search_bar.click()
search_bar.send_keys("The snore meme")
search_bar.submit()

#snore meme maker

result = driver.find_element(By.LINK_TEXT, 'TikTok snoring (ORIGINAL MEME SOUND EFFECT)')
print(result)
result.click()

time.sleep(10)

driver.quit()







