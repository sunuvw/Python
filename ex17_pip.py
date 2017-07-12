# -*- coding: utf-8 -*-
# pip
#######################
# pip install Pillow 安装Pillow库PIL
from PIL import Image # 从PIL库导入Image模块
im = Image.open('ex17.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100)) # 图片缩略
im.save('ex17_thumb.jpg', 'JPEG') # 图片保存
# pip install mysql-connector

# 模块搜索路径
import sys
print(sys.path)
sys.path.append('C:\Users\scc\Python') # 添加路径到模块搜索目录