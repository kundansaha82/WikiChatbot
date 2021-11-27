# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:13:37 2021

@author: kundankantisaha
"""

from elasticsearch import Elasticsearch
import time
from os import popen
import subprocess
import logging
import uuid

def start_cluster():
    
    subprocess.Popen('C:\\Users\\kundansa\\Downloads\\elasticsearch-7.10.2\\bin\\elasticsearch.bat')
    time.sleep(15)
    
    
def connect_elasticsearch():
    es = None
    es = Elasticsearch([{'host': '127.0.0.1', 'port': '9200'}])
    if es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return es

if __name__ == '__main__':
  logging.basicConfig(level=logging.ERROR)

"""start_cluster()
es = connect_elasticsearch()"""


def create_index(es, indexname):
    es.indices.create(index=indexname, ignore=400)

def add_doc(es, indexname, title, link, heading, keywordoriginal):
    new_entry = {
    "title": title,
    "link": link,
    "heading": heading,
    "keywordoriginal": keywordoriginal,
    }
    response = es.index(
    index = indexname,
    doc_type = 'entries',
    id = uuid.uuid4(),
    body = new_entry
    )
    return response

"""def create_doc(es, indexname, title, link, text):
    e1={
    "title":title,
    "link":link,
    "text": text,
    }
    result = es.index(index=indexname,doc_type='entries',id=1,body=e1)
    return result"""

"""result = create_doc(es, "ADQ Support", "https://wiki.ith.intel.com/display/ladtechtme/ADQ+Support",
                   "Application Devices Queues (ADQ) is a networking technology aimed at improving network I/O performance for low-latency applications."
                   )
print(result)

res=es.get(index='wiki',doc_type='entries',id=1)
print(res)"""