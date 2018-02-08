# -*- coding: utf-8 -*-

import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")

num = 1

# 本函数传入文件路径，得到‘本院认为’到‘审判员XXX’之间的内容
def centre_parag(num):
    file = open('article/article' + str(num) + '.txt')
    cenparas = ''
    isbengin = False

    lines = file.readlines()
    for x in lines:
        x = x.strip().decode('gbk', 'utf-8') # 处理前进行相关的处理，包括转换成Unicode等

        if isbengin:
            if x[0] != '审':
                cenparas += x
                # print x # 可注释掉
            else:
                break
        else:
            if x[:4] == '本院认为':
                cenparas += x
                # print x # 可注释掉
                isbengin = True
    return cenparas

# 本函数传入一段文字，得到‘本院认为’和‘判决如下’的具体内容
def split_parag(num):
    cenparas = centre_parag(num)

    cenparas = cenparas.replace('：', '，')
    cenparas = cenparas.replace('；', '。')

    str1 = ''
    str2 = ''

    flag = False
    sentences = cenparas.split('。')
    for sentence in sentences:
        sentences_short = sentence.split('，')
        for sentence_short in sentences_short:
            if sentence_short == '判决如下' or sentence_short == '裁定如下':
                flag = True
        if flag:
            str2 += sentence + '。'
        else:
            str1 += sentence + '。'
    str2 = str2[:len(str2) - 1]

    return str1, str2