# -*- coding: utf-8 -*-

import CentreParag
import word_freq
import word_ord

# 本函数用于显示判断审判结果（是或否）
def result_judge(num):
    str1, str2 = CentreParag.split_parag(num)

    result_freq = word_freq.fenci(str2)
    result_ord = word_ord.fenci(str2)

    flag = -1
    for word in result_ord:
        if word == '不准' or word == '驳回':
            flag = 0
            break
        if word == '准许' or word == '准予':
            flag = 1
            break
    return flag

# 本函数用于显示分词结果（按词频／按词序）
def result_fenci(num):
    str1, str2 = CentreParag.split_parag(num)
    result_freq = word_freq.fenci(str2)
    result_ord = word_ord.fenci(str2)

    print ''
    print 'str2 : ' + str2
    print ''
    print u'str2的按词频分词结果：'
    word_freq.print_fenci(result_freq, 10)
    print ''
    print u'str2的按词序分词结果：'
    word_ord.print_fenci(result_ord)
    print ''