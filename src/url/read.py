from urllib.parse import urlparse
from meta import filemeta
from lxml import html
import requests
import json


def getDomain(url):
    return urlparse(url).netloc
     
def read(url): 
    page = requests.get(url)
    tree = html.fromstring(page.content)
    domain = getDomain(url)
    content = tree.xpath(filemeta.getXPath(url=domain))
    article = json.loads(content[filemeta.getPos(url=domain)], strict=False)[0][filemeta.getJson(url=domain)]
    return article

    