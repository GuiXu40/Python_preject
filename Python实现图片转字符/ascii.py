# -*- coding=utf-8 -*-

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file') # 输入文件
parser.add_argument('-o', '--output') # 输出文件
parser.add_argument('-width', type = int, default = 80) # 输出字符画宽
parser.add_argument('--height', type = int, default = 80) # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file  # 输入的图片文件路径
WIDTH = args.width # 输出字符画的宽度
HEIGHT = args.height # 输出字符画的高度
OUTPUT = args.output # 输出字符画的路径

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char (r, g, b, alpha = 256):
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

	unit = (256.0 + 1) / length
	return ascii_char[int(gray / unit)]

if __name__ == '__main__':
	# 打开病调整图片的宽和高
	im = Image.open(IMG)
	# Image.NEAREST表示输出低质量的图片
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

	txt = "" # 初始化输出的字符串

	# 遍历图片的每一行
	for i in range(HEIGHT):
		# 遍历改行中的每一列
		for j in range(WIDTH):
			# 将 (j, i)坐标的 RGB 像素转为字符后添加到 txt 字符串
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'
	# 输出到屏幕
	print(txt)

	# 字符画输出到文件
	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", "w") as f:
			f.write(txt)