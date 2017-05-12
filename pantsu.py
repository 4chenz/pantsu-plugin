import re
from helpers import retrieve_url, download_file
from novaprinter import anySizeToBytes

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

        while True:
            url = 'https://nyaa.pantsu.cat/search/{}?c='.format(page)+pantsu.supported_categories[cat]+'&q='+what
            url = retrieve_url(url)
            regex_things = re.findall(r'<tr class="torrent-info(.*?)</tr>', url, re.M|re.I|re.S)
            for x in range(len(regex_things)):
                for url in re.findall(r'href=[\'"]?([^\'" >]+)', regex_things[x]):
                    if 'magnet' in url:
                        Link=url
                name=re.findall(r'<td class="name">(.*?)</a>', regex_things[x], re.M|re.I|re.S)
                name=name[0].split('\n')[2]
                size = re.findall(r'<td class="hidden-xs filesize">(.*?)</td>', regex_things[x], re.M|re.I|re.S)
                size=size[0]#.replace('[','').replace(']','')
                seeds=re.findall(r'<b class="text-success">(.*?)</b>', regex_things[x], re.M|re.I|re.S)[0]
                leech=re.findall(r'<b class="text-danger">(.*?)</b>', regex_things[x], re.M|re.I|re.S)[0]
                print(Link+'|'+name+'|'+str(anySizeToBytes(size))+'|'+seeds+'|'+leech+'|'+pantsu.engine_url)
            page+=1
            if len(regex_things) < 50:
                break
