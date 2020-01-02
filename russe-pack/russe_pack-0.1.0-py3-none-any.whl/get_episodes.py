# -*- coding: utf-8 -*-
from time import sleep
import os
import threading
import shutil
from queue import Queue

import configparser
from os.path import expanduser

import requests


from bs4 import BeautifulSoup as BSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_credentials(filepath="~/.russianpodcast"):
    filepath = expanduser(filepath)
    config = configparser.ConfigParser()
    config.read(expanduser("~/.russianpodcast"))
    config = config["russianpodcast"]
    return config["emailadress"], config["password"]


def extract_links(wpbs):
    for wpb in wpbs:
        wrapper = wpb.find(class_="wpb_wrapper")
        if wrapper:
            a = wrapper.find("a")
            if a:
                href = a.attrs["href"]
                if href:
                    if href.startswith(
                        "https://russianpodcast.eu/podcast-"
                    ) or href.startswith("https://russianpodcast.eu/dacha-"):
                        yield href


def get_links_to_pages(page_source):
    soup = BSoup(page_source, "lxml")
    items = soup.select("div.wpb_text_column.wpb_content_element")
    sub_pages = [x for x in extract_links(items)]
    return sub_pages


headless = Options()
headless.add_argument("--headless")

print_pdfs_with_default_printer = False  # Uses default printer on linux
target_folder = expanduser("~/klimova_posdcasts")
quiet = True


class PodcastGetter(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        os.chdir(target_folder)  # Use proper context manager instead
        print("init done")

    @property
    def present_files(self):
        return [f for f in os.listdir(".") if os.path.isfile(f)]
    def log_in(self):
        print("logging in ", end=" ")
        import sys

        emailaddress, password = get_credentials()
        sys.stdout.flush()
        driver = self.driver
        driver.get("https://russianpodcast.eu/russian-dacha-club")
        driver.find_element_by_name("email").send_keys(emailaddress)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("LoginDAPLoginForm").click()
        print("logged in")

    def refreshed_page_source(self, delay=2):
        """ This is a heck because getting the content right after login
        gives you le login page content """
        driver = self.driver

        sleep(delay)
        driver.refresh()  # The url is the same so you need to re-fetch the content
        print("refresed")
        sleep(delay)
        source = driver.page_source
        return source

    def get_content_link_from_page(self, page_link):
        driver = self.driver
        driver.get(page_link)
        source = driver.page_source
        soup = BSoup(source, "lxml")
        targets = soup.find_all("j")
        for j in targets:
            a = j.find("a")
            text = a.text.split("'")[-2]
            text = "".join(reversed(text)).replace(" ", ".", 1)
            text = "".join(reversed(text))
            href = a.attrs["href"]
            yield (href, text)

    def fill_links(self, links, q):
        for link in links:
            for href, text in self.get_content_link_from_page(link):
                print(f"got link for  {text}")
                q.put((href, text))
        q.join()

    def fetch_files(self, q):
        while True:
            pill = q.get()
            if pill is None:
                break
            href, text = pill
            if self.filter_file(text):
                print(f"processing {text}")
                self.process_file([href, text])
            else:
                print(f"{text} is already here")
            print(f"processed {text} by {threading.current_thread().name}")
            q.task_done()

    def __call__(self):
        self.log_in()
        page_source = self.refreshed_page_source()
        print("got source")
        print(os.getcwd())
        # page_source = open('../sample.html').read()
        links = get_links_to_pages(page_source)
        q = Queue()
        link_fetcher = threading.Thread(target=self.fill_links, args=(links, q))
        link_fetcher.start()
        files_fetchers = [
            threading.Thread(target=self.fetch_files, name=str(i), args=(q,))
            for i in range(3)
        ]
        for fetcher in files_fetchers:
            fetcher.start()
        link_fetcher.join()
        print("quitted driver")
        self.driver.quit()
        [q.put(None) for fetcher in files_fetchers]
        [fetcher.join() for fetcher in files_fetchers]

    def filter_file(self, filename):
        return filename not in self.present_files

    def process_file(self, files_to_get):
        link, filename = files_to_get

        with open(filename, "wb") as f:
            with requests.get(link, stream=True) as r:
                shutil.copyfileobj(r.raw, f)
            if filename.lower().endswith("pdf") and print_pdfs_with_default_printer:
                print((os.system("lp %s" % filename)))


def main():
    try:
        print("Checking firefox driver is here")
        if quiet:
            driver = webdriver.Firefox(firefox_options=headless)
        else:
            driver = webdriver.Firefox()
    except Exception as E:
        import logging

        logging.exception(E)

        print("Looks like firefox webdriver is not installed")
        print(
            "See https://github.com/mozilla/geckodriver/releases go to assets todownload"
        )
        print(
            "https://stackoverflow.com/questions/42204897/"
            "how-to-setup-selenium-python-environment-for-firefox for more help"
        )
    else:
        print("Yey firefox driver seems installed")
        PodcastGetter(driver)()


if __name__ == "__main__":
    main()
