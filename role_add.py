"""
Hello Python
我的世界2D更新文件名：主人物控制
开始更新时间：2024-08-18 21:18
"""

import pygame, ast


class Get_data:
    """ 定义get数据的类"""
    def __init__(self):
        self.character_open = False # 是否召唤人物
        # 数据初始化
        self.screen = None
        self.window_size = None
        self.image_size = 0
        self.Get_into_world = None
        self.Load_call_world = None
        self.Communication = None
        self.Object_paper = None
        self.Load_file = None
        self.FONT_XY = None
        self.CA, self.CB, self.CC = None, None, None
        image_character = 'characters\\character.png'
        image_character_ce = 'characters\\close_eye\\character.png'

        # 人物初始化
        self.character = pygame.image.load(image_character)
        self.character_ce = pygame.image.load(image_character_ce)
        self.close_eye = 0                      # 眨眼时频
        self.cr_size = None                     # 人物大小
        self.player_pos = [0, 0]                # 人物位置
        self.speed_jump = self.image_size/2     # 跳跃高度
        self.jump_direction = [False, False, False, False]
        self.gravity = 0.5          # 重力加速度
        self.jump_force = -12       # 跳跃初速度
        self.move_speed_m = 8       # 行走初速度
        self.move_speed_l = 16      # 奔跑初速度

        # 初始化摄像机跟踪人物
        self.window_track_pos = [False, False, False, False]    # 跟踪方向
        self.move_form, self.move_fly = 0, 0    # 跟踪格数

        # 人物指令
        self.order_all = {
            '/character': '人物已', '/character.g': '已设置人物重力加速度为', '/character.j': '已设置人物跳跃初速度为',
            '/character.m': '已设置正常行走速度为', '/character.l': '已设置反常行走速度为'
        }

    def get(self, Get_into_world, screen, WINDOW_SIZE,
            Load_call_world, Load_file, Communication, Object_paper, FONT_XY, CA, CB, CC):
        # 获取数据
        self.screen = screen
        self.window_size = WINDOW_SIZE
        self.Get_into_world = Get_into_world
        self.image_size = Get_into_world.image_size
        self.Load_call_world = Load_call_world
        self.Load_file = Load_file
        self.Communication = Communication
        self.Object_paper = Object_paper
        self.FONT_XY = FONT_XY
        self.CA, self.CB, self.CC = CA, CB, CC

        self.start()

    def exit_world(self):
        """ 退出世界时初始化设置"""
        self.character_open = False
        self.window_track_pos = [False, False, False, False]
        self.move_form, self.move_fly = 0, 0

    def read_dat(self, Load_file, n):
        """ 读取人物数据"""
        self.Load_file = Load_file
        try:
            with open(self.Load_file.world_name[n][0] + '\\character.dat', 'r') as data:
                str_data = data.read()
                if str_data != '':
                    list_data = ast.literal_eval(str_data)
                    self.character_open = list_data[0]
                    self.player_pos = list_data[1]
                    self.gravity = list_data[2][0]
                    self.jump_force = list_data[2][1]
                    self.move_speed_m = list_data[2][2]
                    self.move_speed_l = list_data[2][3]
        except (FileNotFoundError, IndexError, SyntaxError):
            # 文件不存在或数据错误时初始化默认值
            self.character_open = False
            self.player_pos = [self.window_size[0] / 2, self.window_size[1] / 2]

    def write_dat(self, n):
        """ 保存人物数据"""
        data = open(self.Load_file.world_name[n][0] + '\\character.dat', 'w')
        data.write('%s' % [
            self.character_open, self.player_pos,
            [self.gravity, self.jump_force, self.move_speed_m, self.move_speed_l]
        ])
        data.close()

