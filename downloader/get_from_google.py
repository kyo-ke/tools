import argparse
import json
import requests
from bs4 import BeautifulSoup
from urllib import parse
from PIL import Image
import io
import subprocess

#function search returns list of urls
class Google:
    def __init__(self):
        self.g_search_url = 'https://www.google.co.jp/search'
        self.session = requests.session()
        self.session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
    def query_gen(self,keyword,type):
        page = 0
        while 1:
            #num is number of articles which displayed 
            #start is article's number which is displayed first 
            #'tbm' : 'isch' means search engine for images
            if type == 'text':
                params = parse.urlencode({'q':keyword, 'num' : '100', 'filter' : '0', 'start': str(page*100)})
            elif type == 'image':
                params = parse.urlencode({'q' : keyword, 'tbm' : 'isch', 'filter' : '0', 'ijn': str(page)})
            yield self.g_search_url + '?' + params
            page += 1
    def get_links(self,html,type):
        #html is the code which you want to correct
        #laml is the datatype
        soup = BeautifulSoup(html,'lxml')
        if type == 'text':
            elements = soup.select('.rc > .r > a')
            links = [e['href'] for e in elements]
        elif type == 'image':
            #i dont know why but <class = rg_meta notranslate> is written in place where image file is placed
            elements = soup.select('.rg_meta.notranslate')
            #json.loads make jason object to python list 
            #jsons is list ob list
            jsons = [json.loads(e.get_text()) for e in elements]
            links = [js['ou'] for js in jsons]
        return links
    #search can get links of image or text
    def search(self, keyword, type = 'text', maximum = 50):
        print('Google', type.capitalize(),'Search : ',keyword)
        result = []
        total = 0
        query = self.query_gen(keyword,type)
        while 1:
            html = self.session.get(next(query)).text
            links = self.get_links(html,type)
            if not len(links):
                print('no more links')
                break
            elif len(links) > maximum - total:
                result += links[:maximum - total]
                break
            else:
                result += links
                total += len(links)
        print('result : you get',str(len(result)), 'links')
        return result


#urls is lists of image's url
#out_dir is directory which you want to save images
def download_img(urls,out_dir):
    session = requests.session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
    try:
        subprocess.call(['mkdir',out_dir])
    except:
        pass
    for i in range(len(urls)):
        try:
            content = session.get(urls[i]).content
            file_name = out_dir + '/' + 'n_' + str(i) + '.png'
            f = open(file_name,'wb')
            f.write(content)
            f.close()
        except:
            pass
    return

'''

if you want to use byteobject as file you can use io.BytesIO(byte_like_object)
img_bin = io.BytesIO(content)
img = Image.open(img_bin)

'''


def main():
    engine = Google()
    '''
    important variations
    '''
    get_type = 'image'
    keyword = 'cat'
    out_dir = 'test'
    urls = engine.search(keyword,get_type)
    download_img(urls,out_dir)
    return 

main()