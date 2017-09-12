from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functools import partial

def main(hosts, inp):

    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(hosts)
    if 'ebay' in driver.current_url:
        print 'opened ebay'
        search_box = driver.find_element_by_id('gh-ac')
        search_box.clear()
        search_box.send_keys(inp)
        search_box.send_keys(Keys.RETURN)

    elif 'google' in driver.current_url:
        print 'opened google'
        search_box = driver.find_element_by_id('gbqfq')
        search_box.clear()
        search_box.send_keys(inp)
        search_box.send_keys(Keys.RETURN)

    elif 'etsy' in driver.current_url:
        print 'opened etsy'
        search_box = driver.find_element_by_id('search-query')
        search_box.clear()
        search_box.send_keys(inp)
        search_box.send_keys(Keys.RETURN)

    elif 'amazon' in driver.current_url:
        print 'opened amazon'
        search_box = driver.find_element_by_id('twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(inp)
        search_box.send_keys(Keys.RETURN)

    else:
        print "--NONE--"

    # driver.close()

if __name__ == '__main__':
    hosts = ["http://ebay.com", "https://www.google.com/shopping?hl=en", "http://etsy.com", "http://amazon.com"]
    num_hosts = len(hosts)
    inp = raw_input("What do you want to search?: ")
    p = Pool(num_hosts)
    partial_main = partial(main, inp=inp)
    p.map(partial_main, hosts)
    p.close()
    p.join()
