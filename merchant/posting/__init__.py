#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import numpy as np

username = "frictionpetra@gmail.com"
password = "goOnFire@seaparks"

def lag_template(loc, scale):
    lag_time = np.random.normal(loc = loc, scale = scale)
    if lag_time < 0:
        lag_time = lag_time * -2

    sleep(lag_time)

def page_lag():
    lag_template(loc = 2, scale = 0.5)

def link_lag():
    lag_template(1.5, 1.2)

def typing_lag(loc = 0.1, scale = 0.05):
    lag_template(loc, scale)

def enter_text(text, input_field):
    for character in text:
        input_field.send_keys(character)
        typing_lag()

#%%
driver = webdriver.Chrome()
driver.get("https://stlouis.craigslist.org/")
page_lag()
account_button=driver.find_element(By.LINK_TEXT,"my account")
account_button.click()
page_lag()
username_field = driver.find_element(By.ID, "inputEmailHandle")
password_field = driver.find_element(By.ID, "inputPassword")
enter_text(username, username_field)
link_lag()
enter_text(password, password_field)
typing_lag()
password_field.send_keys(Keys.ENTER)

# %%
