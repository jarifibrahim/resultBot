''' Some utility functions '''

from bs4 import BeautifulSoup
from urlparse import urljoin
import os
from send_email import send_mail
import urllib
from config import FACULTY
from send_sms import send_sms


def create_dir(directory):
    if not os.path.exists(directory):
        print ('Creating directory ' + directory.split('/')[-2])
        os.makedirs(directory)


def create_file(file_path):
    if not os.path.exists(file_path):
        print ('Creating file ' + os.path.basename(file_path))
        append_to_file("", file_path)


def append_to_file(data, file_name):
    with open(file_name, 'a') as file:
        file.write(data + '\n')


def file_to_set(file_name):
    ''' Read a file and convert each line to set items '''
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def convert_html_to_list(html, base_url, download_folder):
    ''' Converts list of files in html form into a python list of files

        Returns: List of dictionaries each containing name of the file
                 and link to download it.

    '''
    soup = BeautifulSoup(html, 'html.parser')
    if check_result_declared(soup.text):
        return get_individual_name_and_links(soup.find_all('a'),
                                             base_url,
                                             download_folder)
    return []


def check_result_declared(text):
    ''' Returns True if result is declared else False'''
    if text.strip().lower() == 'no record found.':
        msg = ('\033[93m'
               'Results not yet declared. Try again later.'
               '\033[0m')
        print (msg)
        return False
    return True


def get_individual_name_and_links(links, base_url, download_folder):
    ''' Returns list containing name of the file and link to download it '''
    result = []
    for link in links:
        link = link.get('href').decode("utf-8")
        name = urllib.unquote(link.split('/')[-1]).decode("utf-8")
        item = {
            'name': download_folder + name,
            'link': urljoin(base_url, link)
        }
        result.append(item)
    return result


def download_file(file, dl_file_name):
    ''' Download the file and return its name'''
    file_name = file['name']
    file_name_short = os.path.basename(file_name)
    link = file['link']
    print ('Downloading file: "%s"' % file_name_short)
    urllib.urlretrieve(link, file_name)
    print ('"%s" file saved' % file_name_short)
    append_to_file(file_name, dl_file_name)
    return file_name


def prepare_email(file_paths):
    ''' Prepare email to be sent'''
    file_names = [fp.split('/')[-1] for fp in file_paths]
    subject = "NMU " + FACULTY + " Results Found"
    message = "\r\n".join([
        "",
        "Hi There!",
        "I'm ResultBot. I keep searching for NMU results.",
        "I found the following files (see attachments)"
        " related to NMU {} results.".format(FACULTY),
        "",
    ] + file_names)
    end_message = ("\n\n\nYou received this email because you were added to "
                   "the mailing list by Ibrahim Jarif.\nIf you wish to "
                   "unsubscribe, please reply back to this email."
                   "\n\nCheers,\nResultBot")
    message += end_message
    print ("Sending email...")
    send_mail(subject,
              message, files=file_paths)


def prepare_sms(file_paths):
    ''' Prepare sms to be sent'''
    file_names = [fp.split('/')[-1] for fp in file_paths]
    subject = "NMU " + FACULTY + " Results Found"
    message = "\r\n".join([
        "",
        "{}\n".format(subject),
        "Hi There!",
        "I'm ResultBot. I keep searching for NMU results.",
        "I found the following files"
        " related to NMU {} results.".format(FACULTY),
        "",
    ] + file_names)
    end_message = ("\n\nCheers,\n ResultBot")
    message += end_message
    print ("Sending sms...")
    send_sms(message)
