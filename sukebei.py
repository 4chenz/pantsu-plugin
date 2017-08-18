#VERSION: 1.12
#AUTHORS: anon
import re
from helpers import retrieve_url, download_file
from novaprinter import prettyPrinter
import json
class sukebei(object):
    url = 'https://sukebei.pantsu.cat'
    name = 'sukebei'
    supported_categories = {'all': '_',
                            'anime': '1_1',
                            'books': '4_',
                            'pictures': '1_',
                            'games': '1_3'}
    engine_url='sukebei'
    def __init__(self):
        pass
    def download_torrent(self, info):
        print(download_file(info))
    def search(self, what, cat='all'):
        page=1
        per_page=100
        while True:
            url = self.url+'/api/search/?c='+self.supported_categories[cat]+'&q='+what+'&limit='+str(per_page)+'&page='+str(page)
            link = json.loads(retrieve_url(url))
            for animu in link['torrents']:
                dic={}
                dic['link'] = animu['magnet']
                dic['name'] = animu['name']
                dic['size'] = str(animu['filesize'])+'B'
                dic['seeds']= animu['seeders']
                dic['leech']= animu['leechers']
                dic['engine_url']=self.engine_url
                prettyPrinter(dic)
            page+=1
            if len(link['torrents']) < per_page:
##                print(len(link))
                break
