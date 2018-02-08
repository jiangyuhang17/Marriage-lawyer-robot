# -*- coding: utf-8 -*-

import xlrd
import numpy as np
import group
import rule as ru

xlsfile = r'table.xlsx'
book = xlrd.open_workbook(xlsfile) # 获得excel的book对象
sheet = book.sheet_by_index(0) # 通过sheet索引获得sheet对象


list = []
print u'您有如下情况吗：（存在输入1，不存在输入0）'
for i in range(1, sheet.nrows):
    print str(i) + ':' + sheet.cell_value(i, 4),
    while 1:
        a = input()
        if a ==1 or a==0:
            list.append(a)
            break
        else:
            print u'请重新输入'

array_question = np.array(list)
#print array_question

# 对提问进行预处理，将文章进行相关性排序
# array_total：[表示情况的向量，表示结果的0或1，与提问之间的误差，文章编号]
def yuchuli(array_question):
    array_total = []
    array_condition = group.array_condition
    array_result = group.array_result
    for i in range(0, len(array_condition)):
        sum = 0
        array_minus = array_question - array_condition[i]
        for j in array_minus:
            sum += abs(j)
        array_total.append((array_condition[i], array_result[i], sum, i))
    array_total.sort(key = lambda x: x[2], reverse = False) # 将文章按照编号从小到大排序
    return array_total

# 计算预计胜诉率
# num_article：要用最近的几篇文章计算胜诉率
def shengsulv(array_total, num_article):
    percent = 0
    yes = 0
    no = 0
    for i in range(0, num_article):
        if array_total[i][1] == 1:
            yes += 1
    percent = yes * 100 / num_article
    return percent

array_total = yuchuli(array_question)
# 计算胜诉率
percent = shengsulv(array_total, 5)
# 找出相关案例
article = []
for i in range(0, 3):
    article.append(array_total[i][3])
# 找出相关法律根据
rule = []
for x in ru.rule_for_user(array_question):
    rule.append(x)

print u'\n预计胜诉率为：' + str(percent) + '%'
print u'\n相关案例：'
for item in article:
    print item
print u'\n法律根据：'
for item in rule:
    print item