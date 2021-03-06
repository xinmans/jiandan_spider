import requests
import time
import datetime
import os
from bs4 import BeautifulSoup
import re

pages = ['girl', 'ooxx', 'pic', 'top', 'pond']
pic_foldoer = '/data'

def get_url(url, page):
    html = requests.get(url,timeout=(3.05, 15)).text
    soup = BeautifulSoup(html, 'lxml')
    img_arr = soup.find_all('img')
    try:
        next_page = 'https:' + soup.find('a', class_='previous-comment-page')['href'].split('#')[0]
    except:
        next_page = ''

    download_jpg(img_arr, next_page, page)


def download_jpg(images, next_html, page):
    for img in images:
        img_url = 'https:' + img['src']
        img_name = img['src'].split('/')[-1]
        img_extension = img_url[-3:]
        if img_extension.lower() != 'jpg' and img_extension.lower() != 'png':
            continue
        save_name = pic_foldoer + '/' + page + '_photos_unduplicate' + '/{}'.format(img_name)
        try:
            img_info = requests.get(img_url,timeout=(3.05, 15)).content
        except:
            continue
        create_folder(save_name)
        if save_name != '' and not os.path.exists(save_name):
            print(" [ %s ] downloading  " % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + img_url)
            with open(save_name, 'wb') as f:
                f.write(img_info)
        else:
            break
    if len(next_html):
        get_url(next_html, page)

def create_folder(folder_name):
    path = os.path.split(folder_name)[0]
    if path != '' and not os.path.exists(path):
        os.makedirs(path)

def start(page):
    url1 = "https://jandan.net/" + page
    
    print(" [ %s ] start downloading pics from "  % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + url1)
    get_url(url1, page)


if __name__ == '__main__':
    try:
        for page in pages:
            start(page)
    except Exception as e:
        print(e)
    finally:
        print('end\n')
