#coding:utf-8
# 带有logo的二维码
from PIL import Image
import qrcode
from MyQR import myqr


def make_code(data, filename):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    
    qr.make(fit=True)
    img = qr.make_image()
    img.save(filename)
    img.show()


def logo_code(data, img, filename):
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
    
    icon = Image.open(image).convert('RGBA')
    
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
    img.save(name)


def bg_pic_code(data, img, filename):
    myqr.run(
        words = data, # 扫描二维码后，显示的内容，或是跳转的链接
        version = 5,# 设置容错率
        level = 'H',# 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        picture = './gif_baidu.gif',# 图片所在目录，可以是动图
        colorized = True, # 黑白(False)还是彩色(True)
        contrast = 1.0, # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
        brightness = 1.0, # 用来调节图片的亮度，用法同上。
        save_name = 'Python.gif' # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )


if __name__ == '__main__':
    data = input("输dd入想要做成二维码的话：")
    img = input("logo文件名：")
    filename = input("输入保存名：")
    make_code(data, img, filename)
