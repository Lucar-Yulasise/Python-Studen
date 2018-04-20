# 第三方模块
# pip install 三方库名
'''
安装pip：
windows 需要安装pip
Mac：不需要安装pip
Linux：不需要安装pip
'''

# 安装第三方模块文件：需要知道模块名字
# Pillow 图像处理的第三方库
# 安装语句： pip install Pillow   # cmd下运行

# 引入第三方库:前提是当前库文件要安装成功
import PIL
from PIL import Image
# 打开图片
im = Image.open("111.jpg")
print(im)
# 设置图片大小
im.thumbnail((200,200))
# 保存
im.save('2.png','JPEG')

im1 = Image.open("2.png")
print(im1)


# os date 栈 队列
# 面向对象



