#VERSION: 1.09
#AUTHORS: anon
import re
from helpers import retrieve_url, download_file
from novaprinter import prettyPrinter
import json
class pantsu(object):
    url = 'https://nyaa.pantsu.cat'
    name = 'pantsu'
    supported_categories = {'all': '_',
                            'anime': '3_',
                            'books': '4_',
                            'music': '2_',
                            'pictures': '6_',
                            'software': '1_',
                            'games': '1_2'}
    engine_url='pantsu'
    def __init__(self):
        pass
    def download_torrent(self, info):
        print(download_file(info))
    def search(self, what, cat='all'):
        page=1
        per_page=100#don't change for now
        while True:
            url = 'https://nyaa.pantsu.cat/api/search/'+str(page)+'?c='+self.supported_categories[cat]+'&q='+what+'&limit='+str(per_page)
            link = json.loads(retrieve_url(url))
            for animu in link:
                dic={}
                dic['link'] = animu['magnet']
                dic['name'] = animu['name']
                dic['size'] = str(animu['filesize'])+'B'
                dic['seeds']= animu['seeders']
                dic['leech']= animu['leechers']
                dic['engine_url']=self.engine_url
                prettyPrinter(dic)
            page+=1
            if len(link) < per_page:
                print(len(link))
                break
