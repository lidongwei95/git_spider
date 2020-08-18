#coding:utf-8
# 带有logo的二维码
from PIL import Image
import qrcode


def make_code(test,image,name):
    qr = qrcode.QRCode(version=5,
		error_correction=qrcode.ERROR_CORRECT_H, 
		box_size=10, 
		border=3, 
		image_factory=None, 
		mask_pattern=None
		)
	qr.add_data(text)
	qr.make(fit=True)

	img = qr.make_image()
	img = img.convert('RGBA')

	icon = Image.open(image)

	img_w, img_h = img.size
	factor = 4
	size_w = int(img_w / factor)
	size_h = int(img_h / factor)

	icon_w,icon_h = icon.size
	if icon_w > size_w:
		icon_w = size_w
	if icon_h > size_h:
		icon_h = size_h
	icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

	w = int((img_w - icon_w) / 2)
	h = int((img_h - icon_h) / 2)
	img.paste(icon, (w, h), icon)
	img.show()
	img.save(name + '.png')


if __name__ == '__main__':
	text = raw_input("输入想要做成二维码的话：")
	image = raw_input("logo文件名：")
	name = raw_input("输入保存名：")
	make_code(text,image,name)