class Character(Get_data):
    """ 定义一个人物类"""
    def __init__(self):
        super().__init__()  # 确保调用父类初始化
        self.velocity_y = 0  # 垂直速度
        self.on_ground = False  # 是否在地面

    def block_xy(self):
        """ 碰撞检测"""
        """
        two = False
        n = 0
        for rect in self.Get_into_world.img_size:
            rect.center = self.Get_into_world.img_xy[n]

            self.cr_size.center = self.player_pos
            if rect.colliderect(self.cr_size):
                two = True
            n += 1

        if two:
            self.speed_jump = self.image_size/2
        else:
            wx, wy = self.window_size
            if 0 <= self.player_pos[0] <= wx and 0 <= self.player_pos[1] <= wy:
                self.player_pos[1] += self.image_size/5
        """
        #print(self.Get_into_world.img_xy)
        #print(self.player_pos)

        '''
        leftup_x, leftup_y = self.player_pos[0], self.player_pos[1]
        leftdown_x, leftdown_y  = self.player_pos[0], self.player_pos[1] + self.image_size
        rightup_x, rightup_y = self.player_pos[0] + self.image_size, self.player_pos[1]
        rightdown_x, rightdown_y = self.player_pos[0] + self.image_size, self.player_pos[1] + self.image_size

        for blay in self.Get_into_world.img_xy:
            if blay[0] <= leftdown_x <= blay[0] + self.image_size or blay[0] <= rightdown_x <= blay[0] + self.image_size:
                if blay[1] <= leftdown_y <= blay[1] + self.image_size or blay[1] <= rightdown_y <= blay[1] + self.image_size:
                    #self.player_pos[1] -= self.image_size/8
                    self.player_pos[1] = blay[1] - self.image_size+1
                    self.jump_direction[0] = True
            if blay[0] <= leftup_x <= blay[0] + self.image_size or blay[0] <= rightup_x <= blay[0] + self.image_size:
                if blay[1] <= leftup_y <= blay[1] + self.image_size or blay[1] <= rightup_y <= blay[1] + self.image_size:
                    self.player_pos[1] = blay[1] + self.image_size-1
                    self.jump_direction[1] = True
            """
            if blay[1] <= rightup_y <= blay[1] + self.image_size or blay[1] <= rightdown_y <= blay[1] + self.image_size:
                if blay[0] <= rightup_x <= blay[0] + self.image_size or blay[0] <= rightdown_x <= blay[0] + self.image_size:
                    self.player_pos[0] -= self.image_size/8
            if blay[1] <= leftup_y <= blay[1] + self.image_size or blay[1] <= leftdown_y <= blay[1] + self.image_size:
                if blay[0] <= leftup_x <= blay[0] + self.image_size or blay[0] <= leftdown_x <= blay[0] + self.image_size:
                    self.player_pos[0] += self.image_size/8"""
        '''

    def role(self):
        """ 创建人物"""
        if 400 <= self.close_eye <= 415:
            road = pygame.transform.scale(self.character_ce, (self.image_size, self.image_size))
            if self.close_eye >= 415:
                self.close_eye = 0
        else:
            road = pygame.transform.scale(self.character, (self.image_size, self.image_size))
        self.screen.blit(road.convert_alpha(), (self.player_pos[0], self.player_pos[1]))
        self.cr_size = road.get_rect()
        self.close_eye += 1

    def apply_physics(self):
        """ 应用物理效果"""
        # 应用重力
        self.velocity_y += self.gravity
        self.player_pos[1] += self.velocity_y

        # 地面检测
        self.on_ground = False
        new_pos = self.player_pos[1] + self.velocity_y
        if self.check_collision(self.player_pos[0], new_pos, "vertical"):
            if self.velocity_y > 0:  # 下落碰撞
                self.on_ground = True
                self.velocity_y = 0
            elif self.velocity_y < 0:  # 头顶碰撞
                self.velocity_y = 0

    def key(self):
        """ 人物事件"""
        '''
        keys_pressed = pygame.key.get_pressed()  # 键盘事件

        if keys_pressed[pygame.K_w]:
            if not self.jump_direction[1]:
                self.player_pos[1] -= self.image_size/8
            self.jump_direction[0] = False
        if keys_pressed[pygame.K_s]:
            if not self.jump_direction[0]:
                self.player_pos[1] += self.image_size/8
            self.jump_direction[1] = False

        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_SPACE]:
            self.player_pos[1] -= self.speed_jump
            if self.speed_jump > 0:
                self.speed_jump -= self.image_size/50
        if keys_pressed[pygame.K_a]:
            self.player_pos[0] -= self.image_size/8
        elif keys_pressed[pygame.K_d]:
            self.player_pos[0] += self.image_size/8
        '''

        keys = pygame.key.get_pressed()

        # 水平移动（考虑碰撞）
        if keys[pygame.K_a]:
            if keys[pygame.K_LCTRL]:
                new_pos = self.player_pos[0] - self.move_speed_l
            else:
                new_pos = self.player_pos[0] - self.move_speed_m
            if not self.check_collision(new_pos, self.player_pos[1], "horizontal"):
                self.player_pos[0] = new_pos

        elif keys[pygame.K_d]:
            if keys[pygame.K_LCTRL]:
                new_pos = self.player_pos[0] + self.move_speed_l
            else:
                new_pos = self.player_pos[0] + self.move_speed_m
            if not self.check_collision(new_pos, self.player_pos[1], "horizontal"):
                self.player_pos[0] = new_pos

        # 跳跃（仅在地面时允许）
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False

        # 应用物理效果
        self.apply_physics()

    def check_collision(self, x, y, direction):
        """预测碰撞"""
        test_rect = pygame.Rect(x, y, self.image_size, self.image_size)
        #pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.image_size, self.image_size))

        for i, block_rect in enumerate(self.Get_into_world.img_size):
            rect = pygame.Rect(
                self.Get_into_world.img_xy[i][0],
                self.Get_into_world.img_xy[i][1],
                self.image_size,
                self.image_size
            )

            if test_rect.colliderect(rect):
                # 垂直碰撞处理
                if direction == "vertical":
                    if self.velocity_y > 0:  # 下落碰撞
                        self.player_pos[1] = rect.top - self.image_size
                    elif self.velocity_y < 0:  # 头顶碰撞
                        self.player_pos[1] = rect.bottom
                    return True

                # 水平碰撞处理
                elif direction == "horizontal":
                    if test_rect.left < rect.left:
                        self.player_pos[0] = rect.left - self.image_size
                    else:
                        self.player_pos[0] = rect.right
                    return True

                # 特殊处理可穿越方块（如梯子）
                if self.Get_into_world.block_image[i] != "ladder":
                    return True

        return False

