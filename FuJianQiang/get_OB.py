"""
=========================
# @Time : 2020/8/20 下午3:35 
# @Author : ldw
# @File : get_OB
# @Software: PyCharm
===========================
"""
import math
import os

def get_info(angle_in, length_oa, length_ab):
    PI = math.pi
    if not angle_in[:-1].lstrip('0').replace('.', '').isdigit():
        print("请输入数字并以字母a（表示弧度）或字母b（表示度）结尾，退出！")
        os._exit(0)
    if not length_oa.lstrip('0').replace('.', '').isdigit():
        print("请输入数字，退出！")
        os._exit(0)
    else:
        length_oa = float(length_oa)
    if not length_ab.lstrip('0').replace('.', '').isdigit():
        print("请输入数字，退出！")
        os._exit(0)
    else:
        length_ab = float(length_ab)
    if angle_in[-1] == 'a':
        angle = float(angle_in[:-1])
    elif angle_in[-1] == 'b':
        angle = PI / 180 * float(angle_in[:-1])
        # print('angle:%s' % angle)
    else:
        print("输入格式有误!!!\n请输入数字并以字母a（表示弧度）或字母b（表示度）结尾，退出！")
        os._exit(0)
    if length_ab < length_oa * math.sin(angle):
        print("错误: 数据输入有误，请检查后重新输入，退出")
        os._exit(0)
    oaa = length_oa * math.cos(angle)  # 弧度
    # print('oaa:%s'% oaa)
    abb = ((length_ab ** 2) - (length_oa * math.sin(angle)) ** 2) ** 0.5
    # print('abb:%s'% abb)
    length_ob = oaa + abb
    print("length_ob: %s" % length_ob)

if __name__ == "__main__":
    angle_in = input("输入角度（弧度a/度b）：")
    length_oa = (input("输入oa长度："))
    length_ab = (input("输入ab长度："))
    get_info(angle_in, length_oa, length_ab)
