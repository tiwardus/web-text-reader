import os

INIT = False
info = {}
def init():
    global INIT
    if not INIT:
        f = open('/Users/tiwardus/code/web-text-reader/metadata/finance-meta.txt', 'r')
        for x in f:
            meta = x.split('|')
            info.update({meta[0] : {'xpath' : meta[1],
                                    'pos' : int(meta[2]),
                                    'json' : meta[3]
                                    }})
        INIT = True
        f.close()
        
    
    
def getXPath(url):
    init()
    return info.get(url).get('xpath')
    
def getPos(url):
    init()
    return info.get(url).get('pos')
    
def getJson(url):
    init()
    return info.get(url).get('json')

        
    