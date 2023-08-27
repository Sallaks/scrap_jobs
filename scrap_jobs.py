import helium as he
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# CSS Selectors: https://www.w3schools.com/cssref/css_selectors.php
# Documentacion Helium: https://selenium-python-helium.readthedocs.io/en/latest/
# Cheatsheet Helium: https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md


# options = webdriver.ChromeOptions()

# options.add_argument("--start-maximized")

edge_driver = EdgeChromiumDriverManager().install()

driver = webdriver.Edge(edge_driver)
driver.maximize_window()

he.set_driver(driver)

he.go_to("https://www.linkedin.com")


positionIconJob = 4
# while(not(he.find_all(he.S('li'))) == []):
#     he.go_to("https://www.linkedin.com")

# he.wait_until(he.find_all(he.S('li')))

elementExists = False

ul_icon_job = None

while not elementExists:
    if (he.find_all(he.S('li'))):
        ul_icon_job = (he.find_all(he.S('li'))[positionIconJob])
        he.click(ul_icon_job)
        elementExists = True

he.wait_until(he.S("#job-search-bar-keywords").exists)

he.click(he.S("#job-search-bar-keywords"))

he.write("java jr")

# ul_icon_job = (he.find_all(he.S('li'))[positionIconJob])

# he.click(ul_icon_job)

# he.click("#job-search-bar-keywords")

# he.write("java jr")


# input()
# # driver.quit()
