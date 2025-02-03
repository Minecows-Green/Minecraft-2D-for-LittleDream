"""
Hello Python
项目名：我的世界2D
项目开始时间：2022-02-06 19:02
"""

import ast
import os
import random
import shutil
import time
import sys

import pygame
import pygame.freetype
import win32api
import wx

from role_add import *


class Button_font(object):
    """ 定义一个字体按钮类"""
    def __init__(self):
        """ 定义初始化方法"""
        self.MC_MUSIC = 'music\\clink.mp3'  # 按钮音效路径
        self.instead_0 = None
        self.instead_1 = None
        self.instead_2 = None
        self.instead_3 = None

        self.FONT_SIZE = None       # 字体大小
        self.NMAE_XY = None         # 显示位置
        self.BUTTON_NAME = None     # 按钮名称
        self.BUTTON_COLOR_F = None  # 按钮颜色（当鼠标移到按钮之外时）
        self.BUTTON_COLOR_T = None  # 按钮颜色（当鼠标移到按钮之内时）

    def button(self):
        """ 创建字体按钮"""
        # 获取字体区域
        xw, yw = self.NMAE_XY  # 截取字体显示位置————(xw, yw)
        x0, y0 = self.FONT_SIZE * len(self.BUTTON_NAME)-1 + xw, self.FONT_SIZE-1 + yw
        if xw <= x <= x0 and yw <= y <= y0:
            # 当鼠标移动到字体区域之内时更换字体颜色
            self.instead_0, self.instead_1, self.instead_2, self.instead_3 = \
                self.NMAE_XY, self.BUTTON_NAME, self.BUTTON_COLOR_T, self.FONT_SIZE
        else:
            # 当鼠标移动到字体区域之外时更换字体颜色
            self.instead_0, self.instead_1, self.instead_2, self.instead_3 = \
                self.NMAE_XY, self.BUTTON_NAME, self.BUTTON_COLOR_F, self.FONT_SIZE
        FONT_XY.render_to(
            screen, self.instead_0, self.instead_1, fgcolor=self.instead_2, size=self.instead_3
        )

    def press(self, n=1):
        """ 定义按钮按下"""
        xw, yw = self.NMAE_XY
        x0, y0 = self.FONT_SIZE * len(self.BUTTON_NAME)-1 + xw, self.FONT_SIZE-1 + yw
        if xw <= x <= x0 and yw <= y <= y0:
            """ 点击后的事件"""
            if n:
                self.click_music()
            return True

    def click_music(self):
        """ 定义按钮音效"""
        click = pygame.mixer.Sound(self.MC_MUSIC)
        click.set_volume(MUSIC_BUTTON)
        click.play()

class Button_image(object):
    """ 定义一个图像按钮"""
    def __init__(self):
        """ 定义初始化方法"""
        self.MC_MUSIC = 'music\\clink.mp3'  # 按钮音效路径
        self.instead_0 = None
        self.instead_1 = None
        self.instead_2 = None

        self.IMAGE_OFF = None           # 当鼠标移到按钮之外时的图像
        self.IMAGE_ON = None            # 当鼠标移到按钮之内时的图像
        self.IMAGE_SIZE_OFF = None      # 当鼠标移到按钮之外时的图像大小
        self.IMAGE_SIZE_ON = None       # 当鼠标移到按钮之内时的图像大小
        self.IMAGE_OFF_XY = None        # 图像显示位置（当鼠标移到按钮之外时）
        self.IMAGE_ON_XY = None         # 图像显示位置（当鼠标移到按钮之内时）

    def button(self):
        """ 创建图像按钮"""
        xn, yn = self.IMAGE_SIZE_OFF    # 截取图像大小————(xn, yn)
        xw, yw = self.IMAGE_OFF_XY  # 截取图像显示位置————(xw, yw)

        # 获取图像区域
        x0, y0 = xn-1 + xw, yn-1 + yw
        if xw <= x <= x0 and yw <= y <= y0:
            # 当鼠标移动到图像区域之内时更换图像
            self.instead_0, self.instead_1, self.instead_2 = self.IMAGE_ON, self.IMAGE_SIZE_ON, self.IMAGE_ON_XY
        else:
            # 当鼠标移动到图像区域之外时更换图像
            self.instead_0, self.instead_1, self.instead_2 = self.IMAGE_OFF, self.IMAGE_SIZE_OFF, self.IMAGE_OFF_XY
        insert_image(self.instead_0, self.instead_1, self.instead_2)

    def press(self, n=1):
        """ 定义按钮按下"""
        xn, yn = self.IMAGE_SIZE_OFF
        xw, yw = self.IMAGE_OFF_XY
        x0, y0 = xn-1 + xw, yn-1 + yw
        if xw <= x <= x0 and yw <= y <= y0:
            """ 点击后的事件"""
            if n:
                self.click_music()
            return True

    def click_music(self):
        """ 定义按钮音效"""
        click = pygame.mixer.Sound(self.MC_MUSIC)
        click.set_volume(MUSIC_BUTTON)
        click.play()

class InputBox(object):
    """ 定义一个输入框"""
    def __init__(self):
        """ 定义初始化方法"""
        self.input_open = []  # 是否打开输入框
        self.point_open = []  # 指针开关
        self.point_open_0, self.point_open_1 = (0, 0)  # 均匀指针闪烁
        self.point_time = 10  # 指针闪烁时长
        self.point_place = []  # 指针位置
        self.text = [['', ''] for _ in range(4)]  # 初始化4个输入框的文本存储————[[持续文本数据, 文本数据], ...]
        self.sx, self.sy = (None, None)     # 截取输入框大小————(sx, sy)
        self.gx, self.gy = (None, None)     # 截取输入框位置————(gx, gy)

        self.NUMBER = None                  # 输入框索引
        self.INPUT_SIZE = None              # 输入框大小
        self.INPUT_XY = None                # 输入框位置
        self.INPUT_COLOR_INSIDE = None      # 当鼠标移动到输入框之内时的颜色
        self.INPUT_COLOR_OUTSIDE = None     # 当鼠标移动到输入框之外时的颜色
        self.INPUT_SIZE_INSIDE = None       # 当鼠标移动到输入框之内时的输入框粗细
        self.INPUT_SIZE_OUTSIDE = None      # 当鼠标移动到输入框之外时的输入框粗细
        self.INPUT_COLOR_BG_IF_LIST = None  # 输入框背景颜色
        self.POINT_COLOR = None             # 指针颜色
        self.POINT_SIZE = None              # 指针粗细
        self.POINT_KIND_IF = None           # 指针样式
        self.TEXT_COLOR = None              # 文字颜色

    def house(self):
        """ 绘制一个输入框"""
        self.sx, self.sy = self.INPUT_SIZE
        self.gx, self.gy = self.INPUT_XY
        x0, y0 = self.sx-1 + self.gx, self.sy-1 + self.gy

        # 输入框背景
        if self.INPUT_COLOR_BG_IF_LIST[0]:
            ca, cb, cc = self.INPUT_COLOR_BG_IF_LIST[1]
            if self.INPUT_COLOR_BG_IF_LIST[2]:
                shade_bg((self.sx, self.sy), (ca, cb, cc, self.INPUT_COLOR_BG_IF_LIST[3]), (self.gx, self.gy))
            else:
                pygame.draw.rect(screen, (ca, cb, cc), (self.gx, self.gy, self.sx, self.sy), 0)

        if self.gx <= x <= x0 and self.gy <= y <= y0:
            # 当鼠标移动到输入框区域之内时更换输入框颜色
            pygame.draw.rect(screen, self.INPUT_COLOR_INSIDE, (self.gx, self.gy, self.sx, self.sy),
                             self.INPUT_SIZE_INSIDE)
            self.point_open[self.NUMBER] = True
        else:
            # 当鼠标移动到输入框之外时更换输入框颜色
            pygame.draw.rect(screen, self.INPUT_COLOR_OUTSIDE, (self.gx, self.gy, self.sx, self.sy),
                             self.INPUT_SIZE_OUTSIDE)
            self.point_open[self.NUMBER] = False

    def point(self):
        """ 绘制一个指针"""
        if self.input_open[self.NUMBER]:
            if self.point_open_0 % self.point_time == 0:
                self.point_open_0 = self.point_time - 1
                self.point_open_1 += 1
                if self.point_open_1 == self.point_time:
                    self.point_open_0 = 0
                    self.point_open_1 = 0
                else:
                    a = ((self.sy-3)/2) * (len(self.text[self.NUMBER][0]) + self.point_place[self.NUMBER])
                    if self.POINT_KIND_IF:
                        if a >= self.sx-6 - (self.sy-6)/2:
                            a = self.sx-6 - (self.sy-6)/2
                        gy, zx, sy = self.gy-self.POINT_SIZE-3 + self.sy, (self.sy-6)/2, self.POINT_SIZE
                    else:
                        if a >= self.sx-6:
                            a = self.sx-6
                        gy, zx, sy = self.gy+3, self.POINT_SIZE, self.sy-6
                    pygame.draw.rect(screen, self.POINT_COLOR, (self.gx+3 + a, gy, zx, sy), 0)
            self.point_open_0 += 1

    def press_frame_event(self):
        """ 点击输入框事件"""
        if self.point_open[self.NUMBER]:
            if self.input_open[self.NUMBER]:
                self.input_open[self.NUMBER] = False
                for i in range(len(self.point_place)):
                    self.point_place[i] = 0
            else:
                self.input_open[self.NUMBER] = True
        else:
            self.input_open[self.NUMBER] = False
            for i in range(len(self.point_place)):
                self.point_place[i] = 0

    def words(self, event):
        """ 记录文本数据"""
        if event.type == pygame.KEYDOWN:
            try:
                i = self.input_open.index(True)
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    if self.point_place[i] == 0:
                        self.text[i][0] = self.text[i][0][:self.point_place[i]-1]
                    else:
                        self.text[i][0] = self.text[i][0][:self.point_place[i]-1] + \
                                          self.text[i][0][self.point_place[i]:]
                elif event.key == pygame.K_LEFT:
                    if self.point_place[i] > -len(self.text[i][0]):
                        self.point_place[i] -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.point_place[i] < 0:
                        self.point_place[i] += 1
                else:
                    if self.point_place[i] == 0:
                        self.text[i][0] += event.unicode
                    else:
                        self.text[i][0] = self.text[i][0][:self.point_place[i]] + \
                                          event.unicode + \
                                          self.text[i][0][self.point_place[i]:]
            except:
                pass

    def bill(self):
        """ 显示文本数据"""
        if self.POINT_KIND_IF:
            a = int(self.sx / (self.sy/2))
        else:
            a = int(self.sx / (self.sy/2-1))
        b = 0
        if a <= len(self.text[self.NUMBER][0]):
            b = len(self.text[self.NUMBER][0]) - a
        FONT_XY.render_to(
            screen, (self.gx+3, self.gy+3), self.text[self.NUMBER][0][b:a+b], fgcolor=self.TEXT_COLOR, size=self.sy-3
        )

    def start(self):
        """ 加载输入框"""
        try:
            self.input_open[self.NUMBER]
            self.house()
            self.point()
            self.bill()
        except:
            a = len(self.input_open)
            b = self.NUMBER+1
            for i in range(b-a):
                self.input_open.append(False)
                self.point_open.append(False)
                self.text.append(['', ''])
                self.point_place.append(0)

class Message(object):
    """ 定义消息框"""
    def message_error(self, TEXT, NOTE):
        """ 错误消息框"""
        message = wx.MessageDialog(None, caption=TEXT,
                                   message=NOTE,
                                   style=wx.OK | wx.ICON_ERROR)
        message.ShowWindowModal()

    def message_info(self, TEXT, NOTE):
        """ 消息框"""
        message = wx.MessageDialog(None, caption=TEXT,
                                   message=NOTE,
                                   style=wx.OK | wx.ICON_INFORMATION)
        message.ShowWindowModal()

class Make_one_world(wx.Frame):
    """ 定义创建新世界的GUI"""
    def __init__(self, parent, id):
        """ 定义初始化方法"""
        wx.Frame.__init__(self, parent, id, '创建新世界',
                          pos=(460, 270), size=(400, 130))
        # 创建面板
        panel = wx.Panel(self)
        # 创建“确定”和“取消”按钮,并绑定事件
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        # 创建文本，左对齐
        self.label_user = wx.StaticText(panel, label="世界名:")
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        # 添加容器，容器中控件按横向并排排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

        number = 0  # 新的世界 + number，————"0 <= number <= 10"
        for i in range(len(Load_file.world_name)):
            name_all = Load_file.world_name[i][0][6:]
            if name_all == "新的世界 (" + str(number) + ")" or name_all == "新的世界":
                number += 1
        if number == 0:
            self.text_user.SetValue("新的世界")
        else:
            self.text_user.SetValue("新的世界 (" + str(number) + ")")

    def datawoulds(self, username):
        """ 创建一个存档"""
        adding = 'saves\\' + str(username)
        try:
            os.mkdir(adding)
            Message.message_info("创建世界", "创建成功！")
            def start_create(world_sd):
                open(world_sd, 'a+')
            start_create(adding + '\\' + 'block_image.dat')
            start_create(adding + '\\' + 'block_list.dat')
            start_create(adding + '\\' + 'world.dat')
            start_create(adding + '\\' + 'character.dat')
        except:
            Message.message_error("错误", "创建失败！")

    def OnclickSubmit(self, event):
        """ 点击确定按钮，执行方法"""
        username = self.text_user.GetValue()
        if username == '':
            Message.message_error('错误', '世界名不能为空！')
        elif username != '':
            if len(username.encode('GBK')) > 28:
                Message.message_error('错误', '世界名长度不能超过28个字节！')
            else:
                Make_one_world.datawoulds(self, username)

    def OnclickCancel(self, event):
        """ 点击取消按钮，执行方法"""
        self.text_user.SetValue("")

class Kill_one_world(wx.Frame):
    """ 定义删除世界的GUI"""
    def __init__(self, parent, id):
        """ 定义初始化方法"""
        wx.Frame.__init__(self, parent, id, title="删除世界",
                      pos=(450, 400), size=(400, 220))
        self.world_data = Load_file.world_name[Load_file.fcd][0]
        panel = wx.Panel(self)
        title = wx.StaticText(panel, label='确定要删除？', pos=(60, 30))
        font = wx.Font(24, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        wx.StaticText(panel, label='Name="' + str(self.world_data[6:]) + '"', pos=(80, 80))
        fons = wx.Font(10, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=130)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self, event):
        """ 点击确定按钮，执行方法"""
        try:
            shutil.rmtree(self.world_data)
            Message.message_info("删除世界", "删除成功！")
        except:
            Message.message_error("错误", "世界不存在！")

    def OnclickCancel(self, event):
        """ 点击取消按钮，执行方法"""
        pass

