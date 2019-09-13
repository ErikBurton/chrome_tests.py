from selenium import webdriver

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://erikb.herokuapp.com")

ff = RunChromeTests()
ff.test()
