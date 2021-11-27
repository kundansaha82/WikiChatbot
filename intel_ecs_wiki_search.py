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
from wiki_reader import *

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
        
  
start_cluster()
es = connect_elasticsearch()

looping_condition = True


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
    
    allowed_pos_tags = [["NNP"],["NNS"],["NN"],["VB"],["NNPS"],["CD"],["VBD"],["VBN"]]
    for lemmaset in lemma_pos_token:
        for i in range(len(lemmaset)):
            if lemmaset[i][2] in allowed_pos_tags:
                found_terms.append(lemmaset[i][1])
                
                
    string_found_terms = ' '.join(found_terms)
    
       
    search_param = {

        "query": {
            "simple_query_string" : {
                "query": string_found_terms,
                "fields": ["title", "heading"],
                "default_operator": "and"
                }
            }
        } 
    res = es.search(index="wikifinal", body=search_param)
    """print("%d documents found" % res['hits']['total'])"""
    data = [doc for doc in res['hits']['hits']]
    resulting_search = ""
    for doc in data:
        resulting_search = doc['_source']['heading']
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

        print_con(source_link,keywordoriginal,string_found_terms)

        print("%s" % source_link)    
        

