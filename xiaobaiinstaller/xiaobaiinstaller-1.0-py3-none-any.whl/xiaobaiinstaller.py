#! /usr/bin/env python
"""
__author__ = Tser
__time__ = 2019/12/26 17:23
__file__ = xiaobaiinstaller.py
"""
from requests_html import HTMLSession
from tkinter import Tk, ttk, messagebox
import tkinter
from threading import Thread
from urllib.request import urlretrieve
from re import findall
from zipfile import ZipFile
from os import system, path

root = Tk()
# 界面内容
root.geometry("330x200")
root.title("小白测试工具安装器 V0.1")
# 获取当前目录 #
cur_path = path.dirname(__file__)
root.iconbitmap(cur_path + '/' + "logo.ico")
button_name = tkinter.StringVar()
button_name.set('点击搜索')
data = tkinter.StringVar()
data.set('点击搜索')
checkV = tkinter.IntVar()
checkV.set(0)
alert_data = tkinter.StringVar()
alert_data.set('初始化成功！')

#支持的软件名
versions = {
        'jmeter': 'http://archive.apache.org/dist/jmeter/binaries/',
        'jdk': 'https://cdn.azul.com/zulu/bin/'
        # 'fiddler': '',
        # 'postman': '',
        # 'charles': '',
        # 'python': ''
}

curr_soft_url = []

# 添加搜索框
search_insert = ttk.Combobox(master=root)
search_insert['value'] = tuple(versions.keys())
search_insert.current(0)
search_insert.pack()

result_box = ttk.Combobox(master=root)
alert = tkinter.Label(master=root, textvariable=alert_data)
alert.configure(bg='#008000')
# 请求方法
asession = HTMLSession()
headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

def check():
    global curr_soft_url
    # 清空版本下拉列表内容
    result_box['value'] = ()
    # 搜索软件所有版本信息并写入到下拉列表中
    cur_soft_name = search_insert['value'][search_insert.current()]
    alert_data.set(f'正在检查{cur_soft_name}版本信息，请稍等...')
    r = asession.get(versions[cur_soft_name], headers=headers)
    version_list = []
    if cur_soft_name == 'jmeter':
        curr_soft_url = r.html.absolute_links
        curr_soft_url = list(filter(lambda x: 'apache-jmeter-' in x and '.zip' in x, curr_soft_url))
        for link in curr_soft_url:
            version_list.append(findall('apache-jmeter-(.+?).zip', link)[0])
    elif cur_soft_name == 'jdk':
        curr_soft_url = findall('href="(.+)-win_x64.zip">', r.text)
        for index, link in enumerate(curr_soft_url):
            curr_soft_url[index] = versions[cur_soft_name] + link + '-win_x64.zip'
        for link in curr_soft_url:
            try:
                version_list.append(findall('-jdk(.+?)-win_x64.zip', link)[0])
            except:
                pass
    version_list = list(set(version_list))
    result_box['value'] = tuple(version_list)
    result_box.current(0)
    alert_data.set(f'检查{cur_soft_name}版本信息，已完毕！')

# 按钮事件
def change_button():
    t = Thread(target=check)
    t.start()

# 添加按钮
search_button = tkinter.Button(master=root, textvariable=button_name, command=change_button)
search_button.pack()

result_box.pack()

def Schedule(a,b,c):
     '''''
     a:已经下载的数据块
     b:数据块的大小
     c:远程文件的大小
    '''
     per = 100.0 * a * b / c
     if per > 100 :
         per = 100
     alert_data.set("下载进度：%.2f%%" % per)

def download():
    # 获取当前下载的软件名称
    cur_soft_name = search_insert['value'][search_insert.current()]
    # 获取当前的版本
    cur_soft_version = result_box['value'][result_box.current()]
    # 获取对应的url
    download_url = ''
    for url in curr_soft_url:
        if cur_soft_name in url and cur_soft_version in url:
            download_url = url
            break
    # 下载
    download_file_name = cur_soft_name + cur_soft_version + '.zip'
    if download_url == '':
        messagebox.showwarning(title='警告：', message='下载地址获取失败！')
    try:
        alert_data.set(f'正在下载{download_file_name}文件在当前目录下，请稍等...')
        urlretrieve(download_url, download_file_name, Schedule)
        alert_data.set(f'{download_file_name}文件已经下载成功！')
    except:
        alert_data.set(f'下载{download_file_name}文件失败')
        alert.configure(bg='#8B0000')
    # 解压缩
    alert_data.set(f'正在解下缩{download_file_name}文件，请稍等...')
    ZipFile(download_file_name).extractall('D:\\demo')
    # 安装（加环境变量）
    alert_data.set(f'正在配置{cur_soft_name}环境信息，请稍等...')
    if 'jmeter' in download_file_name:
        system(f'setx PATH "%PATH%;D:\\demo\\{download_file_name[:-4]}\\bin"')
    elif 'jdk' in download_file_name:
        system(f'setx JAVA_HOME000 D:\\demo\\{download_file_name[:-4]}\\bin"')
        system(f'setx PATH "%PATH%;%JAVA_HOME000%D:\\demo\\{download_file_name[:-4]}\\bin;D:\\demo\\{download_file_name[:-4]}\\jre\\bin"')
    system(f'rmdir /Q/S {download_file_name}')
    alert_data.set('环境配置已完成！')

def install():
    t = Thread(target=download)
    t.start()

install_button = tkinter.Button(master=root, text='下载&安装', command=install)
install_button.pack()
tkinter.Label(master=root).pack()
alert.pack()

def main():
    root.mainloop()

if __name__ == '__main__':
    main()