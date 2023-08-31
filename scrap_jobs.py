import helium as he
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
# CSS Selectors: https://www.w3schools.com/cssref/css_selectors.php
# Documentacion Helium: https://selenium-python-helium.readthedocs.io/en/latest/
# Cheatsheet Helium: https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md


def save_jobs_linkedIn(driver):
    he.go_to("https://www.linkedin.com/jobs/search")

    he.wait_until(he.S("body").exists, timeout_secs=2)

    # set parameters

    he.click(he.S("#job-search-bar-location"))

    he.press(he.CONTROL + 'a')
    
    he.write("Argentina")

    he.click(he.S("#job-search-bar-keywords"))

    he.write("java jr")

    he.press(he.ENTER)

    he.wait_until(he.S("body").exists, timeout_secs=2)

    # scroll

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    # get jobs

    anchor_jobs = he.find_all(
        he.S("[data-tracking-control-name='public_jobs_jserp-result_search-card']"))

    # save jobs

    with open('text.txt', 'w', encoding="utf-8") as file:
        for anchor in anchor_jobs:
            anchor_web_element = anchor.web_element

            # get important data
            link_job = anchor_web_element.get_attribute("href")
            title_job = anchor_web_element.text

            # Filter jobs
            filter_jobs = ["java", "java jr", "nodejs", "node.js", "node",
                           "backend", "fullstack"]
            for word in filter_jobs:
                if (word in title_job.lower() or word in link_job.lower()):
                    link_job_title = anchor_web_element.text + " --- " + link_job
                    file.write(link_job_title)
                    file.write('\n')


def save_jobs_indeed(driver):
    he.go_to("https://ar.indeed.com/jobs")
    he.wait_until(he.S("body").exists, timeout_secs=2)

    filter_jobs = ["java", "java jr", "nodejs",
                   "node.js", "node", "backend", "fullstack"]
    anchor_jobs = []

    for page in range(1, 4):

        div_modal = he.S("#mosaic-desktopserpjapopup")
        if div_modal.exists():
            button_close = he.find_all(
                he.S("#mosaic-desktopserpjapopup div button"))[0]
            if button_close.exists():
                he.click(button_close)

        if (page == 1):
            he.click(he.S("#text-input-what"))
            he.press(he.CONTROL + 'a')
            he.write("java jr")

            he.click(he.S("#text-input-where"))
            he.press(he.CONTROL + 'a')
            he.write("Argentina")
            he.press(he.ENTER)

        he.wait_until(he.S("body").exists, timeout_secs=2)

        page_anchors = he.find_all(he.S(".jcs-JobTitle"))

        for anchor in page_anchors:
            anchor_text = anchor.web_element.text
            anchor_link = anchor.web_element.get_attribute("href")

            if any(keyword in anchor_text.lower() or keyword in anchor_link.lower() for keyword in filter_jobs):
                anchor_jobs.append((anchor_text, anchor_link))

        # Click the pagination
        if page < 3:
            pagination = he.find_all(he.S(f"[aria-label='{page + 1}']"))[0]
            he.click(pagination)
            time.sleep(2)

    with open('text.txt', 'a', encoding="utf-8") as file:
        for anchor_text, anchor_link in anchor_jobs:
            file.write(f"{anchor_text} --- {anchor_link}\n")


try:

    edge_driver = EdgeChromiumDriverManager().install()

    driver = webdriver.Edge(edge_driver)
    driver.maximize_window()

    he.set_driver(driver)

    save_jobs_linkedIn(driver)

    print("finish linkedin")
    save_jobs_indeed(driver)
    print("finish ineed")

    print("finish program...")

    input()
    driver.quit()
except TimeoutError:
    print("La página está atascada. Recargando...")
    driver.refresh()