class Start_interface(object):
    """ 定义一个开始界面类"""
    def __init__(self):
        """ 定义初始化方法"""
        # 背景图片路径
        self.BG_IMAGE = [
            'bg', 'logo', 'loading', 'world_gui'
        ]
        # 背景音乐列表
        self.MUSIC_LIST = [
            'music\\C418 - Aria Math.mp3', 'music\\C418 - Haggstrom.mp3',
            'music\\C418 - Haunt Muskie.mp3', 'music\\C418 - Mice on Venus.mp3',
            'music\\C418 - Minecraft.mp3', 'music\\C418 - Minecraft_0.mp3',
            'music\\C418 - Sweden.mp3', 'music\\C418-Menu.mp3'
        ]
        self.click = False  # 跳转（开始界面|False）或（选择世界|True）界面
        self.click_set = False   # 跳转（开始界面|False）或（游戏设置|True）界面
        self.x, self.y = screen.get_size()  # 获取窗口大小

    def bg_music(self):
        """ 播放背景音乐"""
        # 定义背景音乐播放的函数
        def bg_music(music_file, volume):
            # 开始播放
            pygame.mixer.music.load(os.path.join(os.getcwd(), music_file))
            pygame.mixer.music.set_volume(volume)  # 设置音量

        # 当一首音乐被播放完以后
        if pygame.mixer.music.get_busy() == False:
            # 随机获取一首音乐路径并播放
            bg_music(random.choice(self.MUSIC_LIST), MUSIC_MAIN)
            pygame.mixer.music.play()

    def bg_image(self):
        """ 加载背景图片"""
        insert_image(self.BG_IMAGE[0], WINDOW_SIZE, (0, 0))
        mc_logo = insert_image_change(self.BG_IMAGE[1], (756, 121))
        mc_logo.set_colorkey((238, 243, 250))
        screen.blit(mc_logo, (self.x/2-756/2, 50))
        for i in range(5):
            FONT_XY.render_to(screen, (self.x/2-756/2+80-i, 185-i), 'Python--Edition--2D', fgcolor=(80, 80, 80), size=35)
        pygame.draw.rect(screen, (128, 128, 128), (self.x/2-756/2+75, 215, 345, 1), 0)

    def button_1(self, inherit):
        """ 定义“开始游戏”按钮"""
        Button_font.FONT_SIZE = fx = 30
        Button_font.BUTTON_NAME = fy = "开始游戏"
        Button_font.NMAE_XY = (self.x/2-fx*len(fy)/2, self.y/2-len(fy)/2-90)
        Button_font.BUTTON_COLOR_F = (0, 200, 255)
        Button_font.BUTTON_COLOR_T = (0, 255, 255)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_mo'
        Button_image.IMAGE_SIZE_OFF = (250, 50)
        Button_image.IMAGE_SIZE_ON = (252, 52)
        Button_image.IMAGE_OFF_XY = (self.x/2-fx*len(fy)/2-70, self.y/2-len(fy)/2-100)
        Button_image.IMAGE_ON_XY = (self.x/2-fx*len(fy)/2-71, self.y/2-len(fy)/2-101)
        if inherit:
            Button_image.button()
            Button_font.button()

    def button_2(self, inherit):
        """ 定义“退出游戏”按钮"""
        Button_font.BUTTON_NAME = fy = "退出游戏"
        Button_font.NMAE_XY = (self.x/2-Button_font.FONT_SIZE*len(fy)/2, self.y/2-len(fy)/2+90)
        Button_font.BUTTON_COLOR_F = (200, 0, 0)
        Button_font.BUTTON_COLOR_T = (255, 0, 0)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_mo'
        Button_image.IMAGE_SIZE_OFF = (250, 50)
        Button_image.IMAGE_SIZE_ON = (252, 52)
        Button_image.IMAGE_OFF_XY = (self.x/2-Button_font.FONT_SIZE*len(fy)/2-70, self.y/2-len(fy)/2+80)
        Button_image.IMAGE_ON_XY = (self.x/2-Button_font.FONT_SIZE*len(fy)/2-71, self.y/2-len(fy)/2+79)
        if inherit:
            Button_image.button()
            Button_font.button()

    def button_3(self, inherit):
        """ 定义“游戏设置”按钮"""
        Button_font.BUTTON_NAME = fy = "游戏设置"
        Button_font.NMAE_XY = (self.x/2-Button_font.FONT_SIZE*len(fy)/2, self.y/2-len(fy)/2)
        Button_font.BUTTON_COLOR_F = (200, 0, 200)
        Button_font.BUTTON_COLOR_T = (255, 0, 255)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_mo'
        Button_image.IMAGE_SIZE_OFF = (250, 50)
        Button_image.IMAGE_SIZE_ON = (252, 52)
        Button_image.IMAGE_OFF_XY = (self.x/2-Button_font.FONT_SIZE*len(fy)/2-70, self.y/2-len(fy)/2-10)
        Button_image.IMAGE_ON_XY = (self.x/2-Button_font.FONT_SIZE*len(fy)/2-71, self.y/2-len(fy)/2-11)
        if inherit:
            Button_image.button()
            Button_font.button()

    def press_1(self):
        """ 点击“开始游戏”按钮"""
        self.button_1(False)
        if Button_image.press():
            self.click = True

    def press_2(self):
        """ 点击“退出游戏”按钮"""
        self.button_2(False)
        if Button_image.press():
            sys.exit()

    def press_3(self):
        """ 点击“游戏设置”按钮"""
        self.button_3(False)
        if Button_image.press():
            self.click_set = True

class Selection_interface(object):
    """ 定义一个选择世界界面类"""
    def bg_image(self):
        """ 加载背景图片"""
        screen.blit(kill_all, (0, 0))  # 清空屏幕
        Start_interface.click = True    # 当按下开始游戏时
        insert_image(Start_interface.BG_IMAGE[2], WINDOW_SIZE, (0, 0))
        insert_image(
            Start_interface.BG_IMAGE[3], (Start_interface.x-300, Start_interface.y-260),
            (Start_interface.x/2-(Start_interface.x-300)/2, Start_interface.y/2-(Start_interface.y-260)/2)
        )
        # 显示标题
        FONT_XY.render_to(screen, (Start_interface.x/2-75*4/2, 50), "选择世界", fgcolor=(200, 200, 0), size=75)

    def key(self):
        """ 键盘事件（快捷键）"""
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:  # 当按下“Esc”键
            Button_font.click_music()
            Start_interface.click = False   # 返回到主界面

    def button_1(self, inherit):
        """ 定义“返回”按钮"""
        Button_font.FONT_SIZE = fx = 40
        Button_font.NMAE_XY = (30, Start_interface.y-fx-30)
        Button_font.BUTTON_NAME = "返回"
        Button_font.BUTTON_COLOR_F = (0, 200, 255)
        Button_font.BUTTON_COLOR_T = (0, 255, 255)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_oh'
        Button_image.IMAGE_SIZE_OFF = (110, 60)
        Button_image.IMAGE_SIZE_ON = (112, 62)
        Button_image.IMAGE_OFF_XY = (15, Start_interface.y-fx-44)
        Button_image.IMAGE_ON_XY = (14, Start_interface.y-fx-45)
        if inherit:
            Button_image.button()
            Button_font.button()

    def button_2(self, inherit):
        """ 定义“创建新世界”按钮"""
        Button_font.FONT_SIZE = fx = 30
        Button_font.NMAE_XY = (Start_interface.x/4, Start_interface.y-fx-40)
        Button_font.BUTTON_NAME = "创建新世界"
        Button_font.BUTTON_COLOR_F = (0, 200, 0)
        Button_font.BUTTON_COLOR_T = (0, 255, 0)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_oh'
        Button_image.IMAGE_SIZE_OFF = (170, 50)
        Button_image.IMAGE_SIZE_ON = (172, 52)
        Button_image.IMAGE_OFF_XY = (Start_interface.x/4-11, Start_interface.y-fx-51)
        Button_image.IMAGE_ON_XY = (Start_interface.x/4-12, Start_interface.y-fx-52)
        if inherit:
            Button_image.button()
            Button_font.button()

    def button_3(self, inherit):
        """ 定义“删除世界”按钮"""
        Button_font.NMAE_XY = (Start_interface.x/2, Start_interface.y-Button_font.FONT_SIZE-40)
        Button_font.BUTTON_NAME = "删除世界"
        Button_font.BUTTON_COLOR_F = (200, 0, 0)
        Button_font.BUTTON_COLOR_T = (255, 0, 0)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_oh'
        Button_image.IMAGE_SIZE_OFF = (140, 50)
        Button_image.IMAGE_SIZE_ON = (142, 52)
        Button_image.IMAGE_OFF_XY = (Start_interface.x/2-11, Start_interface.y-Button_font.FONT_SIZE-51)
        Button_image.IMAGE_ON_XY = (Start_interface.x/2-12, Start_interface.y-Button_font.FONT_SIZE-52)
        if inherit:
            Button_image.button()
            Button_font.button()

    def press_1(self):
        """ 点击“返回”按钮"""
        self.button_1(False)
        if Button_image.press():
            Start_interface.click = False

    def press_2(self):
        """ 点击“创建新世界”按钮"""
        self.button_2(False)
        if Button_image.press():
            app = wx.App()
            Make_one_world(parent=None, id=-1).Show()
            app.MainLoop()

    def press_3(self):
        """ 点击“删除世界”按钮"""
        self.button_3(False)
        if Button_image.press():
            if len(Load_file.world_name) != 0:
                app = wx.App()
                Kill_one_world(parent=None, id=-1).Show()
                app.MainLoop()

