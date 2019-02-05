#!/usr/bin/python

from selenium import webdriver 
from selenium.common.exceptions import TimeoutException, \
    NoSuchElementException
from general import *
from datetime import datetime
from config import FACULTY, DL_FOLDER, DL_FILE_NAME, PATH_TO_PHANTOMJS, \
    BASE_URL, NOTIFY_VIA_MAIL, NOTIFY_VIA_SMS

def get_file_list(): 
    ''' Utility function to get list of available files on result website '''
    driver = webdriver.PhantomJS(PATH_TO_PHANTOMJS)
    print ("Downloading web page")
    driver.set_page_load_timeout(10)
    file_list_html = ''
    try:
        driver.get(BASE_URL)
        print ("Web Page downloaded")
        element = driver.find_element_by_link_text(FACULTY)
        element.click()
        file_list_html = driver.find_element_by_id(
            'FileList').get_attribute('innerHTML')
        msg = 'Searching for results'
    except TimeoutException as e:
        import ast
        msg = ("Result website took too long to respond"
               " ( >10sec). Please try again later.")
        msg += "\n" + ast.literal_eval(e.msg)['errorMessage']
    except NoSuchElementException as e:
        import ast
        msg = ("Structure of result website has changed. Please contact "
               "jarifibrahim@gmail.com to fix this issue.")
        msg += "\n" + ast.literal_eval(e.msg)['errorMessage']
    except Exception as e:
        import ast
        msg = "Something went wrong. Check faculty name."
        msg += "\n" + ast.literal_eval(e.msg)['errorMessage']
    finally:
        print ("\033[91m" + msg + "\033[0m")
        driver.close()
    return convert_html_to_list(file_list_html, BASE_URL, DL_FOLDER)


def get_files(files, dl_file_name):
    ''' Download files only if the do not exist '''
    downloaded_file_names = file_to_set(dl_file_name)
    if not files:
        print ('No files found to download.')
        return None
    new_files = []
    for file in files:
        if file['name'] in downloaded_file_names:
            print ('File "{}" is already downloaded.'.format(os.path.basename(file['name'])))
            continue
        new_files.append(download_file(file, dl_file_name))
    return new_files


def setup():
    print ('\n' + str(datetime.now().strftime('%d-%b-%Y %H:%M:%S')))
    print ('=' * 40)
    print ("Fetching results related to " + FACULTY + " faculty")
    create_dir(DL_FOLDER)
    create_file(DL_FILE_NAME)


def main():
    setup()
    files = get_file_list()
    new_files = get_files(files, DL_FILE_NAME)
    if new_files:
        if NOTIFY_VIA_MAIL:
            print ('Preparing email to send new files')
            prepare_email(new_files)
        if NOTIFY_VIA_SMS:
            print('Preparing sms for notify')
            prepare_sms(new_files)
    else:
        print ('No new files to mail.')

if __name__ == '__main__':
    main()
