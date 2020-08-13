import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('700x150')
# 设置下载进度条
tk.Label(window, text='下载进度:').place(x=40, y=80)
canvas = tk.Canvas(window, width=600, height=16, bg="white")
canvas.place(x=40, y=100)
# 下载按钮函数
def usr_download():
    pass
    # response = session.get(url_str, headers=headers2, cookies=cookies_xxx, verify=False, stream=True)  # stream=True表示请求成功后并不会立即开始下载，而是在调用iter_content方法之后才会开始下载
    # chunk_size = 40960  # 设置每次下载的块大小
    # content_size = int(m4a.headers['content-length'])  # 从返回的response的headers中获取文件大小
    # # 填充进度条
    # fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
    # raise_data = 600 / (content_size/chunk_size)    # 增量大小，600为进度条的长度
 
    # # 将下载的数据写入文件
    # with open(title + '.m4a', 'wb') as f:
    #       n = 0
    #       for data in response.iter_content(chunk_size=chunk_size):  # 在循环读取文件时，刷新进度条  
    #           f.write(data)
    #           n = n + raise_data    
    #           canvas.coords(fill_line, (0, 0, n, 60))
    #           window.update()
 
# 清空进度条
def clean_progressbar():
    # 清空进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
    x = 500  # 未知变量，可更改
    n = 600 / x  # 465是矩形填充满的次数
 
    for t in range(x):
        n = n + 600 / x
        # 以矩形的长度作为变量值更新
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
 
# 下载按钮
url_text= tk.Text(window,width = 80, height = 1)
url_text.place(x=30,y=40)
# url_text.pack()

btn_download = tk.Button(window, text='开始下载', command=usr_download)
btn_download.place(x=620, y=28)

tip_label = tk.Label(window,text="下载地址" )
tip_label.place(x=45,y=15)

window.mainloop()