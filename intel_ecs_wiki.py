# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:38:30 2021

@author: kundankantisaha
"""
from elasticsearch import Elasticsearch
import time
import subprocess
import logging
import uuid
import scrapy
"""from scrapy.spiders import CrawlSpider"""
from scrapy import Request
from collections import defaultdict
import urllib.parse
import re
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from lemma_tokenizer import Splitter as Splitter
from lemma_tokenizer import LemmatizationWithPOSTagger as LemmatizationWithPOSTagger
import json
import lemma_tokenizer

def start_cluster():
    
    subprocess.Popen('C:\\Users\\kundansa\\Downloads\\elasticsearch-7.10.2\\bin\\elasticsearch.bat')
    """time.sleep(15)"""
    
    
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
    result = es.index(
    index = indexname,
    doc_type = 'entries',
    id = uuid.uuid4(),
    body = new_entry
    )
    return result



class EcsWiki(scrapy.Spider):
    name='ecs_wiki_mod'
    url1='StartPageofWiki'
    indexname='wikifinal'
    allowed_domains = ["subdomain.domain.TLD"]

    
    """def __init__(self, *args, **kwargs):
        super(CrawlSpider, self).__init__(*args, **kwargs)"""
    
    def start_elastic():
        start_cluster()

        es = connect_elasticsearch()
        create_index(es, 'wikifinal')
        return es
    
    es = start_elastic()
    
    

    def start_requests(self):
        curl_string1 = 'curl -H "Authorization: Basic a3VuZGFuc2E6QW5pS3VuQDk5MDM="  -X GET -H "Content-Type: application/json" '+self.url1
        
        request = Request.from_curl(curl_string1, callback = self.parse)
        yield request
    
    def url_correcter(self, link):
        o = urllib.parse.urlsplit(link)
        u = urllib.parse.SplitResult(
            scheme=o.scheme if o.scheme else "https",
            netloc=o.netloc if o.netloc else "wiki.ith.intel.com",
            path=o.path if o.path else "",
            query=o.query if o.query else "",
            fragment=o.fragment if o.fragment else ""
            )
        p = urllib.parse.urlunsplit(u)
        return p

    
    def parse_recursive(self, response):
        wikicontent=str(response.xpath("//div[@class='wiki-content']").extract())
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', wikicontent)
        anchortext = re.findall('''<a(?:[^>]*>)([^<]*)''', wikicontent)
        return links, anchortext    

    def lemmatization_input(self,strings):
        
        lemma_tokenizer.input_string = strings
        found_terms = list() 
    
        splitter = Splitter()
        lemmatization_using_pos_tagger = LemmatizationWithPOSTagger()

        #step 1 split document into sentence followed by tokenization
        tokens = splitter.split(strings)

        #step 2 lemmatization using pos tagger 
        lemma_pos_token = lemmatization_using_pos_tagger.pos_tag(tokens)
        with open('list_tokens.json', 'w') as f:
            for lemmaset in lemma_pos_token:
                for i in range(len(lemmaset)):
                    data = {}
                    data["words"] = []
                    data["words"].append({
                        "Original Word": lemmaset[i][0],
                        "Lemmatized Word": lemmaset[i][1],
                        "POS Tag": lemmaset[i][2]
                        })
                    json.dump(data, f)
        
        string_found_terms = ""  
    
        for lemmaset in lemma_pos_token:
            for i in range(len(lemmaset)):
                found_terms.append(lemmaset[i][1])
                
            string_found_terms = ' '.join(found_terms)
            return string_found_terms



    def parse(self,response):

        
        hyperlink1, anchortext = self.parse_recursive(response)
        extensionsToCheck=['mailto','ECS+AE+resources','.bat','.rpm','.pdf','.PDF','.docx','.DOCX','.doc','.DOC','.efi','.elf','.pyz','.png','.PNG','.jpg','.JPG','.bmp','.BMP','.jar','.jpeg','.JPEG','.msg','.msi','.pptx','.PPTX','.ppt','.PPT','.pkg','.pcap','.bin','.BIN','.xml','.mp4','.gz','.tst','.ostm','.odp','.tar','.tgz','.7z','.wmv','.MOV','.mov','.vsd','.xls','.xlsx','.xos','.kpxe','download/attachments','.zip','.zip?','.exe','.ZIP','.IMA']
        print("Crawling")
        link = str(response.url)
        head = response.xpath("//head/title")
        str1=str(head.xpath("text()").extract())
        str1 = str1.replace("[","")
        str1 = str1.replace("'","")
        str1 = str1.replace("]","")
        """str1 = self.lemmatization_input(str1)"""
        title = str1
        indexname1 = 'wikifinal'
        for head in response.xpath("//h1[@id='title-text']/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h1"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)


        for head in response.xpath("//div[@class='wiki-content']/h1/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h1/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h2"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub,suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h2/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h2/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h3"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h3/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h3/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h4"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h4/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h4/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h5"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h5/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h5/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)
        for head in response.xpath("//div[@class='wiki-content']/h6"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h6/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h6/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h7"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h7/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/h7/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/ul"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/ul/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/ul/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/ol"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/ol/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/ol/a"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for head in response.xpath("//div[@class='wiki-content']/p/strong"):
            sub=str(head.xpath("text()").extract())
            sub = sub.replace("[","")
            sub = sub.replace("'","")
            sub = sub.replace("]","")
            suborig = sub
            sub = self.lemmatization_input(sub)
            if sub:
                result = add_doc(self.es, indexname1, title, link, sub, suborig)
                print(result)

        for count,link in enumerate(hyperlink1):
            link=self.url_correcter(link)
            if any(ext in link for ext in extensionsToCheck):
                continue
            curl_string3 = 'curl -H "Authorization: Basic a3VuZGFuc2E6QW5pS3VuQDk5MDM="  -X GET -H "Content-Type: application/json" '+link
            request = Request.from_curl(curl_string3, self.parse)
            yield request
        


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(EcsWiki)
d.addBoth(lambda _: reactor.stop())
reactor.run()

"""process = CrawlerProcess()
process.crawl(EcsWiki)
process.start()"""