class Window_xyz(Character):
    """ 定义可视窗类"""
    def move_xyz(self):
        """ 移动可视窗（坐标轴）"""
        if self.window_track_pos[0]:
            # 把所有物体的坐标加一格像素并添加到这个列表
            block_poe = []
            for block_xy in self.Get_into_world.block_list:
                block_poe.append([block_xy[0], block_xy[1] + self.image_size])
            self.Get_into_world.start_moving(block_poe)  # 调用后所有物体移动一格
            # 记录当前坐标
            self.Get_into_world.ctcs_y += 1

            self.player_pos[1] = self.player_pos[1] + self.image_size

        elif self.window_track_pos[1]:
            block_poe = []
            for block_xy in self.Get_into_world.block_list:
                    block_poe.append([block_xy[0], block_xy[1] - self.image_size])
            self.Get_into_world.start_moving(block_poe)
            self.Get_into_world.ctcs_y -= 1

            self.player_pos[1] = self.player_pos[1] - self.image_size

        if self.window_track_pos[2]:
            block_poe = []
            for block_xy in self.Get_into_world.block_list:
                block_poe.append([block_xy[0] + self.image_size, block_xy[1]])

            self.Get_into_world.start_moving(block_poe)
            self.Get_into_world.ctcs_x -= 1

            self.player_pos[0] = self.player_pos[0] + self.image_size

        elif self.window_track_pos[3]:
            block_poe = []
            for block_xy in self.Get_into_world.block_list:
                block_poe.append([block_xy[0] - self.image_size, block_xy[1]])
            self.Get_into_world.start_moving(block_poe)
            self.Get_into_world.ctcs_x += 1

            self.player_pos[0] = self.player_pos[0] - self.image_size

        self.role()
        if self.Load_call_world.table_open:
            self.Load_call_world.table()

    def track(self):
        """ 跟踪人物"""
        wx, wy = self.window_size
        fx, fy = int(wx / self.image_size), int(wy / self.image_size)
        if True in self.window_track_pos:
            pass
        else:
            if self.player_pos[0] > wx/2+wx/4:
                self.window_track_pos[3] = True
                self.move_form = int(fx/4)
            elif self.player_pos[0] < wx/4:
                self.window_track_pos[2] = True
                self.move_form = int(fx/4)
            if self.player_pos[1] > wy/2+wy/4:
                self.window_track_pos[1] = True
                self.move_fly = int(fy/4)
            elif self.player_pos[1] < wy/4:
                self.window_track_pos[0] = True
                self.move_fly = int(fy/4)

        if True in self.window_track_pos:
            self.move_xyz()
            if self.move_form == 0:
                self.window_track_pos[3] = False
                self.window_track_pos[2] = False
            else:
                self.move_form -= 1
            if self.move_fly == 0:
                self.window_track_pos[1] = False
                self.window_track_pos[0] = False
            else:
                self.move_fly -= 1

