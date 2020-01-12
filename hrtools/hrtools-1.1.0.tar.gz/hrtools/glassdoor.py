#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from .utils import utils


# In[1]:


class glassdoor:

    def getCompanies(maxpag = 0):
        
     

        url = "https://www.glassdoor.com.br/Avaliações/brasil-avaliações-SRCH_IL.0,6_IN36_IP1.htm"

        headers = {	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, sdch, br',
                'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
                'referer': 'https://www.glassdoor.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive'
            }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text,'html.parser')
        
        pgFinal = str(soup.find("div",{"class":"count margBot floatLt tightBot"}).text).replace(" empresas","").replace(".","").split()[-1]
        pgFinal = int(round(int(pgFinal)/10,0))        

        if (maxpag > 0) and (maxpag < pgFinal):
            pgFinal = maxpag
            
        

        output = pd.DataFrame(columns=["Empresa", "Link","Nota","Avaliacoes","Recomenda"])

        for pg in range(1, pgFinal+1, 1):
        


            url = "https://www.glassdoor.com.br/Avaliações/brasil-avaliações-SRCH_IL.0,6_IN36_IP" + str(pg) + ".htm"

            headers = {	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, sdch, br',
                'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
                'referer': 'https://www.glassdoor.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive'
            }


            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text,'html.parser')
            
            #if response.status_code == 200:
                #print('Requisição bem sucedida!')
                #content = response.content



            for revisoes in soup.findAll("div",{"class":"eiHdrModule"}):
                
                
                
                
                
                try:
                    Empresa = revisoes.find("a",{"class":"tightAll"}).text
                except:
                    Empresa = None
                try:
                    Link = revisoes.find("a",{"class":"eiCell cell reviews"})["href"]
                except:
                    Link = None
                try:
                    Nota = revisoes.find("span",{"class":"bigRating"}).text
                except:
                    Nota = None
                try:
                    Avaliacoes = revisoes.find("span",{"class":"num h2"}).text
                except:
                    Avaliacoes = None
                try:
                    Recomenda = revisoes.find("span",{"class":"minor hideHH margRtLg block margTopXs"}).text
                except:
                    Recomenda = None
                
                
                
                
                

                lista = [Empresa, Link, Nota, Avaliacoes, Recomenda]

                output.loc[len(output)] = lista
                
            
            utils.printProgressBar(pg, pgFinal, prefix = 'Progress:', suffix = 'Complete', length = 50)
         
        return(output)




    def getCompanyReview(links = None):
        global Geral
        global Summary
        global Data
        global Vantagens
        global Job
        global Location
        global Desvantagens
        global Conselho
        global Qualidade
        global Cultural
        global Oportunidades
        global Remuneracao
        global Lideranca
        global Recomenda
                
                
        if links == None:
            
            print("Necessário parâmetro: link da empresa")
            
        elif isinstance(links,str):
        
            print("Passe o parâmetro como lista")
            
        else:
            
            i = 0
            outputAvaliacoes = pd.DataFrame(columns=["Link","Data","Cargo","Location","Summary","Recomenda", "Geral","Qualidade","Cultural","Oportunidades",
                                            "Remuneracao","Lideranca","Vantagens","Desvantagens","Conselho"])
            
            for link in links:
                
                
                printProgressBar(i, len(links), prefix = ' Links Progress:', suffix = 'Complete', length = 50)
                
                i=i+1
                url = "https://www.glassdoor.com.br" + link
              
                headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'accept-encoding': 'gzip, deflate, sdch, br',
                            'accept-language': 'pt-BR;q=0.8,en;q=0.6',
                            'referer': 'https://www.glassdoor.com.br/',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                            'Cache-Control': 'no-cache',
                            'Connection': 'close'
                            }
                
                
                try:
                    numTry = 0
                    
                    response = requests.get(url, headers=headers);
                
                    
                    soup = BeautifulSoup(response.text,'html.parser')
                    
                    try:
                        pgFinal = math.ceil(int(soup.find("h2",{"class":"col-6 my-0"}).text.split()[0])/10)
                    except:
                        pgFinal = 1


                    
                    #for pg in range(1, pgFinal+1, 1):
                    for pg in range(1, pgFinal+1, 1):
                        
                        if numTry > 3:
                            break

                        printProgressBar(pg, pgFinal+1, prefix = ' Person Progress:', suffix = 'Complete', length = 50)

                        url = "https://www.glassdoor.com.br" + link.replace(".htm","_P" + str(pg) + ".htm")
                        #print(url)
                        try:
                            response = requests.get(url, headers=headers);
                            soup = BeautifulSoup(response.text,'html.parser')
                            #print(url)
                            for revisoes in soup.find_all('div','hreview'):
                                Geral = ''
                                Summary = ''
                                Data = ''
                                Vantagens = ''
                                Job = ''
                                Location = ''
                                Desvantagens = ''
                                Conselho = ''
                                Qualidade = ''
                                Cultura = ''
                                Oportunidades = ''
                                Remuneracao = ''
                                Lideranca = ''
                                Recomenda = ''

                                Geral = revisoes.find("span","value-title")['title']
                                try:
                                    Data = revisoes.find("time")['datetime']
                                except:
                                    Data = ''

                                try:
                                    Job = revisoes.find("span","authorJobTitle").text
                                except:
                                    Job = ''

                                try:
                                    Location = revisoes.find("span","authorLocation").text
                                except:
                                    Location = ''
                                    
                                    
                                try:
                                    Summary = revisoes.find("span",{"class":"summary"}).text
                                except:
                                    Summary = ''
                                    

                                try:
                                    Recomenda = revisoes.find("div",{"class":"recommends"}).find("span").text
                                except:
                                    Recomenda = ''

                                for textos in revisoes.findAll("div",{"class":"mt-md"}):

                                    if textos.find("p",{"class":"strong"}).text == "Vantagens":
                                        Vantagens = textos.find("p",{"class":None}).text

                                    elif textos.find("p",{"class":"strong"}).text == "Desvantagens":
                                        Desvantagens = textos.find("p",{"class":None}).text

                                    elif textos.find("p",{"class":"strong"}).text == "Conselho à presidência":
                                        Conselho = textos.find("p",{"class":None}).text



                                for A in revisoes.find_all("ul",'undecorated','minor'):




                                    for B in A.findAll("li"):

                                        
                    
                                        if B.find("div").text == "Qualidade de vida":
                                            Qualidade = B.find("span")['title']

                                        elif B.find("div").text == "Cultura e valores":
                                            Cultura = B.find("span")['title']

                                        elif B.find("div").text == "Oportunidades de carreira":
                                            Oportunidades = B.find("span")['title']

                                        elif B.find("div").text == "Remuneração e benefícios":
                                            Remuneracao = B.find("span")['title']

                                        elif B.find("div").text == "Alta liderança":
                                            Lideranca = B.find("span")['title']

                              
                                lista = [link,Data,Job,Location,Summary,Recomenda, Geral,Qualidade,Cultura,Oportunidades,Remuneracao,Lideranca, Vantagens, Desvantagens, Conselho] 
                                
                                lista = [w.replace("\x00"," ") for w in lista]
                                lista = [w.replace("\r\n"," ") for w in lista]
                                lista = [w.replace('\n', '') for w in lista]
                                lista = [w.replace(',', ' ') for w in lista]
                                lista = [w.replace('\"', '') for w in lista]
                                lista = [w.replace('\'', '') for w in lista]
                                lista = [w.replace('  ', ' ') for w in lista]
                                outputAvaliacoes.loc[len(outputAvaliacoes)] = lista
                                sleep(0.005)
                                
                                
                        except requests.exceptions.ConnectionError as f:
                            numTry = numTry + 1
                            
                            
                except requests.exceptions.ConnectionError as e:
                    print("erro em link")
                    print(link)
        
        return(outputAvaliacoes)
           


 

