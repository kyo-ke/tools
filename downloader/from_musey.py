import argparse
import json
import requests
from bs4 import BeautifulSoup
from urllib import parse
from PIL import Image
import io
import subprocess

class MUSEY:
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
    
    def get_pages(self,html):
        soup = BeautifulSoup(html,'lxml')
        elements = soup.find_all(class_="page-numbers")
        links = []
        for i in range(len(elements)):
            if len(elements[i]['class']) == 1:
                links.append(elements[i]['href'])
        return links
    
    def get_imageplace(self, l):
        lis = [i for i in range(len(l))]
        for i in lis[::-1]:
            t_4 = l[len(l[i])-4:len(l[i])]
            t_3 = l[len(l[i])-4:len(l[i])]
            if t_3 == 'png' or t_3 == 'jpg':
                return l[i]
            elif t_4 == 'jpeg':
                return l[i]
        return -1
            




    def get_elements(self,html):
        soup = BeautifulSoup(html,'lxml')
        elements = soup.find_all(class_="attachment-medium size-medium wp-post-image")
        urls = []
        for i in range(len(elements)):
            s_el = str(elements[i]).split()
            url = s_el[len(s_el)-3]
            urls.append(url)
        return urls
    
    def download_img(self,urls,out_dir):
        try:
            subprocess.call(['mkdir',out_dir])
        except:
            pass
        for i in range(len(urls)):
            try:
                content = self.session.get(urls[i]).content
                file_name = out_dir + '/' + 'n_' + str(i) + '.png'
                f = open(file_name,'wb')
                f.write(content)
                f.close()
                print('save image done')
            except:
                print('cant get image')
        return

    def search(self,artist_url,out_dir):
        print('start downloading')
        counter = 1
        all_url = []
        print('page {}'.format(counter))
        html = self.session.get(artist_url).text
        pages = self.get_pages(html)
        urls = self.get_elements(html)
        all_url.extend(urls)
        print(type(pages))
        for i in range(len(pages)):
            counter += 1
            print('page {}'.format(counter))
            html = self.session.get(pages[i]).text
            urls = self.get_elements(html)
            all_url.extend(urls)
        self.download_img(all_url,out_dir)

    
out_dir = 'test'
artist_url = 'https://www.musey.net/artist/97'
musey = MUSEY()
musey.search(artist_url,out_dir)