class Open_Character(Window_xyz):
    """ 定义一个召唤人物类"""
    def __init__(self):
        super().__init__()

    def compare_order(self, Communication, Get_into_world, Object_paper, WINDOW_SIZE):
        """ 匹配指令"""
        self.Communication = Communication
        self.Get_into_world = Get_into_world
        self.Object_paper = Object_paper
        self.window_size = WINDOW_SIZE
        try:
            if self.Communication.order_data[-1][0] == '/':
                try:
                    for order, text in self.order_all.items():
                        if order.split(' ')[0] == self.Communication.order_data[-1].split(' ')[0] and \
                             self.Communication.order_data[-1].split(' ')[0] == '/character':
                            if len(self.Communication.order_data[-1].split(' ')) == 4 and \
                                self.Communication.order_data[-1].split(' ')[1] == 'on':
                                self.pip_on(text)
                            elif len(self.Communication.order_data[-1].split(' ')) == 2 and \
                                self.Communication.order_data[-1].split(' ')[-1] == 'off':
                                self.pip_off(text)
                            else:
                                self.Communication.screen_text_color.append((255, 0, 0))
                                data = '“' + self.Communication.order_data[-1] + '”' + '不是有效的命令！'
                                self.Communication.get_text.append(data)
                                self.Communication.information.append(data)
                        elif order.split(' ')[0] == self.Communication.order_data[-1].split(' ')[0] and \
                                self.Communication.order_data[-1].split(' ')[0] == '/character.g':
                            self.pip_g(text)
                        elif order.split(' ')[0] == self.Communication.order_data[-1].split(' ')[0] and \
                                self.Communication.order_data[-1].split(' ')[0] == '/character.j':
                            self.pip_j(text)
                        elif order.split(' ')[0] == self.Communication.order_data[-1].split(' ')[0] and \
                                self.Communication.order_data[-1].split(' ')[0] == '/character.m':
                            self.pip_m(text)
                        elif order.split(' ')[0] == self.Communication.order_data[-1].split(' ')[0] and \
                                self.Communication.order_data[-1].split(' ')[0] == '/character.l':
                            self.pip_l(text)
                except:
                    self.Communication.screen_text_color.append((255, 0, 0))
                    data = '“' + self.Communication.order_data[-1] + '”' + '不是有效的命令！'
                    self.Communication.get_text.append(data)
                    self.Communication.information.append(data)
        except:
            pass

    def pip_on(self, text):
        """ 匹配人物召唤"""
        cx, cy = self.Communication.order_data[-1].split(' ')[2], \
                 self.Communication.order_data[-1].split(' ')[3]
        rx, ry = (float(cx) - self.Get_into_world.ctcs_x) * self.Get_into_world.image_size, \
                 (-float(cy) + self.Get_into_world.ctcs_y) * self.Get_into_world.image_size
        wx, wy = self.window_size
        if 0 <= rx <= wx and 0 <= ry <= wy:
            self.Communication.screen_text_color.append((255, 0, 255))
            data = text.split(' ')
            data = data[0] + '召唤'
            self.Communication.get_text.append(data)
            self.Communication.information.append(data)
            self.order_on(rx, ry)
        else:
            text = '人物已超出可视窗！'
            self.Communication.screen_text_color.append((255, 0, 0))
            self.Communication.get_text.append(text)
            self.Communication.information.append(text)

    def pip_off(self, text):
        """ 匹配人物关闭"""
        self.Communication.screen_text_color.append((255, 0, 255))
        data = text.split(' ')
        data = data[0] + '关闭'
        self.Communication.get_text.append(data)
        self.Communication.information.append(data)
        self.order_off()

    def pip_g(self, text):
        """ 匹配人物重力加速度"""
        g = self.Communication.order_data[-1].split(' ')[1]
        try:
            gi = float(g)
            self.order_g(gi)
            self.Communication.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + g
            self.Communication.get_text.append(data)
        except:
            self.Communication.screen_text_color.append((255, 0, 0))
            data = '“' + self.Communication.order_data[-1] + '”' + '不是有效的命令！'
            self.Communication.get_text.append(data)
            self.Communication.information.append(data)


    def pip_j(self, text):
        """ 匹配人物跳跃初速度"""
        j = self.Communication.order_data[-1].split(' ')[1]
        try:
            ji = float(j)
            self.order_j(ji)
            self.Communication.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + j
            self.Communication.get_text.append(data)
        except:
            self.Communication.screen_text_color.append((255, 0, 0))
            data = '“' + self.Communication.order_data[-1] + '”' + '不是有效的命令！'
            self.Communication.get_text.append(data)
            self.Communication.information.append(data)

    def pip_m(self, text):
        """ 匹配正常行走速度"""
        m = self.Communication.order_data[-1].split(' ')[1]
        try:
            mi = float(m)
            self.order_m(mi)
            self.Communication.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + m
            self.Communication.get_text.append(data)
        except:
            self.Communication.screen_text_color.append((255, 0, 0))
            data = '“' + self.Communication.order_data[-1] + '”' + '不是有效的命令！'
            self.Communication.get_text.append(data)
            self.Communication.information.append(data)

    def pip_l(self, text):
        """ 匹配反常行走速度"""
        l = self.Communication.order_data[-1].split(' ')[1]
        try:
            li = float(l)
            self.order_l(li)
            self.Communication.screen_text_color.append((0, 255, 0))
            data = text.split(' ')
            data = data[0] + l
            self.Communication.get_text.append(data)
        except:
            self.Communication.screen_text_color.append((255, 0, 0))
            data = '“' + self.Communication.order_data[-1] + '”' + '不是有效的命令！'
            self.Communication.get_text.append(data)
            self.Communication.information.append(data)

    def order_on(self, rx, ry):
        """ 执行人物召唤"""
        self.player_pos = [rx, ry]
        self.character_open = True

    def order_off(self):
        """ 执行人物关闭"""
        self.character_open = False

    def order_g(self, g):
        """ 执行人物重力加速度"""
        self.gravity = g

    def order_j(self, j):
        """ 执行人物跳跃初速度"""
        self.jump_force = j

    def order_m(self, m):
        """ 匹配正常行走速度"""
        self.move_speed_m = m

    def order_l(self, l):
        """ 匹配反常行走速度"""
        self.move_speed_l = l

    def beyond(self):
        """ 检测人物是否超出可视窗"""
        wx, wy = self.window_size
        if 0 <= self.player_pos[0] <= wx and 0 <= self.player_pos[1] <= wy:
            pass
        else:
            self.Communication.screen_text_color.append((255, 0, 0))
            data = '人物已超出可视窗！'
            self.Communication.get_text.append(data)
            self.Communication.information.append(data)
            self.order_off()

    def see_text(self):
        """ 显示人物属性"""
        self.FONT_XY.render_to(self.screen, (10, 50), '人物属性：重力加速度g=' + str(self.gravity) +
                               '；跳跃初速度j=' + str(self.jump_force),
                          (255-self.CA, 255-self.CB, 255-self.CC), size=15)
        self.FONT_XY.render_to(self.screen, (10, 70), ' '*9 + '正常行走速度M=' + str(self.move_speed_m) +
                               '；反常行走速度L=' + str(self.move_speed_l),
                               (255 - self.CA, 255 - self.CB, 255 - self.CC), size=15)

    def start(self):
        """ 执行人物所有设置"""
        self.role()
        self.apply_physics()
        self.block_xy()
        if not self.Communication.compen and not self.Object_paper.openife:
            self.key()
        self.track()
        self.beyond()
        if self.character_open and self.Load_call_world.read_font_open:
            self.see_text()

