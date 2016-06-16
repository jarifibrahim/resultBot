from selenium import webdriver
from bs4 import BeautifulSoup
from urlparse import urljoin

URL = 'http://exam.nmu.ac.in/online%20result/aspx/online%20result.aspx'
FACULTY = 'Law'
def get_file_list():
    ''' Utility function to get list of available files on result website '''
    driver = webdriver.PhantomJS('./phantomjs')
    print "Downloading web page"
    driver.get(URL)
    print "Web Page downloaded"
    element = driver.find_element_by_link_text(FACULTY)
    element.click()
    file_list_html = driver.find_element_by_id('FileList').get_attribute('innerHTML')
    driver.close()
    return convert_html_to_list(file_list_html)
    
def convert_html_to_list(html):
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    if soup.text.strip().lower() == 'no record found.':
  	print 'Results not yet declared'
        exit()
    for link in soup.find_all('a'):
  	item = {
            'Name' : link.text,
            'Link' : urljoin(URL, link.get('href'))
        }
        result.append(item)
    return result
 
for item in get_file_list():
    print item
