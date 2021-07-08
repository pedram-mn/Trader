import time
from selenium import webdriver
import csv
import datetime

now = ""


def get_price():
    driver = webdriver.Chrome(executable_path=r".\chromedriver.exe")
    driver.get("https://ethereumprice.org/live/")

    def initializing():
        global now
        try:
            p = driver.title
            now = str(datetime.datetime.now())[:-7]
            return float(p[2:10].replace(",", ""))
        except:
            return "An error occurred"

    while 1:
        with open("price_log.csv", "a") as f_price:
            writer = csv.DictWriter(f_price, fieldnames=["Date", "Price($)"])
            price = initializing()
            writer.writerow({"Date": now, "Price($)": price})
            print(now, price)
            now = ""
            time.sleep(2)
get_price()