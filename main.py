import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

YOUR_EMAIL = YOUR_EMAIL
YOUR_PASSWORD = YOUR_PASSWORD
URL = "https://tinder.com/app/recs"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
time.sleep(2)
accept_button = driver.find_element(by=By.XPATH, value='//*[@id="u-684883901"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()
login_button = driver.find_element(by=By.LINK_TEXT, value="Log in")
login_button.click()
time.sleep(2)
facebook_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Log in with Facebook'")
facebook_button.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

try:
    cookie_button = driver.find_element(by=By.CSS_SELECTOR, value="button[value='1'][title='Allow all cookies']")
except NoSuchElementException:
    cookie_button = driver.find_element(by=By.CSS_SELECTOR, value=".x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft")
cookie_button.click()

email = driver.find_element(by=By.CSS_SELECTOR, value="#email")
email.send_keys(YOUR_EMAIL)
password = driver.find_element(by=By.CSS_SELECTOR, value="#pass")
password.send_keys(YOUR_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(driver.window_handles[0])
time.sleep(10)
allow_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Allow']")
allow_button.click()
time.sleep(2)
notif_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='I’ll miss out']")
notif_button.click()
time.sleep(2)

out_of_swipes_check = 0
for i in range(1, 50):
    if out_of_swipes_check < 3:
        try:
            like_button = driver.find_element(by=By.CSS_SELECTOR, value="[class*='Bgi($g-ds-background-like)']")
            time.sleep(0.3)
            like_button.click()
        except ElementClickInterceptedException:
            try:
                close_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-hidden='false']")
                close_button.click()
                out_of_swipes_check += 1
            except ElementClickInterceptedException:
                second_button = driver.find_element(by=By.XPATH, value='//*[@id="o-1212681679"]/main/div/div/div[3]/button[2]')
                second_button.click()
                out_of_swipes_check += 1
        except NoSuchElementException:
            not_interested_button = driver.find_element(by=By.CSS_SELECTOR, value="button[data-size='large']")
            not_interested_button.click()
    else:
        driver.quit()
