import tkinter as tk
url = ''
window = tk.Tk()
window.title('My Window')
window.geometry('800x200')

O_url = tk.Text(window,width = 100, height = 1.5) 
O_url.pack()


# 在文本末尾插入entry输入框的数据
def click_to_run():
    global url
    url = O_url.get("1.0","end")
    t.insert('end', )

b2 = tk.Button(window, text = 'click to run', width = 20, height = 1,command = click_to_run)
b2.pack()

t = tk.Text(window,width = 100, height = 15) # height定义文本框有多少行
t.pack()


window.mainloop()

