# <div align="center">Minecraft 2D</div>

<p align="center">
 <img src="https://img.shields.io/badge/开发语言-Python-coral" alt="语言">
 <img src="https://img.shields.io/badge/核心库-Pygame-blue" alt="核心库">
</p>
 <div align="center">这是一款免费开源的2D沙盒游戏，玩家可以用方块搭建属于自己的世界</div>

## 详细信息

### 特点/功能
- 🧩玩家可以建造、破坏、修改游戏世界，使用游戏内的资源和工具进行创造。
- 🎮️自定义角色的属性，让角色可以行走和跳跃，用方块搭建2D跑酷游戏。
- 🪄自定义添加方块，添加其他的样式作为方块。
- 🎨物品栏及主物品栏，快速查找物品并选定物品。
- 🗒️聊天栏（输入一些指令，或在聊天栏上显示你输入的文字）。

### 兼容性
- 支持 Win8及以上 操作系统

## 如何使用

### 安装
1. 下载 [Releases](https://github.com/Minecows-Green/Minecraft-2D-for-LittleDream/releases) 中的安装程序,它是一个压缩包（···2D.zip）；
2. 解压文件，找到启动器`MC--2D--Launcher.exe`；
3. 双击启动程序。

### 如何使用源代码
1. 下载完源代码文件后解压缩，解压游戏根目录里的 **block.zip** （解压到当前文件夹）
2. 确保您的计算机已经安装了 **Python** 语言环境，如果未安装点击[Python下载](https://www.python.org/) 进行安装。
3. 确保安装了**pip**，如果未安装请参考[官方安装指南](https://pip.pypa.io/en/stable/installation/)进行安装。
4. 下载依赖库，打开**cmd**依次键入以下代码
 ```python
	 pip install pygame
	 pip install pygame.freetype
	 pip install pywin32
	 pip install wxPython
   ```

## 游戏操作

1. ### ==鼠标按键==

> *左键 --------------------- 填充一个物体*

> *滚轮 --------------------- 换物品（选定物品）*

> *右键 --------------------- 放置一个物体*

2. ### ==键盘按键==

> . *W ------------------------ 上移*

> . *S ------------------------ 下移*

> . *A ------------------------ 左移*

> . *D ------------------------ 右移*

> . *Ctrl + W ------------------------ 加速上移*

> . *Ctrl + S ------------------------ 加速下移*

> . *Ctrl + A ------------------------ 加速左移*

> . *Ctrl + D ------------------------ 加速右移*

> . *Shift ------------------------- 前进*

> . *空格 ------------------------- 后退*

> . *Esc ------------------------ 返回*

> . *按住Z键不放 + 鼠标移动 ------------------------- 连续填充物体*

> . *按住X键不放 + 鼠标移动 ------------------------- 连续放置物体*

> . *< ------------------------- 区块加载范围(+)*

> . *> ------------------------- 区块加载范围(-)*

> . *E ----------------------- 打开物品栏*

> *（搜索物品：输入物品代号后再按回车键就把选定的物品移到主物品栏里了）*

> . *Q ----------------------- 摧毁主物品栏的物品*

> . *T ----------------------- 打开聊天栏*

> . *主键盘的数字键（横排）1~9 ------------------------- 换物品（选定物品）*

> . *I ----------------------- 显示表格*

> . *O ---------------------- 隐藏显示信息*

> . *P ---------------------- 隐藏物品栏*

  

3. ### ==指令集（输入后按回车键）===

> *在聊天栏上显示输入的文字  直接输入  如：Hello World!*

> *传送自己 /tp @a 传送到坐标x y  如：/tp @a 114 514*

> *放置物体 /put 从x1 y1 到x2 y2 id=物品id  如：/put 1 9 8 1 id=0114*

> *填充物体 /fill 从x1 y1 到x2 y2  如：/fill 1 9 8 1*

> *填充指定物体 /fill 从x1 y1 到x2 y2 id=物品id  如：/fill 1 9 8 1 id=0114*

> *给予物品 /give @a id=物品id  如：/give @a id=0114*

>  *复制区块 /copy name=变量名 从x1 y1 到x2 y2  如：/copy name=area 1 9 8 1  注：_复制区块时最好放个方块在x1, y1，要不然粘贴时会错位_*

> *粘贴区块 /glue name=变量名 粘贴的位置x y  如：/glue name=area 4 5 7 3*

> *列出所有已复制区块的变量名 /list copy*

> *清除指定已复制区块的变量名 /del copy name=变量名  如：/del copy name=area*

> *清除所有已复制区块的变量名 /del copy*

> *更改当前世界时间 /time 时间 参数(0-默认，1-静止，2-向左流逝，3-向右流逝)  如：/time 100 1*

> *更改时间流逝速度 /time.speed 速度(1~999) 如：/time.speed 1*

> *主人物召唤 /character on 到坐标x y  如：/character on 6 2*

> *主人物关闭 /character off*

> *更改缩放比例 /scale.z 缩放比例  如：/scale.z 72*

> *设置人物重力加速度 /character.g 重力  如：/character.g  1.5*

> *设置人物跳跃初速度 /character.j 跳跃速度  如：/character.j -24*

> *设置正常行走速度 /character.m 行走速度  如：/character.m  10*

> *设置反常行走速度 /character.l 行走速度  如：/character.l  20*

4. ### ==block 文件夹下的三个子文件夹==

> *building --------- 建筑物品 文件夹*

> *circuit ---------- 红石物品 文件夹*

> *other ------------ 其他物品 文件夹*

5. ### ==自定义添加物品==

> *打开此游戏根目录的 block  下三个子文件夹的随机一个文件夹，*

> *找到 dic_block_image.dict  文件并用记事本打开，*

> *你会看到这样的一个字典里有一些键值对 --------- {‘xxx.png’: ['id', *number], ...}，

> *比如字典中的 'xxx.png' 这是字典中的一个键，['id', number] 这是字典*的一个值，

> *而他们两个是相对的就用一个符号“:”相隔开，这样就组成了一个键值*对（一个键对应一个值），

> *然而，要想添加物品就需要添加键值对到字典里，添加的过程就是：*

> *----------- {'物品图片路径+图片名+后缀': ['定义物品id',  定义物品音效0~5]}*

6. ### ==物品音效==

> *0 ------ 无声*

> *1 ------ 草的声音*

> *2 ------ 木头的声音*

> *3 ------ 沙子的声音*

> *4 ------ 玻璃的声音*

> *5 ------ 块的声音*
