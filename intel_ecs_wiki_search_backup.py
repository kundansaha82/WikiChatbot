# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:25:29 2021

@author: kundankantisaha
"""

from elasticsearch import Elasticsearch
from os import popen
"""import logging"""
import subprocess
from lemma_tokenizer import Splitter as Splitter
from lemma_tokenizer import LemmatizationWithPOSTagger as LemmatizationWithPOSTagger
import json
import lemma_tokenizer
import scrapy
from scrapy import Request

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
source_link = ""
keywordoriginal = ""
def print_content(response):
        print("Printing content")
         
        with open("C:\\Users\\kundansa\\ecswikifin\\ecswikifin\\spiders\\data_file7.json", "a") as filee:
            filee.write('[')
            sub=""
            sub_next=""
            h2 = response.xpath("//div[@class='wiki-content']")
            lines = ""
            title=response.xpath("//head/title/text()").extract()
            heading=response.xpath("//div[@class='wiki-content']/h2")
            print(title)
            for head in response.xpath("//div[@class='wiki-content']/h1"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h1[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h1[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h1/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h1[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h1[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in heading:
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h2[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h2[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break
                        
            for head in response.xpath("//div[@class='wiki-content']/h2/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h2[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h2[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            
            for head in response.xpath("//div[@class='wiki-content']/h3"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h3[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h3[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h3/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h3[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h3[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h4"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h4[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h4[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h4/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h4[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h4[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h5"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h5[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h5[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h5/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h5[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h5[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            
            for head in response.xpath("//div[@class='wiki-content']/h6"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h6[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h6[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h6/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h6[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h6[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h7"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h7[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h7[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h7/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h7[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h7[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/ul"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ul[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ul[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/ul/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ul[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ul[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/ol"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ol[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ol[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/ol/strong"):
                sub=str(head.xpath("text()").extract())
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ol[1]//text()").extract())
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ol[1])]//text()").extract()
                        json.dump({
                            'line':(str(line))
                            }, filee
                            )
                        filee.write(']')
                        print(str(line))
                        break
                    else:
                        for i in range(1, 6):
                            i_char = str(i)
                            str_xpath = ".//following::text()[" + i_char + "]"
                            lines = lines + str(head.xpath(str_xpath).extract())
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break
        yield response
                    

"""if __name__ == '__main__':
  logging.basicConfig(level=logging.ERROR)"""
  
start_cluster()
es = connect_elasticsearch()

looping_condition = True

"""key_terms = ['backup', 'Security', 'DPDK', 'Driver', 'OVS', 'ADQ','Containers','NVMe over TCP','Memcached','Netperf','Redis','Aerospike'
             'RDMA','DDP','DPR','AF_XDP','ECS','Columbiaville','OEM','ETA','Ethernet','Pre-Boot']"""

while looping_condition:
    found_terms = list()

    input_string = input("Enter your query/ enter '-1' to exit :")
    if ("-1" == input_string):
        looping_condition = False
        continue
    
    
    lemma_tokenizer.input_string = input_string
 
    
    splitter = Splitter()
    lemmatization_using_pos_tagger = LemmatizationWithPOSTagger()

    #step 1 split document into sentence followed by tokenization
    tokens = splitter.split(input_string)

    #step 2 lemmatization using pos tagger 
    lemma_pos_token = lemmatization_using_pos_tagger.pos_tag(tokens)
    with open('input_tokens.json', 'w') as f:
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
    
    allowed_pos_tags = [["NNP"],["NNS"],["NN"],["VB"],["NNPS"],["CD"]]
    for lemmaset in lemma_pos_token:
        for i in range(len(lemmaset)):
            if lemmaset[i][2] in allowed_pos_tags:
                found_terms.append(lemmaset[i][1])
                
                
    string_found_terms = ' '.join(found_terms)

    search_param = {

        "query": {
            "simple_query_string" : {
                "query": string_found_terms,
                "fields": ["title", "keyword"],
                "default_operator": "and"
                }
            }
        } 
    res = es.search(index="wikifin", body=search_param)
    """print("%d documents found" % res['hits']['total'])"""
    data = [doc for doc in res['hits']['hits']]
    resulting_search = ""
    for doc in data:
        resulting_search = doc['_source']['keyword']
        original_search_phrase = doc['_source']['keywordoriginal']
        print("")
        print("%s" % original_search_phrase)
        keywordoriginal = original_search_phrase
        
        lemma_tokenizer.input_string = resulting_search
        splitter = Splitter()
        lemmatization_using_pos_tagger = LemmatizationWithPOSTagger()

        tokens_out = splitter.split(resulting_search)
        lemma_pos_token_out = lemmatization_using_pos_tagger.pos_tag(tokens_out)
        with open('output_tokens.json', 'w') as f:
            for lemmaset_out in lemma_pos_token_out:
                for i in range(len(lemmaset_out)):
                    data = {}
                    data["words"] = []
                    data["words"].append({
                        "Original Word": lemmaset_out[i][0],
                        "Lemmatized Word": lemmaset_out[i][1],
                        "POS Tag": lemmaset_out[i][2]
                        })
                    json.dump(data, f)
        source_link = (doc['_source']['link'])
        
        curl_string1 = 'curl -H "Authorization: Basic S1VOREFOU0E6QW5pS3VuQDk5MDM="  -X GET -H "Content-Type: application/json" '+source_link        
        response = Request.from_curl(curl_string1, callback = print_content)
        print("%s" % source_link)
        

