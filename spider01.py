# -*- coding:UTF-8 -*-
from selenium.webdriver.firefox.options import Options
from urllib.parse import urlparse
from selenium import webdriver
import requests
import time
import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.title('My Window')
    window.geometry('800x200')

    O_url = tk.Text(window,width = 100, height = 1.5) 
    O_url.pack()

    def click_to_run():
        url = O_url.get("1.0","end")
    # t.insert('end', var)

    b2 = tk.Button(window, text = 'click to run', width = 20, height = 1,command = click_to_run)
    b2.pack()

    t = tk.Text(window,width = 100, height = 15) # height定义文本框有多少行
    t.pack()




    print('正在运行。。。。。。。。。。。。')
    # url = 'https://www.archdaily.com/941837/the-tennessee-state-museum-eoa-architects-plus-hga/5ee96636b3576575aa000044-the-tennessee-state-museum-eoa-architects-plus-hga-section-perspective?next_project=no'
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)
    browser.get(url)

    ori_pic_list = []
    index = 1
    while 1:
        elem_ori_pic = browser.find_element_by_id('original-size-image')
        ori_pic_list.append(elem_ori_pic.get_attribute('href'))
        print(f'正在获取第{index}张........')
        elem_next_pic=browser.find_element_by_id('next-image')
        if elem_next_pic.is_displayed():
            elem_next_pic.click()
            time.sleep(2)
        else:
            break
        index = index + 1
    browser.close()
    # with open('original_pic_src.txt','w') as f:
    #         for line_item in ori_pic_list:
    #             f.write(line_item+'\n')

    print('即将完成........')
    for item in ori_pic_list:
        res = requests.get(item)
        parsed_url = urlparse(item)
        ori_pic_name = parsed_url.path.split('/').pop()
        with open(ori_pic_name,'wb') as f:
            f.write(res.content)
            f.close()
        
    print('saved')
