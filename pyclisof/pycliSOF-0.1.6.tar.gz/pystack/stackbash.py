import numpy as np
import urllib3
from bs4 import BeautifulSoup
import json
import zlib
import requests
from colorama import Fore, Back, Style 
from texttable import Texttable
import re

class stackbash:
    
    

    def url_builder(self,base_url,title):
        
        for i in  title:
            if i>='a' and i<='z' :
                base_url+=i
            elif i>='A' and i<='Z' :
                base_url+=i
            else:
                base_url+='%'+format(ord(i), "X")
        return base_url

    def get_request(self,url,title):
        http = urllib3.PoolManager()
        req=requests.get(self.url_builder(url,title),verify=False)
    #     print(req.data)
        return req.json()

    def similar_questions_search(self,question):
    #     print decompressed_data
        t = Texttable()
        urltemplate="https://api.stackexchange.com/2.2{link}?order=desc&sort=votes&site=stackoverflow&filter=!-*jbN-FjhDuu&key=1F82Z6X9SjP7GrnuzUqjVg((&title="
        json_data = self.get_request(urltemplate.replace("{link}","/similar"),question)
        s=""
        index=0
        for i in range(min(len(json_data["items"]),10)):
            if json_data["items"][i].get("title")!=None :
                s=""
                index=index+1
                s+="ques"+str(index)+" : "+BeautifulSoup(json_data["items"][i]["title"]).text+"\n"
                t.add_row([s])
                
                
        if index==0 :
            return "Sorry! We couldn't Find any Result"
        else:
            return t.draw()

    def get_answers(self,ques):
        t=Texttable()
        urltemplate="https://api.stackexchange.com/2.2{link}?order=desc&sort=votes&site=stackoverflow&filter=!-*jbN-FjhDuu&key=1F82Z6X9SjP7GrnuzUqjVg((&title="
        
        json_data = self.get_request(urltemplate.replace("{link}","/search/excerpts"),ques)
        index=0
        
        s=""
        for i in range(min(len(json_data["items"]),4)):
            if json_data["items"][i].get("answer_id")!=None :
                s=""
                index=index+1
                req1=requests.get("https://api.stackexchange.com/2.2/posts/"+str(json_data["items"][i].get("answer_id"))+"?order=desc&sort=votes&site=stackoverflow&filter=!9Z(-wu0BT&key=8v6rHdiTEj8xgsiVDC9ibA((",verify=False)

                json_data1 = req1.json()
                s+="ans"+str(index)+" : "+BeautifulSoup(json_data1["items"][0]["body"]).text+"\n"
                t.add_row([s])
        
        if index==0 :
            return "Sorry! We couldn't Find any Result"
        else:
            return t.draw()
    
 
    def stack_bash(self):
        # print "success"
        t=Texttable()
        t.add_row(["Menu"])
        t.add_row(["1: Search For Answer for a Question"])
        t.add_row(["2: Search For Questions Similar to the Question"])
        t.add_row(["3: Exit"])
        print(t.draw())
        while True:
            g = input("Enter your Choice : ")    
            if re.search('[^0-9]',str(g))!=None or not g:
                print("Enter Valid Option")
                continue
           
            # print type(g)
            g=int(str(g),10)    
            if g==3 :
                break
            else:
                if g==1:
                    ques = raw_input("Enter The Question that you want to Search : ")
                    print(self.get_answers(str(ques))+"\n")
        #             print ques
                elif g==2:
                    ques = raw_input("Enter The Question that you want to Search : ")
        #             print ques
                    print(self.similar_questions_search(str(ques))+"\n")
                else:
                    print("Enter Valid Option")

    #stack_bash()

