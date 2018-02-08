# -*- coding: utf-8 -*-

import CentreParag
import word_freq
import word_ord
import condition1

# 本函数用于显示提取文案条件
def condition_judge(num):
    str1, str2 = CentreParag.split_parag(num)
    result_freq = word_freq.fenci(str1)
    result_ord = word_ord.fenci(str1)

    flag = []
    for i in range(0, condition1.nrows - 1):
        flag.append(0)

    # flag_temp是每一句话的特征向量，flag是整段文字的特征向量
    sentences = str1.split('，')
    for sentence in sentences:
        words = word_ord.fenci(sentence)
        flag_temp = condition1.get_det(words)
        for i in range(0, len(flag_temp)):
            if flag_temp[i] == 1:
                flag[i] = 1

    return flag

# 本函数用于显示分词结果（按词频／按词序）
def condition_fenci(num):
    str1, str2 = CentreParag.split_parag(num)
    result_freq = word_freq.fenci(str1)
    result_ord = word_ord.fenci(str1)

    print ''
    print 'str1 : ' + str1
    print ''
    print u'str1的按词频分词结果：'
    word_freq.print_fenci(result_freq, 10)
    print ''
    print u'str1的按词序分词结果：'
    word_ord.print_fenci(result_ord)
    print ''