class Load_call_world(object):
    """ 定义一个加载世界类"""
    def __init__(self):
        """ 定义初始化方法"""
        self.JX, self.JY, self.JZ = (64, Start_interface.y-100, Start_interface.x/2-576/2)    # 物品列表位置
        self.tx, self.ty = (0, 1)   # 物品列表间隔
        self.block_use = [None, None, None, None, None, None, None, None, None]   # 主物品栏
        # 此内里的函数开关
        self.select_box_open = True
        self.block_throw_open = True
        self.block_use_key_open = True
        self.convenience_open = True
        self.read_font_open = True
        self.event_repeat_open = True
        self.table_open = False

    def event_repeat(self):
        """ 加载物品列表"""
        insert_image('inventory', (576, 64), (self.tx*self.JX+self.JZ, self.ty*self.JY))
        if Get_into_world.image_number > 8:
            Get_into_world.image_number = 0
        elif Get_into_world.image_number < 0:
            Get_into_world.image_number = 8
        insert_image('choice', (68, 68), (self.tx*self.JX+self.JZ-2 + 64*Get_into_world.image_number,
                                          self.ty*self.JY-2))
        self.block_add_use()

    def block_add_use(self):
        """ 把已选择的物品添加到主物品栏"""
        list_name_id = []
        for name_primary, name_id in dic_list[Object_paper.object_point].items():
            list_name_id.append(name_id[0])
        try:
            self.block_use[Get_into_world.image_number] = list_name_id[int(InputBox.text[0][1])]
            InputBox.text[0][1] = ''
        except:
            pass
        block_index = 0
        for block in self.block_use:
            insert_image(
                block, (45, 45),
                (self.tx*self.JX+self.JZ+10 + 64*block_index, self.ty*self.JY+10)
            )
            block_index += 1

    def block_use_key_num(self):
        """ 当按下数字键时"""
        keys_pressed = pygame.key.get_pressed()  # 键盘事件
        if keys_pressed[pygame.K_1]:
            Get_into_world.image_number = 0
        elif keys_pressed[pygame.K_2]:
            Get_into_world.image_number = 1
        elif keys_pressed[pygame.K_3]:
            Get_into_world.image_number = 2
        elif keys_pressed[pygame.K_4]:
            Get_into_world.image_number = 3
        elif keys_pressed[pygame.K_5]:
            Get_into_world.image_number = 4
        elif keys_pressed[pygame.K_6]:
            Get_into_world.image_number = 5
        elif keys_pressed[pygame.K_7]:
            Get_into_world.image_number = 6
        elif keys_pressed[pygame.K_8]:
            Get_into_world.image_number = 7
        elif keys_pressed[pygame.K_9]:
            Get_into_world.image_number = 8

    def block_use_key(self):
        """ 选定主物品栏的物品"""
        if InputBox.input_open != []:
            if not InputBox.input_open[0]:
                self.block_use_key_open = False
                self.block_use_key_num()
        elif self.block_use_key_open:
            self.block_use_key_num()

    def block_throw(self):
        """ 摧毁物品"""
        keys_pressed = pygame.key.get_pressed()  # 键盘事件
        if keys_pressed[pygame.K_q]:  # 当按下"Q"
            self.block_use[Get_into_world.image_number] = None

    def read_font(self):
        """ 显示字体"""
        CEPN_XY = (10, 10)            # 显示坐标的位置
        mx, my = Get_into_world.block_mxy()
        # 显示当前坐标
        FONT_XY.render_to(screen, CEPN_XY,
                          '坐标：(x=' + str(Get_into_world.ctcs_x + mx // Get_into_world.image_size) +
                          ', y=' + str(Get_into_world.ctcs_y - my // Get_into_world.image_size) +
                          ', z=' + str(Get_into_world.image_size) + ')',
                          (255-CA, 255-CB, 255-CC), size=15)
        # 显示当前世界时间
        FONT_XY.render_to(screen, (10, 30),
                          '时间：'+str(Get_into_world.day_time),
                          (255-CA, 255-CB, 255-CC), size=15)

    def button_1(self, inherit):
        """ 定义————[保存并退出世界]按钮"""
        Button_font.FONT_SIZE = fx = 15
        Button_font.BUTTON_NAME = fy = "保存并退出世界"
        Button_font.NMAE_XY = (Start_interface.x-fx*len(fy)-10, 10)
        Button_font.BUTTON_COLOR_F = (255-CA, 255-CB, 255-CC)
        Button_font.BUTTON_COLOR_T = (255, 0, 0)
        if inherit:
            Button_font.button()

    def select_box(self):
        """ 绘制选定框"""
        mx, my = Get_into_world.block_mxy()
        pygame.draw.rect(
            screen, (255-CA, 255-CB, 255-CC),
            (mx, my, Get_into_world.image_size, Get_into_world.image_size), 1
        )

    def convenience(self, event):
        """ 显示或隐藏信息"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_o: # 当按下"O"
                if self.read_font_open:
                    self.read_font_open = False
                    self.select_box_open = False
                else:
                    self.read_font_open = True
                    self.select_box_open = True
            elif event.key == pygame.K_p:   # 当按下"P"
                if self.event_repeat_open:
                    self.event_repeat_open = False
                else:
                    self.event_repeat_open = True
            elif event.key == pygame.K_i:  # 当按下"I"
                if self.table_open:
                    self.table_open = False
                    self.select_box_open = True
                else:
                    self.table_open = True
                    self.select_box_open = False

    def table(self):
        """ 显示网格"""
        for i in range(int(HIGHLY/Get_into_world.image_size)+1):
            pygame.draw.rect(screen, (0, 255-CB, 255-CC),
                             (0, i*Get_into_world.image_size, WIDTH, 1), 0)
        for i in range(int(WIDTH/Get_into_world.image_size)+1):
            pygame.draw.rect(screen, (0, 255-CB, 255-CC),
                             (i*Get_into_world.image_size, 0, 1, HIGHLY), 0)
        mx, my = Get_into_world.block_mxy()
        pygame.draw.rect(
            screen, (255-CA, 255-CB, 255-CC),
            (mx, my+Get_into_world.image_size/2, Get_into_world.image_size, 1), 0
        )
        pygame.draw.rect(
            screen, (255-CA, 255-CB, 255-CC),
            (mx+Get_into_world.image_size/2, my, 1, Get_into_world.image_size), 0
        )

class Get_into_world(object):
    """ 定义一个进入世界类"""
    def __init__(self):
        """ 定义初始化方法"""
        self.block_list, self.block_image = [], []  # 放置物体的所有id和坐标
        self.image_number = 0   # 物品地址
        self.image_size = 32    # 物体视距（z）
        self.ctcs_x, self.ctcs_y = (0, 0)   # 坐标计数器
        self.SPEED_M, self.SPEED_L = (1, 3) # 坐标轴正常移动速度, 坐标轴最快移动速度
        self.end_the_world = False          # 退出当前世界条件
        self.vibity_0, self.vibity_1 = (0, 0)   # 区块加载范围
        self.time_num = 0   # 时间时序计数器
        self.time_speed = 64    # 时间流逝速度(帧)
        self.ca, self.cb, self.cc, self.ue = (245, 255, 255, 1) # 天空颜色
        self.day_time = 12  # 24小时进制————{1时=100分; 5分=64帧}
        self.board = 0  # 是否静止当前时间————(0-默认，1-静止，2-向左流逝，3-向右流逝)
        self.img_size, self.img_xy = [], []  # 所有物体的大小及位置
        # 此类里的函数开关
        self.kill_block_open = True
        self.place_block_open = True
        self.key_block_open = True
        self.visibility_open = True
        self.move_coordinate_system_open = True
        self.mouse_end_world_open = True
        # 定义物体的音效文件
        self.sound_effect = [
            ['music\\1.mp3', 'music\\2.mp3', 'music\\8.mp3', 'music\\11.mp3', 'music\\18.mp3', 'music\\43.mp3',
             'music\\cloth5.mp3'],
            ['music\\7.mp3', 'music\\25.mp3', 'music\\26.mp3', 'music\\27.mp3', 'music\\28.mp3', 'music\\cloth2.mp3',
             'music\\cloth3.mp3', 'music\\wood3.mp3'],
            ['music\\12.mp3', 'music\\13.mp3'],
            ['music\\14.mp3', 'music\\15.mp3', 'music\\29.mp3'],
            ['music\\16.mp3', 'music\\cloth.mp3'],
            ['music\\3.mp3', 'music\\4.mp3', 'music\\5.mp3', 'music\\6.mp3','music\\9.mp3', 'music\\10.mp3',
             'music\\17.mp3', 'music\\30.mp3','music\\33.mp3', 'music\\34.mp3', 'music\\cloth4.mp3']
        ]

    def block_mxy(self):
        """ 方格算法"""
        mx, my = x // self.image_size * self.image_size, y // self.image_size * self.image_size
        return mx, my

    def block_music(self, imaget):
        """ 播放物体音效"""
        for name_primary, name_id in dic_list[Object_paper.object_point].items():
            if name_id[0] == imaget:
                if name_id[1] == 1:
                    list_music = self.sound_effect[0]
                elif name_id[1] == 2:
                    list_music = self.sound_effect[1]
                elif name_id[1] == 3:
                    list_music = self.sound_effect[2]
                elif name_id[1] == 4:
                    list_music = self.sound_effect[3]
                elif name_id[1] == 5:
                    list_music = self.sound_effect[4]
                elif name_id[1] == 6:
                    list_music = self.sound_effect[5]
                if name_id[1] != 0:
                    music_file = random.choice(list_music)  # 随机获取一个音效文件路径
                    block_music = pygame.mixer.Sound(music_file)
                    block_music.set_volume(MUSIC_BLOCK)
                    block_music.play()

    def kill_window(self):
        """ 定义填充物体"""
        kill = pygame.Surface((self.image_size, self.image_size), flags=pygame.SRCALPHA)
        pygame.Surface.convert(kill)
        kill.fill(pygame.Color(CA, CB, CC, 255))
        return kill

    def kill_block(self):
        """ 鼠标左键填充物体"""
        mx, my = self.block_mxy()
        kill = self.kill_window()
        screen.blit(kill, (mx, my))  # 填充一个物体
        # 删除列表中的一个物体坐标
        if [mx, my] in self.block_list:
            block_image_zc = []  # 物体的位置
            # 循环填充一个位置的物体直到物体被填完
            while True:
                try:
                    # 记录当前位置的物体id
                    block_image_zc = self.block_image[self.block_list.index([mx, my])]
                    del self.block_image[self.block_list.index([mx, my])]
                    self.block_list.remove([mx, my])
                except:
                    # 播放填充的物体音效
                    self.block_music(block_image_zc)
                    break

    def place_block(self):
        """ 鼠标右键放置物品"""
        mx, my = self.block_mxy()
        self.kill_block()   # 先填充
        # 后放置
        try:
            image = Load_call_world.block_use[self.image_number]
            # 添加一个物体坐标和物体id到列表
            self.block_list.append([mx, my])
            self.block_image.append(image)
            self.block_music(image)  # 播放当前物体音效
        except:
            pass

    def key_block(self):
        """ 获取键盘事件"""
        key_repeat = pygame.key.get_pressed()
        if key_repeat[pygame.K_x]:  # 当按下"X"键
            # 循环放置
            while True:
                self.place_block()
                if key_repeat[pygame.K_x]:  # 当"X"键弹起
                    break
        elif key_repeat[pygame.K_z]:    # 当按下"Z"键
            # 循环填充
            while True:
                self.kill_block()
                if key_repeat[pygame.K_z]:  # 当"Z"键弹起
                    break

    def start_moving(self, block_poe):
        """ 刷新所有方块"""
        # 清空物体坐标列表，添加新的物体坐标
        del self.block_list[0:]
        for ope_data in block_poe:
            self.block_list.append(ope_data)
        screen.blit(kill_all, (0, 0))  # 清空屏幕

        # 所有的物体坐标和物体id————[[x, y, id], [x, y, id], ...]
        block_nexy_all = []
        for i in range(len(self.block_list)):
            block_nexy_all.append([
                self.block_list[i][0], self.block_list[i][1],
                self.block_image[i]
            ])
        # 根据物体id和坐标放置物体
        del self.img_size[:], self.img_xy[:]
        for block_data in block_nexy_all:
            # 区域加载器
            if block_data[0] < 0+self.vibity_1 or block_data[1] < 0+self.vibity_1 or \
                    block_data[0] > WIDTH-self.vibity_1 or block_data[1] > HIGHLY-self.vibity_1:
                pass
            else:
                road = insert_image(
                    block_data[2], (self.image_size, self.image_size), (block_data[0], block_data[1])
                )
                if road != None:
                    self.img_size.append(road.get_rect())
                    self.img_xy.append([block_data[0], block_data[1]])

    def visibility(self):
        """ 区块加载范围"""
        keys_pressed = pygame.key.get_pressed()  # 键盘事件
        if keys_pressed[pygame.K_PERIOD]:  # 当按下"<"
            self.vibity_0 += 1
        elif keys_pressed[pygame.K_COMMA]:  # 当按下">"
            self.vibity_0 -= 1
        if HIGHLY-self.vibity_1*2 < 0:
            self.vibity_0 -= 1
        elif HIGHLY-self.vibity_1*2 > HIGHLY:
            self.vibity_0 += 1
        self.vibity_1 = self.image_size * self.vibity_0

        pygame.draw.rect(
            screen, (0, 0, 255),(
                self.vibity_1-1, self.vibity_1-1, WIDTH-self.vibity_1*2+2, HIGHLY-self.vibity_1*2+2
            ), 1
        )

    def move_coordinate_system(self):
        """ 移动坐标系——(x, y, z)"""
        xy_speed = False    # 最快速度的条件
        ZX, ZY = (0, 101)  # (z)的取值范围————{z|z=(x, y), x>=0, (x, y)∈R}

        keys_pressed = pygame.key.get_pressed() # 键盘事件
        if keys_pressed[pygame.K_w]:    # 当按下"W"
            # 把所有物体的坐标加一格像素并添加到这个列表
            block_poe = []
            for block_xy in self.block_list:
                if keys_pressed[pygame.K_LCTRL]:  # 当按下"Ctrl"键
                    block_poe.append([block_xy[0], block_xy[1] + self.image_size * self.SPEED_L])    # 加速
                    xy_speed = True
                else:
                    block_poe.append([block_xy[0], block_xy[1] + self.image_size * self.SPEED_M])    # 正常速度
            self.start_moving(block_poe)  # 调用后所有物体移动一格
            # 记录当前坐标
            if xy_speed:
                self.ctcs_y += self.SPEED_L
            else:
                self.ctcs_y += self.SPEED_M

        elif keys_pressed[pygame.K_s]:  # 当按下"S"
            block_poe = []
            for block_xy in self.block_list:
                if keys_pressed[pygame.K_LCTRL]:  # 当按下"Ctrl"键
                    block_poe.append([block_xy[0], block_xy[1] - self.image_size * self.SPEED_L])
                    xy_speed = True
                else:
                    block_poe.append([block_xy[0], block_xy[1] - self.image_size * self.SPEED_M])
            self.start_moving(block_poe)
            if xy_speed:
                self.ctcs_y -= self.SPEED_L
            else:
                self.ctcs_y -= self.SPEED_M

        if keys_pressed[pygame.K_a]:  # 当按下"A"
            block_poe = []
            for block_xy in self.block_list:
                if keys_pressed[pygame.K_LCTRL]:  # 当按下"Ctrl"键
                    block_poe.append([block_xy[0] + self.image_size * self.SPEED_L, block_xy[1]])
                    xy_speed = True
                else:
                    block_poe.append([block_xy[0] + self.image_size * self.SPEED_M, block_xy[1]])

            self.start_moving(block_poe)
            if xy_speed:
                self.ctcs_x -= self.SPEED_L
            else:
                self.ctcs_x -= self.SPEED_M

        elif keys_pressed[pygame.K_d]:  # 当按下"D"
            block_poe = []
            for block_xy in self.block_list:
                if keys_pressed[pygame.K_LCTRL]:  # 当按下"Ctrl"键
                    block_poe.append([block_xy[0] - self.image_size * self.SPEED_L, block_xy[1]])
                    xy_speed = True
                else:
                    block_poe.append([block_xy[0] - self.image_size * self.SPEED_M, block_xy[1]])
            self.start_moving(block_poe)
            if xy_speed:
                self.ctcs_x += self.SPEED_L
            else:
                self.ctcs_x += self.SPEED_M

        #### 物体视距范围(z)||默认(1~100)
        if keys_pressed[pygame.K_LSHIFT] and self.image_size + 1 != ZY:     # 当按下"Shift"键
            self.image_size += 1
            block_poe = []
            for block_xy in self.block_list:
                block_poe.append([(block_xy[0] / (self.image_size - 1)) * self.image_size,
                                  (block_xy[1] / (self.image_size - 1)) * self.image_size])
            self.start_moving(block_poe)

        elif keys_pressed[pygame.K_SPACE] and self.image_size - 1 != ZX:    # 当按下空格
            self.image_size -= 1
            block_poe = []
            for block_xy in self.block_list:
                block_poe.append([(block_xy[0] / (self.image_size + 1)) * self.image_size,
                                  (block_xy[1] / (self.image_size + 1)) * self.image_size])
            self.start_moving(block_poe)

    def screen_repeat(self):
        """ 刷新屏幕"""
        block_poe = []
        for block_xy in self.block_list:
            block_poe.append([block_xy[0], block_xy[1]])
        self.start_moving(block_poe)

    def mouse_end_world(self):
        """ 点击退出世界（鼠标）————{end the world...}"""
        Load_call_world.button_1(False)
        if Button_font.press():
            self.end_the_world = True

    def key_end_world(self, event):
        """ 退出（键盘快捷键）"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:  # 当按下"Esc"
                if Object_paper.openife:
                    Object_paper.if_object_()   # 关闭物品栏
                elif Communication.compen:
                    Communication.con_if__()    # 关闭聊天栏
                else:
                    self.end_the_world = True   # 退出世界返回到主界面（快捷键）

    def writing(self):
        """ 保存世界进度界面"""
        insert_image('loading', WINDOW_SIZE, (0, 0))
        shade_bg(WINDOW_SIZE, (255, 100, 0, 100), (0, 0))
        FONT_XY.render_to(screen, (WIDTH/2-100, HIGHLY/2), '正在保存世界中...', fgcolor=(0, 0, 0), size=25)
        pygame.display.flip()

    def implement_end_world(self):
        """ 清空全部寄存器——[列表]并退出当前世界存档（回归默认值）"""
        if self.end_the_world:
            self.writing()
            Button_font.click_music()
            self.end_the_world = False
            pygame.display.set_caption('Minecraft 2D')
            self.roll = False
            Load_file.roll = False
            Start_interface.click = False
            del Load_file.write[:], Load_file.world_name[:]
            del self.block_list[:], self.block_image[:]
            self.ctcs_x, self.ctcs_y = (0, 0)
            self.image_number = 0
            self.image_size = 32
            Load_file.distance = 0
            Load_file.fcd = 0
            self.vibity_0, self.vibity_1 = (0, 0)
            self.move_0, self.move_1 = (0, 0)
            self.x0x0, self.y0y0 = (0, 0)
            del InputBox.input_open[:]
            del InputBox.text[:]
            Load_call_world.block_use = [None, None, None, None, None, None, None, None, None]
            del Communication.information[:]
            del Communication.screen_text_color[:]
            del Communication.order_data[:]
            Communication.copy_obj.clear()
            Communication.copy_out.clear()
            Communication.screen_copy.clear()
            Communication.screen_glue.clear()
            self.time_num, self.time_speed = 0, 64
            self.ca, self.cb, self.cc, self.ue = (230, 255, 255, 1)
            self.day_time, self.board = 12, 0
            Load_call_world.read_font_open = True
            Load_call_world.select_box_open = True
            Load_call_world.event_repeat_open = True
            Load_call_world.table_open = False
            Load_call_world.select_box_open = True
            Open_Character.exit_world()

    def preservation_world_data(self):
        """ 写入世界数据并保存"""
        n = Load_file.write[0]
        objects = open(Load_file.world_name[n][0] + '\\block_image.dat', 'w')
        locations = open(Load_file.world_name[n][0] + '\\block_list.dat', 'w')
        world = open(Load_file.world_name[n][0] + '\\world.dat', 'w')

        objects.write('%s'% self.block_image)
        locations.write('%s'% self.block_list)
        world.write('%s'% [
            [self.ctcs_x, self.ctcs_y], self.image_number, self.image_size, Load_call_world.block_use,
            [Communication.copy_obj, Communication.copy_out, Communication.screen_copy, Communication.screen_glue],
            self.time_num, self.time_speed, [self.ca, self.cb, self.cc, self.ue], self.day_time, self.board
        ])

        objects.close()
        locations.close()
        world.close()

        Open_Character.write_dat(n)

    def daytime(self):
        """ 世界时间（白天和黑夜）"""
        global kill_all, CA, CB, CC
        CA, CB, CC = self.ca, self.cb, self.cc
        kill_all = kill_window()
        self.day_time = self.ca

        if self.day_time == 230:
            self.ue = 1
        elif self.day_time == 0:
            self.ue = 0

        if self.time_num%self.time_speed == 0:
            if self.ue:
                self.ca -= 1; self.cb -= 1; self.cc -= 1
            else:
                self.ca += 1; self.cb += 1; self.cc += 1; self.ue = 0

        if self.time_num == 999:
            self.time_num = 1
        else:
            self.time_num += 1

class Load_file(object):
    """ 定义一个加载存档类"""
    def __init__(self):
        """ 定义初始化方法"""
        self.world_name = []    # 获取全部世界
        self.roll = False   # 是否使用鼠标滚轮
        # 存档地址
        self.distance = 0
        self.fcd = 0
        self.xyg = []   # 存档的点击位置
        self.write = []     # 世界数据地址
        self.x_name, self.y_name = (270, 200)   # 加载存档的显示位置
        # 加载存档的长度和间距
        self.long_z, self.spacing = (Start_interface.y/2-(Start_interface.y-260)/2 + Start_interface.y-330, 50)
        self.font_size, self.click_long = (30, Start_interface.x-300) # 字体大小和按下的长度

        self.data_name = None   # 存档data内的所有文件名
        self.data = []  # 存档data内的所有文件名的分割形式

    def all(self):
        """ 获取全部存档"""
        del self.world_name[:]
        for roos, dirs, files in os.walk('saves'):
            # 获取全部存档数据
            if len(roos.split('\\')) == 2:
                self.world_name.append([roos, files])

    def intercept_name(self, i):
        """ 截取世界存档名字的长度，范围：(最大28字节)"""
        name_go = str(i[0][str(i[0]).rindex('\\') + 1:])
        if len(str(i[0][str(i[0]).rindex('\\') + 1:]).encode('GBK')) > 28:
            name_go = str(i[0][str(i[0]).rindex('\\') + 1:]).encode('GBK')[:28].decode('GBK') + "."
        return name_go

    def load(self):
        """ 加载全部世界存档"""
        number = int((self.long_z - self.y_name) / self.spacing + self.fcd) # 加载世界个数
        for i in self.world_name[self.fcd:number]:
            xg, yg = self.x_name, self.y_name + self.distance * 50  # 加载存档的显示位置
            name_go = self.intercept_name(i)
            del self.xyg[:]
            self.xyg.append((xg, yg))

            Button_image.IMAGE_OFF = 'button_off'
            Button_image.IMAGE_ON = 'button_on'
            Button_image.IMAGE_SIZE_OFF = (Start_interface.x-300-xg, 50)
            Button_image.IMAGE_SIZE_ON = (Start_interface.x-300-xg, 50)
            Button_image.IMAGE_OFF_XY = (xg, yg-10)
            Button_image.IMAGE_ON_XY = (xg, yg-10)
            Button_image.button()

            # 加载世界名称
            if yg < self.long_z:
                FONT_XY.render_to(screen, (xg+20, yg), name_go, fgcolor=(100, 200, 200), size=30)
            x0, y0 = self.click_long-1, self.font_size-1 + yg
            if xg <= x <= x0 and yg <= y <= y0:
                if yg < self.long_z:
                    FONT_XY.render_to(screen, (xg+20, yg), name_go, fgcolor=(0, 255, 255), size=30)
            FONT_XY.render_to(screen, (Start_interface.x-300, 200), "<<<", fgcolor=(255, 0, 0), size=45)

            self.distance += 1  # 下一个存档地址
            self.mouse_click()
        if not self.roll:
            self.distance -= self.distance  # 当存档地址到达限定范围后重置世界存档地址

    def archive_site(self):
        """ 存档地址（n）"""
        n = self.distance + self.fcd -1    # 上一个世界存档地址
        self.write.append(n)    # 添加到write列表以保存世界数据（世界数据地址）
        Get_into_world.area = self.write[0]
        '''
        # 测试存档地址是否超出索引地址范围
        try:
            with open(self.world_name[n][0] + '\\' + self.world_name[n][1][0], 'r'):
                pass
        except:
            n = self.distance + self.fcd - 2    # 返回上一个世界存档地址
            del self.write[:]
            self.write.append(n)    # 添加到write列表以保存世界数据（世界数据地址）
        return n
        '''

    def mouse_roll(self):
        """ 当鼠标滚轮滚动时（选择存档）"""
        if Start_interface.click:
            if self.fcd != len(self.world_name) + 1:
                if event.button == 4:  # 向上滚动
                    self.fcd -= 1   # 上一个存档地址
                elif event.button == 5:  # 向下滚动
                    self.fcd += 1   # 下一个存档地址
                if self.fcd < 0:    # 当存档地址到达顶端时
                    self.fcd -= self.fcd
            else:
                self.fcd -= 1   # 当存档地址到达底端时

    def mouse_click(self):
        """ 当鼠标点击存档时"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键
                for xg, yg in self.xyg:
                    x0, y0 = self.click_long-1, self.font_size-1 + yg
                    if xg <= x <= x0 and yg <= y <= y0 and yg < self.long_z:
                        Button_font.click_music()
                        self.reading()
                        self.archive_site()
                        try:
                            self.file_data(self.write[0])
                        except:
                            app = wx.App(False)
                            Message.message_error("错误", "读取世界数据时出错！")
                            app.MainLoop()

    def reading(self):
        """ 读取进度界面"""
        insert_image('loading', WINDOW_SIZE, (0, 0))
        shade_bg(WINDOW_SIZE, (255, 100, 0, 100), (0, 0))
        FONT_XY.render_to(screen, (WIDTH/2-100, HIGHLY/2), '正在读取世界中...', fgcolor=(0, 0, 0), size=25)
        pygame.display.flip()

    def file_data(self, n):
        """ 读取已点击的世界存档数据（读取世界数据）"""
        del Get_into_world.block_list[:], Get_into_world.block_image[:]  # 清空临时数据
        with open(self.world_name[n][0] + '\\block_image.dat', 'r') as image_data:
            image_data = image_data.read()
            with open(self.world_name[n][0] + '\\block_list.dat', 'r') as list_data:
                list_data = list_data.read()
                with open(self.world_name[n][0] + '\\world.dat', 'r') as world:
                    world = world.read()
                    if world != '':
                        str_list = ast.literal_eval(world)
                        Get_into_world.ctcs_x += int(str_list[0][0])
                        Get_into_world.ctcs_y += int(str_list[0][1])
                        Get_into_world.image_number += int(str_list[1])
                        Get_into_world.image_size = 0
                        Get_into_world.image_size += int(str_list[2])
                        Load_call_world.block_use = str_list[3]
                        Communication.copy_obj = str_list[4][0]
                        Communication.copy_out = str_list[4][1]
                        Communication.screen_copy = str_list[4][2]
                        Communication.screen_glue = str_list[4][3]
                        Get_into_world.time_num = str_list[5]
                        Get_into_world.time_speed = str_list[6]
                        Get_into_world.ca, Get_into_world.cb, \
                        Get_into_world.cc, Get_into_world.ue = str_list[7]
                        Get_into_world.day_time = str_list[8]
                        Get_into_world.board = str_list[9]
                if list_data != '':
                    str_list = ast.literal_eval(list_data)
                    for data_list in str_list:
                        Get_into_world.block_list.append(data_list)
            if image_data != '':
                str_list = ast.literal_eval(image_data)
                for data_list in str_list:
                    Get_into_world.block_image.append(data_list)
            self.roll = True  # 添加条件退出主界面进入游戏
            letter = f'Minecraft 2D--wrold_address={Load_file.world_name[n][0]}'
            pygame.display.set_caption(letter)
            Get_into_world.daytime()
            Open_Character.read_dat(Load_file, n)

class Object_paper(object):
    """ 定义一个物品栏类"""
    def __init__(self):
        """ 定义初始化方法"""
        self.openife = False    # 是否打开物品栏
        # 物品栏的颜色
        self.color_paper_inside = (128, 128, 128)
        self.color_paper_outside = (64, 64, 64)
        # 物品栏的物品属性
        self.x_object, self.y_object = (WIDTH/2-330, HIGHLY/2-250)  # 位置
        self.size_object = 40   # 大小
        self.num_0, self.num_1 = (0, 0) # 物品栏物品的行数
        self.n = 0  # 滑轮
        self.skite = 8  # 物品栏物品的列数
        self.index_block = 0    # 物品代号
        self.text_color = (0, 0, 0)
        self.object_point = 3   # 物品栏指针
        self.color_choose_use = (0, 255, 255)   # 物品栏选择框的颜色
        self.press_object = False   # 是否点击物品
        # 拖动的物品
        self.pull_move = None
        self.rxy = (None, None)
        self.exchange = False
        self.press_0_open = True    # 此类里的函数开关

    def paper(self):
        """ 创建一张纸，并装饰（绘制物品栏）"""
        sx, sy = Load_call_world.tx*Load_call_world.JX+Load_call_world.JZ, Load_call_world.ty*Load_call_world.JY
        # 添加阴影效果
        shade_bg((WIDTH, sy), (0, 0, 0, 128), (0, 0))
        shade_bg((sx, sy), (0, 0, 0, 128), (0, sy))
        shade_bg((WIDTH-sx-576, sy), (0, 0, 0, 128), (sx+576, sy))
        shade_bg((576, HIGHLY-sy-64), (0, 0, 0, 128), (sx, sy+64))
        pygame.draw.rect(screen, self.color_paper_inside, (WIDTH/2-350, HIGHLY/2-270, 700, 500), 0)     # 背景
        pygame.draw.rect(screen, self.color_paper_outside, (WIDTH/2-350, HIGHLY/2-270, 700, 500), 15)   # 边框

    def button_0(self, inherit):
        """ 定义“物品栏”按钮"""
        jx, jy, jz, tx, ty = Load_call_world.JX, Load_call_world.JY, Load_call_world.JZ, \
                             Load_call_world.tx, Load_call_world.ty
        Button_image.IMAGE_OFF = 'object_off'
        Button_image.IMAGE_ON = 'object_on'
        Button_image.IMAGE_SIZE_OFF = (45, 45)
        Button_image.IMAGE_SIZE_ON = (39, 39)
        Button_image.IMAGE_OFF_XY = (tx*jx+jz+586, ty*jy+10)
        Button_image.IMAGE_ON_XY = (tx*jx+jz+589, ty*jy+13)
        if inherit:
            Button_image.button()

    def press_0(self):
        """ 点击“物品栏”按钮"""
        self.button_0(False)
        if Button_image.press():
            self.if_object_()

    def if_object_(self):
        """ 判断物品栏是否打开或关闭"""
        Button_image.click_music()
        if self.openife:
            self.openife = False
            InputBox.input_open[0] = False
            InputBox.text[0][0] = ''
            self.object_point, self.n, self.skite = 3, 0, 8
            Load_call_world.select_box_open = True
            Get_into_world.kill_block_open = True
            Get_into_world.place_block_open = True
            Get_into_world.key_block_open = True
            Get_into_world.visibility_open = True
            Get_into_world.move_coordinate_system_open = True
            Get_into_world.mouse_end_world_open = True
            Load_call_world.convenience_open = True
            self.pull_move = None
        else:
            self.openife = True
            Load_call_world.select_box_open = False
            Get_into_world.kill_block_open = False
            Get_into_world.place_block_open = False
            Get_into_world.key_block_open = False
            Get_into_world.visibility_open = False
            Get_into_world.move_coordinate_system_open = False
            Get_into_world.mouse_end_world_open = False
            Load_call_world.convenience_open = False

    def open(self, event):
        """ 打开一张纸"""
        sx, sy = Load_call_world.tx*Load_call_world.JX+Load_call_world.JZ, Load_call_world.ty*Load_call_world.JY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:   # 当按下"E"
                self.if_object_()
        if self.openife:
            if event.type == pygame.MOUSEBUTTONUP:  # 鼠标滚动
                if event.button == 4:  # 向上滚动
                    if self.skite >= 8:
                        self.n -= 1
                        self.skite -= 1
                    else:
                        self.n = 0
                        self.skite = 8
                elif event.button == 5:  # 向下滚动
                    if self.skite <= int(len(dic_list[self.object_point])/13):
                        self.n += 1
                        self.skite += 1
                    else:
                        self.n -= 1
                        self.skite = int(len(dic_list[self.object_point])/13)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
                if event.button == 1:  # 左键
                    self.press_1()
                    self.press_2()
                    self.press_3()
                    self.press_4()
                    self.press_object = True
                    for i in range(9):
                        wx, wy = (sx+10+64*i, sy+10)
                        if wx <= x <= wx + 45 and wy <= y <= wy + 45:
                            self.exchange = True
                elif event.button == 3:  # 右键
                    self.pull_move = None

    def opened(self):
        """ 物品栏打开后"""
        if self.openife:
            self.paper()
            self.get_block()
            self.place_find()
            self.find_block()
            self.choose_box()
            self.choose_object_use()
            self.button_1(True)
            self.button_2(True)
            self.button_3(True)
            self.button_4(True)

    def find_block(self):
        """ 定义查找物品的输入框"""
        FONT_XY.render_to(
            screen, (WIDTH/2-250, HIGHLY/2-328), "输入选择的物品代号：", fgcolor=(30, 30, 30), size=30
        )
        FONT_XY.render_to(
            screen, (WIDTH/2-60, HIGHLY/2-276), "搜索物品：", fgcolor=(130, 160, 190), size=13
        )
        InputBox.NUMBER = 0
        InputBox.INPUT_SIZE = (50, 25)
        InputBox.INPUT_XY = (WIDTH/2, HIGHLY/2-290)
        InputBox.INPUT_COLOR_INSIDE = (64, 64, 64)
        InputBox.INPUT_COLOR_OUTSIDE = (128, 128, 128)
        InputBox.INPUT_SIZE_INSIDE = 1
        InputBox.INPUT_SIZE_OUTSIDE = 1
        InputBox.INPUT_COLOR_BG_IF_LIST = [True, (200, 200, 200), False]
        InputBox.POINT_COLOR = (64, 64, 64)
        InputBox.POINT_SIZE = 1
        InputBox.POINT_KIND_IF = False
        InputBox.TEXT_COLOR = self.text_color
        InputBox.start()

    def find_block_key(self, event):
        """ 按钮回调事件"""
        InputBox.NUMBER = 0
        if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
            if event.button == 1:  # 左键
                InputBox.press_frame_event()

        elif event.type == pygame.KEYDOWN:
            if InputBox.input_open[InputBox.NUMBER]:
                if event.key == pygame.K_RETURN:  # 当按下“回车”键时
                    InputBox.text[InputBox.input_open.index(True)][1] = \
                        InputBox.text[InputBox.input_open.index(True)][0]
                    InputBox.text[InputBox.input_open.index(True)][0] = ''

    def choose_box(self):
        """ 显示已搜索的物品栏（选择物品）"""
        list_name_id = []
        pygame.draw.rect(screen, self.color_paper_inside, (WIDTH/2+60, HIGHLY/2-329, 64, 64), 0)
        pygame.draw.rect(screen, self.color_paper_outside, (WIDTH/2+60, HIGHLY/2-329, 64, 64), 5)
        for name_primary, name_id in dic_list[self.object_point].items():
            list_name_id.append(name_id[0])
        try:
            self.text_color = (0, 0, 0)
            insert_image(list_name_id[int(InputBox.text[0][0])], (50, 50), (WIDTH/2+67, HIGHLY/2-322))
        except:
            self.text_color = (255, 0, 0)

    def get_block(self):
        """ 获取物品"""
        n = 0
        for name_primary, name_id in dic_list[self.object_point].items():
            if (self.skite-8)*13-n == 0:
                if self.num_1 <= self.skite:
                    insert_image(
                        name_id[0], (self.size_object, self.size_object),
                        (self.x_object+(self.size_object+11)*self.num_0, self.y_object)
                    )
                    FONT_XY.render_to(
                        screen, (self.x_object+(self.size_object+11)*self.num_0, self.y_object+41),
                        str(self.index_block), fgcolor=(30, 30, 30), size=10
                    )
                    Button_image.IMAGE_SIZE_OFF = (self.size_object, self.size_object)
                    Button_image.IMAGE_OFF_XY = (self.x_object+(self.size_object+11)*self.num_0, self.y_object)
                    if Button_image.press(0):
                        if self.press_object:
                            self.pull_move = name_id[0]
                    self.index_block += 1
            else:
                n += 1
            self.num_0 += 1
            if self.num_0%13 == 0:
                self.num_0 = 0
                self.num_1 += 1
                self.y_object += self.size_object+11
        self.y_object = HIGHLY/2-250 - (self.size_object+11)*self.n
        self.num_0, self.num_1 = (0, 0)
        self.index_block = self.n*13
        self.press_object = False

    def place_find(self):
        """ 拖动物品"""
        self.rxy = (x, y)
        sx, sy = Load_call_world.tx*Load_call_world.JX+Load_call_world.JZ, Load_call_world.ty*Load_call_world.JY
        for i in range(9):
            wx, wy = (sx+10+64*i, sy+10)
            if wx <= x <= wx+45 and wy <= y <= wy+45:
                self.rxy = (wx, wy)
                if self.exchange:
                    self.exchange = False
                    Load_call_world.block_use[i] = self.pull_move
                    self.pull_move = None
        insert_image(self.pull_move, (45, 45), self.rxy)

    def choose_object_use(self):
        """ 绘制选择物品栏按钮"""
        pygame.draw.rect(screen, self.color_paper_inside, (WIDTH/2-400, HIGHLY/2-250, 55, 234), 0)
        pygame.draw.rect(screen, self.color_paper_outside, (WIDTH/2-400, HIGHLY/2-250, 55, 55), 5)
        pygame.draw.rect(screen, self.color_paper_outside, (WIDTH/2-400, HIGHLY/2-191, 55, 55), 5)
        pygame.draw.rect(screen, self.color_paper_outside, (WIDTH/2-400, HIGHLY/2-132, 55, 55), 5)
        pygame.draw.rect(screen, self.color_paper_outside, (WIDTH/2-400, HIGHLY/2-73, 55, 55), 5)
        if self.object_point == 1:
            oy = 132
        elif self.object_point == 2:
            oy = 191
        elif self.object_point == 3:
            oy = 250
        elif self.object_point == 4:
            oy = 73
        pygame.draw.rect(screen, self.color_choose_use, (WIDTH/2-400, HIGHLY/2-oy, 55, 55), 5)

    def button_1(self, inherit):
        """ 定义“建筑方块的物品栏”按钮"""
        Button_image.IMAGE_OFF = 'grass_block_side'
        Button_image.IMAGE_ON = 'grass_block_side'
        Button_image.IMAGE_SIZE_OFF = (45, 45)
        Button_image.IMAGE_SIZE_ON = (39, 39)
        Button_image.IMAGE_OFF_XY = (WIDTH/2-395, HIGHLY/2-245)
        Button_image.IMAGE_ON_XY = (WIDTH/2-392, HIGHLY/2-242)
        if inherit:
            Button_image.button()

    def button_2(self, inherit):
        """ 定义“红石方块的物品栏”按钮"""
        Button_image.IMAGE_OFF = 'redstone_block'
        Button_image.IMAGE_ON = 'redstone_block'
        Button_image.IMAGE_SIZE_OFF = (45, 45)
        Button_image.IMAGE_SIZE_ON = (39, 39)
        Button_image.IMAGE_OFF_XY = (WIDTH/2-395, HIGHLY/2-186)
        Button_image.IMAGE_ON_XY = (WIDTH/2-392, HIGHLY/2-183)
        if inherit:
            Button_image.button()

    def button_3(self, inherit):
        """ 定义“其他物品的物品栏”按钮"""
        Button_image.IMAGE_OFF = 'crafting_table_front'
        Button_image.IMAGE_ON = 'crafting_table_front'
        Button_image.IMAGE_SIZE_OFF = (45, 45)
        Button_image.IMAGE_SIZE_ON = (39, 39)
        Button_image.IMAGE_OFF_XY = (WIDTH/2-395, HIGHLY/2-127)
        Button_image.IMAGE_ON_XY = (WIDTH/2-392, HIGHLY/2-124)
        if inherit:
            Button_image.button()

    def button_4(self, inherit):
        """ 定义“所有物品的物品栏”按钮"""
        Button_image.IMAGE_OFF = 'find_all_object'
        Button_image.IMAGE_ON = 'find_all_object'
        Button_image.IMAGE_SIZE_OFF = (45, 45)
        Button_image.IMAGE_SIZE_ON = (39, 39)
        Button_image.IMAGE_OFF_XY = (WIDTH/2-395, HIGHLY/2-68)
        Button_image.IMAGE_ON_XY = (WIDTH/2-392, HIGHLY/2-65)
        if inherit:
            Button_image.button()

    def press_1(self):
        """ 点击“建筑方块的物品栏”按钮"""
        self.button_1(False)
        if Button_image.press():
            self.object_point = 3
            self.n, self.skite = 0, 8

    def press_2(self):
        """ 点击“红石方块的物品栏”按钮"""
        self.button_2(False)
        if Button_image.press():
            self.object_point = 2
            self.n, self.skite = 0, 8

    def press_3(self):
        """ 点击“其他物品的物品栏”按钮"""
        self.button_3(False)
        if Button_image.press():
            self.object_point = 1
            self.n, self.skite = 0, 8

    def press_4(self):
        """ 点击“所有物品的物品栏”按钮"""
        self.button_4(False)
        if Button_image.press():
            self.object_point = 4
            self.n, self.skite = 0, 8

class Communication(object):
    """ 定义一个聊天栏"""
    def __init__(self):
        """ 定义初始化方法"""
        self.compen = False     # 是否打开聊天栏
        self.get_text = []      # 聊天回复的数据
        self.alpha = []         # 文字透明度（渐进）
        self.keep_time = []     # 透明时长（渐进）
        self.screen_text_color = []     # 文字颜色
        self.order_data = []    # 聊天发送的数据
        self.information = []   # 历史聊天回复记录
        self.copy_obj = {}  # 区块复制的物体坐标
        self.copy_out = {}  # 区域复制的物体id
        self.screen_copy, self.screen_glue = {}, {}   # 显示区块的范围
        # 指令集
        self.order_all = {
            '/tp @a': '已将自己传送至 x, y = ( , )', '/put id=': '已放置坐标为 x, y = ( , ); 长 宽 的id为 的物品',
            '/fill id=': '已填充坐标为 x, y = ( , ); 长 宽 的id为 的物品', '/give @a id=': '已将id为 的物品给予了玩家',
            '/copy name=': '已复制 x1, y1 = ( , ) 到 x2, y2 = ( , ) 区域为', '/glue name=': '已粘贴 x, y = ( , ) 区域为',
            '/list copy': '已复制的区块所有变量：', '/del copy name=': '已取消复制的区块为变量：',
            '/del copy': '已取消复制的所有区块', '/time': '世界当前时间已设为', '/time.speed': '世界时间流逝速度已更新为 次/帧',
            '/scale.z': '当前缩放比例z:'
        }

    def open(self, event):
        """ 打开聊天栏"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_t:  # 当按下"T"
                self.con_if_()
            elif event.key == pygame.K_RETURN:  # 当按下“回车”键时
                self.con_if__()

    def con_if__(self):
        """ 判断聊天栏是否关闭"""
        if self.compen:
            Button_image.click_music()
            self.compen = False
            InputBox.input_open[1] = False
            InputBox.text[1][0] = ''
            Get_into_world.kill_block_open = True
            Get_into_world.place_block_open = True
            Get_into_world.key_block_open = True
            Get_into_world.visibility_open = True
            Get_into_world.move_coordinate_system_open = True
            Get_into_world.mouse_end_world_open = True
            Load_call_world.block_throw_open = True
            Object_paper.press_0_open = True
            Load_call_world.convenience_open = True

    def con_if_(self):
        """ 判断聊天栏是否打开"""
        if not self.compen:
            Button_image.click_music()
            self.compen = True
            Get_into_world.kill_block_open = False
            Get_into_world.place_block_open = False
            Get_into_world.key_block_open = False
            Get_into_world.visibility_open = False
            Get_into_world.move_coordinate_system_open = False
            Get_into_world.mouse_end_world_open = False
            Load_call_world.block_throw_open = False
            Object_paper.press_0_open = False
            Load_call_world.convenience_open = False

    def opened(self):
        """ 聊天栏打开后"""
        if self.compen:
            shade_bg(0, (0, 0, 0, 150))
            self.input_order()
            self.ordered_history()

    def input_order(self):
        """ 定义命令输入框"""
        FONT_XY.render_to(
            screen, (10, HIGHLY-150), "输入指令：", fgcolor=(0, 0, 128), size=30
        )
        InputBox.NUMBER = 1
        InputBox.INPUT_SIZE = (WIDTH-200, 30)
        InputBox.INPUT_XY = (150, HIGHLY-150)
        InputBox.INPUT_COLOR_INSIDE = (32, 32, 32)
        InputBox.INPUT_COLOR_OUTSIDE = (64, 64, 64)
        InputBox.INPUT_SIZE_INSIDE = 5
        InputBox.INPUT_SIZE_OUTSIDE = 3
        InputBox.INPUT_COLOR_BG_IF_LIST = [False]
        InputBox.POINT_COLOR = (64, 64, 64)
        InputBox.POINT_SIZE = 5
        InputBox.POINT_KIND_IF = True
        InputBox.TEXT_COLOR = (200, 200, 200)
        InputBox.start()
        InputBox.input_open[1] = True
        InputBox.point_open[1] = True

    def finish_order_key(self, event):
        """ 按钮回调事件"""
        InputBox.NUMBER = 1
        if event.type == pygame.KEYDOWN:
            if len(InputBox.input_open)-1 >= InputBox.NUMBER:
                if InputBox.input_open[InputBox.NUMBER]:
                    if event.key == pygame.K_RETURN:  # 当按下“回车”键时
                        InputBox.text[InputBox.input_open.index(True)][1] = \
                            InputBox.text[InputBox.input_open.index(True)][0]
                        InputBox.text[InputBox.input_open.index(True)][0] = ''
                        self.order_data.append(InputBox.text[InputBox.input_open.index(True)][1])
                        self.alpha.append(255)
                        self.keep_time.append(1)
                        self.compare_order()

    def screen_out_order(self):
        """ 执行命令提示"""
        for i in range(len(self.get_text)):
            try:
                ca, cb, cc = self.screen_text_color[i-len(self.get_text)]
                FONT_XY.render_to(
                    screen, (0, 100 + 20*i), '>>> '+self.get_text[i], fgcolor=(ca, cb, cc, self.alpha[i]), size=20
                )
                if self.alpha[i] == 0:
                    del self.get_text[i]
                    del self.alpha[i]
                    del self.keep_time[i]
                else:
                    if self.keep_time[i]%120 == 0:
                        self.alpha[i] -= 1
                    else:
                        self.keep_time[i] += 1
            except:
                pass

    def ordered_history(self):
        """ 聊天历史栏"""
        for i in range(len(self.information)):
            ca, cb, cc = self.screen_text_color[i]
            FONT_XY.render_to(
                screen, (30, 50 + 25*i), '>>> ' + self.information[i], fgcolor=(ca, cb, cc), size=25
            )
        if len(self.information) >= 20:
            del self.information[0]
            del self.screen_text_color[0]

    def button_0(self, inherit):
        """ 定义“清空聊天栏”按钮"""
        Button_font.NMAE_XY = (Start_interface.x/2-50, 20)
        Button_font.BUTTON_NAME = "清空聊天栏"
        Button_font.BUTTON_COLOR_F = (0, 200, 0)
        Button_font.BUTTON_COLOR_T = (0, 255, 0)
        if inherit:
            Button_font.button()

    def press_0(self):
        """ 点击“清空聊天栏”按钮"""
        self.button_0(False)
        if Button_font.press():
            del self.information[:]
            del self.screen_text_color[:]

    def compare_order(self):
        """ 匹配指令"""
        if not self.order_data:
            return
        try:
            if self.order_data[-1][0] == '/':
                try:
                    for order, text in self.order_all.items():
                        if order == self.order_data[-1].split(' ')[0] + ' ' + \
                                self.order_data[-1].split(' ')[1] and \
                                self.order_data[-1].split(' ')[0] == '/tp':
                            self.pip_send(text)
                        elif order == self.order_data[-1].split(' ')[0] + ' ' + \
                                self.order_data[-1].split(' ')[-1][:3] and \
                                self.order_data[-1].split(' ')[0] == '/put':
                            self.pip_put(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/fill':
                            if order.split(' ')[1] == self.order_data[-1].split(' ')[-1][:3]:
                                self.pip_fill_1(text)
                            else:
                                self.pip_fill_0(text)
                        elif order == self.order_data[-1].split(' ')[0] + ' ' + \
                                self.order_data[-1].split(' ')[1] + ' ' + \
                                self.order_data[-1].split(' ')[-1][:3] and \
                                self.order_data[-1].split(' ')[0] == '/give':
                            self.pip_give(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/copy':
                            self.pip_copy(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/glue':
                            self.pip_glue(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/del':
                            if order.split(' ')[1] == self.order_data[-1].split(' ')[1] and \
                                self.order_data[-1].split(' ')[1] == 'copy' and \
                                order.split(' ')[2] == self.order_data[-1].split(' ')[-1][:5]:
                                self.pip_del_0(text)
                            elif order.split(' ')[1] == self.order_data[-1].split(' ')[1] and \
                                self.order_data[-1].split(' ')[1] == 'copy':
                                self.pip_del_1(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/list':
                            if order.split(' ')[1] == self.order_data[-1].split(' ')[1] and \
                                self.order_data[-1].split(' ')[1] == 'copy':
                                self.pip_list_0(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/time':
                            self.pip_time(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/time.speed':
                            self.pip_time_speed(text)
                        elif order.split(' ')[0] == self.order_data[-1].split(' ')[0] and \
                                self.order_data[-1].split(' ')[0] == '/scale.z':
                            self.pip_scale_z(text)
                except:
                    self.screen_text_color.append((255, 0, 0))
                    data = '“' + self.order_data[-1] + '”' + '不是有效的命令！'
                    self.get_text.append(data)
                    self.information.append(data)
            else:
                self.screen_text_color.append((0, 0, 0))
                self.get_text.append(self.order_data[-1])
                self.information.append(self.order_data[-1])
        except:
            pass
        Open_Character.compare_order(Communication, Get_into_world, Object_paper, WINDOW_SIZE)

    def pip_send(self, text):
        """ 匹配传送"""
        self.screen_text_color.append((0, 255, 0))
        ox, oy = self.order_data[-1].split(' ')[2], self.order_data[-1].split(' ')[3]
        data = text.split(' ')
        data = data[0] + data[1] + data[2] + data[3] + data[4] + ox + data[5] + oy + data[6]
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_tp(ox, oy)

    def pip_put(self, text):
        """ 匹配放置"""
        ox, oy, vx, vy, id = self.order_data[-1].split(' ')[1], \
                             self.order_data[-1].split(' ')[2], \
                             self.order_data[-1].split(' ')[3], \
                             self.order_data[-1].split(' ')[4], \
                             self.order_data[-1].split(' ')[-1][3:]
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + data[1] + data[2] + data[3] + data[4] + ox + data[5] + oy + data[6] + data[7] + vx + \
               data[8] + vy + data[9] + id + data[10]
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_put(ox, oy, vx, vy, id)

    def pip_fill_0(self, text):
        """ 匹配填充"""
        ox, oy, vx, vy = self.order_data[-1].split(' ')[1], \
                         self.order_data[-1].split(' ')[2], \
                         self.order_data[-1].split(' ')[3], \
                         self.order_data[-1].split(' ')[4]
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + data[1] + data[2] + data[3] + data[4] + ox + data[5] + oy + data[6] + data[7] + vx + \
               data[8] + vy + data[10]
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_fill(ox, oy, vx, vy)

    def pip_fill_1(self, text):
        """ 匹配填充（自定义）"""
        ox, oy, vx, vy, id = self.order_data[-1].split(' ')[1], \
                             self.order_data[-1].split(' ')[2], \
                             self.order_data[-1].split(' ')[3], \
                             self.order_data[-1].split(' ')[4], \
                             self.order_data[-1].split(' ')[-1][3:]
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + data[1] + data[2] + data[3] + data[4] + ox + data[5] + oy + data[6] + data[7] + vx + \
               data[8] + vy + data[9] + id + data[10]
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_fille(ox, oy, vx, vy, id)

    def pip_give(self, text):
        """ 匹配给予"""
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + self.order_data[-1].split(' ')[-1][3:] + data[1]
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_give(self.order_data[-1].split(' ')[-1][3:])

    def pip_copy(self, text):
        """ 匹配复制"""
        name, ox, oy, vx, vy = self.order_data[-1].split(' ')[1][5:], \
                               self.order_data[-1].split(' ')[2], \
                               self.order_data[-1].split(' ')[3], \
                               self.order_data[-1].split(' ')[4], \
                               self.order_data[-1].split(' ')[5]
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + data[1] + data[2] + data[3] + data[4] + ox + data[5] + oy + data[6] + data[7] + data[8] + \
               data[9] + data[10] + data[11] + vx + data[12] + vy + data[13] + data[14] + name
        self.get_text.append(data)
        self.information.append(data)
        self.screen_copy[name] = [ox, oy, vx, vy]
        Order_start.order_copy(name, ox, oy, vx, vy)

    def pip_glue(self, text):
        """ 匹配粘贴"""
        name, ox, oy = self.order_data[-1].split(' ')[1][5:], \
                       self.order_data[-1].split(' ')[2], \
                       self.order_data[-1].split(' ')[3]
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + data[1] + data[2] + data[3] + data[4] + ox + data[5] + oy + data[6] + data[7] + name
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_glue(name, ox, oy)

    def pip_list_0(self, text):
        """ 匹配已复制的区块所有变量"""
        self.screen_text_color.append((0, 255, 255))
        names = []
        for name, data in self.copy_obj.items():
            names.append(name)
        if names == []:
            data = text
        else:
            data = text + str(names)[1:-1]
        self.get_text.append(data)
        self.information.append(data)

    def pip_del_0(self, text):
        """ 匹配清除某个区域复制"""
        name = self.order_data[-1].split(' ')[-1][5:]
        self.screen_text_color.append((0, 255, 0))
        data = text.split(' ')
        data = data[0] + name
        self.get_text.append(data)
        self.information.append(data)
        Order_start.order_del_0(name)

    def pip_del_1(self, text):
        """ 匹配清除所有区域复制"""
        self.screen_text_color.append((0, 255, 0))
        self.get_text.append(text)
        self.information.append(text)
        Order_start.order_del_1()

    def pip_time(self, text):
        """ 匹配世界当前时间 """
        time_world, board = self.order_data[-1].split(' ')[1], \
                            self.order_data[-1].split(' ')[2]
        if 0 <= int(time_world) <= 230 and 0 <= int(board) <= 3:
            self.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + time_world
            self.get_text.append(data)
            Order_start.order_time(int(time_world), int(board))
        else:
            self.screen_text_color.append((255, 0, 0))
            data = '{时间,参数|0<=时间<=230,0<=参数<=3, 时间,参数∈Z} ' \
                   '参数(0-默认，1-静止，2-向左流逝，3-向右流逝) 请输入正确的指令格式！'
            self.get_text.append(data)
        self.information.append(data)

    def pip_time_speed(self, text):
        """ 匹配世界时间流逝速度"""
        time_speed = self.order_data[-1].split(' ')[1]
        if 1 <= int(time_speed) <= 999:
            self.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + time_speed + data[1]
            self.get_text.append(data)
            Order_start.order_time_speed(int(time_speed))
        else:
            self.screen_text_color.append((255, 0, 0))
            data = '1<=时间帧数<=999 请输入正确的指令格式！'
            self.get_text.append(data)
        self.information.append(data)

    def pip_scale_z(self, text):
        """ 匹配当前缩放比例z"""
        scale_z = self.order_data[-1].split(' ')[1]
        if 1 <= int(scale_z) <= 100:
            self.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + scale_z + 'x' + scale_z
            self.get_text.append(data)
            Order_start.order_scale_z(int(scale_z))
        else:
            self.screen_text_color.append((255, 0, 0))
            data = '1<=缩放比例<=100 请输入正确的指令格式！'
            self.get_text.append(data)
        self.information.append(data)

class Order_start(object):
    """ 定义一个执行指令类"""
    def order_tp(self, ox, oy):
        """ 传送自己"""
        zx, zy = int(ox) - Get_into_world.ctcs_x, int(oy) - Get_into_world.ctcs_y
        block_poe = []
        for block_xy in Get_into_world.block_list:
            block_poe.append([block_xy[0] - Get_into_world.image_size * zx,
                              block_xy[1] + Get_into_world.image_size * zy])
        Get_into_world.start_moving(block_poe)  # 调用后所有物体移动
        # 记录当前坐标
        Get_into_world.ctcs_x += zx
        Get_into_world.ctcs_y += zy

    def order_put(self, ox, oy, vx, vy, id):
        """ 放置物体"""
        self.order_fill(ox, oy, vx, vy)  # 先填充
        put_xy = []
        vx, vy = abs(int(vx) - float(ox))+1, abs(int(vy) - float(oy))+1
        for i in range(int(vy)):
            for j in range(int(vx)):
                put_xy.append(
                    ((float(ox) + j - Get_into_world.ctcs_x) * Get_into_world.image_size,
                     (float(oy) - i - Get_into_world.ctcs_y) * Get_into_world.image_size)
                )
        for put in put_xy:
            ox, oy = put
            # 添加一个物体坐标和物体名称到列表（后放置）
            Get_into_world.block_list.append([ox, -oy])
            Get_into_world.block_image.append(id)
            Get_into_world.block_music(id)  # 播放当前物体音效

    def order_fill(self, ox, oy, vx, vy):
        """ 填充物体"""
        put_xy = []
        vx, vy = abs(int(vx) - float(ox))+1, abs(int(vy) - float(oy))+1
        for i in range(int(vy)):
            for j in range(int(vx)):
                put_xy.append(
                    ((float(ox) + j - Get_into_world.ctcs_x) * Get_into_world.image_size,
                     (float(oy) - i - Get_into_world.ctcs_y) * Get_into_world.image_size)
                )
        kill = Get_into_world.kill_window()
        for put in put_xy:
            ox, oy = put
            screen.blit(kill, (ox, -oy))  # 填充一个物体
            # 删除列表中的一个方块坐标
            if [ox, -oy] in Get_into_world.block_list:
                block_image_zc = []  # 物体的位置
                # 循环填充一个位置的物体直到物体被填完
                while True:
                    try:
                        # 记录当前位置的物体id
                        block_image_zc = Get_into_world.block_image[Get_into_world.block_list.index([ox, -oy])]
                        del Get_into_world.block_image[Get_into_world.block_list.index([ox, -oy])]
                        Get_into_world.block_list.remove([ox, -oy])
                    except:
                        # 播放填充的物体音效
                        Get_into_world.block_music(block_image_zc)
                        break

    def order_fille(self, ox, oy, vx, vy, id):
        """ 填充某个物体"""
        put_xy = []
        vx, vy = abs(int(vx) - float(ox))+1, abs(int(vy) - float(oy))+1
        for i in range(int(vy)):
            for j in range(int(vx)):
                put_xy.append(
                    ((float(ox) + j - Get_into_world.ctcs_x) * Get_into_world.image_size,
                     (float(oy) - i - Get_into_world.ctcs_y) * Get_into_world.image_size)
                )
        kill = Get_into_world.kill_window()
        for put in put_xy:
            ox, oy = put
            if [ox, -oy] in Get_into_world.block_list:
                image_id = Get_into_world.block_image[Get_into_world.block_list.index([ox, -oy])]
                if image_id == id:
                    screen.blit(kill, (ox, -oy))  # 填充一个物体
                    # 删除列表中的一个物体坐标
                    if [ox, -oy] in Get_into_world.block_list:
                        block_image_zc = []  # 物体的位置
                        # 循环填充一个位置的物体直到物体被填完
                        while True:
                            try:
                                # 记录当前位置的物体id
                                block_image_zc = Get_into_world.block_image[Get_into_world.block_list.index([ox, -oy])]
                                del Get_into_world.block_image[Get_into_world.block_list.index([ox, -oy])]
                                Get_into_world.block_list.remove([ox, -oy])
                            except:
                                # 播放填充的物体音效
                                Get_into_world.block_music(block_image_zc)
                                break

    def order_give(self, id):
        """ 给予玩家物品"""
        Load_call_world.block_use[Get_into_world.image_number] = id

    def order_copy(self, name, ox, oy, vx, vy):
        """ 区块复制"""
        put_xy = []
        vx, vy = abs(int(vx) - float(ox))+1, abs(int(vy) - float(oy))+1
        for i in range(int(vy)):
            for j in range(int(vx)):
                put_xy.append(
                    ((float(ox) + j - Get_into_world.ctcs_x) * Get_into_world.image_size,
                     (float(oy) - i - Get_into_world.ctcs_y) * Get_into_world.image_size)
                )
        work_out, put_on = [], []
        for xy0 in put_xy:
            x, y = xy0
            if [x, -y] in Get_into_world.block_list:
                buff = Get_into_world.block_image[Get_into_world.block_list.index([x, -y])]
                if buff is not None:
                    work_out.append(buff)
                    put_on.append([x/Get_into_world.image_size, -y/Get_into_world.image_size])
        Communication.copy_out[name] = work_out
        Communication.copy_obj[name] = put_on

    def screen_copy(self):
        """ 显示复制区块的范围框"""
        for name, bag in Communication.screen_copy.items():
            ox, oy, vx, vy = bag
            vx, vy = (abs(int(vx) - float(ox))+1) * Get_into_world.image_size,\
                     (abs(int(vy) - float(oy))+1) * Get_into_world.image_size
            x, y = (float(ox) - Get_into_world.ctcs_x) * Get_into_world.image_size, \
                   (-float(oy) + Get_into_world.ctcs_y) * Get_into_world.image_size
            pygame.draw.rect(screen, (0, 255, 0), (x, y, vx, vy), 1)

    def order_glue(self, name, ox, oy):
        """ 区块粘贴"""
        ox, oy = float(ox), float(oy)
        work_out, put_on = [], []
        for find_name, id_list in Communication.copy_out.items():
            if find_name == name:
                for id in id_list:
                    work_out.append(id)
        for find_name, xy0_list in Communication.copy_obj.items():
            if find_name == name:
                for xy0 in xy0_list:
                    put_on.append(xy0)
        for id in work_out:
            Get_into_world.block_image.append(id)
            Get_into_world.block_music(id)  # 播放当前物体音效
        kill = Get_into_world.kill_window()
        minx, miny = min(put_on)
        for put in put_on:
            sx, sy = put
            sx, sy = (sx-minx+ox-Get_into_world.ctcs_x)*Get_into_world.image_size, \
                     (sy-miny-oy+Get_into_world.ctcs_y)*Get_into_world.image_size
            screen.blit(kill, (sx, sy))  # 填充一个物体
            # 删除列表中的一个物体坐标
            if [sx, sy] in Get_into_world.block_list:
                block_image_zc = []  # 物体的位置
                # 循环填充一个位置的物体直到物体被填完
                while True:
                    try:
                        # 记录当前位置的物体id
                        block_image_zc = Get_into_world.block_image[Get_into_world.block_list.index([sx, sy])]
                        del Get_into_world.block_image[Get_into_world.block_list.index([sx, sy])]
                        Get_into_world.block_list.remove([sx, sy])
                    except:
                        # 播放填充的物体音效
                        Get_into_world.block_music(block_image_zc)
                        break
            # 添加一个物体坐标和物体id到列表（后放置）
            Get_into_world.block_list.append([sx, sy])

    def screen_glue(self):
        """ 显示粘贴区块的范围框"""
        try:
            if InputBox.text[1][0].split(' ')[0] == '/glue':
                find_name, ux, uy = InputBox.text[1][0].split(' ')[1][5:], \
                                    InputBox.text[1][0].split(' ')[2], \
                                    InputBox.text[1][0].split(' ')[3]
                for name, bag in Communication.screen_copy.items():
                    if name == find_name:
                        ox, oy, vx, vy = bag
                        vx, vy = (abs(int(vx) - float(ox))+1) * Get_into_world.image_size, \
                                 (abs(int(vy) - float(oy))+1) * Get_into_world.image_size
                x, y = (float(ux) - Get_into_world.ctcs_x) * Get_into_world.image_size, \
                       (-float(uy) + Get_into_world.ctcs_y) * Get_into_world.image_size
                pygame.draw.rect(screen, (0, 255, 0), (x, y, vx, vy), 1)
        except:
            pass

    def order_del_0(self, name):
        """ 清除某个区域复制"""
        for names, data in Communication.copy_obj.items():
            if name == names:
                del Communication.copy_obj[name]
                del Communication.copy_out[name]
                del Communication.screen_copy[name]
                del Communication.screen_glue[name]

    def order_del_1(self):
        """ 清除所有区域复制"""
        Communication.copy_obj.clear()
        Communication.copy_out.clear()
        Communication.screen_copy.clear()
        Communication.screen_glue.clear()

    def order_time(self, time_world, board):
        """ 更改世界当前时间"""
        Get_into_world.board = board
        Get_into_world.day_time = time_world
        Get_into_world.ca, Get_into_world.cb, Get_into_world.cc = (time_world, time_world+25, time_world+25)
        if board == 2:
            Get_into_world.ue = 1
        elif board == 3:
            Get_into_world.ue = 0
        Get_into_world.daytime()

    def order_time_speed(self, time_speed):
        """ 更改当前世界时间流逝速度"""
        Get_into_world.time_speed = time_speed

    def order_scale_z(self, scale_z):
        """ 更改当前缩放比例"""
        scale_z = scale_z - Get_into_world.image_size
        if scale_z > 0:
            for i in range(scale_z):
                Get_into_world.image_size += 1
                block_poe = []
                for block_xy in Get_into_world.block_list:
                    block_poe.append([(block_xy[0] / (Get_into_world.image_size - 1)) * Get_into_world.image_size,
                                      (block_xy[1] / (Get_into_world.image_size - 1)) * Get_into_world.image_size])
                Get_into_world.start_moving(block_poe)
        elif scale_z < 0:
            for i in range(-scale_z):
                Get_into_world.image_size -= 1
                block_poe = []
                for block_xy in Get_into_world.block_list:
                    block_poe.append([(block_xy[0] / (Get_into_world.image_size + 1)) * Get_into_world.image_size,
                                      (block_xy[1] / (Get_into_world.image_size + 1)) * Get_into_world.image_size])
                Get_into_world.start_moving(block_poe)

class Set_game_window(object):
    """ 定义一个游戏设置类"""
    def __init__(self):
        self.pa0x, self.pa0y = (WIDTH/30, HIGHLY/20)    # 区域1的位置
        self.pa1x, self.pa1y = (WIDTH/30, HIGHLY/2.7)   # 区域2的位置
        self.pa2x, self.pa2y = (WIDTH/30+310, HIGHLY/2.7+30)   # 区域3的位置
        self.sound_bg = 100             # 背景音乐音量
        self.sound_click = 80           # 按钮音量
        self.sound_click_change = []    # 测试按钮音量
        self.sound_block = 50           # 物品音量
        self.sound_block_change = []    # 测试物品音量
        # 鼠标是否按下或弹起
        self.press_down_sb = False
        self.press_down_sc = False
        self.press_down_sl = False
        # 物品音效
        self.address_sound_block_file = []
        for i in Get_into_world.sound_effect:
            for j in i:
                self.address_sound_block_file.append(j)
        # 是否显示数据到输入框内
        self.sign_0 = True
        self.sign_1 = True
        # 文本字体颜色
        self.text_color_0 = (0, 0, 0)
        self.text_color_1 = (0, 0, 0)

        self.IMAGE_OFF_mouse, self.IMAGE_ON_mouse = 'checkbox_1', 'checkbox_2'
        self.open_mouse = True  # 是否隐藏鼠标指针

    def background(self):
        """ 设置背景"""
        insert_image('set_bg', WINDOW_SIZE, (0, 0))
        shade_bg(WINDOW_SIZE, (0, 0, 0, 64), (0, 0))

    def button_0(self, inherit):
        """ 定义“返回”按钮"""
        Button_font.FONT_SIZE = fx = 40
        Button_font.NMAE_XY = (30, Start_interface.y-fx-30)
        Button_font.BUTTON_NAME = "返回"
        Button_font.BUTTON_COLOR_F = (0, 200, 255)
        Button_font.BUTTON_COLOR_T = (0, 255, 255)
        Button_image.IMAGE_OFF = 'button_bg'
        Button_image.IMAGE_ON = 'button_oh'
        Button_image.IMAGE_SIZE_OFF = (110, 60)
        Button_image.IMAGE_SIZE_ON = (112, 62)
        Button_image.IMAGE_OFF_XY = (15, Start_interface.y-fx-44)
        Button_image.IMAGE_ON_XY = (14, Start_interface.y-fx-45)
        if inherit:
            Button_image.button()
            Button_font.button()

    def press_a(self):
        """ 点击“返回”按钮"""
        self.button_0(False)
        if Button_image.press():
            Start_interface.click_set = False
            self.back_event()

    def key(self):
        """ 键盘事件（快捷键）"""
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:  # 当按下“Esc”键
            Button_font.click_music()
            Start_interface.click_set = False   # 返回到主界面
            self.back_event()

    def back_event(self):
        """ 返回到主界面重置事件"""
        self.sign_0 = True
        self.sign_1 = True

    def area_0(self):
        """ 区域1"""
        surface = insert_image_change('demo_background', (505, 300))
        surface.set_alpha(128)
        screen.blit(surface, (self.pa0x, self.pa0y))
        for i in range(3):
            FONT_XY.render_to(screen, (self.pa0x+200+i, self.pa0y+10), "声音", fgcolor=(50, 50, 50), size=30)

        FONT_XY.render_to(screen, (self.pa0x+20, self.pa0y+60), "背景音乐", fgcolor=(0, 0, 0), size=20)
        FONT_XY.render_to(screen, (self.pa0x+20, self.pa0y+100), "按钮音量", fgcolor=(0, 0, 0), size=20)
        FONT_XY.render_to(screen, (self.pa0x+20, self.pa0y+140), "物品音量", fgcolor=(0, 0, 0), size=20)

        insert_image('smooth', (307, 5), (self.pa0x+115, self.pa0y+67))
        FONT_XY.render_to(screen, (self.pa0x+435, self.pa0y+60), str(self.sound_bg)+'%', fgcolor=(0, 0, 0), size=20)
        insert_image('smooth', (307, 5), (self.pa0x+115, self.pa0y+107))
        FONT_XY.render_to(screen, (self.pa0x+435, self.pa0y+100), str(self.sound_click)+'%', fgcolor=(0, 0, 0), size=20)
        insert_image('smooth', (307, 5), (self.pa0x+115, self.pa0y+147))
        FONT_XY.render_to(screen, (self.pa0x+435, self.pa0y+140), str(self.sound_block)+'%', fgcolor=(0, 0, 0), size=20)

        Button_image.IMAGE_OFF = 'smooth_point'
        Button_image.IMAGE_ON = 'smooth_point'
        Button_image.IMAGE_SIZE_OFF = (7, 15)
        Button_image.IMAGE_SIZE_ON = (7, 15)
        self.smooth_0(True)
        self.smooth_1(True)
        self.smooth_2(True)

    def smooth_0(self, inherit):
        """ 定义背景音乐的滑块"""
        Button_image.IMAGE_OFF_XY = (self.pa0x+115 + 3*self.sound_bg, self.pa0y+62)
        Button_image.IMAGE_ON_XY = (self.pa0x+115 + 3*self.sound_bg, self.pa0y+62)
        if inherit:
            Button_image.button()
        if self.press_down_sb:
            ax = self.pa0x+115
            aloud = round((x-ax)/3)
            if 0 <= aloud <= 100:
                self.sound_bg = aloud
        pygame.mixer.music.set_volume(self.sound_bg/100)

    def smooth_1(self, inherit):
        """ 定义按钮音量的滑块"""
        global MUSIC_BUTTON
        Button_image.IMAGE_OFF_XY = (self.pa0x+115 + 3*self.sound_click, self.pa0y+102)
        Button_image.IMAGE_ON_XY = (self.pa0x+115 + 3*self.sound_click, self.pa0y+102)
        if inherit:
            Button_image.button()
        if self.press_down_sc:
            ax = self.pa0x+115
            aloud = round((x-ax)/3)
            if 0 <= aloud <= 100:
                self.sound_click = aloud
                self.sound_click_change.append(self.sound_click)
                if len(self.sound_click_change) == 2:
                    if self.sound_click_change[0] != self.sound_click_change[1]:
                        del self.sound_click_change[:]
                        Button_image.click_music()
        if len(self.sound_click_change) > 2:
            del self.sound_click_change[1:]
        MUSIC_BUTTON = self.sound_click/100

    def smooth_2(self, inherit):
        """ 定义物品音量的滑块"""
        global MUSIC_BLOCK
        Button_image.IMAGE_OFF_XY = (self.pa0x+115 + 3*self.sound_block, self.pa0y+142)
        Button_image.IMAGE_ON_XY = (self.pa0x+115 + 3*self.sound_block, self.pa0y+142)
        if inherit:
            Button_image.button()
        if self.press_down_sl:
            ax = self.pa0x+115
            aloud = round((x-ax)/3)
            if 0 <= aloud <= 100:
                self.sound_block = aloud
                self.sound_block_change.append(self.sound_block)
                if len(self.sound_block_change) == 2:
                    if self.sound_block_change[0] != self.sound_block_change[1]:
                        del self.sound_block_change[:]
                        sound_file = random.choice(self.address_sound_block_file)
                        block_music = pygame.mixer.Sound(sound_file)
                        block_music.set_volume(MUSIC_BLOCK)
                        block_music.play()
        if len(self.sound_block_change) > 2:
            del self.sound_block_change[1:]
        MUSIC_BLOCK = self.sound_block/100

    def press_0(self):
        """ 点击“背景音乐”滑块"""
        self.smooth_0(False)
        if Button_image.press(0):
            self.press_down_sb = True

    def press_1(self):
        """ 点击“按钮音量”滑块"""
        self.smooth_1(False)
        if Button_image.press():
            self.press_down_sb = False
            self.press_down_sc = True

    def press_2(self):
        """ 点击“物品音量”滑块"""
        self.smooth_2(False)
        if Button_image.press(0):
            self.press_down_sc = False
            self.press_down_sl = True

    def area_1(self):
        """ 区域2"""
        surface = insert_image_change('demo_background', (300, 220))
        surface.set_alpha(128)
        screen.blit(surface, (self.pa1x, self.pa1y))
        for i in range(3):
            FONT_XY.render_to(screen, (self.pa1x+100+i, self.pa1y+10), "摄像机", fgcolor=(50, 50, 50), size=30)

        FONT_XY.render_to(screen, (self.pa1x+20, self.pa1y+60), "正常移动速度", fgcolor=(0, 0, 0), size=20)
        FONT_XY.render_to(screen, (self.pa1x+20, self.pa1y+100), "最快移动速度", fgcolor=(0, 0, 0), size=20)

        self.input_0()
        self.input_1()

    def input_0(self):
        """ 定义“正常移动速度”输入框"""
        InputBox.NUMBER = 2
        InputBox.INPUT_SIZE = (40, 20)
        InputBox.INPUT_XY = (self.pa1x+145, self.pa1y+60)
        InputBox.INPUT_COLOR_INSIDE = (64, 64, 64)
        InputBox.INPUT_COLOR_OUTSIDE = (128, 128, 128)
        InputBox.INPUT_SIZE_INSIDE = 1
        InputBox.INPUT_SIZE_OUTSIDE = 1
        InputBox.INPUT_COLOR_BG_IF_LIST = [True, (200, 200, 200), False]
        InputBox.POINT_COLOR = (64, 64, 64)
        InputBox.POINT_SIZE = 1
        InputBox.POINT_KIND_IF = False
        InputBox.TEXT_COLOR = self.text_color_0
        InputBox.start()
        if self.sign_0:
            self.sign_0 = False
            InputBox.text[InputBox.NUMBER][0] = str(Get_into_world.SPEED_M)
        try:
            if int(InputBox.text[2][0]) < int(InputBox.text[3][0]):
                self.text_color_0 = (0, 0, 0)
                Get_into_world.SPEED_M = int(InputBox.text[InputBox.NUMBER][0])
            else:
                self.text_color_0 = (255, 0, 0)
        except:
            self.text_color_0 = (255, 0, 0)

    def input_1(self):
        """ 定义“最快移动速度”输入框"""
        InputBox.NUMBER = 3
        InputBox.INPUT_SIZE = (40, 20)
        InputBox.INPUT_XY = (self.pa1x+145, self.pa1y+100)
        InputBox.INPUT_COLOR_INSIDE = (64, 64, 64)
        InputBox.INPUT_COLOR_OUTSIDE = (128, 128, 128)
        InputBox.INPUT_SIZE_INSIDE = 1
        InputBox.INPUT_SIZE_OUTSIDE = 1
        InputBox.INPUT_COLOR_BG_IF_LIST = [True, (200, 200, 200), False]
        InputBox.POINT_COLOR = (64, 64, 64)
        InputBox.POINT_SIZE = 1
        InputBox.POINT_KIND_IF = False
        InputBox.TEXT_COLOR = self.text_color_1
        InputBox.start()
        if self.sign_1:
            self.sign_1 = False
            InputBox.text[InputBox.NUMBER][0] = str(Get_into_world.SPEED_L)
        try:
            if int(InputBox.text[2][0]) < int(InputBox.text[3][0]):
                self.text_color_1 = (0, 0, 0)
                Get_into_world.SPEED_L = int(InputBox.text[InputBox.NUMBER][0])
            else:
                self.text_color_1 = (255, 0, 0)
        except:
            self.text_color_1 = (255, 0, 0)

    def press_key_0(self, event):
        """ 按钮回调事件“正常移动速度”"""
        InputBox.NUMBER = 2
        if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
            if event.button == 1:  # 左键
                InputBox.press_frame_event()

    def press_key_1(self, event):
        """ 按钮回调事件“最快移动速度”"""
        InputBox.NUMBER = 3
        if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
            if event.button == 1:  # 左键
                InputBox.press_frame_event()

    def area_2(self):
        """ 区域3"""
        surface = insert_image_change('demo_background', (180, 100))
        surface.set_alpha(128)
        screen.blit(surface, (self.pa2x, self.pa2y))
        FONT_XY.render_to(screen, (self.pa2x+10, self.pa2y+10), "进入游戏时隐藏鼠标", fgcolor=(0, 0, 0), size=17)
        self.check_0(True)
        if self.open_mouse:
            self.IMAGE_OFF_mouse, self.IMAGE_ON_mouse = 'checkbox_1', 'checkbox_2'
        else:
            self.IMAGE_OFF_mouse, self.IMAGE_ON_mouse = 'checkbox_3', 'checkbox_4'

    def check_0(self, inherit):
        """ 定义“鼠标是否隐藏”选框"""
        Button_image.IMAGE_OFF = self.IMAGE_OFF_mouse
        Button_image.IMAGE_ON = self.IMAGE_ON_mouse
        Button_image.IMAGE_SIZE_OFF = (20, 20)
        Button_image.IMAGE_SIZE_ON = (20, 20)
        Button_image.IMAGE_OFF_XY = (self.pa2x+75, self.pa2y+35)
        Button_image.IMAGE_ON_XY = (self.pa2x+75, self.pa2y+35)
        if inherit:
            Button_image.button()

    def press_3(self):
        """ 点击“鼠标是否隐藏”选框"""
        self.check_0(False)
        if Button_image.press():
            if not self.open_mouse:
                self.open_mouse = True
                self.IMAGE_OFF_mouse, self.IMAGE_ON_mouse = 'checkbox_1', 'checkbox_2'
            else:
                self.open_mouse = False
                self.IMAGE_OFF_mouse, self.IMAGE_ON_mouse = 'checkbox_3', 'checkbox_4'

    def area_3(self):
        """ 区域4"""
        surface_0 = insert_image_change('demo_background',
                                        (round(WIDTH - WIDTH / 30) - 570, round(HIGHLY - HIGHLY / 20) + 320))
        surface_1 = insert_image_change('demo_background',
                                        (550, round(HIGHLY - HIGHLY / 20) - 420))
        surface_0.set_alpha(128)
        screen.blit(surface_0, (WIDTH / 30 + 550, HIGHLY / 20))
        surface_1.set_alpha(128)
        screen.blit(surface_1, (WIDTH / 30, HIGHLY / 2.7 + 170))
        n, text = 0, "敬请期待"
        for i in text:
            FONT_XY.render_to(screen,
                              (WIDTH / 30 + 500 + (round(WIDTH - WIDTH / 30) - 570) / 2, HIGHLY / 20 + 70 + 130 * n),
                              i, fgcolor=(80, 80, 80), size=100)
            n += 1
        FONT_XY.render_to(screen, (WIDTH / 30 + 120, HIGHLY / 2.7 + 210), text, fgcolor=(80, 80, 80), size=70)

    def read_cfg(self):
        """ 读取配置数据"""
        with open('set.cfg', 'r') as cfg:
            str_cfg = cfg.read()
            if str_cfg != '':
                list_cfg = ast.literal_eval(str_cfg)
                self.sound_bg = list_cfg[1][0]
                self.sound_click = list_cfg[1][1]
                self.sound_block = list_cfg[1][2]
                Get_into_world.SPEED_M = list_cfg[2][0]
                Get_into_world.SPEED_L = list_cfg[2][1]
                self.open_mouse = list_cfg[3]

    def write_cfg(self):
        """ 保存配置数据"""
        global TICK_TIME
        cfg = open('set.cfg', 'w')
        cfg.write('%s' % [
            WINDOW_SIZE, [self.sound_bg, self.sound_click, self.sound_block],
            [Get_into_world.SPEED_M, Get_into_world.SPEED_L], self.open_mouse, TICK_TIME
        ])
        cfg.close()

    def window_start(self):
        """ 设置界面起始执行位置"""
        self.background()
        self.write_cfg()
        self.area_0()
        self.area_1()
        self.area_2()
        self.area_3()
        self.button_0(True)
        self.key()


def insert_image(name_image, size_image, xy_image):
    """ 定义加载图片的函数"""
    for block, zlock in images.items():
        if block == name_image:
            road = pygame.transform.scale(zlock, size_image)
            screen.blit(road.convert_alpha(), xy_image)
            return road

def insert_image_area(name_image, area_image, size_image, xy_image):
    """ 定义加载图片的函数（选择一个区域加载）"""
    for block, zlock in images.items():
        if block == name_image:
            screen.blit(
                pygame.transform.smoothscale(
                    zlock.subsurface(area_image), size_image
                ).convert(), xy_image
            )

def insert_image_change(name_image, size_image):
    """ 定义加载图片的函数（自定义）"""
    for block, zlock in images.items():
        if block == name_image:
            return pygame.transform.scale(zlock, size_image).convert_alpha()

def shade_bg(size=0, clear=(0, 0, 0, 128), place=(0, 0)):
    """ 定义阴影背景效果"""
    if size == 0:
        size = screen.get_size()
    transparent_rect = pygame.Surface(size, pygame.SRCALPHA)
    transparent_rect.fill(clear)
    screen.blit(transparent_rect, place)

def work_image():
    """ 加载物品到内存"""
    images = {}
    dic_list = []

    try:
        with open('block\\building\\dic_block_image.dict', 'r') as building:
            str_building = building.read()
            with open('block\\circuit\\dic_block_image.dict', 'r') as circuit:
                str_circuit = circuit.read()
                with open('block\\other\\dic_block_image.dict', 'r') as other:
                    str_other = other.read()
                    with open('bg\\dic_bg.dict', 'r') as bg:
                        str_bg = bg.read()
                        if str_bg != '':
                            disc_imagbg = ast.literal_eval(str_bg)
                            dic_list.append(disc_imagbg)
                    if str_other != '':
                        disbuilding_2 = ast.literal_eval(str_other)
                        dic_list.append(disbuilding_2)
                if str_circuit != '':
                    disbuilding_1 = ast.literal_eval(str_circuit)
                    dic_list.append(disbuilding_1)
            if str_building != '':
                disbuilding_0 = ast.literal_eval(str_building)
                dic_list.append(disbuilding_0)
        dic_list.append(dict(
            list(dic_list[1].items()) + list(dic_list[2].items()) + list(dic_list[3].items())
        ))

        for nbg, abg in disc_imagbg.items():
            images[abg] = pygame.image.load('bg\\' + nbg)
        for nblock, ablock in disbuilding_0.items():
            images[ablock[0]] = pygame.image.load('block\\building\\' + nblock)
        for nblock, ablock in disbuilding_1.items():
            images[ablock[0]] = pygame.image.load('block\\circuit\\' + nblock)
        for nblock, ablock in disbuilding_2.items():
            images[ablock[0]] = pygame.image.load('block\\other\\' + nblock)
        return images, dic_list
    except Exception as e:
        print(f"资源加载失败: {e}")
        return {}, []

def button_interface():
    """ 主界面按钮点击"""
    if Start_interface.click_set:
        Set_game_window.press_down_sb = False
        Set_game_window.press_down_sc = False
        Set_game_window.press_down_sl = False
        Set_game_window.press_a()
    else:
        if not Start_interface.click:
            Start_interface.press_1()
            Start_interface.press_2()
            Start_interface.press_3()
        else:
            Selection_interface.press_1()
            Selection_interface.press_2()
            Selection_interface.press_3()
            Load_file.mouse_click()

def main_interface_map():
    """ 主界面地图"""
    if Start_interface.click_set:
        Set_game_window.window_start()
    else:
        if not Start_interface.click:
            Start_interface.bg_image()
            Start_interface.button_1(True)
            Start_interface.button_2(True)
            Start_interface.button_3(True)
        else:
            Selection_interface.bg_image()
            Selection_interface.key()
            Selection_interface.button_1(True)
            Selection_interface.button_2(True)
            Selection_interface.button_3(True)
            Load_file.all()
            Load_file.load()

def game_interface_map():
    """ 进入世界地图"""
    if Get_into_world.board != 1:
        Get_into_world.daytime()
    if Get_into_world.key_block_open:
        Get_into_world.key_block()
    if Get_into_world.move_coordinate_system_open and not Open_Character.character_open:
        Get_into_world.move_coordinate_system()
    Get_into_world.screen_repeat()
    Load_call_world.block_use_key()
    if Load_call_world.table_open:
        Load_call_world.table()
    if Open_Character.character_open:
        Open_Character.get(Get_into_world, screen, WINDOW_SIZE,
                           Load_call_world, Load_file, Communication, Object_paper, FONT_XY, CA, CB, CC)
    if Load_call_world.read_font_open:
        Load_call_world.read_font()
        Load_call_world.button_1(True)
    if Load_call_world.select_box_open:
        Load_call_world.select_box()
    Get_into_world.preservation_world_data()
    Get_into_world.implement_end_world()
    if Get_into_world.visibility_open and not Open_Character.character_open:
        Get_into_world.visibility()
    Order_start.screen_copy()
    Order_start.screen_glue()
    Communication.screen_out_order()
    if Load_call_world.event_repeat_open:
        Load_call_world.event_repeat()
        Object_paper.button_0(True)
    Object_paper.opened()
    if Load_call_world.block_throw_open:
        Load_call_world.block_throw()
    Communication.opened()
    if Communication.compen:
        Communication.button_0(True)

def event_with_deal(event):
    """ 事件处理"""
    if InputBox.input_open != []:
        Object_paper.find_block_key(event)
        Communication.finish_order_key(event)
    if Object_paper.press_0_open:
        Object_paper.open(event)
    Get_into_world.key_end_world(event)
    InputBox.words(event)
    if not Object_paper.openife:
        Communication.open(event)
    if Load_call_world.convenience_open:
        Load_call_world.convenience(event)

def mouse_demo_left():
    """ 鼠标左键按下"""
    if Start_interface.click_set:
        Set_game_window.press_0()
        Set_game_window.press_1()
        Set_game_window.press_2()
        Set_game_window.press_3()

def event_demo(event):
    """ 事件处理"""
    if Start_interface.click_set:
        InputBox.words(event)
        Set_game_window.press_key_0(event)
        Set_game_window.press_key_1(event)

def mouse_left():
    """ 鼠标左键按下（进入世界地图）"""
    if Get_into_world.kill_block_open:
        Get_into_world.kill_block()
    if Get_into_world.mouse_end_world_open:
        Get_into_world.mouse_end_world()
    if Object_paper.press_0_open:
        Object_paper.press_0()
    if Communication.compen:
        Communication.press_0()

def kill_window(CD=255):
    """ 定义清空屏幕"""
    kill_all = pygame.Surface((WIDTH, HIGHLY), flags=pygame.SRCALPHA)
    pygame.Surface.convert(kill_all)
    kill_all.fill(pygame.Color(CA, CB, CC, CD))
    return kill_all

def game_map():
    """ 加载基础项"""
    pygame.display.set_icon(pygame.image.load('MC_ico.ico'))  # 窗口图标
    FONT_XY = pygame.freetype.Font('fonts//simsun.ttc')  # 导入字体
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)  # 启用硬件加速
    screen.fill(COLOR)
    clock = pygame.time.Clock()
    return FONT_XY, screen, clock

class App(object):
    """ 程序入口"""
    def start_side(self):
        """ 进入开始界面"""
        global x, y, event
        pygame.mouse.set_visible(True) # 打开鼠标指针
        while True:
            x, y = pygame.mouse.get_pos()  # 获取鼠标位置
            """ 轮询事件"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
                    if event.button == 1:  # 左键（当鼠标按下时）
                        mouse_demo_left()
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标事件
                    if event.button == 1:  # 左键（当鼠标弹起时）
                        button_interface()
                    else:
                        Load_file.mouse_roll()
                event_demo(event)
            Start_interface.bg_music()  # 加载背景音乐
            main_interface_map()  # 加载主界面

            if Load_file.roll:
                break
            pygame.display.flip()  # 更新全部显示

    def game_side(self):
        """ 进入游戏界面"""
        global x, y, event, TICK_TIME
        pygame.mouse.set_visible(Set_game_window.open_mouse)    # 是否隐藏鼠标指针
        while True:
            clock.tick(TICK_TIME)   # 每秒刷新帧率
            x, y = pygame.mouse.get_pos()  # 获取鼠标位置
            # 轮询事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
                    if event.button == 1:  # 左键
                        mouse_left()
                    elif event.button == 3:  # 右键
                        if Get_into_world.place_block_open:
                            Get_into_world.place_block()
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标滚动
                    if event.button == 4:  # 向上滚动
                        if not Object_paper.openife:
                            Get_into_world.image_number -= 1  # 上一个方块（方块地址减一）
                    elif event.button == 5:  # 向下滚动
                        if not Object_paper.openife:
                            Get_into_world.image_number += 1  # 下一个方块（方块地址加一）
                event_with_deal(event)
            Start_interface.bg_music()  # 加载背景音乐
            game_interface_map()  # 加载主界面

            if not Load_file.roll:
                break
            pygame.display.flip()  # 更新全部显示

    def main(self):
        """ 主循环"""
        while True:
            self.start_side()
            self.game_side()

def load_game_assets():
    """ 加载游戏资源"""
    pygame.display.set_caption('游戏加载中...')  # 窗口标题
    logo1, logo2 = pygame.image.load('bg\\logo1.png'), \
                   pygame.image.load('bg\\logo2.png')
    for i in range(25):
        screen.blit(pygame.transform.scale(logo1, WINDOW_SIZE), (0, 0))
        kill_all = kill_window(255-i*10)
        screen.blit(kill_all, (0, 0))
        pygame.display.flip()
    time.sleep(1)
    global COLOR, CA, CB, CC
    COLOR = CA, CB, CC = (255, 255, 255)
    for i in range(51):
        screen.blit(pygame.transform.scale(logo2, WINDOW_SIZE), (0, 0))
        kill_all = kill_window(255-i*5)
        screen.blit(kill_all, (0, 0))
        pygame.display.flip()
    FONT_XY.render_to(
        screen, (WIDTH/2-22*6.5, HIGHLY-150), "游戏加载中...", fgcolor=(255, 255, 255), size=40
    )
    pygame.display.flip()
    time.sleep(2)


""" 初始化世界"""
pygame.init()   # 初始化pygame
pygame.mixer.init() # 初始化音乐模块
# 窗口大小
WINDOW_SIZE = WIDTH, HIGHLY = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
TICK_TIME = 60
with open('set.cfg', 'r') as cfg:
    str_cfg = cfg.read()
    if str_cfg != '':
        list_cfg = ast.literal_eval(str_cfg)
        if list_cfg[0] != (0, 0):
            WINDOW_SIZE = WIDTH, HIGHLY = list_cfg[0]
        TICK_TIME = list_cfg[4]
COLOR = CA, CB, CC = (0, 0, 0)    # 背景颜色
FONT_XY, screen, clock = game_map()
load_game_assets()
kill_all = kill_window()
images, dic_list = work_image()
App = App()
x, y = (None, None)

""" 实例化Game"""
Start_interface = Start_interface()
Button_font = Button_font()
Button_image = Button_image()
InputBox = InputBox()
Selection_interface = Selection_interface()
Load_file = Load_file()
Get_into_world = Get_into_world()
Load_call_world = Load_call_world()
Message = Message()
Object_paper = Object_paper()
Communication = Communication()
Order_start = Order_start()
Set_game_window = Set_game_window()

Open_Character = Open_Character()

Set_game_window.read_cfg()
# 1.背景音乐音量 2.按钮音量 3.物品音量——[{1=开}, {0=关}, <音量(0~1)>]
MUSIC_MAIN, MUSIC_BUTTON, MUSIC_BLOCK = Set_game_window.sound_bg * 0.01, \
                                        Set_game_window.sound_click * 0.01, \
                                        Set_game_window.sound_block * 0.01

pygame.display.set_caption('Minecraft 2D')


if __name__ == '__main__':
    App.main()

