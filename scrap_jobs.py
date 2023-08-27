import helium as he
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import json

# CSS Selectors: https://www.w3schools.com/cssref/css_selectors.php
# Documentacion Helium: https://selenium-python-helium.readthedocs.io/en/latest/
# Cheatsheet Helium: https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md


# options = webdriver.ChromeOptions()

# options.add_argument("--start-maximized")

edge_driver = EdgeChromiumDriverManager().install()

driver = webdriver.Edge(edge_driver)
driver.maximize_window()

he.set_driver(driver)


try:
    he.go_to("https://www.linkedin.com/jobs/search")

    he.wait_until(he.S("body").exists, timeout_secs=2)

    # set parameters

    he.doubleclick(he.S("#job-search-bar-location"))

    he.write("Argentina")

    he.click(he.S("#job-search-bar-keywords"))

    he.write("java jr")

    he.press(he.ENTER)

    he.wait_until(he.S("body").exists, timeout_secs=2)

    # get jobs

    anchor_jobs = he.find_all(he.S("[data-tracking-control-name='public_jobs_jserp-result_search-card']"))

    # save jobs

    with open ('text.txt', 'w', encoding="utf-8") as file:  
        for anchor in anchor_jobs:
            anchor_web_element = anchor.web_element

            # get important data
            link_job = anchor_web_element.get_attribute("href")
            title_job = anchor_web_element.text
            
           #filter jobs
            filter_jobs = ["java", "nodejs", "node.js", "node", "jr", "backend", "fullstack"]  # Filter jobs
            for word in filter_jobs:
                if(word in title_job.lower() or word in link_job.lower()):
                    link_job_title = anchor_web_element.text + " --- " + link_job
                    file.write(link_job_title)  
                    file.write('\n')

    input()
    driver.quit()
except TimeoutError:
    print("La página está atascada. Recargando...")
    driver.refresh()
    

