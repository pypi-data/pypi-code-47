import requests
import re
import time
import pandas as pd
from bs4 import BeautifulSoup
import os
import random

def get_one_page(url):
    response = requests.get(url)
    print(response.status_code)
    while response.status_code == 403:
        time.sleep(500 + random.uniform(0, 500))
        response = requests.get(url)
        print(response.status_code)
    if response.status_code == 200:
        return response

    return None

def download_papers(save_path,paper,key_words='',time_delay=5):

    paper_struct = paper[paper['title'].str.contains(key_words, case=False)]

    print(len(paper_struct))

    current_time = time.strftime("%Y-%m-%d")
    if not os.path.exists(os.path.join(save_path,current_time)):
        os.makedirs(os.path.join(save_path,current_time))

    for selected_paper_id, selected_paper_title in zip(paper_struct['id'], paper_struct['title']):
        selected_paper_id = selected_paper_id.split(':', maxsplit=1)[1] # arXiv:2001.05982 ==> 2001.05982
        selected_paper_title = selected_paper_title.split(':', maxsplit=1)[1]

        request_url = 'https://arxiv.org/pdf/' + selected_paper_id
        print(request_url)
        r = requests.get(request_url)

        while r.status_code == 403:
            time.sleep(500 + random.uniform(0, 500))
            r = requests.get('https://arxiv.org/pdf/' + selected_paper_id)

        selected_paper_id = selected_paper_id.replace(".", "_")
        pdfname = selected_paper_title.replace("/", "_")
        pdfname = pdfname.replace("?", "_")
        pdfname = pdfname.replace("\"", "_")
        pdfname = pdfname.replace("*","_")
        pdfname = pdfname.replace(":","_")
        pdfname = pdfname.replace("\n","")
        pdfname = pdfname.replace("\r","")
        print(os.path.join(save_path,current_time)+'[/%s]%s.pdf'%(selected_paper_id, pdfname))
        with open(os.path.join(save_path,current_time)+'[/%s]%s.pdf'%(selected_paper_id,pdfname), "wb") as code:
           code.write(r.content)

        time.sleep(time_delay)

def download(save_path,time_sleep=5):
    url = 'https://arxiv.org/list/cs.CV/pastweek?show=1000'
    html = get_one_page(url)
    content = html.text
    # with open("test.html", "w") as fp:
    #     fp.write(content)
    # with open("test.html", "r") as fp:
    #     content = fp.read()
    # print(content)
    soup = BeautifulSoup(content, features='html.parser')

    content = soup.dl
    list_ids = content.find_all('a', title='Abstract')
    list_title = content.find_all('div', class_='list-title mathjax')

    items = []
    for i, paper in enumerate(zip(list_ids, list_title)):
        items.append([paper[0].text, paper[1].text])
    name = ['id', 'title']
    paper = pd.DataFrame(columns=name,data=items)

    download_papers(save_path,paper,time_delay=time_sleep)

if __name__ == '__main__':
    download('./test_nn')
