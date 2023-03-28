
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#site credentials
username = "87241870dr"
password = "*******"
item = "	KKM11-018-400-10"

# initialize the Chrome driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome("chromedriver", options=chrome_options)

#open full screen browser
driver.maximize_window()

# head to login page
driver.get("https://www.etm.ru/ipro3/actions")
#find the login button
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button["
                                                                                      "@data-testid='authorization-button']"))).click()

# find username/email field and send the username itself to the input field
driver.find_element(By.NAME, "login").send_keys(username)
# find password input field and insert password as well
driver.find_element(By.NAME, "password").send_keys(password)
# click login button
driver.find_element(By.XPATH, "//button[""@data-testid='go-to-system']").click()
# find search input field and insert item's article as well
search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Умный поиск по названию, артикулу, свойству, производителю'].MuiInputBase-input.MuiInputBase-inputAdornedStart")

#activate the search input field by first clicking it
action = ActionChains(driver)
action.click(search_input).perform()

#enter the search query into the input field
search_input.send_keys(item)
