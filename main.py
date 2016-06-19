#!/usr/bin/python

from selenium import webdriver
from general import *
from datetime import datetime
from config import FACULTY, DL_FOLDER, DL_FILE_NAME, PATH_TO_PHANTOMJS, \
    BASE_URL


def get_file_list():
    ''' Utility function to get list of available files on result website '''
    driver = webdriver.PhantomJS(PATH_TO_PHANTOMJS)
    print "Downloading web page"
    driver.get(BASE_URL)
    print "Web Page downloaded"
    try:
        element = driver.find_element_by_link_text(FACULTY)
        element.click()
        file_list_html = driver.find_element_by_id(
            'FileList').get_attribute('innerHTML')
    except Exception as e:
        import ast
        import shutil
        msg = ("\033[91m" + "Something went wrong. Check faculty name. "
               "ERROR: " + ast.literal_eval(e.msg)['errorMessage'] + "\033[0m"
               "\nDeleting directory " + DL_FOLDER.split('/')[-2])
        print msg
        shutil.rmtree(DL_FOLDER)
        exit()
    finally:
        driver.close()
    return convert_html_to_list(file_list_html, BASE_URL, DL_FOLDER)


def get_files(files, dl_file_name):
    ''' Download files only if the do not exist '''
    downloaded_file_names = file_to_set(dl_file_name)
    if not files:
        print 'No files found to download.'
        return None
    new_files = []
    for file in files:
        if file['name'] in downloaded_file_names:
            print 'File "{}" is already downloaded.'.format(
                os.path.basename(file['name']))
            continue
        new_files.append(download_file(file, dl_file_name))
    return new_files


def setup():
    print '\n' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print '=' * 40
    print "Fetching results related to " + FACULTY + " faculty"
    create_dir(DL_FOLDER)
    create_file(DL_FILE_NAME)


def main():
    setup()
    files = get_file_list()
    new_files = get_files(files, DL_FILE_NAME)
    if new_files:
        print 'Preparing email to send new files'
        prepare_email(new_files)
    else:
        print 'No new files to mail.'

if __name__ == '__main__':
    main()
