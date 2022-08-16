

from RPA.Browser.Selenium import Selenium

browser = Selenium(auto_close=False)


def minimal_task():
    browser.open_available_browser("https://www.google.com")
    browser.go_to("https://robotsparebinindustries.com/")


if __name__ == "__main__":
    minimal_task()
