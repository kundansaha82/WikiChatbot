# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:06:58 2021

@author: kundankantisaha
"""

import pycurl
from lxml import etree
from lxml.etree import tostring 
import base64
from io import BytesIO
import json
from itertools import chain

def print_con(source_link,keywordoriginal,string_found_terms):
    access_details = 'kundansa:AniKun@9903'
    cred1 = base64.b64encode(bytes(access_details, 'ascii'))
    cred = cred1.decode('ascii')


    headers = { 'Authorization' : 'Basic %s' % cred }


    response = BytesIO()
    conn = pycurl.Curl()


    """conn.setopt(pycurl.VERBOSE, 1)"""
    conn.setopt(pycurl.HTTPHEADER, ["%s: %s" % t for t in headers.items()])
    conn.setopt(pycurl.URL, source_link)


    conn.setopt(conn.WRITEDATA, response)

    conn.perform() 
    conn.close()

    get_body = response.getvalue()
    page_content = get_body.decode('utf8')
    """print('Output of GET request:\n%s' % page_content) """

    dom = etree.HTML(page_content)
    print_content(dom,keywordoriginal,string_found_terms)

def stringify_children(node):
    parts = ([node.text] + list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) + [node.tail]) 
    return ''.join(filter(None, parts))



def print_content(response,keywordoriginal,string_found_terms):
        lines = "" 
        with open("C:\\Users\\kundansa\\ecswikifin\\ecswikifin\\spiders\\data_file7.json", "a") as filee:
            filee.write('[')
            sub=""
            sub_next=""
            lines = ""
            head1 = response.xpath("//div[@class='wiki-content']")
            title=response.xpath("//head/title/text()")
            heading=response.xpath("//div[@class='wiki-content']/h2")
            metadata=response.xpath("//div[@class='page-metadata']")
            print(title)
            """
            for head in response.xpath("//h1[@id='title-text']/a"):    
            
                sub = str(head.xpath("text()"))
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                
                if re.search( string_found_terms, sub ):
                    for head1 in response.xpath("//div[@class='wiki-content']"):
                        sub=str(head1.xpath("text()") )
                        sub = sub.replace("[","")
                        sub = sub.replace("'","")
                        sub = sub.replace("]","")
                        lines = lines.join(sub)
                    print(lines[0:30])
                break
            """
            for head in response.xpath("//div[@class='wiki-content']/h1"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h1[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h1[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h1/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h1[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h1[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']//h1//a"):
                sub=str(head.xpath("../text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h1[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h1[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in heading:
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h2[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h2[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break
                        
            for head in response.xpath("//div[@class='wiki-content']/h2/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h2[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h2[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            
            for head in response.xpath("//div[@class='wiki-content']/h3"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h3[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h3[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h3/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h3[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h3[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h4"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h4[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h4[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h4/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h4[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h4[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h5"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h5[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h5[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h5/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h5[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h5[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            
            for head in response.xpath("//div[@class='wiki-content']/h6"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h6[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h6[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h6/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h6[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h6[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/h7"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h7[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h7[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/h7/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::h7[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::h7[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/ul"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ul[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ul[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/ul/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ul[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ul[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break


            for head in response.xpath("//div[@class='wiki-content']/ol"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ol[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ol[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break

            for head in response.xpath("//div[@class='wiki-content']/ol/strong"):
                sub=str(head.xpath("text()") )
                sub = sub.replace("[","")
                sub = sub.replace("'","")
                sub = sub.replace("]","")
                if sub == keywordoriginal:
                    sub_next=str(head.xpath("following-sibling::ol[1]//text()") )
                    sub_next = sub_next.replace("[","")
                    sub_next = sub_next.replace("'","")
                    sub_next = sub_next.replace("]","")
                    if sub_next != "":
                        line = head.xpath(".//following-sibling::*[count(following-sibling::ol[1])]//text()") 
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
                            lines = lines + str(head.xpath(str_xpath) )
                        json.dump({
                            'line':(lines)
                            }, filee
                            )
                        filee.write('...]')
                        print(str(lines))
                        break
        
        
        author=response.xpath("//div[@class='page-metadata']/ul/li/span[@class='author']/a/text()")
        editor=response.xpath("//div[@class='page-metadata']/ul/li/span[@class='editor']/a[@class='url fn confluence-userlink']/text()")
        date_edited=response.xpath("//div[@class='page-metadata']/ul/li/a[@class='last-modified']/text()")
        print("author : "+str(author))
        print("edited by : "+str(editor))
        print("Last modified : "+str(date_edited))
        