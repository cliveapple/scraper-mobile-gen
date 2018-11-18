from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

#using selenium
#must have firefox geckodriver in same dir as project
# a simple proxy for firefox using online free proxy list uk
# again this can be changed to desired country at '5.148.128.44' change with desired ip
'''created by clive hunt date /17/11/2018'''

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", '5.148.128.44')
profile.set_preference("network.proxy.http_port", 8080) #port we want to run on
profile.set_preference("network.proxy.ssl", '5.148.128.44')
profile.set_preference("network.proxy.ssl_port", 8080)
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://''www.facebook.com/login/identify?ctx=recover&lwv=110')


#file to irate through
fname = ('numm.txt')
if len(fname) < 1:
    fname = 'numm.txt'
hand = open(fname)


def one():
    for lin in hand:
        elem = driver.find_element_by_xpath('//*[@id="identify_email"]')
        elem.send_keys(lin)
        sleep(3)
        elem.send_keys(Keys.ENTER)
        sleep(2)
        driver.implicitly_wait(15)


        if lin != elem:
            sleep(2)
            driver.back()



    else:
        sleep(3)
        driver.back()
        print(lin)



one()

