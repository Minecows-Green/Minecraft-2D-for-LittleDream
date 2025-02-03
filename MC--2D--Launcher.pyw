#!/usr/bin/env python
#-*- coding:utf-8 -*-
# name: Minecraft--2D--Launcher
# time: 2024-8.15    19:48

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

import tkinter as tk
from PIL import Image, ImageTk

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('MC--2D--启动器')
        self.master.geometry('486x294')
        self.master.iconbitmap('MC_launcher_ico.ico')
        self.master.resizable(False, False)
        self.master = master
        self.pack()
        self.create_widgets()
        self.cfg = None
        # 读取cfg文件数据
        with open('set.cfg', 'r') as cfg:
            str_cfg = cfg.read()
            if str_cfg != '':
                list_cfg = ast.literal_eval(str_cfg)
                self.cfg = list_cfg
                self.wx, self.wy = list_cfg[0]
                self.tick = list_cfg[4]
        self.createWidgets()

    def create_widgets(self):
        # 创建一个标签用于展示图片
        self.image_label = tk.Label(self)
        self.image_label.pack()

        # 读取并转换图片
        image = Image.open('bg_launcher.png')
        image = image.resize((486, 294), Image.LANCZOS)  # 指定图片大小
        self.image = ImageTk.PhotoImage(image)

        # 设置标签的图片内容
        self.image_label.configure(image=self.image)

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Command1.TButton',background='#0078D7', font=('微软雅黑',18))
        self.Command1 = Button(self.top, text='启动游戏', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.362, rely=0.657, relwidth=0.282, relheight=0.167)

        self.Text3Var = StringVar(value=self.wy)
        self.Text3 = Entry(self.top, text=self.wy, textvariable=self.Text3Var, font=('微软雅黑',10))
        self.Text3.place(relx=0.082, rely=0.272, relwidth=0.117, relheight=0.088)

        self.Text2Var = StringVar(value=self.tick)
        self.Text2 = Entry(self.top, text=self.tick, textvariable=self.Text2Var, font=('微软雅黑',10))
        self.Text2.place(relx=0.823, rely=0.19, relwidth=0.084, relheight=0.085)

        self.Text1Var = StringVar(value=self.wx)
        self.Text1 = Entry(self.top, text=self.wx, textvariable=self.Text1Var, font=('微软雅黑',10))
        self.Text1.place(relx=0.082, rely=0.163, relwidth=0.117, relheight=0.085)

        self.style.configure('Label7.TLabel', anchor='w', font=('微软雅黑', 16))
        self.Label7 = Label(self.top, text='启动器', style='Label7.TLabel')
        self.Label7.place(relx=0.428, rely=0.163, relwidth=0.138, relheight=0.112)

        self.style.configure('Label6.TLabel', anchor='w', font=('微软雅黑', 18))
        self.Label6 = Label(self.top, text='Minecraft 2D', style='Label6.TLabel')
        self.Label6.place(relx=0.346, rely=0.054, relwidth=0.315, relheight=0.112)

        self.style.configure('Label5.TLabel', anchor='w', font=('微软雅黑', 9))
        self.Label5 = Label(self.top, text='帧率为0时无限制', style='Label5.TLabel')
        self.Label5.place(relx=0.79, rely=0.299, relwidth=0.216, relheight=0.085)

        self.style.configure('Label4.TLabel', anchor='w', font=('微软雅黑', 9))
        self.Label4 = Label(self.top, text='全屏：x=0,y=0', style='Label4.TLabel')
        self.Label4.place(relx=0.016, rely=0.381, relwidth=0.183, relheight=0.085)

        self.style.configure('Label3.TLabel', anchor='w', font=('微软雅黑', 12))
        self.Label3 = Label(self.top, text='y=', style='Label3.TLabel')
        self.Label3.place(relx=0.033, rely=0.272, relwidth=0.051, relheight=0.085)

        self.style.configure('Label2.TLabel', anchor='w', font=('微软雅黑', 12))
        self.Label2 = Label(self.top, text='x=', style='Label2.TLabel')
        self.Label2.place(relx=0.033, rely=0.163, relwidth=0.051, relheight=0.085)

        self.style.configure('Label1.TLabel',anchor='w', font=('微软雅黑',15))
        self.Label1 = Label(self.top, text='游戏帧率', style='Label1.TLabel')
        self.Label1.place(relx=0.79, rely=0.054, relwidth=0.216, relheight=0.112)

        self.style.configure('Labell.TLabel',anchor='w', font=('微软雅黑',15))
        self.Labell = Label(self.top, text='窗口大小', style='Labell.TLabel')
        self.Labell.place(relx=0.033, rely=0.054, relwidth=0.183, relheight=0.095)

import ast
import subprocess
import sys

from tkinter import messagebox

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def write_cfg(self):
        """ 写入数据到cfg文件"""
        cfg = open('set.cfg', 'w')
        cfg.write('%s' % self.cfg)
        cfg.close()

    def start_exe(self):
        """ 启动Minecraft--2D.exe程序"""
        # 读取Minecraft--2D地址
        with open('mc2d_path.txt', 'r') as path:
            path = path.read()
        try:
            subprocess.run(path + 'Minecraft--2D.exe')
            sys.exit()
        except FileNotFoundError as R:
            messagebox.showerror("游戏启动失败", R)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        try:
            wx, wy = int(self.Text1Var.get()), int(self.Text3Var.get())
            tc = int(self.Text2Var.get())
            self.cfg[0] = (wx, wy)
            self.cfg[4] = tc
            self.write_cfg()
            self.start_exe()
        except ValueError as R:
            messagebox.showerror("游戏启动失败", R)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass

